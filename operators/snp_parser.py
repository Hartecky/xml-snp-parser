import re
import os

def key_validation(name, data):

    if name in data:
        print(f"Key '{name}' exists in a dataset")
        return True
    else:
        print(f"\nGene with name {name} does not exists in a current database\nOperation stopped \nCheck if your gene name is provided correctly or update database with \nanother XML file with SNP connected to a specified gene.")
        raise SystemExit


def parse_snp_id(gene_name, dataset):

    if key_validation(gene_name, dataset):
        pass
    else:
        return False

    subset = dataset[gene_name]

    results = dict()

    for line in iter(subset.splitlines()):
        if 'rsId' in line:  # rsID
            find_id = re.findall(r'rsId="([^"]*)"', line)
            tmp_id = 'rs' + find_id[0]

            find_genotype = re.findall(r'observed="(.*?)"', line)

        elif 'start=' in line:  # SNP position in a gene / chromosome
            find_position = re.findall(r'start="([^"]*)"', line)
            
            find_orientation = re.findall(r'rsOrientToChrom="(.*?)"', line)
            results[tmp_id] = [int(find_position[0]), find_genotype[0], find_orientation[0]]
            
    return results, gene_name