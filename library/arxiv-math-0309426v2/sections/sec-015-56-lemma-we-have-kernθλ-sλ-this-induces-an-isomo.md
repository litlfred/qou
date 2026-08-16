---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-015-56-lemma-we-have-kernθλ-sλ-this-induces-an-isomo
section_title: "Lemma. We have Kernθλ =S(λ)⊥. This induces an isomorphism"
section_number: 5.6
pages: 7-7
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
S(λ′)# ✲ψλ
∼ S(λ)∗ ; zλ′ ·# h ✲ ⟨xλh, −⟩λ,
whereh ∈ H .
Proof. Both Kernθλ andS(λ)⊥ are pure submodules of M (λ). Over Z[q,q −1], both
S(λ′)# andS(λ)∗ are free of rank nλ, so it suﬃces to prove that Kern θλ ⊆S(λ)⊥.
By (5.5) this is equivalent to showing that S(λ) ⁄⊆Kernθλ. So it is enough to show
thatzλθλ ⁄= 0. The bilinear form ⟨, ⟩λ′ is associative, so
⟨zλθλ,xλ′ ⟩λ′ =q−α(λ)⟨zλ′T −1
wλ ′xλ′,xλ′ ⟩λ′
=q−α(λ′)(
∑
w∈Sλ ′
qℓ(w))⟨zλ′,xλ′T −1
wλ ⟩λ′ .
Now, zλ′ = ∑
v∈Sλ
(−q)−ℓ(v)xλ′Twλ ′v, where each wλ′v is a distinguished coset
representative for Sλ′ . In contrast, T −1
wλ is equal to Twλ ′ plus a linear combi-
nation of terms Tu, where u ∈ Sn with ℓ(u) < ℓ(wλ′ ). Thus ⟨zλ′,xλ′T −1
wλ ⟩λ′ =
⟨xλ′Twλ ′,xλ′Twλ ′ ⟩λ =qℓ(wλ ′ ). Hence, ⟨zλθλ,xλ′ ⟩λ′ ⁄= 0.
A comparison of the short exact sequences
0 ✲ Kernθλ ✲ M (λ) ✲θλ
S(λ′)# ✲ 0
and
0 ✲ S(λ)⊥ ✲ M (λ) ✲δλ
S(λ)∗ ✲ 0
yields the isomorphism ψλ. □
For each node (i,j ) ∈ [λ], we let hi,j = (λi −j)+ (λ′
j −i)+ 1 be the corresponding
hook length and set hλ(q) = ∏
(i,j)∈[λ][hi,j]q. The next lemma follows from results
of Murphy [ 11].
