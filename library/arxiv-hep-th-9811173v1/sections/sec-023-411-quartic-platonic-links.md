---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-023-411-quartic-platonic-links
section_title: "Quartic platonic links"
section_number: 4.11
pages: 13-15
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
Our ﬁrst guess, that the 4 non-self-dual platonic links might yield qu adratic number ﬁelds,
failed. Nonetheless, it is interesting to determine their number ﬁelds , and hence obtain
accurate volumes. This is clearly a taxing job. To prepare for it, we ﬁ rst tackled a problem
of similar complexity, where an accurate answer could be inferred.
We found that by adding n concentric components at each of the 4 “vertices” of
Fig. 1, one obtains a volume Z20 + 2nZ15 for the link with 24 + 24 n crossings and 10 + 4n
components, when n ≤ 5. At n = 6, SnapPea was given the 34-component link with
168 crossings, which was triangulated to give 632 ideal tetrahedra , each having a volume
12http://home.att.net/~Manoharan/SnapPea/snappea.html
12
D(zk) with zk ∈ Q(√−5) or zk ∈ Q(√−15). We output the 632 shapes, and computed,
at 1800-digit precision, the 3 × 632 = 1, 896 Clausen values entailed by
D(z) = V (arg(z), − arg(1 −z)) (38)
V (θ1,θ 2) := 1
2 {Cl2(2θ1) + Cl2(2θ2) − Cl2(2θ1 + 2θ2)} (39)
obtaining 1800-digit agreement with the expectation Z20 + 12Z15 = 502. 408032... for the
volume. This gave us conﬁdence that we could process the 950 ideal tetrahedra entailed
by the remaining 4 platonic links.
We obtained from SnapPea the low-precision volumes
vol(C) ≈ vol(O) ≈ 114. 537611 (40)
vol(D) ≈ vol(I) ≈ 310. 913145 (41)
from 128 + 130 + 346 + 346 = 950 ideal tetrahedra.
The duality between cube and octahedron, and between dodecahe dron and icosahe-
dron, is gratifying. Such duality is not restricted to platonic links. Mo re generally, suppose
that we have a link, L, with an alternating projection in which the components may be
separated into two classes: vertex (V) components and edge (E) components, with pairs
of crossings only between V and E components, and every E connec ting a pair of V’s.
Thus the crossing number is 4 times the number of E components. No w shrink the V com-
ponents to true vertices (some of which may be divalent) and the E c omponents to true
edges that connect these points, to obtain a planar graph, P . Then construct the dual
graph,P ∗, whose vertices lie in the regions of the plane partitioned by the edge s of P and
whose edges thus cross the edges of P . Now thicken P ∗ to obtain the alternating link L∗
dual to L. The crossing numbers of L and L∗ are equal, but the numbers of components
need not be. For example C := 48 20
cub has more components than C ∗ := O := 48 18
oct, and
D := 120 50
dod has more than D∗ :=I := 120 42
ico. On the basis of these and further tests, we
conjecture that vol(L) = vol(L∗), for every shrinkable link L.
To identify the number ﬁelds of the {C,O } and {D,I } pairs, we ﬁrst examined the
cusp shapes, and found that
KC := Q
( √
8
√
2 − 15
)
(42)
gave a simple ﬁt to the cusp shapes of {C,O }, at the 12-digit precision provided by
SnapPea, while
KD := Q
( √
−12
√
5 − 31
)
(43)
similarly ﬁtted the cusp shapes of {D,I }.
We then output z-values of the triangulations. Fitting these was not easy, since the
data now consisted of numerical values, to 12 decimal places, of 1 , 900 real or imaginary
parts, each of which was supposed to be ﬁttable by two powers of
√
15 − 8
√
2, in the
cubical and octahedral cases, or
√
31 + 12
√
5, in the dodecahedral and icosahedral cases.
13
In each of the 1 , 900 cases we required a signiﬁcant integer relation between 3 numbe rs:
the 12-digit SnapPea datum and the two powers, namely 0 and 2 for a real part, or 1 and
3 for an imaginary part. Whether this can be done by a reliable and unif ormly automated
method depends upon the largest integer. If it has more than 4 digit s, the matter is moot,
since ﬁtting 12-digit data with 3 integers with up to 4 digits is already a p arlous business.
In fact our ﬁrst attempt yielded garbage in a signiﬁcant fraction of the 1, 900 cases.
Fortunately, 3 features of the mathematics enable us to crack th is tough nut. First,
the 6-fold symmetry of the Bloch–Wigner function
D(z) = D(1/ (1 −z)) = D(1 − 1/z ) = D(1/ z) = D(1 −z) = D(z/ (z − 1)) (44)
gave us 6 bites at each cherry. Secondly, number theory suggest ed that we might do well
to make the Ansatz
z = 1
Iz
3∑
p=0
Ipup (45)
with 6 × 950 × 5 = 28 , 500 integers relating 6 equivalent z values of 950 ideal volumes
to 4 powers of u = 1
