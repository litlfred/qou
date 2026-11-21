---
doc_id: arxiv-2212.04436v1
doc_title: "Dilute neutron star matter from neural-network quantum states"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 2212.04436v1.pdf
source_sha256: 0f98a851d030ec05
toc_source: undetermined
doc_brief: "Dilute neutron star matter from neural-network quantum states — 6 sections: Page 1; Page 2; Page 3"
---
0.010
0.015
0.020
0.025
0.030
0.035
0.040
Density (fm−3)
4
6
8
10
12
14
Energy (MeV)
/πEFT
AV18+UIX
Fermi Gas
FIG. 2. Low-density neutron-matter /πEFT equation of state
as obtained with the hidden-nucleon NQS (solid green circles)
compared with FHNC/SOC calculations with the AV18+UIX
Hamiltonian (red triangles) and the non-interacting Fermi
Gas (solid blue line).
As shown in Fig. 1 for ρ = 0.04 fm−3, after ≃2000
stochastic-reconﬁguration steps, the NQS ansatz con-
verges to the virtually exact unconstrained AFDMC en-
ergy, using a fraction of its computing time:
about
100 hours on NVIDIA-A100 GPUs vs approximately
1.2 million hours on Intel-KNL CPUs. Notice that the
constrained-path approximation violates the variational
principle. In contrast, variational Monte Carlo calcula-
tions based on the NQS never yield energies below that
of the Hamiltonian’s ground state. Comparing with the
Hartree-Fock approximation, it appears that the hidden-
nucleon ansatz captures the overwhelming majority of
the correlation energy.
In Fig. 2, we compare the /πEFT energies obtained with
the NQS ansatz against Fermi hypernetted chain/single-
operator chain calculations that take as input the so-
phisticated AV18+UIX Hamiltonian, consistent with the
celebrated APR equation of state [40]. For all densities
considered, /πEFT and AV18+UIX are in excellent agree-
ment, the maximum diﬀerence being always below 0.30
MeV per particle — both of them provide energies much
below the non-interacting Fermi gas. These minor diﬀer-
ences are likely because model “o” yields a slightly larger
nn scattering length than the experimental value and,
therefore, more attraction in neutron matter. The latter
is not compensated for by the three-body force, whose
repulsive contribution is at most 0.25 MeV per neutron.
Once trained on the systems’ energy,
the NQS
can
be
used
to
accurately
evaluate
a
variety
of
quantum-mechanical observables, such as the spin-singlet
and triplet two-body distribution functions deﬁned in
Ref. [48]. Figure 3 shows these distributions at ρ = 0.01
fm−3 (panel a) and ρ = 0.04 fm−3 (panel b). The sig-
niﬁcant increase in the spin-singlet channel compared to
the non-interacting Fermi Gas indicates that the NQS
wave function can capture the emergence of the
1S0
neutron pairing, despite not being explicitly encoded in
the ansatz.
Consistent with the behavior of the pair-
ing gap [13, 22], the enhancement is more prominent at
ρ = 0.01 fm−3 than ρ = 0.04 fm−3. On the other hand,
at these densities, no pairing correlations are present in
the spin-triplet channel.
Conclusions –
In this work, we have put forward an
NQS suitable to model the normal and superﬂuid phases
of inﬁnite neutron matter in a uniﬁed fashion. We im-
prove the expressivity of the hidden-nucleon ansatz of
Ref. [29] by adding state-dependent generalized back-
ﬂow correlations, whose inclusion has proven beneﬁcial
in condensed-matter applications [32, 33]. Periodic-box
boundary conditions are imposed by mapping the spatial
coordinates of the neutrons onto periodic functions.
Combined with Monte Carlo techniques to sample the
Hilbert space and the stochastic-reconﬁguration algo-
rithm to optimize the variational parameters, the NQS
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
5.5
r [fm]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
g(r)
(a)
Singlet Fermi Gas
Triplet Fermi Gas
Singlet NQS
Triplet NQS
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
r [fm]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
g(r)
(b)
Singlet Fermi Gas
Triplet Fermi Gas
Singlet NQS
Triplet NQS
FIG. 3. Spin-singlet and triplet two-body distribution func-
tions at ρ = 0.01 fm−3 (panel a) and ρ = 0.04 fm−3 (panel
b). The NQS calculations (solid symbols) are compared with
non-interacting Fermi Gas results.
