#!/usr/bin/env python3

import coreapi
import json
import sys

# Check number of arguments
if len(sys.argv) != 4:
    print('Usage: python3 jaspar_core_hs_matrix_api-calls.py <json_file> <format_motif> <txt file containing matrix id list>')
    sys.exit()


# Assign arguments to variables
json_file = sys.argv[1]
format_motif = sys.argv[2]
matrix_to_filter = sys.argv[3]

# Check that the format_motif argument is either jaspar or meme
if format_motif not in ['jaspar', 'meme']:
    print('The format_motif argument must be either <jaspar> or <meme>')
    sys.exit()

# Check that the json_file argument is a json file
if not json_file.endswith('.json'):
    print('The json_file argument must be a json file')
    sys.exit()

# Load the metadata file
with open(json_file) as f:
    metadata = json.load(f)
    
# Load the list of matrix ids to filter
matrix_ids = []

with open(matrix_to_filter, 'r') as file:
    for line in file:
        matrix_ids.append(line.strip())

# Set up a client
client = coreapi.Client()

# Extract the "results" list of dictionaries from the metadata dictionary
results = metadata['results']

# Grab all the urls from the results list of dictionaries
urls = [d['url'] for d in results if d['matrix_id'] in matrix_ids]

# Now we can iterate over the urls and make the API calls
# Note that the url should be appended with .meme as we want to get the matrix in the MEME format

# Initialize a counter
count = 0

# Set filename
if format_motif == 'jaspar':
    filename = 'jaspar_core_hs_TF_nonredundant-filt-matrices_chipseq-exo.jaspar'
elif format_motif == 'meme':
    filename = 'jaspar_core_hs_TF_nonredundant-filt-matrices_chipseq-exo_meme.txt'

for url in urls:
    
    # Strip the offending slash from the end of the URL, then add the appropriate extension
    url = url.rstrip('/') + '.' + format_motif

    matrix = client.get(url)

    # Determine the file mode based on the count
    mode = 'w' if count == 0 else 'a'

    # Write or append the matrix to the file
    with open(filename, mode) as f:
        f.write(matrix)

    count += 1

        
print('Number of matrices retrieved: {}'.format(count))
