---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-039-1a3-the-crystalline-realization
section_title: "1A3. The crystalline realization"
section_number: null
pages: 51-52
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
the pull back of X byσ iteratedα times.
Letφ be the Frobenius of the crystalline pro-unipotent fundamental groupoid of P1\{ 0,µ N,∞}
[Deligne 1989, Sections 11 and 13.6]. It is a σ -linear isomorphism of groupoids π un,dR
1 (X(p)) ∼−→
π un,dR
1 (X). For any α∈ N∗, the Frobenius iteratedα times isφα=(σα−1)∗φ◦···◦ σ∗(φ)◦φ. It is a σα-
linear isomorphism of groupoidsπ un,dR
1 (X(pα)) ∼−→π un,dR
1 (X). Whenα is divisible by o= log(p)/log(q),
thenσα= id, thusφα is K -linear in the usual sense, its source and target are the same, and it is equal to
φo iteratedα/o times: we will write α= o˜α, andφo˜α=φ˜α
o . We denote byφ−α=φ−1
α .
Let us now consider the Frobenius at base-points (1, 0)= (⃗11,⃗10): φα: 5(pα)
1,0
∼−→51,0 where
5(pα)
1,0 =π un,dR
1 (X(pα),⃗11,⃗10). The noncommutative generating series of p-adic cyclotomic multiple zeta
values are 8p,α=τ( pα)φα(1)∈51,0(K), and 8p,−α=φ−α(1)∈5(pα)
1,0 (K). Let us denote again by
σ the map K⟨⟨e0∪µN⟩⟩→ K⟨⟨e0∪µN⟩⟩deﬁned by applying the Frobenius σ of K to each coefﬁcient of a
formal power series. The formal properties of the Frobenius imply the following formulas:
τ( pα)φα: f∈5(pα)
1,0 (K)↦→8p,α◦∫1,0σ−α( f)∈51,0(K), (1-3)
φ−α: f∈51,0(K) ↦→8p,−α◦∫1,0τ( pα)σα( f)∈5(pα)
1,0 (K). (1-4)
One also has the other notion8KZ
q ∈51,0(K) of a noncommutative generating series of p-adic cyclotomic
multiple zeta values, deﬁned by the following equality:
φlog(q)/log(p)(8KZ
q )=8KZ
q , (1-5)
where the existence and uniqueness of a ﬁxed point of φlog(q)/log(p) in51,0(K) follows from the theory
of Coleman integration [Coleman 1982; Besser 2002; V ologodsky 2003]. Item (ii) of the notation below
will be justiﬁed by the results of Section 2.
1718 David Jarossay
Notation 1A.1. (i) For any ˜α∈ Z\{ 0}, let8q,˜α=8p,log(q)/log(p)·˜α.
(ii) Let 8q,−∞=8KZ
q , and let8q,∞ be the inverse of8q,−∞ for the Ihara product◦∫1,0.
(iii) Forα∈ Z∪{±∞}\{0}, the p-adic cyclotomic multiple zeta values are the numbersζq,˜α((ni)d;(ξi)d)=
(−1)d8q,˜α[end−1
0 eξd··· en1−1
0 eξ1] (and similarly forζp,α and8p,α.)
1A4. Around the adjoint action Ad(e1). We use the convention that the adjoint action Ad(·)(x) on51,0
is f ↦→ f−1x f (instead of the usual f ↦→ f x f−1, due to our convention of reading the groupoid
multiplication from the right to the left). The adjoint Ihara action, deﬁned in [Jarossay 2015], is the group
law on Ad51,0(e1) deﬁned by
h◦
∫1,0
Ad f= f(e0,( h(ξ))ξ). (1-6)
Let˜51,0 be the subgroup scheme of51,0 deﬁned by the equations f[e1]= f[e0]= 0 (see Section 1A1);
Ad(e1) induces an isomorphism of groups (˜51,0(K),◦∫1,0) ∼−→(Ad˜51,0(K)(e1),◦
∫1,0
Ad).
By (1-1) and (1-2), one has a semidirect product Gm ⋉˜51,0, which acts on ˜51,0. Similarly, by (1-6)
and (1-2), one has a semidirect product Gm ⋉Ad˜51,0(e1), which acts on Ad˜51,0(e1). The map id× Ad(e1)
induces an isomorphism between these two group actions. For all f, g∈51,0(K),λ∈ K∗, n∈ N, we
have
g◦∫1,0(τ(λ)( f))=
∑
n∈N
λng◦∫1,0(τn f). (1-7)
We have
τn+1◦ Ad(e1)= Ad(e1)◦τn, (1-8)
Adg(e1)◦
∫1,0
Ad
τ(λ)
λ Ad f(e1)=
∑
n∈N
λn Adg(e1)◦
∫1,0
Ad τn+1 Ad f(e1). (1-9)
