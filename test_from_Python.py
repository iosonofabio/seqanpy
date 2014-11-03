# vim: fdm=marker
'''
author:     Fabio Zanini
date:       30/01/14
content:    Test of the seqanpy module from Python.
'''
# Modules


# Script
if __name__ == '__main__':

    # Try import
    import seqanpy as sap

    # Global pairwise alignment
    seq1 = 'AAAGGTCTA'
    seq2 = 'AAATCGA'
    output = sap.align_global(seq1, seq2, band=5)
    print output

    # Overlap pairwise alignment
    seq1 = 'AAAGGTCTA'
    seq2 = 'ATCT'
    output = sap.align_overlap(seq1, seq2)
    print output

    # Ladder pairwise alignment
    seq1 = 'AAAGGTCTA'
    seq2 = 'TCTAGGGAAACCC'
    output = sap.align_ladder(seq1, seq2)
    print output

    # Local pairwise alignment
    seq1 = 'AAAGGTCTACCGTAGCCT'
    seq2 = 'AAGTCTAC'
    output = sap.align_local(seq1, seq2)
    print output
