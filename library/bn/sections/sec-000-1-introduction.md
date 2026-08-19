---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
2 Topological preliminaries . . . . . . . . . . . . . . . . . . . . . 8
3 From Hodge theory to topology . . . . . . . . . . . . . . . . . 13
4 Action of the braid group . . . . . . . . . . . . . . . . . . . . 17
5 Complex reﬂection groups . . . . . . . . . . . . . . . . . . . . 21
6 The period map . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7 Arithmetic groups . . . . . . . . . . . . . . . . . . . . . . . . 31
8 Factors of the Jacobian . . . . . . . . . . . . . . . . . . . . . 35
9 Deﬁnite integrals . . . . . . . . . . . . . . . . . . . . . . . . . 39
10 Complex hyperbolic geometry . . . . . . . . . . . . . . . . . . 44
11 Lifting homological symmetries . . . . . . . . . . . . . . . . . 49
12 The hyperelliptic case . . . . . . . . . . . . . . . . . . . . . . 51
13 Polygons and Teichm¨ uller curves . . . . . . . . . . . . . . . . 54
Research supported in part by the NSF.
1 Introduction
Every conﬁguration of distinct points ( b1,...,b n) in C determines a compact
Riemann surface X by the equation
yd = (x −b1)(x −b2) · · ·(x −bn). (1.1)
This paper gives an account of the unitary representations o f the braid group,
and the geometric structures on moduli space, that arise via this branched-
covering construction. It also develops new connections wi th arithmetic
groups, Teichm¨ uller curves and ergodic theory, and highlights open problems
in surface topology and complex reﬂection groups.
The general approach presented here pivots on the classiﬁca tion of cer-
tain arithmetic subgroups of U( r,s ) which envelop the image of the braid
group ( §7). The case U(0 ,s ) yields metrics of positive curvature on moduli
space, ﬁnite representations of the braid group, algebraic deﬁnite integrals
and rigid factors of the Jacobian of X. The case U(1 ,s ) leads to the complex
hyperbolic metrics on moduli space considered by Picard, De ligne–Mostow
and Thurston. Other unitary groups U( r,s ) provide moduli space with
natural indeﬁnite metrics. In particular, the hyperellipt ic case ( §12) yields
an action of the braid group which, together with results of R atner and
Kapovich, illuminates the topology and ergodic theory of th e period map
and its connection with the foliation of M∗
0,n by Teichm¨ uller geodesics.
This section presents a overview of the discussion.
Action of the braid group. We begin with topological considerations.
Let ζd =e2πi/d .
The braid group Bn is the fundamental group of the space C⟨n⟩ of ﬁnite
sets B ⊂ C with |B| = n. Each point conﬁguration B determines, via
equation (1.1), a compact Riemann surface X, whose cohomology group
H 1(X) forms the ﬁber of a ﬂat, complex vector bundle over C⟨n⟩. The
natural monodromy representation
ρ :Bn ∼
=π1(C⟨n⟩,B ) → Aut(H 1(X))
preserves the interesection form ( √
−1/2)
∫
α ∧β, and commutes with the
action of the deck group Z/d of X/ˆC; thus it also preserves the eigenspace
decomposition
H 1(X) =
⨁
qd=1
H 1(X)q = Ker(T ∗ −qI ),
where T (x,y ) = (x,ζ dy).
1
As we will see in §3, the signature ( r,s ) of the Hermitian vector space
H 1(X)q can be determined by drawing a line through 1 and q in C; then
r is the number of nth roots of unity strictly below the line, and s is the
number strictly above. The signature changes from deﬁnite t o hyperbolic to
higher rank, and then back again, as q moves around the circle (Figure 1).
s
(0,0)
(3,1)
(2,2)
(1,3) (0,4)
(4,0)
1
q
(3,2)
r
Figure 1. The signature of H 1(X)q forn = 6.
Restricting attention to a single eigenspace, we obtain an i rreducible
unitary representation
ρq :Bn → U(H 1(X)q) ∼
= U(r,s ).
In fact, Bn acts by a complex reﬂection group of type An−1(q) (see §5); there
is a spanning set ( ei)n−1
1 for H 1(X)q adapted to the standard generators τi
of the braid group, such that
⟨ei,e j⟩ =
√
−1






q −q 1 −q 0 ... 0
q − 1 q −q 1 −q ... 0
...
0 ... 0 q − 1 q −q






,
and
~τ ∗
i (x) = x − (q + 1) ⟨x,e i⟩
⟨ei,e i⟩ei
(for q ⁄= ±1). In particular, the generating twists τi of Bn act with ﬁnite
order on H 1(X)q.
Although purely topological, these results are convenient ly established
using particular algebraic models such as yd = xn − 1 for X. We also use
consistency of ρq under restriction to Bi ×Bn−i; geometrically, this amounts
to lettingX degenerate to a stable curve where a given Dehn twist becomes a
holomorphic automorphism. (For a more algebraic approach t o homological
representations of Bn, see e.g. [KT].)
2
The period map. Now ﬁx q = ζ −k
d with 1/n < k/d <1, let T ∗
0,n denote
the Teichm¨ uller space ofn points in the plane, and let Hr,s denote the space
of positive lines in PH 1(X)q ∼
= PCr,s . The period map
fq : T ∗
0,n → H r,s
sends a point ( C,B ) in Teichm¨ uller space to the positive line spanned by
the holomorphic form [ dx/yk] ∈H 1, 0(X) ⊂H 1(X). Thus it records a part
of the Hodge structure on X.
Using ideas familiar from polygonal billiards, in §6 we show that fq is a
local homeomorphism when qn ⁄= 1. It is also equivariant with respect to the
action of Bn via the mapping-class group on T ∗
0,n and via the representation
ρq on Hr,s . Thus the period map gives the moduli space M∗
0,n the structure of
a (G,X )-manifold, where G = U(r,s ) and X = Hr,s . A similar construction
applies to M0,n (the moduli space of n points in the sphere instead of in the
plane), when q = ζ −2
n . (For more on period mappings in general, see e.g.
[CMP].)
Arithmetic groups. It is a challenging problem to describe the image of
the braid group under ρq. In particular, it is unknown when An−1(q) ∼
=
ρq(Bn) is a lattice in U( r,s ).
To study the image of ρq in more detail, we begin by observing that the
action of Bn on H 1(X)q preserves the module Λ n,q = H 1(X, Z[q])q. Thus
ρq(Bn) is contained in the countable subgroup
U(Λ n,q ) ⊂ U(H 1(X)) ∼
= U(r,s )
of unitary automorphisms of this module.
In §7 we determine all pairs ( n,q ) such that U(Λ n,q ) is discrete (see
Table 9). When discreteness holds, ρq(Bn) is also discrete, and potentially
arithmetic. There are inﬁnitely many ( n,q ) such that U(Λ n,q ) is discrete, but
for n> 12 this only occurs when Z[q] is itself discrete (i.e. when d = 2, 3, 4
or 6).
Special cases. In §8— §13 we develop the interaction between fq, ρq(Bn)
and U(Λ q,n ) in more detail, in three special cases.
