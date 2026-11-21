---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
f ∈k⟨X⟩, m ∈M,
fm = (f + Id(S))m.
We note that AM is an epimorphic image of some free A-module. Now, we assume
that AM = modA⟨Y |T ⟩= modA⟨Y ⟩/AT , where T ⊂modA⟨Y ⟩and modA⟨Y ⟩is
a free left A-module with the basis Y . Let T1 = {P fiyi ∈modk⟨X⟩⟨Y ⟩| P(fi +
Id(S))yi ∈T } and R = SX∗Y ∪T1. Then, by the following Lemma 3.3, we have, as
k⟨X⟩-modules, AM ∼= modk⟨X⟩⟨Y |R⟩.
Lemma 3.3 ([11]). Let the notation be the same as above.
Then, as k⟨X⟩-
modules,
σ: AM →modk⟨X⟩⟨Y |R⟩,
X
(fi + Id(S))(yi + AT ) 7→
X
fiyi + k⟨X⟩R
is an isomorphism, where each fi ∈k⟨X⟩.
P r o o f.
For any P(fi +Id(S))(yi +AT ), P(gi +Id(S))(yi +AT ) ∈A M we have
X
(fi + Id(S))(yi + AT ) =
X
(gi + Id(S))(yi + AT )
in AM
⇔
X
(fi −gi)yi ∈AT
in AM
⇔
X
(fi −gi)yi ∈k⟨X⟩R
⇔
X
fiyi + k⟨X⟩R =
X
giyi + k⟨X⟩R.
Hence, σ is injective. It is easy to see that σ is also surjective and consequently, it is
a k⟨X⟩-module isomorphism.
□
By Lemma 3.2 and Lemma 3.3, we know that if we want to ﬁnd a k-linear basis for
the module AM = modA⟨Y |T ⟩, where A = k⟨X|S⟩, we only need to ﬁnd a Gröbner-
Shirshov basis for the module modk⟨X⟩⟨Y |SX∗Y ∪T1⟩, where T1 = {P fiyi ∈
modk⟨X⟩⟨Y ⟩| P(fi + Id(S))yi ∈T }.
The next theorem gives a relationship between the Gröbner-Shirshov bases (pairs)
in free associative algebras and in “double-free” modules.
Theorem 3.4. Let X, Y be well ordered sets, < a monomial ordering on X∗
and ≺the ordering on X∗Y as in (∗). Let S, T ⊂k⟨X⟩be monic sets. Then the
following statements hold:
(1) S ⊂k⟨X⟩is a Gröbner-Shirshov basis in k⟨X⟩with respect to the ordering <
if and only if SX∗Y ⊂modk⟨X⟩⟨Y ⟩is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩
with respect to the ordering ≺.
65
