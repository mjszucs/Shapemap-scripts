#!/bin/sh

# File1=find . -type f -name "*R1_001.fastq.gz"
# File2=*_R2_001.fastz.gz

FILES=$(find *.fastq.gz)
Dir=${PWD##*/}

echo $FILES
echo $Dir

java \
-jar /data/home/szucsm/211207_A00405_0503_AHLNMFDSX2/1m7_xrn1_deg/trimmomatic-0.39.jar \
PE -phred33 \
$FILES \
${Dir}_output_R1_paired.fastq.gz ${Dir}_output_R1_unpaired.fastq.gz \
${Dir}_output_R2_paired.fastq.gz ${Dir}_output_R2_unpaired.fastq.gz \
ILLUMINACLIP:../NexteraPE-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
