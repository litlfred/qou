---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-009-7-circuit-depth-certification
section_title: "Circuit depth certification"
section_number: 7
pages: 10-11
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Circuit depth certification
A key task is to certify the depth of the cir-
cuit that was used to prepare a given quantum
state ρ.
For noiseless circuits, i.e.
S2(ρ) = 0,
the circuit depth can be certified efficiently using
Bell measurements [51]. We now prove that the
same task is also efficient for noisy quantum cir-
cuits, assuming the final state has low entropy,
i.e. S2(ρ) = O(log n).
We apply a noisy circuit of d layers ρ = Λd ◦
Λd−1 · · · ◦Λ1(|0⟩⟨0|), where Λi consists of noisy
two-qubit gates implemented in a fixed architec-
ture. The entanglement usually grows with each
layer, and can be used to bound the total depth.
One chooses an bipartition of equal size, where
the cut is placed such that the two-qubit gates
that act across the cut are minimal. Then, the
maximal possible entanglement is only a func-
tion of the |∂A| two-qubit gates that act across
the cut, while all other gates cannot increase en-
tanglement.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
10
We now bound the maximal entanglement gen-
erated in such circuits: We show that, the overall
entanglement after d layers is bounded as
E(ρ) ≤d|∂A| ln 2 .
(50)
The proof is given in Appendix G.
With this bound, we can efficiently certify the
minimal circuit depth d that generated a given
state ρ by measuring E4(ρ).
In particular, we
have
d ≥
1
|∂A| ln 2E4(ρ) .
(51)
where we used the inequality Eq. (15). By mea-
suring E4(ρ), one can certify d, where the esti-
mator of E4(ρ) gives a non-trivial lower bound
on d as long as S2(ρ) = O(log n).
We derive
the error bounds on the estimator for certifica-
tion in Appendix H. For example, when we have
E4 = ω(log n), our estimator correctly determines
d = ω(log n) using a polynomial number of mea-
surements.
8
