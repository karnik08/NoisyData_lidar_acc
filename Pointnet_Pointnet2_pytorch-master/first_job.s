#!/bin/bash
#
#SBATCH --job-name=myfirstjob
#SBATCH --nodes=1 
#SBATCH --time=1:00:00
#SBATCH --mem=16GB
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --output=./first_job.out
#SBATCH --error=./first_job.err

singularity exec --nv --overlay $SCRATCH/singular/overlay-25GB-500K.ext3:rw /scratch/work/public/singularity/cuda11.3.0-cudnn8-devel-ubuntu20.04.sif 
/bin/bash -c " source /ext3/env.sh; conda activate pytorch_test; python train_classification.py --log_dir log --gpu 0" 


