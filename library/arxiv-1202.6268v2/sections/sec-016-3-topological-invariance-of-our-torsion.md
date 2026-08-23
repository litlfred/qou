---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-016-3-topological-invariance-of-our-torsion
section_title: "Topological invariance of our torsion"
section_number: 3
pages: 15-16
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
Given a one-cusped hyperbolic manifold M with regular triangulation T ={∆ i}N
i=1 and
Neumann-Zagier datum ˆβT = (z, A, B,f ), we have proposed that the nonabelian torsion is
given by
(3.1) τT :=±1
2 det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f ∈ EM/{±1},
where ∆ z = diag(z1,...,z N ), and similarly for ∆ z′′. Since ( z,z ′,z ′′)∈ EM we must have
τT∈EM as well.
After a brief example of how the formula ( 3.1) works, we will proceed to prove Theorems
1.3 and 1.4 on the topological invariance of τT . We saw in Section 2 that the Neumann-Zagier
datum depends not only on a triangulation T , but also on a choice of
(1) quad type for T ,
(2) one edge of T whose gluing equation is redundant,
(3) normal meridian path,
(4) ﬂattening f .
We will begin by showing that τT is independent of these four choices, and then show that
it is invariant under 2–3 moves, so long as the 2–3 moves connect two regular triangulations.
The four choices here are independent, and can be studied in any or der. However, in
order to prove independence of ﬂattening, it is convenient to use a quad type for which the
matrix B is non-degenerate. Such a quad type can always be found (Lemma
A.3), but is
not automatic. Therefore, we will ﬁrst show invariance under chan ge of quad type, and then
proceed to the other choices. It is interesting to note that of all t he arguments that follow
(including the 2–3 move), independence of ﬂattening is the only one t hat requires the use of
the full gluing equations zAz′′B = (−1)ν.
16 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
3.1. Example: 4 1 continued. To illustrate the Deﬁnition
1.8, consider the ﬁgure-eight
knot complement again. From Section 2.6, we already have one possible choice for the
Neumann-Zagier matrices ( 2.13) and a generic ﬂattening ( 2.15). We use them to obtain
±τ41 = 1
2 det
[(
2 2
1 1
)(
z′′ 0
0 w′′
)
+
(
1 1
1 0
)(
z−1 0
0 w−1
)]
w′′−1
= 1
2w′′ det
(
2z′′ +z−1 2w′′ +w−1
z′′ +z−1 w′′
)
= 1
2w′′ det
(
z′′ + 1 w′′ + 1
1 w′′
)
= 1
2(z′′−w′′−1) = 1
2
√
−3,(3.2)
where at intermediate steps we used z′′ +z−1− 1 = w′′ +w−1− 1 = 0, and at the end we
substituted the discrete faithful solution z =z′′ =w =w′′ =eiπ/ 3.
The invariantτ41 belongs to the invariant trace ﬁeld E41 = Q(√
−3), and agrees with the
torsion of the ﬁgure-eight knot complement [ DFJ].
