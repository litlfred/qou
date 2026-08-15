---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-001-11-the-kashaev-invariant-and-perturbative-chern
section_title: "The Kashaev invariant and perturbative Chern-Simons theory"
section_number: 1.1
pages: 1-4
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
1.2. The Neumann-Zagier datum 4
1.3. The 1-loop invariant 5
1.4. Expectations 6
1.5. The higher-loop invariants 6
1.6. Feynman diagrams 8
1.7. The 2-loop invariant 8
1.8. The 3-loop invariant 9
1.9. Generalizations 10
Date: October 25, 2012.
The work of SG is supported by NSF grant DMS-11-05678. The work of TD is supported primarily by
the Friends of the Institute for Advanced Study, and in part by DO E grant DE-FG02-90ER40542.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M25.
Key words and phrases: volume, complex Chern-Simons theory , Kashaev invariant, gluing equations,
Neumann-Zagier equations, Neumann-Zagier datum, hyperbo lic geometry, ideal triangulations, 1-loop,
torsion, quantum dilogarithm, state-integral, perturbat ion theory, Feynman diagrams, formal Gaussian
integration.
1
2 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Acknowledgment 10
2. Mechanics of triangulations 10
2.1. Ideal tetrahedra 11
2.2. The gluing matrices 11
2.3. The Neumann-Zagier matrices 12
2.4. Combinatorial ﬂattenings 13
2.5. The shape solutions to the gluing equations 14
2.6. Example: 41 14
3. Topological invariance of our torsion 15
3.1. Example: 41 continued 16
3.2. Independence of a choice of quad type 16
3.3. Independence of a choice of edge 17
3.4. Independence of a choice of meridian path 18
3.5. Independence of a choice of ﬂattening 19
3.6. Invariance under 2–3 moves 19
4. Torsion on the character variety 22
4.1. A review of ρ-regular ideal triangulations 23
4.2. The Epstein-Penner cell decomposition and its triangulations 23
4.3. Neumann-Zagier datum and the geometric component 24
4.4. Flattening compatible with a longitude 25
4.5. Invariance of the generalized torsion 26
4.6. Example: 41 continued 27
5. The state integral and higher loops 29
5.1. Critical points 30
5.2. Volume 32
5.3. Torsion revisited 33
5.4. Feynman diagrams and higher loops 33
5.5. n-loop invariants on the character variety 35
5.6. Example: 41 completed 37
Appendix A. Symplectic properties of A and B 37
Appendix B. The shape parameters are rational functions on the c haracter variety 39
Appendix C. Deriving the state integral 40
C.1. Symplectic gluing 40
C.2. Quantization 41
C.3. Quantum reduction 42
C.4. Introducing a ﬂattening 44
C.5. Normalization and invariance 44
Appendix D. Computer implementation and computations 46
References 47
1. Introduction
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 3
1.1. The Kashaev invariant and perturbative Chern-Simons theor y. The Kashaev
invariant⟨K⟩N ∈ C of a knot K in 3-space (for N = 2, 3,... ) is a powerful sequence of
complex numbers determined by the Jones polynomial of the knot [ Jon87] and its cablings
[Tur88, Wit89]. The Volume Conjectureof Kashaev and Murakami-Murakami [Kas94, Kas95,
MM01] relates the Kashaev invariant of a hyperbolic knot K with the hyperbolic volume
Vol(M) of its complement M =S3\K [Thu77]
(1.1) lim
N →∞
1
N log|⟨K⟩N| = Vol(M)
2π .
A generalization of the Volume Conjecture [ Guk05] predicts a full asymptotic expansion of
the Kashaev invariant to all orders in 1 /N
(1.2) ⟨K⟩N
N →∞
∼ ZM (2πi/N)
for a suitable formal power series
(1.3) ZM (ℏ) = exp
(1
ℏSM, 0− 3
2 log ℏ +SM, 1 +
∑
n≥2
ℏn−1SM,n
)
, ℏ = 2πi
N .
The formal power series ZM (ℏ) in ( 1.3) is conjectured to coincide with the perturbative par-
tition function of Chern-Simons theory with complex gauge group SL (2, C) along the discrete
faithful representation ρ0 of the hyperbolic manifold M. Combining such an interpretation
with further conjectures of [ DGLZ09, Gar08, GL11] one predicts that
• SM, 0 = i(VolM +iCSM )∈ C/(4π2Z) is the complexiﬁed volume of M (cf. [Thu82,
Neu92]).
• SM, 1 is related [ Wit91, BNW91, GM08] to the nonabelian Ray-Singer torsion [ RS71],
which ought to equal (cf. [M¨ ul93]) the combinatorial nonabelian Reidemeister torsion.
More precisely, [ DG, Conj.1.8] we should have
(1.4) τ R
M = 4π3 exp(−2SM, 1)∈E∗
M
where τ R
M is the nonabelian Reidemeister-Ray-Singer torsion of M with respect to
the meridian [ Por97, Dub06], and EM is the invariant trace ﬁeld of M.
• For n≥ 2, the n-loop invariants SM,n are conjectured to lie in the invariant trace
ﬁeld EM [DGLZ09, Gar08].
The generalization ( 1.2) of the Volume Conjecture has been numerically veriﬁed for a few
knots using either state-integral formulas for Chern-Simons the ory when available [ DGLZ09]
or a numerical computation of the Kashaev invariant and its numeric al asymptotics, lifted
to algebraic numbers [ GZ, Gar].
Our goal is to provide an exact, combinatorial deﬁnition of the form al power seriesZM (ℏ)
via formal Gaussian integration using the shape parameters and th e Neumann-Zagier ma-
trices of a regular ideal triangulation of M. Our deﬁnitions
• express the putative torsion exp( −2SM, 1) and the n-loop invariants SM,n manifestly
in terms of the shape parameters zi and the gluing matrices of a regular ideal trian-
gulationT of M;
• manifestly deduce that the putative torsion and the n-loop invariants for n≥ 2 are
elements of the invariant trace ﬁeld;
4 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
• explain the diﬀerence of ZM (ℏ) for pairs of geometrically similar knots studied by
Zagier and the second author;
• provide an eﬀective way to compute the n-loop invariants using standard commands
of the SnapPy toolbox [ CDW] — as demonstrated for n = 1, 2, 3 for hyperbolic knots
with at most 14 crossings; and
• allow eﬃcient tests of the asymptotics of the Volume Conjecture ( 1.2), the “1-loop
Conjecture” ( 1.4) and other conjectures in Quantum Topology.
We note that we only deﬁne exp( −2SM, 1) up to a sign, and SM, 2 modulo Z/24. All higher
n-loop invariants are deﬁned unambiguously.
Although we give a purely combinatorial deﬁnition of ZM (ℏ) without any knowledge of
state integrals or Chern-Simons theory with complex gauge group, in Section 5 we explain
how our deﬁnition follows from the state-integral model of the ﬁrs t author [ Dim] and its
perturbative expansion.
