#!/bin/bash
#SBATCH -p batch   
#SBATCH --mem=8GB         
#SBATCH -n 4
##SBATCH -N 1
#SBATCH --time=10:00:00
cd /fast/users/a1607156/MG5_ROOT
DIR="C62_C63_OLD"
rm -r $DIR