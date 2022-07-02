# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:09:41 2022

@author: tyson.fuller
"""

import os
import sys
import pysam
import time
import argparse

def parse_user_input():
    parser = argparse.ArgumentParser(
            description = "Return percent of genome at or above specified coverage"
            )
    parser.add_argument('-b', '--bam',
                        help="The input BAM file",
                        type=str, required=True
                        )
    parser.add_argument('-t', '--threshold',
                        help="The input, frc Features.txt file",
                        type=int, default=3
                        )
    parser.add_argument('-o', '--output',
                        help="The output tsv file",
                        type=str, required=True
                        )
    
    return parser.parse_args()
    
    
def get_chromosomes_names(input):

    # opening the bam file with pysam
    bamfile = pysam.AlignmentFile(input, 'rb')
    # query all the names of  the chromosomes in a list
    list_chromosomes = bamfile.references
    list_length = bamfile.lengths
    bamfile.close()
    return list_chromosomes, list_length


def count_depth(chr_name, size, threshold, input):
    """
    Count the depth of the read. For each genomic coordinate return the
    number of reads
    -----
    Parameters :
        chr : (str) name of the chromosome
        threshold : (int) minimum value to count pileup
    -----
    Returns :
        int : count of pileups above threshold
    """
    bp = 0
    bamfile = pysam.AlignmentFile(input, 'rb')
    for pileupcolumn in bamfile.pileup(chr_name):
        depth = pileupcolumn.nsegments
        if depth >= threshold:
            bp += 1
    bamfile.close()
    return bp


if __name__ == "__main__":
    args = parse_user_input()
    
    print(f'Starting depth estimate for bam: {args.bam} at threshold {args.threshold}')
    
    sum = 0
    list_chrs, list_sizes = get_chromosomes_names(args.bam)
    print("Found {} chromosomes to count".format(len(list_chrs)))
    
    asmsize = 0
    
    for chr, size in zip(list_chrs, list_sizes):
        sum += count_depth(chr, size, args.threshold, args.bam)
        asmsize += size
        print(f'Finished with chr: {chr}. {size} {sum}')
    per_cov= (sum/asmsize)*100
    per_cov = round(per_cov, 2)
    with open(args.output, 'w') as final:
        final.write(f'bp at {args.threshold}x depth\tasm_size\tasm percent at {args.threshold}x depth\n')
        final.write(f'{sum}\t{asmsize}\t{per_cov}\n')



