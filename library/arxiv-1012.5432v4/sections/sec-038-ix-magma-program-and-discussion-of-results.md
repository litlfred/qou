---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-038-ix-magma-program-and-discussion-of-results
section_title: "IX MAGMA Program and Discussion of Results"
section_number: null
pages: 32-33
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
The tables computed in this paper were produced using the MAGMA program included in Appendix 1. The MAGMA program computes the particles (and their properties - e.g. spin), braiding, and fusion rules for an arbitrary finite residual gauge group. The program can also explicitly compute the entries of the S matrix. As part of the fusionprinter(Group) procedure, the MAGMA program computes the change of basis S matrix and implements the Verlinde formula to determine the fusion coefficients based on the S matrix for an arbitrary group.

In addition, the MAGMA program can compute the probabilities of obtaining any given fusion product used in many different topological quantum computation schemes. More detail on this connection is provided in the next section.

The two examples included here were chosen mainly due to their possible applications to universal quantum computation (as described in the next section). In particular, since $S_3$ is the smallest non-abelian group, a method for achieving universal quantum computation in that case has the best chance of being engineered in the lab or found in nature.

In Appendix B, the quantum doubles for the remaining finite subgroups of $SO(3)$ are tabulated and analyzed. Each of these are interesting from either a physics theory or implementation point of view. For example, from the physics theory perspective, in the two theories $S_3$ and $A_5$ discussed above, every particle is its own antiparticle. However, this is not always the case and $A_4$ illustrates this point. Furthermore, other dihedral groups, for example, could be interesting from the implementation perspective as they arise naturally from spontaneous symmetry breaking in p-wave superconductors.
