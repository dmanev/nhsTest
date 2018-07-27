#!/usr/bin/python

''' Python command line hscic-news index and search

Example output:
./ns.py -o "Care Quality Commission"                                                                                 ~/Documents/Job Interviews/nhs/solutions/nhsTest
0, 1, 2, 3, 4, 5, 6

./ns.py -a "Care Quality Commission admission"                                                                       ~/Documents/Job Interviews/nhs/solutions/nhsTest
1

'''

from newssearch.newssearch import newssearch

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i',
    metavar='in-file',
    type=argparse.FileType('rt'),
    default='./test/data/hscic-news.txt')
qgroup = parser.add_mutually_exclusive_group()
qgroup.add_argument(
    '-o',
    '--or-query',
    type=str,
    help='OR query'
)
qgroup.add_argument(
    '-a',
    '--and-query',
    type=str,
    help='AND query'
)
args = parser.parse_args()

ns = newssearch(args.i)

if args.and_query:
    print ', '.join(str(i) for i in ns.andquery(args.and_query))
elif args.or_query:
    print ', '.join(str(i) for i in ns.orquery(args.or_query))
else:
    pass
