# CAGI6-Sherloc-model

The model from the SYSU-SAIL group for the CAGI6 Sherloc challenge.


## Input
- vcf: only the first 5 columns are required
```
chrom   position    ID  ref alt
```

- build version: hg19


## Demo 
1. generate features
```
./prepare_features.sh input.vcf hg19 output
```
The feature file can be found at `output/input.std.avinput.features-ALL.tsv`

2. run prediction
```
./run_prediction.sh output/input.std.avinput.features-ALL.tsv
```
The final prediction will be at `input.std.avinput.features-ALL.output.txt`

## Requirements
- [ANNOVAR](http://annovar.openbioinformatics.org/)
- [MMSplice](https://github.com/gagneurlab/MMSplice_MTSplice)  
- [bedtools](https://bedtools.readthedocs.io/en/latest/)  
- [pyBigWig](https://github.com/deeptools/pyBigWig)  
- [xgboost](https://xgboost.readthedocs.io/)  
- [CrossMap](http://crossmap.sourceforge.net/)
- [skopt](https://scikit-optimize.github.io/stable/install.html)(only for training model)  



