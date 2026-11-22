---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-006-4-quantifying
section_title: "Quantifying"
section_number: 4
pages: 8-9
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Quantifying
entanglement
dimen-
sionality
Beyond traditional entanglement measures, en-
tanglement dimensionality has been identified
as a crucial resource that quantifies the min-
imum dimension required to represent a given
state [105].
This is formally measured by the
Schmidt number, which we define as follows.
Consider the Schmidt decomposition for a pure
state |ψ⟩in the subsystem A:
|ψ⟩=
s(|ψ⟩)
X
i=1
p
λi |i⟩A |i⟩B ,
(39)
where λi are known as the Schmidt coefficients
The number of nonzero Schmidt coefficients is
called the Schmidt rank s(|ψ⟩), which is an en-
tanglement monotone for pure states [108]. For
mixed states, we can extend this concept using
a convex-roof construction to define the Schmidt
number as [94, 105]
s(ρ) =
min
ρ=P
i pi|ψi⟩⟨ψi| max
i
s(|ψi⟩),
(40)
where the minimum is taken over all possible
pure-state decompositions ρ =
P
i pi |ψi⟩⟨ψi|.
The Schmidt number is also an entanglement
monotone for general mixed states [105].
Determining the exact Schmidt number for a
given mixed state is a challenging task.
Con-
sequently, there has been significant interest in
finding efficient methods to bound this quantity
in experiments. Previous works have introduced
techniques based on fidelity witnesses [94, 105],
covariance matrices [64], and symmetric informa-
tionally complete measurement [75]. In the fol-
lowing, we demonstrate that our witnesses also
provide a lower bound to the Schmidt number.
For pure states, the Schmidt rank is equivalent
to the exponential of the entanglement R´enyi en-
tropy eS0(|ψ⟩). Therefore, it can be lower bounded
by the R´enyi entropies as ln s(|ψ⟩) ≥Sα(|ψ⟩) for
any α > 0.
Following this idea, the pα-negativity also pro-
vides a lower bound to the Schmidt number for
all mixed states. To show this, we first establish
that the Schmidt number is bounded by the PT
negativity as
E(ρ) ≤ln s(ρ).
(41)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
8
The proof is given in Appendix 41. As a conse-
quence, the Schmidt number is also bounded by
the pα negativity due to Eq. (15). In particular,
we have
E4(ρ) ≤ln s(ρ)
(42)
and similarly
C4(ρ) ≤ln s(ρ) .
(43)
This provides an efficient lower bound to the
Schmidt number.
5
