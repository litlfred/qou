---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-015-2-two-dimensions
section_title: "Two Dimensions"
section_number: 2
pages: 14-15
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
***Indistinguishable Particles: Braid Group*** On the other hand, in two dimensions the fundamental group of the configuration space of a system of $n$ identical particles is given by the more general braid group: $$\pi_1(C_n(\mathbb{R}^2)) \simeq B_n(\mathbb{R}^2) = \langle \sigma_i,  1 \leq i \leq n-1 | \sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1},$$ $$\sigma_i \sigma_j = \sigma_j \sigma_i \forall |i-j| \geq 2 \rangle .$$ The $\sigma_i$ are defined physically by interchanging the $i^{th}$ and $(i+1)^{st}$ particles counterclockwise. In contrast to the symmetric group, not all braid group generators satisfy $\sigma_i^2 = Id$. The monodromy operator/$R^2$ matrix is defined as the square of the braiding operator/R matrix.

Intuitively, two dimensional space allows for more possibilities because particles are topologically pointlike. Adding a particle to a 2D surface is like poking a hole in the surface, so loops around the hole can no longer be continuously deformed to a single point. (Note that our motivational Aharonov-Bohm effect example simulates 2D as the solenoid is infinite in length, so only 2 of the dimensions really matter. This corresponds to the fact that the loops around a line are characterized by the fundamental group (first homotopy group), $\pi_1(\mathbb{R}^2 \setminus line) = \pi_1(S^1 \times \mathbb{R}) = \mathbb{Z}$.)

***Truncated Braid Group*** The braid group as defined is infinite and torsion-free (all elements of the group have infinite order). For theories with a finite symmetry group, it is actually the truncated braid group $B(m,n)$, that governs the interaction of particles. These are the braid groups on $n$ elements with the additional condition that $\sigma^m=1$ for some finite $m$ ($m$ is taken to be minimal. $m=2$ corresponds to the case of $S_n$, so the truncated braid group is indeed a generalization of the symmetric groups.) When $\sigma$ acts on physical particles, the Hamiltonian transforms as a representation of $\sigma$ (the braid operator), which we call the $R$ matrix. (More on this topic will be discussed in the next section.)

***Distinguishable Particles: Colored (Pure) Braid Group*** If the particles are distinguishable, the configuration space is given by $C((\mathbb{R}^2)^n - D)$. The colored (pure) braid group $P(m,n)$, for $n$ even, describes the fundamental group of the configuration space of the underlying manifold. (Intuitively, only monodromy operators make sense since after each exchange the two particles have to be back in their original positions.) Formally, the pure braid group $P(m,n)$ is the kernel of the homomorphism $\phi: B_n \rightarrow S_n$ mapping each braid to the associated corresponding permutation.

***Partially Colored Braid Group*** If the system consists of a combination of distinguishable particles and indistinguishable particles, then the fundamental group is the partially colored braid group.
