/*
 *  Created on:	26/01/2014
 *  Author:	Fabio Zanini
 *  Contents:	SWIG file for the seqanpy Python wrapper of SeqAn
 */
%module seqanpy

%{
#define SWIG_FILE_WITH_INIT
#include "seqanpy.h"
%}

/* STL types */
%include "std_string.i"

/* SEQANPY */
/* convert any Python input to string before passing down to C++ (duck typing) */
%pythonprepend align_global %{
    seq1 = ''.join(seq1)
    seq2 = ''.join(seq2)
%}
%pythonprepend align_overlap %{
    seq1 = ''.join(seq1)
    seq2 = ''.join(seq2)
%}
%pythonprepend align_ladder %{
    seq1 = ''.join(seq1)
    seq2 = ''.join(seq2)
%}
%pythonprepend align_local %{
    seq1 = ''.join(seq1)
    seq2 = ''.join(seq2)
%}

/* "output" string pointers */
%typemap(in, numinputs=0) std::string *aliout1(std::string temp) {
    $1 = &temp;
}
%typemap(in, numinputs=0) std::string *aliout2(std::string temp) {
    $1 = &temp;
}
%typemap(argout) std::string *aliout1 {
    PyObject *alipy = PyString_FromString((*$1).c_str());

    /* $result should be the C++ return value (score) */
    PyObject *score = $result;
    $result = PyTuple_New(3);
    PyTuple_SetItem($result, 0, score);
    PyTuple_SetItem($result, 1, alipy); 

    /* NOTE: all Python objects are still in use at the end,
             so no need to reduce their refcount */
}
%typemap(argout) std::string *aliout2 {
    PyObject *alipy = PyString_FromString((*$1).c_str());

    /* $result should already be a tuple by now */
    PyTuple_SetItem($result, 2, alipy); 
}

/* Documentation */
%feature("autodoc", "0");
%feature("docstring") align_global
"Global alignment of two sequences.

Parameters:
   seq1: string with the first seq
   seq2: string with the second seq
   band: make banded alignment, maximal shear between the sequences (-1 to turn off)
   score_...: scores for the alignment
";

%feature("docstring") align_overlap
"Align a subsequence onto a longer, reference one.

Parameters:
   seq1: string with the reference seq
   seq2: string with the subsequence (end gaps are free)
   band: make banded alignment, maximal shear between the sequences (-1 to turn off)
   score_...: scores for the alignment

Note: band counts also gaps at the edges, so it must be used with care.
";

%feature("docstring") align_ladder
"Align two sequences where the second is an overlapping extension of the first.

Parameters:
   seq1: string to be extended (end gaps are free)
   seq2: string to use for extension (start gaps are free)
   band: make banded alignment, maximal shear between the sequences (-1 to turn off)
   score_...: scores for the alignment

Note: band counts also gaps at the edges, so it must be used with care.
";

%feature("docstring") align_local
"Local alignment of two strings.

Parameters:
   seq1: string with the first seq
   seq2: string with the second seq
   score_...: scores for the alignment
";


/* HEADER */
%include "seqanpy.h"
