#!/bin/bash



bayes_opt_nonpro_other.json
bayes_opt_nonpro_snp.json
bayes_opt_protein_other.json
bayes_opt_protein_snp.json
no_protein_features.json

## coding
export CUDA_VISIBLE_DEVICES=1
./cv.py \
    -c ./bayes_opt_protein_snp.json \
    -d ./train.protein-snp.tsv \
    -p cv_protein_snp \
    -f ./all_features.json &> cv_protein_snp.log &


export CUDA_VISIBLE_DEVICES=1
./cv.py \
    -c ./bayes_opt_protein_other.json \
    -d ./train.protein-other.tsv \
    -p cv_protein_other \
    -f ./all_features.json &> cv_protein_other.log &


export CUDA_VISIBLE_DEVICES=1
./cv.py \
    -c ./bayes_opt_nonpro_snp.json \
    -d ./train.nonpro-snp.tsv \
    -p cv_nonpro_snp \
    -f ./no_protein_features.json &> cv_nonpro_snp.log &


export CUDA_VISIBLE_DEVICES=1
./cv.py \
    -c ./bayes_opt_nonpro_other.json \
    -d ./train.nonpro-other.tsv \
    -p cv_nonpro_other \
    -f ./no_protein_features.json &> cv_nonpro_other.log &

wait
