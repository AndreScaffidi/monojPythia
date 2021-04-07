#!/bin/bash
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p batch   
#SBATCH --qos=xlong
#SBATCH --mem=8GB         
#SBATCH -n 32
##SBATCH -N 1
#SBATCH --time=72:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
cd /fast/users/a1607156/MG5_ROOT

export TMPDIR=/fast/users/a1607156/tmp
###################################################
# Edit master madgraph scripts
cp mono_jet_launch7.py                    mono_jet_launch_7${mass}_${Opp}.py
sed -i 's/set O1 1.0/set '"$Opp"' 1.0/g'    mono_jet_launch_7${mass}_${Opp}.py
sed -i 's/set mchi/set mchi '"$mass"'/g' mono_jet_launch_7${mass}_${Opp}.py
sed -i 's/set nevents/set nevents '"$NEvents"'/g' mono_jet_launch_7${mass}_${Opp}.py
sed -i 's/launch MONO_JET/launch MONO_JET_'"${Opp}"'_'"${mass}"'/g' mono_jet_launch_7${mass}_${Opp}.py

cp mono_jet_out7.py                       mono_jet_out_7${mass}_${Opp}.py
sed -i 's/output MONO_JET/output MONO_JET_'"${Opp}"'_'"${mass}"'/g' mono_jet_out_7${mass}_${Opp}.py

cp cards7.sh                              cards_7${mass}_${Opp}.sh
sed -i 's/MONO_JET/MONO_JET_'"${Opp}"'_'"${mass}"'/g' cards_7${mass}_${Opp}.sh
###################################################
# Run!
./bin/mg5_aMC mono_jet_out_7${mass}_${Opp}.py
./cards_7${mass}_${Opp}.sh
./bin/mg5_aMC mono_jet_launch_7${mass}_${Opp}.py
###################################################
# Clean things up
rm mono_jet_out_7${mass}_${Opp}.py cards_7${mass}_${Opp}.sh mono_jet_launch_7${mass}_${Opp}.py
###################################################
# Run the ATLAS cutflow
module load GCC/8.2.0-2.31.1
currentDir=$PWD
export DISPLAY=localhost:0.0
cd /fast/users/a1607156/MG5_ROOT/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/ATLAS_13TEV_MONOJET.C("${currentDir}/MONO_JET_${Opp}_${mass}/Events/run_01/tag_1_delphes_events.root", "${currentDir}/MONO_JET_${Opp}_${mass}/Events/run_01/NUMBER_OF_M_JETS.csv")
.q
EOF
echo "Done."
cd $currentDir
###################################################
# Delete large ATLAS analysis files
cd MONO_JET_${Opp}_${mass}/Events/run_01
# rm tag_1_delphes_events.root tag_1_pythia8_events.hepmc.gz unweighted_events.lhe.gz
rm tag_1_delphes_events.root unweighted_events.lhe.gz
cd /fast/users/a1607156/MG5_ROOT
###################################################
# Run Delphes on CMS. First regenerate root file
cd Delphes
export DISPLAY=localhost:0.0
gunzip ../MONO_JET_${Opp}_${mass}/Events/run_01/tag_1_pythia8_events.hepmc.gz
./DelphesHepMC ../delphes_card_CMS.tcl ../MONO_JET_${Opp}_${mass}/Events/run_01/tag_1_delphes_events_CMS.root ../MONO_JET_${Opp}_${mass}/Events/run_01/tag_1_pythia8_events.hepmc
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/CMS_36invfb_MONOJET.C("../MONO_JET_${Opp}_${mass}/Events/run_01/tag_1_delphes_events_CMS.root", "../MONO_JET_${Opp}_${mass}/Events/run_01/NUMBER_OF_M_JETS_CMS.csv")
.q
EOF
echo "Done."
cd $currentDir
###################################################
# Delete large ATLAS analysis files
cd MONO_JET_${Opp}_${mass}/Events/run_01
rm tag_1_delphes_events_CMS.root tag_1_pythia8_events.hepmc
cd /fast/users/a1607156/MG5_ROOT
