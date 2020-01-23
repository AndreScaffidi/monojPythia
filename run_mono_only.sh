#!/bin/bash
###################################################
# Script to run event generation for given M,THETA
###################################################
#SBATCH -p skylake                           
#SBATCH --mem=8GB         
#SBATCH -n 32
#SBATCH --time=20:00:00
###################################################
# Initialize environment
cd
source activate monoJ 
module load GCC/6.2.0-2.27
module load GCCcore/6.2.0
cd /fast/users/a1607156/MG5_ROOT
###################################################
./cards.sh
./bin/mg5_aMC mono_jet.py

