---
doc_id: arxiv-1704.01735v4
doc_title: "Modular curves, invariant theory and E 8"
section_id: sec-008-4-a-diﬀerent-construction-from-the-modular-curve
section_title: "A diﬀerent construction: from the modular curve"
section_number: 4
pages: 30-33
source_pdf: 1704.01735v4.pdf
source_sha256: 3935747ae9291f76
toc_source: inferred
doc_brief: "Modular curves, invariant theory and E 8 — The E8 root lattice can be constructed from the modular curve X(13) by the invariant theory for the simple group PSL(2, 13)."
---
X(13) to E8
4.1. E8-singularity: from X(13) to E8
In this section, we will give a diﬀerent construction of the equation of the
E8-singularity: the symmetry group is the simple group PSL(2, 13) and the
equation has a modular interpretation in terms of theta constants of order
thirteen.
Put
Φj = Φj(x1(z), . . . , x6(z))
for j = 12, 18, 20, 30.
By Theorem 1.1, the relations
j(z) := E4(z)3
∆(z) = Φ3
20
Φ5
12
,
j(z) −1728 = E6(z)2
∆(z) = Φ2
30
Φ5
12
(4.1)
give the equation
Φ3
20 −Φ2
30 = 1728Φ5
12.
(4.2)
Hence, we have the following:
Theorem 4.1 (A diﬀerent construction of the E8-singularity: from X(13)
to E8). The equation of the E8-singularity can be constructed from the mod-
ular curve X(13) as follows:
Φ3
20 −Φ2
30 = 1728Φ5
12,
30
where Φ12, Φ20 and Φ30 are G-invariant polynomials.
Let us recall some facts about exotic spheres (see [20]). A k-dimensional
compact oriented diﬀerentiable manifold is called a k-sphere if it is homeo-
morphic to the k-dimensional standard sphere. A k-sphere not diﬀeomorphic
to the standard k-sphere is said to be exotic. The ﬁrst exotic sphere was dis-
covered by Milnor in 1956 (see [32]). Two k-spheres are called equivalent
if there exists an orientation preserving diﬀeomorphism between them. The
equivalence classes of k-spheres constitute for k ≥5 a ﬁnite abelian group Θk
under the connected sum operation. Θk contains the subgroup bPk+1 of those
k-spheres which bound a parallelizable manifold. bP4m (m ≥2) is cyclic of
order 22m−2(22m−1 −1) numerator (4Bm/m), where Bm is the m-th Bernoulli
number. Let gm be the Milnor generator of bP4m. If a (4m −1)-sphere Σ
bounds a parallelizable manifold B of dimension 4m, then the signature τ(B)
of the intersection form of B is divisible by 8 and Σ = τ(B)
8 gm. For m = 2 we
have bP8 = Θ7 = Z/28Z. All these results are due to Milnor-Kervaire (see
[21]). In particular,
2m
X
i=0
zizi = 1,
z3
0 + z6k−1
1
+ z2
2 + · · · + z2
2m = 0
is a (4m−1)-sphere embedded in S4m+1 ⊂C2n+1 which represents the element
(−1)mk · gm ∈bP4m. For m = 2 and k = 1, 2, · · · , 28 we get the 28 classes
of 7-spheres. Theorem 4.1 shows that the higher dimensional liftings of two
distinct symmetry groups and modular interpretations on the equation of the
E8-singularity give the same Milnor’s standard generator of Θ7.
4.2. The Barlow surface: from X(13) to E8
In this section, we will construct the Barlow surface from the modular
curve X(13) by the method of transversal linear sections.
By Theorem 1.1, we have
Φ12(x1(z), . . . , x6(z)) · Φ18(x1(z), . . . , x6(z)) −Φ30(x1(z), . . . , x6(z)) = 0.
(4.3)
This gives a morphism
Φ : X(13) →X ⊂CP5
(4.4)
with Φ(z) = (x1(z), . . . , x6(z)), where the variety X is given by an equation
in six variables z1, . . . , z6 of degree 30:
Φ12(z1, . . . , z6) · Φ18(z1, . . . , z6) −Φ30(z1, . . . , z6) = 0.
(4.5)
31
Moreover, we have the following morphism
ϕ : X →Z ⊂CP13,
(z1, . . . , z6) 7→(δ0, δ1, . . . , δ12, δ∞),
(4.6)
where δ0, δ1, . . . , δ12, δ∞are given by (1.4). The variety Z is given by



