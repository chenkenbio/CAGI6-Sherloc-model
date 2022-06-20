#!/usr/bin/env python3

import argparse, os, sys, time
import numpy as np
from typing import Any, Dict, List, Union
from functools import partial
print = partial(print, flush=True)

import logging, warnings, json, gzip, pickle
from collections import defaultdict, OrderedDict
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import pearsonr, spearmanr, ttest_ind, mannwhitneyu
# from sklearn.metrics import auc, roc_auc_score, roc_curve, precision_recall_curve, average_precision_score

def get_args():
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # p.add_argument('data', help="/home/chenken/Documents/CAGI6-Sherloc/data/cagi6/final_test_092921.marked.vcf")
    p.add_argument('--ps', required=True, help="protein snp")
    p.add_argument('--po', required=True, help="protein other")
    p.add_argument('--ns', required=True, help="noncoding snp")
    p.add_argument('--no', required=True, help="noncoding other")
    #p.add_argument('--seed', type=int, default=2020)
    return p


if __name__ == "__main__":
    p = get_args()
    args = p.parse_args()
    #np.random.seed(args.seed)

    # raw_label = OrderedDict()
    # with open(args.data) as infile:
    #     for l in infile:
    #         fields = l.strip().split('\t')
    #         if l.startswith('#'):
    #             if "label" in fields:
    #                 label_col = fields.index("label")
    #             else:
    #                 label_col = None
    #             chrom_col = fields.index("chrom")
    #         chrom = fields[chrom_col]
    #         key = fields[0]
    #         if label_col is None:
    #             label = "-100"
    #         else:
    #             label = fields[label_col]
    #         raw_label[key] = (label, chrom)
    
    print("#key\tchrom\tlabel\tprotein_snp\tprotein_other\tnoncoding_snp\tnoncoding_other")
    
    with open(args.ps) as infile:
        for l in infile:
            label, prob, key = l.strip().split('\t')
            chrom = key.split("_")[0].split("@")[-1]
            print('\t'.join([
                key, chrom, label, prob, '0', '0', '0'
            ]))
    with open(args.po) as infile:
        for l in infile:
            label, prob, key = l.strip().split('\t')
            chrom = key.split("_")[0].split("@")[-1]
            print('\t'.join([
                key, chrom, label, '0', prob, '0', '0'
            ]))
 
    with open(args.ns) as infile:
        for l in infile:
            label, prob, key = l.strip().split('\t')
            chrom = key.split("_")[0].split("@")[-1]
            print('\t'.join([
                key, chrom, label, '0', '0', prob, '0'
            ]))

    with open(args.no) as infile:
        for l in infile:
            label, prob, key = l.strip().split('\t')
            chrom = key.split("_")[0].split("@")[-1]
            print('\t'.join([
                key, chrom, label, '0', '0', '0', prob
            ]))


    
    # for key in raw_label:
    #     chrom, label, prob, category = prediction[key]
    #     print("{}\t{}\t{}\t{}\t{}".format(key, chrom, -1 if label == -1 else (1 if label == 2 else 0), label, category))

