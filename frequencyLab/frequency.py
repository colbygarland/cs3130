#!/usr/bin/env python3

"""Frequency lab, lab2 for cs3130
   Author: Colby Garland
   ID#   : 5034957
   Deals with the file handling/processing functions"""

dictionary = {}

# Opens the appropriate file and processes the file
def process_file(fileName):

    lines = open(fileName, "r")
    word = ""
    
    for ch in lines:
        ch = lines.read(1)
        if ch.isalpha():
            word = word + ch
        else:
            dictionary[word] = 1

    lines.close()

    dump_dictionary()


def dump_dictionary():
    
    print("--")
    print("File Processing Complete.")
    print("\nWord Frequency Table")
    print("WORD                       FREQUENCY")
    print("-------------------------------------")

    for key in dictionary:
        print("{0}                             {1}".format(key, dictionary[key]))
