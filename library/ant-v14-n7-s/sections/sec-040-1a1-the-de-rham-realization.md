---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-040-1a1-the-de-rham-realization
section_title: "1A1. The de Rham realization"
section_number: null
pages: 50-50
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
of Section 0A. The de Rham pro-unipotent fundamental groupoid πun,dR
1
(X), in the sense of [Deligne
1989], is a groupoid in pro-afﬁne schemes over X. Its base points are the points of X and the nonzero
tangent vectors at {0, µN, ∞} ⊂P1, called tangential base-points. The groupoid structure is deﬁned by
the morphisms πun,dR
1
(X K, z, y) × πun,dR
1
(X K, y, x) →πun,dR
1
(X K, z, x) for any base-points x, y, z. By
[loc. cit., Section 12.9], each πun,dR
1
(X, y, x) is canonically isomorphic to the spectrum of the shufﬂe
Hopf algebra OX,e0∪µN over the alphabet e0∪µN = {ex | x ∈{0}∪µN(K)}. This isomorphism is compatible
with the groupoid structure.
Following [Deligne and Goncharov 2005], for any N-th root of unity ξ ∈µN(K), we denote by
5ξ,0 = πun,dR
1
(X,⃗1ξ,⃗10). Let f 7→f (ξ) be the isomorphism 51,0 →5ξ,0 induced by the automorphism
x 7→ξx of X by functoriality of πun,dR
1
.
Let K⟨⟨e0∪µN ⟩⟩be the noncommutative K-algebra of formal power series over the noncommuting
variables ex, x ∈{0∪µN(K)}. We will write an element f ∈K⟨⟨e0∪µN ⟩⟩as f ((ex)x) = f ((ex)x∈{0}∪µN(K))
or f (e0, (eξ)ξ) = f (e0, (eξ)ξ). The coefﬁcient in f of a word w on the alphabet e0∪µN is denoted by
f [w]. This notation extends by linearity to linear combinations of words, and if for any n ≥0 wn is
a linear combination of words of weight n, we denote by f
P∞
n=0 wn

= P∞
n=0 f [wn] if this series
converges. We have a canonical inclusion Spec(OX,e0∪µN )(K) ⊂K⟨⟨e0∪µN ⟩⟩; namely, Spec(OX,e0∪µN )(K)
is the group of elements satisfying the shufﬂe equation: for all words w, w′, f [w] f [w′] = f [wXw′]
where X is the shufﬂe product of words on the alphabet e0∪µN .
