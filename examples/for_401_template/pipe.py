import os
import json
import numpy as np

import classy_blocks as cb

with open ('../../geo_data/pipe.json', 'r') as f:
    data = json.load(f)


pipe_radius = data['pipe_radius']
ref_length =  data['ref_length']

print("Pass para to classy_block, pipe_radius = {}".format(pipe_radius))
print("Pass para to classy_block, ref_length = {}".format(ref_length))

# cell_size = 0.000063
cell_size = data['cell_size']
# NOTE: cell_size relate to mesh number:
# 0.000063 -> 1458660
# 0.00063  -> 2820
# 0.0005   -> 3480
# 0.00005  -> 2975400
# 0.0001   -> 393300
# 0.00008  -> 719712
print("Pass para to classy_block, cell_size = {}".format(cell_size))

shapes = []
# 1
shapes.append(cb.Cylinder([0, 0, 0], [ref_length, 0, 0], [0,pipe_radius,0]))
shapes[-1].chop_axial(start_size=cell_size)
shapes[-1].chop_radial(start_size=cell_size)
shapes[-1].chop_tangential(start_size=cell_size)
shapes[-1].set_start_patch("inlet")

# shapes.append(cb.Cylinder.chain(shapes[-1], 2.0 * ref_length))
# shapes[-1].chop_axial(start_size=cell_size)
shapes[-1].set_end_patch("outlet")

mesh = cb.Mesh()
for shape in shapes:
    mesh.add(shape)

mesh.set_default_patch("walls", "wall")

mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
