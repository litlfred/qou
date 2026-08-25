---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-026-5-the-state-integral-and-higher-loops
section_title: "The state integral and higher loops"
section_number: 5
pages: 29-30
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
Our explicit formulas for the torsion τT , as well as higher invariants ST ,n , have been ob-
tained from a state integral model for analytically continued SL(2 , C) Chern-Simons theory.
In this section, we will review the state integral, and analyze its asym ptotics in order to
re-derive the full asymptotic expansion
(5.1) ZT (ℏ) = ℏ− 3
2 exp
[ 1
ℏST , 0 +ST , 1 + ℏST , 2 + ℏ2ST , 3 +...
]
,
and to unify the formulas of previous sections. We should point out t hat this section is not
analytically rigorous, but serves as a motivation for our deﬁnition of the all-loop invariants,
and provides a glimpse into the calculus of (complex, ﬁnite dimensional) state-integrals.
The basic idea of a state integral is to cut a manifold M into canonical pieces (ideal
tetrahedra); to assign a simple partition function to each piece (a q uantum dilogarithm); and
then to multiply these simple partition functions together and integr ate out over boundary
conditions in order to obtain the partition function of the glued manif oldM. A state integral
provides a ﬁnite-dimensional reduction of the full Feynman path integral on M.
Currently, there are two ﬂavors of SL(2 , C) state integrals in the literature. The ﬁrst,
introduced in [ Hik01, Hik07], studied in [ DGLZ09], and made mathematically rigorous in
[AK], is based on a 3-dimensional lift of the 2-dimensional quantum Teichm ¨ uller theory in
Kashaev’s formalism [Kas98]. It uses variables associated to faces of tetrahedra. The secon d,
developed in [ Dim], explicitly uses shape parameters — associated to edges of tetrah edra —
and constitutes a 3d lift of Teichm¨ uller theory in the Fock-Chekhov formalism [ FC99]. The
two types of state integrals should be equivalent, though this has o nly been demonstrated
in isolated examples so far [ SV].
It is the second state integral that we employ in this paper, due to it s explicit dependence
on shape parameters. Indeed, suppose that M is an oriented one-cusped hyperbolic manifold
with a ρ0–regular triangulationT and enhanced Neumann-Zagier datum ˆβT = (z, A, B,f ),
with Af + Bf ′′ = ν. We must also assume that B is non-degenerate, which (Lemma A.3)
is always possible. Then we will 5 show in Appendix C that the state integral of [ Dim] takes
the form
ZT (ℏ) =
√
8π3
ℏ3 det B
∫ dNZ
(2πℏ)N/ 2e
1
ℏ
[ 1
2
(
iπ + ℏ
2
) 2
f ·B−1ν−
(
iπ + ℏ
2
)
Z·B−1ν+ 1
2 Z·B−1AZ
] N∏
i=1
ψℏ(Zi),
(5.2)
whereψℏ(Z) is a non-compact quantum dilogarithm [
Bar99, Fad95], the Chern-Simons par-
tition function of a single tetrahedron. The integration variables Zi are, literally, the loga-
rithmic shape parameters of T .
The integration contour of ( 5.2) is unspeciﬁed. A complete, non-perturbative deﬁnition
ofZT (ℏ) requires a choice of contour, and the choice leading to invariance u nder 2–3 moves
(etc.) may be quite subtle. However, a formal asymptotic expansio n of the state integral as
in ( 5.1) does not require a choice of contour. It simply requires a choice of critical point for
5Here we multiply ( C.23) (at u = 0) by an extra, canonical normalization factor (2 π/ ℏ)3/2, in order to
precisely match the asymptotics of the Kashaev invariant at the dis crete faithful representation.
30 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
the integrand. Then the asymptotic series may be developed via formal Gaussian integration
in an inﬁnitesimal neighborhood of the critical point.
We will show in Section
