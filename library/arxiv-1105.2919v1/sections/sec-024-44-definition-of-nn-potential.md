---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-024-44-definition-of-nn-potential
section_title: "Definition of NN potential"
section_number: 4.4
pages: 34-35
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
We have now rounded up everything needed for a realistic nuclear force—long, intermediate, and short
ranged components—and so we can ﬁnally proceed to the lower partial waves. However, here we encounter
another problem. The two-nucleon system at low angular momentum, particularly, in S waves, is character-
ized by the presence of a shallow bound state (the deuteron) and large scattering lengths. Thus, perturbation
theory does not apply. In contrast to π-π and π-N, the interaction between nucleons is not suppressed in
the chiral limit (Q →0). Weinberg [50, 51] showed that the strong enhancement of the scattering amplitude
arises from purely nucleonic intermediate states (“infrared enhancement”). He therefore suggested to use
perturbation theory to calculate the NN potential (i.e., the irreducible graphs) and to apply this potential
in a scattering equation to obtain the NN amplitude. We will follow this prescription and discuss potential
problems in the next subsection.
Since the irreducible diagrams that make up the potential are calculated using covariant perturbation
theory (cf. Section 4.1), it is consistent to start from the covariant Bethe-Salpeter (BS) equation [143]
describing two-nucleon scattering. In operator notation, the BS equation reads
T = V + V G T
(4.44)
where T denotes the invariant T-matrix (T = iM with M the invariant amplitude) for the two-nucleon
scattering process, V the sum of all connected two-particle irreducible diagrams, and G is (−i) times the
relativistic two-nucleon propagator. The BS equation is equivalent to a set of two equations
T
=
V + V g T
(4.45)
V
=
V + V (G −g) V
(4.46)
=
V + V1π (G −g) V1π + . . . ,
(4.47)
where g is a covariant three-dimensional propagator which preserves relativistic elastic unitarity. We choose
the propagator g proposed by Blankenbecler and Sugar (BbS) [133] (for more details on relativistic three-
dimensional reductions of the BS equation, see Ref. [11]). The ellipsis in Eq. (4.47) stands for terms of
irreducible 3π and higher pion exchanges which we neglect.
Note that when we speak of covariance in conjunction with (heavy baryon) ChPT, we are not referring
to manifest covariance. Relativity and relativistic oﬀ-shell eﬀects are accounted for in terms of a Q/MN
expansion up to the given order and up to the number of pions we take into consideration. Thus, Eq. (4.47)
is evaluated in the following way,
V
≈
V(on-shell) + V1π G V1π −V1π g V1π
(4.48)
≈
V1π + eV2π + V1π G V1π −V1π g V1π
(4.49)
=
V1π + V ′
2π ,
(4.50)
where V1π denotes the relativistic (oﬀ-shell) 1PE, while V1π is the on-shell 1PE given in Eq. (4.5). eV2π stands
for the irreducible 2π exchanges calculated (on-shell) in Section 4.1.2, but without the covariant planar box
diagram, which in the above equations is given by V1π G V1π. Furthermore, V1π g V1π is the iterated 1PE
discussed in Section 4.1.2. Thus, the term (V1π G V1π −V1π g V1π) represents the irreducible part of the box
diagram contribution. Finally, V ′
2π subsumes all 2π exchanges without the iterated V1π and is, therefore,
also known as the irreducible 2PE. Since all contributions are calculated on shell, the potential has no energy
dependence.
Adding the short-range contact terms Vct to the above, yields the full NN potential,
V = V1π + V ′
2π + Vct .
(4.51)
Notice that the pion-exchange part of this potential diﬀers from the perturbative amplitude, Eq. (4.30),
by the absence of the iterative 2PE. The latter is generated automatically when the potential is inserted
into a Schroedinger or Lippmann-Schwinger equation (see below). We also note that adding the contact
34
interactions to the pion interactions will generate loop corrections of the contact terms. This leads to a
