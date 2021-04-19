##################################################                                                   
import model /hpcfs/users/a1607156/MG5_ROOT/models/Dirac_DMEFT_UFO  --model name
generate p p    > chi chi~ @0 QCD=2
add process p p > chi chi~ j @1 QCD=3
add process p p > chi chi~ j j NP=1 QCD=4 QED=0 @2
output MONO_JET
####################################################