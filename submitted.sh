#!/bin/bash -l
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p batch
#SBATCH --mem=8GB         
#SBATCH -n 32
#SBATCH -N 2
#SBATCH --ntasks-per-node 16
## SBATCH --time=72:00:00
###################################################
# Initialize environment
cd
ulimit -s unlimited
module load Anaconda3/2020.07
conda activate monoJ 
# arch/arch/haswell
# module load GCC/6.2.0-2.27
# module load GCCcore/6.2.0
cd /hpcfs/users/a1607156/MG5_ROOT/
export PYTHIA8DATA=/hpcfs/users/a1607156/MG5_ROOT/MG5_aMC_v2_9_2/HEPTools/pythia8/share/Pythia8/xmldoc
export TMPDIR=/hpcfs/users/a1607156/tmp
###################################################
# Edit master madgraph scripts
cp mono_jet_launch.py mono_jet_launch_${mass}_${theta}.py
sed -i 's/set O1/set '"$O1"' '"$C1"'/g'    mono_jet_launch_${mass}_${theta}.py
sed -i 's/set O2/set '"$O2"' '"$C2"'/g'    mono_jet_launch_${mass}_${theta}.py
sed -i 's/set mchi/set mchi '"$mass"'/g' mono_jet_launch_${mass}_${theta}.py
sed -i 's/set nevents/set nevents '"$NEvents"'/g' mono_jet_launch_${mass}_${theta}.py
sed -i 's/launch MONO_JET/launch MONO_JET_'"${mass}"'_'"${theta}"'/g' mono_jet_launch_${mass}_${theta}.py

cp mono_jet_out.py                       mono_jet_out_${mass}_${theta}.py
sed -i 's/output MONO_JET/output MONO_JET_'"${mass}"'_'"${theta}"'/g' mono_jet_out_${mass}_${theta}.py

cp cards.sh                              cards_${mass}_${theta}.sh
sed -i 's/MONO_JET/MONO_JET_'"${mass}"'_'"${theta}"'/g' cards_${mass}_${theta}.sh

###################################################
# Run!
python ./MG5_aMC_v2_9_2/bin/mg5_aMC mono_jet_out_${mass}_${theta}.py
./cards_${mass}_${theta}.sh
python ./MG5_aMC_v2_9_2/bin/mg5_aMC mono_jet_launch_${mass}_${theta}.py
###################################################
# Clean things up
rm mono_jet_out_${mass}_${theta}.py cards_${mass}_${theta}.sh mono_jet_launch_${mass}_${theta}.py
###################################################
# Run the ATLAS cutflow
# module load GCC/8.2.0-2.31.1
currentDir=$PWD
export DISPLAY=localhost:0.0
cd /hpcfs/users/a1607156/MG5_ROOT/MG5_aMC_v2_9_2/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/ATLAS_13TEV_139invfb_MONOJET.C("${currentDir}/MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events.root", "${currentDir}/MONO_JET_${mass}_${theta}/Events/run_01/NUMBER_OF_M_JETS.csv")
.q
EOF
echo "Done."
cd $currentDir
###################################################
# Delete large ATLAS analysis files
cd MONO_JET_${mass}_${theta}/Events/run_01
rm tag_1_delphes_events.root unweighted_events.lhe.gz tag_1_pythia8_events.hepmc.gz
cd /hpcfs/users/a1607156/MG5_ROOT
cd MONO_JET_${mass}_${theta}
rm -rf SubProcesses
cd /hpcfs/users/a1607156/MG5_ROOT
# ###################################################
# # Run Delphes on CMS. First regenerate root file
# cd Delphes
# export DISPLAY=localhost:0.0
# gunzip ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_pythia8_events.hepmc.gz
# ./DelphesHepMC ../delphes_card_CMS.tcl ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events_CMS.root ../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_pythia8_events.hepmc
# echo "Beginning: "
# root -l<<EOF
# gSystem->Load("libDelphes");
# .X ${currentDir}/CMS_36invfb_MONOJET.C("../MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events_CMS.root", "../MONO_JET_${mass}_${theta}/Events/run_01/NUMBER_OF_M_JETS_CMS.csv")
# .q
# EOF
# echo "Done."
# cd $currentDir
# ###################################################
# # Delete large CMS analysis files
# cd MONO_JET_${mass}_${theta}/Events/run_01
# rm tag_1_delphes_events_CMS.root tag_1_pythia8_events.hepmc
# cd /hpcfs/users/a1607156/MG5_ROOT



conda deactivate