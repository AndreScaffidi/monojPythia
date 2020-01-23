#!/bin/bash
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p batch                            
#SBATCH --mem=2GB         
#SBATCH -n 2  
#SBATCH -N 1
#SBATCH --time=8:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
cd /fast/users/a1607156/MG5_ROOT
currentDir=$PWD
module load GCC/8.2.0-2.31.1
analysis_dir="MONO_JET"

# ATLAS
# export DISPLAY=localhost:0.0
# cd /fast/users/a1607156/MG5_ROOT/Delphes
# echo "Beginning: "
# root -l<<EOF
# gSystem->Load("libDelphes");
# .X ${currentDir}/ATLAS_13TEV_MONOJET.C("${currentDir}/${analysis_dir}/Events/run_01/tag_1_delphes_events.root", "${currentDir}/${analysis_dir}/Events/run_01/NUMBER_OF_M_JETS.csv")
# .q
# EOF
# echo "Done."
# cd $currentDir

#Generate CMS root file
# export DISPLAY=localhost:0.0
# gunzip ${currentDir}/${analysis_dir}/Events/run_01/tag_1_pythia8_events.hepmc.gz
# cd /fast/users/a1607156/MG5_ROOT/Delphes
# ./DelphesHepMC ../delphes_card_CMS.tcl ../${analysis_dir}/Events/run_01/tag_1_delphes_events_CMS.root ../${analysis_dir}/Events/run_01/tag_1_pythia8_events.hepmc

cd /fast/users/a1607156/MG5_ROOT/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/CMS_36invfb_MONOJET.C("${currentDir}/${analysis_dir}/Events/run_02/tag_1_delphes_events.root", "${currentDir}/${analysis_dir}/Events/run_02/NUMBER_OF_M_JETS_CMS.csv")
.q
EOF
echo "Done."
cd $currentDir

