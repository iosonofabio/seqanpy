#include "seqanpy.h"
#include <seqan/align.h>

using namespace seqan;


// Functions
int align_global(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2, int band,
                 int score_match, int score_mismatch, int score_gapext, int score_gapopen) {

	typedef String<char> TSequence;                 // sequence type
	typedef Align<TSequence,ArrayGaps> TAlign;      // align type
	typedef Row<TAlign>::Type TRow;                 // gapped sequence type
	std::stringstream rowstream;
	int score;

	// Build alignment object
	TAlign ali;
        resize(rows(ali), 2);
	assignSource(row(ali, 0), seq1);
	assignSource(row(ali, 1), seq2);

	// Align
	if(band >= 0)
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen),
					-band, band);
	else
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen));

	// Set the output
	TRow row1 = row(ali,0);
	rowstream.str("");
	rowstream << row1;
	(*ali1) = rowstream.str();

	TRow row2 = row(ali,1);
	rowstream.str("");
	rowstream << row2;
	(*ali2) = rowstream.str();

	return score;
}


int align_overlap(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2, int band,
                 int score_match, int score_mismatch, int score_gapext, int score_gapopen) {

	typedef String<char> TSequence;                 // sequence type
	typedef Align<TSequence,ArrayGaps> TAlign;      // align type
	typedef Row<TAlign>::Type TRow;                 // gapped sequence type
	std::stringstream rowstream;
	int score;

	// Build alignment object
	TAlign ali;
        resize(rows(ali), 2);
	assignSource(row(ali, 0), seq1);
	assignSource(row(ali, 1), seq2);

	// Align
	if(band >= 0)
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen),
					AlignConfig<true, false, false, true>(),
					-band, band);
	else
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen),
					AlignConfig<true, false, false, true>());

	// Set the output
	TRow row1 = row(ali,0);
	rowstream.str("");
	rowstream << row1;
	(*ali1) = rowstream.str();

	TRow row2 = row(ali,1);
	rowstream.str("");
	rowstream << row2;
	(*ali2) = rowstream.str();

	return score;
}


int align_ladder(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2, int band,
                 int score_match, int score_mismatch, int score_gapext, int score_gapopen) {

	typedef String<char> TSequence;                 // sequence type
	typedef Align<TSequence,ArrayGaps> TAlign;      // align type
	typedef Row<TAlign>::Type TRow;                 // gapped sequence type
	std::stringstream rowstream;
	int score;

	// Build alignment object
	TAlign ali;
        resize(rows(ali), 2);
	assignSource(row(ali, 0), seq1);
	assignSource(row(ali, 1), seq2);

	// Align
	if(band >= 0)
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen),
					AlignConfig<true, false, true, false>(),
					-band, band);
	else
		score = globalAlignment(ali,
					Score<int,Simple>(score_match, score_mismatch,
                                                          score_gapext, score_gapopen),
					AlignConfig<true, false, true, false>());

	// Set the output
	TRow row1 = row(ali,0);
	rowstream.str("");
	rowstream << row1;
	(*ali1) = rowstream.str();

	TRow row2 = row(ali,1);
	rowstream.str("");
	rowstream << row2;
	(*ali2) = rowstream.str();

	return score;
}


int align_local(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2,
                 int score_match, int score_mismatch, int score_gapext, int score_gapopen) {

	typedef String<char> TSequence;                 // sequence type
	typedef Align<TSequence,ArrayGaps> TAlign;      // align type
	typedef Row<TAlign>::Type TRow;                 // gapped sequence type
	std::stringstream rowstream;
	int score;

	// Build alignment object
	TAlign ali;
        resize(rows(ali), 2);
	assignSource(row(ali, 0), seq1);
	assignSource(row(ali, 1), seq2);

        // Align (best alignment only)
        score = localAlignment(ali,
                               Score<int,Simple>(score_match, score_mismatch,
                                                 score_gapext, score_gapopen));

	// Set the output
	TRow row1 = row(ali,0);
	rowstream.str("");
	rowstream << row1;
	(*ali1) = rowstream.str();

	TRow row2 = row(ali,1);
	rowstream.str("");
	rowstream << row2;
	(*ali2) = rowstream.str();

        return score;
}
