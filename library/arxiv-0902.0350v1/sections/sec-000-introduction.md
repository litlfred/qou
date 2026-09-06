---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
Part 1. F ormal Proof Initiative 3
1. The Flyspeck project 3
2. Blueprint edition of the Kepler conjecture 5
3. Formalizing the ordinary mathematics 7
4. Standard ML reimplementation of code 10
5. Proving nonlinear inequalities with Bernstein bases 12
6. Tame graph enumeration 16
7. Verifying linear programs 19
Part 2. Addendum to and Errata in the Original Proof 22
8. Biconnected graphs 22
9. Errata listing 35
References 38
1
arXiv:0902.0350v1  [math.MG]  2 Feb 2009
2 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
Introduction
In 2006,Discrete and Computational Geometrydevoted an issue to the proof
of the Kepler conjecture on sphere packings, which asserts that no packing
of congruent balls in three-dimensional Euclidean space can have density
greater than that of the face-centered cubic packing [22], [13], [14], [15], [5].
The proof is long and complex. The editors’ forward to that issue remarks
that “the reviewing of these papers was a particularly enormous and daunt-
ing task.” “The main portion of the reviewing took place in a seminar run at
E¨ otvos University over a 3 year period. Some computer experiments were
done in a detailed check. The nature of this proof, consisting in part of
a large number of inequalities having little internal structure, and a com-
plicated proof tree, makes it hard for humans to check every step reliably.
Detailed checking of specific assertions found them to be essentially cor-
rect in every case tested. The reviewing process produced in the reviewers a
strong degree of conviction of the essential correctness of the proof approach,
and that the reduction method led to nonlinear programming problems of
tractable size.”
The process of review and revision did not end when the proof was pub-
lished. This article summarizes the current status of a long-term initiative
to reorganize the original proof into a more transparent form and to provide
a greater level of certification of the correctness of the computer code and
other details of the proof.
The article contains two parts. The first part describes an initiative to
give a formal proof of the Kepler conjecture. The second part gives errata
in the original proof of the Kepler conjecture. Most of these errata are
minor. However, a significant new argument appears in a separate section
(Section8). Itfinishesanincompleteargumentintheoriginalproofasserting
that there is no loss in generality in assuming (for purposes of the main
estimate) that subregions are simple polygons. The incomplete argument
was detected during the preparation of the blueprint edition of the proof,
which is described in Section 2.
In this article, theoriginal proof refers to the proof published in [22]. S.
Ferguson and T. Hales take full responsibility for every possible error in the
original proof of the Kepler conjecture. Over the past decade, many have
contributed significantly to making that proof more reliable.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 3
Part 1. F ormal Proof Initiative
