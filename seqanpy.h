// vim:
/*
 *  Created on:	26/01/2014
 *  Author:	Fabio Zanini
 *  Contents:	Main header for the python wrapper of the SeqAn library.
 */
// Includes
#include <string>
#include  <iostream>
#include <sstream>

// Functions
int nothing();
int align_overlap(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2, int band=100);
