#!/bin/bash


#SBATCH --job-name=opennmt
#SBATCH --account=adarsh
#SBATCH --output=%x.out
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=5gb
#SBATCH --gres=gpu:1
#SBATCH --time=01-12:00:00
#SBATCH --partition=standard
#SBATCH --mail-type=ALL
#SBATCH --mail-user=abanerjee@arizona.edu

module load anaconda/2020
conda init bash
./scripts/test