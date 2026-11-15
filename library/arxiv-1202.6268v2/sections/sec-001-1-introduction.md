---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
1. Introduction
THE QUANTUM CONTENT OF THE GLUING EQUATIONS
3
1.1. The Kashaev invariant and perturbative Chern-Simons theory. The Kashaev
invariant ⟨K⟩N ∈C of a knot K in 3-space (for N = 2, 3, . . . ) is a powerful sequence of
complex numbers determined by the Jones polynomial of the knot [Jon87] and its cablings
[Tur88, Wit89]. The Volume Conjecture of Kashaev and Murakami-Murakami [Kas94, Kas95,
MM01] relates the Kashaev invariant of a hyperbolic knot K with the hyperbolic volume
Vol(M) of its complement M = S3 \ K [Thu77]
(1.1)
lim
N→∞
1
N log |⟨K⟩N| = Vol(M)
2π
.
A generalization of the Volume Conjecture [Guk05] predicts a full asymptotic expansion of
the Kashaev invariant to all orders in 1/N
(1.2)
⟨K⟩N
N→∞
∼
ZM(2πi/N)
for a suitable formal power series
(1.3)
ZM(ℏ) = exp
1
ℏSM,0 −3
2 log ℏ+ SM,1 +
X
n≥2
ℏn−1SM,n

,
ℏ= 2πi
N .
The formal power series ZM(ℏ) in (1.3) is conjectured to coincide with the perturbative par-
tition function of Chern-Simons theory with complex gauge group SL(2, C) along the discrete
faithful representation ρ0 of the hyperbolic manifold M. Combining such an interpretation
with further conjectures of [DGLZ09, Gar08, GL11] one predicts that
• SM,0 = i(VolM + iCSM) ∈C/(4π2Z) is the complexiﬁed volume of M (cf. [Thu82,
Neu92]).
• SM,1 is related [Wit91, BNW91, GM08] to the nonabelian Ray-Singer torsion [RS71],
which ought to equal (cf. [M¨ul93]) the combinatorial nonabelian Reidemeister torsion.
More precisely, [DG, Conj.1.8] we should have
(1.4)
τ R
M = 4π3 exp(−2SM,1) ∈E∗
M
where τ R
M is the nonabelian Reidemeister-Ray-Singer torsion of M with respect to
the meridian [Por97, Dub06], and EM is the invariant trace ﬁeld of M.
• For n ≥2, the n-loop invariants SM,n are conjectured to lie in the invariant trace
ﬁeld EM [DGLZ09, Gar08].
The generalization (1.2) of the Volume Conjecture has been numerically veriﬁed for a few
knots using either state-integral formulas for Chern-Simons theory when available [DGLZ09]
or a numerical computation of the Kashaev invariant and its numerical asymptotics, lifted
to algebraic numbers [GZ, Gar].
Our goal is to provide an exact, combinatorial deﬁnition of the formal power series ZM(ℏ)
via formal Gaussian integration using the shape parameters and the Neumann-Zagier ma-
trices of a regular ideal triangulation of M. Our deﬁnitions
• express the putative torsion exp(−2SM,1) and the n-loop invariants SM,n manifestly
in terms of the shape parameters zi and the gluing matrices of a regular ideal trian-
gulation T of M;
• manifestly deduce that the putative torsion and the n-loop invariants for n ≥2 are
elements of the invariant trace ﬁeld;
4
TUDOR DIMOFTE AND STAVROS GAROUFALIDIS
• explain the diﬀerence of ZM(ℏ) for pairs of geometrically similar knots studied by
Zagier and the second author;
• provide an eﬀective way to compute the n-loop invariants using standard commands
of the SnapPy toolbox [CDW] — as demonstrated for n = 1, 2, 3 for hyperbolic knots
with at most 14 crossings; and
• allow eﬃcient tests of the asymptotics of the Volume Conjecture (1.2), the “1-loop
Conjecture” (1.4) and other conjectures in Quantum Topology.
We note that we only deﬁne exp(−2SM,1) up to a sign, and SM,2 modulo Z/24. All higher
n-loop invariants are deﬁned unambiguously.
Although we give a purely combinatorial deﬁnition of ZM(ℏ) without any knowledge of
state integrals or Chern-Simons theory with complex gauge group, in Section 5 we explain
how our deﬁnition follows from the state-integral model of the ﬁrst author [Dim] and its
perturbative expansion.
