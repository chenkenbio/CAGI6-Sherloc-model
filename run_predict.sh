#!/bin/bash


if [ $# -lt 1 ]; then
    echo "usage: $0 input"
    exit 1
fi
WORKING_DIR=`dirname $0`

input="$1"
prefix=`basename $input`
prefix=${prefix%.gz}
prefix=${prefix%.tsv}

$WORKING_DIR/src/split_data.py $input -p $prefix

# $WORKING_DIR/src/predict.py -i ${prefix}.
$WORKING_DIR/src/predict.py \
    -i ${prefix}.protein_snp.tsv \
    -m ${WORKING_DIR}/models/cv_protein_snp.model.pkl \
    -p ${prefix}.protein_snp &> ${prefix}.protein_snp.log

$WORKING_DIR/src/predict.py \
    -i ${prefix}.protein_other.tsv \
    -m ${WORKING_DIR}/models/cv_protein_other.model.pkl \
    -p ${prefix}.protein_other &> ${prefix}.protein_other.log

$WORKING_DIR/src/predict.py \
    -i ${prefix}.nonpro_snp.tsv \
    -m ${WORKING_DIR}/models/cv_nonpro_snp.model.pkl \
    -p ${prefix}.nonpro_snp &> ${prefix}.nonpro_snp.log

$WORKING_DIR/src/predict.py \
    -i ${prefix}.nonpro_other.tsv \
    -m ${WORKING_DIR}/models/cv_nonpro_other.model.pkl \
    -p ${prefix}.nonpro_other &> ${prefix}.nonpro_other.log

$WORKING_DIR/src/merge_4_model.py \
    --ps ${prefix}.protein_snp.prediction.txt \
    --po ${prefix}.protein_other.prediction.txt \
    --ns ${prefix}.nonpro_snp.prediction.txt \
    --no ${prefix}.nonpro_other.prediction.txt > ${prefix}.combined.tsv

$WORKING_DIR/src/predict.py \
    -i ${prefix}.combined.tsv \
    -m $WORKING_DIR/models/final.model.pkl \
    -p ${prefix}.final

$WORKING_DIR/src/reorder.py ${prefix}.final.prediction.txt > ${prefix}.output.txt