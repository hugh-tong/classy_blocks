import os

import classy_blocks as cb

mesh = cb.Mesh()

base_palne_length = 1.8
num_of_cell = 500
lower_plane_depth = 0.001
upper_plane_depth = 0.0001

depth_of_stick = 2

lower_box = cb.Box([0, 0, 0], [base_palne_length, base_palne_length, lower_plane_depth])
lower_box.chop(0, count=num_of_cell)
lower_box.chop(1, count=num_of_cell)
lower_box.chop(2, count=1)
lower_box.set_patch("top"   , "top_slave")
lower_box.set_patch("bottom", "lower_bottom")
lower_box.set_patch("left"  , "perimeter")
lower_box.set_patch("right" , "perimeter")
lower_box.set_patch("front" , "perimeter")
lower_box.set_patch("back"  , "perimeter")
mesh.add(lower_box)

upper_box = cb.Box([0, 0, lower_plane_depth], [base_palne_length, base_palne_length, lower_plane_depth + upper_plane_depth])
upper_box.chop(0, count=num_of_cell)
upper_box.chop(1, count=num_of_cell)
upper_box.chop(2, count=1)
upper_box.set_patch("top"   , "upper_top")
upper_box.set_patch("bottom", "bottom_master")
upper_box.set_patch("left"  , "perimeter")
upper_box.set_patch("right" , "perimeter")
upper_box.set_patch("front" , "perimeter")
upper_box.set_patch("back"  , "perimeter")
mesh.add(upper_box)

mesh.merge_patches("lower_bottom", "top_slave")
mesh.set_default_patch("walls", "wall")
mesh.write(os.path.join("..", "case", "system", "blockMeshDict"))
