---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-010-3-from-hodge-theory-to-topology
section_title: "From Hodge theory to topology"
section_number: 3
pages: 14-16
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove r- ings of P1, highlighting their"
---
In this section we analyze the action of the braid group furth er, by using
holomorphic 1-forms to represent the cohomology of X.
Hodge structure. A given point conﬁguration B ⊂ C determines a com-
plex structure on the genus g cyclic covering space π : X → ˆC branched
overB ∪ {∞}. The complex structure in turn determines the g-dimensional
space of holomorphic 1-forms Ω( X) on X, and the Hodge decomposition
H 1(X) = H 1, 0(X) ⊕H 0, 1(X) ∼
= Ω(X) ⊕
Ω(X).
The intersection form
⟨α,β ⟩ =
√−1
2
∫
X
α ∧β (3.1)
is positive-deﬁnite on H 1, 0(X) and negative-deﬁnite on H 0, 1(X).
Symmetric curves. Now assume B coincides with the nth roots of unity.
Then X is isomorphic to the smooth algebraic curve given by
yd =xn − 1,
with the projection to ˆC given by π(x,y ) = x and with the generating deck
transformation of X/ˆC given by
T (x,y ) = (x,ζ dy).
We then have an additional symmetry R :X →X given by
R(x,y ) = (ζnx,y ).
Eigenforms. Since the abelian group ⟨R,T ⟩ preserves the intersection form
and the Hodge structure, we have a decomposition
H 1(X) =
⨁
H 1(X)jk
of the cohomology of X into orthogonal eigenspaces
H 1(X)jk = Ker(R∗ −ζ j
nI) ∩ Ker(T ∗ −ζ −k
d I),
13
1,0
k H0,1
H
1 2 4 5 6 7 83
5
4
3
2
1
j
Figure 6. Occupied eigenspaces H 1(X)jk are shown in white. Those above
the diagonal span H 1, 0(X), and those below span H 0, 1(X).
and a further reﬁnement
H 1(X)jk =H 1, 0
jk (X) ⊕H 0, 1
jk (X).
We can assume 0 ≤j/n,k/d< 1.
To populate these eigenspaces, we consider the meromorphic forms de-
ﬁned by
ωjk = xj−1dx
yk .
The divisor ( ωjk ) = ( dx/x) + j(x) − k(y) is easily calculated using the
fact that the ﬁbers of X/ˆC have multiplicity d/e over ∞, d over B, and
1 elsewhere, where e = gcd(d,n ) = |~∞|. Letting ~B, ~∞ and~0 denote the
preimages of B, 0 and ∞ onX, considered as divisors where each point has
weight one, we obtain
(x) = −(d/e)~∞ +~0,
(y) = −(n/e)~∞ + ~B, and
(dx/x) = −~∞ −~0 + (d − 1)~B,
which yields
(ωjk ) = ( kn/e −jd/e − 1)~∞ + (j − 1)~0 + (d − 1 −k)~B. (3.2)
14
Thusωjk is holomorphic for all j,k such that 0 <j/n<k/d< 1, and hence
in this range we have dim H 1, 0(X)jk ≥ 1. Similarly, by considering ωjk , we
ﬁnd dim H 0, 1(X)jk ≥ 1 for 0 < k/d < j/n <1. But the total number of
pairs (j,k ) satisfying one condition or the other is exactly ( n−1)(d−1)+(1 −
e) = 2g = dimH 1(X). Thus ωjk andωjk account for the full cohomology of
