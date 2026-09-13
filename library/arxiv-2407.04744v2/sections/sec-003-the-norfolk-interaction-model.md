---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-003-the-norfolk-interaction-model
section_title: "The Norfolk interaction model"
section_number: null
pages: 3-4
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
---
We base our calculations on electromagnetic many-
body currents [6, 7, 11, 12] derived consistently with the
Norfolk two- and three-body (NV2+3) nuclear interac-
tions [1–5]. The Norfolk two-body potential (NV2) is
a fully local interaction – hence suitable to be utilized
within QMC methods – and includes terms up to N3LO
in the χEFT expansion. To this order, the NV2 consists
of one- (OPE) and two-pion-exchange (TPE) contribu-
tions, as well as contact interactions with strengths spec-
ified by unknown low-energy constants (LECs). Non-
localities emerging from the contact terms entering at
N3LO have been eliminated by i) leveraging Fierz trans-
formations to develop a minimally non-local interaction
to order N3LO [1]; and ii) constraining the LECs asso-
ciated with the leftover N3LO non-local terms to van-
ish [2]. This choice is motivated by the consideration
that the LECs associated with the non-local terms are of
natural size, as opposed to those associated with the local
isovector and isotensor operators required to obtain good
agreement with nucleon-nucleon (NN) scattering data.
Schematically, the NV2 interaction can be broken
down into three parts as
v12 =vL
12 +vS
12 +vEM
12 , (11)
FIG. 1: Diagrams illustrating the contributions to the
electromagnetic current up to N2LO. Nucleons,
∆-isobars, pions, and external fields are denoted by
solid, thick-solid, dashed, and wavy lines, respectively.
The square in panel (d) represents relativistic
corrections to the LO current. Figure from Ref. [6].
where vL
12 is the long-range term consisting of OPE and
TPE contributions to order N2LO,vS
12 is the short-range
term consisting of contact interactions, and vEM
12 is an
electromagnetic contribution. The electromagnetic term
retains second-order Coulomb, Darwin-Foldy, vacuum
polarization, and magnetic moment interaction terms [9].
The radial functions in vL
12 have∼1/rn (with n≤ 6)
singularities at the origin that are regulated with the
function
CRL(r) = 1− 1
(r/RL)6e2(r−RL)/RL + 1, (12)
whereRL is the long-range cutoff. The short-range regu-
lator comes from a Gaussian smearing of the δ-functions
in coordinate space, expressed as
CRS(r) = 1
π3/2R3
S
e−(r/RS)2
, (13)
whereRS is the Gaussian parameter governing the width
of the smearing. Consequently, two regulator parameters
need to be specified in the model.
Embedded within vS
12 are 26 unknown LECs that pa-
rameterize the strengths of the contact terms, adjusted
to fit NN scattering data [53–55]. There are four classes
of models for the NV2. Model classes denoted by I
(II) are fit to NN scattering data up to 125 (200) MeV
with a χ2/datum ≈ 1.1 (1.4). For model classes de-
noted by a (b), the regulators used in the potential are
[RL,RS] = [1.2 fm, 0.8 fm] ([RL,RS] = [1.0 fm, 0.7 fm]).
In addition to the NV2, the Norfolk models incorpo-
rate a three-body force (NV3) [56, 57] that requires the
determination of two additional LECs; namely, cD and
cE. These are fit either to the triton ground state en-
ergy andnd doublet scattering length [3] or to the triton
ground state energy and Gamow-Teller matrix element
for β-decay [4]. The latter fitting procedure corresponds
4
FIG. 2: Diagrams illustrating the contributions to the
electromagnetic current at N3LO adopted in this work.
Nucleons, pions, and external fields are denoted by
solid, dashed, and wavy lines, respectively. The solid
circle in panel (f) is associated with a sub-leading γπN
interaction. Figure from Ref. [6].
to the model classes denoted with a star, which are the
ones used in this work.
