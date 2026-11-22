---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-035-effects-of-depolarizing-noise-on-entanglement
section_title: "Effects of depolarizing noise on entanglement"
section_number: null
pages: 42-43
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Effects of depolarizing noise on entanglement
In this section, we consider the effects of global depolarizing noise
ρ′ = (1 −p) |ψ⟩⟨ψ| + pI/2n,
(147)
on the bipartite entanglement of a general pure state |ψ⟩. For a given subsystem A, the entanglement
in the pure state (p = 0) is characterized by the Schmidt coefficients λi for i = 1, . . . , r, where λi ≥λj
for i < j, and the Schmidt decomposition of the state is given by
|ψ⟩=
r
X
i=1
p
λi |i⟩A |i⟩B .
(148)
Applying the partial transpose on a pure state ρ = |ψ⟩⟨ψ|, one can show that the spectrum of ρΓ is
sij
pλiλj for i, j = 1, . . . , r and sij = 1 if i ≤j and sij = −1 otherwise. From Eq. (147), the spectrum
of (ρ′)Γ is simply rescaled and shifted to (1 −p)sij
pλiλj + p/2n. Thus, the state becomes PPT when
p ≥1 −
1
1 + 2n√λ1λ2
.
(149)
Namely, the robustness of a state with respect to depolarizing noise is determined solely by the two
largest Schmidt coefficients.
As an illustration, let us now consider stabilizer states.
These states are known to have a flat
entanglement spectrum, i.e., λi = const for any λi̸ = 0 [106]. As a consequence, the entanglement
R´enyi entropy is determined by integer k, with Sα = k ln 2 and λi = 2−k, for i = 1, . . . , 2k. Thus, for
k > 0, we have that the state becomes PPT when
p ≥1 −
1
1 + 2n−k .
(150)
We see that exponentially strong noise is required to destroy entanglement, regardless of the initial
value of the entanglement in the noise-free state. Surprisingly, states with less entanglement are more
robust when subjected to noise. Despite of this, one can show that
E4 ≃S2 + ln(1 −p),
(151)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
42
and thus the entanglement is detected when p < 1 −e−S2. For low-entangled pure states, E4 already
fails to detect entanglement at a low value of p. This is intuitively expected, since states with low
entanglement are harder to distinguish from separable states. Note that a similar result holds for the
p3-PPT condition, where the entanglement is detected at p < 1 −e−2S3.
