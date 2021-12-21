#!/bin/bash
#----------------------------------------------------------------------#
# This file is a part of ShapeMapper, and is licensed under the terms  #
# of the MIT license. Copyright 2017 Steven Busan.                     #
#----------------------------------------------------------------------#

# Run simple ShapeMapper pipeline on a small subset of example data

set -e # exit on first error (if any)

# Find the parent folder of this script,
# resolving (possibly nested) symlinks

shapemapper \
--name "211215_1m7_top_2_trimmed" \
--out "211215_1m7_top_2_trimmed_OUT" \
--temp "211215_1m7_top_2_trimmed_TEMP" \
--target POWV_3UTR.fa \
--verbose \
--overwrite \
--min-depth 5000 \
--modified --folder plus \
--untreated --folder minus 
