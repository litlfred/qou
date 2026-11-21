---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-016-7-positive-characteristic
section_title: "Positive characteristic"
section_number: 7
pages: 47-49
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Atiyah’s paper makes some excursions to positive characteristic. Here,
we do the same for q-diﬀerence equations. We replace the ﬁeld C by a ﬁeld C
which is algebraically closed and complete for a non trivial non archimedean
valuation. The case where C has characteristic 0 (i.e., C ⊃Qp for some
prime p) is not very interesting since most of the preceeding results can be
copied from the complex case with the help of some rigid analysis.
In this section we consider an algebraically closed ﬁeld C of characteristic
p > 0, complete with respect to a non trivial valuation. Further we choose
a q ∈C with 0 < |q| < 1.
Over K = C({z}), K = C((z)) and C(z) one can deﬁne q-diﬀerence
modules and study their properties. The elliptic curve associated to this is
the Tate curve Eq := C∗/qZ, constructed with the help of rigid analysis.
We note that this curve is special in the sense that its j-invariant is tran-
scendental over Fp and in particular Eq is ordinary. We make now a quick
investigation of the main results of this paper in this new context.
– 710 –
Galois theory of q-diﬀerence equations
Lemma 7.1. — There exists an explicit pair (F, φ) of an algebraically
closed ﬁeld F and an automorphism φ, such that F ⊃K and φ extends the
given automorphism of K. The pair (F, φ) induces automorphisms of the
algebraic closures of K and K extending the given φ.
Proof. — The algebraic closure of K has no explicit description. How-
ever, there is an explicit algebraically closed ﬁeld F := C((zQ)) containing
K. The elements of this ﬁeld are expressions 
λ∈Q aλzλ with all aλ ∈C
and such that {λ| aλ̸ = 0} is a well ordered subset of Q. It is well known
that F is a maximally complete ﬁeld with residue ﬁeld C and value group
Q. In particular, F is algebraically closed. Choose a homomorphism λ →qλ
from Q to C∗with q1 = q. One deﬁnes an automorphism φ of F by the
formula φ(
λ∈Q aλzλ) = 
λ∈Q aλqλzλ. This extends the action of φ on
K. The algebraic closures of K and K can be seen as subﬁelds of F. They
are obviously invariant under φ. This proves the assertion.
□
Lemma 7.2. — Let K ⊂L be an extension of degree m < ∞such that φ
extends to an automorphism of L. Then L = K(z1/m). A similar statement
holds for K replacing K.
Proof. — Write L = C((t)). Then z = amtm + am+1tm+1 + · · · with
am̸ = 0. The action of φ on L has therefore the form φ(t) = q1t + · · · with
qm
1 = q. Since 0 < |q1| < 1, one can produce an element s ∈C[[t]] such that
C[[s]] = C[[t]] and φ(s) = q1s. Thus we may assume that φ(t) = q1t. Then
q(amtm + am+1tm+1 + · · ·) = qz = φ(z) = amqm
1 tm + am+1qm+1
1
tm+1 + · · ·
implies that z = amtm. This proves the statement for the case K.
For the case K, one has to show that L = C{t} contains an element s
with C{s} = C{t} and φ(s) = s. Write φ(t) = q1t + a2t2 + · · · and s =
t+b2t2 +b3t3 +· · ·. Then φ(s) = q1s leads to a sequence of equations for the
bi. An inspection shows that the convergence of the series q1t + 
n⩾2 antn
implies the convergence of the series t + 
n⩾2 bntn.
□
Most of the preceeding sections remain valid, after a small adaptation,
in the present context. We give now some details.
In section 1, the ﬁelds K∞and K∞should be read here, not as the
algebraic closures but as the ﬁelds ∪n⩾1Kn with Kn := C({z1/n}) and
∪n⩾1 Kn with Kn := C((z1/n)). The complex function theory for Eq is
replaced by the rigid analytic theory (see for instance [Fr-vdP]) and the
– 711 –
Marius van der Put, Marc Reversat
formulas in subsection 1.1 remain valid. The only part of section 1 that has
no (obvious) translation is subsubsection 1.4.1.
All of section 2 remains valid with the exception of Remarks 2.4. Indeed,
the formulas for the decomposition of tensor products of indecomposable
modules (or for indecomposable vector bundles on Eq) are diﬀerent in pos-
itive characteristic. Especially, the decomposition of Ua ⊗K Ub poses a non
trivial combinatorial problem, solved in [At] in the context of vector bundles
on Eq.
No changes are needed for the results of sections 3 and 4. However we
will rewrite Section 5 completely by developing a suitable Picard-Vessiot
theory, calculating diﬀerence Galois groups and a universal Picard-Vessiot
ring. We take [vdP-S 1,2] as guide for this.
It is not possible to attach, as in Theorem 6.1, to regular singular dif-
ference modules M over K, connections on v(M). Indeed, for the mod-
ule Ke with Φe = ce and c ∈C∗, the connection must have the form
∇e = a(c) dz
z ⊗e, where a : C∗→C is a homomorphism and satisﬁes
a(q) = 1. However, a(q) = p · a(q1/p) = 0.
