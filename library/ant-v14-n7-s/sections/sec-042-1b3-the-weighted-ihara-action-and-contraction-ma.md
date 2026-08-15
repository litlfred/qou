---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-042-1b3-the-weighted-ihara-action-and-contraction-ma
section_title: "1B3. The weighted Ihara action and contraction mappings"
section_number: null
pages: 53-55
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
within the topological framework reviewed above. The exponent−1∫1,0 means the inverse for the Ihara
product (1-1).
Deﬁnition 1B.2. Letκ∈ K∗ with|κ|p< 1. We say that a mapψ:51,0(K)→51,0(K) is aκ-contraction
(with respect to N3,D and◦∫1,0) if, for all f1, f2∈51,0(K), we have
N3,D(ψ( f2)−1∫
1,0◦∫1,0ψ( f1))(3, D)⩽ N3,D( f
−1∫
1,0
2 ◦∫1,0 f1)(κ3, D). (1-14)
Indeed, letψ:51,0(K)→51,0(K) be a contraction in the sense of Deﬁnition 1B.2. Then, by the
submultiplicativity of the Ihara product with respect to N3,D ((1-11)) and the fact that K⟨⟨e0∪µN⟩⟩is
complete with respect to the distance deﬁned by N3,D (Section 1B), a standard proof tells us that ψ
is continuous (with respect to N3,D) and has a unique ﬁxed point, equal to ﬁxψ= lima→∞ψa( f) for
1720 David Jarossay
all f∈51,0(K). Thus the contractions in the sense of Deﬁnition 1B.2 satisfy the usual properties of
contractions regarding ﬁxed points.
Deﬁnition 1B.3. Let(λ, g)∈ Gm(K)×51,0(K). We call weighted Ihara action by g with parameterλ
and we denote by(λ, g)◦∫1,0 the map
51,0(K)→51,0(K), f↦→(λ, g)◦∫1,0 f= g◦∫1,0τ(λ)( f).
We now relate the two previous deﬁnitions in the case where λ is small.
Proposition 1B.4. (i) Let(λ, g)∈ Gm(K)×51,0(K) such that|λ|p < 1. The map (λ, g)◦∫1,0 is a
λ-contraction. More precisely, the inequality (1-14) is an equality ifκ=λ.
(ii) For all(λ, g)∈ Gm(K)×51,0(K), the Ihara action of g weighted byλ is an automorphism of the
scheme51,0×Spec Q Spec K , whose inverse is
f↦→τ(λ−1)(g−1∫1,0◦∫1,0 f).
Proof. (i) We have
((λ, g)◦∫1,0( f2))−1∫
1,0◦∫1,0((λ, g)◦∫1,0( f1))=(g◦∫1,0τ(λ)( f2))−1∫
1,0 g◦∫1,0τ(λ)( f1)
=τ(λ)( f2)−1∫
1,0◦∫1,0 g−1∫
1,0◦∫1,0 g◦∫1,0τ(λ)( f1)
=τ(λ)( f2)−1∫
1,0◦∫1,0τ(λ)( f1)
=τ(λ)(( f2)−1∫
1,0◦∫1,0 f1).
Thus
N3,D((λ, g)◦∫1,0( f2))−1∫
1,0◦∫1,0((λ, g)◦∫1,0( f1))(3, D)= N3,Dτ(λ)(( f2)−1∫
1,0◦∫1,0 f1)(3, D)
= N3,D(( f2)−1∫
1,0◦∫1,0 f1)(λ3, D)
by (1-12).
(ii) Follows from the deﬁnitions. □
Knowing that we have a family of contractions, we consider their ﬁxed points and their iterations.
Deﬁnition 1B.5. Let(λ, g)↦→ ﬁxλ,g be the ﬁxed point map which sends(λ, g)∈{ z∈ K| 0<|z|p< 1}×
51,0(K) to the unique ﬁxed point of the weighted Ihara action (λ, g)◦∫1,0.
It follows from the deﬁnitions that the map ﬁxλ: g↦→ ﬁxλ,g is an automorphism of the scheme
51,0×Spec QSpec K , whose inverse isﬁx−1
λ : f↦→ f◦∫1,0τ(λ)( f)−1∫1,0 . The ﬁxed point map is characterized
by the equation
g(e0,( eξ)ξ) ﬁxλ,g(λe0,λ( g−1
ξ eξ gξ)ξ)= ﬁxλ,g(e0,( eξ)ξ). (1-15)
Note that the inversion for the Ihara product on 51,0(K) is characterized by
g(e0,( eξ)ξ).g−1∫1,0(e0,( g−1
ξ eξ gξ)ξ)= 1.
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1721
Deﬁnition 1B.6. Let a∈ N∗. Let the map of iteration a times of the Ihara action weighted by λ,
iter
∫1,0
a,λ:51,0(K)→51,0(K) be deﬁned by g↦→ ga(◦∫1,0,λ) where
ga(◦∫1,0,λ)=(λ, g)◦∫1,0···◦ ∫1,0(λ, g)| {z }
a
◦∫1,01= g◦∫1,0τ(λ)( g)◦∫1,0···◦ ∫1,0τ(λ a−1)(g). (1-16)
Thus ga(◦∫1,0,λ) is the unique element of 51,0(K) such that we have, for all f∈51,0(K),
(λ, g)◦∫1,0···◦ ∫1,0(λ, g)| {z }
a
◦∫1,0 f=(λa, ga(◦∫1,0,λ))◦∫1,0 f.
The iteration map is expressed in terms of the usual de Rham multiplication on 51,0(K) by
iter
∫1,0
a,λ(g)= g(e0,( eξ)ξ∈µN(K))g(λe0,(λ Adgξ(eξ))ξ)··· g(λa−1e0,(λ a−1 Adga−1
ξ
(eξ))ξ). (1-17)
