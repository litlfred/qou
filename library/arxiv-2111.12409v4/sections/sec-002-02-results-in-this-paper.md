---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem Paolo Dolce Francesco Zucconi 0 Introduction 1 0.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
section_id: sec-002-02-results-in-this-paper
section_title: "Results in this paper"
section_number: 0.2
pages: 1-3
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmi"
---
1 Adelic curves 4
2 The interpolating polynomial 7
3 Integral estimates 8
4 Roth’s theorem for adelic curves (A) 13
5 Roth’s theorem for adelic curves (B) 17
Appendices 19
A Construction of the interpolating polynomial 19
References 20
Abstract
We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming
some technical conditions on the behavior of the logarithmi c absolute values. We illustrate how
tightening such assumptions makes our inequalities strong er. As special cases we recover Corvaja’s
results [Cor97] for ﬁelds admitting a product formula, and Vojta’s ones [ Voj21] for arithmetic function
ﬁelds.
0 Introduction
0.1 History
The celebrated Roth’s theorem proved in [ Rot55] asserts that the irrationality measure of a real
algebraic number is 2. An equivalent, but more detailed stat ement is the following:
Theorem 0.1 (Roth). Let α be a real algebraic number and let ε > 0 be a real number. Then there
exists a real constant C(α, ε) > 0 such that for every pair of coprime integers (p, q) with q > C (α, ε),
it holds that: ⏐⏐⏐⏐α − p
q
⏐⏐⏐⏐ > q −2−ε
The above statement can be naturally generalised in diﬀeren t directions by considering a number
ﬁeld K instead of Q and the simultaneous approximation of the elements α1, . . . , αn algebraic over
K by an element of K with respect to diﬀerent valuations (see [ Lan83, Chapter 7]). Actually, the
statement proved in [ Lan83, Chapter 7] holds for ﬁelds that are more general than number ﬁelds.
At the moment we don’t have an eﬀective version of Roth’s theorem (i.e. a bound for the constant
C(α, ε), see [ Cor95]), but we have a quantitative version (i.e. bounds, in terms of α and ε, on the
number of good approximants see [ BvdP88], [ BvdP90], [ Eve97]).
Let k be a ﬁeld of characteristic 0 and let Vk be a set in bijection with a family of absolute values
of k. The bijection is denoted by v ↦→ | · |v, for any v ∈ V k and we don’t put any restriction on
the cardinality of Vk, therefore we recall that a sum over an uncountable set is deﬁ ned to be the
supremum of the sums over all ﬁnite subsets. The couple ( k, Vk) satisﬁes the product formula if for
any element a ∈ k× the series ∑
v∈Vk
log |a|v converges absolutely and moreover ∑
v∈Vk
log |a|v = 0.
In this setting one also has a natural notion of logarithmic height for a ∈ k×:
h(a) :=
∑
v∈VK
log+ |a|v ,
1
and we set H(a) := eh(a). Roth’s theorem was generalised by Corvaja in [ Cor97] for any couple
(k, Vk) satisfying the product formula:
Theorem 0.2. [Cor97, Corollaire 1]. Assume that (k, Vk) satisﬁes the product formula. Let α1, . . . , αn
be distinct elements algebraic on k, and let | · | v1 , . . . ,| · | vn be distinct absolute values of k, with
v1, . . . , vn ∈ V k. For any i = 1, . . . , n let’s ﬁx an appropriately normalised extension of | · |vi to k(αi)
(and by abuse of notation denote it with the same symbol | · | vi ). Then for any ε > 0 there exists a
constant C = C(Vk, α1, . . . , αn, v1, . . . , vn, ε) > 0 such that for all β ∈ k with H(β) > C it holds that:
n∑
i=1
log |αi − β|vi > −(2 + ε)h(β) .
Notice that there are no further assumptions on the ﬁeld k, which might be for instance a function
ﬁeld; therefore, theorem 0.2 is a unifying result, as well as a generalisation of the class ical Roth’s
theorem. Moreover, in the same paper Corvaja obtained also a quantitative version of Theorem 0.2
(see [ Cor97, Corollaire 3.7]).
An arithmetic function ﬁeld , is a ﬁnitely generated ﬁeld over Q. The “geometrisation” of these
ﬁelds in terms of Arakelov geometry is wonderfully explaine d in [ Mor00]. Recently, Vojta in [ Voj21]
proved a version of Roth’s theorem for arithmetic function ﬁ elds with a big polarisation. For obvious
reasons this can be considered as a “higher dimensional” gen eralisation of Roth’s theorem. We
conclude this short historic overview by explaining the sta tement of Vojta’s result. A big polarisation
of an arithmetic function ﬁeld K consists of a couple ( X, L) where:
(i) X → Spec Z is a normal arithmetic variety whose function ﬁeld is isomor phic to K.
(ii) Denote with d the relative dimension of X over Spec Z; then L = {L 1, . . .L d} is a collection
of hermitian, arithmetically nef and big line bundles.
Now ﬁx an arithmetic function ﬁeld K with a big polarisation; then we can deﬁne a geometric height
function hL for a prime divisor Y as the Arakelov intersection number of the hermitian line bu ndles
L 1, . . . ,L d restricted to Y . We can now deﬁne a non-archimedean absolute value on K, associated
to Y :
|a|Y := e−hL(Y )ord Y (a) ∀a ∈ K .
Moreover, for any closed point p ∈ XC = X ×Spec Z Spec C that doesn’t come from the base change of
a divisor on X we have the following archimedean absolute value:
|a|p :=
√
a(p)a(p) ∀a ∈ K .
By putting all together, we get a set of absolute values MK which turns out to be a measure space
with a measure that we denote with µ. The notion of product formula holds true for the couple
(K, MK ) in the following form:
∫
MK
log |a|ν dµ(ν) = 0 , ∀a ∈ K ×
Moreover there is a notion of height for any element of a ∈ K ×:
hK (a) :=
∫
MK
log+ |a|v dµ(v) .
We set HK (a) := ehK (a). One of the 4 equivalent versions of Vojta’s generalisation of Roth’s theorem
is given below.
Theorem 0.3. [Voj21, Theorem 4.5] Consider a couple (K, MK ) where K is an arithmetic function
ﬁeld with a big polarisation such that L 1 = . . . = L d, and MK is a set of absolute values as explained
before. Let S be a subset of MK of ﬁnite measure and ﬁx some distinct elements α1, . . . , αn ∈ K.
Then for any ε > 0 and any c ∈ R there exists a real constant C > 0 (depending on the ﬁxed data)
such that for any β ∈ K with hK (β) > C it holds that:
∫
S
min
1≤i≤n
(
log− |β − αi|ω
)
dµ(ω) > −(2 + ε)hK(β) + c (1)
0.2 Results in this paper
The goal of this paper is to generalise Roth’s theorem in a wid er framework which includes Corvaja’s
and Vojta’s settings.
The theory of adelic curves introduced by Chen and Moriwaki i n [ CM20] provides such natural
framework: an adelic curve X consists of a ﬁeld K of characteristic 0 and a measure space (Ω , A, µ)
endowed with a function φ : ω ↦→ | · | ω that maps Ω into the set of places of K and such that
2
ω ↦→log |a|ω is in L1(Ω , µ) for any a ∈ K×. On X we have a well deﬁned notion of height hX, and
