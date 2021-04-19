#############################
# Python script to loop over
# scan parameters
#############################
import os
import numpy as np
#############################
# Define parameter ranges
# NOW FOR ALL MASSES
# Dim-6 case
# Grid_size    = 19   
# MASS         = np.linspace(1,1000,Grid_size)
# THETA        = np.linspace(0,np.pi,Grid_size) 
# Dim-7 case
Grid_size    = 19   
MASS         = np.linspace(1,1000,Grid_size)
nevents      = 500000  
JUST_CUTFLOW = False
PAIR         = 2 # PAIR of intefereing opperators. 1 referes to C1 and C4. 2 referes to C2 and C3 
DIM          = 7 # Opperator dimention to do 
#############################
print "PAIR = ", PAIR
print "DIM = ", DIM
# Submit C1 and C4
if DIM == 6: 
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
                                        os.system('sbatch --job-name=m%1.2F_th%1.2F.run --output=m%1.2F_th%1.2F.out --export=mass=%1.2F,theta=%1.2F,C1=%1.2F,C2=%1.2F,NEvents=%d,O1=%s,O2=%s submitted.sh' %(m,th,m,th,m,th,np.sin(th),np.cos(th),nevents,O1,O2))
                                        # exit(0)

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

elif DIM == 7:
        O1 = str('C71')
        O2 = str('C72')
        O3 = str('C73')
        O4 = str('C74')
        for m in MASS:
                os.system('sbatch --job-name=m%1.2F_C71.run --output=m%1.2F_C71.out --export=mass=%1.2F,NEvents=%d,Opp=%s submitted_dim7.sh' %(m,m,m,nevents,O1))
                os.system('sbatch --job-name=m%1.2F_C72.run --output=m%1.2F_C72.out --export=mass=%1.2F,NEvents=%d,Opp=%s submitted_dim7.sh' %(m,m,m,nevents,O2))
                os.system('sbatch --job-name=m%1.2F_C73.run --output=m%1.2F_C73.out --export=mass=%1.2F,NEvents=%d,Opp=%s submitted_dim7.sh' %(m,m,m,nevents,O3))
                os.system('sbatch --job-name=m%1.2F_C74.run --output=m%1.2F_C74.out --export=mass=%1.2F,NEvents=%d,Opp=%s submitted_dim7.sh' %(m,m,m,nevents,O4))