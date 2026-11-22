---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
Lemma 3.2 ([11], Composition-Diamond lemma for “double-free” modules). Let
S ⊂modk⟨X⟩⟨Y ⟩be a non-empty set with each s ∈S monic and ≺the ordering on
X∗Y as before. Then the following statements are equivalent:
(1) S is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩.
(2) If 0̸ = f ∈k⟨X⟩S, then f = a¯s for some a ∈X∗, s ∈S.
(2′) If
0̸ = f ∈k⟨X⟩S, then f = P αiaisi with a1¯s1 ≻a2¯s2 ≻. . ., where each
αi ∈k, ai ∈X∗, si ∈S.
(3) Irr(S) = {w ∈X∗Y | w̸ = a¯s, a ∈X∗, s ∈S} is a k-linear basis for the factor
modk⟨X⟩⟨Y |S⟩= modk⟨X⟩⟨Y ⟩/k⟨X⟩S.
P r o o f.
(1) ⇒(2). Suppose that 0̸ = f ∈k⟨X⟩S. Then f = P αiaisi for some
αi ∈k, ai ∈X∗, si ∈S. Let wi = ai¯si and w1 = w2 = . . . = wl ≻wl+1 ⪰. . .. We
now prove that f = a¯s for some a ∈X∗, s ∈S, by using induction on l and w1. If
l = 1, then the result is clear. If l > 1, then a1¯s1 = a2¯s2. Thus, we may assume that
a1 = a2a, ¯s2 = a¯s1 for some a ∈X∗. Now, by (1),
a1s1 −a2s2 = a2as1 −a2s2 = a2(as1 −s2) = a2
X
βjbjuj =
X
βja2bjuj,
where βj ∈k, bj ∈X∗, uj ∈S and bj ¯uj ≺¯s2. Therefore, a2bj ¯uj ≺w1. By using
induction on l and w1, we obtain the result.
It is clear that (2) is equivalent to (2′).
(2) ⇒(3). For any 0̸ = f ∈modk⟨X⟩⟨Y ⟩, if f = u1 ∈Irr(S), then f = β1u1 + . . ..
If f̸ ∈Irr(S), then f = α1a1s1 + . . .. Consequently, f can be expressed by
f =
X
αiaisi +
X
βjuj,
where αi, βj ∈k, ai ∈X∗, si ∈S and uj ∈Irr(S).
Then Irr(S) generates the
factor module.
Moreover, if 0̸ = P αiaisi = P βjuj, where ai ∈X∗, si ∈S,
uj ∈Irr(S), a1¯s1 ≻a2¯s2 ≻. . . and u1 ≻u2 ≻. . . , then u1 = a1¯s1, which is clearly a
contradiction. Hence, Irr(S) is a k-linear basis of the factor module.
(3) ⇒(1). For any f, g ∈S, suppose that f = ag. Since (f, g)f ∈k⟨X⟩S, by (3)
we have (f, g)f = f −ag = P αiaisi, where si ∈S, ai ∈X∗and ai ¯si ⪯(f, g)f ≺f.
Now, it is clear that S is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩.
□
Remark. We view k⟨X⟩as a free left k⟨X⟩-module with one generator e. Then
modk⟨X⟩⟨e⟩= k⟨X⟩e =k⟨X⟩k⟨X⟩is a cyclic k⟨X⟩-module. If S ⊂k⟨X⟩, then k⟨X⟩S
is a left ideal of k⟨X⟩which is also a left k⟨X⟩-submodule of k⟨X⟩e. This implies
that Lemma 2.3 is a special case of Lemma 3.2.
Let S ⊂k⟨X⟩and let A = k⟨X|S⟩be an associative algebra.
Then, for any
left A-module AM, we can regard AM as a k⟨X⟩-module in a natural way: for any
64
