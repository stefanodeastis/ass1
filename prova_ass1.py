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

def read(file_path):
    """read the book
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r',encoding='utf-8') as input_file:
        text = input_file.read()
    print(text)
    print('Done.')

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
    if args.read:
        read(args.infile)
    if args.histogram:
        plot_histogram()
    end=time.time()
    print(end-start)
