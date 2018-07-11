This is the repository associated with the VAPPER Galaxy Tool available in the Galaxy Toolshed
VAPP accurately quantifies the variant antigen diversity in Trypanosoma congolense isolates or the variable Cog presence in T.vivax isolates


The Trypanosoma congolense variant antigen repertoire is divided into 15 clades or phylotypes. These phylotypes are present in any T. congolense isolate, but their relative abundance varies between strains. The purpose of the VAPPER is to accurately quantify antigen diversity in any T. congolense isolate by calculating the relative frequency of each phylotype. 

The Galaxy VAPPER Tool has three modes. 
1) T.congolense Genomic:
This takes raw NGS reads (or pre-assmebled contigs) as input, assembles them de-novo, searches for evidence of each phylotype based on hidden Markov models (HMM), and calculates their relative abundances. 
The results are visualized in three different ways: a table with each phylotype and their relative frequencies as proportions of the full repertoire in the given genome; a heat map with dendogram showing either absolute VAP variation or deviation from the mean, using our pilot dataset; and a Principal Component Analysis (PCA) plot showing variation distribution in the given sample compared to our pilot dataset. 

2) T.congolense Transcriptomic:
This requires NGS paired reads and uses bowtie2 and samtools for read mapping and processing, cufflinks for transcript abundance estimation, and hmmer for sequence identification. The output is a stacked bar chart and a table of frequencies based on the transcript abundances.

3) T.vivax clusters of orthologs
The approach for T. vivax relies on the presence/absence of clusters of orthologs (COGs). It requires velvet for the genome assembly and blast. it recieves paired sequencing reads in fastq format (or a contig file if already assembled) and the output is a binary matrix of the presence/absence of each COG/gene for a given sample. Within the tool there is a database of 28 isolates that are used as a comparison producing a heatmap and dendogram.






