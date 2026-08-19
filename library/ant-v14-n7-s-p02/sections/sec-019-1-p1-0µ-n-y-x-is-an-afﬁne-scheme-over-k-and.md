---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values David Jarossay p-adic cyclotomic multiple zeta values depend on the choice of a n"
section_id: sec-019-1-p1-0µ-n-y-x-is-an-afﬁne-scheme-over-k-and
section_title: "(P1\{ 0,µ N,∞}, y, x) is an afﬁne scheme over K , and"
section_number: 1
pages: 8-11
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values David Jarossay p-adic cyclotomic multiple zeta values depend on the choice of a number of iterations"
---
we have a canonical embedding5y,x(K)⊂ K⟨⟨e0∪µN⟩⟩. We consider now an enrichment of K⟨⟨e0∪µN⟩⟩
into a ultrametric complete normed K -algebra: we review facts from [Jarossay 2015], and we add a
few complements. In particular, in Section 1B3 we add a notion of contraction and we apply it to the
Frobenius at base-points(1, 0).
1B1. From afﬁne schemes to ultrametric normed algebras overK . For n, d∈ N∗, let Wd∗,d(e0∪µN), resp.
Wdn,d(e0∪µN) the set of words on e0∪µN that are of depth d, resp. of weight n and depth d. Let 3 and D
be two formal variables.
Let K⟨⟨e0∪µN⟩⟩<∞⊂ K⟨⟨e0∪µN⟩⟩, be the subset of the elements f such that, for each d∈ N∗, we
have supw∈Wd∗,d(e0∪µN)| f[w]|p <∞. We say that the elements of K⟨⟨e0∪µN⟩⟩<∞ are bounded. Let
K⟨⟨e0∪µN⟩⟩o(1)⊂ K⟨⟨e0∪µN⟩⟩<∞ be the subset of the elements f such that, for each d∈ N∗, we have
supw∈ Wdn,d(e0∪µN)| f[w]|p n→∞−−−→0. We say that the elements of K⟨⟨e0∪µN⟩⟩o(1) are summable.
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1719
Let
N3,D: f∈ K⟨⟨e0∪µN⟩⟩↦→
∑
(n,d)∈N2
( max
w∈Wdn,d(e0∪µN)
| f[w]|p)3n Dd∈ R+[[3, D]],
and
ND: f∈ K⟨⟨e0∪µN⟩⟩<∞↦→
∑
d∈N
( sup
w∈Wd∗,d(e0∪µN)
| f[w]|p)Dd∈ R+[[D]].
One can check that these deﬁnitions give structures of complete normed ultrametric K -algebra on
K⟨⟨e0∪µN⟩⟩, K⟨⟨e0∪µN⟩⟩<∞ and K⟨⟨e0∪µN⟩⟩o(1) [Jarossay 2015, Proposition 1.3.3].
1B2. Compatibility between the ultrametric structure and the usual algebraic operations. By [Jarossay
2015, Proposition 1.3.6], the Ihara product (1 -1), the adjoint Ihara action (1 -6), and the action τ (1-2) are
continuous relative to the topologies deﬁned by N3,D and ND on51,0(K) and the p-adic topology on
K . And for all f, g∈51,0(K),λ∈ K×, we have (by [Jarossay 2015, proof of Proposition 1.3.6])
N3,D(Ad f(e1))⩽3DN3,D( f), (1-10)
N3,D(g◦∫1,0 f)⩽ N3,D(g)× N3,D( f), (1-11)
N3,D(τ(λ)( f))(3, D)= N3,D( f)(λ3, D). (1-12)
These equations imply similar equations with ND instead of N3,D by passing to supremums.
Let us add another compatibility, which concerns the maps τn deﬁned in Section 1A2.
Lemma 1B.1. (i) For all n∈ N∗, for all f∈ K⟨⟨e0∪µN⟩⟩, we have N3,D(τn( f))⩽ N3,D( f), and in
particularτn is a continuous linear map for the N3,D-topology.
(ii) K⟨⟨e0∪µN⟩⟩<∞ and K⟨⟨e0∪µN⟩⟩o(1) are stable byτn.
(iii) For all f, g∈51,0(K) and n∈ N we have
N3,D(Ad(g◦∫1,0τn( f))(e1))⩽3DN3,D(g)N3,D( f). (1-13)
Proof. (i) and (ii) are clear from the deﬁnitions. (iii) follows from (1-10), (1-11) and (i). □
1B3. The weighted Ihara action and contraction mappings. We deﬁne a notion of contraction mappings
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
1B4. Application to the Frobenius. We apply the previous paragraphs to study the iteration of Frobenius
at the base-points(1, 0) which we view as a map φ:5(p)
1,0(K)→51,0(K).
Lemma 1B.7. The map φ− log(q)/log(p):51,0(K)→51,0(K) is a (1/q)-contraction. If 5(p)
1,0(K) is
identiﬁed to51,0(K) by the isomorphism deﬁned by e0↦→ e0 and eξ(pα)↦→ eξ for allξ∈µN(K), the map
φ−1:51,0(K)→5(p)
1,0(K) is a(1/p)-contraction.
Proof. This follows from the formula (1-3), from Proposition 1B.4 and from the fact that σ is an isometry
of K for the p-adic metric. □
In the rest of this paper, for simplicity, we will deal mostly with the iterations of φ− log(q)/log(p). This
is sufﬁcient, knowing that, for any α∈ N∗, writing the Euclidean divisionα= r+ u log(q)/log(p), we
haveφα=φu
log(q)/log(p)◦φr.
1C. Prime weighted cyclotomic multiple harmonic sums. The numbers harqα((ni)d;(ξi)d+1) will play
a central role; here, we formally explain how to study them.
1C1. The three frameworks of computation. Multiple polylogarithms are the solutions to the Knizhnik–
Zamolodchikov differential equation, which is the universal connection associated with π un,dR
