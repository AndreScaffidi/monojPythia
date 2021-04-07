#############################
# Python script to loop over
# scan parameters
#############################
import os
import sys 
import numpy as np
#############################
# Dim-6 opperators
# Grid_size    = 4
# MASS         = np.linspace(1,150,Grid_size)

# Dim 7 opperators
Grid_size    = 19   
MASS         = np.linspace(1,1000,Grid_size)
# Define parameter ranges
THETA        = np.linspace(0,np.pi,Grid_size)    
nevents      = 500000  
DIR          = {1:'C62_C63', 2: 'C61_C64', 3:'C62_C63_low', 4: 'C61_C64_low'}
O1           = str('C62')
O2           = str('C63')
dim7Opps     = [str("C71"),str("C72"),str("C73"),str("C74")]
dir_         = str(DIR[1])  # Make sure this is changed to corresponding directory. 
#############################
# Function to check if file exists 
def exists(m,th):
    atlas = os.path.exists("MONO_JET_%1.2F_%1.2F/Events/run_01/NUMBER_OF_M_JETS.csv" %(m,th))
    cms   = os.path.exists("MONO_JET_%1.2F_%1.2F/Events/run_01/NUMBER_OF_M_JETS_CMS.csv" %(m,th))
    return atlas,cms

def exists7(m,opp):
    atlas = os.path.exists("%s/MONO_JET_%s_%1.2F/Events/run_01/NUMBER_OF_M_JETS.csv" %(opp,opp,m))
    cms   = os.path.exists("%s/MONO_JET_%s_%1.2F/Events/run_01/NUMBER_OF_M_JETS_CMS.csv" %(opp,opp,m))
    return atlas,cms    
 
for m in MASS:
    # for th in THETA:
    for opp in dim7Opps: 
        exist_ = exists7(m,opp)
        if exist_[0] and exist_[1]:
        #    print "Both files exist!"
            continue 
        else:
            # if m==1000: ############### Get rid of this line if not debugging!!
            #     # continue
            #     os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))

            # else: 
                # continue
            print "Error with following mass/opperator combo:", opp,m
                # os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))