δ0 + δ1 + · · · + δ12 + δ∞= 0,
(δ2
0 + · · · + δ2
∞)(δ3
0 + · · · + δ3
∞) −4056
1315(δ5
0 + · · · + δ5
∞) = 0,
(4.7)
which is a Fano 11-fold. Let
W = Z ∩H1 ∩H2 ∩· · · ∩H9
(4.8)
be a transversal linear section, where the hyperplane Hi := {δ4+i = 0} (1 ≤
i ≤8) and H9 := {δ∞= 0}. Now, let us recall the following:
Proposition 4.2 (see [15]). In the family of quintic surfaces S(λ:µ) in P4
given by
S(λ:µ) = {(x0 : . . . : x4) ∈P4 : σ1 = 0, λσ2σ3 + µσ5 = 0},
(where σk denotes the k-th elementary symmetric polynomial in x0, . . . , x4
and λ, µ ∈C), all but the following six are non-singular:
(i) σ5 = 0 (reducible, consisting of 5 planes, meeting along 10 lines which
in turn meet 3 at a time in 10 points),
(ii) σ2σ3 = 0 (reducible, consisting of a quadric and a cubic surface meet-
ing along a non-singular sextic curve),
(iii) 2σ5 + σ2σ3 = 0 (20 singularities, namely the S5-orbit of (−2 : −2 :
−2 : 3 + √−7 : 3 −√−7)),
(iv) 25σ5−12σ2σ3 = 0 (10 singularities, namely the S5-orbit of (−2 : −2 :
−2 : 3 : 3)),
(v) 50σ5 + σ2σ3 = 0 (5 singularities, namely the S5-orbit of (1 : 1 : 1 : 1 :
−4)),
(vi) 2σ5 −σ2σ3 = 0 (15 singularities, namely the S5-orbit of (0 : 1 : −1 :
1 : −1)).
Using the notation in Theorem 4.2, we ﬁnd that W is equivalent to the
quintic surface S(1:−676
413 ), which can be deformed in the family S(λ:µ) to the
surface (iii) in Theorem 4.2. Note that the surface (iii) in Theorem 4.2 is
32
equivalent to the quintic surface Q in (2.5). Let Φ : Y →Q be a covering
map, where Y is 2 : 1 onto the 20-nodal quintic Q ⊂CP4. The icosahedral
group A5 acts on CP4 by the standard action on the coordinates. The quintic
Q is A5-invariant and its 20 nodes are the A5-orbit of the point (2, 2, 2, −3 −
√−7, −3 + √−7). The A5-action on Q is covered by an action on Y , so
that we have an action of A5 × Z/2Z = A5 ∪A5σ on Y , where the generator
σ ∈Z/2Z is the covering involution. Elements of A5 ×Z/2Z acting on Y are
denoted like the corresponding elements acting on Q. Now, we can apply the
main result from [2]:
Proposition 4.3 (see [2] and [28]). Let α = (02)(34)σ, β = (01234).
Then β acts freely on Y and α has 4 ﬁxed points. The resolution of the
nodes of Y/D10, where D10 = ⟨α, β⟩, gives a minimal surface B of general
type with π1 = 0, q = pg = 0 and K2 = 1.
By [28], B is homeomorphic but not diﬀeomorphic to CP2#8CP
2. There-
fore, we have proved the following:
Theorem 4.4. The Barlow surface can be constructed from the modular
curve X(13).
