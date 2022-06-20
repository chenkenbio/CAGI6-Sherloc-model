#!/bin/bash

if [ $# -lt 1 ]; then
    echo "usage: $0 features"
    exit 1
fi
input="$1"
prefix=`basename $input`
prefix=${prefix%.gz}
prefix=${prefix%.tsv}

for group in protein-other protein-snp nonpro-other  nonpro-snp; do
    echo "##$group" > ${prefix}.${group}.tsv
    grep "^#" ${input} >> ${prefix}.${group}.tsv
done

grep -v "^#" $input | awk '$NF != "NaN"' | awk '$18 != 0' >> ${prefix}.protein-other.tsv
grep -v "^#" $input | awk '$NF != "NaN"' | awk '$18 == 0' >> ${prefix}.protein-snp.tsv
grep -v "^#" $input | awk '$NF == "NaN"' | awk '$18 != 0' >> ${prefix}.nonpro-other.tsv
grep -v "^#" $input | awk '$NF == "NaN"' | awk '$18 == 0' >> ${prefix}.nonpro-snp.tsv

