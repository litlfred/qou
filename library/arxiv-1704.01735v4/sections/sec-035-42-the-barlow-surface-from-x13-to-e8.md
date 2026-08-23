---
doc_id: arxiv-1704.01735v4
doc_title: "Modular curves, invariant theory and E8"
section_id: sec-035-42-the-barlow-surface-from-x13-to-e8
section_title: "The Barlow surface: from X(13) to E8"
section_number: 4.2
pages: 31-33
source_pdf: 1704.01735v4.pdf
source_sha256: 3935747ae9291f76
doc_brief: "Modular curves, invariant theory and E8 — The E8 root lattice can be constructed from the modular curve X(13) by the invariant theory for the simple group PSL(2 , 13)."
---
In this section, we will construct the Barlow surface from the modu lar
curve X(13) by the method of transversal linear sections.
By Theorem 1.1, we have
Φ 12(x1(z), . . . , x6(z)) · Φ 18(x1(z), . . . , x6(z)) − Φ 30(x1(z), . . . , x6(z)) = 0 .
(4.3)
This gives a morphism
Φ : X(13) → X ⊂ CP5 (4.4)
with Φ( z) = ( x1(z), . . . , x6(z)), where the variety X is given by an equation
in six variables z1, . . . , z6 of degree 30:
Φ 12(z1, . . . , z6) · Φ 18(z1, . . . , z6) − Φ 30(z1, . . . , z6) = 0 . (4.5)
31
Moreover, we have the following morphism
ϕ : X → Z ⊂ CP13,
(z1, . . . , z6) ↦→(δ0, δ1, . . . , δ12, δ∞), (4.6)
where δ0, δ1, . . . , δ12, δ∞ are given by (1.4). The variety Z is given by



δ0 + δ1 + · · · + δ12 + δ∞ = 0,
(δ2
0 + · · · + δ2
∞)(δ3
0 + · · · + δ3
∞) − 4056
1315 (δ5
0 + · · · + δ5
∞) = 0 ,
(4.7)
which is a Fano 11-fold. Let
W = Z ∩ H1 ∩ H2 ∩ · · · ∩ H9 (4.8)
be a transversal linear section, where the hyperplane Hi := {δ4+i = 0} (1 ≤
i ≤ 8) and H9 := {δ∞ = 0}. Now, let us recall the following:
Proposition 4.2 (see [15]). In the family of quintic surfaces S(λ :µ ) in P4
given by
S(λ :µ ) = {(x0 : . . . : x4) ∈ P4 : σ1 = 0, λσ2σ3 + µσ5 = 0},
(where σk denotes the k-th elementary symmetric polynomial in x0, . . . , x4
and λ, µ ∈ C), all but the following six are non-singular :
(i) σ5 = 0 ( reducible, consisting of 5 planes, meeting along 10 lines which
in turn meet 3 at a time in 10 points),
(ii) σ2σ3 = 0 ( reducible, consisting of a quadric and a cubic surface meet-
ing along a non-singular sextic curve ),
(iii) 2 σ5 + σ2σ3 = 0 (20 singularities, namely the S5-orbit of (−2 : −2 :
−2 : 3 + √−7 : 3 − √−7)),
(iv) 25 σ5 −12σ2σ3 = 0 (10 singularities, namely the S5-orbit of (−2 : −2 :
−2 : 3 : 3)) ,
(v) 50 σ5 + σ2σ3 = 0 (5 singularities, namely the S5-orbit of (1 : 1 : 1 : 1 :
−4)),
(vi) 2 σ5 − σ2σ3 = 0 (15 singularities, namely the S5-orbit of (0 : 1 : −1 :
1 : −1)).
Using the notation in Theorem 4.2, we ﬁnd that W is equivalent to the
quintic surface S(1:− 676
413 ), which can be deformed in the family S(λ :µ ) to the
surface (iii) in Theorem 4.2. Note that the surface (iii) in Theorem 4.2 is
32
equivalent to the quintic surface Q in (2.5). Let Φ : Y → Q be a covering
map, where Y is 2 : 1 onto the 20-nodal quintic Q ⊂ CP4. The icosahedral
group A5 acts on CP4 by the standard action on the coordinates. The quintic
Q is A5-invariant and its 20 nodes are the A5-orbit of the point (2 , 2, 2, −3 −√−7, −3 + √−7). The A5-action on Q is covered by an action on Y , so
that we have an action of A5 × Z/2Z = A5 ∪ A5σ on Y , where the generator
σ ∈ Z/2Z is the covering involution. Elements of A5 × Z/2Z acting on Y are
denoted like the corresponding elements acting on Q. Now, we can apply the
main result from [2]:
Proposition 4.3 (see [2] and [28]). Let α = (02)(34) σ, β = (01234) .
Then β acts freely on Y and α has 4 ﬁxed points. The resolution of the
nodes of Y /D10, where D10 = ⟨α, β⟩, gives a minimal surface B of general
type with π1 = 0, q = pg = 0 and K 2 = 1.
By [28], B is homeomorphic but not diﬀeomorphic to CP2#8CP
2
. There-
fore, we have proved the following:
Theorem 4.4. The Barlow surface can be constructed from the modular
curve X(13).
