##################################################                                                   
# Script file for madDM. Arguments get parsed                                                        
# Sequentially as would be in the interactive mode                                                   
################################################                                                   
# import model Dirac_DMEFT_UFO
# generate p p    > chi chi~ @0
# add process p p > chi chi~ j @1
# add process p p > chi chi~ j j NP=1 QCD=2 QED=0 @2
# output MONO_JET

####################################################
launch MONO_JET
shower=Pythia8
delphes=on
detector=ATLAS
set C72 1e+10
set C73 1e+10
set C71 1e+10
set C74 1e+10
set nevents 100
set mchi 800

