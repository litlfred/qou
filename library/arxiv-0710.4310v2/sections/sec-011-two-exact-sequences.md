---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-011-two-exact-sequences
section_title: "Two exact sequences"
section_number: null
pages: 16-17
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
This subsection is not necessary to understand the rest of the ar ticle.
Deﬁnition 22 Let M be a smooth manifold. Let ∗ ∈ M . The group π2
2(M, ∗)
is given by all 2-paths Γ ∈S2(M ) such that Γ(∂([0, 1]2)) = {∗}, up to the equiva-
lence relation given by Γ ∼= Γ ′ if there exists a rank-2 homotopy J : [0, 1]2 × [0, 1] →M ,
connecting Γ and Γ ′, such that, in addition, J
(
(∂([0, 1]2) ×I
)
= {∗}. The group
law is taken to be the horizontal composition.
For more details see [MP].
Theorem 23 Let M be a smooth manifold with a base point ∗. The crossed
module Π 2,1
2 (M, ∗) can be embedded into the exact sequence:
{0} → π2
2(M, ∗)
i
− →π2,1
2 (M, ∗)
∂
− →π1
1(M, ∗)
p
− →π1(M, ∗) → {1}.
Proof. The only non-trivial part is the proof that the natural map i :π2
2(M, ∗) →
π2,1
2 (M, ∗) is injective. This follows from Lemma 52.
Deﬁnition 24 The thin k-invariant of M is deﬁned as being the cohomol-
ogy class kt(M, ∗) ∈ H 3(
π1(M, ∗),π 2
2(M, ∗)
)
determined by the exact sequence
above. See [EML, Br] for the construction of these group coho mology classes.
We can deﬁne a 2-category Q2(M ), with objects given by the points of M and
morphisms given by the arrows of the groupoid S1(M ). The set of 2-morphisms
Q2(M ) of Q2(M ) is given by the set of 2-paths of M up to homotopy. Here
the notion of homotopic 2-paths is deﬁned in the same way as the not ion of
rank-2 homotopic 2-paths (Deﬁnition 19), but omitting the ﬁnal co ndition on
the rank of the derivative of the map deﬁning the homotopy; see th e remarks
after deﬁnition 36. If Γ and Γ ′ are 2-paths, we write Γ ∼=∞ Γ ′ to denote that
they are homotopic. Applying the construction that deﬁned the cr ossed module
Π 2,1
2 (M, ∗) to Q2(M, ∗) yields a crossed module
Π ∞,1
2 (M, ∗) =
(
π∞,1
2 (M, ∗)
∂
− →π1
1(M, ∗),⊲
)
.
16
Here the group π∞,1
2 (M, ∗) is given by
π∞,1
2 (M, ∗) = {[Γ] ∈ Q 2(M, ∗) :∂d([Γ]) = [ ∗]}
with the product law being the horizontal composition. Therefore t he map
∂ .=∂u : π∞,1
2 (M, ∗) →π1
1(M, ∗) is a group morphism.
As before we have:
Theorem 25 The crossed module Π ∞,1
2 (M, ∗) can be embedded into the exact
sequence:
{0} → π2(M, ∗)
i
− →π∞,1
2 (M, ∗)
∂
− →π1
1(M, ∗)
p
− →π1(M, ∗) → {1}.
It is easy to show that the cohomology class k(M, ∗) ∈H 3 (π1(M, ∗),π 2(M, ∗))
given by this exact sequence coincides with the k-invariant of M . This follows
from the explicit construction of it in [EML], and also from the no-free -lunch
principle.
