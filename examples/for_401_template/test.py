import os

import numpy as np

import classy_blocks as cb

mesh = cb.Mesh()


# base_points = [
    # [0, 0, 0],
    # [1, 0, 0],
    # [1, 1, 0],
    # [0, 1, 0]
# ]

base_points = np.array([
    [0, 0, 0], 
    [1, 0, 0], 
    [1, 1, 0], 
    [0, 1, 0]
    ])

base_face = cb.Face(base_points)
extruded_block = cb.Extrude(base_face, 3)

extruded_block.set_patch('top', 'atmosphere')
extruded_block.set_patch('bottom', 'floor')
extruded_block.set_patch(['left', 'right', 'front', 'back'], 'sides')


extruded_block.chop(0, count=10)
extruded_block.chop(1, count=10)
extruded_block.chop(2, start_size=0.01, c2c_expansion = 1.1)

mesh.add(extruded_block)
mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
