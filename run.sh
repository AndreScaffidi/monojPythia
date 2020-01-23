#!/bin/bash
currentDir=$PWD
module load GCC/8.2.0-2.31.1
analysis_dir="MONO_JET"
cd /fast/users/a1607156/MG5_ROOT/Delphes
echo "Beginning: "
root -l<<EOF
gSystem->Load("libDelphes");
.X ${currentDir}/CMS_36invfb_MONOJET.C("${currentDir}/${analysis_dir}/Events/run_02/tag_1_delphes_events.root", "${currentDir}/${analysis_dir}/Events/run_02/NUMBER_F_M_JETS_CMS.csv")
.q
EOF
echo "Done."
EOF
