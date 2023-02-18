# 1001ArabidopsisGenomes_RFLPs

A list of all the RFLP sites that are variable among the 1001 Arabidopsis genomes for EcoRI, BamHI, NotI, PstI, and HindIII. The genotypes of all 1135 lineages are available at [FigShare – DOI: 10.6084/m9.figshare.22121804](https://doi.org/10.6084/m9.figshare.22121804). The genotype format is a modified VCF format, such that 0|0 means that the accession has the restriction site (i.e., same genotype as TAIR10), while 1|1 means that the accession lacks the restriction site (i.e., different genotype from TAIR10). Original VCF header was as follows:

\#\#fileformat=VCFv4.1<br>
\#\#FILTER=<ID=PASS,Description="All filters passed"><br>
\#\#FILTER=<ID=q30,Description="Quality below 30"><br>
\#\#INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth"><br>
\#\#FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype"><br>
\#\#FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality"><br>
\#\#FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth"><br>
\#\#FILTER=<ID=q25,Description="Quality below 25"><br>
\#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT<br>

If you'd like another restriction enzyme added, please get in touch (joel.sharbrough@nmt.edu), or feel free to use the code posted here to do it yourself. Amplicons and primers for selected markers are also posted here.

Data from:
https://1001genomes.org/data/GMI-MPI/releases/v3.1/

1,135 Genomes Reveal the Global Pattern of Polymorphism in Arabidopsis thaliana
1001 Genomes Consortium Cell (2016), 166(2) 481-91. https://doi.org/10.1016/j.cell.2016.05.063
