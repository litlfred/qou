---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-014-34-equivariant-matrix-factorizations
section_title: "Equivariant matrix factorizations"
section_number: 3.4
pages: 15-16
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
proof the lemma 2.1 relies on the fact that every map from Hom<0(C+, C+) is homotopically trivial and
hence we can construct a homotopy that connects this map to 0. It appears to us that the analog of this
statement does not hold in the equivariant setting: the homotopy connecting the map to 0 in general is
equivariant up to homotopy.
Thus to make our proof of lemma 2.1 work in equivariant setting one would have to enlarge our category
of equivariant complexes to the category of L∞-complexes. That would make our theory extremely technical
and we postpone this development for subsequent publications. Below we explain more elementary way to
get around this problem: we incorporate Eilenberg-Chevalley complex in our deﬁnition of equivariant matrix
factorizations. We give details below and we start with some preliminary material.
Let us deﬁne by ∆the standard map h →h ⊗h deﬁned by x 7→x ⊗1 + 1 ⊗x. Suppose V and W
are modules over Lie algebra h then we use notation V ⊗
∆
W for h-module which is isomorphic to V ⊗W
as vector space, the h-module structure being deﬁned by ∆. Respectively, for a given h-equivariant matrix
factorization F = (M, D) we denote by CEh⊗
∆
F the h-equivariant matrix factorization (CEh⊗
∆
F, D + dce).
The h-equivariant structure on CEh⊗
∆
F originates from the left action of U(h) that commutes with right
action on U(h) used in the construction of CEh.
In more details, for a given h-module M the complex CEh⊗
∆
M has terms U(h)⊗Λi(h)⊗M with h-module
structure
x · (u ⊗ω ⊗m) = x · u ⊗ω ⊗m,
and the diﬀerential of the complex is dce = d1 + d2 where:
d1(u ⊗x1 ∧· · · ∧xp ⊗m) =
p
X
i=1
(−1)i+1 (uxi ⊗mx1 ∧· · · ∧ˆxi ∧· · · ∧xp ⊗m+
x1 ∧· · · ∧ˆxi ∧· · · ∧xp ⊗xi · m) ,
d2(u ⊗x1 ∧· · · ∧xp) =
X
i<j
(−1)i+ju ⊗[xi, xj] ∧x1 ∧· · · ∧ˆxi ∧· · · ∧ˆxj ∧· · · ∧xp.
A slight modiﬁcation of the standard fact that CEh is the resolution of the trivial module implies that
CEh⊗
∆
M is a free resolution of the h-module M.
3.4. Equivariant matrix factorizations. We keep previous notations: Z is an aﬃne variety with H-action
and F ∈C[Z]h. Deﬁne a category Modh whose objects are ﬁnite-dimensional H-representations V . Now
deﬁne the category MFh(Z, F) whose objects are triples (M, D, ∂) where M = M 0⊕M 1 and M i = C[Z]⊗V i,
V i ∈ModH, ∂∈⊕i>j HomC[Z](Λih ⊗M, Λjh ⊗M) and D is an odd endomorphism D ∈HomC[Z](M, M)
such that
D2 = F,
Dtot
2 = F,
Dtot = D + dce + ∂,
where the total diﬀerential Dtot is an endomorphism of CEh⊗
∆
M, that commutes with the U(h)-action.
Note that we do not impose the equivariance condition on the diﬀerential D in our deﬁnition of matrix
factorizations.
On the other hand, if F = (M, D) ∈MF(Z, F) is a matrix factorization with D that
commutes with h-action on M then (M, D, 0) ∈MFh(Z, F).
There is a natural forgetful functor MFh(Z, F) →MF(Z, F) that forgets about the correction diﬀerentials:
F = (M, D, ∂) 7→F♯:= (M, D).
15
Given two h-equivariant matrix factorizations F = (M, D, ∂), ˜F = ( ˜
M, ˜D, ˜∂) the space of morphisms
Hom(F, ˜F) consists of homotopy equivalence classes of elements Ψ ∈HomC[Z](CEh⊗
∆
M, CEh⊗
∆˜
M) such that
Ψ ◦Dtot = ˜Dtot ◦Ψ and Ψ commutes with U(h)-action on CEh⊗
∆
M. Two map Ψ, Ψ′ ∈Hom(F, ˜F) are
homotopy equivalent if there is h ∈HomC[Z](CEh⊗
∆
M, CEh⊗
∆˜
M) such that Ψ −Ψ′ = ˜Dtot ◦h + h ◦Dtot and
h commutes with U(h)-action on CEh⊗
∆
M.
Given two h-equivariant matrix factorizations F = (M, D, ∂) ∈MFh(Z, F) and ˜F = ( ˜
M, ˜D, ˜∂) ∈
MFh(Z, ˜F) F ⊗˜F ∈MFh(Z, F + ˜F) as the equivariant matrix factorization (M ⊗˜
M, D + ˜D, ∂+ ˜∂).
