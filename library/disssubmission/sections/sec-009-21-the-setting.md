---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-009-21-the-setting
section_title: "The setting"
section_number: 2.1
pages: 31-34
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
Let X be an abelian variety over an algebraically closed ﬁeld k which
has characteristic zero or is the algebraic closure of a ﬁnite ﬁeld. As in [10]
we consider the derived category Db
c (X,Λ) of complexes of Λ-sheaves with
bounded constructible cohomology sheaves, where Λ is either a subﬁeld
of Ql for some ﬁxed prime number l̸ = char(k) or a subﬁeld of C if we are
working over the base ﬁeld k = C. We denote by Perv(X,Λ) ⊂Db
c (X,Λ)
the full abelian subcategory of perverse sheaves as deﬁned in loc. cit., and
we write π1(X,0) for the ´etale fundamental group, resp. for the topological
fundamental group in the complex case. By a character χ : π1(X,0) −→Λ∗
we mean in the ´etale setting a continuous character with image in a ﬁnite
extension ﬁeld of Ql. Any such character deﬁnes a local system Lχ, and as
in the previous chapter we denote by Kχ = K ⊗Λ Lχ the corresponding twist
of a complex K ∈Db
c (X,Λ).
Our Tannakian proof of theorem 1.1 relies on the notion of convolution
of sheaf complexes. Let a : X ×X −→X denote the group law, and consider
the convolution product
∗:
Db
c (X,Λ)×Db
c (X,Λ) −→Db
c (X,Λ), K1 ∗K2 = Ra∗(K1 ⊠K2).
It has been shown in [106, sect. 2.1] that the category Db
c (X,Λ) equipped
with this convolution product is a symmetric monoidal category in the sense
of [73, sect. VII.7]. In other words, there exists a unit object 1 in Db
c (X,Λ)
23
24
Chapter 2 – Proof of the vanishing theorem(s)
such that we have natural unity constraints
K ∗1
∼=
←−K
∼=
−→1∗K
and natural commutativity and associativity constraints
SK,L : K ∗L
∼=
−→L∗K
and
AK,L,M : K ∗(L∗M)
∼=
−→(K ∗L)∗M
for all objects K,L,M in Db
c (X,Λ), and these constraints satisfy the usual
compatibilities, in particular the pentagon and hexagon axioms as well as
the symmetry property SL,K ◦SK,L = idK∗L. The commutativity constraint
is deﬁned as follows. The involution σ : X × X −→X × X,(x,y) 7→(y,x)
together with the usual commutativity constraint for the tensor product of
complexes induces a natural isomorphism K ⊠L ∼= σ∗(L ⊠K), and SK,L is
deﬁned by the following commutative diagram.
K ∗L
SK,L
/
ooooooooooo
ooooooooooo
L∗K
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
P
Ra∗(K ⊠L)
∼=
'N
N
N
N
N
N
N
N
N
N
N
Ra∗(L⊠K)
∼=
wooooooooooo
Ra∗(σ∗(L⊠K))
Ra∗(σ∗σ∗(L⊠K))
The deﬁnition of the associativity constrains AK,L,M is similar, and the unit
object 1 of the category Db
c (X,Λ) is the skyscraper sheaf δ0 of rank one with
support in the zero point of the abelian variety.
Furthermore, if we deﬁne the adjoint dual of a complex K ∈Db
c (X,Λ)
in terms of the Verdier dual D(K) by
K∨= (−idX)∗D(K),
then the symmetric monoidal category Db
c (X,Λ) has been shown in [105] to
be rigid in the following sense: We have natural evaluation and coevaluation
morphisms
evK : K∨∗K −→1
and
coevK : 1 −→K ∗K∨
such that the composite morphisms
K
coevK∗idK
/ (K ∗K∨)∗K
A−1
K,K∨,K
/ K ∗(K∨∗K)
idK∗evK
/ K
K∨idK∨∗coevK∨/ K∨∗(K ∗K∨)
AK∨,K,K∨
/ (K∨∗K)∗K∨
evK∗idK∨
/ K∨
are the identity morphisms. In passing we remark that every skyscraper
sheaf K = δx of rank one, supported in a point x ∈X(C), is an invertible
2.1. The setting
25
object in the sense that the morphism evK is an isomorphism. Over a base
ﬁeld k of characteristic zero every invertible object has this form, indeed
from the K¨unneth formula [7, exp. XVII, sect. 5.4]
H•(X,K ∗L) ∼= H•(X,K)⊗Λ H•(X,L)
one easily checks that every invertible object has Euler characteristic one,
so proposition 1.6 (b) applies. In what follows, if we want to stress the rigid
symmetric monoidal structure on Db
c (X,Λ) we write (Db
c (X,Λ),∗).
The most prominent examples of rigid symmetric monoidal categories
are the abelian categories (VectΛ,⊗) of ﬁnite-dimensional vector spaces and
more generally the abelian categories (RepΛ(G),⊗) of representations of
an afﬁne group scheme G over Λ. Indeed, at the heart of the Tannakian
formalism lies the fact that a rigid symmetric monoidal Λ-linear abelian
category (C,∗) with EndC(1) = Λ is of the form (RepΛ(G),⊗) provided
that it admits a ﬁbre functor, by which we mean a faithful exact Λ-linear
functor
ω :
(C,∗) −→(VectΛ,⊗)
which is a tensor functor ACU in the sense that it is compatible with the
symmetric monoidal structures on both sides [33, th. 2.11].
Now the Λ-linear rigid symmetric monoidal category Db
c (X,Λ) is not
an abelian category but only triangulated; on the other hand, its full abelian
subcategory Perv(X,Λ) does not inherit the structure of a rigid symmetric
monoidal category since in general the convolution of two perverse sheaves
is no longer perverse. However, for the full subcategory D ⊆Db
c (X,Λ) of all
direct sums of degree shifts of semisimple perverse sheaves, we will obtain
in section 2.4 by a general quotient construction due to Andr´e and Kahn [1]
a symmetric monoidal quotient category D which is indeed a semisimple
abelian category. Under the quotient morphism
D −→D
an sheaf complex K ∈D becomes isomorphic to zero in D iff all its simple
constituents have Euler characteristic zero. Over k = C the classiﬁcation
in proposition 1.6 shows that this is the case if and only if H•(X,Kχ) = 0
for most characters χ. Furthermore, via a characterization of semisimple
rigid symmetric Λ-linear abelian categories given by Deligne [30] we will
see in section 2.5 that the category D is a limit of representation categories
of reductive algebraic super groups over Λ.
It then turns out that the non-perversity of convolution products can be
controlled by central characters of these groups. This will imply via an
argument from representation theory that the semisimple perverse sheaves
deﬁne a full subcategory of D that is stable under convolution. So for any
semisimple perverse sheaf P and r ∈N the convolution powers P∗r split
26
Chapter 2 – Proof of the vanishing theorem(s)
by Gabber’s decomposition theorem into a sum of a perverse sheaf and a
complex Nr which is isomorphic to zero in the quotient category D. From
the K¨unneth isomorphism
H•(X,P∗r) ∼= (H•(X,P))⊗r
we will then deduce in lemma 2.11 the vanishing in theorem 1.1 for any
character χ with the property that H•(X,(Nr)χ) = 0 for some r > g. Indeed
the vanishing theorem is closely connected to the Tannakian property of the
above categories — for the rigid symmetric abelian subcategory C = ⟨P⟩
generated inside D by a semisimple perverse sheaf P, we will see later on
that the functor
ω :
C −→VectΛ,
K 7→H0(X,Kχ)
is a ﬁbre functor for any character χ with the property in theorem 1.1. As
a ﬁrst step in this direction, we will show in the next section that the twist
functor K 7→Kχ is a tensor functor ACU.
