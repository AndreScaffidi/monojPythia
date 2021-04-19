##################################################                                                   
# Script file for madDM. Arguments get parsed                                                        
# Sequentially as would be in the interactive mode                                                   
##################################################                                                   
# import model /hpcfs/users/a1607156/MG5_ROOT/models/Dirac_DMEFT_UFO  --model name
# generate p p    > chi chi~ @0
# add process p p > chi chi~ j @1
# add process p p > chi chi~ j j NP=1 QCD=2 QED=0 @2
# output MONO_JET_TEST
###################################################
launch MONO_JET_TEST
shower=Pythia8
detector=Delphes
# analysis=EXROOTANALYSIS
set C62 0
set C63 1
set nevents 50000
set mchi 150
