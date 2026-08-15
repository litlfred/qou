---
doc_id: afst-2007-6-16-3-665-0
doc_title: "ANNALES DE LA FACULTÉ DES SCIENCES Mathématiques"
section_id: sec-020-7-positive-characteristic
section_title: "Positive characteristic"
section_number: 7
pages: 47-49
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Atiyah’s paper makes some excursions to positive characteristic. Here,
wedothesamefor q-diﬀerenceequations.Wereplacetheﬁeld Cb yaﬁeldC
whichisalgebraicallyclosedandcompleteforanontrivialnonarchimedean
valuation. The case whereC has characteristic 0 (i.e.,C ⊃ Q
p for some
primep) is not very interesting since most of the preceeding results can be
copied from the complex case with the help of some rigid analysis.
Inthissectionweconsideranalgebraicallyclosedﬁeld Cofcharacteristic
p> 0, complete with respect to a non trivial valuation. Further we choose
aq ∈ C with 0< |q|<1.
Over K = C({z}), ˆK = C((z)) and C(z) one can deﬁneq-diﬀerence
modules and study their properties. The elliptic curve associated to this is
the Tate curveE
q := C∗/qZ, constructed with the help of rigid analysis.
We note that this curve is special in the sense that itsj-invariant is tran-
scendental overFp and in particularEq is ordinary. We make now a quick
investigation of the main results of this paper in this new context.
– 710 –
Galois theory ofq-diﬀerence equations
Lemma 7.1.— There exists an explicit pair (F,φ) of an algebraically
closed ﬁeldF and an automorphismφ, such thatF ⊃ ˆK and φ extends the
given automorphism of ˆK. The pair(F,φ) induces automorphisms of the
algebraic closures of ˆK and K extending the givenφ.
Proof.— The algebraic closure of ˆK has no explicit description. How-
ever, there is an explicit algebraically closed ﬁeldF := C((zQ)) containing
ˆK. The elements of this ﬁeld are expressions∑
λ∈Qaλzλ with allaλ ∈ C
and such that{λ| aλ ⁄=0 } is a well ordered subset ofQ. It is well known
that F is a maximally complete ﬁeld with residue ﬁeldC and value group
Q. In particular,F is algebraically closed. Choose a homomorphismλ ↦→qλ
from Q to C∗ with q1 = q. One deﬁnes an automorphismφ of F by the
formula φ(∑
λ∈Qaλzλ)= ∑
λ∈Qaλqλzλ. This extends the action ofφ on
ˆK. The algebraic closures ofˆK and K can be seen as subﬁelds ofF. They
are obviously invariant underφ. This proves the assertion. □
Lemma 7.2.—L et ˆK ⊂L be an extension of degreem< ∞ such thatφ
extends to an automorphism ofL. ThenL= ˆK(z1/m). A similar statement
holds forK replacing ˆK.
Proof.— Write L = C((t)). Then z = amtm +am+1tm+1 + ··· with
am ⁄= 0. The action ofφ on L has therefore the formφ(t)= q1t+ ··· with
qm
1 =q. Since 0< |q1|<1, one can produce an elements ∈ C[[t]] such that
C[[s]] =C[[t]] andφ(s)= q1s. Thus we may assume thatφ(t)= q1t. Then
q(amtm +am+1tm+1 + ··· )= qz =φ(z)= amqm
1 tm +am+1qm+1
1 tm+1 + ···
implies thatz =amtm. This proves the statement for the caseˆK.
For the caseK, one has to show thatL = C{t} contains an elements
with C{s} = C{t} and φ(s)= s. Writeφ(t)= q1t+a2t2 + ··· and s =
t+b2t2+b3t3+ ··· . Thenφ(s)= q1s leads to a sequence of equations for the
bi. An inspection shows that the convergence of the seriesq1t+ ∑
n/greaterorequalslant2antn
implies the convergence of the seriest+ ∑
n/greaterorequalslant2bntn. □
Most of the preceeding sections remain valid, after a small adaptation,
in the present context. We give now some details.
In section 1, the ﬁeldsK∞ and ˆK∞ should be read here, not as the
algebraic closures but as the ﬁelds ∪n/greaterorequalslant1Kn with Kn := C({z1/n}) and
∪n/greaterorequalslant1 ˆKn with ˆKn := C((z1/n)). The complex function theory forEq is
replaced by the rigid analytic theory (see for instance [Fr-vdP]) and the
– 711 –
Marius van der Put, Marc Reversat
formulas in subsection 1.1 remain valid. The only part of section 1 that has
no (obvious) translation is subsubsection 1.4.1.
All of section 2 remains valid with the exception of Remarks 2.4. Indeed,
the formulas for the decomposition of tensor products of indecomposable
modules (or for indecomposable vector bundles onE
q) are diﬀerent in pos-
itive characteristic. Especially, the decomposition ofUa ⊗K Ub poses a non
trivialcombinatorialproblem,solvedin[At]inthecontextofvectorbundles
onE
q.
No changes are needed for the results of sections 3 and 4. However we
will rewrite Section 5 completely by developing a suitable Picard-Vessiot
theory, calculating diﬀerence Galois groups and a universal Picard-Vessiot
ring. We take [vdP-S 1,2] as guide for this.
It isnot possible to attach, as in Theorem 6.1, to regular singular dif-
ference modules M over K, connections onv(M). Indeed, for the mod-
ule Ke with Φe = ce and c ∈ C
∗, the connection must have the form
∇e = a(c)dz
z ⊗e, where a : C∗ → C is a homomorphism and satisﬁes
a(q) = 1. However,a(q)= p ·a(q1/p)=0 .
