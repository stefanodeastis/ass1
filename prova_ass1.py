#!/usr/bin/env python3
# Copyright (C) 2022 s.deastis@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23.
"""
import argparse
import time
import string
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

ALPHABET=tuple(string.ascii_lowercase)

def process(file_path):
    """read the file
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r',encoding='utf-8') as input_file:
        book_text = input_file.read()
    print('Done.')
    return book_text

def print_relatives(occurrency):
    '''print relative freqences
    '''
    tot_char=occurrency.sum()
    print(tot_char)
    frequences= occurrency/tot_char
    for i, letter in enumerate(ALPHABET):
        print(f"la lettera {letter} ha un'incidenza relativa pari a {frequences[i]} \n")

def relative_freq(book_text):
    """compute the relative frequence of each letter of the alphabet
    """
    occurrency=np.zeros(len(ALPHABET))
    for letter in book_text:
        for j, alphabet_letter in enumerate(ALPHABET):
            if letter==alphabet_letter:
                occurrency[j] +=1
                break
    return occurrency
#https://www.programiz.com/python-programming/file-operation
if __name__ == '__main__':
    '''programma principale
    '''
    start=time.time()
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    parser.add_argument('-r','--read', help='print the book', action='store_true')
    parser.add_argument('-histo','--histogram', help='display the histogram', action='store_true')
    args = parser.parse_args()
    text=process(args.infile)
    if args.read:
        print(text)

    relatives=relative_freq(text.lower())

    print_relatives(relatives)

    if args.histogram:
        plt.bar(ALPHABET,relatives)
    end=time.time()
    print("time elapsed=",end-start)
    if args.histogram:
        plt.show()
