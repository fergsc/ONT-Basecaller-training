# ONT-Basecaller-training

Update this with a link to paper, abstract, etc.


## Scripts
1. Create a pseudo-haploid high-accuray HiFi genome (hifiasm.sh)
	1. Assebmle a HiFi genome
	2. Extract and combine haplotype 1 &2 into a single fasta
2. Train a ONT basecaller model
	1. Subdivide fast5 files (optional) (subdivideFast5.sh)
	2. Basecall fast5 files (bonito-basecall.sh)
	3. Iteratively perfrom basecaller training (train.sh)
	4. Save final model in a Guppy compatible format (train.sh)
3. readAssessment
	1. Get read quality scores and lengths from fastq (ONT-getStats.py)
	2. Calculate read identity scores (accuracy versus the HiFI "Truth" genome) (readIdentity.sh)
	3. Combine q-scores and identity scores into a single csv file (combinedIdentityQscores.py)
4. Plotting
	1. Create density plots for qualityAssessment data (densityPlots.py)
5. Regression
	1. Calculate R2 and other linear regression stats (regressionStats.sh)
	2. Plot scatter and regression plot in percent (plotPC.py)
	3. Plot scatter and regression plot in phred (plotPhred.py)


