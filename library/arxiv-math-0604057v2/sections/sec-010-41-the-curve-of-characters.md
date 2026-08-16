---
doc_id: arxiv-math-0604057v2
doc_title: "VOLUME CONJECTURE, REGULA TOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT"
section_id: sec-010-41-the-curve-of-characters
section_title: "The curve of characters"
section_number: 4.1
pages: 7-9
source_pdf: 0604057v2.pdf
source_sha256: 649fad141dc34eb9
doc_brief: "VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER VARIETY OF A KNOT — In this paper, by using the regulator map of Beilinson-Delig ne, we show that the quan- tization condition posed by Gukov is true"
---
character varieties and its component D0.
Since ∂MK is a torus, we identify R(∂MK ) with the set {(A, B)|A, B ∈ SL2(C), AB = BA},
where A = ρ(µ), B = ρ(λ) for ρ a representation of π1(∂MK ) in SL2(C). As in Section 2 .3,
RD ⊂ R(∂MK ) is the subvariety consisting of the representations of dia gonal matrices. We have
the isomorphism p : RD → C∗ × C∗ deﬁned by p(ρ) = ( m, l) if
ρ(µ) =
[
m 0
0 m−1
]
, ρ (λ) =
[
l 0
0 l−1
]
.
Let RD be identiﬁed with C∗ × C∗ via p. By the proof of [CS, Proposition 1.4.1], χ ∈ X(∂MK ) is
determined by its values on µ, λ and µλ. Deﬁne a map t : R(∂M ) → C3 by t(ρ) = ( σ(ρ(µ)), σ(ρ(λ)), σ(ρ(µλ)))
. Then X(∂MK ) = t(R(∂MK )). This map is the regular surjective morphism t : R(∂MK ) →
X(∂MK ). That is why we use the same letter t. The map tD, the restriction of t on RD = C∗ × C∗,
is given explicitly by, for ( m, l) ∈ C∗ × C∗,
tD(m, l) = ( m + m−1, l + l−1, ml + m−1l−1).
It is straightforward to check that tD(C∗ × C∗) = X(∂MK ) and tD is 2 : 1 except at four points
(±1, ±1) where it is 1 : 1.
We have the following diagram:
8 WEIPING LI AND QINGXUE W ANG
R(MK) ⊃ R0 D0 = t−1
D (Y0) ⊂ C∗ × C∗ = RD ⊂ R(∂MK )
t


↓ tD


