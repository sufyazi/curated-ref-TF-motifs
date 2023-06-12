#!/usr/bin/env python3

from pyjaspar import jaspardb
import sys

# Assign arguments to variables
motif_id = sys.argv[1]

# Load the database into an object
jdb_obj = jaspardb(release='JASPAR2022')

# Fetch motifs
motifs_db = jdb_obj.fetch_motifs(
collection = 'CORE',
species = 9606
)
print("The number of motifs in the CORE Hs JASPAR2022 database is: ", len(motifs_db))

print("Searching for metadata for motif: ", motif_id)

for m in motifs_db:
    if motif_id == m.matrix_id:
        print(m)
    else:
        print("Motif metadata not found.")
        



