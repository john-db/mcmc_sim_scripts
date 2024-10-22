#!/bin/bash
 
#SBATCH --mem=2g
#SBATCH --time=1:00:00

ARGS="$ARGS"

/home/bridgersjd/trisicell/software/modified_scite/scite ${ARGS}