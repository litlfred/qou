---
doc_id: arxiv-0811.1338v1
doc_title: "Modern Theory of Nuclear Forces"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
toc_source: undetermined
doc_brief: "Modern Theory of Nuclear Forces — 52 sections: Page 1; Page 2; Page 3"
---
ing in the loop graphs) and the gi denotes a collection
of coupling constants, often called low-energy constants
(LECs). These parameterize (encode) the unknown high-
energy (short-distance) physics and must be determined
by a ﬁt to data (or can be directly calculated if the cor-
responding high-energy theory is known/can be solved).
The counting index ν in general depends on the ﬁelds
in the eﬀective theory, the number of derivatives and
the number of loops. This deﬁnes the so-called power
counting which allows to categorize all contributions to
any matrix element at a given order.
It is important
to stress that ν must be bounded from below to deﬁne
a sensible EFT. In QCD e.g. this is a consequence of
the spontaneous breaking of its chiral symmetry.
The
contributions with the lowest possible value of ν deﬁne
the so-called leading order (LO) contribution, the ﬁrst
corrections with the second smallest allowed value of ν
the next-to-leading order (NLO) terms and so on.
In
contrast to more conventional perturbation theory, the
small parameter is not a coupling constant (like, e.g., in
Quantum Electrodynamcis) but rather one expands in
small energies or momentum, where small refers to the
hard scale Λ. The archetype of such a perturbative EFT
is chiral perturbation theory that exploits the strictures
of the spontaneous and explicit chiral symmetry break-
ing in QCD (35; 36). Here, the light degrees of freedom
are the pions, that are generated through the symmetry
violation. Heavier particles like e.g. vector mesons only
appear indirectly as they generate local four-pion interac-
tions with four, six, . . . derivatives. For a recent review,
see Ref. (37). Of course, the pions also couple to heavy
matter ﬁelds like e.g. nucleons, that can also be included
in CHPT, as reviewed by Bernard (38).
So far, we have made the implicit assumption of nat-
uralness, which implies e.g. that the scattering length
a is of natural size as e.g.
in CHPT, where the scale
is set by 1/Λχ ≃1 GeV−1 ≃0.2 fm. This also implies
that there are no bound states close to the scattering
thresholds. In many physical systems and of particular
interest here, especially in the two-nucleon system, this is
not the case, but one rather has to deal with unnaturally
large scattering lengths (and also shallow bound states).
To be speciﬁc, let us consider nucleon-nucleon scattering
at very low energies in the 1S0 channel, cf. Eq. (1.10).
For such low energies, even the pions can be considered
heavy and are thus integrated out. To construct an EFT
that is applicable for momenta p > 1/a, one must retain
all terms ap ∼1 in the scattering matrix. This requires
a non-perturbative resummation and is most elegantly
done in the power divergence scheme of Kaplan, Savage
and Wise (39; 40). This amounts to summing the lead-
ing four-nucleon contact term ∼C0(ψ†ψ)2 to all orders
in C0 and matching the scale-dependent LEC C0 to the
scattering length. This leads to the T-matrix
T = 4π
m
1
1/a + ip

1 + O(p2)

,
(1.13)
where the expansion around the large scattering length
is made explicit.
All other eﬀects, like e.g.
eﬀective
range corrections, are treated perturbatively. This com-
pact and elegant scheme is, however, not suﬃcient for
discussing nuclear processes with momenta p ≥Mπ. We
will come back to this topic when we give the explicit con-
struction of the chiral nuclear EFT in sec. II.B. It is im-
portant to stress that such EFTs with unnaturally large
scattering length can exhibit universal phenomena that
can be observed in physical systems which diﬀer in their
typical energy scale by many orders of magnitude, for a
review see Braaten and Hammer (41). We also remark
that there are many subtleties in constructing a proper
EFT, but space forbids to discuss these here. Whenever
appropriate and/or neccessary, we will mention these in
the following sections and provide explicit references.
E. First results from lattice QCD
Lattice QCD (LQCD) is a promising tool to calculate
hadron properties ab initio from the QCD Lagrangian on
a discretized Euclidean space-time. This requires state-
of-the-art high performance computers and reﬁned algo-
rithms to analyse the QCD partition function by Monte
Carlo methods. Only recently soft- and hardware devel-
opments have become available that allow for full QCD
simulations at small enough quark masses (correspond-
ing to pion masses below 300 MeV), large enough vol-
umes (corresponding to spatial dimensions larger than
2.5 fm) and suﬃciently ﬁne lattice spacing (a ≃0.05 fm)
so that the results are not heavily polluted by computa-
tional artefacts and can really be connected to the phys-
ical quark masses by sensible chiral extrapolations.
For the nuclear force problem, there are two main de-
velopments in LQCD to be reviewed here. These con-
cern the extraction of hadron-hadron scattering lengths
from unquenched simulations and the ﬁrst attempts to
construct a nuclear potential. These are groundbreaking
studies, but clearly at present one has not yet achieved an
accuracy to obtain high-precision predictions for nuclear
properties. We look very much forward to the develop-
ment of these approaches in the years to come.
The ﬁrst exploratory study of the nucleon-nucleon
scattering lengths goes back to Fukugita et al. (42; 43)
in the quenched approximation. They make use of an
elegant formuala, frequently called the “L¨uscher for-
mula”, that relates the S-wave scattering length a0 be-
tween two hadrons h1 and h2 to the energy shift δE =
Eh1h2 −(m1 + m2) of the two-hadron state at zero rela-
tive momentum conﬁned in spatial box of size L3. It is
given by (44; 45; 46)
δE = −2πa0
µL3

1 + c1
a0
L + c2
a2
0
L2

+ O(L−6) ,
(1.14)
with µ = m1m2/(m1 + m2) the reduced mass and c1 =
2.837297 and c2 = 6.375183.
A generalization of this
formalism was given by Beane et al.(47) utilizing methods
developed for the so-called pionless nuclear EFT (EFT
