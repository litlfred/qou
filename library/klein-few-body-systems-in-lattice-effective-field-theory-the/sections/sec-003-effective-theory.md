---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-003-effective-theory
section_title: "Effective Theory"
section_number: null
pages: 9-11
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
Eﬀective theory played a role in particle physics already long before the discovery of quarks and the
full formulation of the standard model. For example, Fermi’s theory of the beta decay [9],n→ pe−¯νe,
where a neutron decays into a proton, an electron and a neutrino can be understood as an eﬀective theory
of the standard model. In a modern language, the process is mediated by a W-boson with a mass of
mW = 80 GeV as shown in Fig. 1.2. As long as we remain in the low-energy regime in which q2≪ m2
W,
the propagator can be replaced by a contact interaction that is equivalent to Fermi’s contact interaction.
In the low-energy limit of quantum chromodynamics a similar approach can be employed. Due to
the strong coupling resulting in quark conﬁnement, the quarks always form colorless objects, namely
hadrons and it is impossible to observe single quarks or gluons. This means that quarks and gluons are
not a suitable set of degrees of freedom, so we could formulate our theory with a new set of degrees of
freedom. Naturally, hadrons are such a suitable set of degrees of freedom as they are observable at the
low-energy scale.
For the construction of the new Lagrangian, only the symmetries of QCD must be preserved, which
3
Chapter 1 Introduction and Motivation
≈ 1
q2−m2
W
≈ − 1
m2
W
Figure 1.2: Fermi’s beta decay. Left: Exact picture. Right: Eﬀective picture for q2≪ m2
W.
leads to the emergence of inﬁnitely many terms and a non-renormalizable theory in general. Once all
terms are included, one reproduces the underlying theory exactly, as stated by Weinberg [10],
"if one writes down the most general possible Lagrangian, including all terms consistent
with assumed symmetry principles, and then calculates matrix elements with this Lagrangian
to any given order of perturbation theory, the result will simply be the most general possible
S-matrix consistent with analyticity, perturbative unitarity, cluster decomposition and the
assumed symmetry principles. "
Fortunately, not all terms are equally important and a power counting scheme is introduced to classify
the importance of the terms. Consequently, one has to deal only with a ﬁnite number of terms at each
order and the theory is exact up to higher-order terms which are truncated. Such a power counting
expands inO(Q/Λ), where Q is a small expansion parameter with respect to the breakdown scale of the
theory, Λ. Once a counting scheme is set up, it can be used to classify quantum corrections in the form of
Feynman loops as well and now it is possible to solve the theory completely up to an accuracy ofO(Q/Λ)
in an energy region below Λ. To be speciﬁc, we start from the Lagrangian written in Eq. (1.2). On the
one hand, the masses of the u-, d-, and s-quark are given by 2.2 MeV , 4.7 MeV and 96 MeV , and they
are called light quarks. On the other hand, the masses of the c-, b- and t-quark are given by 1.28 GeV ,
4.18 GeV and 173.1 GeV , and they are called heavy quarks. As we stay in the low-energy limit, we can
neglect the heavy quarks and integrate them out of the theory. Then Eq. (1.2) reduces to the light quark
sector with f = 1, 2, 3. By assuming the light quark masses to vanish in the so-called chiral limit, a new
SU(3)L× SU(3)R symmetry emerges in the ﬂavor sector, whose ground state symmetry is spontaneously
broken to SU(3)V. Over and above neglecting the heavy quark sector, one could integrate out the s-quark
as well, and we have a SU(2)L× SU(2)R/ SU(2)V symmetry where pions are the respective Goldstone
bosons of the theory. With these symmetry groups in mind, one builds up the whole Lagrangian. In
the meson sector, this work started in the 1980s mainly by Gasser and Leutwyler in the framework of
chiral perturbation theory (ChPT) [11, 12]. The ﬁrst extension to the two-nucleon sector was done by
[13, 14]. In the following two decades this framework has been extended to the baryon-meson sector in
the non-relativistic approach of heavy-baryon ChPT (HBChPT) [15, 16] and the relativistic approach
of extended on-mass shell (EOMS) renormalization scheme [17, 18]. An extended review on chiral
perturbation theory in the meson- and one-nucleon sector is given by [19, 20]. While the meson sector
must be formulated relativistically due to the lightness of its constituents, the meson-baryon sector can
be formulated in both ways, and the nucleon-nucleon sector is formulated non-relativistically.
In the formulation of the nucleon-nucleon action an important question concerning the scales appears.
Generally, the scale is set by the breakdown scale of ChPT, ΛChPT∼ 4πF0∼ 1.2 GeV with the pion
decay constant F0 = 92.1 MeV . However, in most of the reactions vector meson resonances play a role
although they are not included explicitly. This results in a decrease of validity below theρ resonance,
Mρ∼ 770 MeV . In the nucleon sector we do not use dimensional regularization or power-divergence
subtraction schemes for the absorption of possible ultraviolet divergences, but we use a momentum cutoﬀ
4
