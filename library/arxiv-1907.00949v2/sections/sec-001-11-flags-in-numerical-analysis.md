---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-001-11-flags-in-numerical-analysis
section_title: "Flags in numerical analysis"
section_number: 1.1
pages: 2-3
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
multigrid, spectral and pseudospectral methods, wavelets, iterative matrix computations, etc, in
several ways.
Example 1.1 (Reﬁning mesh). In multigrid, algebraic multigrid, ﬁnite element methods, we often
consider a sequence of increasingly ﬁner grids or meshes G1⊆ G2⊆ G3⊆··· on the domain of
interest Ω. The vector space of real-valued functions
Vk :={f :Gk→ R}
gives us a ﬂag V1⊆ V2⊆ V3⊆··· of ﬁnite-dimensional vector spaces where dim Vk = #Gk.
The aforementioned numerical methods are essentially diﬀerent ways of extracting approximate
solutions of increasing accuracy from the ﬂag.
Example 1.2 (Increasing order). In spectral and pseudospectral methods, we consider a class of
functions of increasing complexity determined by an order d, e.g., polynomial or trigonometric
polynomial functions of degree d, on the domain of interest Ω. The vector space
Vd :={f : Ω→ R : deg(f)≤d}
gives us a ﬂag V1⊆ V2⊆ V3⊆··· as d is increased. Again, these methods operate by extracting
approximate solutions of increasing accuracy from the ﬂag.
Example 1.3 (Cyclic subspaces). GivenA∈ Rn×n and b∈ Rn, the subspace
Kk(A,b ) := span{b,Ab,...,A k−1b}
is called the kth Krylov subspace. The gist behind Krylov subspace methods in numerical linear
algebra, whether for computing solutions to linear systems, least squares problems, eigenvalue prob-
lems, matrix functions, etc, are all based on ﬁnding a sequence of increasingly better approximations
from the ﬂag K0(A,b )⊆K1(A,b )⊆···⊆ Kk(A,b ).
Example 1.4 (Multiresolution). A standard way to construct wavelets is to deﬁne amultiresolution
analysis, i.e., a sequence of subspaces Vk+1⊆ Vk deﬁned by
f(t)∈ Vk ⇔ f(t/2)∈ Vk+1.
The convention in wavelet literature has the indexing in reverse order but this is a minor matter
— a nested of sequence of subspaces is a ﬂag regardless of how the subspaces in the sequence are
labeled. So a multiresolution analysis is also a ﬂag.
This is not an exhaustive list, ﬂags also arise in numerical analysis in other ways, e.g., analysis
of eigenvalue methods [4, 21].
OPTIMIZATION ON FLAG MANIFOLDS 3
