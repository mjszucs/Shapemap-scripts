#!/bin/bash
#----------------------------------------------------------------------#
# This file is a part of ShapeMapper, and is licensed under the terms  #
# of the MIT license. Copyright 2017 Steven Busan.
#
# MSz edit. So this script will now autopopulate the variable
# fields based on WHAT YOU NAME THE FILE!!!!!!!!
# Saves a bunch of grunt work changing all of the information in the files
#----------------------------------------------------------------------#

# Run simple ShapeMapper pipeline on a small subset of example data
#



set -e # exit on first error (if any)

# Find the parent folder of this script,
# resolving (possibly nested) symlinks


NAME=$0
MODNAME=${NAME:2:-3} # find the name and trim off stuff
MODNAME_OUT="${NAME:2:-3}_Out" #make as string that has out
MODNAME_TEMP="${NAME:2:-3}_temp" #make a string that has temp as the folder
FASTA=$(find . -name "*.fa") #find the fasta file
FASTA_TRIM=${FASTA:2} # trim off the beginning

shapemapper \
--name $MODNAME \
--out $MODNAME_OUT \
--temp $MODNAME_TEMP \
--target $FASTA_TRIM \
--verbose \
--overwrite \
--min-depth 5000 \
--modified --folder plus \
--untreated --folder minus
