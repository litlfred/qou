---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-011-4-fusion-rules
section_title: "Fusion Rules:"
section_number: 4
pages: 32-36
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 19 sections: A Hamiltonian; Instantons; Dirac Monopoles"
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.985
---
The fusion rules for $A_5$ can be found in the following pages. Once again every particle is its own antiparticle. Note that, unlike in the $S_3$ case, there are multiple ways of obtaining some of the products - For instance, E and F can fuse to produce E in two distinct ways.

<figure id="fig:A5a">
<img src="A5a.jpg" style="width:19cm;height:9cm" />
<figcaption>Fusion Rules for <span class="math inline"><em>A</em><sub>5</sub></span></figcaption>
</figure>

<figure id="fig:A5b">
<img src="A5b.jpg" style="width:19cm;height:9cm" />
<figcaption>Fusion Rules for <span class="math inline"><em>A</em><sub>5</sub></span></figcaption>
</figure>

<figure id="fig:A5c">
<img src="A5c.jpg" style="width:19cm;height:9cm" />
<figcaption>Fusion Rules for <span class="math inline"><em>A</em><sub>5</sub></span></figcaption>
</figure>

<figure id="fig:A5d">
<img src="A5d.jpg" style="width:19cm;height:9cm" />
<figcaption>Fusion Rules for <span class="math inline"><em>A</em><sub>5</sub></span></figcaption>
</figure>

# MAGMA Program and Discussion of Results

The tables computed in this paper were produced using the MAGMA program included in Appendix 1. The MAGMA program computes the particles (and their properties - e.g. spin), braiding, and fusion rules for an arbitrary finite residual gauge group. The program can also explicitly compute the entries of the S matrix. As part of the fusionprinter(Group) procedure, the MAGMA program computes the change of basis S matrix and implements the Verlinde formula to determine the fusion coefficients based on the S matrix for an arbitrary group.

In addition, the MAGMA program can compute the probabilities of obtaining any given fusion product used in many different topological quantum computation schemes. More detail on this connection is provided in the next section.

The two examples included here were chosen mainly due to their possible applications to universal quantum computation (as described in the next section). In particular, since $S_3$ is the smallest non-abelian group, a method for achieving universal quantum computation in that case has the best chance of being engineered in the lab or found in nature.

In Appendix B, the quantum doubles for the remaining finite subgroups of $SO(3)$ are tabulated and analyzed. Each of these are interesting from either a physics theory or implementation point of view. For example, from the physics theory perspective, in the two theories $S_3$ and $A_5$ discussed above, every particle is its own antiparticle. However, this is not always the case and $A_4$ illustrates this point. Furthermore, other dihedral groups, for example, could be interesting from the implementation perspective as they arise naturally from spontaneous symmetry breaking in p-wave superconductors.

## Majorana Particles

From the fusion tables derived for $S_3$ and $A_5$, every particle is its own antiparticle, i.e. the particles are all Majorana. Most commonly, photons are their own antiparticles. However, Majorana particles of noninteger spin are currently an active area of research in physics, even beyond condensed matter applications. In particular, neutrinos are conjectured by some to be Majorana and SUSY would demand a fermionic photino as the fermionic superpartner of the photon (among many other Majorana particles). Finally, one suggestion is that WIMPS (a dark matter candidate, possibly the dominant component of dark matter mass in our universe) are also Majorana.

# Quantum Computation Schemes

## Universal Quantum Computation

Universal computation: any unitary operation can be approximated to arbitrary accuracy

## Schemes for Topological Quantum Computation

States used in a topological quantum computation scheme must be selected according to their fusion rules since the environment can distinguish between states fusing to different superselection sectors, causing decoherence. In addition, most implementation proposals use particle-antiparticle pairs as the fundamental building block since these interact trivially with other pairs when kept far apart from each other. Braiding computations are achieved by transporting a given pair in between other pair(s).

If anyons from different superselection sectors are used in the actual quantum computation scheme, then two distance scales come into play. In particular, the anyons must be kept far enough apart from each other that they cannot influence each other by local interactions (and thus superselection sectors are exhibited). Similarly, the environment must be far enough removed that it can only detect the cumulative long range quantum numbers of the whole system. (This provides protection against decoherence.)

The prototype of anyon computation based on superselection sectors is the Fibonacci (also known as Yang-Lee) anyons, in which there are only two superselection sectors 0 and 1, with nontrivial fusion rule $1\times1=0+1$. The dimension of the Hilbert space fusing to the vacuum increases exponentially in the golden ratio $\phi=\dfrac{1+\sqrt{5}}{2}$. The associated R-matrix and its F-matrix conjugate $FR F^{-1}$ then form a dense subgroup of $SU(2)$. Thus any unitary operation can be approximated with arbitrary accuracy and universal quantum computation is possible. The Fibonacci anyons have spin given by $\frac{4}{5}$ (This can be obtained by, for instance, solving the pentagon and hexagons explicitly for the R matrix and then using the generalized spin-statistics connection to infer the spins.) Thus this model is equivalent to $SO(3)_3$ (the restriction of $SU(2)_3$).
