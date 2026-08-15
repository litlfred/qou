---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-163-4-heights-and-bogomolov-constants
section_title: "Heights and Bogomolov constants"
section_number: 4
pages: 322-323
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
We recall the deﬁnition of the absolute Weil height function h: K→ R for a number ﬁeld K . For each
ﬁnite extension L/K , denote by ML the set of places of L, and for each placev let|·|v be a corresponding
absolute value normalized so that it coincides with either the standard real or p-adic absolute value when
restricted to Q. Givenα∈ K , Let L/K be a ﬁnite extension containing α, and deﬁne
h(α)=
∑
v∈ML
rv log+|α|v (5)
where rv=[ Lv: Qv]/[L: Q] and log+ t= log max(1, t). Standard arguments show that this deﬁnition
is independent of the choice of L, and that h(α)≥ 0 for allα∈ K , with h(α)> 0 unlessα is zero or
a root of unity. It is immediate from the deﬁnition that h(ζα)= h(α) for all roots of unity ζ , and that
h(αn)=| n|h(α) for all n∈ Z.
Given a ﬁeld K⊆ L⊆ K (with L/K not necessarily a ﬁnite extension), deﬁne the Bogomolov constant
of L by
B0(L)= lim inf{h(α)|α∈ L and h(α)> 0}.
In other words, B0(L) is the unique extended real number [0,+∞] with the property that the set
{α∈ L| 0< h(α)≤ B} is ﬁnite for all B< B0(L) and inﬁnite for all B> B0(L).
Theorem 9 [Amoroso and Zannier 2000]. If L/K ab is a ﬁnite extension of degree D=[ L: K ab], then
h(α)≥ CK,D> 0 for all nonzero, nonroot of unityα∈ L, where CK,D is a constant depending only on K
and D. In particular , B0(L)≥ CK,D> 0.
This result generalizes a result of Amoroso and Dvornicich [2000], which states that h(α)≥(log 5)/12
for all nonzero, nonroot of unity α∈ Qab. In particular, B0(Qab)≥(log 5)/12. For our purposes, another
useful result from the paper [Amoroso and Dvornicich 2000] is the following. For each k≥ 1, let
ζk be a primitive k-th root of unity in C, and let µk be the group of all k-th roots of unity in C. Let
µ2∞=⋃
m≥1µ2m; thus Q(µ2∞)=⋃
m≥1 Q(ζ2m).
Theorem 10 [Amoroso and Dvornicich 2000]. Ifα∈ Q(µ2∞) is nonzero and not a root of unity, then
h(α)≥(log 2)/4. In particular, B0(Q(µ2∞))≥(log 2)/4.
Basically all of the ideas needed to prove this result are present in Proposition 2 of [Amoroso and
Dvornicich 2000], which treats the cyclotomic ﬁelds Q(ζk) for 4| k. The statement of the height bound
in that result excludes certain elements of Q(ζk), but we can easily recover the bound for these excluded
elements in the special case that k= 2m. As it may be of some interest, we include the complete proof in
this case.
Proof of Theorem 10. If ζα ∈ Q for some root of unity ζ∈ Q(µ2∞), then ζα /∈{ 0,±1} and so
h(α)= h(ζα)≥ log 2>( log 2)/4. Thus we may assume thatζα/∈ Q for all roots of unityζ∈ Q(µ2∞). Let
m be the smallest positive integer with the property that ζα∈ Q(ζ2m) for some root of unity ζ∈ Q(µ2∞);
Abelian extensions in dynamical Galois theory 1989
thus m≥ 2 by assumption. Since h(ζα)= h(α), without loss of generality we may just assume that
α∈ Q(ζ2m) and thatζα /∈ Q(ζ2m−1) for all roots of unity ζ∈ Q(µ2∞).
Write Gal(Q(ζ2m)/Q(ζ2m−1))={ 1,σ}; thusσ(ζ 2m)=−ζ2m. Set
γ=σ(α) 2−α2.
Note thatγ⁄= 0 as otherwise eitherσ(α)=α orσ(α)=−α; the former case implies α∈ Q(ζ2m−1), and
the latter case impliesζ2mα∈ Q(ζ2m−1), both of which are forbidden by assumption.
Ifv is a place of Q(ζ2m), then
|γ|v≤ max(1,|α|v)2 max(1,|σ(α)|v)2 ifv ∤2,∞ (6)
|γ|v≤ 1
4 max(1,|α|v)2 max(1,|σ(α)|v)2 ifv| 2 (7)
|γ|v≤ 2 max(1,|α|v)2 max(1,|σ(α)|v)2 ifv|∞ (8)
These inequalities and the product formula, together with the fact that h(σ(α))= h(α), imply that
0=∑
v rv log|γ|v≤ 4h(α)− log 4+ log 2, and the desired bound h(α)≥(log 2)/4 follows. The bounds
(6) and (8) are trivial applications of the triangle inequality.
It remains only to prove (7); thus ﬁx a place v| 2 of Q(ζ2m). Using Proposition Lemma 4.4.12 of
[Bombieri and Gubler 2006], there exists β∈ Z[ζ2m] such thatαβ∈ Z[ζ2m] and|β|v= max(1,|α|v)−1.
Note that for arbitrary x∈ Z[ζ2m], writing x=6 ja jζ j
2m, sinceσ(ζ 2m)=−ζ2m we have
σ( x)2− x2=(σ( x)− x)(σ( x)+ x)=− 4
(∑
2∤ j
a jζ j
2m
)(∑
2| j
a jζ j
2m
)
and thus|σ( x)2− x2|v≤ 1
4. We conclude
|β|2
v|γ|v=|β2σ(α) 2−α2β2|v
=|(β2−σ(β) 2)σ(α) 2+σ(αβ) 2−(αβ)2|v
≤ max(|β2−σ(β) 2|v|σ(α)|2
v,|σ(αβ) 2−(αβ)2|v)
≤ max
( 1
4|σ(α)|2
v, 1
4
)
= 1
4 max(1,|σ(α)|v)2,
which is equivalent to (7) as|β|v= max(1,|α|v)−1. □
