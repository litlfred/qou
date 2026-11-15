---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-001-1-conventions-and-notations
section_title: "Conventions and notations"
section_number: 1
pages: 1-3
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
Conventions and notations
3
2.
Quantum invariants and Hopf diagrams
5
3.
Hopf monads
11
4.
Quantum double of Hopf monads
14
5.
Reshetikhin-Turaev invariants from categorical centers
16
References
19
Introduction
In the early 90’s, two new ‘quantum’ invariants of 3-manifolds were introduced:
the Reshetikhin-Turaev invariant, and the Turaev-Viro invariant. The deﬁnition
of the Reshetikhin-Turaev invariant RTB [RT91, Tur94] involves a modular cate-
gory B, that is, a ribbon fusion category over a commutative ring k satisfying a
non-degeneracy condition (invertibility of the S-matrix). The algorithm for com-
puting its value on a 3-manifold consists in presenting the manifold by surgery
along a ribbon link and then taking a linear combination of colorings of this link
by simple objects of B.
Similarly, the deﬁnition of the Turaev-Viro invariant TVC [TV92], as revisited
by Barrett and Westbury [BW96], involves a spherical category, that is, a sovereign
fusion category over a commutative ring k such that left and right traces coincide.
Date: November 3, 2018.
2000 Mathematics Subject Classiﬁcation. 57M27,16W30,18C20.
The second author thanks the organizers of the International Conference on Quantum Topology
held at the Institute of Mathematics of Hanoi (Vietnam) in August 2007.
This paper is an
enhanced version of the talk he gave there.
1
2
A. BRUGUI`ERES AND A. VIRELIZIER
The dimension dim C of C (which is the sum of squares of dimensions of simple
objects) is moreover assumed to be invertible in k. The algorithm for computing
TVC(M) consists in presenting the 3-manifold M by a triangulation, coloring the
edges of the triangulation with simple objects of C, and then evaluating the colored
tetrahedra by means of the 6j-symbols of C.
If B is a modular category, then it is also a spherical category, and the Reshetikhin-
Turaev and Turaev-Viro invariants are related [Tur94, Ro95] by:
TVB(M) = RTB(M)RTB(−M)
for any 3- manifold M, where −M is the 3-manifold M with opposite orientation.
But in general a spherical category need not to be braided and so cannot be
used as input to deﬁne the Reshetikhin-Turaev invariant. However, spherical and
modular categories are related by a theorem of M¨uger [M¨u03]: if C is a spherical
fusion category over an algebraically closed ﬁeld k and has invertible dimension,
then its center Z(C) is a modular fusion category of dimension dim Z(C) = (dim C)2.
In this setting, Turaev conjectured that, for any 3-manifold M,
TVC(M) = RTZ(C)(M).
This conjecture was shown to be true for some spherical categories C arising from
subfactors, see [KSW05]. The general case is still open.
In this context, a natural question is: how can we compute RTZ(C)(M)? Using
the algorithm given by Reshetikhin and Turaev is not a practicable approach here,
as that would require a description of the simple objects of Z(C) in terms of those
of C, and no such description is available in general. What we need is a diﬀerent
algorithm for computing RTZ(C)(M), which one should be able to perform inside C,
without reference to the simple objects of Z(C). This is the primary objective of
this paper.
In order to fulﬁll this objective, it will be convenient to adopt an alterna-
tive approach for constructing RT-like quantum invariants of 3-manifolds, due to
Lyubashenko [Lyu95] and later developed in [KL01, Vir06], where the input data
is a (non-necessarily linear neither semisimple) ribbon category B which admits a
coend C = R X∈B ∨X ⊗X. This coend C is naturally endowed with a very rich
algebraic structure. In particular, it is a Hopf algebra in the braided category B
and comes equipped with a Hopf pairing ω: C ⊗C →
1. Such a category B is
modular if the pairing ω is non-degenerate (this is the natural way of formulating
the invertibility of the S-matrix in this setting).
The construction of the Lyubashenko invariant consists in presenting the 3-man-
ifold by surgery along a ribbon link L, using the universal property of the coend C
to associate a form φL to the link, and then evaluating this form on an integral Λ
of the Hopf algebra C. Note that, more generally, one can evaluate the form φL
by a ‘Kirby element’ α of B to get other invariants τB(M; α) of 3-manifold invari-
ants, see [Vir06]. In particular, up to normalization, τB(M; Λ) is the Lyubashenko
invariant and, in the special case where B is a modular fusion category, τB(M; Λ)
is the Reshetikhin-Turaev invariant.
In order to make this construction eﬀective, we need an algorithm for computing
the forms φL which are deﬁned by universal property. Such an algorithm, based
on an encoding of certain tangles by means of Hopf diagrams, is given in [BV05].
Thus the invariants τB(M; α) can be expressed in terms of certain structural mor-
phisms of the coend C. Section 2 is devoted to these quantum invariants and their
computation.
Hence, when C is a spherical fusion category, we may compute τZ(C)(M; Λ) pro-
vided we can describe explicitly the structural morphisms of the coend of Z(C). In
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS
3
other words, we need an algebraic interpretation of the center construction. If C
is braided and has a coend A (which is a Hopf algebra), then the category Z(C)
coincides with the category of (right) A-modules in C. However the diﬃculty here
is that we don’t want to assume C is braided. To bypass this diﬃculty, we use the
notion of Hopf monad introduced in [BV07].
Hopf monads generalize Hopf algebras in a non-braided setting.
In particu-
lar, ﬁnite-dimensional Hopf algebras and their diﬀerent generalizations (Hopf al-
