---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-001-the-hurwitz-topological-quantum-field-theory
section_title: "The Hurwitz Topological Quantum Field Theory"
section_number: null
pages: 2-4
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
---
The Hurwitz Topological Quantum Field Theory
2
2.1
The Hurwitz Theory at Fixed Degree . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
The Extended Hurwitz Theory . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.3
The String Dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
3
From Two-dimensional Yang-Mills to Hurwitz
7
3.1
The Observables of Two-dimensional Yang-Mills Theory
. . . . . . . . . . . .
8
3.2
The Schur-Weyl Dictionary
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.3
The Gross-Taylor Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.4
Chiral Yang-Mills Theory as a Deformed Hurwitz Theory . . . . . . . . . . . .
12
4
The Stringy Structure of Chiral Yang-Mills Theory
14
4.1
A Double Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.2
Vertex Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.3
A Stringy Deformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
5
A Deformed Gromov-Witten Theory
18
5.1
The Partial Permutation Algebra of Yang-Mills Theory . . . . . . . . . . . . .
18
5.2
The Duality Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5.3
The Gromov-Witten Formulation . . . . . . . . . . . . . . . . . . . . . . . . .
20
5.4
The Inverse Map
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
5.5
Remarks on Wilson Loops . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
6
Conclusions
24
A Useful Identities
25
B Determining the Dictionary
25
C Phase Transitions
26
C.1 Analytical Phase Transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
C.2 Numerical Phase Transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
1
Introduction
Two-dimensional Yang-Mills theory provides an interesting case study for the proposed rela-
tion between large N gauge theory and string theory [1–5]. For a gauge theory with gauge
group U(N), one can rearrange the Feynman diagram expansion of observables in an ex-
pansion in terms of the genus of a Riemann surface that one would like to interpret as the
world-sheet of a string [1]. Formulating the corresponding string theory from first principles
1
is a challenge. Topological string theory proposals exist for the dual of two-dimensional Yang-
Mills theory [6, 7]. See also [8] for a recent contribution on how to describe the dual string
theory in more detail.
In this paper, we wish to increase the conceptual clarity of the correspondence between
two-dimensional Yang-Mills theory and a topological string theory. The main point will be to
provide a dual string theory which is of a canonical form, namely a deformed Gromov-Witten
theory. The latter has a standard definition that includes an integral over the moduli space
of Riemann surfaces. The manner in which we attain the string theory dual is through a
known rewriting of the gauge theory, combined with a relation between a second quantized
symmetric group gauge theory and Gromov-Witten theory [9, 10]. One essential ingredient
which distinguishes our approach from the literature is the treatment of the Ωpoints and of
the transpositions. They are both viewed as finite deformations of the string theory which
respectively modify the moduli space and introduce extra string interactions.
The plan of the paper is as follows. In section 2, we review the necessary background on
the Hurwitz topological quantum field theory of Sd principal bundles on Riemann surfaces.
We review its grand canonical version that treats all degrees d of covering maps simultaneously
and how the grand canonical theory corresponds to a Gromov-Witten theory [9,10]. In section
3, we review the rewriting of the two-dimensional Yang-Mills partition functions in terms of a
sum of contributions of degree d covering maps described by Hurwitz theories [2–5]. We argue
that boundary holonomies play a role similar to local observables, much like in topological
field theories. We provide an explicit map between the Hurwitz observables and those of
two-dimensional Yang-Mills theory. We think of the Ωoperator as well as the transposition
operator as deformations in the grand canonical Hurwitz theory.
In section 4, we clarify the stringy nature of the chiral Yang-Mills theory and prove that
the treatment of Ωoperators and transposition operators as deformations is consistent with its
string theoretic structure. In section 5, we argue that the algebra underlying the chiral Yang-
Mills theory is an algebra of partial permutations. We exploit the correspondence between
Hurwitz theory and the stationary sector of Gromov-Witten theory. This enables us to express
Yang-Mills correlators as observables of a string theory, which is a Gromov-Witten theory
deformed by a number of operators that describe a modification of the moduli space as well
as extra string interactions. We conclude in section 6 with a brief description of our findings,
connections with the AdS3 literature, and further open questions.
Appendix A is a collection of useful identities for symmetric polynomials. Appendix B
contains an explicit proof of the dictionary of observables we provide in section 5. Finally,
appendix C is an application of our perspective in that it naturally suggests a phase diagram
for the deformed string theory that generalizes the stringy phase transition of [11–13] to a
case with two extra parameters.
2
The Hurwitz Topological Quantum Field Theory
In this section, we review the Hurwitz topological field theory.
It is a two-dimensional
Dijkgraaf-Witten theory [14] with gauge group Sd. The grand canonical version of this theory
is dual to a string theory [9, 10]. We describe the string theory concretely as the stationary
subsector of a matter model coupled to gravity. We also discuss the relation between the
relative Gromov-Witten dual and the introduction of boundaries.
2
