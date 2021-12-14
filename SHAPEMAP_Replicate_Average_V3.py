#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:35:09 2021

@author: mattszucs
"""

import pandas as pd
import numpy as np
import sys
import os


file1 = pd.read_table(sys.argv[1])
file2 = pd.read_table(sys.argv[2]) 
name = sys.argv[3]
    


def subset(file1,file2):
    '''Takes a dataframe and returns the columns for the normilized and stdev'''
    
    subset1 = file1[["Nucleotide","Sequence","Norm_profile", "Norm_stderr"]]
    subset2 = file2[["Nucleotide","Sequence","Norm_profile", "Norm_stderr"]]
    
    return subset1 , subset2


def change_col_name (subsetTuple):
    '''This function will take two dataframes which only contain the columns that we are looking for and will
    will rename them based on the criteria explained below'''
    
    rep1_names = subsetTuple[0].rename(columns={'Norm_profile': 'Norm_Prof_rep1', 'Norm_stderr': 'Norm_stderr_rep1'})
    rep2_names = subsetTuple[1].rename(columns={'Norm_profile': 'Norm_Prof_rep2', 'Norm_stderr': 'Norm_stderr_rep2'})
    
    return rep1_names, rep2_names


def join_df_avg(df_tuple):
    
    rep1 = df_tuple[0]
    rep2 = df_tuple[1]

    joined_df= rep1.merge(rep2, how = 'left') #This will merge the two dataframes
    #by their index which is just the number of each column
    
    joined_df['avg'] = joined_df[['Norm_Prof_rep1','Norm_Prof_rep2']].mean(axis=1)
    joined_df= joined_df.fillna(0)
    
    return joined_df

    

def parse_and_fill(joined_df):
    '''this function will take a joined df, parse out the average column and export to tsv for varna'''
    new_df = joined_df['avg']
    new_df = new_df.fillna(0)
    
    return new_df


def Shapemapper_Replicate_Average(file1,file2,name):
    '''this function will take the two outputs from SHAPEMAPPER2 and perform the appropriate functions
    to parse the correct columns, rename them, average them, and write them as a tsv file'''
    
    name2 = "Prof_Stdev.txt"
    
    subsetDF = subset(file1,file2)
    renameDF = change_col_name(subsetDF)
    joinedDF = join_df_avg(renameDF)
    filledDF = parse_and_fill(joinedDF)
    
    joinedDF.to_csv(name2, sep = '\t', index = True, header = True)
    
    filledDF.to_csv(name, sep = '\t', index = False, header = False)

    
    return print("all Done!")


Shapemapper_Replicate_Average(file1, file2, name)


#jdf2 = c[['Norm_Prof_rep1_0','Norm_Prof_rep2_0']] = c[['Norm_Prof_rep1','Norm_Prof_rep2']].clip(lower=0)
#This command is useful

This is just a test baby 
