---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-3
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
In 2006, {\it Discrete and Computational Geometry} devoted an issue to the
proof of the Kepler conjecture on sphere packings, which asserts that no
packing of congruent balls in three-dimensional Euclidean space can
have density greater than that of the face-centered cubic packing \cite{Hales:2006:DCG}, \cite{Hales:2006:DCG:3}, \cite{Hales:2006:DCG:4}, \cite{Hales:2006:DCG:6}, \cite{Ferguson:2006:DCG:5}.



The proof is long and complex.  The editors' forward to that issue remarks
that ``the reviewing of these papers was a particularly enormous and daunting task.''
``The main portion of the reviewing took place in a seminar run at E\"otvos University
over a 3 year period.  Some computer experiments were done in a detailed check.
The nature of this proof, consisting in part of a large number of inequalities having
little internal structure, and a complicated proof tree, makes it hard for humans
to check every step reliably.  Detailed checking of specific assertions found them to
be essentially correct in every case tested.  The reviewing process produced in the
reviewers a strong degree of conviction of the essential correctness of the proof
approach, and that the reduction method led to nonlinear programming problems of
tractable size.''

The process of review and revision did not end when the proof was published.
This article summarizes the current status of a long-term initiative to
reorganize the original proof into a more transparent form and to provide a greater
level of certification of the correctness of the computer code and other details of the proof.  

The article contains two parts.  The first part describes
an initiative to give a formal proof of the Kepler conjecture.  The second part gives errata in the original proof of the Kepler conjecture.  Most of these errata are minor.  However, a significant new argument appears in a separate section (Section~\ref{sec:biconnected}).  It finishes an incomplete argument in the original proof asserting that there is no loss in generality in assuming (for purposes of the main estimate) that subregions are simple polygons.  The incomplete argument was detected during the preparation of the blueprint edition of the proof, which is described in Section~\ref{sec:blueprint}.

In this article, the {\it original proof} refers to the proof published
in \cite{Hales:2006:DCG}.
S. Ferguson and T. Hales take full responsibility for every possible error in the original proof of the Kepler conjecture.  Over the past decade, many have contributed significantly to making that proof more reliable.


\part{Formal Proof Initiative}
