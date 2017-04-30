# Dummy fuzzer

First, lets answer the most important question of this repo:
**Why?!**
**__becouse I can__** :)

I was inspired by GynvaelColdwind's stream:
[Click to view covering stream on YT](https://www.youtube.com/watch?v=BrDujogxYSk)


The main reason of writting this code is fun and practice. If you need really good and convinient fuzzer go for [AFL](http://lcamtuf.coredump.cx/afl/)


## Usage
To run fuzzer, create sample files (they should be valid sample files, processed by fuzzed binary). 

###### Help:
To display help, simply run:
`python main.py -h`

###### Fuzzing:
`python main.py -b file.bin -f sample`




TODO
- [ ] argument parsing
- [ ] parsing config file
- [ ] tbd.
