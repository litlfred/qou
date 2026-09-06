---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-008-33-bar-constructions
section_title: "Bar constructions"
section_number: 3.3
pages: 24-25
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
an A-bimodule, i.e., the monadic bar construction for the algebra A. Let C∗(A)tr denote the
cosimplicial object obtained by passing to transposes, i.e., the como nadic cobar construction for the
coalgebra (A′,µ t). Likewise, let C∗(A)r denote the cosimplicial object obtained by passing to right
adjoints, i.e., the comonadic cobar construction for ( Ar,µ r). Note however that unless A is rigid,
the right adjoint to the unit morphism is not continuous, hence this c osimplicial object is not a
diagram of continuous functors. We use the term semi-cosimplicial o bject to refer to the diagram
object obtained from such a cosimplicial object by forgetting its co degeneracies, see [L1, Notation
6.5.3.6]. By [L1, Lemma 6.5.3.7], the inclusion of the semisimplical ∞-category in the simplicial one
is coﬁnal, so that we may calculate totalizations of cosimplicial object s as limits over the underlying
semi-cosimplicial objects. The underlying semi-cosimplicial object of C∗(A)r is indeed a diagram of
continuous functors. The following is an immediate corollary of the ab ove proposition:
Corollary 3.12. If A∈ Alg(StC) is a semi-rigid monoidal category, then the semi-cosimplic ial
objects underlying C∗(A)r and C∗(A)tr are canonically equivalent. (If in addition A is rigid, the
cosimplicial objects C∗(A)r and C∗(A)tr are canonically equivalent.) In fact, there is a natural
equivalence of diagrams of A-bimodules
C∗(A)r
LL
R /d47/d47C∗(A)tr
where the right A-action on C∗(A)r is twisted by the monoidal automorphism LL.
Recall from Section 2.3.2 that the cosimplicial diagram C∗(A)tr can be used to calculate Hochschild
cohomology of A-bimodules. The cosimplicial object C∗(A)r can likewise be used to calculate
Hochschild homology, so that Corollary 3.12 results in a general ident iﬁcation of traces and centers:
Proposition 3.13. LetA∈Alg(StC) be a semi-rigid monoidal category.
(1) For any A-bimodule, we have an equivalence between a twist of the cent er and the trace:
HH∗(A,B )≃ HH∗(A, LLB).
24
(2) In particular, for M a dualizable left A-module with dual M ′ and N an arbitrary left A-
module, there is a canonical equivalence
HomA(M, LLN )≃M ′⊗AN
between a twist of the relative Hom and the relative tensor product of the dual of M withN .
Proof. Recall the description of Hochschild homology via the bar resolution,
HH∗(A,B ) = A⊗A⊗AopB≃ colimC∗(A)⊗A⊗AopB.
By Section 2.1.4, this colimit can be identiﬁed with the limit over the corre sponding cosimplicial
diagram, obtained by taking right adjoints (note that the simplicial o bject C∗(A)⊗A⊗Aop B, the
relative tensor product of a diagram of continuous functors by B, is a diagram of continuous func-
tors). This adjoint cosimplicial diagram is naturally identiﬁed with C∗(A)r⊗A⊗Aop B, i.e., can be
calculated by taking right adjoints in C∗(A). Hence by Corollary 3.12, we ﬁnd
HH∗(A,B ) ≃ colimC∗(A)⊗A⊗AopB
≃ limC∗(A)r⊗A⊗AopB
≃ limC∗(A)t
RR⊗A⊗AopB
≃ limC∗(A)t⊗A⊗Aop LLB
≃ HH∗(A, LLB).
The second assertion follows immediately from the special case B =N⊗M ′.
□
Proposition 3.14. ForA semi-rigid and M an A-module, M is A-dualizable if and only if M is
dualizable in StC. In this case, the A-dual is canonically identiﬁed with the twisted naive dual M ′
RR
as right A-modules.
In particular, the canonical pivotal structure on Ae = A⊗Aop induces an identiﬁcation of the
Ae-dual and StC-duals of A (or any A-bimodule).
Proof. Suppose M is dualizable in S. We ﬁrst apply Proposition 3.13 and ﬁnd
HomA(M,A ) ≃ M ′⊗A LLA
≃ M ′
RR.
On the other hand
M ′
RR⊗AM ≃ M ′⊗A LLM
≃ HomA(M,M ).
We can now realize M ′
RR as the A-dual of M by taking the canonical evaluation and coevaluation
maps
M⊗M ′
RR≃M⊗ HomA(M,A ) ev /d47/d47A VectC /d47/d47 HomA(M,M )≃M ′
RR⊗AM
Similarly, if M is A-dualizable with dual ~M , we can explicitly exhibit a duality in StC between
M and M ′ = ~MLL. □
