#############################
# Python script to loop over
# scan parameters
#############################
import os
import numpy as np
#############################
# Define parameter ranges
Grid_size    = 15
MASS         = np.linspace(150,1000,Grid_size)
THETA        = np.linspace(0,np.pi,Grid_size)    ``
nevents      = 500000  
JUST_CUTFLOW = False
PAIR         = 1 # PAIR of intefereing opperators. 1 referes to C1 and C4. 2 referes to C2 and C3 
#############################
print "PAIR = ", PAIR

# Submit C1 and C4
if PAIR == 1:
        O1 = str('C61')
        O2 = str('C64')

        if JUST_CUTFLOW:
                for m in MASS:
                        for th in THETA:
                                # print O1,O2
                                os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted_cutflow.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))
        else:   
                for m in MASS:
                        for th in THETA:
                                # print O1,O2
                                os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))

# Submit C2 and C3
elif PAIR == 2:
        O1 = str('C62')
        O2 = str('C63')
        if JUST_CUTFLOW:
                for m in MASS:
                        for th in THETA:
                                # print O1,O2
                                os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted_cutflow.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))
        else:   
                for m in MASS:
                        for th in THETA:
                                # print O1,O2
                                os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))
