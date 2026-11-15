---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-7
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
Few-Body Systems in
Lattice Eﬀective Field Theory
Dissertation
zur
Erlangung des Doktorgrades (Dr. rer. nat.)
der
Mathematisch-Naturwissenschaftlichen Fakultät
der
Rheinischen Friedrich-Wilhelms-Universität Bonn
von
Nico Klein
aus
Bonn, November 2018
Dieser Forschungsbericht wurde als Dissertation von der Mathematisch-Naturwissenschaftlichen
Fakultät der Universität Bonn angenommen und ist auf dem Hochschulschriftenserver der ULB Bonn
http://hss.ulb.uni-bonn.de/diss_online elektronisch publiziert.
1. Gutachter:
Prof. Dr. Ulf-G. Meißner
2. Gutachter:
Prof. Dr. Thomas Luu
Tag der Promotion:
11.01.2019
Erscheinungsjahr:
2019
Abstract
Nuclear lattice eﬀective ﬁeld theory is a novel approach in nuclear physics combining classical eﬀective
ﬁeld theory with lattice methods and newly available computational resources. It is particularly successful
for few- and many-body systems, where one calculates ground state and scattering state properties using
ab initio techniques. Thanks to the discretization of space and time, one can use Monte Carlo methods to
evaluate physical observables and additionally, one may use discretization improvement programs as
well for the reduction of lattice spacing artifacts. In contrast to lattice quantum chromodynamics, the
lattice spacing does have a physical meaning, namely the cutoﬀwhich is inherent to any eﬀective theory.
Hence, it is necessary to understand the discretization eﬀects. Such a study has been a missing part of
nuclear lattice eﬀective ﬁeld theory as most calculations have been performed at a ﬁxed lattice spacing
of a = 1.97 fm. I will have a thorough look at it and examine the problem from diﬀerent perspectives
in the following. Due to computational limitations we restrict ourselves to few-body systems, where
we have a lot of data from Nijmegen partial wave analysis for nucleon-nucleon scattering, very precise
knowledge on the bound state of triton and helium-4 and also various correlation theorems. The Tjon
line is such a correlation theorem between triton and helium-4 binding energies which states that the
two-nucleon interaction results in a correlated prediction of triton and helium binding energies while a
three-nucleon interaction that ﬁxes the triton binding energy automatically reproduces the right helium-4
binding energy.
The ﬁrst project looks at the deuteron binding energy and low-energy scattering observables, namely the
S wave scattering length and eﬀective range in dependence on the lattice spacing for various regularization
schemes. We employ lattice spacings up to a = 0.5 fm and we show that the neutron-proton system with
and without pion exchange becomes stable if the regularization scheme is chosen rightly and the lattice
spacing is small enough.
Secondly, I perform an analysis of 2N, 3N and 4N systems for three diﬀerent lattice spacings at
leading, next-to-leading and next-to-next-to-leading order. I show that the continuum correlation between
3N and 4N systems is reproduced once the lattice spacing is chosen ﬁne enough.
Lastly, I examine the few-body boson system in one dimension. Such a system does have an exact
solution and hence, lattice artifacts can be observed in a very transparent way. I show that we can absorb
lattice spacing artifacts systematically by adding additional operators due to a consistent power counting
scheme. Finally, we can do robust continuum extrapolations. We examine systems up to and including
ﬁve bosons and the remaining errors scale linearly, as the third and fourth power of the lattice spacing at
leading, next-to-leading and next-to-next-to-leading order.
iii
During the time of my thesis, the following articles have been published:
1. N. Klein, D. Lee, W. Liu and U.-G. Meißner, “Regularization Methods for Nuclear Lattice Eﬀective
Field Theory,” Phys. Lett. B 747 (2015) 511.
2. S. Elhatisari, N. Li, A. Rokash, J. M. Alarcón, D. Du, N. Klein, B.-N. Lu, U.-G. Meißner,
E. Epelbaum, H. Krebs, T. A. Lähde, D. Lee and G. Rupak, “Nuclear binding near a quantum
phase transition,” Phys. Rev. Lett. 117 (2016) no.13, 132501.
3. J. M. Alarcón, D. Du, N. Klein, T. A. Lähde, D. Lee, N. Li, B.-N. Lu, T. Luu and U.-G. Meißner,
“Neutron-proton scattering at next-to-next-to-leading order in Nuclear Lattice Eﬀective Field
Theory,” Eur. Phys. J. A 53 (2017) no.5, 83.
4. N. Klein, S. Elhatisari, T. A. Lähde, D. Lee and U.-G. Meißner, “The Tjon Band in Nuclear Lattice
Eﬀective Field Theory,” Eur. Phys. J. A 54 (2018) no.7, 121.
5. N. Klein, D. Lee and U.-G. Meißner, “Lattice Improvement in Lattice Eﬀective Field Theory,”
arXiv:1807.04234 [hep-lat].
Article 1, 4 and 5 are the basis for this thesis.
iv
Contents
1
Introduction and Motivation
1
1.1
The standard model of particle physics and quantum chromodynamics . . . . . . . . .
1
1.2
Lattice QCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.3
Eﬀective Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.4
From nucleons to nuclei . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.5
Quantum Monte Carlo methods - status and open challenges . . . . . . . . . . . . . .
5
2
Theory
9
2.1
The eﬀective theory of few-nucleon systems . . . . . . . . . . . . . . . . . . . . . . .
9
2.2
Scattering Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.2.1
Basic concepts of scattering theory . . . . . . . . . . . . . . . . . . . . . . . .
13
2.2.2
Extension to systems with internal degrees of freedom and coupled channels
.
17
2.2.3
Scattering theory for Coulomb forces
. . . . . . . . . . . . . . . . . . . . . .
18
2.3
Correlations in Few-Body physics . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3
Nuclear Lattice Effective Field Theory
21
3.1
Eﬀective theory on the lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
3.2
The reduced symmetry of SO(3, Z) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.3
Bound states on the lattice
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
3.4
Scattering on the lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.4.1
Lüscher’s eﬀective range expansion in the ﬁnite volume
. . . . . . . . . . . .
26
3.4.2
Spherical wall and radial projection . . . . . . . . . . . . . . . . . . . . . . .
26
3.5
Exact methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
3.6
The auxiliary ﬁeld partition function . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3.7
Hybrid Monte Carlo algorithm for Nuclear Lattice Eﬀective Field Theory . . . . . . .
33
3.8
The sign problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
4
Regularization Methods for Nuclear Lattice Effective Field Theory
39
4.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
4.2
The lattice Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
4.3
The pionless theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
4.4
The pionful theory
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
4.5
Conclusion and Outlook
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
5
The Tjon band in Nuclear Lattice Effective Field Theory
49
5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
5.2
Two-body-sector
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
5.2.1
Theoretical framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
v
5.2.2
Results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
5.3
Three-body sector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
5.3.1
Theoretical framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
5.3.2
Results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
5.4
Four-body sector
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
5.4.1
Theoretical framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
5.4.2
Results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64
5.5
The Tjon band . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
5.5.1
Theoretical framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
5.5.2
Results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
5.6
Conclusion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
6
Lattice Improvement in Lattice Effective Field Theory
69
6.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
6.2
Bosons in one dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
6.3
Lattice implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
6.4
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
6.5
Summary and outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
7
Conclusions and Perspectives
79
A
Special functions and algebras
83
A.1
Partial wave decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
A.2
Pauli matrices and spin algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
A.3
Anticommutator and Grassmann algebra . . . . . . . . . . . . . . . . . . . . . . . . .
85
B
Density and current operators
87
C
Uncertainty analysis
89
D
Loop integrals
91
E
Non-perturbative calculation of lattice artifacts in the two-boson sector
93
Bibliography
97
vi
CHAPTER 1
