##################################################                                                   
# Script file for madDM. Arguments get parsed                                                        
# sequentially as would be in the interactive mode                                                   
# ##################################################                                                   
# set lhapdf /home/andre/Uni/LHAPDF-6.2.2/bin/lhapdf-config
# import model Dirac_DMEFT_UFO
# generate p p       > vl vl~      @0
# add process p p    > vl vl~ j @1
# add process p p    > vl vl~ j j  @2
# output SM_JET
launch SM_JET
shower=Pythia8

# ./run_mono.dat
# ./mono_param.dat
# ./mono_pythia8.dat
# set ptj=30                                                                                         
#set drjj=0                                                                                          
# set mmjj=0                                                                                         
# set setptj1min=0                                                                                   
# set xqcut=0  