---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-008-34-the-lawrence-krammer-bigelow-representation
section_title: "The Lawrence-Krammer-Bigelow representation"
section_number: 3.4
pages: 13-15
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
---
The Lawrence-Krammer-Bigelow representation
We will now discuss another homological representation introduced by R. Lawrence [23] and
studied by D. Krammer [22] and S. Bigelow [4]. Let us ﬁx a natural number n ≥1 and denote
by D the unit disk with n distinguished points Q = {p1, . . . , pn}. We also set
Σ := D −Q, F := ˆC2(Σ), C := C2(Σ).
Here we use the notation introduced above for conﬁguration spaces. That is, F is the con-
ﬁguration space of two ordered points in Σ, and C is the conﬁguration space of two unordered
points in Σ. There is a natural double sheeted covering F →C. A point in C is an unordered
set of distinct points of Σ and we use the notation {x, y} for points of C. A path in C can be
represented as a pair of paths {ζ1, ζ2} where ζi : I →Σ such that for all s ∈I, ζ1(s)̸ = ζ2(s).
A loop in C is a path such that {ζ1(0), ζ2(0)} = {ζ1(1), ζ2(1)}. That is, a pair of maps (ζ1, ζ2)
deﬁnes a loop in C if either they deﬁne a loop in F or deﬁne a path in F that permutes the
starting points.
Given a loop ζ = {ζ1, ζ2} in C we deﬁne the number w(ζ) ∈Z as follows. If the pair (ζ1, ζ2)
deﬁnes a loop in F, then each of the ζi are loops in Σ and we set
w(ζ) := φ(ζ1) + φ(ζ2),
where, as above, φ is the group homomorphism that counts the total winding number with
respect to Q.
If the pair (ζ1, ζ2) does not deﬁne a loop in F, then it deﬁnes a path that
permutes the endpoints. Therefore ζ1 ◦ζ2 deﬁnes a loop is Σ and we set:
w(ζ) := φ(ζ1 ◦ζ2).
We deﬁne a second numerical invariant u(ζ) as follows. Consider the map γζ : I →S1 given
by the formula:
γζ(s) :=
 ζ1(s) −ζ2(s)
|ζ1(s) −ζ2(s)|
2
.
Observe that this map is well deﬁned for ζ, since ζ1 and ζ2 play a symmetric role. Since ζ is a
loop, we also conclude that γζ(0) = γζ(1) and therefore γζ deﬁnes a map S1 →S1 whose degree
is the value of u at ζ. It is a simple exercise to prove that the maps w and u are well deﬁned on
homotopy classes and are group homomorphisms π1(C) →Z.
We ﬁx two distinct points d1, d2 ∈∂(Σ) and take {d1, d2} as the basepoint of C. We denote
by
ρ : π1(C, {d1, d2}) →Z ⊕Z,
13
the group homomorphism given by the formula:
ρ(ζ) = qw(ζ)tu(ζ),
where q and t are the canonical generators of Z ⊕Z.
Lemma 3.14. The group homomorphism ρ : π1(C, {d1, d2}) →Z ⊕Z is surjective.
Proof. It suﬃces to prove that both q and t are in the image of ρ. Let us ﬁrst prove that q
is in the image. Let ζ = {ζ1, ζ2} be the loop in C such that ζ1 is constant and ζ2 is a small
counterclockwise loop around p1. Then:
w(ζ) = φ(ζ1) + φ(ζ2) = 1.
Since ζ2 stays close to p1 and ζ1 is constant, we conclude that u(ζ) = 0. Thus ρ(ζ) = q.
Let us now prove that t is in the image of ρ. Consider a small disk B ⊂Σ and deﬁne the loop
ϕ = {ϕ1, ϕ2} as follows. Fix two distinct points x, y ∈∂(B). Set ϕ1 the path that goes along
∂B from x to y in counterclockwise direction and ϕ2 the path that goes along ∂B from y to x
in counterclockwise direction. Then:
w(ϕ) = φ(ϕ1 ◦ϕ2) = 0,
and
u(ϕ) = deg(id) = 1.
We conclude that ρ(ϕ) = t.
□
Let ˜C →C be the covering space that corresponds to the subgroup ker(ρ) of π1(C, {d1, d2}).
The group Z ⊕Z acts as the group of deck transformations of ˜C. Therefore, the space
H := H2( ˜C, Z),
has the structure of a module over the ring:
R := Z[q, q−1, t, t−1].
We will now describe an action of the braid group Bn on the R-module H. We will again use
the identiﬁcation
Bn ∼= Mod(D, Q).
Take a homeomorphism f of D that ﬁxes the boundary pointwise and permutes the elements
of Q. The map f induces a homeomorphism ˆf : C →C given by:
ˆf({x, y}) := {f(x), f(y)}.
Since f ﬁxes the boundary pointwise, we know that ˆf({d1, d2}) = {d1, d2} and therefore ˆf
induces an isomorphism ˆf∗: π1(C, {d1, d2}) →π1(C, {d1, d2}).
Lemma 3.15. The homomorphism ˆf∗preserves the invariant ρ, i.e. ρ ◦ˆf∗= ρ.
14
Proof. We need to prove that w ◦ˆf∗= w and u ◦ˆf∗= u. The ﬁrst statement reduces to the
fact that the total winding number is preserved by ˆf∗, which we have already seen. Let us now
prove the second statement. Consider the inclusion of conﬁguration spaces:
ι : C = C2(Σ) ,→C2(D),
induced by the inclusion Σ ,→D. The deﬁnition of the invariant u can be extended word by
word to an invariant ˆu of loops in C2(D) in such a way that the diagram:
π1(C, {x, y})
ι /
u
)
π1(C2(D), {x, y})
ˆu

Z
commutes.
On the other hand, ˆf extends to a homeomorphism f of C2(D) which, by the
Alexander-Tietze theorem proved in Example 2.9, is isotopic to the identity. Thus f acts trivially
on the fundamental group of C2(D). Then, for any element γ ∈π1(C, {x, y}):
u ◦ˆf∗(γ) = ˆu ◦ι ◦ˆf∗(γ) = ˆu ◦f∗◦ι ◦γ = ˆu ◦ι(γ) = u(γ).
□
The previous lemma implies that the homeomorphism ˆf lifts naturally to a homeomorphism
˜f : ˜C →˜C that commutes with the deck transformations of the covering. This homeomorphism
induces a homomorphism in homology ˜f∗: H2( ˜C, Z) →H2( ˜C, Z).
Deﬁnition 3.16. The Lawrence-Krammer-Bigelow representation of the braid group Bn is the
homomorphism:
Bn →AutR(H2( ˜C, Z)),
given by the formula:
f 7→˜f∗.
Theorem 3.17 (Krammer [22], Bigelow [4]). The following statements hold for all n ≥2:
1. There is a natural isomorphism of R-modules:
H ∼= R
n(n−1)
2
.
2. The Lawrence-Krammer-Bigelow representation Bn →AutR(H) is faithful.
Proof. The interested reader may consult [18] Theorem 3.15.
□
The second statement of the theorem implies that Bn is a linear group, i.e. it is isomorphic to
a group of matrices with real coeﬃcients. This can be obtained by setting q, t to be algebraically
independent real numbers.
