---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: sec-002-3-composition-diamond-lemma-for-double-free-modu
section_title: "Composition-Diamond lemma for “double-free” modules"
section_number: 3
pages: 6-9
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
---
Let X, Y be sets and modk⟨X⟩⟨Y ⟩ a free left k⟨X⟩-module with the basis Y .
Then modk⟨X⟩⟨Y ⟩ = ⨁
y∈Y
k⟨X⟩y is called a “double-free” module. We now deﬁne
the Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩. Suppose that < is a monomial ordering
on X ∗, < a well ordering on Y and X ∗Y = {uy | u ∈ X ∗, y ∈ Y }. We deﬁne an
ordering ≺ on X ∗Y as follows: for any w1 = u1y1, w 2 = u2y2 ∈ X ∗Y ,
(∗) w1 ≺ w2 ⇔ u1 < u 2 or u1 = u2, y 1 < y 2.
It is clear that the ordering ≺ is left compatible in the sense
w ≺ w′ ⇒ aw ≺ aw′ for any a ∈ X ∗.
Let S ⊂ modk⟨X⟩⟨Y ⟩ with each s ∈ S monic. Then we deﬁne the composition
in S only the inclusion composition which means f = ag for some a ∈ X ∗, where
f, g ∈ S. If (f, g )f = f − ag = ∑ α iaisi, where α i ∈ k, ai ∈ X ∗, si ∈ S and ai¯si ≺ f ,
then this composition is called trivial modulo (S, f ) and is denoted by
(f, g )f ≡ 0 mod( S, f ).
Deﬁnition 3.1 ([11]). Let S ⊂ modk⟨X⟩⟨Y ⟩be a non-empty set with each s ∈ S
monic. Let the ordering ≺ be deﬁned as before. Then we call S a Gröbner-Shirshov
basis in the module modk⟨X⟩⟨Y ⟩if all compositions in S are trivial modulo S.
The proof of the following lemma is basically taken from [11] . For the sake of
convenience, we sketch the proof.
63
Lemma 3.2 ([11], Composition-Diamond lemma for “double-free” modules). Let
S ⊂ modk⟨X⟩⟨Y ⟩be a non-empty set with each s ∈ S monic and ≺ the ordering on
X ∗Y as before. Then the following statements are equivalent:
(1) S is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩.
(2) If 0 ⁄= f ∈ k⟨X⟩S, then f = a¯s for some a ∈ X ∗, s ∈ S.
(2′) If 0 ⁄= f ∈ k⟨X⟩S, then f = ∑ α iaisi with a1¯s1 ≻ a2¯s2 ≻ . . . , where each
α i ∈ k, ai ∈ X ∗, si ∈ S.
(3) Irr(S) = {w ∈ X ∗Y | w ⁄= a¯s, a ∈ X ∗, s ∈ S} is a k-linear basis for the factor
modk⟨X⟩⟨Y |S⟩= mod k⟨X⟩⟨Y ⟩/k ⟨X⟩S.
P r o o f. (1) ⇒ (2). Suppose that 0 ⁄= f ∈ k⟨X⟩S. Then f = ∑ α iaisi for some
α i ∈ k, ai ∈ X ∗, si ∈ S. Let wi = ai¯si and w1 = w2 = . . . = wl ≻ wl+1 ≽ . . . . We
now prove that f = a¯s for some a ∈ X ∗, s ∈ S, by using induction on l and w1. If
l = 1, then the result is clear. If l > 1, then a1¯s1 = a2¯s2. Thus, we may assume that
a1 = a2a, ¯s2 = a¯s1 for some a ∈ X ∗. Now, by (1),
a1s1 − a2s2 = a2as1 − a2s2 = a2(as1 − s2) = a2
∑
β jbjuj =
∑
β ja2bjuj,
where β j ∈ k, bj ∈ X ∗, uj ∈ S and bj ¯uj ≺ ¯s2. Therefore, a2bj ¯uj ≺ w1. By using
induction on l and w1, we obtain the result.
It is clear that (2) is equivalent to (2′).
(2) ⇒ (3). For any 0 ⁄= f ∈ modk⟨X⟩⟨Y ⟩, if f = u1 ∈ Irr(S), then f = β 1u1 + . . . .
If f ⁄∈Irr(S), then f = α 1a1s1 + . . . . Consequently, f can be expressed by
f =
∑
α iaisi +
∑
β juj,
where α i, β j ∈ k, ai ∈ X ∗, si ∈ S and uj ∈ Irr(S). Then Irr(S) generates the
factor module. Moreover, if 0 ⁄= ∑ α iaisi = ∑ β juj, where ai ∈ X ∗, si ∈ S,
uj ∈ Irr(S), a1¯s1 ≻ a2¯s2 ≻ . . . and u1 ≻ u2 ≻ . . . , then u1 = a1¯s1, which is clearly a
contradiction. Hence, Irr(S) is a k-linear basis of the factor module.
(3) ⇒ (1). For any f, g ∈ S, suppose that f = ag. Since (f, g )f ∈ k⟨X⟩S, by (3)
we have (f, g )f = f − ag = ∑ α iaisi, where si ∈ S, ai ∈ X ∗ and ai ¯si ≼ (f, g )f ≺ f .
Now, it is clear that S is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩. □
Remark. We view k⟨X⟩as a free left k⟨X⟩-module with one generator e. Then
modk⟨X⟩⟨e⟩= k⟨X⟩e =k⟨X⟩k⟨X⟩is a cyclic k⟨X⟩-module. If S ⊂ k⟨X⟩, then k⟨X⟩S
is a left ideal of k⟨X⟩which is also a left k⟨X⟩-submodule of k⟨X⟩e. This implies
that Lemma 2.3 is a special case of Lemma 3.2.
Let S ⊂ k⟨X⟩ and let A = k⟨X|S⟩ be an associative algebra. Then, for any
left A-module AM , we can regard AM as a k⟨X⟩-module in a natural way: for any
64
f ∈ k⟨X⟩, m ∈ M ,
f m = (f + Id(S))m.
We note that AM is an epimorphic image of some free A-module. Now, we assume
that AM = mod A⟨Y |T ⟩ = mod A⟨Y ⟩/AT , where T ⊂ modA⟨Y ⟩ and modA⟨Y ⟩ is
a free left A-module with the basis Y . Let T1 = {∑ fiyi ∈ modk⟨X⟩⟨Y ⟩|∑ (fi +
Id(S))yi ∈ T } and R = SX ∗Y ∪ T1. Then, by the following Lemma 3.3, we have, as
k⟨X⟩-modules, AM ∼= modk⟨X⟩⟨Y |R⟩.
Lemma 3.3 ([11]). Let the notation be the same as above. Then, as k⟨X⟩-
modules,
σ : AM → modk⟨X⟩⟨Y |R⟩,
∑
(fi + Id(S))(yi + AT ) ↦→
∑
fiyi + k⟨X⟩R
is an isomorphism, where each fi ∈ k⟨X⟩.
P r o o f. For any ∑ (fi + Id(S))(yi + AT ), ∑ (gi + Id(S))(yi + AT ) ∈A M we have
∑
(fi + Id(S))(yi + AT ) =
∑
(gi + Id(S))(yi + AT ) in AM
⇔
∑
(fi − gi)yi ∈ AT in AM
⇔
∑
(fi − gi)yi ∈ k⟨X⟩R
⇔
∑
fiyi + k⟨X⟩R =
∑
giyi + k⟨X⟩R.
Hence, σ is injective. It is easy to see that σ is also surjective and consequently, it is
a k⟨X⟩-module isomorphism. □
By Lemma 3.2 and Lemma 3.3, we know that if we want to ﬁnd a k-linear basis for
the module AM = mod A⟨Y |T ⟩, where A = k⟨X|S⟩, we only need to ﬁnd a Gröbner-
Shirshov basis for the module modk⟨X⟩⟨Y |SX ∗Y ∪ T1⟩, where T1 = {∑ fiyi ∈
modk⟨X⟩⟨Y ⟩ |∑ (fi + Id(S))yi ∈ T }.
The next theorem gives a relationship between the Gröbner-S hirshov bases (pairs)
in free associative algebras and in “double-free” modules.
Theorem 3.4. Let X, Y be well ordered sets, < a monomial ordering on X ∗
and ≺ the ordering on X ∗Y as in (∗). Let S, T ⊂ k⟨X⟩be monic sets. Then the
following statements hold:
(1) S ⊂ k⟨X⟩is a Gröbner-Shirshov basis in k⟨X⟩with respect to the ordering <
if and only if SX ∗Y ⊂ modk⟨X⟩⟨Y ⟩is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩
with respect to the ordering ≺.
65
(2) We consider k⟨X⟩as a free k⟨X⟩-module having one generator e. Then (S, T )
is a Gröbner-Shirshov pair for the A-module M = A/A (T + Id( S)), where
A = k⟨X|S⟩if and only if S is a Gröbner-Shirshov basis in the algebra k⟨X⟩
with respect to the ordering < and (SX ∗ ∪ T )e is a Gröbner-Shirshov basis in
the free module modk⟨X⟩⟨e⟩with respect to the ordering ≺.
P r o o f. (1) Suppose that S is a Gröbner-Shirshov basis in k⟨X⟩. We shall prove
that all compositions in SX ∗Y are trivial modulo SX ∗Y . For any f , g ∈ SX ∗Y ,
let f = s1a1y, g = s2a2y, s1, s 2 ∈ S, a1, a 2 ∈ X ∗, y ∈ Y and w = f = ag. Then
¯s1a1 = a¯s2a2. Since S is a Gröbner-Shirshov basis in k⟨X⟩, we have
(f, g )w = f − ag = s1a1y − as2a2y = (s1a1 − as2a2)y =
∑
(α iuirivi)y,
where ui, v i ∈ X ∗, ri ∈ S and ui¯riviy ≺ w. Thus, every composition is trivial modulo
SX ∗Y and hence, SX ∗Y is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩. Conversely,
assume that SX ∗Y is a Gröbner-Shirshov basis in the module modk⟨X⟩⟨Y ⟩. For any
f , g ∈ S and w = f a = bg, we have w1 = f ay = bgy and
(f ay, bgy )w1 = (f a − bg)y =
∑
α i(airi)y,
where α i ∈ k, ri = sibi, ai, b i ∈ X ∗, si ∈ S and ai ¯riy ≺ w1. Then
(f, g )w = f a − bg =
∑
α iaisibi
with ai¯sibi < w . This shows that each composition of intersection in S is trivial mod-
ulo S. Similarly, every composition of inclusion in S is trivial modulo S. Therefore,
S is indeed a Gröbner-Shirshov basis in k⟨X⟩.
(2) The results follow directly from Deﬁnitions 2.6 and 3.1. □
Remark. By Theorem 3.4 it is clear that Theorem 2.7 follows from Lemma 3.2.
