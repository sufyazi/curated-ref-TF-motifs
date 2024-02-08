# Scripts to Extract and Collate Reference Motif Data

This repo contains all of the R scripts used to collate, extract, and modify the formats of reference motif data from various databases, for use with downstream footprinting tools, specifically TOBIAS.

## Motif Data Sources

Use the python script `pyjaspar_db_query.py` to get a list of jaspar motif IDs corresponding to whatever filter you set when querying the database.

Note: For the current footprinting analysis we are doing on TOBIAS (as of 2023-06-23), we are using a compilation of all motifs originating from ChIP-related experimental sources. The total number of curated motifs for the current analysis is 1360. 
