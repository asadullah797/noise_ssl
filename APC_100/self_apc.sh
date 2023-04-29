#!/bin/bash -l
#SBATCH --job-name=APC100
# speficity number of nodes 
#SBATCH -N 1
# specify the gpu queue

#SBATCH --partition=csgpu
# Request 2 gpus
#SBATCH --gres=gpu:1
# specify number of tasks/cores per node required
#SBATCH --ntasks-per-node=1

# set to email at start,end and failed jobs
#SBATCH --mail-type=ALL
#SBATCH --mail-user=asad@gmail.com

# run from current directory
cd $SLURM_SUBMIT_DIR

# command to use

#python3 runner_apc.py --train
python3 runner_mockingjay.py --train_phone --run_apc
#python3 runner_mockingjay.py --test_phone --run_apc

