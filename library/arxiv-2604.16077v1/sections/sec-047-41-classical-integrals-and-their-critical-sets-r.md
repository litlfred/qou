---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-047-41-classical-integrals-and-their-critical-sets-r
section_title: "Classical integrals and their critical sets. Recall the contour CN from (87). By the"
section_number: 4.1
pages: 35-36
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
assumption (86), when z ∈CN both cases 0 < I(l0,∞ +z)< 2π and −2π <I(l0,∞ +z)< 0
may happen. If 0 < I(l0,∞ +z)< 2π, then ˆSN (l0,∞ +z) is given by the formulas (47)-(50),
and Lemma 3.3 yields
(92) ˆSN (l0,∞ +z) = e
N
2iπ Li2(el0,∞+z)ON →∞(1).
If −2π <I(l0,∞ +z)< 0, we get ˆSN (l0,∞ +z) = (1 −eN (l0,∞+z)) ˆSN (l0,∞ +z + 2πi) by using
N times the functional equation (52); so in this case we have
(93) ˆSN (l0,∞ +z) =
{
eN l0,∞e
N
2iπ (Li2(el0,∞+z)+2iπz)ON →∞(1) if R(l0,∞ +z)> 0
e
N
2iπ Li2(el0,∞+z)ON →∞(1) if R(l0,∞ +z)< 0.
It is easily checked that coth( Nz
2 ) is bounded on CN , and therefore the integrand on the RHS
of (88) satisﬁes, for z ∈CN :
(94) e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 ) =




eN l0,∞e
N
2iπ L+(z;l0,∞,l1,∞)ON →∞(1) if R(l0,∞ +z)> 0 and
−2π <I(l0,∞ +z)< 0,
e
N
2iπ L−(z;l0,∞,l1,∞)ON →∞(1) otherwise ,
where
(95)
{
L−(z; l0,∞, l1,∞) := Li 2(el0,∞+z) +z2 − l1,∞z,
L+(z; l0,∞, l1,∞) := Li 2(el0,∞+z) +z2 − (l1,∞ − 2iπ)z.
Note that the two halves of CN , in the left and right half spaces of C, are homotopic to
i[s−
N, 2π −s+
N ] (with opposite orientations) relatively to their endpoin ts. We call
(96) I±,N (l0,∞, l1,∞) =
∫
i[s−
N,2π−s+
N ]
e
N
2iπ L±(z;l0,∞,l1,∞)dz
the classical integrals.
Because of (94), it is reasonable to expect that the asymptot ics of the integralsI±,N (l0,∞, l1,∞)
have a lot to do with those of the integral on the RHS of (88) (se e Lemma 5.1 for a rigourous
statement). Then, in view of the saddle point method (see Sec tion 4.2), we are naturally let
to consider the critical sets of the functions z ↦→ L±(z; lx
0,∞, lx
1,∞), where the parameters lx
0,∞,
lx
1,∞, with x = u and v, are associated to the tetrehedra ∆ 0 and ∆ 1, as usual. In particular,
36 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
by Lemma 2.10 it is interesting to consider the situations wh ere (elu
0,∞,e lu
1,∞,e lv
0,∞,e lv
1,∞ ) ∈
{0}×A (T,b ) ⊂ C (T,b )×A(T,b ). By (41) and (44), such a tuple ( lu
0,∞, lu
1,∞, lv
0,∞, lv
1,∞) satisﬁes
the sole relation
(97) lu
1,∞ + 2lu
2,∞ − 2lv
0,∞ − lv
1,∞ = 0 mod(2 πi),
and it determines an asymptotic angular holonomy by the syst em
(98)
{ lu
0,∞ + lu
1,∞ + lv
0,∞ + lv
1,∞ = −i arg(κ∞(µK)) mod(2 πi)
4lu
0,∞ + 2lu
1,∞ =i arg(κ∞(λK )) mod(2 πi).
Denote by A′(T,b ) the set of solutions of the equation (97). Let us deﬁne a sign
(99) ⋆ :=
{
+1 if 2 lu,∞
0 + lu,∞
1 = i arg(κ∞(λK ))
2 mod(2πi)
−1 if 2 lu,∞
0 + lu,∞
1 = i arg(κ∞(λK ))
2 +πi mod(2πi).
Lemma 4.1. The function L±(·; l0,∞, l1,∞) has a unique critical point z0 := z±
0 (l0,∞, l1,∞),
and this point satisﬁes the equation:
(100) ⋆e− i arg(κ∞(λK ))
2 e2(l0,∞+z0) +el0,∞+z0 − 1 = 0.
Moreover, the image of the map
Ξ : A′(T,b ) − → C2
