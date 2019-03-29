import argparse

def ref_finder(file_loc, out_loc):
 
    '''
    Counts the number of times 'Python' or 'python' occurs in a document.
    >>> ref_finder('C:/Users/ley015/DATASCHOOL/Python/intermediate_practical/raw_data/42pythons.txt', 'intermediate_practical/output_files/42pythons.txt')
    42  
    
    
    '''


    with open (file_loc, encoding = 'Latin-1') as f:
        with open (out_loc, 'w') as out_file:
            python_count = 0
            for line in f:
                line = line.lower()
                if 'python' in line:
                    python_count += line.count('python')
            out_file.write("'Python' occurs in the document " + str(python_count) + " times!")
            return (python_count)
        
parser = argparse.ArgumentParser()
parser.add_argument("file_loc")
parser.add_argument("out_loc")
args = parser.parse_args()
ref_finder(args.file_loc,args.out_loc)
