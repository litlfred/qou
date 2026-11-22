---
doc_id: arxiv-math-9909088v1
doc_title: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
toc_source: undetermined
doc_brief: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg(Z) ≥0 as the"
---
4
J. FRANECKI, M. KAPRANOV
We now specialize to the case M = Z, V = g, n = dim(G) and f = ΓZ. The
number deg(ΓZ) will be denoted by gdeg(Z) and called the Gaussian degree of Z.
Let Λ = T ∗
ZG be the conic Lagrangian variety associated to Z. We will write
gdeg(Λ) for gdeg(Z). As in Section 1, for γ ∈g∗let Ωγ ⊂T ∗X be the graph of the
left-invariant1-form ωγ on G associated to γ. Proposition 2.1 implies easily:
(2.2) Proposition. Let γ ∈g∗be a generic linear functional. Then Λ∩Ωγ consists
of ﬁnitely many points which are smooth on Λ and in which the intersection is
transverse. The number of these points is equal to gdeg(Λ).
3. Characteristic cycle of an open embedding
A non-intrinsic way to ﬁnd χ(U, F) where U is a noncompact manifold, is to
apply (1.1) to Rj∗F where j : U֒ →X is a smooth compactiﬁcation. We will indeed
use this approach in the proof of Theorem 1.3, so we recall the (now well known)
proceedure of ﬁnding CC(Rj∗F) from CC(F), see [7] [17].
Let X be a not necessarily compact smooth variety, f ∈C[X] a regular function,
U ⊂X the open set {f̸ = 0}, and j : U֒ →X the embedding. Let Λ ⊂T ∗U be an
irreducible conic Lagrangian variety. For s ∈C∗let
(3.1)
Λ#
s = Λ + sd log f = {(ξ + s(d log f)(x), x)|(x, ξ) ∈Λ}
This is a closed (no longer conic) Lagrangian subvariety in T ∗X. The total space
of the family of Λ#
s is a subvariety Λ# ⊂T ∗X × C∗. The limit lim
s→0 Λ#
s (also called
the specialization of Λ# in [7]) is an eﬀective Lagrangian cycle in T ∗X deﬁned
as follows. We ﬁrst take the closure Λ# in T ∗X × C and then form the scheme-
theoretic intersection Λ# ∩(T ∗X × {0}). The cycle lim
s→0 Λ#
s is obtained by taking
the irreducible components of this intersection with the multiplicities given by the
scheme structure.
We extend this construction by Z-linearity to conic Lagrangian cycles in T ∗U.
Thus, if Σ is such a cycle, we have the family of non-conic cycles Σ#
s , s ∈C∗and
the conic cycle lim
s→0 Σ#
s in T ∗X. Now, the fact we need is as follows.
(3.2) Theorem. If F is a bounded constructible complex on U, then
CC(Rj∗F) = lim
s→0 CC(F)#
s .
This statement can be obtained from Theorem 3.2 of [7] by applying the Riemann-
Hilbert correspondence, or from Theorem 3.1 of [17] which is applicable to the more
general case of R-constructible sheaves. (To be precise, the concepts of the char-
acteristic cycle used in [7-9] and [13][14][17] refer to diﬀerent contexts: holonomic
D-modules vs. constructible complexes. The compatibility of these two deﬁnitions
of the characteristic cycle inder the Riemann-Hilbert correspondence follows from
the results of [7].)
Consider now a nominally more general situation (cf. [9], Appendix A): let X be
as before but suppose that we have n regular functions f1, . . . , fn ∈C[X]. Let U
be the intersection of the n open sets {fi̸ = 0} and j : U֒ →X be the embedding.
Of course, this situation can be analyzed by applying Theorem 3.2 to f = f1 . . . fn,
but it will be convenient for us to have a more ﬂexible formulation.
