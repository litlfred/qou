---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-11
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Properties of Eigenvalues on Riemann
Surfaces with Large Symmetry Groups
by
Joseph Cook
A Doctoral Thesis
Submitted in partial fulﬁllment of the requirements
for the award of
Doctor of Philosophy of Loughborough University
December 2, 2018
c⃝by Joseph Cook, 2018
Abstract
On compact Riemann surfaces, the Laplacian ∆has a discrete, non-negative spectrum of
eigenvalues {λi} of ﬁnite multiplicity. The spectrum is intrinsically linked to the geometry
of the surface. In this work, we consider surfaces of constant negative curvature with a
large symmetry group. It is not possible to explicitly calculate the eigenvalues for surfaces
in this class, so we combine group theoretic and analytical methods to derive results about
the spectrum.
In particular, we focus on the Bolza surface and the Klein quartic. These have the high-
est order symmetry groups among compact Riemann surfaces of genera 2 and 3 respec-
tively. The full automorphism group of the Bolza surface is isomorphic to GL2(Z3) ⋊Z2;
in Chapter 3 we analyze the irreducible representations of this group and prove that the
multiplicity of λ1 is 3, building on the work in [41], and identify the irreducible represen-
tation that corresponds to this eigenspace. This proof relies on a certain conjecture, for
which we give substantial numerical evidence and a hopeful method for proving. We go
on to show that λ2 has multiplicity 4.
The full automorphism group of the Klein quartic is isomorphic to PGL2(Z7) ⋊Z2. In
Chapter 4 we give some preliminary results about the surface, including a calculation of
its systole length and Fenchel-Nielsen coordinates, and prove that the multiplicity of λ1
for the Klein quartic is 6, 7, or 8. In the appendices, we include numerical computations
of eigenvalues for the Bolza surface, the Klein quartic, and other interesting hyperbolic
surfaces, such as the Fermat quartic.
ii
Acknowledgements
I am indebted to my supervisor Alexander Strohmaier for providing me with an interesting
project that I have enjoyed from the start, and for introducing me to several fascinating
areas of mathematics. His encouragement, expertise, and patience in explaining and re-
explaining key areas of subject matter have been invaluable in the production of this
work. I am grateful to Eugenie Hunsicker for the beneﬁcial advice and feedback she has
given me at yearly progress review meetings, which has been imperative in shaping this
thesis. I would like to thank Claudia Garetto for agreeing to co-supervise this project,
and for checking the ﬁnal draft.
I am grateful for the support and friendship of my fellow PhD students, both at
Loughborough University and the University of Leeds. The discussions and opportuni-
ties to present my work to my peers have kept me motivated throughout my time as a
postgraduate, and have vastly improved my conﬁdence in speaking about mathematics.
I would like to thank the EPSRC for providing ﬁnancial support throughout my period
of study, as well as the Loughborough University School of Science, and University of
Leeds School of Mathematics, for facilitating and ﬁnancing my trips to various conferences
over the past three and a half years. Furthermore, I would like to thank the School
of Mathematics at the University of Leeds for hosting me when I moved here with my
supervisor. They have given me all the beneﬁts of a full University of Leeds PhD student,
for which I am beholden.
I would like to thank the providers of free software: notably, FreeFEM++ and GAP.
These programs have vastly enriched the theoretical work I have done. In particular,
images produced in FreeFEM++ have been an asset when presenting my work at confer-
ences and seminars.
Finally, I would like to acknowledge that the completion of this research project would
not have been possible without the continued love and support my family and close
friends.
iv
Dedicated to Alice
vi
Contents
1
Introduction
1
2
Background
25
2.1
Spectral theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.2
Hyperbolic geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
2.3
Harmonic analysis on H
. . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.4
Representation theory
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
2.5
Selberg’s trace formula . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
3
The Bolza Surface
50
3.1
Symmetry group of the Bolza surface . . . . . . . . . . . . . . . . . . . .
50
3.2
Length spectrum of the Bolza surface . . . . . . . . . . . . . . . . . . . .
55
3.3
Upper bounds on eigenvalues of the Bolza surface . . . . . . . . . . . . .
56
3.4
First eigenspace of the Bolza surface
. . . . . . . . . . . . . . . . . . . .
64
3.5
Second eigenspace of Bolza surface
. . . . . . . . . . . . . . . . . . . . .
85
4
The Klein Quartic
88
4.1
Systole of the Klein quartic
. . . . . . . . . . . . . . . . . . . . . . . . .
88
4.2
Fenchel-Nielsen parameters of the Klein quartic
. . . . . . . . . . . . . .
90
4.3
Spectral theory of the Klein quartic . . . . . . . . . . . . . . . . . . . . .
93
5
Concluding Remarks
98
A GAP Code for Bolza Surface
101
B GAP Code for Klein Quartic
105
C FreeFEM++ Code for Genus 2
108
D FreeFEM++ Code for Genus 3
120
viii
E FreeFEM++ Code for Genus 4
134
F Mathematica Code for Bolza Surface
140
G Alternative approach to proving Conjecture 3.12
143
ix
Chapter 1
