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

def relative_freq_v2(book_text):
    """compute the relative frequence of each letter of the alphabet with dict v2
    """
    occurrency=dict(zip(ALPHABET, np.zeros(len(ALPHABET))))

    for letter in book_text:
        if letter in occurrency:
            occurrency[letter]+=1

    return np.asarray(list(occurrency.values()))

def count_line (book_text):
    '''number of lines of the books
    '''
    lines=1
    for letter in book_text:
        if letter == '\n':
            lines+=1
    return lines
def count_words (book_text):
    '''number of words of the books
    '''
    words=0
    for i, letter in enumerate(book_text):
        if letter not in ALPHABET and letter!= "'" and book_text[i-1] in ALPHABET:
            words+=1
    return words




if __name__ == '__main__':
    start=time.time()
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    parser.add_argument('-r','--read', help='print the book', action='store_true')
    parser.add_argument('-histo','--histogram', help='display the histogram', action='store_true')
    parser.add_argument('-c','--char', help='number of characters', action='store_true')
    parser.add_argument('-l','--lines', help='number of lines', action='store_true')
    parser.add_argument('-w','--words', help='number of words', action='store_true')
    args = parser.parse_args()
    text=process(args.infile)
    if args.read:
        print(text)
    text=text.lower()
    relatives=relative_freq_v2(text)#serve lower
    print_relatives(relatives)
    if args.char:
        print(f'il numero di lettere presenti nel libro è:{relatives.sum()}')
    if args.lines:
        print(f'il numero di righe presenti nel file è:{count_line(text)}')
    if args.words:
        print(f'il numero di parole presenti è: {count_words(text)}')
    if args.histogram:
        plt.bar(ALPHABET,relatives)
    end=time.time()
    print("time elapsed=",end-start)
    if args.histogram:
        plt.show()
