---
doc_id: arxiv-1012.5432v4
doc_title: "quant-ph Towards Topological Quantum Computation? -"
section_id: sec-006-2-antiparticles
section_title: "Antiparticles"
section_number: 2
pages: 21-23
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.608
latex_coverage_ratio: 0.987
---
An antiparticle is defined to be the representation which when fused with the original particle yields the identity as one possible outcome. It turns out that the antiparticle is unique, and the charge conjugation operator $C=S^2$ takes a particle to its antiparticle. Note that since the S matrix commutes with the T matrix (which encodes the spin), the spin of a particle is the same as that of the corresponding antiparticle.

## Alice Physics and Cheshire Charges in Non-Abelian Gauge Theories

Cheshire charge is a non-localizable form of charge that is carried by a configuration of particles. Globally, charge must be conserved. Thus, a special type of entanglement is observed if the particles with Cheshire charge are kept far apart from one another so that charge cannot be transferred by local interactions. This entanglement opens up the possibility of topological quantum computation using anyons. In particular, consider a collection of particle/antiparticle pairs. Each local particle/antiparticle pair has trivial total flux and charge - If kept sufficiently separated, the environment cannot distinguish between states with long range quantum numbers the same as those given by the ground state. However, the configuration still has nontrivial Cheshire charge, so the state cannot annihilate. In other words, since the environment acts locally on the system, it cannot effect the non-local Cheshire charge carried by the configuration. Thus the system is protected against decoherence.

# Summary

The topology of the configuration space restricts the possible symmetry groups of the Hamiltonian. In turn, every term in the Hamiltonian must transform as a singlet under all the representations of the symmetry group so this restricts the types of terms that can appear in the Hamiltonian. In (2+1)-dimensional systems, the truncated braid group must be used instead of the symmetric group. Consistent braiding and fusion then impose conditions which must be solved by any particles in the theory. Particles have two degrees of freedom given by the magnetic flux and electric charge. In (2+1)-dimensional theories based on a finite symmetry group, representations of the quantum double of the symmetry group determine the kinds of particles that can possibly exist in the given theory. The fusion rules are then encoded by the comultiplication of the dual.

# Explicit Derivations of Particles and Fusion Rules for Special Physical Theories {#exs}

## Abelian vs. Non-Abelian: Physical Origin and Computational Potential

In Abelian groups, the fusion rules obtained by the quantum double formalism are deterministic as only one product can result from fusion of two particles. However, in non-Abelian Groups, the fusion rules obtained for at least two input particles include multiple possible output particles so the product is not determined solely by the symmetry group. (Letting $N^C_{AB}$ be the number of ways of obtaining particle $C$ when the particles $A$ and $B$ are fused, mathematically this condition is just $\sum_C N^C_{AB} > 1$ for some particles $A,B$.) To obtain a deterministic result, the more detailed dynamics of the specific interaction have to be taken into account.

From another perspective, non-Abelian groups lead to multidimensional Hilbert Spaces so there is more wiggle room for changes in the state (i.e. the operators can be noncommutative in a multidimensional space). This is the key behind the computational power of non-Abelian groups in quantum computation.

Abelian groups are severely limited in their applications to quantum computation by the fact that they can only be used to store information (not to process it). However, Abelian groups nonetheless underlie some physical systems and are used in Kitaev's Toric Code for storage [@kitaevToric] and are included here for completeness. Specifically, superconductivity in a material corresponds to SSB of the electromagnetic $U(1)$ gauge field - the standard condensed matter Cooper Pair, for example, arises from the SSB of the electromagnetic $U(1)$ to $\mathbb{Z}/N\mathbb{Z}$ with $N=2$.

## Applying the Quantum Double Formalism to Abelian Finite Groups $\mathbb{Z}/N\mathbb{Z}$

Finite abelian groups are the simplest case that has been worked out - computer algebra is not required. [@prop] Here we include the results for completeness and so we can analyze the tables for Majorana particles.

Consider the effect of spontaneous symmetry breaking of an Abelian $U(1)$ gauge group (or the nonabelian $SO(3)$, $SU(2)$, or $SU(3)$ gauge groups) down to the finite abelian subgroup $\mathbb{Z}/N\mathbb{Z}$. Screening precludes electromagnetic effects between two particles from influencing the long-distance interactions. However, the topological charges persist. For these Abelian theories, the monodromy operator is just a phase.
