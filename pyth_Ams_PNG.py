##################################################
# Script file for madDM. Arguments get parsed 
# sequentially as would be in the interactive mode
##################################################
import model pngDM_UFO
define darkmatter ~x
generate indirect_detection
# output AMS_FIT_pyth
launch AMS_FIT_pyth
set vave_indirect 1e-03                        # Local average velocity of annihilation region
# set fast
set sigmav_method reshuffle
set indirect_flux_source_method pythia8      # Use dragon to propagate CR's through galaxy
set nevents 20000
indirect=flux_source
set Mtwo 300
# set vs 1E-1
# nestscan=on
