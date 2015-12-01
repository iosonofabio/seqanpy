// vim:
/*
 *  Created on:	26/01/2014
 *  Author:	Fabio Zanini
 *  Contents:	Main header for the python wrapper of the SeqAn library.
 */
// Includes
#include <string>
#include <iostream>
#include <sstream>

// Functions
int nothing();

int align_global(std::string seq1, std::string seq2,
                 std::string* aliout1, std::string* aliout2, int band=100,
                 int score_match=3, int score_mismatch=-3,
                 int score_gapext=-1, int score_gapopen=-5);


int align_overlap(std::string seq1, std::string seq2,
                  std::string* aliout1, std::string* aliout2, int band=-1,
                  int score_match=3, int score_mismatch=-3,
                  int score_gapext=-1, int score_gapopen=-5);


int align_ladder(std::string seq1, std::string seq2,
                 std::string* aliout1, std::string* aliout2, int band=-1,
                 int score_match=3, int score_mismatch=-3,
                 int score_gapext=-1, int score_gapopen=-5);


int align_local(std::string seq1, std::string seq2,
                std::string* aliout1, std::string* aliout2,
                int score_match=3, int score_mismatch=-3,
                int score_gapext=-1, int score_gapopen=-5);
