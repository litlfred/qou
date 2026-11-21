---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-003-22-historical-overview
section_title: "Historical Overview"
section_number: 2.2
pages: 4-6
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.975
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
[]{#historical label="historical"}

The octonions first appeared in relation to quantum theory in the classification of Jordan algebras by Jordan et. al. [@jordan1993algebraic]. In this context, the Jordan algebras represent algebras of observables, because unlike the usual matrix product, the commutative but non-associative Jordan product of two Hermitian operators is again Hermitian. In particular, the classification of Jordan algebras identified the single exceptional Jordan algebra $J_3(\mathbb{O})$, consisting of $3\times 3$-matrices with (off-diagonal) entries in $\mathbb{O}$.

Not long after the discovery of quarks, Güynadin and Gürsey combined these earlier ideas and utilized $\mathbb{O}$ to describe the ${\rm{SU}}(3)$ color symmetry of quarks [@gunaydin1973quark]. Such an octonion-based description of quarks is motivated by the observation that ${\rm{SU}}(3)$ corresponds to a subgroup of the octonion automorphism group $G_2$ that leaves invariant one of the octonion imaginary unit vectors.

This early work relating $\mathbb{O}$ to quarks was extended upon by Dixon who demonstrated that the division algebras $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ provide the algebraic underpinnings of modern particle theory. Specifically, many of the mathematical features of the standard model, including its gauge symmetries to which a single generation of fermions and leptons are subject, together with the correct multiplets into which they fall, are inherent in the 64 real dimensional composition algebra $\mathbb{T}=\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$, [@dixon1990derivation; @dixon19991; @dixon1999algebraic; @dixon2004division; @dixon2010division; @dixon2013division].

Conventionally, spinors are considered as column vectors with entries in $\mathbb{R}$ or $\mathbb{C}$. An example being Dirac spinors corresponding to wave functions in $4\times 1$-column vectors over $\mathbb{C}$, acted upon by the Dirac algebra (a complex Clifford algebra). Dixon's underlying idea is to generalize this notion and consider tensor products of division algebras (for example $\mathbb{T}$ defined above) themselves as spinors.

Such spinors are acted upon from the left or right by the algebra itself, with each possible action corresponding to a linear map. The composition of all such adjoint actions generate the *associative multiplication algebra*, a Clifford algebra, which acts on the spinor space (corresponding to a tensor product of division algebras).

In such a construction therefore, the spinor space itself exhibits algebraic structure. It is this nontrivial algebraic structure of the spinor components that provides the algebraic source of the internal symmetries needed to replicate the structure of the standard model. In particular, since $\mathbb{T}$ itself is not a division algebra, it admits a nontrivial decomposition of its identity into mutually orthogonal primitive idempotents, corresponding to projectors. These projectors simultaneously decompose the spinor space into mutually orthogonal subspaces, as well as the associative multiplication algebra into subalgebras whose actions preserve these subspaces.

For the case of the spinor $\mathbb{T}$, the identity can be resolved into four orthogonal projectors, each composed of other projectors associated with ${\rm{SU}}(2)$ isospin and ${\rm{SU}}(3)$ color. The spinor $\mathbb{T}$ is then found to transform with respect to these Lie groups as ${\rm{SU}}(2)$ doublets and ${\rm{SU}}(3)$ singlets and triplets. Additionally, the quantum numbers associated with hypercharge, isospin and color can be mathematically assigned to the invariant subspaces of $\mathbb{T}$. That is, the gauge symmetries and multiplets of spinors encountered in the standard model are both part of the same mathematical structure arising from the spinor $\mathbb{T}$, which then transforms as ${\rm{U}}(1)\times {\rm{SU}}(2)\times {\rm{SU}}(3)$, with each invariant subspace corresponding to a Pauli spinor. Dirac spinors can subsequently be produced by doubling the spinor space to $\mathbb{T}^2$, that is $2\times 1$-column vectors over $\mathbb{T}$.

In the models of Güynadin and Gürsey [@gunaydin1973quark] and Dixon [@dixon2013division], the bosons live in the associative multiplication algebra, whereas the fermions reside in the spinors on which this algebra acts. Furey instead describes both bosons and fermions within the associative multiplication algebra by considering the minimal left ideals of the algebra as the spinors [@furey2016standard; @furey2018demonstration; @furey231; @furey232; @furey233]. The representation of spinors as minimal ideals of Clifford algebras dates back to the 1930s [@juvet1930operateurs; @sauter1930losung] and 1940s [@riesz2013clifford]. The fermions in such a construction then correspond to the basis states of the minimal left ideals of the associative multiplication algebra, constructed via a standard procedure based on a Witt decomposition proposed by Ablamowicz [@ablamowicz1995construction], and the gauge symmetries are then the unitary symmetries that preserve these ideals.

Since the predominant focus of the present paper is connecting causal fermion systems to the octonions, in what follows we shall disregard the factor of $\mathbb{H}$ in $\mathbb{T}$. Instead, we restrict attention to the $\mathbb{C}\otimes\mathbb{O}$-component of the algebra $\mathbb{T}$.
