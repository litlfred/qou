---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-039-411-preparations
section_title: "Preparations"
section_number: 4.1.1
pages: 90-91
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Preparations
The exact PIMC expectation value of operator ˆO is calculated by Eq.(2.3) and
therefore Eq.(2.11), and we need to choose a proper total imaginary time τ and time
step ∆τ to project out the ground state |Φ0⟩. In this section, we discuss the choice of
τ and ∆τ and use 4He as an example.
From Eq.(2.6) we can see that, the residual amount of excited states depends on
the ratio ai/a0 and the factor e−(Ei−E0)τ1. We have to make sure that the coeﬃcient of
the ﬁrst excited state |Φ1⟩is negligible compared with the ground state |Φ0⟩.
The experimental ground state energy E0 of 4He is about -28.3 MeV and the
ﬁrst excited state energy E1 is the energy of a separated nucleon and triton, -8 MeV
(Tilley et al. (1992)). The energy diﬀerence E1 −E0 is about -20 MeV. If we choose
τ1 = 0.1 MeV−1 then e−(E1−E0)τ1 will be e−2 ≈0.135. If there is only |Φ0⟩and |Ψ1⟩
in |ΨT⟩, and if |a1/a0| is small enough, then the percentage of the ﬁrst excited state
|Φ1⟩in |ΨT⟩will be greatly suppressed by |a1/a0e−(E1−E0)τ1|, therefore e−Hτ1|ΨT⟩is
dominated by the ground state |Φ0⟩. In fact, if there are other excited states in |ΨT⟩,
the ground state |Φ0⟩will be projected out even sooner, because |a1/a0| will be smaller
for a good trial wave function and other excited states |Φi⟩will die out faster than
|Φ1⟩due to the factor |ai/a0e−(Ei−E0)τ1|. So, even a less than 0.1 MeV−1 imaginary
time τ1 may still be adequate.
The analysis above suggests that τ1 = 0.1 MeV−1 should be enough for our PIMC
80
to project out the ground state. Since we usually put operator ˆO in the middle of
two propagators as ⟨ΨT|e−Hτ1 ˆOe−Hτ2|ΨT⟩as shown in Eq.(2.3), and we usually set
