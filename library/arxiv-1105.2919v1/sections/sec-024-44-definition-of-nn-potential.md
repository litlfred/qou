---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-024-44-definition-of-nn-potential
section_title: "Definition of NN potential"
section_number: 4.4
pages: 34-36
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
mπ-dependent renormalization of the contact parameters and can be ignored if mπ-dependence is not an
issue.
As discussed, the irreducible 2PE, V ′
2π, is organized according to increasing orders,
V ′
2π = V
′(2)
2π
+ V
′(3)
2π
+ V
′(4)
2π
+ . . . ,
(4.52)
and was calculated in Section 4.1.2: V
′(2)
2π
is given by the contributions of Eqs. (4.9) and (4.10), V
′(3)
2π
is
made up from Eqs. (4.13)-(4.24), and V
′(4)
2π
is contained in Appendix D.
The contact potentials come in even orders,
Vct = V (0)
ct
+ V (2)
ct
+ V (4)
ct
+ . . . ,
(4.53)
and were presented in Section 4.3.
In summary, the NN potential V , calculated to certain orders, is given by:
VLO
=
V1π + V (0)
ct
(4.54)
VNLO
=
VLO + V
′(2)
2π
+ V (2)
ct
(4.55)
VNNLO
=
VNLO + V
′(3)
2π
(4.56)
VN3LO
=
VNNLO + V
′(4)
2π
+ V (4)
ct
(4.57)
The potential V satisﬁes the relativistic BbS equation, Eq. (4.45), which reads explicitly,
T(⃗p ′,⃗p) = V (⃗p ′,⃗p) +
Z
d3p′′
(2π)3 V (⃗p ′,⃗p ′′) M 2
N
Ep′′
1
p2 −p′′2 + iϵ T(⃗p ′′,⃗p)
(4.58)
with Ep′′ ≡
q
M 2
N + p′′2. The advantage of using a relativistic scattering equation is that it automatically
includes relativistic corrections to all orders. Thus, in the scattering equation, no propagator modiﬁcations
are necessary when raising the order to which the calculation is conducted.
Deﬁning
bV (⃗p ′,⃗p) ≡
1
(2π)3
s
MN
Ep′ V (⃗p ′,⃗p)
s
MN
Ep
(4.59)
and
bT(⃗p ′,⃗p) ≡
1
(2π)3
s
MN
Ep′ T(⃗p ′,⃗p)
s
MN
Ep
,
(4.60)
where the factor 1/(2π)3 is added for convenience, the BbS equation collapses into the usual, nonrelativistic
Lippmann-Schwinger (LS) equation,
bT(⃗p ′,⃗p) = bV (⃗p ′,⃗p) +
Z
d3p′′ bV (⃗p ′,⃗p ′′)
MN
p2 −p′′2 + iϵ
bT(⃗p ′′,⃗p) .
(4.61)
Since bV satisﬁes Eq. (4.61), it can be used like a usual nonrelativistic potential, and bT may be perceived as
the conventional nonrelativistic T-matrix. In applications, it is more convenient to use the K-matrix instead
of the T-matrix and to have the LS equation decomposed into partial waves: all these technical issues are
explained in detail in Appendix A of Ref. [13] where also the formulas for the calculation of np and pp (the
latter with Coulomb) phase shifts are provided. The partial wave decomposition of the operators by which
the potential is represented can be found in section 4 of Ref. [142], and numerical methods for solving the
LS equation are explained in Ref. [144].
35
