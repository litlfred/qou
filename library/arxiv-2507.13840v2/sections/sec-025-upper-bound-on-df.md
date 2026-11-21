---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-025-upper-bound-on-df
section_title: "Upper bound on DF"
section_number: null
pages: 33-34
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Upper bound on DF
Here, we prove the bound on the fidelity of separability DF as
Sα(ρA(B)) ≥DF(ρ) ,
(98)
for any α ≥0.
First, by the Uhlman’s theorem [80], we can write
DF(ρ) = min
σ∈SEP min
|ψσ⟩−ln | ⟨√ρ|ψσ⟩|2
(99)
where

√ρ

 is the canonical purification of ρ defined in Eq. (93) and |ψσ⟩is a purification of σ in
HA ⊗HB ⊗HA′ ⊗HB′ ≃C2n ⊗C2n. Consider the Schmidt decomposition for the state

√ρ

 in the
subsystem A:
|√ρ⟩=
X
i
p
λi |ϕi⟩A ⊗|ϕi⟩A′BB′ ,
(100)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
33
where λi are the eigenvalues of ρA = TrB(ρ), where λ1 is the largest eigenvalue.
The state
TrA′B′(|ϕ1⟩A ⊗|ϕ1⟩A′BB′ ⟨ϕ1|A ⊗⟨ϕ1|A′BB′) = |ϕ1⟩A ⟨ϕ1|A ⊗TrA′B′(|ϕ1⟩A′BB′ ⟨ϕ1|A′BB′) is a separable
state in HA ⊗HB. Thus, we have
DF(ρ) ≤−ln | ⟨√ρ||ϕ1⟩A ⊗|ϕ1⟩A′BB′⟩|2 = −ln λ1.
(101)
Note that −ln λ1 = limα→∞Sα(ρA). Thus, by the hierarchy of R´enyi entropy, we have
Sα(ρA) ≥DF(ρ),
(102)
for any α ≥0. By exchanging A and B, we obtain a similar inequality with Sα(ρB).
