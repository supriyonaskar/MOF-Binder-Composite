from __future__ import division
import math
import numpy as np
import random
import MDAnalysis as mda
import MDAnalysis.analysis.msd as msd
import matplotlib.pyplot as plt
from MDAnalysis import transformations as trans
import sys


u = mda.Universe('co2.pdb','traj.dcd')
#trans.unwrap(u.atoms)

MSD = msd.EinsteinMSD(u, select='name CO2 ', msd_type='xyz', fft=True)
MSDx = msd.EinsteinMSD(u, select='name CO2 ', msd_type='x', fft=True)
MSDy = msd.EinsteinMSD(u, select='name CO2 ', msd_type='y', fft=True)
MSDz = msd.EinsteinMSD(u, select='name CO2 ', msd_type='z', fft=True)



MSD.run()
MSDx.run()
MSDy.run()
MSDz.run()
nframes = MSD.n_frames
timestep = 1 # this needs to be the actual time between frames
x = np.arange(nframes)*timestep # make the lag-time axis
y = MSD.results.timeseries
y1 = MSDx.results.timeseries
y2 = MSDy.results.timeseries
y3 = MSDz.results.timeseries

f = open ('outfile.dat',"w+")
for i in range (len (y)):
    f.write("%f\t%f\t%f\t%f\t%f\n"%(x[i],y[i],y1[i],y2[i],y3[i]))
f.close()

