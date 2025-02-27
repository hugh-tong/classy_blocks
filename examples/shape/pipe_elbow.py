import os

import numpy as np

import classy_blocks as cb

###### 文献中的参数 ######
# CASE 2, De = 423

Re = 1000
R0 = 5.7
De = 423
dt = 3.95e-3

rt = dt / 2.0
Rb = R0 * rt
print("Tube radius = {}".format(rt))
print("Rb = {}".format(Rb)) # 文献中的Rb貌似是错误的？

rho_particle = 895
# dia_particle = 20e-6  # 5-20 um
dia_particle = 5e-6  # 5-20 um
mu_fluid = 1.85e-5
spec_velo = 3.86 # m/s
spec_lenth = dt

stokes_num = rho_particle * dia_particle**2 * spec_velo  / ( 18.0 * mu_fluid * spec_lenth) 
print("Stokes number = {}".format(stokes_num))

num_particle = 1100
m1 = num_particle * dia_particle
print("Moment.1 = {}".format(m1))
######

pipe_radius = rt
muffler_radius = Rb
ref_length =  dt


cell_size = 0.000063

shapes = []
# 1
shapes.append(cb.Cylinder([0, 0, 0], [ref_length, 0, 0], [0,pipe_radius,0]))
shapes[-1].chop_axial(start_size=cell_size)
shapes[-1].chop_radial(start_size=cell_size)
shapes[-1].chop_tangential(start_size=cell_size)
shapes[-1].set_start_patch("inlet")

 
# 2
# elbow_center = shapes[-1].sketch_2.center + np.array([0, 2 * muffler_radius, 0])
elbow_center = shapes[-1].sketch_2.center + np.array([0, muffler_radius, 0])
shapes.append(
    cb.Elbow.chain(shapes[-1], np.pi / 2, elbow_center, [0, 0, 1], pipe_radius)
)

shapes[-1].chop_axial(start_size=cell_size)


# 3
shapes.append(cb.Cylinder.chain(shapes[-1], 2.0 * ref_length))
shapes[-1].chop_axial(start_size=cell_size)

shapes[-1].set_end_patch("outlet")
 
# add everything to mesh
mesh = cb.Mesh()
for shape in shapes:
    mesh.add(shape)
 
mesh.set_default_patch("walls", "wall")
 
mesh.write(os.path.join("..", "case", "system", "blockMeshDict"), debug_path="debug.vtk")
