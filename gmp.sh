#!/bin/bash

##input setting - change to your path and values
#? Set the path to your input structure --> please make sure that the structure contains the letters 'wt'   example: my_protein_wt.pdb
input_pdb=$1

#? Set your project name
#PROJECT_NAME='GM'
PROJECT_NAME=$2

#? Set the path to your residue list for the mutations
reslist_csm='res.txt'

#? Set the number of relax-rounds your wish to perform
#relax_n=10
sugar=$3


workdir=$PROJECT_NAME

module purge
module load Anaconda3
source /software/all/Anaconda3/2021.11/etc/profile.d/conda.sh
conda deactivate

conda activate /home/sc.uni-leipzig.de/fs642jhoe/.conda/envs/glycanmasking



## Create the working directory and its subdirectories
mkdir -p "$workdir/csm"
mkdir -p "$workdir/csm"
mkdir -p "$workdir/csm/output"
mkdir -p "$workdir/fastrelaxes"
mkdir -p "$workdir/fastrelaxes/fr_csm"
mkdir -p "$workdir/fastrelaxes/fr_csm/merged"
mkdir -p "$workdir/glycans/glycosylate"
mkdir -p "$workdir/glycans/glycosylate/output"
mkdir -p "$workdir/glycans/model_glycans"
mkdir -p "$workdir/glycans/model_glycans/output"
mkdir -p "$workdir/results"
mkdir -p "$workdir/results/pdbs"
mkdir -p "$workdir/results/scores"


#works
job_id=$(sbatch --parsable helper_scripts/csm.job $input_pdb $PROJECT_NAME $sugar) 
job_id=$(sbatch --parsable --dependency=afterok:$job_id helper_scripts/relax.job $input_pdb $PROJECT_NAME $sugar)
job_id=$(sbatch --parsable --dependency=afterok:$job_id helper_scripts/analyze.job $input_pdb $PROJECT_NAME $sugar)
job_id=$(sbatch --parsable --dependency=afterok:$job_id helper_scripts/glycosylate.job $input_pdb $PROJECT_NAME $sugar)
job_id=$(sbatch --parsable --dependency=afterok:$job_id helper_scripts/model_glycan.job $input_pdb $PROJECT_NAME $sugar)




# __author__ = "Franz Dietzmeyer"
# __contact__ = "franz.dietzmeyer@medizin.uni-leipzig.de"
# __version__ = "1.5.1"