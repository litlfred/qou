---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-023-54-determinants
section_title: "Determinants"
section_number: 5.4
pages: 45-46
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
in the form
U(qt,λ,q ) =A(t;q)U(t,λ,q ) and V (qt,q ) =A(t;q)V (t,q ) (237)
where
A(t,q ) =
(
0 1
−q−2 2q−1−q−2t−1
)
. (238)
Therefore, we see that
det(U(qt,λ,q )) = det(U(t,λ,q ))q−2 and det( V (qt,q )) = det(V (t,q ))q−2. (239)
Lemma 5.4. We have
− det(U(t,λ,q )) = det(V (t,q )) =q−1t−2. (240)
Proof. Firstly notice that both det(U(t,λ,q ))t2 and det(V (t,q ))t2 are elliptic functions in t.
Furthermore,
det(U(t,λ,q )) =f (1)(t,λ,q )f (−1)(qt,q )−f (1)(qt,λ,q )f (−1)(t,q ) (241)
has potentially simple poles in t at±q−1/4−n/2λ−1. Lemma 5.3 implies that
Rest=±q−1/4−nλ−1 det(U(t,λ,q )) =θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6
∞θ(q−1λ;q)θ(q−3/2λ;q)
×f (−1)(±q−1/4−nλ−1,q )f (−1)(±q3/4−nλ−1,q )
− θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6
∞θ(q−1λ;q)θ(q−3/2λ;q)
×f (−1)(±q3/4−nλ−1,q )f (−1)(±q−1/4−nλ−1,q )
= 0.
A similar calculation shows that Rest=±q1/4−nλ−1 det(U(t,λ,q )) = 0. Therefore, U(t,λ ;q)t2 is
elliptic and holomorphic in t∈ C ×, hence it is constant in t. Now considering the limit as
t→ 0, using the deﬁnition of f (±1) and their asymptotic expansions (given by their formal
power series expansions, by a q-version of Watson’s lemma), it follows that
det(U(t,λ,q ))t2 = lim
t→0
det(U(t,λ,q ))t2 = lim
t→0
θ(t;q)
θ(t;q)t2− lim
t→0
θ(qt;q)
θ(q−1t;q)t2
=− lim
t→0
q−1θ(t;q)
θ(t;q) =−q−1.
(242)
ForV notice that
det(V (t,q ))t2 =g(0,0)(t,q )g(0,1)(qt,q )t2−g(0,0)(qt,q )g(0,1)(t,q )t2. (243)
This has potentially simple poles at t∈qZ . There is no non-constant elliptic function that
satisﬁes this [2]. Therefore, det( V (t,q ))t2 is constant. Then notice that
det(V (t,q ))t2 = lim
t→∞
det(V (t,q ))t2 =q−1. (244)
□
46 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Corollary 5.5. If h(t,q ) is holomorphic for t ∈ C × and satisﬁes the q-diﬀerence equa-
tion (28) then
h(t,q ) =C0(q)g(0,0)(t,q ). (245)
Proof. Every solution to equation (28) can be written in the form
h(t,q ) =C0(t,q )g(0,0)(t,q ) +C1(t,q )g(0,1)(t,q ) (246)
for some elliptic functions C0 and C1. Now we see that
det
(
g(0,0)(t,q ) h(t,q )
g(0,0)(qt,q ) h(qt,q )
)
=C1(t,q )q−1t−2 (247)
is holomorphic and therefore C1(t,q ) = C1(q) is independent of t. Now notice that if
g(t0,q ) = 0 then g(qt0,q )⁄= 0 as otherwise this would imply det( V (t0,q )) = 0. This means
that if C1(q)⁄= 0 then C0(t,q ) has simple poles at t∈ qZ and no other poles for t∈ C ×
which contradicts the fact that C0(t,q ) is elliptic as this would give an isomorphism from
the elliptic curve to CP1. Therefore C1(q) = 0. Then again noting that if g(t0,q ) = 0 then
g(qt0,q )⁄= 0 we see that C0(t,q ) must be constant in t.
We remark that an alternative proof can be given using the fact that all holomorphic
solutions on C × have a convergent Laurent/Fourier series expansion
∑
k∈Z
αk(q)tk. (248)
This is a consequence of Cauchy’s theorem and a detailed discussion of this can be found,
for example, in [1]. In our case, the functional equations imply this expansion is divergent
if α−1⁄= 0. This forces α−1 = 0, and the functional equation then implies that αk = 0 for
k <0 and that αk are uniquely determined by C0(q) = α0(q) for k≥ 0 which implies that
our function is equal to C0(q)g(0,0)(t,q ). □
