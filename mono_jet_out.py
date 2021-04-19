##################################################                                                   
import model /hpcfs/users/a1607156/MG5_ROOT/models/Dirac_DMEFT_UFO  --model name
generate p p    > chi chi~ @0
add process p p > chi chi~ j @1
add process p p > chi chi~ j j NP=1 QCD=2 QED=0 @2
output MONO_JET
####################################################