↓
X(MK ) ⊃ X0 = t(R0) r− − − − → Y0 =
r(X0) ⊂ X(∂MK ).
First we characterize the map tD and the character variety X(∂M ).
Proposition 4.1. The map tD : RD = C∗ × C∗ → X(∂MK ) is a ﬁnite morphism.
Proof. The aﬃne coordinate ring for C∗ × C∗ is C[x, x−1, y, y−1]. Notice that tD is surjective, we
can identify the coordinate ring of X(∂MK ) with the sub-ring C[x + x−1, y + y−1, xy + x−1y−1] of
C[x, x−1, y, y−1]. Let t = x + x−1, then x and x−1 are roots of the equation X 2 − tX + 1 = 0. Hence
x and x−1 are integral over C[x + x−1, y + y−1, xy + x−1y−1], so are y and y−1. Now x, x−1, y, y−1
are integral over C[x + x−1, y + y−1, xy + x−1y−1], it follows that C[x, x−1, y, y−1] is also integral
over it. Therefore, tD is ﬁnite. □
Proposition 4.2. The character variety X(∂MK ) is a surface in C3 deﬁned by
(4.1) x2 + y2 + z2 − xyz − 4 = 0 .
Proof. Let x, y, z be the traces of a = ρ(µ), b = ρ(λ), c = ρ(µλ) respectively. By the formula
(5.14), we have
σ((ab)a−1b−1) = σ(ab)σ(a−1b−1) + σ(a−1)σ(a) + σ(b−1)σ(aba−1) − σ(ab)σ(a−1)σ(b−1) − σ(I).
Since a and b commute, σ((ab)a−1b−1) = σ(I) = 2, where I is the 2 × 2 identity matrix. This
gives the equation (4.1) by (5.11) and (5.12). Hence, X(∂MK ) is contained in the surface in C3.
On the other hand, let ( x, y, z) ∈ C3 be a solution to (4.1). It is a straightforward calculation
that we can ﬁnd ( m, l) ∈ C∗ × C∗ such that x = m + m−1, y = l + l−1, and z = ml + m−1l−1.
Hence the result follows. □
For each γ ∈ π1(MK ), there is a natural regular map Iγ : X(MK ) → C deﬁned by Iγ (χ) = χ(γ).
The set of functions Iγ , γ ∈ π1(MK ) generates the aﬃne coordinate ring of X(MK ). Moreover, by
[CGLS, Proposition 1.1.1], for each nonzero γ ∈ π1(∂MK ), the function Iγ is non-constant on X0.
This implies that r(X0) ⊂ X(∂MK ) has dimension 1. We set Y0 = r(X0), the Zariski closure of
r(X0) in X(∂MK ). Then Y0 is an irreducible aﬃne curve. Denote by D0 the inverse image t−1
D (Y0).
Proposition 4.3. (i) The inverse image D0 ⊂ C∗ × C∗ is an aﬃne algebraic set of dimension 1;
(ii) the image of each 1-dimensional component of D0 under tD is the whole Y0;
(iii) D0 has no 0-dimensional components and has at most two 1-dimensional components.
Proof. (i). As Y0 is closed, so is D0 = t−1
D (Y0). Thus D0 and Y0 have the same dimension 1 because
tD is ﬁnite by Proposition 4.1.
(ii). Next we show that if V is a 1-dimensional irreducible component of D0, then tD(V ) = Y0.
In fact, since a ﬁnite morphism maps closed sets to closed set s, tD(V ) ⊂ Y0 is closed, irreducible
and its dimension is 1. Hence tD(V ) = Y0 due to the irreducibility of Y0.
(iii). Suppose that D0 has three distinct 1-dimensional components Vi, 1 ≤ i ≤ 3. Since the
Vi ∩ Vj, i ⁄= j are empty or ﬁnite sets, we can choose y0 ∈ Y0 such that y0 /∈ tD(Vi ∩ Vj) for ∀i ⁄= j.
We see that tD(Vi) = Y0, hence t−1
D (y0) has three elements. This contradicts that t−1
D (y) has at most
two elements for any y ∈ Y0. Therefore, D0 has at most two 1-dimensional irreducible components.
Now we show that it has no 0-dimensional components. Conside r the morphism σ : C∗ × C∗ →
C∗ × C∗ deﬁned by σ(m, l) = ( m−1, l−1). It is an involution and hence an automorphism of C∗ × C∗
with σ(D0) = D0. So it is an automorphism of D0 when restricting on it. Therefore it maps
1-dimensional component to 1-dimensional component. Now f or any y ∈ Y0, σ permutes elements
of t−1
D (y) and at least one element of t−1
D (y) is contained in some 1-dimensional component since tD
maps every 1-dimensional component onto Y0. Therefore, no 0-dimensional component for D0. □
VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT 9
Remark. For the character variety X(MK ), by [CCGLS, Proposition 2.4] , there is no zero-
dimensional components of X(MK ). Proposition 4.3 part (iii) shows that D0 in RD ⊂ R(∂MK )
has no 0-dimensional components.
In summary, we have the following two cases:
(I) D0 itself is an irreducible aﬃne curve;
(II) D0 = V1 ∪ V2, where Vi are two 1-dimensional irreducible components. Each is an ir reducible
aﬃne curve with tD(Vi) = Y0, i = 1 , 2. Moreover, they are isomorphic to each other under the
involution σ by Proposition 4.3 (iii) . We also have tD : Vi → Y0 is a one-to-one and onto regular
map.
