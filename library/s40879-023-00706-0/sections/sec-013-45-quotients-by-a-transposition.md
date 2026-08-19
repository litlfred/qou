---
doc_id: s40879-023-00706-0
doc_title: "RESEARCH ARTICLE"
section_id: sec-013-45-quotients-by-a-transposition
section_title: "Quotients by a transposition"
section_number: 4.5
pages: 32-35
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
The strategy of quotienting from theP4-model using semi-invariants from the previous
sections can also be used to calculate the quotient of Bring’s curve by a transposition.
We take semi-invariants
(s1, s2, s3, s4)T =
⎛
⎜⎜⎝
1100
1 −10 0
0011
001 −1
⎞
⎟⎟⎠ (x1, x2, x3, x4)T,
and in terms of these variables the deﬁning equations of Bring’s curve become
H2 = 1
2 (s2
1 + s2
2) + s2
3 + s2
4 + (s1 + s3 + s4)2,
H3 = 1
4 (s3
1 + 3s1s2
2) + s3
3 + s3
4 − (s1 + s3 + s4)3.
Taking invariants [s : t : u : v]=[ s1 : s2
2 : s3 : s4] and eliminating t yields the elliptic
curve
E2 : 4s3 + 8s2u + 7su 2 + u3 + sv2 − uv2 = 0, jE2 =− 25
2 = j(5τ0). (18)
We observe that (also curiously) the quotient of B by a transposition is isomorphic to
the quotient by a 4-cycle. It is not clear that there is any a priori reason for this to be
the case. We are however able to relate the elliptic curves E2 and E4 as follows.
123
Bring’s curve: old and new Page 33 of 46 3
The normaliser of ⟨(12)⟩in S5 is NS5 (⟨(12)⟩) =⟨(12), (34), (345)⟩∼= D12 where
now NS5 (⟨(12)⟩)/⟨(12)⟩∼= S3.26 We may immediately identify the action of (34) as
the hyperelliptic involution on E2 as it acts as v →− v, but we also retain another
group action, that of (345). To understand this action recall that there are six ﬁxed
points of the action of (12) on B, which are all Weierstrass points. This gives six
more distinguished points on the curve E2 in addition to the two images of the vertices
we have seen previously. The six Weierstrass points ﬁxed by (12) break into two
orbits of three under (345) which we denote by {Hi},{H′
i }, i = 1, 2, 3. Just as (345)
gives Bring’s curve as an unramiﬁed cover of the genus 2 curve C2, quotienting each
by a transposition has (345) yielding an unramiﬁed automorphism of the quotient
curves. Hence there exists a quotient from E2 = B/⟨(12)⟩to another elliptic curve
E4 = B/⟨(12), (345)⟩such that the following diagram commutes:
BC 2
E2 E4
(345)
(12) (12)
(345)
To view this action on the elliptic curve E2, we calculate that (345):[ s : t : u : v]→
[s : t :− s − u/2 − v/2 : s + 3u/2 − v/2].I nt h e s = 1 afﬁne chart 4 + 8u + 7u2 +
u3 + (1 − u)v 2 = 0 we can take as a cohomology basis
η ..= du
2v(1 − u) ,
and it is a simple algebraic calculation to see that this differential is invariant under
the action of (345).I f {Hi},{H′i} are the images of the Weierstrass points on E2 such
that (345)(Hi) = Hi+1, (345)(Hi) = Hi+1 and so forth, the invariance of η tells us
that
∫H 2
H 1
η =
∫H 3
H 2
η =··· ,
∫H′2
H′1
η =
∫H′3
H′2
η =··· ,
∫H′1
H 1
η =
∫H′2
H 2
η =···
This means that if/Lambda1=⟨1, 5τ0⟩is the period lattice of the elliptic curveE2 then
∫Hi+1
Hi
η
and
∫H′i+1
H′i
η are the same ﬁxed element of /Lambda1/3. By choosing an appropriate basis we
may take (345): z → z+ 1/3f o rz ∈ C/⟨1, 5τ0⟩. Then the quotient map will be a 3: 1
isogeny of elliptic curves and we have the period of E4 to be 15τ0 and jE4 = j(15τ0).
Under this isogeny the six images on E2 of the Weierstrass points [1: 1: α :β : γ]
are mapped to two on E4. Indeed, one may construct the isogeny explicitly using the
Weierstrass-℘ function and the Abel–Jacobi map via the diagram
26 The cosets of ⟨(12)⟩ in the normaliser are {e,( 12)}, {(345), (12)(345)}, {(354), (12)(354)},
{(34), (12)(34)}, {(35), (12)(35)},a n d{(45), (12)(45)}.
123
3 Page 34 of 46 H.W. Braden, L. Disney-Hogg
E2 E4
J(E2) J(E4)
P↦→
∫P
∞ η
z↦→3z
z↦→(℘( z),℘′(z))
where J(E) represents the Jacobian of the elliptic curve viewed at C/⟨1,τ ⟩.
Remark 4.2 This calculation may be veriﬁed numerically, as shown in the notebooks.
Remark 4.3 Note that when we call (345) an automorphism of the elliptic curve, we
have to think about it only in the category of projective varieties with morphisms given
by rational maps. To consider the group structure on an elliptic curve E we need to
also give a base point O ∈ E which acts as the additive identity. A morphism from
pair (E, O) → (E
′, O′) must map O → O′. If we denote the group of automorphisms
of E as a projective variety as Aut (E), and the group of O-ﬁxing automorphisms as
Aut O(E), then we have short exact sequence
0 → TE → Aut(E) → Aut O(E) → 0,
where TE is the group of translations of E. It is a classical theorem that Aut O(E) ∈
{C2, C4, C6} (here we are over C).
Here (345) is indeed a translation. To see this take variables x, y deﬁned by
u = − 70s3 + 6sx
2(25s2 + 3x) ,v = − 3y
25s2 + 3x ,
which in the afﬁne patch wheres = 1g i v eE2 as the curvex3−25/3x+2950/27+y2 =
0. In these coordinates (345) acts as
x ↦→ 5(275 − 3x + 15y)
3(65 + 15x − 3y) , y ↦→ 20(55 − 15x − 3y)
(65 + 15x − 3y) .
Indeed for the projective coordinates [X : Y : Z] of our curve X 3 − 25/3XZ 2 +
2950/27Z 3 + Y 2 Z = 0 we have under (345) that
[X : Y : Z] ↦→
[
5(275Z/3 − X + 5Y) : 20(55Z − 15X − 3Y): 65Z + 15X − 3Y
]
↦→
[
275Z/3 − X − 5Y :− 220Z + 60X − 12Y : 13Z + 3X + (3Y)/5
]
↦→[ X : Y : Z].
When working with a Weierstrass model of an elliptic curve it is standard to take the
distinguished point to be ∞=[ 0 : 1: 0] and we see in terms of (x, y) that ∞ ↦→
(−25/3, 20) ↦→ (−25/3,−20) ↦→∞ .
123
Bring’s curve: old and new Page 35 of 46 3
