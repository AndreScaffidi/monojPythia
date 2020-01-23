##################################################                                                   
# Script file for madDM. Arguments get parsed                                                        
# sequentially as would be in the interactive mode                                                   
# ##################################################                                                   
#set lhapdf /home/andre/Uni/LHAPDF-6.2.2/bin/lhapdf-config
import model DMsimp_s_spin1
generate p p    > xd xd~ 
add process p p > xd xd~ j 
add process p p > xd xd~ j j 
output SIMP
launch SIMP
shower=Pythia8

# ./run_mono.dat
# ./mono_param.dat
# ./mono_pythia8.dat

# set ptj=30                                                                                         
#set drjj=0                                                                                          
# set mmjj=0                                                                                         
# set setptj1min=0                                                                                   
# set xqcut=0  
