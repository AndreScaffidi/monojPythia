#!/bin/bash
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p batch                            
#SBATCH --mem=8GB         
#SBATCH -n 16
#SBATCH -N 1
#SBATCH --time=12:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
cd /fast/users/a1607156/MG5_ROOT
###################################################
# Edit master madgraph scripts
cp mono_jet_launch.py                    mono_jet_launch_${mass}_${theta}.py
sed -i 's/set C62/set C62 '"$C62"'/g'    mono_jet_launch_${mass}_${theta}.py
sed -i 's/set C63/set C63 '"$C63"'/g'    mono_jet_launch_${mass}_${theta}.py
sed -i 's/set mchi/set mchi '"$mass"'/g' mono_jet_launch_${mass}_${theta}.py
sed -i 's/set nevents/set nevents '"$NEvents"'/g' mono_jet_launch_${mass}_${theta}.py

sed -i 's/launch MONO_JET/launch MONO_JET_'"${mass}"'_'"${theta}"'/g' mono_jet_launch_${mass}_${theta}.py

cp mono_jet_out.py                       mono_jet_out_${mass}_${theta}.py
sed -i 's/output MONO_JET/output MONO_JET_'"${mass}"'_'"${theta}"'/g' mono_jet_out_${mass}_${theta}.py

cp cards.sh                              cards_${mass}_${theta}.sh
sed -i 's/MONO_JET/MONO_JET_'"${mass}"'_'"${theta}"'/g' cards_${mass}_${theta}.sh
###################################################
# Run!
./bin/mg5_aMC mono_jet_out_${mass}_${theta}.py
./cards_${mass}_${theta}.sh
./bin/mg5_aMC mono_jet_launch_${mass}_${theta}.py
###################################################
# Clean things up
rm mono_jet_out_${mass}_${theta}.py cards_${mass}_${theta}.sh mono_jet_launch_${mass}_${theta}.py
###################################################
# Run the cutflow
module load GCC/8.2.0-2.31.1
currentDir=$PWD
export DISPLAY=localhost:0.0
cd /fast/users/a1607156/MG5_ROOT/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/ATLAS_13TEV_MONOJET.C("${currentDir}/MONO_JET_${mass}_${theta}/Events/run_01/tag_1_delphes_events.root", "${currentDir}/MONO_JET_${mass}_${theta}/Events/run_01/NUMBER_OF_M_JETS.csv")
.q
EOF
echo "Done."
cd $currentDir
