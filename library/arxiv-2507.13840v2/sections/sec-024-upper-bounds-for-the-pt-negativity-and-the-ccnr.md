---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-024-upper-bounds-for-the-pt-negativity-and-the-ccnr
section_title: "Upper bounds for the PT negativity and the CCNR negativity"
section_number: null
pages: 32-33
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Upper bounds for the PT negativity and the CCNR negativity
Here, we prove upper bounds for the PT negativity and the CCNR negativity. First, we show an
inequality that holds for the pα-negativity:
Eα(ρ) ≤1
2(n ln 2 −S2(ρ)),
(90)
for any α ≥0. This can be directly shown using the monotonicity of the pα-negativity E0(ρ) ≥Eα(ρ).
An upper bound for the PT negativity is thus obtained by setting α = 1.
Next, we have
E(ρ) ≤m ln 2,
(91)
where m = min(nA, nB). To see this, we will show that
E(ρ) ≤min(S1/2(ρA), S1/2(ρB)),
(92)
which immediately leads to Eq. (91) since S1/2(ρA(B)) ≤nA(B) ln 2. We define
|√ρ⟩=
X
i
(ρ1/2 |i⟩) ⊗|i⟩,
(93)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
32
which is a purification of ρ in HA ⊗HB ⊗HA′ ⊗HB′ ≃C2n ⊗C2n. It is also known as the canon-
ical purification [34]; however, the particular purification does not matter in this context. The PT
negativity of the subsystem A in

√ρ

 is given by S1/2(ρA) (since

√ρ

 is a pure state) , while the
original PT negativity E(ρ) is obtained by tracing out A′B′ in

√ρ

. Due to the monotonicity of PT
negativity with respect to partial tracing [84], we obtain E(ρ) ≤S1/2(ρA). By exchanging A and B,
we also obtain E(ρ) ≤S1/2(ρB), thus proving Eq. (92).
While the upper bound in Eq. (91) does not apply for Eα with α < 1, we can give an upper bound
for p0 as
ln p0 ≤2m ln 2 + ln r,
(94)
where r = rank(ρ). For r = 1, i.e. ρ is a pure state, this can easily be shown using the Schmidt
decomposition. To show the inequality for general r, note that ρ can be purified using an ancilla
with physical dimension r. We denote a purification of ρ as |ψρ⟩∈C2n ⊗Cr. We can represent |ψρ⟩
as an MPS, where the ancilla, that we now denote as subsystem C, is placed in the middle of the
chain, separating the subsystems A and B, which are placed to the left and right of C, respectively.
In this case, the PT spectrum is stored in the PT of the transfer matrix of C, denoted by EΓ
C (see
Appendix N). One can see that the maximal size of this matrix is (2S0(ρA)×2S0(ρB))×(2S0(ρA)×2S0(ρB)),
so that the maximal rank of ρΓ is
ln p0 ≤S0(ρA) + S0(ρB).
(95)
Finally, Eq. (94) follows by noticing that S0(ρB) ≤S0(ρA) + ln r and vice versa.
It is worth noting that Eq. (95) also implies
Eα(ρ) ≤1
2(S0(ρA) + S0(ρB) −S2(ρ))
(96)
by monotonicity of pα-negativity. The term on the right hand side has a form that resembles the mutual
information Iα(ρAB) = Sα(ρA)+Sα(ρB)−Sα(ρAB), although with different R´enyi indices for Sα(ρA(B))
and Sα(ρAB). Note that the mutual information is not a measure of mixed-state entanglement, as it is
sensitive to classical correlations. If the entanglement spectrum is flat (such that all R´enyi entropies
are identical), this gives a direct relation between the PT negativity and the mutual information as
E(ρ) ≤1
2I(ρ). The latter inequality has been shown, e.g., for stabilizer states [93].
For the rα-negativity, we have
Cα(ρ) ≤m ln 2 −1
2S2(ρ),
(97)
for any α ≥0, and we recall m = min(nA, nB). This can again be shown using the monotonicity of the
rα-negativity C0(ρ) ≥Cα(ρ). An upper bound for the CCNR negativity is obtained by setting α = 1.
