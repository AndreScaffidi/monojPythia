#!/bin/bash
#SBATCH --qos=xlong
#SBATCH -p batch           # partition (this is the queue your job will be added to)  
#SBATCH -n 16             # number of cores 
#SBATCH --time=24:00:00   # time allocation, which has the format (D-HH:MM), here set to 1 hour
#SBATCH --mem=8GB         # specify memory required per node (here set to 32 GB)
module load GCC/5.3.0-binutils-2.25
cd /home/a1607156/MG5_aMC_v2.6.6
./bin/mg5_aMC mono_jet_out.py
./cards.sh
./bin/mg5_aMC mono_jet_launch.py
