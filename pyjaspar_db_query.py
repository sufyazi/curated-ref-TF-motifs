#!/usr/bin/env python3

from pyjaspar import jaspardb
import sys

# Check if the user has provided correct arguments
try:
    sys.argv[1] not in ['nothing', 'motif_id', 'tf_name', 'tf_class', 'tf_family', 'tax_group', 'species', 'data_type']
except IndexError:
    print("Please provide a valid first argument.")
    print("First argument should be one of these query filters: 'nothing', 'motif_id', 'tf_name', 'tf_class', 'tf_family', 'tax_group', 'species', or 'data_type'.")
    print("Second argument should be the query string associated with your query filter.")
    sys.exit(1)

# Check the number of arguments
if len(sys.argv) != 3:
    print("Please provide a second argument.")
    print("Second argument should be the query string associated with your query filter.")
    sys.exit(1)


# Assign arguments to variables
query_filter = sys.argv[1]
query_value = sys.argv[2]
if query_filter == 'data_type' or query_filter == 'tax_group':
    if ',' in query_value:
        query_list = query_value.split(', ')
        print(query_list)
    else:
        query_list = [query_value]

# Load the database into an object
jdb_obj = jaspardb(release='JASPAR2022')

# Change modes based on the arguments
if query_filter == 'nothing':
    print("Extracting all CORE Hs motifs from the JASPAR2022 database...")
    # Fetch motifs
    motifs_db = jdb_obj.fetch_motifs(
    collection = 'CORE',
    species = 9606
    )
    print("The number of ALL motifs in the CORE Hs JASPAR2022 database is: ", len(motifs_db))
    # Ask user if they want to print out all motifs to stdout
    user_input = input("Do you want to print out all motifs to stdout? (y/n): ")
    if user_input.lower() == 'y':
        # Print the motifs
        for motif in motifs_db:
            print(motif)
            
else:
    print("Filtering database based on the following query: ", query_filter)
    
    # Create a dictionary of query filters and their corresponding query values
    filter_args = {
        query_filter: query_list
    }

    # Fetch motifs
    motifs_db = jdb_obj.fetch_motifs(
    collection = 'CORE',
    species = 9606,
    **filter_args
    )
    
    print("The number of motifs after filtering is: ", len(motifs_db))
    # initialize an empty list
    motif_list = []
    # Iterate over the motifs and append the matrix_id to the list
    for m in motifs_db:
        motif_list.append(m.matrix_id)
    
    # Save the motifs to a file
    user_input = input("Do you want to save the motifs to a file? (y/n): ")
    if user_input.lower() == 'y':
        # Save the motifs
        with open(f'filtered_motifs_{query_filter}.txt', 'w') as file:
            for item in motif_list:
                file.write(f"{item}\n")
    else:
        print("Exiting program...")

        



