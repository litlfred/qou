---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values"
section_id: sec-027-1-p1-0µ-n-restricted-to-the-rigid-analytic-secti
section_title: "(P1\{ 0,µ N,∞}), restricted to the rigid analytic sections on"
section_number: 1
pages: 33-35
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values — 33 sections: Introduction 1711; Preliminaries 1716; Iteration of the harmonic Frobeniu"
---
P1,an\⋃
ξ∈µN(K) B(ξ, 1), is given, with the conventions of [Jarossay 2019], by the formula
τ( pα)φα: f(e0,( eξ)ξ)(z)↦→ Li†
p,α(e0,( eξ)ξ)(z)× f(pα)(z pα
)(e0, Ad8(ξ)
p,α
(eξ)ξ). (5-5)
This implies the result. □
5C. Another iteration equation via regularized iterated integrals. The computation of overconvergent
p-adic multiple polylogarithms in [Jarossay 2019], which was centered around a notion of regularization
of iterated integrals, gives us another point of view on how they depend on α. Below, for a power series
S∈ K[[z]], we denote by S[zm] the coefﬁcient of zm in S for all m∈ N. Again we restrict the statement
to positive numbers of iteration of the Frobenius for simplicity, but a similar statement holds for negative
number of iterations.
Proposition 5C.1. For any wordw on e0∪µN and any m0∈ N, there exists a sequence
(c(l,ξ,n)[w](m0)) l∈N
ξ∈µN(K)
n∈N
of elements of K such that, for any˜α∈ N such that q˜α> m0 and m∈ N∗ satisfying|m− m0|p⩽ q−˜α, we
have
Li†
q,˜α[w][zm]=
∞∑
n=0
(q˜α)n
(∑
l∈N
∑
ξ
c(l,ξ,n)[w](m0)ξ−m(m− m0)l
)
.
Proof. In [Jarossay 2019, Section 3], we have deﬁned a notion of regularized iterated integrals attached
to any sequence of differential forms among pα dz
z , pαdz
z−ξ ,ξ∈µN(K), d(z pα
)
z pα−ξ pα ,ξ∈µN(K). We have
computed these regularized iterated integrals by induction on the depth, and this gives us information
on how they depend on α. Namely, each regularized iterated integral is a rigid analytic function on
P1,an\⋃
ξ∈µN(K) B(ξ, 1) which has a power series expansion∑∞
m=0 cmzm satisfying the following property:
for any m0∈{ 0,..., pα− 1}, there exists a sequence (c(l,ξ)(m0)) l∈N
ξ∈µN(K)
of elements of K such that, for
all m∈ N with|m− m0|p⩽ p−α, we have cm=∑∞
l=0
∑
ξ c(l,ξ)(m0)ξ−m(m− m0)l.
In [Jarossay 2019, Appendix B], we have showed that the numbers c(l,ξ)(m0) have an expression
as certain sums of series involving multiple harmonic sums, and particularly prime weighted multiple
harmonic sums.
1744 David Jarossay
In [Jarossay 2019, Section 4], we have showed an expression of each Li†
p,α[w] as a linear combination
of regularized p-adic iterated integrals over the ring of p-adic cyclotomic multiple zeta valuesζp,α(w′).
Combining these facts with the results of Sections 1 and 2 on how ζq,˜α and harq˜α depend on˜α, we
deduce the result. □
Appendix: A Poisson bracket corresponding to the pro-unipotent harmonic action
of integrals at(1, 0)
We have seen that, by their deﬁnitions, the pro-unipotent harmonic actions (Section 1D and Deﬁnition 2A.3)
are connected to the Ihara product (1-1). However, often in the literature, what is used is not the Ihara
product but the corresponding Lie bracket, called the Ihara bracket, which is a Poisson bracket. In
this section we explain that the pro-unipotent harmonic action of integrals at (1, 0) (Deﬁnition 2A.3)
corresponds naturally to a Poisson Lie bracket.
A.1. The Ihara bracket and the adjoint analogue. Let Vω be the group of automorphisms deﬁned in
[Deligne and Goncharov 2005, Section 5.10]. The Ihara bracket is the Lie bracket of Lie(Vω), regarded
via the isomorphism Lie(Vω)≃ Lie(51,0),v↦→v(150); namely, it is given by the following formula
[loc. cit, Section 5.12–5.13]:
{ f, g}=[ f, g]+ D f(g)+ Dg( f),
where D f is the derivation which sends e0↦→ 0 and eξ↦→[ f(ξ), eξ] for any ξ∈µN(K). The Ihara
bracket is a Poisson bracket; namely it satisﬁes the equality{ f g, h}={ f, h}g+ f{g, h}.
Let ˜Vω be the preimage of ˜51,0 by the isomorphism Vω ∼−→51,0,v↦→v(150).
We have deﬁned in [Jarossay 2015, Deﬁnition 1.1.3] the adjoint Ihara product ((1 -6)) and we have
proved in [loc. cit., Proposition 1.1.4] that Ad(e1) is an isomorphism of groups from(˜51,0(K),◦∫1,0) ∼−→
(Ad˜51,0(K)(e1),◦
∫1,0
Ad).
We have viewed Lie(˜Vω) as a subset of K⟨⟨e0∪µN⟩⟩and we can again view Lie(Ad˜Vω(e1)) as a subset
of K⟨⟨e0∪µN⟩⟩. The derivative of f↦→ f−1e1 f , the map f↦→[ e1, f] is the isomorphism of Lie algebras
deﬁned by Lie(˜Vω) ∼−→ Lie(Ad˜Vω(e1)).
Proposition A.1.1. The Lie bracket of Lie(Ad˜Vω(e1)) is{ f, g}Ad= d f(g)− dg( f) where d f is the
derivation sending e0↦→ 0, eξ↦→ f(ξ) for allξ∈µN(K).
Let the product.
∫1,0
Ad on Ad˜51,0(K)(e1) be deﬁned by(g−1e1g).
∫1,0
Ad( f−1e1 f)=(g f)−1e1(g f), and its
Lie version be[g, e1].
∫1,0
Ad[ f, e1]=[ g f, e1].
Then,{·,·} Ad is a Poisson bracket, namely, it satisﬁes{a.
∫1,0
Ad b, c}={ a, c}.
∫1,0
Ad b+ a.
∫1,0
Ad{b, c}.
Proof. Let us proceed as in the proof of Proposition 5.13 in [Deligne and Goncharov 2005]. We write
g= 1+ aϵ. When ϵ→ 0, we have(1+ aϵ)◦
∫1,0
Ad f= f+ϵdg( f)+ O(ϵ2). Thus, the action of Lie(Vω)
on Ad(˜51,0)(e1) by◦
∫1,0
Ad is by g↦→ dg. This map is injective. By the injectivity of d, we only have to
show that[d f, dg]= dd f(g)−dg( f). Since they are derivations, it is sufﬁcient to prove that these two maps
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1745
agree on e1, and this follows directly from their deﬁnitions. The fact that it is a Poisson bracket follows
from the isomorphism of Lie algebras Lie(˜Vω) ∼−→ Lie(Ad˜Vω(e1)). □
Deﬁnition A.1.2. We call{·,·} Ad the adjoint Ihara bracket.
A.2. Harmonic analogue of the Ihara bracket. We also have deﬁned in Deﬁnition 2A.3 the pro-
unipotent harmonic action of integrals at (1, 0),◦
∫1,0
har , by pushing forward the adjoint Ihara action
by the map comp6∫ (see Section 4B), which amounts to the map S of Deﬁnition 2A.2. We are now
going to push-forward{·,·} Ad by a linear and injective version of the map S of Deﬁnition 2A.2. Below,
K[[3]]⟨⟨e0∪µN⟩⟩
∫1,0
har is deﬁned like K⟨⟨e0∪µN⟩⟩
∫1,0
har with coefﬁcients in K[[3]]instead of K .
Deﬁnition A.2.1. (i) Let Sλ: K⟨⟨e0∪µN⟩⟩~o(1)→ K[[3]]⟨⟨e0∪µN⟩⟩
∫1,0
har deﬁned by
h↦→
∑
d∈N∗
ξ1,...,ξd+1∈µN(K)
n1,...,nd∈N∗
h
[ 1
1−3e0
eξd+1end−1
0 eξd··· en1−1
0 eξ1
]
eξd+1end−1
0 eξd··· en1−1
0 eξ1.
(ii) Let Lhar(K)= Sλ Lie Ad˜Vω(K)(e1).
Proposition A.2.2. Lhar(K) has a canonical Lie bracket{·,·} har deﬁned by
{S3 f, S3g}har= S3({ f, g}Ad).
It is a Poisson bracket , i.e., we have{a.
∫1,0
har b, c}={ a, c}.
∫1,0
har b+ a.
∫1,0
har{b, c}, where the product .
∫1,0
har is
deﬁned by S3g.
∫1,0
har S3 f= S3(g.
∫1,0
Ad f).
Proof. Similar to the proof of Proposition A.1.1. □
Deﬁnition A.2.3. We call{·,·} har the harmonic Ihara bracket.
Remark A.2.4. (i) The harmonic Ihara bracket{·,·} har corresponds to the group law˜◦
∫1,0
har deﬁned by
S3g˜◦
∫1,0
har S3 f= S3(g◦
∫1,0
Ad f). Because of the injectivity of S3g, the group law˜◦
∫1,0
har can be thought of as
another version of the pro-unipotent harmonic action of integrals◦
∫1,0
har of Deﬁnition 2A.3.
(ii) Another way to deﬁne a harmonic variant of the Ihara bracket would be to restrict to summable
points Ad˜51,0(K)o(1)(e1)⊂ Ad˜51,0(K)o(1)(e1) and to use comp6∫
iter , which is injective by Proposition 4B.2,
instead of comp6∫
3 .
