---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-010-3-experimentation
section_title: "Experimentation"
section_number: 3
pages: 9-10
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
software.
2.6.4. An algorithm. To ﬁnd a good choice of B, we ﬁrst ﬁnd some linearly inde-
pendent basis of S (by brute force, if necessary), then express each element of S in
terms of that basis, yielding vectors in Qd (if this could not be achieved, it would
be a contradiction of Borel’s result). We then test all d-sized sets of vectors, and
select the one with the least determinant. The ratio of this determinant to the
fractional GCD of all such determinants yields the ﬁt ratio.
In our implementation, we use PARI for the lindep algorithm, and as noted in
2.6.1, we use a combination of high precision and detection of large coeﬃcients to
determine linear dependence.
Applied to the example, rational vecs is calculated as
{
(V, (1, 0)), (X, (0, 1)), (Y, (1
4,− 2
15)), (Z, (−7,−1
3))
}
,
discarding W since it is a linear multiple of V . Calculating determininants of
potential bases gives:
{V,X}→ det
[1 0
0 1
]
= 1 {V,Y}→ det
[1 4
0 − 2
15
]
=− 2
15
{V,Z}→ det
[1 −7
0 − 1
3
]
=−1
3 {X,Y}→ det
[0 4
1 − 2
15
]
= 4
{X,Z}→ det
[0 −7
1 − 1
3
]
= 7 {Y,Z}→ det
[ 4 −7
− 2
15 − 1
3
]
=−34
15.
Since 2
15 is the smallest absolute value of all possible determinants, B ={V,Y}
is returned by the algorithm. Since the fractional GCD of all possible determinants
is 1
15, the ﬁt ratio of B is 2.
10 GILLES AND HUSTON
