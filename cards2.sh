#!/bin/bash

# Copy cards to correct directory
dir="MONO_JET2/Cards"
here=$PWD

cp mono_param.dat $dir/param_card.dat 
cp run_mono.dat $dir/run_card.dat
# cp mono_pythia8.dat $dir/pythia8_card.dat
cp mono_plot.dat $dir/plot_card.dat
cp delphes_card_ATLAS.tcl $dir/delphes_card_ATLAS.dat
cp mono_setcuts.f $dir/../SubProcesses/setcuts.f
cp mono_cuts.f $dir/../SubProcesses/cuts.f
