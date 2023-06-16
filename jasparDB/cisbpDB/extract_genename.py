#!//usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pandas as pd

# check arguments
if len(sys.argv) != 3:
    print("Usage: python3 extract_genename.py <pwm_motifs_folder> <tf_info_metadata_tsv>")
    sys.exit(1)

# get arguments
pwm_motifs_folder = sys.argv[1]
tf_info_metadata_tsv = sys.argv[2]

# read in tf_info_metadata_tsv
metadata_df = pd.read_csv(tf_info_metadata_tsv, sep="\t", header=0)




    