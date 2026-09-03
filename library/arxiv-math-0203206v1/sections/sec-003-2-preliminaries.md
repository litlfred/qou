---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-003-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-4
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
2.1 Tensor Categories
For the deﬁnitions of categories, functors and natural transfo rmations we refer, e.g., to [24]. In this subsection
we brieﬂy recall some of the less standard notions of category the ory which will be needed here, others will be
introduced as we proceed. We may occasionally say ‘arrows’ instead of ‘morphisms’ in order to avoid confusion
with algebra homomorphisms. All categories which we consider are es sentially small, i.e. equivalent to a small
3
category. We mostly speak of ‘tensor categories’ rather than ‘monoidal categories’ but cannot avoid the adjective
‘monoidal’. In view of the coherence theorems for (braided, symmet ric) tensor categories we may assume all
tensor categories to be strict, satisfying X ⊗ (Y ⊗Z) = (X ⊗Y )⊗Z for all X,Y,Z . Following widespread use, we
also consider the tensor categories of vector spaces as strict, a ppealing to the canonical isomorphisms to identify
X ⊗ (Y ⊗Z) with (X ⊗Y ) ⊗Z. We often write XY in the place of X ⊗Y . By H we mean the strictiﬁcation
of Hilb. (We also suppress all other canonical isomorphisms in Hilb, iden tifying B(H ⊗K) = B(H) ⊗B(K).)
Note, however, that one cannot assume all tensor functors to b e strict without losing generality. Thus we need
the following.
Definition 2.1 Let C, D be (strict) tensor categories. A functor F : C → D is weakly monoidal if there exist
morphisms dX,Y :F (X) ⊗F (Y ) →F (X ⊗Y ) for all X,Y ∈ C and a morphism e : 1D →F (1C) such that
1. The morphisms dX,Y are natural w.r.t. both arguments.
