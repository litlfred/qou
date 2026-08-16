---
doc_id: arxiv-math-9909088v1
doc_title: "THE GAUSS MAP AND A NONCOMP ACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEA VES ON SEMIABELIAN V ARIETIES"
section_id: sec-004-3-characteristic-cycle-of-an-open-embedding
section_title: "Characteristic cycle of an open embedding"
section_number: 3
pages: 4-5
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
doc_brief: "THE GAUSS MAP AND A NONCOMPACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEAVES ON SEMIABELIAN VARIETIES — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg( Z)≥ 0 as the"
---
A non-intrinsic way to ﬁnd χ(U, F) where U is a noncompact manifold, is to
apply (1.1) to Rj∗F where j :֒→X is a smooth compactiﬁcation. We will indeed
use this approach in the proof of Theorem 1.3, so we recall the (now well known)
proceedure of ﬁnding CC (Rj∗F) from CC (F), see [7] [17].
Let X be a not necessarily compact smooth variety, f∈ C[X] a regular function,
U⊂ X the open set {f⁄= 0}, and j :֒→X the embedding. Let Λ ⊂ T ∗U be an
irreducible conic Lagrangian variety. For s∈ C∗ let
(3.1) Λ #
s = Λ + sd log f ={(ξ + s(d log f )(x), x)|(x, ξ)∈ Λ}
This is a closed (no longer conic) Lagrangian subvariety in T ∗X. The total space
of the family of Λ #
s is a subvariety Λ #⊂ T ∗X× C∗. The limit lim
s→0
Λ #
s (also called
the specialization of Λ # in [7]) is an eﬀective Lagrangian cycle in T ∗X deﬁned
as follows. We ﬁrst take the closure
Λ # in T ∗X× C and then form the scheme-
theoretic intersection Λ #∩ (T ∗X×{ 0}). The cycle lim
s→0
Λ #
s is obtained by taking
the irreducible components of this intersection with the mu ltiplicities given by the
scheme structure.
We extend this construction by Z-linearity to conic Lagrangian cycles in T ∗U .
Thus, if Σ is such a cycle, we have the family of non-conic cycl es Σ #
s , s∈ C∗ and
the conic cycle lim
s→0
Σ #
s in T ∗X. Now, the fact we need is as follows.
(3.2) Theorem. If F is a bounded constructible complex on U , then
CC (Rj∗F) = lim
s→0
CC (F)#
s .
This statement can be obtained from Theorem 3.2 of [7] by appl ying the Riemann-
Hilbert correspondence, or from Theorem 3.1 of [17] which is applicable to the more
general case of R-constructible sheaves. (To be precise, the concepts of the char-
acteristic cycle used in [7-9] and [13][14][17] refer to diﬀ erent contexts: holonomic
D-modules vs. constructible complexes. The compatibility of these two deﬁnitions
of the characteristic cycle inder the Riemann-Hilbert corr espondence follows from
the results of [7].)
Consider now a nominally more general situation (cf. [9], Ap pendix A): let X be
as before but suppose that we have n regular functions f1, . . . , fn∈ C[X]. Let U
be the intersection of the n open sets {fi⁄= 0} and j :֒→X be the embedding.
Of course, this situation can be analyzed by applying Theore m 3.2 to f = f1 . . . fn,
but it will be convenient for us to have a more ﬂexible formula tion.
NONCOMPACT RIEMANN-ROCH 5
For a point s = ( s1, . . . , sn)∈ (C∗)n and a conic Lagrangian variety Λ ⊂ T ∗U
we form, similarly to (3.1), a non-conic Lagrangian variety
(3.3) Λ #
s = Λ +
n∑
i=1
sid log fi⊂ T ∗X.
The total space of this family lies in T ∗X× (C∗)n. Taking the closure in T ∗X× Cn
and then intersecting with T ∗X×{ (0, . . . ,0)} deﬁnes, similarly to the above, a
conic Lagrangian cycle lim
s→(0,..., 0)
Λ #
s . Of course, this “limit” could be taken along
any curve in Cn passing through 0 and generically lying in ( C∗)n. As before, we
extend this construction by linearity to conic Lagrangian c ycles in T ∗U . The next
statement follows by iterated application of Theorem 3.2.
(3.4) Theorem. If F is a bounded constructible complex on U , then
CC (Rj∗F) = lim
s→(0,..., 0)
CC (F)#
s , s = (s1, . . . , sn)∈ (C∗)n.
Taking the limit along diﬀerent curves approaching (0, . . . ,0) corresponds, roughly,
to diﬀerent choices of our equation for the reducible hypers urface X\ U . For exam-
ple, restricting to the curve with parametric equation si = tmi, mi > 0 corresponds
to taking ∏
i f mi
i as an equation.
We now need a slight globalization of Theorem 3.4. First of al l, let ( L,∇) be a
line bundle on X with an algebraic ﬂat connection. If f is a regular section of L,
then f −1∇f is a scalar 1-form regular over the open set {f⁄= 0}. We denote this
form∇ log f .
Suppose now that we have n line bundles with ﬂat connections ( Li,∇i) on X,
i = 1 , . . . , n. Suppose fi∈ Γ( X, Li), i = 1 , . . . , n and U⊂ X is the intersection of
the open sets {fi⁄= 0}. As before, let j :֒→X be the embedding.
(3.5) Theorem. For a bounded constructible complex F on U we have
CC (Rj∗F) = lim
s→(0,..., 0)
(
CC (F) +
n∑
i=1
si∇i log fi
)
.
Proof: As before, it is enough to consider the case n = 1, as the general case
can be obtained by iteration, as in [9], Appendix A. The state ment for n = 1 is
a consequence of Theorem 6.3 of [8] which deals with the more g eneral case of
the zero locus of a section f of an arbitrary line bundle L, not necessarily with
connection. The recipe in this case is to consider the “twist ed cotangent bundles”
(T ∗X)(s), s∈ C, deﬁned as the symplectic quotients of T ∗L by the hamiltonian
action of C∗ induced by dilations of L. Now, if L is equipped with a ﬂat connection
∇, then all the ( T ∗X)(s) become identiﬁed with T ∗X and the formulation of [8],
Theorem 6.3 reduces to our statement.
