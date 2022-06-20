#!/usr/bin/env python3

import argparse
import os
import sys
import numpy as np
import pandas as pd
from utils import copen

def get_args():
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("prediction")
    p.add_argument('-c', "--clinvar", required=True)
    p.add_argument("--keep-uncertain", action="store_true")
    p.add_argument('--seed', type=int, default=2020)
    return p


if __name__ == "__main__":
    args = get_args().parse_args()

    clinvar_anno = dict()
    with copen(args.clinvar) as infile:
        for l in infile:
            if l.startswith("#"):
                continue
            chrom, pos, _, ref, alt, _, _, info = l.strip().split('\t')
            key = '_'.join(["chr" + chrom, pos, ref, alt])

            for kv in info.rstrip(';').split(';'):
                k, v = kv.split('=')
                if k == "CLNSIG":
                    annotation = v.lower()
                    if "conflict" in annotation:
                        continue
                    elif "pathogenic" in annotation:
                        clinvar_anno[key] = (1, annotation)
                    elif "benign" in annotation:
                        clinvar_anno[key] = (0, annotation)
                    elif "uncertain_significance" and args.keep_uncertain:
                        clinvar_anno[key] = (0, annotation)
                    break
                else:
                    continue

    # import json
    # json.dump(clinvar_anno, open("clinvar.json", 'w'), indent=4)

    with open(args.prediction) as infile:
        for l in infile:
            if l.startswith("#"):
                continue
            key, label, score = l.strip().split('\t')
            if key in clinvar_anno:
                label, anno = clinvar_anno[key]
            else:
                label, anno = "__unknown__", "__unknown__"
            print(f"{label}\t{score}\t{key}\t{anno}")
            