##################################################
# Script file for madDM. Arguments get parsed 
# sequentially as would be in the interactive mode
##################################################
import model pngDM_UFO
define darkmatter ~x
generate relic_density
generate indirect_detection
# output AMS_FIT
launch AMS_FIT
set vave_indirect 1e-03                        # Local average velocity of annihilation region
set fast
# set sigmav_method reshuffle
# set indirect_flux_source_method pythia8      # Use dragon to propagate CR's through galaxy
# set nevents 20000
# set indirect_flux_source_method maddm
indirect=flux_source
# set Mx scan:[30.000000, 45.423729, 62.552966, 61.885593, 60.847458, 56.101695]
nestscan=on
# set Mtwo 2000
set vs 1E-1
# set save_output all