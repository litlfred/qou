---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-014-6-construction-of-noncommutative-examples
section_title: "Construction of noncommutative examples"
section_number: 6
pages: 30-31
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
For J 1
A and J 1
E, we need only a diﬀerential algebra (A, Ω, d) (plus a connection on E in the
vector bundle case) and for J 2
A and J 2
E also a torsion free connection on Ω1 (and the connection
inE should be ﬂat). Thus we can use for∇any number of connections in the literature, including
the QLCs of the many known quantum Riemannian geometries as covered in [4].
For general Jk
A and Jk
E, however, we need a torsion free ﬂat connection ∇with the extra
conditions of being ∧-compatible, extendable and the Leibniz-compatibility condition. In the
vector bundle case we also need the connection on E to be ﬂat and the extra conditions of
extendable and Leibniz compatible. We also know that Leibniz-compatibility implies the relevant
braid relations. In the classical case, all of the extra conditions hold automatically as σ,σE are
the ﬂip map. Hence, classically, we see only the geometric part of this data. This is still a
signiﬁcant restriction as discussed in the Introduction.
An obvious example in the noncommutative case is to assume that A has a central basis of
1-forms {ei}i=n
i=1 which are closed and have the usual Grassmann algebra wedge product. This
applies for example to the noncommutative torus and many other diﬀerential algebras. If we set
∇ei = 0 on the basis then
da⊗ei =∇(aei) =∇(eia) =σ(ei⊗da)
for all a ∈A, which means (pulling the coeﬃcients of d a = ∂iaei to one side by centrality)
thatσ = ﬂip on the basis. Sum over repeated indices should be understood here. As we assumed
dei = 0 then∇is torsion free and clearly ﬂat when computed on the basis (which is enough as the
torsion and curvature tensors are left module maps). For the other conditions of extendability,
∧-compatibility and Leibniz-compatibility, all of these can likewise can be checked on the basis
(moving all coeﬃcients to the left) and then they all obviously hold since σ is just the ﬂip map.
Hence all conditions of Theorem 4.8 apply in this easy case. The prolongation map is
(16) j∞(s) =s+(∂is)ei+(∂j∂is)ej⊗ei+/uni22EF.
That the 3rd term here lives in Ω2
S follows from d2s= 0 because, for the Grassmann algebra, this
implies that ∂j∂is = ∂i∂js while Ω 2
S has a basis of symmetric tensor products ei⊗ej +ej⊗ei.
The bullet bimodule structure for k = 2, for example, is
a●2s=j2(a)s, a ●2ω =aω+ da⊗ω+ω⊗da, a ●2 (ω1⊗ω2) =aω1⊗ω2
for ω ∈Ω1 and ω1⊗ω2 ∈Ω2
S and similarly on the other side. Moreover, the algebra Ω S can be
identiﬁed withSσ(Ω1) generated overA by the polynomialsk[e1,/uni22EF,en]. J∞
A is similar but much
bigger in allowing powerseries, and for each k has bimodule actions transferred from ●k.
For more nontrivial examples, we look at the opposite extreme from classical, where Ω is inner.
This says that there is a θ ∈Ω1 such that d = [θ, }, where [, }is the graded commutator. This
happens frequently in noncommutative geometry, in spite of no classical analogue. The main
theorem we need in this case is a result in [18, 4] that any bimodule connection on Ω 1 can be
constructed as
∇=θ⊗( )−σ(( )⊗θ)+α, σ ∶Ω1⊗
A
Ω1→Ω1⊗
A
Ω1, α ∶Ω1→Ω1⊗
A
Ω1
QUANTUM JET BUNDLES 31
for bimodule maps σ,α as shown. Then σ becomes the generalised braiding. We will say that ∇
is inner if α= 0.
Proposition 6.1. For an inner ∇on an inner diﬀerential algebra (A, Ω,θ):
(1) ∇has zero torsion iﬀ ∧σ(ω⊗θ) =−ω∧θ for all ω ∈Ω1.
(2) ∇is ∧-compatible iﬀ the 2nd part of Fig. 1(c) gives a well-deﬁned map σΩ2. In this case
∇Ω2 =θ⊗( )−σΩ2(( )⊗θ).
(3) If ∇is extendable then it is ﬂat iﬀ σ(ω⊗θ2) =θ2⊗ω for all ω ∈Ω1.
(4) If ∇is extendable then R∇is a bimodule map.
(5) ∇obeys the Leibniz-compatibility Fig. 1(e) iﬀ σ obeys the braid relations Fig. 1(g). The
latter hold iﬀ σ they hold on Ω1⊗A Ω1⊗Aθ.
Proof. (1) This is immediate from putting the form of ∇into Fig. 1(a) and d = {θ,( )} on 1-
forms. As in [18], it means that the the second part of (a) is equivalent to torsion freeness in
this case. (2) Putting the form of ∇into Fig. 1(c) and cancelling immediately gives the stated
formula for ∇Ω2. Hence in this case, the 2nd part of Fig. 1(c) implies and is hence equivalent
to the ﬁrst part. (3) Putting in the form of ∇into Fig. 1(b) and d = {θ,( )} gives ﬂatness iﬀ
θ∧θ⊗ω = ∧1σ2σ1(ω⊗θ⊗θ) for all ω ∈Ω1, as noted in [18, 4]. In the extendable case, this
simpliﬁes as shown. We actually just needed Fig. 1(d) applied to θ⊗θ. (4) We put in the
form of ∇and d = {θ,( )} into Fig. 1(f) and ﬁnd in the extendable case that all the terms
cancel. We actually just need Fig. 1(d) applied to Ω 1⊗θ and θ⊗Ω1. (5) We put in the form
of ∇into Fig. 1(e) and ﬁnd that all terms cancel except for two, which are Fig. 1(g) applied to
Ω1⊗A Ω1⊗Aθ. Hence this is equivalent to Leibniz compatible. But if this holds then it implies
that σ obeys the braid relations on all of Ω 1⊗A 3. □
