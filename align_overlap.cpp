#include "seqanpy.h"
#include <seqan/align.h>

using namespace seqan;

int align_overlap(std::string seq1, std::string seq2, std::string* ali1, std::string* ali2, int band) {

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
					Score<int,Simple>(1,-1,-1),
					AlignConfig<true, false, false, true>(),
					-band, band);
	else
		score = globalAlignment(ali,
					Score<int,Simple>(1,-1,-1),
					AlignConfig<true, true, true, true>());

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
