import argparse

if __name__ == '__main__':
 parser= argparse.ArgumentParser(description='Print some book statistics')
 parser.add_argument('infile', type=str, help='path to the input file')
 args = parser.parse_args()
 process(args.infile)
