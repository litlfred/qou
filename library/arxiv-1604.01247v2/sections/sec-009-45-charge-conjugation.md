---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-009-45-charge-conjugation
section_title: "Charge conjugation"
section_number: 4.5
pages: 23-30
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3 generations, we develop an"
---
In the identiﬁcation of the octonion algebra O as C ⊕ C3, the octonionic
conjugate of ( z, Z ) = z + Z is
(z, Z ) = (¯z, −Z) = ¯z − Z.
On the other hand if one interprets Z ∈ C3 as an internal quark state and
z ∈ C as an internal state of the corresponding lepton, the charge con jugation
C induces the complex conjugation in C3 and in C that is
C(z + Z) = ¯z + ¯Z (4.20)
23
for z ∈ C, Z ∈ C3.
It is easy to verify by using Formula (2.8) that C is an automorphism of
O (C ∈ G2) with C2 = 1 l by construction. This automorphism of O induces
canonically an involutive automorphism of the Jordan algebra J 8
3 as well as
of the J 8
3 -modules. These automorphisms will be all denoted by C.
5 Diﬀerential calculus over Jordan algebras
5.1 First order diﬀerential calculi
Given a category C of algebras over some ﬁeld K and an algebra A in C, a
pair (Ω 1, d ) of an A-bimodule Ω 1 for C [14] and a derivation d of A into Ω 1,
that is a K-linear mapping satisfying (the Leibniz rule)
d(xy) = d(x)y + xd(y)
for any x, y ∈ A, will be refered to as a ﬁrst order diﬀerential calculus over A
for C or simply a ﬁrst order calculus over A when no confusion arises. There
is an obvious notion of homomorphism of ﬁrst order diﬀerential calcu li over
A. This terminology as well as the one for higher order diﬀerential calc uli
was introduced in [40] for the case of the category of associative algebras on
a ﬁeld K.
In the following we shall be concerned with the category of real unit al
Jordan algebras so, if J is such a unital Jordan algebra, a J-bimodule is
a unital J-module which will be simply refered to as a J-module when no
confusion arises.
Let J be a unital Jordan algebra and let us deﬁne its center Z(J) by
Z(J) = {z ∈ J|[x, y, z ] = [ x, z, y ] = 0 , ∀x, y ∈ J} (5.1)
where [ x, y, z ] = ( xy)z − x(yz) denotes the associator of x, y, z ∈ J. The
center Z(J) is a unital associative subalgebra of J. The Lie algebra Der( J)
of all derivations of J into itself is also a Z(J)-module and we denote by
Ω 1
Der(J) the J-module of all the Z(J)-homomorphisms of Der( J) into J. One
deﬁnes a derivation
dDer : J → Ω 1
Der(J)
24
by setting
dDer(x)(X) = X(x)
for any x ∈ J and X ∈ Der(J).
This ﬁrst-order diﬀerential calculus (Ω 1
Der(J), d Der) will be referred to as the
derivation-based ﬁrst order diﬀerential calculus over J.
5.2 First order diﬀerential calculi over J 8
3
The Lie algebra Der( J 8
3 ) of all derivations of the exceptional Jordan algebra
J 8
3 is the exceptional compact simple Lie algebra f4. Since J 8
3 is simple
Z(J 8
3 ) = R so the unital J 8
3 -module Ω 1
Der(J 8
3 ) is the vector space of all linear
mappings of Der( J 8
3 ) into J 8
3 that is
Ω 1
Der(J 8
3 ) = J 8
3 ⊗ Der(J 8
3 )∗
where Der( J 8
3 )∗ = f∗
4 denotes the dual vector space of Der( J 8
3 ).
One deﬁnes as before the derivation dDer : J 8
3 → Ω Der(J 8
3 ) by setting
dDer(x)(X) = X(x) for any x ∈ J 8
3 and X ∈ Der(J 8
3 ). The ﬁrst order dif-
ferential calculus (Ω Der(J 8
3 ), d Der) over J 8
3 is characterized by the following
universal property.
Proposition 3. For any ﬁrst order calculus (Ω 1, d ) over J 8
3 , there is a unique
(unital) Jordan module homomorphism id : Ω 1
Der(J 8
3 ) → Ω 1 such that one has
d = id ◦ dDer.
Proof
. From the general structure of the J 8
3 -modules, Ω 1 is of the form
Ω 1 = J 8
3 ⊗ E for some vector space E. Let ( eα) be a basis of E then
d(x) = Xα(x) ⊗ eα with Xα ∈ Der(J 8
3 ) for any α . Let ( ∂k) be a basis
of Der( J 8
3 ) with dual basis θk then one has d(x) = ∂k(x) ⊗ C k
αeα with the
C k
α ∈ R. Deﬁne id by id(x ⊗ θk) = x ⊗ C k
αeα, then id is a J 8
3 -module homo-
morphism satisfying d = id ◦ dDer which is clearly unique. □
Remark. Proposition 3 is very speciﬁc to the exceptional Jordan algebra
J 8
3 and is a direct consequence of the fact that J 8
3 is, as J 8
3 -module, the only
irreducible module. For instance if J is a ﬁnite-dimensional simple Euclidean
Jordan algebras of Theorem 2 which is distinct of R and of J 8
3 , the ﬁrst order
diﬀerential calculus (Ω 1
Der(J), d Der) is not universal since then there several
inequivalent irreducible J-modules and not only J itself. In all these cases
25
one has Ω 1
Der(J) = J ⊗ Der(J)∗ and Der( J) is a real compact form of a
classical simple Lie algebra. Furthermore all the classical simple Lie alg ebras
are realized in this way as Lie algebras of derivations of the ﬁnite-dime nsional
simple special Euclidean Jordan algebras.
5.3 Diﬀerential graded Jordan algebras
Let us deﬁne a diﬀerential graded Jordan algebra to be a N-graded algebra
Ω = ⊕n∈NΩ n
which is a Jordan superalgebra , (see e.g. in [29], [33]), for the induced Z/ 2Z
degree and which is equipped with a diﬀerential, that is with an antideriva-
tion d of degree 1 and of square 0.
Thus Ω is a graded-commutative algebra, that is one has
ab = (−1)|a‖b|ba ∈ Ω |a|+|b| (5.2)
for a ∈ Ω |a|, b ∈ Ω |b|, and one has the graded Jordan identity
(−1)|a‖c|[Lab, L c]gr + (−1)|b‖a|[Lbc, L a]gr + (−1)|c‖b|[Lca, L b]gr = 0 (5.3)
for a ∈ Ω |a|, b ∈ Ω |b|, c ∈ Ω |c| where La is the left-multiplication operator by
a ∈ Ω deﬁned by La(x) = ax for any x ∈ Ω and where [ •, •]gr denotes the
graded commutator
[A, B ]gr = AB − (−1)|a‖b|BA
for A of degree |a| and B of degree |b|. The diﬀerential d satisﬁes
d2 = 0
dΩ n ⊂ Ω n+1
for any n ∈ N, and the graded Leibniz rule
d(ab) = d(a)b + (−1)|a|ad(b)
for a ∈ Ω |a|, b ∈ Ω.
26
In the following the real unital diﬀerential graded Jordan algebras will be
our models for the “algebras of diﬀerential forms” on “quantum sp aces”.
Let J be a Jordan algebra. A diﬀerential graded Jordan algebra Ω =
⊕n≥0Ω n such that Ω 0 = J will be called a diﬀerential calculus over J.
5.4 Higher order derivation-based diﬀerential calculi
Let J be a unital Jordan algebra with center Z(J) and let Ω n
Der(J) be the
J-module of all n-Z(J)-linear antisymmetric mappings of Der( J) into J, that
is ω ∈ Ω n
Der(J) is a Z(J)-linear mapping
ω : ∧n
Z(J)Der(J) → J
of the n-th exterior power over Z(J) of the Z(J)-module Der( J) into J as
a Z(J)-module. Then Ω Der(J) = ⊕n≥0 Ω n
Der(J) is canonically a diﬀerential
graded Jordan algebra with diﬀerential given by the Chevalley-Eilenb erg for-
mula
dω (X0, · · · , X n) = ∑
0≤k≤n(−1)kXk ω (X0,
k
∨
· · ·, X n)
+ ∑
0≤r<s≤n(−1)r+s ω ([Xr, X s], X 0,
r
∨
· · ·
s
∨
· · ·, X n)
(5.4)
for ω ∈ Ω n
Der(J) and Xp ∈ Der(J). Thus Ω Der(J) is a diﬀerential calculus over
J which will be referred as the derivation-based diﬀerential calculus over J.
If J is a ﬁnite-dimensional simple Euclidean Jordan algebra, (i.e. one of
the list of Theorem 2), one has
Ω Der(J) = J ⊗ ∧Der(J)∗ (5.5)
where ∧Der(J)∗ is the exterior algebra of the dual of the ﬁnite-dimensional
real Lie algebra Der( J). In the case where J is the exceptional Jordan al-
gebra J 8
3 , this diﬀerential calculus is characterized by the following universal
property.
Proposition 4. Any homomorphism ϕ of unital Jordan algebra of J 8
3 into the
Jordan subalgebra Ω 0 of a unital diﬀerential graded Jordan algebra Ω = ⊕Ω n
has a unique extension ˜ϕ : Ω Der(J 8
3 ) → Ω as a homomorphism of diﬀerential
graded Jordan algebras.
27
Proof (sketch of). By using the fact that the J 8
3 -modules are of the form
J 8
3 ⊗ E for some vector spaces E and the deﬁnition of the N-graded Jordan
superalgebras, Formulae (5.2) and (5.9), it follows that any unital d iﬀeren-
tial graded Jordan algebra Ω = ⊕Ω n which contains J 8
3 as unital Jordan
subalgebra of Ω 0 is as algebra of the form
Ω = J 8
3 ⊗ Ω (0)
where Ω (0) = ⊕Ω n
(0) is an associative graded-commutative algebra (this gen-
eralizes a classical result in the non graded case). The proof follows then
from Proposition 3, from d2 = 0 with the graded Leibniz rule for d and from
the simplicity of J 8
3 . □
A more detailed proof will appear in a forthcoming paper.
Remark
. Notice that as Proposition 3, Proposition 4 is very speciﬁc to the
exceptional Jordan algebra J 8
3 .
As a consequence all diﬀerential calculus over J 8
3 which are generated as
diﬀerential graded Jordan algebra by J 8
3 are quotients of Ω Der(J 8
3 ), in partic-
ular among these, one has all the diﬀerential graded Jordan algebr as of the
form
Ω = J 8
3 ⊗ ∧g∗ (5.6)
where g is a Lie subalgebra of Der( J 8
3 ) = f4, the diﬀerential being the
Chevalley-Eilenberg diﬀerential ( g acting by derivations on J 8
3 ).
5.5 Diﬀerential calculi as A∞-algebras
Let A be a complex unital ∗-algebra and let Ω u(A) = ⊕n≥0Ω n
u(A) be the
universal diﬀerential calculus over A, [30]. It is shown in [40] (see also in
[14]) that there is a unique involution on Ω u(A) which extends the involution
of A for which it is a diﬀerential graded ∗-algebra. This means that one has
{
(αβ )∗ = (−1)abβ ∗α ∗
d(γ∗) = ( dγ)∗ (5.7)
for any α ∈ Ω a
u(A), β ∈ Ω b
u(A) and γ ∈ Ω u(A). The cohomology of Ω u(A)
is trivial, i.e. H n(Ω u(A)) = 0 for n ≥ 1 and H 0(Ω u(A)) = C, and in fact
28
by using a linear form ω on A such that ω (1 l) = 1, one constructs a linear
mapping K of degree -1 on Ω u(A) such that
dK + Kd = I (5.8)
on ⊕n≥1Ω n
u(A) (see in [14]). By replacing K by 1
2(K + K ∗) one can assume
that K(α ∗) = K(α )∗ for any α ∈ Ω u(A).
Let J = H(A) be the real Jordan algebra of the hermitian elements of A,
i.e. J = {h ∈ A|h∗ = h} endowed with the product
h ◦ h′ = 1
2 (hh′ + h′h)
for h, h ′ ∈ J. Then the real graded subspace Ω( J) of Ω u(A) of hermitian
elements is a real diﬀerential graded Jordan algebra, that is a diﬀer ential
calculus over J for the graded Jordan product deﬁned by
α ◦ β = 1
2 (αβ + (−1)abβα ) (5.9)
for α ∈ Ω a(J), β ∈ Ω b(J).
The contracting homotopy K restricts to Ω( J). By using K, one con-
structs by induction on n a sequence of product mn(α 1, · · · , α n) of respective
degrees 2 − n on Ω( J) starting with m1(α ) = dα and m2(α, β ) = α ◦ β such
that, endowed with these products, Ω( J) is an A∞-algebra [32]. This implies
in particular that the graded Jordan product α ◦ β of Ω( J) is associative up
to homotopy. In fact, by taking
m3(α, β, γ ) = K((α ◦ β ) ◦ γ − α ◦ (β ◦ γ)) (5.10)
for α ∈ Ω a(J), β ∈ Ω b(J), γ ∈ Ω c(J) with a + b + c ≥ 1, one gets
(α ◦ β ) ◦ γ − α ◦ (β ◦ γ) = d(m3)(α, β, γ )
i.e. the associativity up to homotopy of the graded Jordan product .
The occurrence of A∞-structures in the present context is not accidental.
For instance it will be shown in another paper that, for the simple ﬁnit e
dimensional Euclidean Jordan algebras of Theorem 2, the derivation -based
diﬀerential calculus admits such A∞-structures with m1 given by the diﬀer-
ential and m2 given by the graded Jordan product.
29
