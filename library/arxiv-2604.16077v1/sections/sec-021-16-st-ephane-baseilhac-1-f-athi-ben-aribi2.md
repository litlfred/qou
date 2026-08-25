---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-021-16-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 16
pages: 16-18
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
Proposition 2.8. ([7, Proposition 4.6] and [8, Remark 1.4]) The restriction
(25) ˜hol| : Ghyp(T,b ) → ˜Xhyp(M )
is a birational isomorphism, and the dilation factor δ : Ghyp(T,b ) →H 1(∂ ¯M ; C∗) ∼
= (C∗×C∗)p
is a birational isomorphism onto its image.
The proof combines Thurston’s hyperbolic Dehn ﬁlling theor em in the form of [52, 44] with
Dunﬁeld’s arguments showing that r has degree one.
Set
(26) Ghyp,N (T,b ) := π−1
N (Ghyp(T,b )),
with πN the map (24). Deﬁne NXhyp(M ) as the set of pairs ( ρ,κ ) where ρ ∈ Xhyp(M ),
κ ∈ H 1(∂ ¯M ; C∗), and κN (γ) is a squared eigenvalue of ρ(γ) for all γ ∈ H1(∂ ¯M ; Z). Thus
NXhyp(M ) has the structure of a ﬁbered product Xhyp(M ) ×X(∂ ¯M )H 1(∂ ¯M ; C∗). Clearly, the
mapπX
N : NXhyp(M ) → ˜Xhyp(M ), (ρ,κ ) ↦→(ρ,κN ), has degree N 2p. Consider the “boundary
weight map” (see (23))
(27) κ : Ghyp,N (T,b ) − → H 1(∂ ¯M ; C∗)
w ↦− →κw.
Since κw(γ)N =δw(γ), we can lift ˜hol| to a regular map
(28) ~hol : Ghyp,N (T,b ) − → NXhyp(M )
w ↦− →(ρw,κ w).
It has degree Nn−p (see Theorem 2.7 and the comment thereafter), and by constru ction
πN = ( ˜hol|)∗πX
N.
FinallyκX : NXhyp(M ) → C∗ × C∗ is deﬁned by κX (ρ,κ ) = (κ(µK ),κ (λK )); so κ =κX ◦~hol.
Remark 2.9. (see [7, Proposition 4.6 and pages 2017-2019] and [8, Remark 1.4]). Denote by
EP the set of triangulations obtained by subdividing the Eps tein-Penner polyhedral decompo-
sition of M . For every T ∈EP , ﬁx a branchings bT ofT as at the beginning of Section 2.1.2,
and set ZT := Ghyp(T,bT ) ⊂ G(T,bT ). There is a maximal Zariski open subset Ω ZT in ZT
containing whyp, such that hol(ΩZT ) is Zariski open in Xhyp(M ) and hol : ΩZT →hol(ΩZT )
is a homeomorphism. Then
Ω :=
⋂
T ∈EP
hol(ΩZT )
is a canonical Zariski open subset Ω of Xhyp(M ) which contains ρhyp and whose points can
be (uniquely) encoded by points in the components Ghyp(T,b ), for every T ∈EP .
2.3. The case of the ﬁgure-eight knot complement. Fix an orientation of M =S3 \ 41.
Denote by λK and µK the canonical longitude and the meridian of K, oriented so that the
ordered pair (µK,λK) followed by the outward normal to ∂ ¯M deﬁnes a positive frame of ¯M .
We denote also by λK , µK their classes in H1(∂ ¯M ; Z).
In this section we implement on M the structures deﬁned in Sections 2.1 and 2.2.1. We will
use the geometric, positive ideal triangulation T ofM shown in Figure 1, with branching b as
indicated. The two tetrahedra ∆ 0, ∆ 1 have opposite b-orientations, and ∆ 0 is the positively
b-oriented one; note that they were denoted U , V in Section 1.2.
Denote by u := (u0,u 1,u 2) and u := ( u0, u1, u2) triples of classical and quantum shape
parameters on ∆ 0, and by ( a0,a 1,a 2) a triple of edge colors compatible with u. Denote
similarly by v := (v0,v 1,v 2), v := (v0, v1, v2) and (b0,b 1,b 2) the corresponding data for ∆ 1.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 17
The Thurston gluing variety G(T,b ) is well-known, and can be described as follows. For
the computation of the formulas (29) and (30) below, we refer to [44, Section 15.1.4], where
we note that both tetrahedra are given positively oriented b ranchings, the classical shape
parameters are ordered diﬀerently (the parameters w and z are u2 and 1 −v2 =v−1
0 in our
notations), and the curves m and l are µK and µ−2
K λK . Now, G(T,b ) can be identiﬁed with
the irreducible curve in C2 with coordinates (u0,v 0) and deﬁning equation
u1u2
2v−2
0 v−1
1 = 1,
or equivalently
(29) u2
0v2
0 = (1 −u0)(1 −v0).
The point whyp ∈ G(T,b ) with coordinates ( u0,v 0) = ( eπi/3,e −πi/3) realizes the complete
structure on M , and any point w ∈ G(T,b ) suﬃciently close to whyp determines a (non-
complete) hyperbolic structure on M (see (ii) in Section 2.1.2).
For every point w = (u,v ) ∈G(T,b ) the dilation factor δw ∈H 1(∂ ¯M ; C∗) in (15) is given by
(30) δw(λK ) = u2
0u−2
2 = u4
0
(1 −u0)2 , δw(µK ) = u2v2 = (u0 − 1)(v0 − 1)
u0v0
.
The quantum gluing variety GN (T,b ) is the subspace of C6 formed by the pairs ( u, v) of
triples of quantum shape parameters u := ( u0, u1, u2) and v := ( v0, v1, v2) satisfying the
tetrahedral and edge relations
(31) u0u1u2 =e− πi
N , v0v1v2 =e+ πi
N
u1u2
2v−2
0 v−1
1 =e− 2πi
N , u1u2
0v−2
2 v−1
1 =e− 2πi
N .
Using the tetrahedral relations it is easy to see that the two edge relations are equivalent. Thus
we can identifyGN (T,b ) with the set of tuples ( u0, u1, v0, v1) satisfying u1u2
0v−2
2 v−1
1 =e− 2πi
N ,
for instance. Since G(T,b ) is an irreducible curve, we have
(32) Ghyp(T,b ) = G(T,b ) and Ghyp,N (T,b ) = GN (T,b ).
Given a point w := (u, v) ∈GN (T,b ), let w := (u,v ) ∈G(T,b ), and d := (a,b ) be a system of
edge colors such that ( w,d ) is compatible with w; hence they are related by the formula (6).
Consider the log weight lκ associated to ( w,d ) by (18), and the boundary weight κ := κw
associated to w by (22). Recall the bulk weight h2 ∈ H 1(M ; Z/2) in (19), and the relation
(23). As M is a knot complement we have h2(λK) = 0. Therefore
(33) κw(λK ) = u2
0u−2
2 =e
lκ(λK )
N , κw(µK) = u2v2 = (−1)h2(µK )e
lκ(µK )
N .
Fork = 0, 1, 2, let us write uk, vk as in (6), in terms of edge colors and rescaled log-parameter s
lu
k :=N −1(Log(uk) +πiak), lv
k :=N −1(Log(vk) +πibk); so
(34) uk = exp(lu
k +πiak) , vk = exp(lv
k +πibk).
The relations (11), (12) and (18) provide logarithms of (31) and (33) of the form
(35)













lu
0 + lu
1 + lu
2 = −πi
N +πi(a0 +a1 +a2)
lv
0 + lv
1 + lv
2 = + πi
N +πi(b0 +b1 +b2)
lu
1 + 2lu
2 − 2lv
0 − lv
1 = − 2πi
N +πi(a1 + 2a2 − 2b0 −b1)
2lu
0 − 2lu
2 = lκ(λK )
N +πi(2a0 − 2a2)
lu
2 + lv
2 = lκ(µK )
N +πi(a2 +b2).
Note that h2(µK ) = a2 +b2 mod(2) by (19); all other sums of edge colors on the right side
of the system (35) are even integers ( e.g., by (8)).
