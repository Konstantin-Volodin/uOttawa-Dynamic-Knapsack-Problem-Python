#!/bin/bash
#SBATCH --time=00-6
#SBATCH --mem-per-cpu=8G
#SBATCH --job-name=simple
#SBATCH --output=optim-simple.out
python3 ../main-simple.py