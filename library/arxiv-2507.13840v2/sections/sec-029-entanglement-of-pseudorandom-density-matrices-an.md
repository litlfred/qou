---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-029-entanglement-of-pseudorandom-density-matrices-an
section_title: "Entanglement of pseudorandom density matrices and pseudoentanglement"
section_number: null
pages: 36-37
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Entanglement of pseudorandom density matrices and pseudoentanglement
In this section, we show that pseudorandom density matrices (PRDMs) with S2 = O(log n) must have
E(ρ) = ω(log n).
PRDMs are efficiently preparable states that are indistinguishable for any efficient observer from
truly random mixed states [10]. They generalize pseudorandom states (PRSs), which are computa-
tionally indistinguishable from Haar random states [59]. PRDMs are indistinguishable from random
mixed states. Formally, these random mixed states are sampled from the generalized Hilbert-Schmidt
ensemble (GHSE) [10, 15, 50, 125]
ηn,m = {trm(|ψ⟩⟨ψ|)}|ψ⟩∈µn+m ,
(118)
which are states constructed by taking n + m qubit random states from the Haar measure µn+m and
tracing out m qubits.
PRDMs are now defined as follows:
Definition I.1 (Pseudo-random density matrix (PRDM) [10]). Let κ = poly(n) be the security pa-
rameter with keyspace K = {0, 1}κ. A family of n-qubit density matrices {ρk,m}k∈K are pseudorandom
density matrices (PRDMs) with mixedness parameter m if:
1. Efficiently preparable: There exists an efficient quantum algorithm G such that G(1κ, k, m) = ρk,m.
2. Computational indistinguishability: t = poly(n) copies of ρk,m are computationally indistinguish-
able (for any quantum polynomial time adversary A) from the GHSE ηn,m

 Pr
k←K[A(ρ⊗t
k,m) = 1] −
Pr
ρ←ηn,m[A(ρ⊗t) = 1]

 = negl(n).
(119)
For m = 0, one recovers PRS [59], while for m = ω(log n), PRDMs are computationally indistin-
guishable from the maximally mixed state [10, 54]. However, the case m = O(log n) has not been
understood well so far.
Proposition 5 (Lower bound on entanglement of PRDM). Any ensemble of PRDMs with entropy
S2 = O(log n) must have PT negativity E(ρ) = ω(log n) with high probability.
Proof. We prove by contradiction: Assume there exists PRDMs with E(ρ) = O(log n). Since E4(ρ) ≤
E(ρ), we also have that E4(ρ) = O(log n). If S2 = O(log n), then −ln p4 = O(log n). On the other
hand, GHSE have −ln p4 = Θ(n) (see Sec. L). Therefore, the algorithm to measure p4 in Fact. A.1
can distinguish the two ensembles with polynomial number of copies, thus contradicting the definition
of PRDM. Therefore, PRDMs must have E(ρ) = ω(log n) whenever S2 = O(log n).
Finally, let us formally define pseudoentanglement. Note that our definition explicitly allows mixed
states, in contrast to Ref. [2] which used entanglement entropy as measure of entanglement and thus
was only well defined for pure states. We extend to mixed states by using for entanglement E(ρ) and
fidelity of separability:
Definition I.2 (Pseudoentanglement). A pseudoentangled state ensemble with gap f(n) vs g(n)
consists of two ensembles of n-qubit states ρk and σk, indexed by a key k ∈{0, 1}poly(n) with the
following properties:
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
36
1. Efficient Preparation: Given k, ρk (or σk, respectively) is efficiently preparable by a uniform,
poly-sized quantum circuit.
2. Pseudoentanglement: With probability ≥1−1/poly(n) over the choice of k, the PT negativity E(ρ)
and fidelity of separability DF(ρ) for ρk (or σk, respectively) is Θ(f(n)) (or Θ(g(n)), respectively).
3. Indistinguishability: For any polynomial p(n), no poly-time quantum algorithm can distinguish
between the ensembles of poly(n) copies with more than negligible probability. That is, for any
poly-time quantum algorithm A, we have that

Pr
k [A(ρ⊗poly(n)
k
) = 1] −Pr
k [A(σ⊗poly(n)
k
) = 1]

 = negl(n) .
