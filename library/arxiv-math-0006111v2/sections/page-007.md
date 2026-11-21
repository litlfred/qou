---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
toc_source: undetermined
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of symmet- ric groups."
---
APPROXIMATE FACTORIZATION AND CONCENTRATION
7
making an error bounded by Cδql/2. On the other hand the right hand side of
(2.1.5) can be replaced by
(2.1.8)
X
(π1,π2)
1
(q + 1)2 (q)comp(π1)(q)comp(π2)ψ(π1)ψ(π2)
The diﬀerence between (2.1.7) and (2.1.8) is
X
(π1,π2)
1
(q + 1)2 ((q)comp(π) −(q)comp(π1)(q)comp(π2))ψ(π1)ψ(π2)
One has
comp(π1 ∪π2) = comp(π1) + comp(π2)
thus
|(q)comp(π1∪π2) −(q)comp(π1)(q)comp(π2)| ≤Cqcomp(π1)+comp(π2)−1
By Lemma 4.3.2 and 4.3.3 of [B], one has
n1 + n2 + |h(π1)| + |h(π2)| ≥2(comp(π1) + comp(π2)) −4
therefore each term in this diﬀerence is bounded by Cql/2−1 and one gets the stated
result.
□
Using the Lemma, we can now estimate the variance of mn(λ) under the measure
Πψ, indeed it follows from Section 3.3 in [B] that one has
Πψ((ml(λ) −ml(ψ))2) = τψ(⟨Γ(ψ)l⟩2) −τψ(⟨Γ(ψ)l⟩)2
therefore, using Lemma 2.1, for ψ ∈Fn
c,δ one has
Πψ((ml(λ) −ml(ψ))2) ≤K(δ + q−1)ql
by Lemma 2.1
Theorem 1 now follows by an application of Markov’s inequality.
□
Corollary 1 is a simple consequence of Theorem 1 and of the moment-cumulant
formula.
Finally for the proof of Theorem 2, we can use the same arguments as in Section
4 of [B], and the hypotheses (1) and (2) of Deﬁnition 3.1. This shows that there
exists a constant K such that, for all ψ ∈Fn
c,δ, all l ≤n and all cycle ρ on l −1
elements, one has
|cl(ψ)q1−l −ψ(ρ)| ≤K(δ + q−1)q−l/2
for all l ≤n
This combined with Corollary 1 gives Theorem 2
□
