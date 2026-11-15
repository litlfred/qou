---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-003-a-aharonov-bohm-effect
section_title: "A Aharonov-Bohm Effect"
section_number: null
pages: 7-9
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.93
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
As motivation, recall the Aharonov-Bohm effect in quantum electrodynamics. [@aharonovbohm] Initially, gauge fields were introduced into classical physics as auxiliary fields to aid calculations - While they were present in the canonical formalism, they were not necessary and did not appear in the classical equations of motion (Maxwell's equations in the case of electromagnetism). However, quantum mechanics promotes observables to operators and mandates the use of the canonical formalism. As a result, the topology of the gauge fields can indeed have observable physical consequences. In particular, in quantum mechanics, electrons become waves which exhibit an interference pattern. Aharonov and Bohm predicted that a change in the gauge fields (by for example, the introduction of a solenoid in between the two beams) will cause a shift in the interference pattern observed. As quantum mechanics only permits local interactions among fields and the two electron beams do not pass through the region in which the gauge fields are nontrivial, the use of the vector potential in this case is inescapable.

While first introduced as a Gedanken-experiment for demonstrating the influence of topological defects on physical systems, the Aharonov-Bohm Effect has now been verified by many actual physical experiments (including a 1998 experiment using magnetostatic metal rings [@metalring]). The typical experiment demonstrating the Aharonov-Bohm effect is the 2 slit electron diffraction experiment in which electrons are fired at the slits one at a time and the diffraction pattern on a screen a fixed distance away is measured. A change in the interference pattern is observed when a solenoid (ideally, infinitely long so the magnetic field completely vanishes outside the solenoid) is placed in between the two slits. Thus it is found that the vector potential itself has intrinsic physical meaning in this effectively two dimensional setting, not just the curl as originally supposed in classical electrodynamics.

Formally, Feynman's path integral method can be applied to to the system at hand. The phase for the interference term is determined by the path difference between the two electron beams. The degree of the effect is thus determined by the integral of the vector potential around a loop surrounding the solenoid.

Given a non-simply connected system, if the gauge potential is changed by an amount $\delta A$, then the resulting change in the wave equation is only invariant if $\oint \delta A(r) \cdot d r = n \frac{h}{e_j}$ where $n$ is an integer. Thus the fractional part of $\frac{e}{h} \oint A(r) \cdot d r$ has measurable physical consequences.

In broken gauge theories, the flux is quantized - In order to ensure the wave function is single valued, the vector potential can only encircle the solenoid an integer number of times. Note that this is a purely topological effect as it is determined solely by the winding number of the path. (In mathematical terms: the path integral exponent corresponds to an element of the fundamental group of the space . Specifically, the solenoid is a puncture in the plane (the third dimension is trivialized) so $\pi_1(\mathbb{R}^2 \setminus 0 \times \mathbb{R}) = \pi_1(S^1) = \mathbb{Z}$.) Thus topology can play an influential role in determining quantum physics phenomena. In fact, since topological interactions are by nature robust against local perturbations, harnessing this resource for quantum computation could lead to a fault-tolerant quantum computer.
