import pydlpoly

# initiattion
pd = pydlpoly.pydlpoly("Fe_Cl_op_opt_3_3_3")

# to set up the system

pd.setup(key="system.key_ref", control="system.control", bcond=3, pdlp_restart='Fe_Cl_op_opt_3_3_3/Fe_Cl_op_opt_3_3_3.pdlp', restart=True, read_stage='equi2')

#minimization
#pd.write_tinker_xyz("init.xyz")


#pd.MIN_lbfgs(0.1)
#pd.write_xyz("min.xyz")
#pd.write_tinker_xyz("min.xyz")

#lattice minimization
#pd.LATMIN_sd(0.1, 0.1)
#write the minimized struture
#pd.write_txyz("lastmin.xyz")
#pd.write_tinker_xyz("lastmin.xyz")


pd.MD_init("equi0", ensemble="nve", T=300.0, traj=["xyz", "vel","cell"], rnstep=10)
pd.MD_run(50000)
pd.write_tinker_xyz("equi.xyz")


pd.MD_init("equi2", ensemble="nvt", T=300.0 , thermo="hoover", relax=[0.1], traj=["xyz", "vel","cell"], startup=True)
pd.MD_run(100000)
pd.write_tinker_xyz("MD_equi.xyz")


pd.MD_init("nst", ensemble="nst", T=300.0, p=0.001, thermo="hoover", relax=[0.1,1.0], traj=["xyz", "vel","cell"])
pd.MD_run(500000)
pd.write_tinker_xyz("MD_nst.xyz")

pd.MD_init("prod", ensemble="nve", T=300.0, traj=["xyz", "vel","cell"])
pd.MD_run(4000000)
pd.write_tinker_xyz("prod.xyz")
