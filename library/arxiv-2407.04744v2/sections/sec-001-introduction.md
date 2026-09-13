---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
---
In this work, we present quantum Monte Carlo (QMC)
calculations, including both variational Monte Carlo
(VMC) and Green’s Function Monte Carlo (GFMC)
methods, to study magnetic moments and form factors
of A≤ 10 nuclei. We use the precise experimental mea-
surements of these electromagnetic observables to val-
idate our microscopic modeling; namely, we verify the
accuracy of the approach in which we treat the nucleus
as a system of correlated nucleons interacting amongst
themselves via two- and three-nucleon forces. Addition-
ally, we include the coupling to external electromagnetic
fields via one- and two-nucleon currents.
The specific models upon which we base this study
are the Norfolk two- and three-nucleon potentials [1–5],
derived from a χEFT that retains pions, nucleons, and
∆’s as explicit degrees of freedom. The Norfolk two- and
three-nucleon interactions are formulated in configura-
tion space and we denote them as NV2+3 throughout the
reminder of this work. The associated electromagnetic
currents – derived within the sameχEFT framework with
pions, nucleons, and ∆’s – were most recently reported
in Refs. [6, 7], where they were obtained up to next-to-
next-to-next-to-leading order (N3LO) in the chiral ex-
pansion. The LO contribution consists of the standard
single-nucleon convection and spin-magnetization terms,
while sub-leading two-nucleon currents include contribu-
tions of one- and two-pion range, as well as contact terms
∗ chambers-wall@wustl.edu
† agnech@odu.edu
‡ kingg@wustl.edu
§ saori@wustl.edu
¶ m.piarulli@wustl.edu
∗∗ schiavil@jlab.org
†† wiringa@anl.gov
encoding short-range dynamics [6].
Previous QMC calculations of magnetic moments and
transitions in A≤ 9 systems [8] highlighted the impor-
tance of sub-leading two-nucleon currents to reach agree-
ment with the available experimental data. The studies
of Ref. [8] adopt the so-called ‘hybrid approach’ where nu-
clear wave functions were determined from realistic two-
and three-nucleon interactions, specifically the Argonne
AV18 [9] and the Illinois-7 [10], respectively. Mean-
while, the electromagnetic currents were derived from
χEFT [11–14], thus under-utilizing the full potential of
theχEFT framework to make systematic determinations
of model dependencies. For instance, recent calculations
of magnetic moments, based on bothχEFT Hamiltonians
and consistently derived χEFT electromagnetic current
operators [7, 15, 16], indicated a sizable sensitivity to the
regulators inherent in the theoretical approach. Further,
the studies in Ref. [7, 15] also showed that the N3LO con-
tribution to the magnetic moment is enhanced relative to
the size expected from naive dimensional analysis.
By reexamining the evaluation of the magnetic struc-
ture of light nuclei using the NV2+3 model, in combina-
tion with consistent chiral electromagnetic currents, we
aim to verify the accuracy of our χEFT approach, un-
derstand its kinematic regime of applicability, and exam-
ine the convergence of the power expansion. As in the
study of Gamow-Teller β-decays reported in Ref. [17],
we similarly perform an in-depth analysis of two-nucleon
magnetic densities. These quantities prove again to be
instrumental in determining model dependencies, iden-
tifying universal short-range behaviors, and understand-
ing the role played by inherent parameters in the models,
such as low-energy constants and regulators.
Along with magnetic moments, the framework de-
scribed above also allows for the study of magnetic form
factors, as has already been performed for A≤ 3 sys-
tems [7]. In particular, the work of Ref. [7], based on
arXiv:2407.04744v2  [nucl-th]  4 Dec 2024
2
the hyperspherical harmonics method, showed excellent
agreement with data for magnetic form factors of A≤ 3
nuclei up to momentum transfers q∼ 4 fm−1, which is
well beyond the region of convergence forχEFT. Here, we
extend these calculations to nuclei with mass number up
to A = 10 with the VMC method to further investigate
this high-momentum behavior. We note that these are
the first QMC calculations of form factors in A = 7− 10
systems.
All together, the studies of electromagnetic proper-
ties in this work provide a benchmark of electroweak
current models against readily available data over a
wide range of kinematics. Such a wide-ranging valida-
tion is necessary, as an accurate electromagnetic current
model is needed for studies of electromagnetic transi-
tions [8, 18–21], electron-nucleus scattering [22–28], and
radiative corrections to super-allowed beta decays [29–
31]. These models are also needed to interpret future
searches for new physics [32], including precision beta-
decay at low energy- and momentum-transfer [32–37],
neutrinoless double beta decay at moderate momentum-
transfers [38–41], and long-baseline neutrino oscillation
experiments that will involve both high energy- and
momentum-transfer neutrino-nucleus scattering [42–48].
These analyses rely on theoretical inputs in order to dis-
entangle signals of new physics from nuclear physics ef-
fects; thus, an accurate understanding of the underlying
nuclear dynamics is necessary. Therefore, the compu-
tation of electromagnetic properties for light nuclei and
detailed analysis of model dependencies are pivotal for
the future of programs in both nuclear and fundamental
science.
This work is organized as follows: In Section II, we de-
tail the theoretical basis for the calculation. We review
the QMC computational technique in Section II A and
report on the NV2+3 interaction models and associated
electromagnetic current used in this work in Sections II B
and II C, respectively. Section II D contains the multi-
pole analysis relating QMC matrix elements to electro-
magnetic observables. Magnetic moments and two-body
magnetic densities computed in this formalism are pre-
sented in Section III A. This is followed, in Section III B,
by a detailed discussion of magnetic form factors that
supplements the results and extends the analysis of a
PRL submitted concurrently to this article [49]. Finally,
we give concluding remarks in Section IV.
II. THEORY
