#############################
# Python script to delete
# hepcmc files
#############################
import os
import sys
import numpy as np
from multiprocessing import Pool
#############################
# Define parameter ranges
MASS         = np.linspace(150,1000,20)
THETA        = np.linspace(0,np.pi,20)    
#############################
def run(m):
    for th in THETA:
        print " In directory %1.2F, %1.2F" %(m,th)
        os.system('rm MONO_JET_%1.2F_%1.2F/Events/run_01/tag_1_pythia8_events.hepmc' %(m,th))
Pool(16).map(run,MASS)