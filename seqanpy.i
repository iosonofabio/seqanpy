/*
 *  Created on:	26/01/2014
 *  Author:	Fabio Zanini
 *  Contents:	Test implementation file
 */
%module seqanpy

%{
#define SWIG_FILE_WITH_INIT
#include "seqanpy.h"
%}

/* STL types */
%include "std_string.i"

/* SEQANPY (move to a separate file?) */
/* align_overlap */
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
   seq1: string with the mother seq
   seq2: string with the child subseq
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
