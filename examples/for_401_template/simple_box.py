import os
import json
import classy_blocks as cb
from classy_blocks.optimize.clamps.free import FreeClamp
from classy_blocks.optimize.optimizer import MeshOptimizer

mesh = cb.Mesh()

with open ('../../geo_data/box.json', 'r') as f:
    data = json.load(f)

x_len = data['x_len']
y_len = data['y_len']
z_len = data['z_len']
x_cells_num = data['x_cells_num']
y_cells_num = data['y_cells_num']
z_cells_num = data['z_cells_num']
default_patch_name = data['default_patch_name']
default_patch_type = data['default_patch_type']

# generate a cube, consisting of 2x2x2 smaller cubes
# for x in (-1, 0):
#     for y in (-1, 0):
#         for z in (-1, 0):
#             box = cb.Box([x, y, z], [x + x_len - 1, y + y_len - 1, z + z_len - 1])

#             # for axis in range(3):
#             #     print(f"Chopping box along axis {axis}")
#             #     box.chop(axis, count=10)

#             # Chop box along the x-axis (axis 0)  
#             box.chop(0, count=x_cells_num)  

#             # Chop box along the y-axis (axis 1)  
#             box.chop(1, count=y_cells_num)  

#             # Chop box along the z-axis (axis 2)  
#             box.chop(2, count=z_cells_num)
#             mesh.add(box)


box = cb.Box([-1, -1, -1], [-1 + x_len - 1, -1 + y_len - 1, -1 + z_len - 1])

# for axis in range(3):
#     print(f"Chopping box along axis {axis}")
#     box.chop(axis, count=10)

# Chop box along the x-axis (axis 0)  
box.chop(0, count=x_cells_num)  

# Chop box along the y-axis (axis 1)  
box.chop(1, count=y_cells_num)  

# Chop box along the z-axis (axis 2)  
box.chop(2, count=z_cells_num)
mesh.add(box)



mesh.set_default_patch(default_patch_name, default_patch_type)
mesh.assemble()

# # move the middle vertex to a sub-optimal position
# finder = cb.GeometricFinder(mesh)
# mid_vertex = list(finder.find_in_sphere([0, 0, 0]))[0]
# mid_vertex.translate([0.6, 0.6, 0.6])

# # find a better spot for the above point using automatic optimization
# optimizer = MeshOptimizer(mesh)

# # define which vertices can move during optimization, and in which DoF
# mid_clamp = FreeClamp(mid_vertex.position)
# optimizer.add_clamp(mid_clamp)


# optimizer.optimize()

mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
