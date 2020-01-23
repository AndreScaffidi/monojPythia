#!/bin/bash
## ##################################################
## Script to run event generation for given M,THETA
## ##################################################
## SBATCH -p batch                            
## SBATCH --mem=2GB         
## SBATCH -n 1
## SBATCH --time=1:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
cd /fast/users/a1607156/MG5_ROOT
###################################################
# Just run the cutflow!
module load GCC/8.2.0-2.31.1
currentDir=$PWD
export DISPLAY=localhost:0.0
cd /fast/users/a1607156/MG5_ROOT/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/ATLAS_13TEV_MONOJET.C("${currentDir}/MONO_JET_TEST/Events/run_01/tag_1_delphes_events.root", "${currentDir}/MONO_JET_TEST/Events/run_01/NUMBER_OF_M_JETS.csv")
.q
EOF
echo "Done."
cd $currentDir
