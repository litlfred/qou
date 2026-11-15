---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-004-32-from-the-realignment-moments
section_title: "From the realignment moments"
section_number: 3.2
pages: 6-7
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
From the realignment moments
We also define entanglement witnesses based on
the CCNR negativity C(ρ) using the realignment
matrix moments. We define the rα-negativity as
Cα(ρ) =
1
2 −α ln (rα) + 1 −α
2 −α ln (r2)
=
1
2 −α[ln(rα) + (α −1)S2(ρ)] ,
(20)
Using similar argument for the pα-negativity, by
replacing pα with rα, one can show that Cα sat-
isfies the monotonicity Cα ≥Cβ for α < β, which
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
6
implies
Cα(ρ) ≤C(ρ),
(21)
where C(ρ) ≡C1(ρ). Although C(ρ) is not an en-
tanglement monotone, it provides a lower bound
to the robustness of entanglement via
C(ρ) ≤ln(2R(ρ) + 1),
(22)
as shown in Appendix E. Therefore, Cα(ρ) for
α ≥1 also serves as a quantitative entanglement
witness, as it provides a lower bound to the ro-
bustness of entanglement.
In particular, the r4-negativity reads
C4(ρ) = 1
2 ln
 
r3
2
r4
!
= 1
2[−ln(r4)−3S2(ρ)] , (23)
where C4(ρ) > 0 implies that the state is entan-
gled. We can give bounds −1
2S2(ρ) ≤C4(ρ) ≤
min(nA, nB) ln 2 −1
2S2(ρ), where nA(B) is the
number of qubits in A(B). (see Appendix C for
the upper bound). The witness C4 can be mea-
sured by a scheme similar to that for E4 [68],
without full-state tomography.
As detailed in
Appendix B, we introduce a new measurement
scheme which employs a constant-depth circuit
of Clifford gates, offering a significant advantage
in terms of experimental feasibility. It can also
be measured via randomized measurements as
demonstrated in previous experiments [17, 88].
