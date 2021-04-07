#############################
# Script to go and read all results
# from madgraph output
#############################
import matplotlib
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.interpolate import Rbf
import itertools
import json
#############################
# Go to each folder subdiretroy
# Grid_size = 15
# MASS      = np.linspace(150,1000,Grid_size)
# THETA     = np.linspace(0,np.pi,Grid_size)   
# For low mas
Grid_size = 4
MASS      = np.linspace(1,150,Grid_size)
THETA     = np.linspace(0,np.pi,Grid_size)  
# For dim7
# Grid_size = 19    
# MASS      = np.linspace(1,1000,Grid_size)  
#############################
# Get data
FILES  = {"ATLAS":"NUMBER_OF_M_JETS","CMS":"NUMBER_OF_M_JETS_CMS"} 
DIR    = {1:'C62_C63_low', 2: 'C61_C64_low' }
DIR_7  = {3: 'C71', 4:'C72',5:'C73', 6:'C74'}
for group,name in DIR.items():
    print ("For opperator combination %s..." %(name))
    for experiment, file in FILES.items():
        for m in MASS:  
            for th in THETA:
                if group==1:
                    Path = '%s/MONO_JET_%1.2F_%1.2F/Events/run_01/%s.csv' %(name,m,th,file)
                elif group ==2:
                    Path = '%s/MONO_JET_%1.2F_%1.2F/Events/run_01/%s.csv' %(name,m,th,file)    
                if os.path.exists(Path):
                    # Do not include nans ************ just remove points
                    os.system('cp %s /fast/users/a1607156/MG5_ROOT/%s_DATA_ONLY/%s_%1.2F_%1.2F.csv' %(Path,name,file,m,th))
                    continue
                # else:
                #     print ("Uncompleted run! mass = %1.2F, th = %1.2F" %(m,th) )
                continue

# for group,name in DIR_7.items():
#     print ("For opperator combination %s..." %(name))
#     for experiment, file in FILES.items():
#         for m in MASS:  
#                 Path = '%s/MONO_JET_%s_%1.2F/Events/run_01/%s.csv' %(name,name,m,file)     
#                 if os.path.exists(Path):
#                     # Do not include nans ************ just remove points
#                     os.system('cp %s /fast/users/a1607156/MG5_ROOT/%s_DATA_ONLY/%s_%1.2F.csv' %(Path,name,file,m))
#                     continue
#                 else:
#                     print ("Uncompleted run! mass = %1.2F, th = %1.2F" %(m,th) )
#                 continue