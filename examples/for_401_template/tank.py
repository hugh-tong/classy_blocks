import os
import json
import classy_blocks as cb

with open ('../../geo_data/tank.json', 'r') as f:
    data = json.load(f)

# a cylindrical tank with round end caps
diameter = data['sph_radius']
length   = data['ref_length']  # including end caps
cell_size= data['cell_size']

mesh = cb.Mesh()

cylinder = cb.Cylinder([0, 0, 0], [length, 0, 0], [0, diameter / 2, 0])

wall_name = "tank_wall"

cylinder.set_outer_patch(wall_name)

start_cap = cb.Hemisphere.chain(cylinder, start_face=True)
start_cap.set_outer_patch(wall_name)

end_cap = cb.Hemisphere.chain(cylinder, start_face=False)
end_cap.set_outer_patch(wall_name)

mesh.add(cylinder)
mesh.add(start_cap)
mesh.add(end_cap)

grader = cb.SimpleGrader(mesh, cell_size)
grader.grade()

mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
