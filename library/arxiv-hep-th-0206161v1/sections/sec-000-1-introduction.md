---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1 — 26 sections: Introduction; (1 .3); (α±"
---
The dynamics of gauge theories is a long and fascinating subj ect. The dynamics of
supersymmetric gauge theories is a subject with shorter his tory. However, more facts are
known about susy theories, and with better precision [2] yet with rich enough applications
both in physics and mathematics. In particular, the solutio n of Seiberg and Witten [3]
of N = 2 gauge theory using the constraints of special geometry of the moduli space of
vacua led to numerous achievements in understanding of the s trong coupling dynamics
of gauge theory and as well as string theory backgrounds of wh ich the gauge theories in
question arise as low energy limits. The low energy eﬀective Wilsonian action for the
massless vector multiplets (al) is governed by the prepotential F (a; Λ), which receives one-
loop perturbative and instanton non-perturbative correct ions (here Λ is the dynamically
generated scale):
F (a; Λ) = F pert(a; Λ) + F inst(a; Λ) (1 .1)
In spite of the fact that these instanton corrections were ca lculated in many indirect ways,
their gauge theory calculation is lacking beyond two instan tons[4][5]. The problem is that
the instanton measure seems to get very complicated with the growth of the instanton
charge, and the integrals are hard to evaluate.
The present paper attempts to solve this problem via the loca lization technique, pro-
posed long time ago in [1][6][7]. Although we tried to make th e paper readable to both
mathematicians and physicists we don’t expect it to be quite understandable without some
background material, which we suggest to look up in [3][8][9 ].
Notations. Let G be a semi-simple Lie group, T is maximal torus, g = Lie(G) its
Lie algebra, t = Lie(T ) its Cartan subalgebra, W = N (T )/T denote its Weyl group,
U = (t ⊗
C)/W denotes the complexiﬁed space of conjugacy classes in g. We consider the
1
moduli space Mk(G) of framed G-instantons: the anti-self-dual gauge ﬁelds A,F +
A = 0, in
the principal G-bundle P over the 4-sphere S4 = I R4 ∪ ∞ with
k = − 1
8hπ2
∫
I R4
tr FA ∧FA (1.2)
considered up to the gauge transformations g : A ↦→g−1Ag +g−1dg, s.t. g(∞) = 1. We
also consider several compactiﬁcations of the space Mk(G): the Uhlenbeck compactiﬁcation
˜Mk(G) and the Gieseker compactiﬁcation ~Mk for G = U (N ) or SU (N ). In the formula
(1.2) we use the trace in the adjoint representation, and h stands for the dual Coxeter
number of G.
Field theory description. We calculate vacuum expectation value of certain gauge
theory observables. These observables are annihilated by a combination of the super-
charges, and their expectation value is not sensitive to var ious parameters, the energy
scale in particular. Hence, one can do the calculation in the ultraviolet, where the
theory is weakly coupled and the instantons dominate. Or, on e can do the calculation
in the infrared, and relate the answer to the prepotential of the eﬀective low-energy
theory. By equating these two calculations we obtain the des ired formula.
Mathematical description. We studyG×T2 equivariant cohomology of the moduli
space ~Mk, where G acts by rotating the gauge orientation of the instantons at i nﬁnity,
and T2 is the maximal torus of SO(4) – the group of rotations of I R 4 which also acts
naturally on the moduli space 2. Let p : ~Mk →pt be the map collapsing the moduli
space to a point. We consider the following quantity:
Z(a,ǫ 1,ǫ 2;q) =
∞∑
k=0
qk
∮
~Mk
