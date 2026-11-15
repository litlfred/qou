---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-014-10-entanglement-and-noise
section_title: "Entanglement and noise"
section_number: 10
pages: 14-15
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Entanglement and noise
In this section, we analyze the average bipartite
entanglement of Haar-random pure states sub-
jected to global depolarizing noise.
These sys-
tems approximate deep random quantum circuits
with local noise [31]. We are interested in deter-
mining under which condition entanglement sur-
vives in the presence of noise. We consider Haar
states subject to global depolarizing noise
ρ′ = (1 −p) |ψ⟩⟨ψ| + pI/2n,
(69)
with noise probability p and |ψ⟩being drawn
from the Haar measure. One can show that the
R´enyi-2 entropy of the depolarized state is given
by EH[S2[ρ′]]
=
−ln
(1 −p)2 + p(2 −p)/2n.
Now, let p′
α be the PT moment of the depolar-
ized Haar-random states and pα those of a Haar-
random state. Then, the mean values EH[p′
α] can
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
14
be expressed in terms of the mean values EH[pα]
as
EH[p′
α] =
α
X
k=0
 
α
k
!
(1−ϵ)kEH[pk](ϵ/2n)α−k , (70)
with E[p0] = p0 = 2n.
For any fixed p < 1 and n →∞, we find that
the leading term EH[E4] ≃min(nA, nB) ln 2 for
extensive subsystems nA and nB. Therefore, the
averaged bipartite entanglement entropy of the
depolarized state, quantified by the PT negativ-
ity, is unchanged from that of the pure state,
which follows the Page curve [82]. As a conse-
quence, E4 is remarkably effective in detecting
mixed-state entanglement in Haar states even in
the presence of strong noise.
We further consider exponential noise p =
1 −2−βn with fixed β, and determine for which
β the witness E4 can successfully detect entan-
glement.
For β ≤1/2, we have EH[S2(ρ′)] ≃
2βn ln 2.
Moreover, using Eq. (70), we obtain
EH[p4] ≃2−4βn−2nB, yielding
EH[E4] ≳min(nA, nB) ln 2 −βn ln 2.
(71)
Thus,
we
detect
entanglement
via
E4
>
0
for
extensive
subsystems
whenever
β
<
min(nA, nB)/n. Beyond detection, the value of
E4 in Eq. (71) shows rigorously that the nega-
tivity obeys a volume law in the entangled re-
gions. Notably, the p3-PPT condition is unable
to show the volume law. In fact, the PT neg-
ativity can also be obtained by considering the
distribution of the Schmidt coefficients of a Haar
random state, yielding [101]
EH[E] ≃min(nA, nB) ln 2 −βn ln 2.
(72)
Thus, E4 matches E in depolarized Haar random
states, i.e. EH[E4] ≃EH[E]. This highlights the
effectiveness of E4 to quantitatively detect entan-
glement, even under exponentially strong noise.
We provide further discussion on the effects of
global depolarizing noise on entanglement in Ap-
pendix O.
11
