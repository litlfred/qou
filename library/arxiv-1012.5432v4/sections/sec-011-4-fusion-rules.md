---
doc_id: arxiv-1012.5432v4
doc_title: ""
section_id: sec-011-4-fusion-rules
section_title: "Fusion Rules:"
section_number: 4
pages: 32-36
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
doc_brief: "quant-ph Towards Topological Quantum Computation? - — 19 sections: A Hamiltonian; Instantons; Dirac Monopoles"
---
The fusion rules for A5 can be found in the following pages. Once again every particle is
its own antiparticle. Note that, unlike in the S3 case, there are multiple ways of obtaining
some of the products - For instance, E and F can fuse to produce E in two distinct ways.
IX. MAGMA PROGRAM AND DISCUSSION OF RESULTS
The tables computed in this paper were produced using the MAGMA program included
in Appendix 1. The MAGMA program computes the particles (and their properties - e.g.
spin), braiding, and fusion rules for an arbitrary ﬁnite residual gauge group. The program
can also explicitly compute the entries of the S matrix. As part of the fusionprinter(Group)
procedure, the MAGMA program computes the change of basis S matrix and implements the
Verlinde formula to determine the fusion coeﬃcients based on the S matrix for an arbitrary
group.
In addition, the MAGMA program can compute the probabilities of obtaining any given
fusion product used in many diﬀerent topological quantum computation schemes. More
detail on this connection is provided in the next section.
32
FIG. 6: Fusion Rules for A5
The two examples included here were chosen mainly due to their possible applications to
universal quantum computation (as described in the next section). In particular, since S3
is the smallest non-abelian group, a method for achieving universal quantum computation
in that case has the best chance of being engineered in the lab or found in nature. In
Appendix B, the quantum doubles for the remaining ﬁnite subgroups ofSO(3) are tabulated
and analyzed. Each of these are interesting from either a physics theory or implementation
point of view. For example, from the physics theory perspective, in the two theories S3 and
A5 discussed above, every particle is its own antiparticle. However, this is not always the
case and A4 illustrates this point. Furthermore, other dihedral groups, for example, could
be interesting from the implementation perspective as they arise naturally from spontaneous
symmetry breaking in p-wave superconductors.
A. Majorana Particles
From the fusion tables derived forS3 andA5, every particle is its own antiparticle, i.e. the
particles are all Majorana. Most commonly, photons are their own antiparticles. However,
Majorana particles of noninteger spin are currently an active area of research in physics, even
33
FIG. 7: Fusion Rules for A5
beyond condensed matter applications. In particular, neutrinos are conjectured by some to
be Majorana and SUSY would demand a fermionic photino as the fermionic superpartner of
the photon (among many other Majorana particles). Finally, one suggestion is that WIMPS
(a dark matter candidate, possibly the dominant component of dark matter mass in our
universe) are also Majorana.
X. QUANTUM COMPUTATION SCHEMES
A. Universal Quantum Computation
Universal computation: any unitary operation can be approximated to arbitrary accuracy
B. Schemes for Topological Quantum Computation
States used in a topological quantum computation scheme must be selected according to
their fusion rules since the environment can distinguish between states fusing to diﬀerent
superselection sectors, causing decoherence. In addition, most implementation proposals
use particle-antiparticle pairs as the fundamental building block since these interact trivially
34
FIG. 8: Fusion Rules for A5
with other pairs when kept far apart from each other. Braiding computations are achieved
by transporting a given pair in between other pair(s).
If anyons from diﬀerent superselection sectors are used in the actual quantum compu-
tation scheme, then two distance scales come into play. In particular, the anyons must be
kept far enough apart from each other that they cannot inﬂuence each other by local inter-
actions (and thus superselection sectors are exhibited). Similarly, the environment must be
far enough removed that it can only detect the cumulative long range quantum numbers of
the whole system. (This provides protection against decoherence.)
The prototype of anyon computation based on superselection sectors is the Fibonacci
(also known as Yang-Lee) anyons, in which there are only two superselection sectors 0 and
1, with nontrivial fusion rule 1× 1 = 0 + 1. The dimension of the Hilbert space fusing to the
vacuum increases exponentially in the golden ratio φ = 1 +
√
5
2 . The associated R-matrix
and its F-matrix conjugateFRF−1 then form a dense subgroup ofSU (2). Thus any unitary
operation can be approximated with arbitrary accuracy and universal quantum computation
is possible. The Fibonacci anyons have spin given by4
5 (This can be obtained by, for instance,
solving the pentagon and hexagons explicitly for the R matrix and then using the generalized
spin-statistics connection to infer the spins.) Thus this model is equivalent to SO(3)3 (the
35
