#!//usr/bin/env python3
import os
import csv

def extract_line(path, extension, output_file):
    data = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                with open(os.path.join(root, file)) as f:
                    first_line = f.readline()
                    split_line = first_line.split()
                    if len(split_line) > 1:
                        tf_tuple = (split_line[0][1:], split_line[1])
                        data.append(tf_tuple)
    
    # sort the list of tuples by the first element, then second element
    data.sort(key=lambda x: (x[1], x[0]))

    # write the sorted list of tuples to a file
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerows(data)


path = '/Users/sufyazi/Documents/local-storage/bioinf/repos/reference-TF-motifs/combined-filt-individual-motifs/individuals'
extension = '.jaspar'
output_file = '/Users/sufyazi/Documents/local-storage/bioinf/repos/reference-TF-motifs/combined-filt-individual-motifs/tf-motif-IDs-and-tf-names.tsv'

extract_line(path, extension, output_file)





    