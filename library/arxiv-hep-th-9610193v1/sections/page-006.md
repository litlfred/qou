---
doc_id: arxiv-hep-th-9610193v1
doc_title: "KNOTS AND PARTICLES"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9610193v1.pdf
source_sha256: e879864ec3a68faf
toc_source: undetermined
doc_brief: "KNOTS AND PARTICLES — 14 sections: Page 1; Page 2; Page 3"
---
plane. Besides the inversion invariance, the equations of motion are now also invariant
under z →−z. Since the unknot solution is even in z, this halves the CPU time in our
simulation.
In ﬁgures 1-4 we describe an unknot vortex which is a result of over 50h of CPU time
with each time step taking about 9 minutes on a 9600 triangle mesh. The mesh has
been selected so that it is more dense at the boundaries and near the core of the vortex.
In our simulation we ﬁnd impressive convergence, allowing us to increase the time step
by up to 8 orders of magnitude while keeping the relative change in energy intact. The
Hopf invariant is also very stable, and we have identiﬁed the ﬁnal conﬁguration on the
basis that the numerically computed Hopf invariant has a slight local maximum with
QH = 0.999996 ...
The trefoil vortex (QH = ±3) described in ﬁgure 5 is a result of almost 200h in
CPU time on a 213 cubic ﬁnite element lattice with tri-cubic Hermite basis functions.
Consequently the number of nodes is about the same as in the case of unknot, but due
to a lack of any obvious reﬂection symmetry each time iteration now takes about 20
minutes of CPU time. The yellow center in ﬁgure 5 corresponds to the core⃗x(λ) of
our initial conﬁguration, which has been determined using the energy concept developed
by J. Simon [16]. The points in ﬁgure 5 have been evaluated using the piecewise cubic
polynomial approximation obtained from the ﬁnite element algorithm. As in ﬁgure 4,
the picture describes a volume where the energy density inside the vortex essentially
vanishes, i.e. it can be viewed as an extended core of our trefoil vortex.
We expect that the nonhomogeneity in ﬁgure 5 reﬂects the underlying lattice struc-
ture that we have used in our simulation. Indeed, a 213 lattice is obviously too rough
to describe our trefoil solution adequately, but unfortunately we do not have access to a
computer that would allow us to use an essentially larger lattice. Nevertheless, we have
found deﬁnite numerical stability in the sense that the ﬁnal conﬁguration in ﬁgure 5 has
remained essentially intact under a large number of iterations. We view this stability as
a strong evidence that we indeed have convergence towards a trefoil vortex solution.
In conclusion, we have performed numerical simulations with a high-performance
computer to investigate knotted vortex solutions in the model introduced in [13]. By
investigating the unknot and trefoil vortices, we have found strong evidence that torus
knots indeed appear as solitons. For the unknot, we have found very impressive con-
vergence and our results for the trefoil are also quite encouraging. However, since the
computers we can access do not allow us to eﬀectively study dense three dimensional
lattices, our simulation of the trefoil is still tentative.
We expect that our results will have numerous important applications. In particular,
since the order parameter in nematic liquid crystal and 3He superﬂuid involves a unit
three vector, an experimental investigation of vortices in these materials should reveal
the existence of stable knotlike structures. We also expect that an extension of our work
5
