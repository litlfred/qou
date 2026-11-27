---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The action of the Virasoro algebra in quantum spin chains.
I. The non-rational case
Linnea Grans-Samuelsson 1, Jesper Lykke Jacobsen 1,2,3,4, and Hubert Saleur 1,5
1 Institut de Physique Th´ eorique, Universit´ e Paris Saclay, CEA, CNRS, F-91191 Gif-sur-Yvette, France
2 Laboratoire de Physique de l’ ´Ecole Normale Sup´ erieure, ENS, Universit´ e PSL,
CNRS, Sorbonne Universit´ e, Universit´ e de Paris, F-75005 Paris, France
3 Sorbonne Universit´ e,´Ecole Normale Sup´ erieure, CNRS, Laboratoire de Physique (LPENS), F-75005 Paris, France
4 Institut des Hautes ´Etudes Scientiﬁques, Universit´ e Paris Saclay, CNRS,
Le Bois-Marie, 35 route de Chartres, F-91440 Bures-sur-Yvette, France
5 Department of Physics and Astronomy, University of Southern California, Los Angeles, CA 90089, USA
Abstract
We investigate the action of discretized Virasoro generators, built out of generators of the lattice
Temperley-Lieb algebra (“Koo-Saleur generators” [1]), in the critical XXZ quantum spin chain. We ex-
plore the structure of the continuum-limit Virasoro modules at generic central charge for the XXZ vertex
model, paralleling [2] for the loop model. We ﬁnd again indecomposable modules, but this time not loga-
rithmic ones. The limit of the Temperley-Lieb modules Wj,1 for j ⁄= 0 contains pairs of “conjugate states”
with conformal weights ( hr,s, hr,−s) and ( hr,−s, hr,s) that give rise to dual structures: Verma or co-Verma
modules. The limit of W0,q±2 contains diagonal ﬁelds (hr,1, hr,1) and gives rise to either only Verma or only
co-Verma modules, depending on the sign of the exponent in q±2. In order to obtain matrix elements of
Koo-Saleur generators at large system size N we use Bethe ansatz and Quantum Inverse Scattering meth-
ods, computing the form factors for relevant combinations of three neighbouring spin operators. Relations
between form factors ensure that the above duality exists already at the lattice level. We also study in which
sense Koo-Saleur generators converge to Virasoro generators. We consider convergence in the weak sense,
investigating whether the commutator of limits is the same as the limit of the commutator? We ﬁnd that
it coincides only up to the central term. As a side result we compute the ground-state expectation value of
two neighbouring Temperley-Lieb generators in the XXZ spin chain.
Contents
1 Introduction 2
2 Discrete Virasoro algebra and the Koo-Saleur formulae 5
2.1 The Temperley-Lieb algebra in the periodic case . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.1 The algebra Ta
N(m) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.1.2 Standard modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Physical systems and the Temperley-Lieb Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Indecomposability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.4 Discrete Virasoro algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 Some features of the continuum limit 11
3.1 Modules in the continuum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 Bosonization and expected results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 The choices of metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1
arXiv:2010.12819v2  [hep-th]  22 Feb 2021
3.4 Feigin-Fuchs modules and conjugate states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4 Bethe Ansatz picture 17
4.1 Bethe-ansatz and the identiﬁcation of scaling states . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.1.1 Overlaps and mixing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.2 Conjugate states and Bethe roots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.3 Some results about form factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.3.1 Properties under conjugation and parity, implications for the modules . . . . . . . . . . . 21
5 Lattice Virasoro in the non-degenerate case 22
5.1 Koo-Saleur generators and lattice momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
5.2 Numerical results for L−1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
6 Lattice Virasoro in the degenerate case 25
6.1 Modules Wj,1 for j⁄= 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
6.2 Modules W0,q±2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7 Anomalies, and the convergence of the Koo-Saleur generators 27
7.1 “Scaling-weak” convergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.2 A closer look at limits and commutators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.2.1 The case of n⁄= 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.2.2 The case of n = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
8 Conclusions 36
A Some remarks on scalar products 36
B More on form factors 38
B.1 General framework, notations, conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
B.2 Quantum Inverse Scattering Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
B.3 The expressions for the necessary FO1,...,Oj . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
B.3.1 Fz,Fzz,F−+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
B.3.2 Fz−+, F−z+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
B.3.3 Scalar products and the homogeneous limit . . . . . . . . . . . . . . . . . . . . . . . . . . 42
C Numerical results for the degenerate case 42
C.1 The case of Wj,1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
C.1.1 Considerations at level 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
C.1.2 Form factor results for Wj,1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
C.2 The case of W0,q±2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
C.3 Relevant Bethe roots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
D Proof of (133) 49
D.1 The limit γ→ 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
E F urther numerical results for Section 7.2 50
F The chiral-antichiral commutator 53
G The ordinary XXZ case 55
G.1 Algebraic description of the ordinary XXZ case . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
G.2 Central charge and conformal weights for the ordinary XXZ case . . . . . . . . . . . . . . . . . . 56
G.3 Numerical results for the ordinary XXZ case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
G.4 Interpolation between c = 1 and c = 1− 6
x(x+1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
