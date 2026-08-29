---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner"
section_id: sec-020-lemma
section_title: "Lemma"
section_number: null
pages: 15-16
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner — This paper presents an exposition of Soergel bimodules, the categ oriﬁcation of Hecke alge- bras, and their applications to"
---
Suppose that λ, µ∈ h∗ are compatible. Then the translation functors
Oλ Oµ
T µ
λ
T λ
µ
are biadjoint.
Proof: If Vη is deﬁned as it is above, then V ∗
η = V(−w0η ) where w0 is the longest element in
W. Then T λ
µ = πλ◦ (V ∗⊗ (−))◦ ιµ . The desired result follows from the fact that V ⊗ (−) and
V ∗⊗ (−) are biadjoint.
4.2.3 Lemma
Translation functors send projective modules to projectiv e modules.
Proof of this fact follows from the previous lemma and a more genera l result about projective
objects in abelian categories, the proof of which has been relegate d to the appendix. 6.4
With our earlier setup for g, let E be the real span E = R⊗Z P⊂ h∗, equipped by the Killing
form with the inner product ( , ). For any root α∈ R±, deﬁne the hyperplane Hα , orthogonal to
α, by
Hα :={λ∈ E| (λ + ρ, α) = 0},
or equivalently, Hα :={λ∈ E| (λ + ρ)(α∨) = 0}. InO0, we will give an important construction.
Let s ∈ S, and choose an integral weight µ such that the dot-action stabilizer of µ is{id, s},
and choose a dominant integral weight ν such that ν− µ is also dominant integral. Deﬁne the
composition of functors
Θ s := T 0
ν◦ T ν
µ ◦ T µ
ν ◦ T ν
0 .
An important property of this construction is the following, wherein we let the Verma module
M(w·0) be denoted by Mw.
4.2.4 Lemma
For any w∈ W , s∈ S, the following sequence is nonsplitting and short exact:
0 Mw Θ sMw Mws 0 if ws > w
0 Mws Θ sMw Mw 0 if ws < w
Noticing that [Θ sMw] = [ Mw] + [Mws] in the Grothendieck group, we observe the following
15
