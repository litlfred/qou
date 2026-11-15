---
doc_id: arxiv-1011.4891v1
doc_title: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold"
section_id: sec-006-7-perspectives-new-knot-energies-for-computer-si
section_title: "§7. Perspectives: new knot energies for computer simulations"
section_number: null
pages: 16-18
source_pdf: 1011.4891.pdf
source_sha256: c3529df5dd909b5e
toc_source: inferred
doc_brief: "Mechanical Normal Forms of Knots and Flat Knots A.B.Sossinsky Independent University of Moscow Institute for Problems in Mechanics RAS Dedicated to the memory of V.I.Arnold — A new type of knot"
---
The analytical speciﬁcation of a knot energy mimicking the resilience of
our little device is ongoing joint research with Oleg Karpenkov and will be
published elsewhere.
Here we only mention that our functional is deﬁned for ﬂat knots only,
it depends on a small parameter d in the space of smooth ﬂat knots in R2;
roughly speaking, the functional is based on an “unbending force” (the larger
the curvature in the vicinity of some point, the stronger the force that tends
to straighten out the curve near that point).
For ﬂat knots, unlike “fat
knots” of cross section diameter d in space, no δ-function type of repulsive
term that does not allow diﬀerent branches of the curve to be at a distance
strictly smaller than d from each other, but allows theses branches to be at
a distance exactly equal to d, is needed.
However, because of Theorem 1, an energy functional for ﬂat knots suﬃces
to determine if two knot diagrams correspond to the same knot (i.e., are
ambient isotopic in space). To do this, compute the Whitney index of the
two knot diagrams, add an appropriate number of little loops to one of them
so as to equalize their Whitney indices and then apply the energy functional;
the given knot diagrams present the same knot if and only if the two ﬂat
normal forms obtained are identical.
Of course this works only provided that the number of crossings is small
enough to ensure uniqueness of normal forms. An optimistic prediction is
that “small” means less than 30; if this were so, we would have a fast eﬀective
algorithm for comparing knot diagrams with 30 crossings or less.
To my mind, a more interesting problem is to deﬁne other energy function-
als that do not necessarily mimic our little device. Such functionals should
include not only a δ-function-like repulsive term, but other terms related to
curvature, torsion, twisting numbers, and whatnot.
More speciﬁcally, such a functional could mimic another concrete device
with which I have performed a series of similar experiments. This new de-
17
vice is made from a thin (∼3mm) three-strand metallic cable which resists
twisting (unlike the device described in this article, it does the “belt trick”).
The corresponding functional would involve three summands: an unbending
term (related to local curvature), a repulsive term (related to the thickness of
the device), and an untwisting term (related to torsion and/or the so called
“blackboard framing” of the initial knot diagram).
Acknowledgements
I am is grateful to Elena Eﬁmova, for providing me with the device used
in the experiments (and for many other things) and to Mikhail Panov and
Victor Shuvalov, who helped with the illustrations. I also ackowledge the
support of the RFBR-CNRS-a grant #10-01-93111.
References
[1] Jun O’Hara, Energy of Knots and Conformal Geometry, World Scien-
tiﬁc, Singapore, 2003
[2] M.H.Freedman, Z.-X.He, Z.Wang, M¨obius energy of knots and un-
knots, Ann. of Math. (2) 139, 1-50, (1994)
[3] K.Ahara, Energy of a knot. video available on youtube.com
[4] Ying-Qing Wu, Polygonal knot energy, available at
http://www.uiowa.edu/∼wu/min/ming.html
[5] V.V.Prasolov, A.B.Sossinsky, Knots, Links, Braids and 3-Manifolds,
AMS Publ., Providence, R.I. 1997
[6] H.K.Moﬀat The degree of knottedness of tangled vortex lines J.Fluid
Mech. 35 (1), (1969) 117-129
[7] V.I.Arnold Asymptotic Hopf invariant and its applications [In Russian]
In the book: Proceedings of the All-Union School in Diﬀerential Equations,
Erevan, Acad. Sc. Armenian SSR (1974) 229-256.
[8] H.K.Moﬀat Magnetostatic equilibria and analogous Euler ﬂows of ar-
bitrarily complex topology, J.Fluid Mech. 159, (1985) 359-378.
[9] Jun O’Hara, Energy of a knot, Topology 30, 241-247 (1992)
[10] M.H.Freedman, Z.-X.He, Links of tori and the energy of incompress-
ible ﬂows, Topology, 30, 283-387, (1992)
[11] J.W.Milnor On the total curvature of knots, Ann. of Math. 52 (1950),
248-257.
18
[12] S.V.Matveev, Unraveling closed curves in the plane [in Russian],
Kvant, 1983, no.4, 22-28.
[13] A.Sossinsky, Wire loops on the plane [in Russian], in: Problems of
the Tournament of Towns, MCCME Publishers, Moscow, 2009
