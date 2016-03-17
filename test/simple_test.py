# vim: fdm=indent
'''
author:     Fabio Zanini
date:       16/03/16
content:    Import test for seqanpy
'''
# Modules
from __future__ import print_function


# Tests
def import_test():
    print('Test import')
    import seqanpy
    assert 1 == 1


def global_test():
    print('Test align_global')
    import seqanpy
    (score, ali1, ali2) = seqanpy.align_global('ACCGT', 'AGT')
    assert ali1 == 'ACCGT'
    assert ali2 == 'A--GT'


def overlap_test():
    print('Test align_overlap')
    import seqanpy
    (score, ali1, ali2) = seqanpy.align_overlap('ACCGT', 'CCG')
    assert ali1 == 'ACCGT'
    assert ali2 == '-CCG-'


def overlap_ladder():
    print('Test align_ladder')
    import seqanpy
    (score, ali1, ali2) = seqanpy.align_ladder('ACCGT', 'CGTAA')
    assert ali1 == 'ACCGT--'
    assert ali2 == '--CGTAA'

