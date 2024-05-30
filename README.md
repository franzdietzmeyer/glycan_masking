
# GLYCAN MASKING PIPELINE

With this pipeline you should be able to perfom glycan masking in vaccine development using rosetta suite.



## Authors

- [@fradie21](https://github.com/fradie21/)


## how to use 

1. Start by cloning this repository into your working directory or your HPC directory.

2. Edit the res.txt file containig the residues you like to insert the motif at. The number of the residue represents the N of the NxT motif.
Make sure you give the position number as a three digit input line by line like:

`002`

`013`

`043`

`121`

3. make sure you have access to the rosetta:ml docker image.

4. copy your input pdb into the same working directory as the git repository.

5. start the pipeline by sbatch`ing the gmp.sh file. Make sure to give the following three variables in the command line:



this is just the name or the path to your input PDB file                    
`INPUT_PDB` 

set the name of the project, this name is given to the work_dir as well as the files later on.
`PROJECT_NAME`

select  the tupe of sugar your like to model onto your protein. The mover can deal with a few different types of glycan names including full IUPAC names, files with the full IUPAC names, and short common names such as 'man9' or 'man5'.   [See RosettaCommons for more info](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/carbohydrates/SimpleGlycosylateMover)  
`SUGAR_TYPE`


So, an example command would look like this:
`sbatch input_file.pdb GlycMask man5`




The vanilla number of relaxes is set to n=10. You can change this in the relax.job file located in the "helper_scripts" folder.

## Settings




#### Environment Settings

`conda activate /home/sc.uni-leipzig.de/fs642jhoe/.conda/envs/glycanmasking`

`SING='singularity run /home/sc.uni-leipzig.de/fs642jhoe/docker/rosetta_ml.sif'`


## Version

1.5.1
