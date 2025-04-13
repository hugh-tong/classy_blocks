import os

import classy_blocks as cb

mesh = cb.Mesh()

base_palne_length = 41
num_of_stick = 41
len_of_single_box = base_palne_length / num_of_stick
depth_of_stick = 2


for i in range(num_of_stick):
    if i % 2 == 0:
        box = cb.Box([len_of_single_box * i, 0, 0], [len_of_single_box * (i + 1), base_palne_length, depth_of_stick])
    else:
        box = cb.Box([len_of_single_box * i, 0, 0], [len_of_single_box * (i + 1), base_palne_length, depth_of_stick / 2.0])

    box.chop(0, count=1)
    box.chop(1, count=10)
    if i % 2 == 0:
        box.chop(2, count=2)
    else:
        box.chop(2, count=1)
    if i == 0:
        box.set_patch("left", "perimeter")
        box.set_patch("right", f"box_slave{i}")
    elif i == (num_of_stick - 1):
        box.set_patch("left", f"box_master{i - 1}")
        box.set_patch("right", "perimeter")
    else:    
        box.set_patch("left", f"box_master{i - 1}")
        box.set_patch("right", f"box_slave{i}")
    
    box.set_patch("bottom", "interface")
    mesh.add(box)

for i in range(num_of_stick):
    if  i ==  (num_of_stick - 1):  
        break  
    mesh.merge_patches( f"box_master{i}",  f"box_slave{i}")

box = cb.Box([0, 0, -1], [base_palne_length, base_palne_length, 0])
box.chop(0, count=base_palne_length)
box.chop(1, count=base_palne_length)
box.chop(2, count=1)
box.set_patch("top", "interface_down")
box.set_patch("right", "perimeter")
box.set_patch("left", "perimeter")
box.set_patch("bottom", "lower_down")
mesh.add(box)
mesh.merge_patches("interface", "interface_down")


mesh.set_default_patch("walls", "wall")
mesh.write(os.path.join("..", "case", "system", "blockMeshDict"))
