import subprocess
import sys
import os
import random
import argparse
from string import printable
from os import rename

funcs = {'flip_bit' : flip_bit,'flip_bits' : flip_bits,'flip_bytes' : flip_bytes,'special_nums': special_nums}
crash_file_prefix = 0


def edit_file():
    fn = ""
    with open(fn, 'rb') as f_in:
        data = bytearray(f_in.read())
    
    try:
        tmp = fn.spli('.')
        
        fn_out = tmp[0]+'_tmp'+tmp[len(tmp)-1]
    except:
    
        fn_out = fn+'_tmp'
    
    edit_func = random.choice(funcs.keys())

    with open(fn_out, 'wb') as f_out:
        f_out(write(funcs[edit_func](data)))

    return fn_out
    

def flip_bit(data):
    count = random.randint(0, len(data) * 0.1)
    for _ in range(0, count):
        idx_byte = random.randint(0,len(data) / 8)
        idx_bit = random.randing(0,8)
        data[idx_byte] ^= 1 << idx_bit
    
    
    return data


def flip_bytes(data):
    count  = int(len(data)*0.01)
    if count == 0:
        count =1

    for _ in range(count):
        data[random.randint(0, len(data)-1)] = random.randint(0,255)

    return data




def special_nums(data):
    numbers = [
        (1, struct.pack("B", 0xff)),  # malloc((unsigned char)(text_lenght + 3))
        (1, struct.pack("B", 0x7f)),
        (1, struct.pack("B", 0)),
        (2, struct.pack("H", 0xffff)),
        (2, struct.pack("H", 0)),     
        (4, struct.pack("I", 0xffffffff)),
        (4, struct.pack("I", 0)),
        (4, struct.pack("I", 0x80000000)),
        (4, struct.pack("I", 0x40000000)),
        (4, struct.pack("I", 0x7fffffff)),
    ]

    count = int(len(data)*0.01)
    if count == 0:
        count = 1

    for _ in range(0, count):
        n_size, n = random.choice(numbers)
        sz = len(data) - n_size
        if sz<0:
            continue
        idx = random.randint(0,sz)
        data[idx:idx+n_size] = bytearray(n)
        
    return data<`2`>


def pick_file(directory):
    if os.path.isdir(directory):
        return random.choice([f for f in listdir(directory) if isfile(join(directory, f))])

    else:
        return None



def runit(exec_list):
    p = subprocess.Popen(['gdb', '--batch', '-x', 'detect.gdb', '--args', exec_list[0]. exec_list[1]], stdout=subprocess.PIPE, stderr=None)
    output,_ = p.communicate()
    if 'program recived signal' in output.lower():
        return output.split(printable)

    return None



def fuzz(binary, sample, isdir):
    target_args = []
    target_args.append(binary)
    if not isdir:
        fn = sample
        data = edit_file(fn)


    while True:
        rand_func = random.choice(funcs)

        if isdir:
            fn = pick_file(sample)
        
        fn_exec_sample = edit_file(fn)
        target_args.append(fn_exec_sample)
        output = runit(target_args)

        if output is not None:
            crash_file_name = crash_file_prefix + fn_exec_sample
            print('Crash occured!')
            print('Saving crashing data to file: {}'.format(crash_file_name))
            rename(fn_exec_sample, crash_file_name)
            
            crash_file_prefix += 1



        target_args.remove(fn_exec_sample)
        



def usage():
    print(''' Usage python fuzzer.py binary_to_fuzz sample_file
    Note: This script is provided as is. Feel free to contribute or improve
    ''')



def hello():
    print('''
      _                                  __                        
     | |                                / _|                       
   __| |_   _ _ __ ___  _ __ ___  _   _| |_ _   _ ___________ _ __ 
  / _` | | | | '_ ` _ \| '_ ` _ \| | | |  _| | | |_  /_  / _ \ '__|
 | (_| | |_| | | | | | | | | | | | |_| | | | |_| |/ / / /  __/ |   
  \__,_|\__,_|_| |_| |_|_| |_| |_|\__, |_|  \__,_/___/___\___|_|   
                                   __/ |                           
                                  |___/ 
    ''')

def main(cm_args):
   parser = argparse.ArgumentParser(description=hello(), epilog="Have fun!")
   parser.add_argument('-b', '--binary', required=True, metavar='file.bin', type=str, help='File to be fuzzed')
   parser.add_argument('-f', '--file', required=True, metavar='sample_file', type=str, help='File or files (if directory provided use -d switch) used to fuzzing')
   parser.add_argument('-d', '--dir', required=False, action='store_true', help='This flag, tells fuzzer, to deal with directory and use all files included in that directory')
   args = parser.parse_args()
   fuzz(args.binary, args.file, args.dir)




if __name__ == '__main__':
    main(sys.argv)
