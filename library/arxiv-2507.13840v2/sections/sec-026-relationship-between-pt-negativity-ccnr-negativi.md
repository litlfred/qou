---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-026-relationship-between-pt-negativity-ccnr-negativi
section_title: "Relationship between PT negativity, CCNR negativity, and robustness of entanglement"
section_number: null
pages: 34-35
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Relationship between PT negativity, CCNR negativity, and robustness of entan-
glement
Here, we prove the inequality between the PT negativity and robustness of entanglement:
E(ρ) ≤ln(2R(ρ) + 1).
(103)
Note that this has previously been proven in Ref. [107], and here we give an alternative proof. Let s
be the optimal value such that ρ = (1 + s)ρ+ −sρ−for ρ+, ρ−∈SEP, so that R(ρ) = s. We have
ρΓ = (1 + s)ρΓ
+ −sρΓ
−, with ρΓ
+, ρΓ
−∈SEP, yielding
∥ρΓ∥1 ≤(1 + s)∥ρΓ
+∥1 + s∥ρΓ
−∥1 = 2s + 1.
(104)
In the first inequality, we used the triangle inequality on the trace norm ∥·∥1, and the second equation
is due to ∥ρs∥1 = 1 for ρs ∈SEP. Taking the logarithm, we obtain Eq. (103).
Similarly, for the CCNR negativity, we have
∥Rρ∥1 ≤(1 + s)∥Rρ+∥1 + s∥Rρ−∥1 ≤2s + 1,
(105)
where we used that ∥Rρ∥1 ≤1 for separable states.
F
Relationship between PT negativity, CCNR negativity, and the Schmidt number
Here, we prove the inequality
E(ρ) ≤ln s(ρ).
(106)
. Let ρ = P
i pi |ψi⟩⟨ψi| be the optimal pure-state decomposition such that s(ρ) = maxi s(|ψi⟩). We
have
∥ρΓ∥1 ≤
X
i
pi∥(|ψi⟩⟨ψi|)Γ∥1
=
X
i
pieS1/2(|ψi⟩)
≤
X
i
pis(|ψi⟩)
≤s(ρ).
(107)
Here, we used the triangle inequality in the first line. In the second line, we used that E(ρ) = S1/2(|ψ⟩)
for pure states ρ = |ψ⟩⟨ψ|. In the third line, we used the monotonicity of entanglement R´enyi entropy.
It is easy to see that the argument above immediately extends to the CCNR negativity, thus we
also have
C(ρ) ≤ln s(ρ) .
(108)
This was previously shown in Ref. [60] through a different technique.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
34
