# CAGI6-Sherloc-model

The model from the SYSU-SAIL group for the CAGI6 Sherloc challenge.

**This repository has been archived. See [here](https://github.com/biomed-AI/ML-GVP) for updates.**


## Input
- vcf: only the first 5 columns are required
```
chrom   position    ID  ref alt
```

- build version: hg19

- Annotation database


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
- blast: NCBI BLAST  
- [MMSplice](https://github.com/gagneurlab/MMSplice_MTSplice)  
- [bedtools](https://bedtools.readthedocs.io/en/latest/)  
- [pyBigWig](https://github.com/deeptools/pyBigWig)  
- [xgboost](https://xgboost.readthedocs.io/)  
- [CrossMap](http://crossmap.sourceforge.net/)
- [skopt](https://scikit-optimize.github.io/stable/install.html)(only for training model)  



## How to configure `config.sh`  
Set the keys in `config.sh`: 
- `blastp`: path to the `blastp` program
- `hg19`/`hg38`: GRCh37(hg19)/GRCh38(hg38) reference genome  
- `hg19_gtf`: hg19 gene annotation in `GTF` format
- `PSSM_SPOT_PATH`: path to `PSSM-HHM-SPOT_DISORDER` folder (decompress `PSSM-HHM-SPOT_DISORDER.tgz` in `data/PSSM-HHM-SPOT_DISORDER`)  
- `ROADMAP_DB`: path to Roadmap ChIP-seq/DNase-seq processed data (download using the following commands in `data/roadmap`)
    ```bash
    for eid in `seq 63 113`; do
        eid=`python -c "print('E%03d' % $eid)"`
        for assay in DNase H3K27ac H3K27me3 H3K36me3 H3K4me1 H3K4me3 H3K9me3; do
            wget -c https://egg2.wustl.edu/roadmap/data/byFileType/signal/consolidated/macs2signal/pval/${eid}-${assay}.pval.signal.bigwig
        done
    done
    ```
- `ENCODE_CHIPSeq_DB`: path to `data/encode_chipseq` folder (unzip `data/encode_chipseq/encode_chipseq.tgz`)
- `ENCODE_eCLIP_DB`: path to RNA binding protein (RBP) binding sites data, `tar -xf ENCODE_RBP.tar` in `data/eCLIP`
- `gtex_eQTL_loci`: path to `data/GTEx.eQTL.v8.hg38to19.merged.bed.gz`
- `gnomAD_AF_DB`: path to `gnomAD.v3` folder (`tar -xf gnomad.v3.AF.vcf.tar` in `data/gnomAD.v3`)
- `uniprot_fasta`: uniprot protein fasta file (`unzip data/uniprot_human.fa.gz`)
- `hg19_phastCons_100way`
- `hg19_phyloP_100way`
- `hg19_phastCons_46way_primates`
- `hg19_phyloP_46way_primates`
- `hg19_phastCons_46way_vertebrate`
- `hg19_phyloP_46way_vertebrate`  
    Download the above files in bigWig format in `data/ucsc/hg19` using
    ```bash
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phyloP46way/vertebrate.phyloP46way.bw
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phyloP46way/primates.phyloP46way.bw
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phyloP100way/hg19.100way.phyloP100way.bw
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phastCons46way/primates.phastCons46way.bw
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phastCons46way/vertebrate.phastCons46way.bw
    wget -c http://hgdownload.cse.ucsc.edu/goldenpath/hg19/phastCons100way/hg19.100way.phastCons.bw  
    ```
- `mmsplice_python`  
    install mmsplice and set `mmsplice_python` to the python interpreter with MMSplice installed
