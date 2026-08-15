---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-005-4-projective-pushforward-in-twisted-cohomology
section_title: "Projective pushforward in twisted cohomology"
section_number: 4
pages: 21-25
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
In this section, we describe how one gets projective pushforward maps in twisted E-cohomology for E
an SL-oriented motivic spectrum. We rely on the six-functor formalism. This is a bit different from the
treatment of projective pushforward given by Ananyevskiy [2016a]: in that treatment, one relies on the
factorization of an arbitrary projective morphism Y→ X into a closed immersion Y→ X× PN followed
by a projection X× PN→ X. This factorization property will however reappear in our treatment when
we discuss the uniqueness of the pushforward maps in Section 6.
We continue to work over a noetherian separated base scheme B of ﬁnite Krull dimension.
Lemma 4.1. Let s: Y→ X be a section of a smooth morphism p: X→ Y and let η: id→ s∗s∗,
ϵ: s∗s∗→ id be unit and counit of adjunction. Then the composition
idSH(Y)−→∼ p!◦ s!= p!◦ s∗
s∗
→ s∗◦ s∗
ϵ→ idSH(Y)
is the identity. Here the morphism s∗: p!→ s∗ is the one constructed in Remark 2.9.
Proof. The functor s∗s∗ is an equivalence [Hoyois 2017, Corollary 4.19]. As a general property of adjoint
functors, s∗ϵs∗◦ηs∗s∗= ids∗s∗ (see, e.g., [Mac Lane 1971, p. 134]), hence s∗ϵs∗s∗◦ηs∗s∗s∗= ids∗s∗s∗
and thus s∗ϵ◦ηs∗= ids∗. The result follows from the commutative diagram
id
≀

pX!◦ s∗
pX!ηs∗

id
’’
s∗
&&
pX!◦ s!
pX!◦ s∗s∗s∗
pX!s∗ϵ // pX!◦ s∗
pX!◦ s!◦ s∗◦ s∗
≀

pX!s!ϵ // pX!◦ s!
≀

s∗◦ s∗ ϵ
// id □
Remark 4.2. Let s: Y→ V be the zero-section of a vector bundle p: V→ Y. Then the canonical
isomorphism idS H(Y)≃ p!s∗ is equal to the composition
idSH(Y)≃6−V6V=6−V p#s∗≃ p#6−p∗V s∗≃ p!s∗.
1822 Marc Levine and Arpon Raksit
Indeed6−V6V→ idSH(Y) is the counit of the adjunction 6−V⊢6V, corresponding to id:6V→6V,
6−V p#s∗→ idSH(Y) is the counit of the adjunction 6−V= s! p∗⊢ p#s∗. The functors 6−V and p# are
both left adjoints, so6−V p# is left adjoint to s∗ and the counit of the adjunction
6−V p#⊢ p∗6V≃6 p∗V p∗≃ p!≃ s∗
is the same as that of 6−V⊢ p#s∗. Composing with the isomorphism p!≃ p#6−p∗V≃6−V p#, we see
that the counit of the adjunction p!⊢ s∗ is induced from that of 6−V p#⊢ s∗, and thus agrees with the
canonical isomorphism p!s∗≃ idSH(Y).
Lemma 4.3. Let(E, th(−)) be an SL-oriented motivic spectrum in SH(B). Suppose given X∈ SmB of
dimension dX over B, i: Z→ X a closed subset, and p: L→ X a line bundle. Then the isomorphism
ϑ E
L−TX/B:61−det(L−TX/B)π∗
X E→6rL−TX/B−L+TX/Bπ∗
X E
induces an isomorphism
ρX,Z,L: Ea,b
Z (X;ωX/B⊗ L)≃ Ea−2dX,b−dX(X Z/BB.M.; L),
where the right-hand side is as deﬁned in Remark 3.9.
Proof. We have det(L− TX/B)= det−1(TX/B)⊗ L=ωX/B⊗ L and rL−TX/B= 1− dX. Moreover, we
have canonical isomorphisms
Ea,b
Z (X;ωX/B⊗ L)≃ HomSH(X)(i∗(1Z), Sa,b∧61−ωX/B⊗Lπ∗
X E)
and
Ea−2dX,b−dX(X Z/BB.M.; L)≃ HomSH(X)(i∗(1Z), Sa,b∧6(1−dX)+TX/B−Lπ∗
X E).
Finally,ϑ E
L−TX/B induces the isomorphism
Sa,b∧ϑ E
L−TX/B: Sa,b∧61−ωX/B⊗Lπ∗
X E→ Sa,b∧6(1−dX)+TX/B−Lπ∗
X E,
which completes the proof. □
Using the isomorphismsρX,Z,L, we make the following deﬁnition.
Deﬁnition 4.4. Let(E, th(−)) be an SL-oriented motivic spectrum inSH(B), let f:Y→ X be a proper mor-
phism of relative dimensiond in SmB, let L→ X be a line bundle, and letZ⊂ X be a closed subset. Deﬁne
f∗: Ea,b
f−1(Z)(Y,ω Y/B⊗ f∗L)→ Ea−2d,b−d
Z (X,ω X/B⊗ L)
to be the unique map making the diagram
Ea−2dY,b−dY(Y f−1(Z)/BB.M.; f∗L)
( f∗)∗
// Ea−2dY,b−dY(X Z/BB.M.; L)
Ea,b
f−1(Z)(Y,ω Y/B⊗ f∗L)
ρY, f−1 Z, f∗ L
OO
f∗
// Ea−2d,b−d
Z (X,ω X/B⊗ L)
ρX,Z,L
OO
commute.
Motivic Gauss–Bonnet formulas 1823
Let p: V→ Y be a rank r vector bundle on some Y∈ SmB, with 0-section s: Y→ V. Letting
L= det V, the exact sequence
0→ p∗V→ TV/B
dp−→ p∗TY/B→ 0
gives the canonical isomorphismωV/B≃ p∗(det−1 V⊗ωY/B), or p∗ det−1 V≃ωV/B⊗ω−1
Y/B. Letting
(E, th) be an SL-oriented motivic spectrum, we have the pushforward map
s∗: Ea,b(Y)→ Ea+2r,b+r(V, p∗ det−1 V),
and the version with supports,
s∗: Ea,b(Y)= Ea,b
Y (Y)→ Ea+2r,b+r
0V (V, p∗ det−1 V).
Lemma 4.5. Let 1E
Y∈ E0,0(Y) be the unitπ∗
Y/B(u). Then
s∗(1E
Y)= thV∈ E2r,r
0V (V, p∗ det−1 V).
As a consequence, s∗(1E
Y) in E2r,r(V, p∗ det−1 V) is the image of thV under the “forget supports” map
E2r,r
0V (V, p∗ det−1 V)→ E2r,r(V, p∗ det−1 V).
Proof. The exact sequence
0→ p∗V→ TV/B
dp−→ p∗TY/B→ 0
gives us the isomorphism
ω−1
V/B⊗ det−1 V≃ p∗ω−1
Y/B.
Keeping this in mind, we have the following commutative diagram deﬁning s∗:
E−2dY,−dY(Y/BB.M.;ω−1
Y/B)
(s∗)∗
// E−2dY,−dY
0V (V/BB.M., p∗ω−1
Y/B)
E0,0
Y (Y)
ρY,Y,s∗ p∗ω−1
Y/B
OO
s∗
//
s∗ **
E2r,r
0V (V, det−1 V)
ρV,0V,p∗ω−1
Y/B
OO
forget supports

