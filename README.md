# XML SNP Data parser

## Project description

The aim of this project is to create a simple tool for SNP analysis contained in XML structured file from NCBI FTP server:
```
https://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606/genotype_by_gene/
```

It allows user to check whether there are other mutations within the polymorphism being tested with specified distance, what can be useful for biologist in designing primers for DMAS (Double mismatch allele specific) qPCR reaction primers.

## Fragment of a file structure

```
<SnpInfo rsId="781249833" observed="G/T">
        <SnpLoc genomicAssembly="108:GRCh38.p7" geneId="19" geneSymbol="ABCA1" chrom="9" start="104791890" locType="2" rsOrientToChrom="fwd" contigAllele="T" contig="NT_008470:20"/>
        <SsInfo ssId="1689589581" locSnpId="EXAC_0.3.9:g107554172t&gt;g" ssOrientToRs="fwd">
            <ByPop popId="16571" sampleSize="121386">
                <AlleleFreq allele="G" freq="0"/>
                <AlleleFreq allele="T" freq="1"/>
            </ByPop>
        </SsInfo>
    </SnpInfo>
```

Main attributes:

- Single Nucleotide Polymorphisms ID - __rsId__ tag
- Their positions in the gene - __start__ tag
- Genotype - __observed__ tag
- Strandness - __rsOrientToChrom__ tag

and many more, but these above are in our fields of interests.
This repo contains a database direcotory, which is a set of 20 genes in different XML files, some SNPs of this genes contributes to the development of Alzheimer's disease. The database directory can be extended with another gene files.

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

Note: After analysis, running script again is deleting existing files with results, so make sure that you copied them into another file.
