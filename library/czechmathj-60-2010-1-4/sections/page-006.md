---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
The following is Kang-Lee’s Composition-Diamond lemma for a left module.
Theorem 2.7 ([16], [17]). Let (S, T ) be a pair of subsets of monic elements in
k⟨X⟩and A = k⟨X|S⟩the associative algebra deﬁned by S. Let AM =A A/A(T +
Id(S)) be a left A-module deﬁned by (S, T ). If (S, T ) is a Gröbner-Shirshov pair for
the A-module AM and p ∈k⟨X⟩T +Id(S), then ¯p = a¯sb or ¯p = c¯t, where a, b, c ∈X∗,
s ∈S, t ∈T .
Lemma 2.3 is a special case of Theorem 2.7 when S = ∅.
3. Composition-Diamond lemma for “double-free” modules
Let X, Y be sets and modk⟨X⟩⟨Y ⟩a free left k⟨X⟩-module with the basis Y .
Then modk⟨X⟩⟨Y ⟩= L
y∈Y
k⟨X⟩y is called a “double-free” module. We now deﬁne
the Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩. Suppose that < is a monomial ordering
on X∗, < a well ordering on Y and X∗Y = {uy | u ∈X∗, y ∈Y }. We deﬁne an
ordering ≺on X∗Y as follows: for any w1 = u1y1, w2 = u2y2 ∈X∗Y ,
(∗)
w1 ≺w2 ⇔u1 < u2
or u1 = u2, y1 < y2.
It is clear that the ordering ≺is left compatible in the sense
w ≺w′ ⇒aw ≺aw′ for any a ∈X∗.
Let S ⊂modk⟨X⟩⟨Y ⟩with each s ∈S monic. Then we deﬁne the composition
in S only the inclusion composition which means f = ag for some a ∈X∗, where
f, g ∈S. If (f, g)f = f −ag = P αiaisi, where αi ∈k, ai ∈X∗, si ∈S and ai¯si ≺f,
then this composition is called trivial modulo (S, f) and is denoted by
(f, g)f ≡0 mod(S, f).
Deﬁnition 3.1 ([11]).
Let S ⊂modk⟨X⟩⟨Y ⟩be a non-empty set with each s ∈S
monic. Let the ordering ≺be deﬁned as before. Then we call S a Gröbner-Shirshov
basis in the module modk⟨X⟩⟨Y ⟩if all compositions in S are trivial modulo S.
The proof of the following lemma is basically taken from [11]. For the sake of
convenience, we sketch the proof.
63
