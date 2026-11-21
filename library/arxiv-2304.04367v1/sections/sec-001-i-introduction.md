---
doc_id: arxiv-2304.04367v1
doc_title: "Angle-dependent pair production in the polarized two-photon Breit-Wheeler process"
section_id: sec-001-i-introduction
section_title: "I Introduction"
section_number: null
pages: 1-2
source_pdf: 2304.04367.pdf
source_sha256: 63fc9a4a5f6b6b71
toc_source: outline
doc_brief: "Angle-dependent pair production in the polarized two-photon Breit-Wheeler process — 11 sections: Angle-dependent pair production in; I Introduction; II Methods of theory and numerical"
---
The quantum electrodynamics (QED) theory predicts the
interaction between photons, wherein the collision of two real
γ photons can produce the e+e−pair, known as the linear Breit-
Wheeler (LBW) process. The LBW process is the second-order
process in QED [1], and its validation in terrestrial laborato-
ries requires an ultrahigh-brilliance γ-ray beam with a peak
cross-section of ∼1.6 × 10−29 m2 [2]. To date, the only veri-
ﬁed interaction of real photons in experiments is multiphoton
Breit-Wheeler pair production [3]. However, the production
of LBW pairs via virtual photons has been demonstrated in
high-energy collider experiments by utilizing the photons of a
highly Lorentz-contracted Coulomb ﬁeld [4].
The LBW process is a fundamental ingredient in high-energy
astrophysics, playing a crucial role in the production of pair
plasma in γ-ray bursts [5–7] and black hole activity [8, 9].
Furthermore, the LBW process can dominate the laser-driven
QED plasmas, as demonstrated by numerical simulations [10,
11]. In recent years, several γγ colliders have been proposed
in the platform of laser-plasma interactions to produce LBW
pairs [12–20].
Despite the calculation of the total LBW cross section σγγ
for increasing the luminosity of γγ colliders, the photon po-
larization and e± spins, which are the fundamental quantum
nature of the photons and leptons [21], entail the exclusive char-
acteristics of the LBW process [2, 4, 22–26]. When utilizing
two linearly polarized (LP) photons, σγγ can be expressed in
terms of mutual-parallel or mutual-perpendicular polarization
vectors, and the non-polarized cross section can be obtained via
∗tangl@hebtu.edu.cn
† jianxing@xjtu.edu.cn
a simple average over the two LP cross sections [22, 26]. The
LBW process has been demonstrated in high-energy colliders
by means of the equivalent photon approximation of ultra-
relativistic heavy-ions, which presents the ﬁrst measurement of
the unique cos 4ϕ modulation of the distinct diﬀerential cross
section with two LP photons, where ϕ is the angle between
the lepton pair transverse momentum and the individual lepton
transverse momentum [27, 28]. Fundamentally, the angular
modulations, both in polar and azimuthal directions, originate
from the total helicity of the Λγ = 0, ±2 two-photon system,
which must be transferred to the orbital angular momentum
of the e+e−pair [2, 4]. Therefore, the LBW diﬀerential cross
section can be extended to the fundamental level of helicity
amplitudes to more deeply investigate the eﬀects of photon
polarization [29].
Moreover, to clarify the eﬀects of arbitrary photon polar-
ization, the polarization states of photons and pairs can be
described by the corresponding density matrices, leading to the
completely polarized LBW cross section in terms of Stokes pa-
rameters, which is applicable to perform the Monte Carlo (MC)
simulation incorporating the beam eﬀects [2, 30]. The collision
of quasi-energetic circularly polarized (CL) γ-photon beams
can produce distinct energy-angle spectra. When the colliding
photons have the same right-hand or left-hand helicities, the
collision produces the quadrupole angular spectrum imprinted
by the longitudinal polarization. Conversely, the opposite
helicities lead to the dipole one imprinted by the transverse
polarization [2]. Although the eﬀects of independent linear
polarization or circular polarization have been elucidated, their
coupling eﬀects are still elusive when the colliding photons are
partially circular polarization and linear polarization.
In this paper, we undertake an investigation of the fully
angle-dependence in the polarized LBW process using both
analytical cross-section and MC numerical simulation. By
arXiv:2304.04367v1  [hep-ph]  10 Apr 2023
deﬁning a new spin base, the transverse and longitudinal polar-
ization of e± are decoupled from the diﬀerential cross section,
allowing for the analytical clariﬁcation of the eﬀects of pho-
ton linear polarization on the angle-distribution of e+e−pair
polarization. By utilizing the MC simulation, we have quanti-
tatively retrieved the azimuthal and polar dependence of e+e−
pair, revealing that the linear polarization of photons induces
an azimuthal-dependent pair yield and pair polarization. This
comprehensive understanding of the polarized LBW process is
highly beneﬁcial for the upcoming γγ collider and the associ-
ated research in high-energy astrophysics.
The paper is structured as follows. In Sec. II, the theoretical
deduction of the completely polarized LBW cross-section is
described, and the method of spin-resolved MC sampling is
established. The eﬀects of arbitrary photon polarization are
analyzed theoretically and numerically in Sec. III. The pro-
posed ultrabrilliant polarized γ-photon source that could be
used to perform the polarized LBW veriﬁcation is discussed
in IV. Finally, a brief conclusion of this paper is presented in
Sec. V.
II.
