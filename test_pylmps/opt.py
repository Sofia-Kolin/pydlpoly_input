import pylmps

pl = pylmps.pylmps("mil88")
pl.setup(kspace=False, ff="file", bcond=3)

pl.MIN(0.1)

pl.write("mil88_opt.mfpx")

