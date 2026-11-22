---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-002-3-from-hodge-theory-to-topology
section_title: "From Hodge theory to topology"
section_number: 3
pages: 14-18
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
From Hodge theory to topology
In this section we analyze the action of the braid group further, by using
holomorphic 1-forms to represent the cohomology of X.
Hodge structure. A given point conﬁguration B ⊂C determines a com-
plex structure on the genus g cyclic covering space π : X →bC branched
over B ∪{∞}. The complex structure in turn determines the g-dimensional
space of holomorphic 1-forms Ω(X) on X, and the Hodge decomposition
H1(X) = H1,0(X) ⊕H0,1(X) ∼= Ω(X) ⊕Ω(X).
The intersection form
⟨α, β⟩=
√−1
2
Z
X
α ∧β
(3.1)
is positive-deﬁnite on H1,0(X) and negative-deﬁnite on H0,1(X).
Symmetric curves. Now assume B coincides with the nth roots of unity.
Then X is isomorphic to the smooth algebraic curve given by
yd = xn −1,
with the projection to bC given by π(x, y) = x and with the generating deck
transformation of X/bC given by
T(x, y) = (x, ζdy).
We then have an additional symmetry R : X →X given by
R(x, y) = (ζnx, y).
Eigenforms. Since the abelian group ⟨R, T⟩preserves the intersection form
and the Hodge structure, we have a decomposition
H1(X) =
M
H1(X)jk
of the cohomology of X into orthogonal eigenspaces
H1(X)jk = Ker(R∗−ζj
nI) ∩Ker(T ∗−ζ−k
d I),
13
1,0
k
H0,1
H
1
2
4
5
6
7
8
3
5
4
3
2
1
j
Figure 6. Occupied eigenspaces H1(X)jk are shown in white. Those above
the diagonal span H1,0(X), and those below span H0,1(X).
and a further reﬁnement
H1(X)jk = H1,0
jk (X) ⊕H0,1
jk (X).
We can assume 0 ≤j/n, k/d < 1.
To populate these eigenspaces, we consider the meromorphic forms de-
ﬁned by
ωjk = xj−1 dx
yk
.
The divisor (ωjk) = (dx/x) + j(x) −k(y) is easily calculated using the
fact that the ﬁbers of X/bC have multiplicity d/e over ∞, d over B, and
1 elsewhere, where e = gcd(d, n) = |f
∞|. Letting eB, f
∞and e0 denote the
preimages of B, 0 and ∞on X, considered as divisors where each point has
weight one, we obtain
(x)
=
−(d/e)f
∞+ e0,
(y)
=
−(n/e)f
∞+ eB,
and
(dx/x)
=
−f
∞−e0 + (d −1) eB,
which yields
(ωjk)
=
(kn/e −jd/e −1)f
∞+ (j −1)e0 + (d −1 −k) eB.
(3.2)
14
Thus ωjk is holomorphic for all j, k such that 0 < j/n < k/d < 1, and hence
in this range we have dim H1,0(X)jk ≥1. Similarly, by considering ωjk, we
ﬁnd dim H0,1(X)jk ≥1 for 0 < k/d < j/n < 1. But the total number of
pairs (j, k) satisfying one condition or the other is exactly (n−1)(d−1)+(1−
e) = 2g = dim H1(X). Thus ωjk and ωjk account for the full cohomology of
X. In summary:
Theorem 3.1 We have
dim H1(X)jk = dim H1,0(X)jk = 1
if 0 < j/n < k/d < 1,
and
dim H1(X)jk = dim H0,1(X)jk = 1
if 0 < k/d < j/n < 1.
The remaining eigenspaces are zero.
The case of a degree d = 6 covering branched over n = 9 points (and inﬁnity)
is shown in Figure 6.
Corollary 3.2 When q = ζ−k
d , the signature of the intersection form on
H1(X, C)q is given by (r, s) = (⌈n(k/d) −1⌉, ⌈n(1 −k/d) −1⌉).
Indeed, the signature (r, s) just counts the number of terms of type (1, 0) and
(0, 1) in the expression H1(X)q = L
j H1(X)jk, or equivalently the number
of terms above and below (but not on) the diagonal in the kth row of Figure
6.
Corollary 3.3 The eigenspace H1(X)q has dimension n −2 if qn = 1, and
dimension n −1 otherwise.
Genus zero quotients. We note that the Riemann surfaces X/⟨R⟩, X/⟨T⟩
and X/⟨RT⟩all have genus zero. This provides another explanation for the
vanishing of eigenspaces — any R, T or RT-invariant cohomology class
descends to the sphere, and H1(bC) = 0.
Remark: Lefschetz formulas. The eigenspace decomposition of H1(X)
shown in Figure 6 can be determined, alternatively, by applying the Lef-
schetz formulas
Tr(g|H1(X)) = 2 −
X
g(z)=z
1
and
Tr(g|H0,1) = 1 −
X
g(z)=z
(1 −g′(z))−1
to compute the characters of G = ⟨R, T⟩acting on H1(X) and H0,1(X).
The Chevalley-Weil formula similarly gives the characters of G|H1,0(X) for
general Galois coverings [ChW]; see also [Hu].
15
Figure 7. A model for the branched covering X.
Remark: the hexagon model. Here is an explicit model for H1(X, Z) as
a symplectic lattice equipped with the action of G = Z/n × Z/d = ⟨R, T⟩.
The proof will also provide a global topological model for G acting on X.
Let S = {(1, 0), (0, 1), (−1, −1)} ⊂G. Deﬁne an alternating form on the
standard basis of the group ring Z[G] ∼= Znd by
[g, h] =





1
if g −h ∈S,
−1
if h −g ∈S, and
0
otherwise,
(3.3)
and extend it by linearity to Z[G]. Let R ⊂Z[G] denote the radical of this
form (the set of elements x such that [x, y] = 0 for all y).
Theorem 3.4 The space H1(X, Z) is isomorphic to Z[G]/R as a symplectic
Z[G]-module.
Sketch of the proof.
Let A and B be a pair of 2-disks, colored white
and black respectively. Construct a surface Y0 from (A ⊔B) × G by joining
A × {g} to B × {g + s} with a band whenever s ∈S (see Figure 7). The
group G acts by deck transformations on Y0, with quotient a surface Y0/G
of genus 1 with 1 boundary component.
Now put a half-twist in each band of Y0 (as in Figure 5), to obtain a new
surface Y1. Then Y1/G has genus 0 and 3 boundary components. By ﬁlling
in the boundary components of Y1 and Y1/G with disks, we obtain closed
surfaces Y and Z ∼= S2 and a degree nd branched covering
π : Y →S2
with deck group G.
16
Let C ⊂Y be the core curve of one of the hexagons appearing in Figure 7.
It is then straightforward to check that the intersection number (gC) · (hC)
in H1(Y, Z) is given by (3.3). By comparing the rank of this form with the
ﬁrst Betti number of Y , we ﬁnd the inclusion Z[G]/R →H1(Y, Z) is an
isomorphism.
Now one can also regard Y/G as an orbifold with signature (n, d, nd/e),
where e = gcd(d, n).
The generators of G correspond loops around the
points of orders n and d. Similarly, the map p : X →bC given by p(x, y) = xn
presents X/⟨R, T⟩as a covering of the same orbifold, with singular points at
0, 1, ∞. The proof is completed by identifying p : X →bC with π : Y →S2.
