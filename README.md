# XML SNP Data parser

## Project description

The aim of this project is to create a simple tool for SNP analysis contained in XML structured file from NCBI FTP server. These files consists of data with tags:

- Single Nucleotide Polymorphisms ID - __rsId__ tag
- Their positions in the gene - __start__ tag
- Genotype - __observed__ tag
- Strandness - __rsOrientToChrom__ tag

and many more, but these above are in our fields of interests.
This repo contains a set of 20 genes in different XML files, some SNPs of this genes contributes to the development of Alzheimer's disease

## Runnning script

```
git clone https://github.com/Hartecky/xml-snp-parser.git
cd xml-snp-parser
python main.py 
```

## Providing arguments
```
- -db,      --database        Path to a directory with XML files
- -gene,    --gene_name       Name of the gene containing SNP which will be analyzed
- -rs,      --reference_snp   Reference ID of analyzed SNP
- -dist,    --distance        Distance to check before and after SNP
```

Results are saved into 'results.txt' file.

Note: After analysis, running script again is deleting existing files with results, so please copy them into another file.
