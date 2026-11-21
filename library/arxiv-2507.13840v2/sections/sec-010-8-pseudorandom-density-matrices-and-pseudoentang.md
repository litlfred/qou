---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-010-8-pseudorandom-density-matrices-and-pseudoentang
section_title: "Pseudorandom density matrices and pseudoentanglement"
section_number: 8
pages: 11-12
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
pseudoentanglement
Our quantitative witnesses have direct implica-
tions on recent developments in quantum cryp-
tography.
In particular, pseudorandom states
(PRS) have been proposed as efficiently prepara-
ble pure state ensembles that are indistinguish-
able from Haar random states by any efficient
quantum algorithm [59]. Such states have been
generalized to mixed states, known as pseudoran-
dom density matrices (PRDMs). They are effi-
ciently preparable states which are indistinguish-
able from random mixed states with entropy S2
for any efficient algorithm [10]. Their formal def-
inition is given in Appendix I.
For pure states, it has been shown that PRS
(which are equivalent to PRDMs with S2 = 0)
must have ω(log n) entanglement entropy [2, 59].
Further, it has been shown that PRDMs with
S2 = ω(log n) can possess any amount of entan-
glement.
However, the entanglement property
of PRDMs for bounded entropy S2 = O(log n)
has been unclear. We now show that for S2 =
O(log n), the entanglement of PRDMs as mea-
sured by PT negativity is bounded as follows:
Proposition 1 (Entanglement of PRDM). Any
ensemble of PRDMs with entropy S2 = O(log n)
must have PT negativity E(ρ) = ω(log n) with
high probability.
This is proven in Appendix I. The key idea is
to assume by contradiction that there exists a
PRDM with E(ρ) = O(log n).
This would im-
ply that p4 = 1/poly(n), which can be efficiently
distinguished from Haar random states via the
efficient measurement of the PT moment p4 in
Appendix A.
A related notion is pseudoentanglement [2, 10],
which are (efficiently preparable) ensemble of
states with low entanglement g(n) that are in-
distinguishable from an ensemble with high en-
tanglement f(n). The formal definition is given
in Appendix I. Our results allow to provide new
bounds on pseudoentanglement of mixed states.
A fundamental question is the difference in en-
tanglement between the two ensembles, which
is dubbed the pseudoentanglement gap. Previ-
ous works have shown that the pseudoentangle-
ment gap is bounded as f(n) = Θ(n) vs g(n) =
ω(log n) for pure states, i.e. S2(ρ) = 0 [2], while
for highly mixed states with S2(ρ) = ω(log n),
one finds the maximal possible gap of f(n) =
Θ(n) vs g(n) = 0 [10].
However, the gap for
weakly mixed states S2(ρ) = O(log n) has been
an open problem.
Here, we now compute the entanglement in
terms of PT negativity and fidelity of separa-
bility. Then, we can bound the largest possible
pseudoentanglement gap as follows:
Proposition 2 (Pseudoentanglement of mixed
states). Pseudoentangled state ensembles with
entropy S2 = O(log n) can have a pseudoentan-
glement gap of at most f(n) = Θ(n) vs g(n) =
ω(log n), where entanglement is measured by both
PT negativity E(ρ) and fidelity of separability
DF(ρ).
Proof. This follows directly from contradiction:
Assume there exists pseudoentangled state en-
sembles with low-entanglement g(n) = E(ρ) =
DF(ρ)
=
O(log n),
and
high-entanglement
f(n) = E(ρ) = DF(ρ) = Θ(log n).
Then, via
Thm. 1 and assuming S2(ρ) = O(log n), those
ensembles can be efficiently distinguished, thus
they cannot be pseudoentangled.
We note that pseudoentanglement is connected
to the existence of a fundamental primitive of
quantum cryptography [14]: EFI pairs are pairs
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
11
of mixed states that are statistically far, yet in-
distinguishable for any efficient quantum algo-
rithm. EFI pairs require pseudoentanglement to
exist [47], thus our bounds place potential restric-
tions on EFI pairs as well.
