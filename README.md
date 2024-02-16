# Collation of Reference Motif Data

This repo contains all of the R scripts used to collate, extract, and modify the formats of reference motif data from various databases, for use with downstream footprinting tools, specifically TOBIAS.

## Motif Data Sources

Use the python script `pyjaspar_db_query.py` to get a list of JASPAR motif IDs corresponding to whatever filter you set when querying the database.

Note: For the current footprinting analysis we are doing on TOBIAS (as of 2023-06-23), we are using a compilation of all motifs originating from ChIP-related experimental sources. The total number of curated motifs for the current analysis is **1360**. 

Below is the breakdown of the number of motifs from each source:

| Database | Organism | Experimental Sources | Number of Motifs |
|----------|----------|----------------------|----------------|
| JASPAR | *Homo sapiens* | ChIP-seq, ChIP-exo | 208 |
| HOCOMOCO | *Homo sapiens* | ChIP-seq | 401 |
| CisBP | *Homo sapiens* | ChIP-seq, ChIP-exo, ChIP-chip | 751 |

