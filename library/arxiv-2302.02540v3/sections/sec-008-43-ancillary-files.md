---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-008-43-ancillary-files
section_title: "Ancillary files"
section_number: 4.3
pages: 8-9
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
we explain how to estimate these integrals in the proof and state the resulting estimate
that was obtained using interval arithmetic inSageMath. The calculations behind these es-
timates are all contained in theJupyternotebookcertified integrals.ipynbattached
as an ancillary file to the arXiv version of this paper.
Then there is one fileverify invariant.ipynbfor each of the invariants we consider.
Each such file contains a functioninvariant polywhich computes a pair of polynomials
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 9
(p,q) such thatf(x) =p(x 2)e−x2/2 and bf(x) =q(x 2)e−x2/2 are the Fourier transform of
one another given a list of double zeros for each and perhaps additional data. Another
functioninvariant verifychecks that all the required conditions onfand bfare satisfied
and outputs a resulting rigorous upper bound on the invariant in question. The lists of
input parameters that we used to produce the bounds in Tables 1 to 7 are stored in various
filesparameters invariant.sobjthat are loaded in the last cell of theverify invariant
notebook. Upon execution of this last cell, the program runs theinvariant verifyfunc-
tion on each of these input parameters and prints out the resulting bounds.
