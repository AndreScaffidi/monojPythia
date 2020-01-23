##################################################                                                   
# Script file for madDM. Arguments get parsed                                                        
# Sequentially as would be in the interactive mode                                                   
################################################                                                   
# import model Dirac_DMEFT_UFO
# generate p p    > chi chi~ @0
# add process p p > chi chi~ j @1
# # add process p p > chi chi~ j j NP=1 QCD=2 QED=0 @2
# output MONO_JET2

####################################################
launch MONO_JET2
shower=Pythia8
delphes=on
detector=ATLAS
set C62 0.00
set C63 1.00
set nevents 1000
set mchi 200

