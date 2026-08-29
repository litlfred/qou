---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-044-82-invariants-of-3-manifolds
section_title: "Invariants of 3-manifolds"
section_number: 8.2
pages: 50-52
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
There are two classes of invariants of 3-manifolds associat ed with a modular tensor cate-
gory C, cf. [53]. On the one hand we have the surgery invariants RT (M, C) of Reshetikhin
and Turaev [50] which are based on the fact that every connect ed oriented closed 3-
manifold can be obtained from S3 by surgery along a framed link. It turned out [8] that
modularity of the category C is not really necessary, since it suﬃces that C be ‘modu-
larizable’. Yet, the invariant of the manifold being deﬁned in terms of a link invariant,
the existence of a (non-symmetric) braiding is essential. O n the other hand there are the
state sum invariants based on a triangulation of the manifol d. Generalizing on [54], an
invariant T V (M, C) associated with any modular category C was deﬁned in [53]. Later it
was understood that in fact no braiding is necessary for the c onstruction of a triangula-
tion invariant, cf. [5, 16], provided C has two-sided duals. (This had been anticipated in
[44], which was never published.) We denote the correspondi ng invariant by T r(M, C).
Gelfand and Kazhdan formulated a conjecture [16, Conjectur e 1] pointing towards a link
between the two invariants being provided by the quantum dou ble. Our results on the
quantum double of semisimple tensor categories allow us to p rove this conjecture.
50
Proposition 8.3 Let C satisfy the assumptions of Theorem 1.2 and consider the state -
sum TQFT associated with C, as deﬁned in [16]. Then the dimension of the vector space
HS1×S1 associated to the two dimensional torus equals the number #Z1(C) of isomorphism
classes of simple objects of Z1(C).
Sketch of Proof. By the considerations of Subsection 5.1, # Z1(C) coincides with the
dimension of the center of the tube algebra Ξ L. But this center is isomorphic to HS1×S1,
as discovered by Ocneanu [45] and explained in more detail in [15, Theorem 3.1]. ■
Remark 8.4 The above argument is only a sketch because the triangulatio n TQFT in
2+1 dimensions considered in [45, 15] is derived from a subfa ctor, see [27] for a detailed
exposition. Here as in [38, Section 7] we use the fact that the latter is equivalent to the
invariant deﬁned in [5, 16]. This is more or less clear, but ce rtainly deserves being made
precise, as we plan to do in [39]. Note also that in order for a s pherical category to give
rise to a triangulation TQFT – as opposed to just the invarian t – one must assume that it
does not contain symplectic self-dual simple objects. This is done in [53] and [6, p. 4018],
but unfortunately ignored in the bulk of the literature on th e subject. ✷
By Theorem 1.2, Z1(C) is modular, thus gives rise to a surgery TQFT in 2+1 dimen-
sions, cf. [53]. For these TQFTs it is known (by construction ) that the dimension of the
vector space HS1×S1 associated with the torus equals the number of isomorphism c lasses
of simple objects in the category. Thus the above result prov ides support for the conjec-
ture that the triangulation and surgery TQFTs associated wi th C and Z1(C), respectively,
are isomorphic. (This conjecture, while very natural, seem s to have appeared in print
only in [26, Question 5].) In particular, the corresponding invariants of closed oriented
3-manifolds should coincide:
RT (M, Z1(C)) = T r(M, C) ∀M. (8.4)
Presently, we have no proof for this, but we note that Sato and Wakui recently announced
a proof in the setting of unitary categories arising from a su bfactor. If C is modular, the
braided equivalence Z1(C)
⊗
≃br C ⊠ ˜C proven in Section 7 implies
RT (M, Z1(C)) = RT (M, C ⊠ ˜C) = RT (M, C) · RT (M, ˜C) = RT (M, C) · RT (−M, C),
and (8.4) follows from [53, Theorem VII.4.1.1], according t o which T V (M, C) = RT (M, C)·
RT (−M, C). For non-modular C we only have the following weaker result:
Proposition 8.5 Let C be as in Theorem 1.2 and M an oriented closed 3-manifold. Then
RT (M, D(C)) · RT (−M, Z1(C)) = T r(M, C) · T r(−M, C).
If C is unitary then |RT (M, Z1(C))| = |T r(M, C)|.
51
Proof. We compute
RT (M, Z1(C)) · RT (−M, Z1(C)) = T V (M, Z1(C))
= T r(M, Z1(C))
= T r(M, C ⊠ Cop)
= T r(M, C) · T r(M, Cop)
= T r(M, C) · T r(−M, C).
Here the ﬁrst equality is due to Turaev’s theorem, which appl ies since Z1(C) is modular.
The second is the equality [6] of T V and T r for spherical C. The third equality follows
from the weak monoidal Morita equivalence Z1(C) ≈ C ⊠ Cop together with the Morita
invariance of the invariant T r, cf. [38, Theorem 7.1]. The last two equalities follow from
general properties of the invariant T r [6].
If C is unitary we have RT (−M, Z1(C)) = RT (M, Z1(C)) and T r(−M, C) = T r(M, C),
and we are done. ■
