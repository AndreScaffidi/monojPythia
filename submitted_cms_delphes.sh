#!/bin/bash
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p batch                            
#SBATCH --mem=8GB         
#SBATCH -n 24  
##SBATCH -N 1
#SBATCH --time=40:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
module load GCC/8.2.0-2.31.1
cd /fast/users/a1607156/MG5_ROOT
currentDir=$PWD
###################################################
# Delete large ATLAS analysis files
cd MONO_JET_${mass}_${theta}/Events/run_01
rm tag_1_delphes_events.root unweighted_events.lhe.gz
cd /fast/users/a1607156/MG5_ROOT
###################################################
# Run Delphes on CMS. First regenerate root file
cd Delphes
export DISPLAY=localhost:0.0
gunzip ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_pythia8_events.hepmc.gz
./DelphesHepMC ../delphes_card_CMS.tcl ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events_CMS.root ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_pythia8_events.hepmc
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/CMS_36invfb_MONOJET.C("../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events_CMS.root", "../MONO_JET_${mass}_${theta}/Events/run_01/NUMBER_OF_M_JETS_CMS.csv")
.q
EOF
echo "Done."
cd $currentDir
###################################################
# Delete large ATLAS analysis files
cd MONO_JET_${mass}_${theta}/Events/run_01
rm tag_1_delphes_events_CMS.root tag_1_pythia8_events.hepmc
cd /fast/users/a1607156/MG5_ROOT