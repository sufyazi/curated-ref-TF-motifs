#!//usr/bin/env python3
import os
import csv

def extract_line(path, extension, output_path, outfile):
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

    # construct the output file name
    output_file = os.path.join(output_path, outfile)

    # write the sorted list of tuples to a file
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerows(data)

    return output_file

def cleanup_file(output_file, clean_filename):
    # find all instances of :: and replace with empty string
    with open(output_file, 'r') as file:
        data = file.read()
        data = data.replace('::', '')

    # for each row, append element from column 2 as prefix to element in column 1 + _
    data = data.split('\n')
    data = [row.split('\t') for row in data]
    data = [ [row[1] + '_' + row[0], row[1]] if len(row) > 1 else row for row in data]
    data = '\n'.join('\t'.join(item) if isinstance(item, list) else str(item) for item in data)
    
    # construct the output file name
    output_path = os.path.dirname(output_file)
    output_cleanfile = os.path.join(output_path, clean_filename)

    # write the cleaned data back to the file
    with open(output_cleanfile, 'w') as f:
        f.write(data)

    print('Cleanup complete!')
    return data

def subset_column(data, column, output_path, outfile):
    # Split the data into rows
    rows = data.split('\n')

    # construct the output file name
    output_file = os.path.join(output_path, outfile)

    # write the first column of each row to a file
    with open(output_file, 'w') as f:
        for row in rows:
            columns = row.split('\t')
            f.write(columns[0] + '\n')

    print('Subset complete!')
    

if __name__ == '__main__':
    path = '/Users/sufyazi/Documents/local-storage/bioinf/repos/reference-TF-motifs/combined-filt-individual-motifs/individuals'   
    output_path = '/Users/sufyazi/Documents/local-storage/bioinf/repos/reference-TF-motifs/combined-filt-individual-motifs'
    filename = 'tf-motif-IDs-and-tf-names.tsv'
    clean_filename = 'tf-motif-IDs-and-tf-names-sanitized.tsv'
    subset_filename = 'tf-motif-IDs-sanitized-one-col-only.tsv'
    extension = '.jaspar'
    col = 0

    output_file = extract_line(path, extension, output_path, filename)
    # run cleanup
    clean_file = cleanup_file(output_file, clean_filename)

    # truncate file into one column
    subset_column(clean_file, col, output_path, subset_filename)









    