E2r,r(V, det−1 V)
(4.5.1)
Here the lower s∗ is the one we are considering and the upper s∗ is the map with supports. Thus, we need
to show that the upper s∗ satisﬁes s∗(1E
Y)= thV .
We will be using the isomorphisms
E−2dY,−dY(Y/BB.M.;ω−1
Y/B)≃ HomSH(Y)(1Y,6 1−dY+TY/B−ω−1
Y/Bπ∗
Y E),
E−2dY,−dY
0V (V/BB.M., p∗ω−1
Y/B)≃ HomSH(V)(s∗(1Y),6 1−dY+TV/B−p∗ω−1
Y/Bπ∗
V E),
E2r,r
0V (V, det−1 V)≃ HomSH(V)(s∗(1V),6 r+1−det−1 Vπ∗
V E).
(4.5.2)
1824 Marc Levine and Arpon Raksit
By Lemma 4.1, the composition
πY!−→∼ πV!◦ s!
πV!α−−→πV!◦ s∗ s∗
→πY!
is the identity. Evaluating at 1Y gives the commutative diagram
YB.M.
φ
∼
//πV!(s∗(1Y))
s∗
xx
V0V/BB.M.
YB.M.
(4.5.3)
and the isomorphismφ induces the isomorphism
φ∗: E−2dY,−dY
0V (V/BB.M., p∗ω−1
Y/B)→ E−2dY,−dY(YB.M.,ω−1
Y/B).
The isomorphismρV,0V,p∗ω−1
Y/B
is the map induced on Hom SH(V)(s∗(1Y),−) by the isomorphism
ϑp∗ω−1
Y/B−TV/B:61−det−1 Vπ∗
V E→61−dV+TV/B−p∗ω−1
Y /Bπ∗
V E.
We have the isomorphisms
6r−Vϑ−V:6r+1−V−det−1 Vπ∗
Y E→π∗
Y E,
6r−Vϑω−1
Y/B−TY/B−V:6r+1−V−det−1 Vπ∗
Y E→6r+1−dY+TY/B−ωY/Bπ∗
Y E,
ϑωY/B−TT/B:π∗
Y E→61−dY+TY/B−ωY/Bπ∗
Y E.
The ﬁrst induces an isomorphism
ρ−V: HomSH(Y)(1Y,6 r+1−V−det−1 Vπ∗
Y E)→ E0,0(Y),
the second an isomorphism
ρTY/B+V−ω−1
Y/B
: HomSH(Y)(1Y,6 r+1−V−det−1 Vπ∗
Y E)→ E−2dY,−dY(Y/BB.M.,ω−1
Y/B),
while the third induces the isomorphism
ρY,Y,ω−1
Y/B
: E0,0(Y)→ E−2dT Y,−dY(Y/BB.M.,ω−1
Y/B).
Altogether these maps and isomorphisms gives the diagram of isomorphisms
E−2dY,−dY
0V (V/BB.M., p∗ω−1
Y/B)
φ∗
// E−2dY,−dY(Y/BB.M.,ω−1
Y/B)
E0,0(Y)
ρY,Y,ω−1
Y/B
hh
E2r,r
0V (V, det−1 V)
ρV,0V,det−1 V
OO
ψ
// HomSH(Y)(1Y,6 r+1−V−det−1 Vπ∗
Y E)
ρTY/B+V−ωY/B
OO
ρ−V
66 (4.5.4)
