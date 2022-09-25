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
    """read the book
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r',encoding='utf-8') as input_file:
        text = input_file.read()
    print('Done.')
    return text

def print_relatives(occurrency):
    n=(occurrency).sum()
    print(n)
    relatives = occurrency/n
    for i in range (0,len(ALPHABET)):
        print(f"la lettera {ALPHABET[i]} ha un'incidenza relativa pari a {relatives[i]} \n")

def plot_histogram():
    """plot the histogram of relative frequences
    """

#https://www.programiz.com/python-programming/file-operation
if __name__ == '__main__':
    start=time.time()
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    parser.add_argument('-r','--read', help='print the book', action='store_true')
    parser.add_argument('-histo','--histogram', help='display a histogram of the frequences ', action='store_true')
    args = parser.parse_args()
    text=process(args.infile)
    text=text.lower() #toglie tutte le maiuscole
    if args.read:
        print(text)
    N=len(text)
    print(N)
    occurrency=np.zeros(len(ALPHABET))
    print(type(occurrency))

    for i in range (0,len(text)):
        for j in range (0,len(ALPHABET)):
            if text[i]==ALPHABET[j]:
                occurrency[j] +=1
                break
    print(occurrency)
    plt.bar(ALPHABET,occurrency)



    print_relatives(occurrency)
    if args.histogram:
        plot_histogram()
    end=time.time()
    print(end-start)
    plt.show()
