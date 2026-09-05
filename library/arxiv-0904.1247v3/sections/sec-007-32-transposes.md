---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-007-32-transposes
section_title: "Transposes"
section_number: 3.2
pages: 22-24
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
a comodule structure over A′, with coaction map given by the transpose
at
M :M
η⊗id /d47/d47A′⊗A⊗M
id⊗aM/d47/d47A′⊗M
It is evident from this construction that the comodule structure is functorial for all A-linear functors
M→N . In other words, we have an equivalence
ModA(StC)≃ ComodA′ (StC)
commuting with the natural forgetful functors to StC.
The left and right dualities on compact objects
L(a) = ∨a, R (a) = a∨, for a∈A compact,
canonically extend by continuity to equivalences
L,R :A ∼ /d47/d47A′
LetLL,RR :A→A denote the inverse monoidal automorphisms of A given by taking double duals.
Moreover, the identities
HomA(∨(x⋆m⋆y ),n )≃ HomA(∨m, ∨∨y⋆n⋆x ),
HomA((x⋆m⋆y )∨,n )≃ HomA(m∨,y⋆n⋆x ∨∨)
show that L is a naturally a morphism of right A-modules and R of left A-modules, while L inter-
twines the left action of A with the action twisted by the monoidal automorphism LL :A→A, and
likewiseR intertwines the right action of A with the action twisted by the monoidal automorphism
RR :A→A. In other words, we have isomorphisms of A-bimodules
RRA L /d47/d47A′ ALL
R/d111/d111
where we twist the bimodule A on one side or the other by the inverse monoidal automorphisms
LL,RR .
22
Deﬁnition 3.8. A pivotal structure on a semi-rigid monoidal category A∈Alg(StC) is a monoidal
identiﬁcation of the automorphism LL (or equivalently, of its inverse RR) with the identity of A.
It follows that a pivotal structure is equivalent to a lift of either of t he functors L,R :A→A′ to
a morphism of A-bimodules (or to a monoidal identiﬁcation of left and right duals in A).
Example 3.9. For any semi-rigid monoidal category A∈ Alg(StC), the semi-rigid monoidal cat-
egory Ae = A⊗ Aop has a canonical pivotal structure, deduced from its symmetric st ructure
Ae ∼ /d47/d47 (Ae)op exchanging left and right duals.
Remark 3.10 (The canonical trace) . It is enlightening (though not necessary for the rest of this
paper) to understand the notion of a pivotal structure in terms o f traces.
Suppose A ∈ Alg(StC) is a semi-rigid monoidal category. Consider the unit morphism u :
VectC→A and its transpose
τ :=utr :A R /d47/d47A′ u′
/d47/d47 Vect′
C
R−1
/d47/d47 VectC
If a∈A is compact, then we have
τ (a)≃ HomA(1A,a )
and in general τ is the continuous extension of this assignment (which will agree with t he Hom
functional if and only if A is rigid).
Given compact objects a,b∈A, we have canonical identiﬁcations
τ (a⋆b ) = Hom A(1A,a⋆b )≃ HomA((b∨)∨,a ) = τ ((b∨)∨⋆a )
It follows that a pivotal structure on A, i.e., a monoidal identiﬁcation RR≃ id, gives rise to a
trace structure on the functional τ , i.e., a functorial identiﬁcation τ (a⋆b )≃ τ (b⋆a ) plus higher
compatibilities. More precisely, a pivotal structure gives rise to a fa ctorization
A tr /d47/d47
τ
/d34/d34❊❊❊❊❊❊❊❊❊ Tr(A)
/d15/d15
S
and is in fact equivalent to such a factorization.
3.2.1. Adjoints are transposes. We may now identify the two coalgebras (A,µ r) and (A′,µ t) obtained
from a semi-rigid monoidal category:
Proposition 3.11. LetA∈Alg(StC) be a semi-rigid monoidal category.
There is a canonical equivalence of comonoidal categories (A,µ r)≃ (A′,µ t) given on the level of
objects by taking right duals, i.e., by the equivalence R :A→A′.
In particular, for an A-module M with action map aM : A⊗M→ M , the right adjoint ar
M :
M→A⊗M and the transpose at
M :M→A′⊗M are related by the duality R in the sense that the
following diagram canonically commutes:
M
ar
M /d35/d35❍❍❍❍❍❍❍❍❍
at
M /d47/d47A′⊗M
R⊗id
/d15/d15
A⊗M
Proof. The ﬁrst assertion follows from the identiﬁcations
ComodAr (StC)≃ ModA(StC)≃ ComodA′(StC)
of categories comonadic over StC, whence the coalgebras Ar andA′ representing the corresponding
comonads are naturally identiﬁed.
23
To verify that the identiﬁcation is given by right duals, let us check by hand the second part of
the proposition. Note that the action aM is quasi-proper by Lemma 3.4. Since A generates the
category of A-modules by colimits, it suﬃces to establish the claim in the universal ca se M = A,
where a =aA is the left action of A on itself. Thus we have to identify the map
µr :A /d47/d47A⊗A
with the map
A at
/d47/d47A′⊗A
R⊗id /d47/d47A⊗A.
Both are maps of right A-modules, hence it suﬃces to identify the images of the unit
ηA : VectC /d47/d47A /d47/d47A⊗A
under the two maps. For the ﬁrst, it is characterized on compact o bjects by
HomA(m⊗n,µ r(1A)) ≃ HomA(m⋆n, 1A)
≃ HomA(m,n ∨)
For the second, the composition
VectC /d47/d47A /d47/d47A′⊗A /d47/d47A⊗A
sends the unit to ( R⊗ id)([Hom])∈A⊗A, which is characterized on compact objects by
HomA⊗A(m⊗n, (R⊗ id)([Hom])) ≃ HomA(∨m,n )
≃ HomA(m,n ∨)
□
