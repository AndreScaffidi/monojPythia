#############################
# Python script to loop over
# scan parameters
#############################
import os
import sys
import numpy as np
#############################
# Define parameter ranges
MASS         = np.linspace(150,1000,15)
THETA        = np.linspace(0,np.pi,15)    
nevents      = 500000  
DIR          = {1:'C62_C63', 2: 'C61_C64'}
O1           = str('C61')
O2           = str('C64')
dir_         = str(DIR[2]) 
#############################
# Function to check if file exists 
def exists(mas,theta):
    atlas = os.path.exists("%s/MONO_JET_%1.2F_%1.2F/Events/run_01/NUMBER_OF_M_JETS.csv" %(dir_,m,th))
    cms   = os.path.exists("%s/MONO_JET_%1.2F_%1.2F/Events/run_01/NUMBER_OF_M_JETS_CMS.csv" %(dir_,m,th))
    return atlas,cms

for m in MASS:
    for th in THETA:
            exist_ = exists(m,th)
            if exist_[0] and exist_[1]:
#                print "Both files exist!"
                continue 
            else:
                # if m==1000: ############### Get rid of this line if not debugging!!
                #     # continue
                #     os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))

                # else: 
                    # continue
                print "Submitting", m,th
                    # os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))

