---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-029-reflexively-polite-kernels
section_title: "Reflexively polite kernels."
section_number: null
pages: 35-38
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
Reﬂexively polite kernels.
We still need to address one more compatibility between the dualities con-
structed above. Given a kernel Φ, the previous proposition yields a polite
duality
Φ
∨
←→Φ∨.
Given any polite duality Φ
∨
←→Φ†, we get, symmetrically, a polite duality
Φ†
∨
←→Φ by switching the adjunctions 1 and 3 and the adjunctions 2 and
4. Thus there is a natural polite duality
Φ∨
∨
←→Φ.
On the other hand, applying Proposition 20 to the kernel Φ∨we get a polite
duality Φ∨
∨
←→Φ∨∨and then, using the canonical identiﬁcation Φ∨∨∼= Φ,
we get another polite duality
Φ∨
∨
←→Φ.
The fundamental question is whether these two polite dualities are the same.
35
Deﬁnition. Let Φ: X →Y be a kernel. We shall say that Φ is reﬂexively
polite if the two dualities above are equal.
Immediately we get the following result.
Proposition 21. If a kernel Φ is reﬂexively polite then so is Φ∨.
Proposition 22. If Φ: X →Y and Ψ: Y →Z are reﬂexively polite kernels
then so is Ψ ◦Φ.
Proof. This follows at once from the fact that the adjunctions deﬁned in
Proposition 18 are canonical.
Proposition 23. Suppose that Φ: X →Y and Ψ: X′ →Y ′ are reﬂexively
polite kernels then so is Φ ⊠Ψ: X × X′ →Y × Y ′, the kernel deﬁned by
Φ ⊠Ψ := π∗
XYΦ ⊗π∗
X′Y′Ψ.
Proof. This is obvious once one realises that all operations decompose with
respect to the box product operation, and the canonical bundle of a product
of spaces is the box product of the canonical bundles of the factors.
Proposition 24. Let ∆: X →X × X denote the diagonal map, let E be an
object in D(X), then the kernel ∆∗E : X →X is reﬂexively polite.
Proof. The dual (∆∗E )∨of ∆∗E is naturally identiﬁed with
∆∗(E ∨⊗ω−1
X [−dim X]).
The result now follows from Proposition 2 and the fact that the functor
given by tensoring with an object of the derived category is left and right
adjoint to the one obtained by tensoring with the dual object.
Proposition 25. Let X be a space, then the kernel OX considered as a kernel
X →pt is reﬂexively polite, and so also is O∨
X : pt →X.
Proof. First, observe that checking reﬂexive duality amounts to checking the
equality of two quadruples of adjunctions. In each quadruple, any one of
the adjunctions determines the remaining three, and thus in order to check
the equality it suﬃces to check that one of the compatibilities (1+2), (1+3),
etc. holds with one adjunction chosen from one duality, and the other one
from the second duality.
Furthermore, adjunctions are completely determined by their respective
units and counits, and these are determined by considered functors between
derived categories of the form
Φ ◦−: D(Z × X) =: HomV ar(Z, X) →HomV ar(Z, pt) := D(Z),
and analogues for Φ∨◦−, for various choices of the space Z. Thus, if we argue
that the desired equality holds for the adjunctions between these induced
36
functors (for arbitrary choice of Z), we will have argued that Φ is reﬂexively
polite.
For ease of notation, write Φ for the kernel OX: X →pt. For a given
space Z, let πZ: X × Z →Z denote the projection. The functors Φ ◦−
and Φ∨◦−are then naturally identiﬁed with πZ,∗and π∗
Z, respectively.
Adjunctions 1 and 2 from the polite duality Φ
∨
←→Φ∨correspond to the
classical adjunctions
π∗
Z ⊣πZ,∗⊣π!
Z,
while the same ones from the polite duality Φ∨
∨
←→Φ∨∨correspond to
πZ,! ⊣π∗
Z ⊣πZ,∗.
Indeed, the standard way (see [6, Theorem 4.6]) to deﬁne the adjunctions
πZ,∗⊣π!
Z and πZ,! ⊣π∗
Z is to require them to satisfy the analogue of condi-
tion (1+2) from the deﬁnition of a polite duality.
The condition of polite duality can now can be stated as the statement
that the composite isomorphism
HomX×Z(Θ,π∗
ZΨ) ∼= HomZ(πZ,!Θ, Ψ) = HomZ(πZ,∗S(Θ), Ψ)
∼= HomX×Z

S(Θ), π!
ZΨ

= HomX×Z(S(Θ), S(π∗
ZΨ))
is the one induced by the functor S(−) = −⊗π∗
XωX[dim X], where πX denotes
the projection from X × Z to X. This fact corresponds to the fact that the
diagram marked (!) below commutes
Hom(Θ, π∗Ψ)
∼
Hom(S−1π∗SΘ, Ψ)
∼
Hom(π∗SΘ, SΨ)
∼
Hom(SΘ, Sπ∗Ψ)
Serre
(!)
Serre
Hom(π∗Ψ, SΘ)
∨
∼
∼
Hom(Ψ, π∗SΘ)
∨
∼
=== Hom(Ψ, π∗SΘ)
∨
∼
∼
Hom(π∗Ψ, Θ)
∨.
∼
Proposition 26. Let πX: X × Y →X be the projection, and (abusing nota-
tion) denote by πX,∗: X × Y →X and π∗
X: X →X × Y the kernels represented
in D(X × X × Y) by the structure sheaf of the graph of πX. Then πX,∗and
π∗
X are reﬂexively polite.
Proof. Both kernels are of the form O∆X ⊠OY, and the result then follows
from Propositions 25, 24, and 23.
Theorem 27. Every kernel is reﬂexively polite.
Proof. With notation as in Proposition 26, any kernel Φ: X →Y decomposes
as
Φ = πY,∗◦(−⊗Φ) ◦π∗
X.
Since the claim of the theorem holds for each individual kernel in the decom-
position (Propositions 26 and 24), the result follows from Proposition 18.
37
