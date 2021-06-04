import os
import re
from operators import read_files, snp_parser, dist_processing
import argparse

def parse_arguments():

    parser = argparse.ArgumentParser(description='CLI application for parsing XML files containg informations about SNPs')

    required = parser.add_argument_group('required_arguments')
    required.add_argument('-db',
                          '--database',
                          type=str,
                          metavar='',
                          help='Path to a directory with XML files')

    required.add_argument('-gene',
                          '--gene_name',
                          type=str,
                          metavar='',
                          help='Name of the gene in which the polymorphism is located')
    
    required.add_argument('-rs',
                          '--reference_snp',
                          type=str,
                          metavar='',
                          help='rs ID of analyzing SNP')

    required.add_argument('-dist',
                          '--distance',
                          type=int,
                          metavar='',
                          help='Distance to check before and after SNP')

    args = parser.parse_args()

    return args





# name = 'ABCA1'
# rsid = 'rs2230806'



if __name__ == '__main__':
    
    args = parse_arguments()
    path = r'C:\Users\Bartek\Desktop\xml-snp-parser\database'

    data = read_files.import_database(args.database)

    dataset = snp_parser.parse_snp_id(args.gene_name, data)

    dist = dist_processing.distance_processing(dataset, args.reference_snp, args.distance)

    dist_processing.compare_values(dataset, args.reference_snp, dist)


