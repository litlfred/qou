---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-014-11-a-conjecture-of-joseph
section_title: "A conjecture of Joseph"
section_number: 11
pages: 26-28
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
The asymptotic relation
θΓ (λ) = cΓ (λ)θO + o(|λ|e)
(1)
may be used to prove a conjecture of Joseph [1984, Conjecture 9.8]. The conjecture may be explained as
follows. Let
T = {(b, ν)|b ∈Bo, ν ∈b⊥∩bo
⊥}.
(2)
This is the conormal variety of the action of the ﬁxed Borel subgroup Bo of Go on the ﬂag manifold Bo
of Go. (The complexiﬁcation of Go does not enter into the picture here.) T is also the inverse image
Bo
∗(bo
⊥) of bo
⊥under the Springer map Bo
∗→No. Its dimension is no = dimCBo
∗and our general
construction gives a representation of Wo on H∗(T ). In top degree, H2no(T ) has as basis the fundamental
cycles of the components of T . These components are the closures of the conormal bundles Tw of the
Bo-orbits Bo · w−1bo:
Tw = {Bo · (w−1bo, ν)|ν ∈bo
⊥∩w−1bo).
(3)
For each w ∈Wo there is a unique Go-orbit O = O(w) on No which intersects bo
⊥∩w−1bo densely; and for
each O the components of O ∩bo
⊥are the closures in O ∩bo
⊥of the dense parts of the Bo · (bo
⊥∩w−1bo)
cut out by O when O(w) = O. For a given O these components V(w) of O ∩bo
⊥all have the same
dimension = 1
2dimO. (For these results see Steinberg [1976] and Joseph [1984].) To each such subvariety
V(w) of No Joseph associates a polynomial pV(w) on h∗
o, homogeneous of degree no −1
2dimO. This degree
= eo = dimBoν for ν ∈O. Joseph’s conjecture says that if one writes
Zw =

y∈Wo
A(w, (y, 1))(y, 1) · Z1
(4)
REPRESENTATIONS OF WEYL GROUPS
27
in the homology H2n(Z) of the conormal variety Z , then
pV(w) = const.

y∈Wo
A(w, (y, 1))y · ρoeo,
(5)
and the exponent eo = dimBoν in this relation is the least for which the right side is non-zero.
ρo
denotes half the sum of the roots of ho in bo
⊥, which must here be thought of as an element of ho by
meansof a Wo-invariant bilinear form (Joseph identiﬁes ho and ho
∗); in (5) we take (y, 1) as element of
W = Wo × Wo and use the W-action on the homology of Z deﬁned earlier (which by section 12 is also
the action constructed by Kazhdan-Lusztig [1980], to which Joseph refers. Joseph writes this action of
Wo × Wo as a Wo–Wo bimodule.)
To prove the conjecture we consider the projection B∗= Bo
∗× Bo
∗→Bo through the second
factor. It restricts to a ﬁbration
T ⊂
→Z →Bo
(6)
with T as in (2) as ﬁbre over bo. The components Zw of Z meet the ﬁbre T in the components Tw of T .
For any ν ∈bo
⊥there is a diagram
Bo
ν
⊂
→
T
→
bo
⊥
∩
∩
∩
Bo
ν
⊂
→
Z
→
N
(7)
For a given Go-orbit O on No and ν ∈O∩bo
⊥, Zw meets the ﬁbre Bν of Z →N in a single Ao(ν)-orbit of
components; Tw meets the ﬁbre Boν of T →bo
⊥in a union of components which lie in a single Ao(ν)-orbit
and determine an element of H2eo(boν)Ao(ν). (For these facts see Spaltenstein [1977].) According to a result
of Hotta [1984], the map which sends pV(w) to this element of H2eo(Boν)Ao(ν) extends to a Wo-isomorphism
of the space spanned by the pV(w) , O(w) = O, onto H2eo(Boν)Ao(ν).
On the other hand, the inclusion Boν ⊂
→Bo gives a Wo-injection H2eo(Boν)Ao(ν) →H2eo(Bo) ≈
H(ho), as we know from sections 3 and 7. Hence the element of H2eo(Boν)Ao(ν) mentioned above gives
rise to another (harmonic) polynomial on ho
∗, homogeneous of degree eo. Because of Lemma 8.1, this
polynomial must be pV(w) up to a (non-zero) factor depending only on O.
To make use of the relation (1) note that the ﬁbration (6) leads to a Wo × {1}-isomorphism
H2n(Z) →H2no(T ) which sends the fundamental cycle of Zw to the fundamental cycle of Tw. From
Theorem 5.1 we know that the relation
Zw =

y∈Wo
A(w, (y, 1))(y, 1) · Z1
(4)
implies that
θSw =
(−1)n
π

y∈Wo
A(w, (y, 1))e(y−1,1)λ.
(8)
Of course, we also know that
A(w, y) = (−1)l(w)−l(y)Euy(Zw),
(9)
REPRESENTATIONS OF WEYL GROUPS
28
but this will not even be needed. Rather, we use the formula (9.8) to write
cw(λ) = kO

y∈Wo
A(w, (y, 1))⟨λ1, y · λ2⟩eo.
(10)
On the other hand, the polynomial cw represents the fundamental cycle of the component Bν
w of Bν in
H2e(B) ≈H(h). Since Bν = Boν × Boν that component must factor Bν
w = Cw × C′
w as a product of a pair
of components of Boν depending on w. These two components correspond to two harmonic polynomials
pw , p′
w on ho
∗and the factorization Bν∗w = Cw × C′
w means that
cw(λ) = pw(λ1)p′
w(λ2)
(11)
if λ = (λ1, λ2) in h∗= ho
∗× ho
∗. From the discussion around diagram (7) it is clear that
pw = const.pV(w).
To prove Joseph’s conjecture we may therefore replace pV(w) by pw in (5). From (10) and (11) one ﬁnds
pw(λ1) =
kO
p′w(λ2)

y∈Wo
A(w, (y, 1))⟨λ1, y · λ2⟩eo
provided p′
w(λ2)̸ = 0, which know to be the case for regular λ2. Choosing λ2 = ρo we get the formula
conjectured by Joseph:
pV(w) = const.

y∈Wo
A(w, (y, 1))y · ρoeo.
For the record we point out once more that we have actually proved the more precise formula
pV(w) = const.

y∈W/Wo
(−1)l(w)−l(y)Euy(Zw)y · ρoeo.
(12)
for a constant depending only on O.
