---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-019-43-the-cohomological-wall-crossing-isomorphism-t
section_title: "The cohomological wall crossing isomorphism — Theorem B"
section_number: 4.3
pages: 40-43
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
section we prove Theorem B, which is a categoriﬁcation of the motivic wall crossing
formula (8). In Section 6.4 we will prove that this isomorphism can be r ealised in
terms of multiplication in the cohomological Hall algebra. Even without considering
the CoHA we can still prove that there is some isomorphism (10). The mere
existence of this isomorphism is enough for many applications.
Fix a dimension vector d ∈ NQ0. Denote by HN d the set of Harder–Narasimhan
types for d, that is, sequences d1, . . . ,ds ∈ NQ0\{0} such that the slopes Ξζ (d1), . . . ,Ξζ (ds)
are strictly decreasing and ∑ s
i=1 di = d. Recall that by [37, Prop.3.4], the moduli
stack Md has a stratiﬁcation by locally closed substacks
(64) Md =
∐
d∈HNd
Mζ
d
where Mζ
d is the stack of representations which have Harder–Narasimhan ty pe d
with respect to the stability condition ζ.
This is a stratiﬁcation in the following weak sense. We deﬁne similarly to
[37, Def.3.6] a partial ordering ≤′ on HN d. First, given d = ( d1, . . . ,ds) ∈
HNd we deﬁne P (d) to be the convex hull in C of the origin and the points
(∑ k
l=1|dl|, Ξζ (dl)|dl|) for 1 ≤ l ≤ s. As in [37, Prop.3.7] it is easy to show that for
a representation ρ of Harder–Narasimhan type
d, the polytope P (d) is the convex
hull of 0 ,ζ · d andζ · dim(ρ′) for all representations ρ′ ⊂ρ with slope greater than
Ξζ (d). We write e ≤′ d if the polygon P (d) is contained in P (e). The condition
on a representation ρ to have a subrepresentation ρ′ ⊂ρ of ﬁxed dimension d′ is
closed, since the morphism Md′,d − d′ → Md is proper. It follows that
Mζ
d ⊂
⋃
e∈HNd
e≤′d
Mζ
e.
Each of the stacks Mζ
d can be written as a global quotient stack
Mζ
d
∼
= Xζ
d/Gd
where Xζ
d ⊂ Xd is the subspace of representations preserving the ﬂag deﬁned by d,
such that each of the associated dr-dimensional subquotients is ζ-semistable, and
Gd ⊂ Gd is the subgroup preserving the same ﬂag. Each of these stacks co mes
with a map pd : Mζ
d → M d sending a representation to its semisimpliﬁcation, and
an inclusion id : Mζ
d → Md given by forgetting the Harder-Narasimhan ﬁltration.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 41
The diagram
Mζ
d
pd
/d15/d15
id /d47/d47 Md
pd
/d125/d125④④④④④④④④④
Md
commutes. In the following theorem, the map qζ
µ is as deﬁned in (46).
Theorem 4.12. Let ζ be a Bridgeland stability condition on Q, not necessarily
generic. Then there are isomorphisms
(65) H
(
p!φ mon
Tr(W )IC M(Q)
)
∼
= ⊠
tw
⊕,−∞
µ
− →∞ H
(
qζ
µ ,!pζ
µ ,!φ mon
Tr(W )ζ
µ
IC Mζ -ss
µ
(Q)
)
and
(66) H
(
p∗φ mon
Tr(W )IC M(Q)
)
∼
= ⊠
tw
⊕,∞
µ
− →−∞ H
(
qζ
µ ,∗pζ
µ ,∗φ mon
Tr(W )ζ
µ
IC Mζ -ss
µ
(Q)
)
.
Assume in addition that ζ is generic. Then there are isomorphisms
(67) H
(
p!φ mon
Tr(W )IC M(Q)
)
∼
= ⊠
tw
⊕,−∞
µ
− →∞ Sym⊠⊕
(
qζ
µ ,!BPSζ
W,µ ⊗ H(BC*)∨
vir
)
and
(68) H
(
p∗φ mon
Tr(W )IC M(Q)
)
∼
= ⊠
tw
⊕,∞
µ
− →−∞ Sym⊠⊕
(
qζ
µ ,∗BPSζ
W,µ ⊗ H(BC*)vir
)
.
Proof. As in the proof of Theorem 4.10 we only need to prove the case for wh ich
W = 0 and then we can deduce the general case from the fact that mo nodromic
vanishing cycle functors are exact, and commute with proper maps and the relevant
monoidal structures. We ﬁrst prove that the isomorphism (65) ex ists. Fix a d ∈
NQ0 . Then if we complete ≥′ to a total ordering ≥ of HN d and deﬁne, for each
d ∈ HNd,
Mζ
≤
d :=
⋃
e≤d
Mζ
e
Mζ
<
d :=
⋃
e<d
Mζ
e
then Mζ
≤
d ⊂ Md is a closed embedding, and Mζ
d ⊂ Mζ
≤
d is an open embedding
with complement Mζ
<
d ⊂ Mζ
≤
d. We denote by
id : Mζ
d֒→Md(69)
i<d : Mζ
<
d֒→Md(70)
i≤d : Mζ
≤
d֒→Md(71)
the natural inclusions. We will show that all of the terms in the followin g distin-
guished triangle are pure, and that the connecting maps are zero, and furthermore
that the triangle is split:
(72) H
(
pd,!i
d,!QMζ
d
)
→ H
(
pd,!i≤d,!QMζ
≤
d
)
→ H
(
pd,!i<d,!QMζ
<
d
)
→ .
42 BEN DA VISON AND SVEN MEINHARDT
Fix
d ∈ HNd. Consider the following commutative diagram
Mζ
d
qd
/d15/d15
id /d47/d47 Md
pd
/d15/d15
Xζ
d/(Gd1 × . . . × Gds)
q2, d /d47/d47
q1, d
/d53/d53❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
Mζ -ss
d1 × . . . × Mζ -ss
ds
pζ
d1 ×...×pζ
ds
/d15/d15
Mζ -ss
d1 × . . . × Mζ -ss
ds
qζ
d1 ×...×qζ
ds
/d15/d15
Md1 × . . . × Mds
⊕ /d47/d47 Md
where q1,d is an aﬃne ﬁbration of relative dimension
f1(d) :=
∑
1≤r<r ′≤s
dr · dr′
and q2,d is an aﬃne ﬁbration of relative dimension
f2(d) :=
∑
1≤r<r ′≤s
∑
a∈Q1
dr′
s(a) dr
t(a) .
We deﬁne
(73) (
d, d) := f1(d) − f2(d).
For f ∈ NQ0 we deﬁne f · d =∑
r≤s f · dr. Fix n, and let f ≫ 0. Then since there
are isomorphisms
Hn
(
pd,!i
d,!QMd
)
∼
= Hn
(
⊕!(qζ
d1 × . . . × qζ
ds)!(pζ
d1 × . . . × pζ
ds)!L−(
d,d)
Mζ -ss
d1 ×...×Mζ -ss
ds
)
∼
= Hn
(
⊕!(qζ
d1 × . . . × qζ
ds)!(πζ
f ,d1 × . . . ×πζ
f ,ds)!L−(
d,d)−f ·d
Mζ
f , d1 ×...×Mζ
f , ds
)
the complex Hn
(
pd,!i
d,!QMd
)
is pure, by properness of qζ
dr , πζ
f ,dr and ⊕. The
claim regarding the distinguished triangles (72) then follows by induct ion, and
semisimplicity of the category of pure mixed Hodge modules. Taking ca re of the
twists, we calculate
H (p!IC M(Q)) = H
(
p!L(d,d)/2
M
)(74)
∼
=
⨁
d∈HN
H
(
pd,!id,!L(d,d)/2
Md
)
∼
=
⨁
(d1,...,ds)∈HN
qζ
d1,! H
(
pζ
d1,!QMζ -ss
d1
)
⊠⊕ . . . ⊠⊕ qζ
ds,! H
(
pζ
ds,!QMζ -ss
ds
)
⊗ L−(
d,d)+(d,d)/2
∼
=
⨁
(d1,...,ds)∈HN
qζ
ds,! H
(
pζ
ds,!IC Mζ -ss
ds
(Q)
)
⊠tw
⊕ . . . ⊠tw
⊕ qζ
d1,! H
(
pζ
d1,!IC Mζ -ss
d1
(Q)
)
∼
=⊠
tw
⊕,−∞
µ
− →∞qζ
µ ,! H
(
pζ
µ ,!IC Mζ -ss
µ
(Q)
)
.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 43
This completes the proof of the ﬁrst part of the theorem: since pζ
µ is approximated
by proper maps, and qζ
µ is proper, there are isomorphisms
qζ
µ ,! H(pζ
µ ,!IC Mζ -ss
µ
(Q)) ∼
= H(qζ
µ ,!pζ
µ ,!IC Mζ -ss
µ
(Q))
as required.
Since qζ
µ : Mζ -ss
µ → Mµ is a morphism of monoids, qζ
µ ,! is a symmetric monoidal
functor. If ζ is generic, we may then apply Theorem 4.10 at each slope µ ∈
(−∞, ∞), to deduce (67). Finally we prove that there are isomorphisms (66 ) and
(68). Note that it is enough to construct the restrictions of thes e isomorphisms
to each space Md. Restricting to this component, there are ﬁnitely many ten-
sor products of sheaves on the left hand side and the right hand sid e of (66) and
(68), involving H(pd′,∗IC Md′ (Q)) and H(pζ
d′,∗IC Mζ -ss
d′
(Q)) for d′ ∈ Λζ
µ satisfying
d′ ≤ d. Then the isomorphisms are given by taking the Verdier duals of (65) and
(67) respectively, by Remarks 2.15 and 3.9. □
Arguing as in the proof of Theorem 4.10, using properness of qζ and approxima-
tion of pζ
µ by proper maps for the relevant base change isomorphisms, we ded uce
the corollary
Corollary 4.13. Letζ be a Bridgeland stability condition for Q, not necessarily
assumed to be generic. Then there is an isomorphism of NQ0 -graded monodromic
mixed Hodge structures
Hc(MS , ICW )∨ ∼
= ⊠
tw
+,∞
µ
− →−∞ Hc
(
Mζ -ss,S
µ , ICζ
W,µ
) ∨
ifζ is generic, we may combine this isomorphism with the absolut e integrality iso-
morphisms for each slope µ (Theorem A) to obtain the isomorphism
Hc(MS , ICW )∨ ∼
= ⊠
tw
+,∞
µ
− →−∞ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
µ
)
.
Remark 4.14. In the case W = 0, and S = CQ−mod we obtain the isomorphism
(75) H ( M, IC M(Q)) ∼
= ⊠
tw
+,∞
µ
− →−∞ H
(
Mζ -ss
µ , IC Mζ -ss
µ
(Q)
)
.
The existence of such an isomorphism is proved by Franzen and Reineke in [17] via a
vanishing result for even cohomology, and before that for th e case of a Dynkin quiver
which is not an orientation of E8 by Rimanyi in [38], where this result is a corollary
of the existence of a Poincar´ e–Birkhoﬀ–Witt isomorphism f or hypercohomology.
