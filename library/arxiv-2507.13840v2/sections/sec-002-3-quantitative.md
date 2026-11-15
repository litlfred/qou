---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-002-3-quantitative
section_title: "Quantitative"
section_number: 3
pages: 5-5
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
(e.g. in terms of inequalities) related to the PT
negativity.
An alternative approach to detect entangle-
ment in mixed states is via the CCNR crite-
rion [24]. We define the realignment matrix Rρ
as

a, a′

 Rρ

b, b′
 = ⟨a, b| ρ

a′, b′
 ,
(8)
which provides a necessary condition for separa-
bility that ∥Rρ∥1 ≤1. The CCNR negativity is
defined by [73, 117, 118]
C(ρ) = ln∥Rρ∥1 = ln
X
i
|λi|,
(9)
where λi are singular values of Rρ. Unlike the
PT negativity, C(ρ) is not a proper entanglement
measure, since it can become negative. Never-
theless, by the CCNR criterion, C(ρ) > 0 implies
that the state is entangled, and thus it serves as
an entanglement witness. We further denote the
moments of the realignment matrix as
rα(ρ) = tr((R†
ρRρ)α/2) =
X
i
|λi|α.
(10)
We will also consider two other entanglement
monotones. First, the fidelity of separability is
defined as [25, 97, 103]
DF(ρ) = min
σ∈SEP −ln F(ρ, σ)
(11)
where we have the Uhlmann fidelity F(ρ, σ) =
tr(√ρσ)2 [61].
Finally, the robustness of entanglement [109] is
given by
R(ρ) = min s s.t ρ = (1+s)ρ+
s −sρ−
s ,
ρ+
s , ρ−
s ∈SEP .
(12)
3
Quantitative
entanglement
wit-
nesses
In this section, we formally introduce the en-
tanglement witnesses based on the PT moments
and realignment moments.
We also define the
symmetry-resolved witnesses in the presence of a
global symmetry.
