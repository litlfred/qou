---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-010-34-the-lawrence-krammer-bigelow-representation
section_title: "The Lawrence-Krammer-Bigelow representation"
section_number: 3.4
pages: 13-15
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
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
the group homomorphism given by the formula:
le) = are",
where q and t are the canonical generators of Z @ Z.
Lemma 3.14. The group homomorphism p : 7(C, {di,d2}) > Z© Z is surjective.

Proof. It suffices to prove that both q and ¢ are in the image of p. Let us first prove that q
is in the image. Let ¢ = {¢1,¢2} be the loop in C such that ¢) is constant and ¢ is a small
counterclockwise loop around p;. Then:

w(d) = (4) + o(@) = 1.

Since ¢9 stays close to p; and ¢, is constant, we conclude that u(¢) = 0. Thus p(¢) = q.

Let us now prove that t is in the image of p. Consider a small disk B C ¥ and define the loop
vp = {¥1,%2} as follows. Fix two distinct points x,y € 0(B). Set y; the path that goes along
OB from «x to y in counterclockwise direction and y2 the path that goes along 0B from y to x
in counterclockwise direction. Then:

w(y) = o(¥1° v2) = 0,
and
u(y) = deg(id) = 1.
We conclude that p(y) = t. o

Let C > C be the covering space that corresponds to the subgroup ker(p) of 7(C, {d1, do}).
The group Z @ Z acts as the group of deck transformations of C. Therefore, the space

H := H(C,Z),
has the structure of a module over the ring:

R:=2Zlq,q1,t,t7].

We will now describe an action of the braid group B, on the R-module H. We will again use
the identification
Br, = Mod(D,Q).

Take a homeomorphism f of D that fixes the boundary pointwise and permutes the elements
of Q. The map f induces a homeomorphism f : C > C given by:

f({x,y}) = {f(@), Fw)}-

Since f fixes the boundary pointwise, we know that f ({d1,d2}) = {di,d2} and therefore f
induces an isomorphism f, : 71(C, {di,d2}) > ™1(C, {di, do}).

Lemma 3.15. The homomorphism fe preserves the invariant p, i.e. po fe =p.

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
