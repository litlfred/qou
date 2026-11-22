---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-033-pt-and-realignment-moments-in-translation-invari
section_title: "PT and realignment moments in translation-invariant MPS"
section_number: null
pages: 40-41
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
PT and realignment moments in translation-invariant MPS
Let us consider a translationally invariant (TI) MPS of n qubits of bond dimension χ:
|ψ⟩=
X
s1,s2,··· ,sn
tr (As1As2 · · · Asn) |s1, s2, · · · sn⟩
(138)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
40
with As being a χ × χ matrix. We consider the entanglement within ρ = trC(|ψ⟩⟨ψ|), where C is
a contiguous subsystem of |ψ⟩.
In particular, we study entanglement for ρ with bipartition A =
{1, 2, · · · , nA}, B = {nA + 1, nA + 2, · · · , nA + nB}, and we assume that all subsystems are extensive.
The transfer matrix of the MPS is defined as
E =
X
s
As ⊗As.
(139)
We denote the eigenvalues of E as λi, with λ1 ≥λ2 ≥· · · λr.
The corresponding left and right
eigenvectors, Li and Ri, satisfy P
s(As)†LiAs = λ1L and P
s AsRi(As)† = λiR, respectively. Here,
we impose tr(LiRi) = 1. The matrices Li and Ri are Hermitian with non-negative eigenvalues. We
assume that the dominant eigenvalue λ1 is unique.
The PT moment can be written as
pα =
P
ijk λαnA
i
λαnB
j
λαnC
k
tr((LkRi)α)tr((LjRk)α)tr((LiRj)α/2)2
P
i λαn
i
,
(140)
for even α. In the thermodynamic limit n →∞, we find
pα = tr((L1R1)α)2tr((L1R1)α/2)2 + O(|λ2
λ1
|αm),
(141)
where m = min(nA, nB, nC). This yields the PT negativity
E(ρ) = lim
α→1/2 ln p2α ≃2 ln tr((L1R1)1/2),
(142)
where the subleading term decays exponentially with n. Here, limα→1/2 tr((L1R1)2α) = 1 since the
eigenvalues of L1R1 are non-negative. Note that one can also find that S1/2(ρA) ≃4 ln tr((L1R1)1/2)
for n →∞, where ρA = trB(ρ). This implies that E(ρ) ≃1
2S1/2(ρA). Note that a similar observation
was made in quantum circuits at short times [11]
For the realignment moment, we find for even α
rα =
P
ijk λαnA
i
λαnB
j
λαnC
k
tr((LkRi)2)α/2tr((LjRk)2)α/2tr((LiRj)α/2)2
P
i λαn
i
,
(143)
which in the limit n →∞gives
rα = tr((L1R1)2)αtr((L1R1)α/2)2 + O(|λ2
λ1
|αm).
(144)
Thus, the CCNR negativity is given by
C(ρ) = lim
α→1/2 ln r2α ≃2 ln tr((L1R1)1/2) + ln tr((L1R1)2) = 1
2(S1/2(ρA) −S2(ρA)).
(145)
We see that C(ρ) is smaller than E(ρ), and thus provides a weaker entanglement witness for any TI
MPS. This is similarly the case for stabilizer states and Haar random states [6]. Nevertheless, C(ρ) is
always successful in detecting entanglement in the generic case when the spectrum of L1R1 is not flat.
