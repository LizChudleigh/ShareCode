#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

def calculate_percentage(seq):
    total_bases = len(seq)
    a_count = seq.count('A')
    c_count = seq.count('C')
    g_count = seq.count('G')
    t_count = seq.count('T')
    u_count = seq.count('U')  # Count 'U' for RNA

    a_percentage = (a_count / total_bases) * 100
    c_percentage = (c_count / total_bases) * 100
    g_percentage = (g_count / total_bases) * 100

    if 'T' in seq:
        t_percentage = (t_count / total_bases) * 100
        return a_percentage, c_percentage, g_percentage, t_percentage
    elif 'U' in seq:
        u_percentage = (u_count / total_bases) * 100
        return a_percentage, c_percentage, g_percentage, u_percentage
    else:
        return a_percentage, c_percentage, g_percentage

parser = ArgumentParser(description='Classify a sequence and calculate base percentages')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()

if 'T' in args.seq and 'U' in args.seq:
    print('The sequence is not DNA nor RNA (both T and U present)')
else:
    a_percent, c_percent, g_percent, t_or_u_percent = calculate_percentage(args.seq)
    
    print(f'A percentage: {a_percent:.2f}%')
    print(f'C percentage: {c_percent:.2f}%')
    print(f'G percentage: {g_percent:.2f}%')
    
    if 'T' in args.seq:
        print(f'T percentage: {t_or_u_percent:.2f}% (DNA)')
    elif 'U' in args.seq:
        print(f'U percentage: {t_or_u_percent:.2f}% (RNA)')
