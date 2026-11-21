---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-048-66-vanishing-of-integrals
section_title: "Vanishing of integrals"
section_number: 6.6
pages: 28-29
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
In this subsection we consider the space Cn of G(2)-equivalence classes of conﬁgurations of points on
the Euclidean plane. Every two indices i, j, i̸ = j, 1 ≤i, j ≤n give a forgetting map Cn−→C2 ≃S1. We
denote by dφi,j the closed 1-form on Cn which is the pullback of the standard 1-form d(angle) on the circle.
We use the same notation for the pullback of this form to Confn.
28
Lemma. Let n ≥3 be an integer. The integral over Cn of the product of any 2n −3 = dim(Cn) closed
1-forms dφiα,jα, α = 1, . . . , 2n −3, is equal to zero.
Proof: First of all, we identify Cn with the subset C′
n of Confn consisting of conﬁgurations such that
the point pi1 is 0 ∈C and pj1 is on the unit circle S1 ⊂C. Also, we rewrite the form which we integrate as
2n−3
^
α=1
dφiα,jα = dφi1,j1 ∧
2n−3
^
α=2
d(φiα,jα −φi1,j1) .
Let us map the space C′
n onto the space C′′
n ⊂Confn consisting of conﬁgurations with pi1 = 0 and
pj1 = 1, applying rotations with the center at 0. Diﬀerential forms d(φiα,jα −φi1,j1) on C′
n are pullbacks of
diﬀerential forms dφiα,jα on C′′
n. The integral of a product of 2n−3 closed 1-forms dφiα,jα, α = 1, . . . , 2n−3
over C′
n is equal to ±2π times the integral of the product 2n −4 closed 1-forms dφiα,jα, α = 2, . . . , 2n −3
over C′′
n.
The space C′′
n is a complex manifold. We are calculating the absolutely converging integral of the type
Z
C′′
n
Y
α
dArg(Zα)
where Zα are holomorphic invertible functions on C′′
n (diﬀerences between complex coordinates of points of
the conﬁguration). We claim that it is zero, because of the general result proven in 6.6.1.
