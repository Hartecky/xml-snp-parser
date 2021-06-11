import os
import re
from operators import read_files, snp_parser, dist_processing
import argparse

def parse_arguments():

	 parser = argparse.ArgumentParser(description='CLI application for parsing XML files containg informations about SNPs')

	 required = parser.add_argument_group('required_arguments')

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


if __name__ == '__main__':

	path = os.getcwd()
	tmp = path + '\\database\\'

	args = parse_arguments()

	#read_files.prepare_space('results.txt')

	data = read_files.import_database(tmp)

	dataset = snp_parser.parse_snp_id(args.gene_name, data)

	dist = dist_processing.distance_processing(dataset[0], args.reference_snp, args.distance)
	
	dist_processing.compare_values(dataset[0], args.reference_snp, dist, dataset[1])



