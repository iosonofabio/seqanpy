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
%typemap(in, numinputs=0) std::string *aliout(std::string temp) {
    $1 = &temp;
}
%typemap(argout) std::string *aliout {
    PyObject *alipy;
    alipy = PyString_FromString((*$1).c_str());

    /* If the result is not a long and not a tuple, bad! */
    if ((!$result) || ($result == Py_None)) {
        $result = alipy;
    } else {

        /* After the first output arg, we have a long, make a triple */        
        if (!PyTuple_Check($result)) {
                PyObject *score = $result;
                $result = PyTuple_New(3);
                PyTuple_SetItem($result, 0, score);
                PyTuple_SetItem($result, 1, alipy);

        /* After the second arg, we have a triple already */
        } else
                PyTuple_SetItem($result, 2, alipy);
    }

    /* NOTE: all Python objects are still in use at the end,
             so no need to reduce their refcount */
}

/* HEADER with changed input variable names to fit typemaps (this is C.R.A.P.) */
int nothing();
int align_overlap(std::string seq1, std::string seq2, std::string* aliout, std::string* aliout, int band=100);
