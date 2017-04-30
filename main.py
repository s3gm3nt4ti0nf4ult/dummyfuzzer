import subprocess
import sys
import os
import random
import argparse



def flip_bit():
    pass



def flip_bits(sample):
    pass



def flip_bytes(sample):
    pass



def special_nums(sample):
    pass



def pick_file():
    pass



def fuzz(binary, sample, isdir):
    while True:
        if isdir:
            fn = pick_file()
    
        else:
            fn = sample

        random_func = random.choice([flip_bit, flip_bits, flip_bytes, special_nums])
        
        with open(fn, 'rb') as f:
            data = random_func(f.read())

        break




def usage():
    print(''' Usage python fuzzer.py binary_to_fuzz sample_file
    Note: This script is provided as is. Feel free to contribute or improve
    ''')



def hello():
    pass



def main(cm_args):
   parser = argparse.ArgumentParser(description=hello(), epilog="Have fun!")
   parser.add_argument('-b', '--binary', required=True, metavar='file.bin', type=str, help='File to be fuzzed')
   parser.add_argument('-f', '--file', required=True, metavar='sample_file', type=str, help='File or files (if directory provided use -d switch) used to fuzzing')
   parser.add_argument('-d', '--dir', required=False, action='store_true')
   args = parser.parse_args()
   fuzz(args.binary, args.file, args.dir)




if __name__ == '__main__':
    main(sys.argv)
