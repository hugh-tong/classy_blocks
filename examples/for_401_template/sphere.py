import os
import json
import classy_blocks as cb

with open ('../../geo_data/sphere.json', 'r') as f:
    data = json.load(f)

mesh = cb.Mesh()

sph_radius = data['sph_radius']
box_len = sph_radius / 3.0 # pipe radius / 3

default_patch_name = data['default_patch_name']
default_patch_type = data['default_patch_type']
out_block_cell_num = data['out_block_cell_num']
in_block_cell_num  = data['in_block_cell_num']
# Create a 7-block sphere by offsetting a box's faces.
box = cb.Box([-box_len, -box_len, -box_len], [box_len,box_len, box_len])

for i in range(3):
    box.chop(i, count=in_block_cell_num)
mesh.add(box)

# faces must point 'out' of the original block or
# newly created blocks will be inside-out;
offset_faces = [box.get_face(orient) for orient in ("bottom", "top", "left", "right", "front", "back")]
for i in (0, 2, 4):
    offset_faces[i].invert()

shell = cb.Shell(offset_faces, box_len)
shell.chop(count=out_block_cell_num)

for operation in shell.operations:
    operation.project_side("top", "sphere", edges=True, points=True)

mesh.add(shell)

# 字典初始化  
my_dict = {  
    "sphere": [  
        "type searchableSphere",  
        "centre (0 0 0)",  
        f"radius {sph_radius}",  
    ]  
}    
mesh.add_geometry(my_dict)
# mesh.add_geometry(
    # {
    #     "sphere": [
    #         "type searchableSphere",
    #         "centre (0 0 0)",
    #         "radius 3.0",
    #     ]
    # }
# )
mesh.set_default_patch(default_patch_name, default_patch_type)
mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
