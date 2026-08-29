---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-5
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — W e introduce “sheaﬁﬁcation” functors from categories of (l ax monoidal) linear functors to categories of quasi-coherent sheaves"
---
If G is an aﬃne group scheme over a ﬁeld k, classical Tannaka’s reconstruction problem
consists in reconstructing the group G from RepGk, its category of ﬁnite representations: if
F : RepGk − →Vectk is the forgetful functor then G is canonically isomorphic to the sheaf of
automorphisms of F (opportunely deﬁned, see [ DM82, Proposition 2.8]). More generally one can
recover the stack B G of G-torsors by looking at ﬁber functors. Given a ring A denote by Loc A
the category of locally free sheaves of ﬁnite rank over A, that is ﬁnitely generated projective A-
modules. If SMon G
k is the stack over k whose ﬁber over a k-algebraA is the category of k-linear,
strong monoidal and exact functors Γ : RepGk − →LocA then the functor
BG − →SMonG
k, (SpecA
s
− − →BG) ↦− →(s∗
| RepGk : RepGk − →LocA)(⋆)
is an equivalence of categories (see [ DM82, Theorem 3.2]). Here Rep Gk is thought of as the
category of locally free sheaves of ﬁnite rank on B G.
The above functor can be deﬁned in a way more general context. Let us introduce some
notations and deﬁnitions. We ﬁx a base commutative ring R and a category ﬁbered in groupoids
X overR. We say that X is pseudo-algebraic (resp. quasi-compact) if there exists a scheme (resp.
aﬃne scheme) X and a map X − → X representable by fpqc covering of algebraic spaces. We
denote by QCoh X and Loc X the categories of quasi-coherent sheaves and locally free s heaves
of ﬁnite rank respectively (see Section 1). Given a full subcategory C of QCoh X we say that C
generates QCoh X if all quasi-coherent sheaves on X are quotient of a (possibly inﬁnite) direct
sum of sheaves in C. We say that X satisﬁes (or has) the resolution property if Loc X generates
QCoh X .
Given a monoidal and additive full subcategory C of Loc X and a category ﬁbered in groupoids
Y over R deﬁne Fib X, C(Y) as the category of R-linear and strong monoidal functors Γ : C − →
Loc Y which are exact on right exact sequences in C (in the ambient abelian category QCoh X ).
Denote also by Fib X, C the stack over R whose ﬁber over an R-algebra A is Fib X, C(SpecA) and
by PC the functor
PC : X − → FibX, C, (SpecA
s
− − → X) ↦− →(s∗
|C : C − →LocA)
The functor (⋆) is obtained by taking R =k, X = BG and C = Loc X . We prove the following
non-neutral form of Tannaka’s reconstruction.
1
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 2
Theorem (5.3, 5.4). Let X be a quasi-compact stack over R for the fpqc topology with quasi-
aﬃne diagonal and C ⊆ Loc X be a full, additive and monoidal subcategory with duals gener ating
QCoh X .
If Γ : C − →ModA, whereA is anR-algebra, is an R-linear, contravariant and strong monoidal
functor such that Γ , as well as Γ ⊗Ak for all geometric points Speck − →SpecA, is left exact
on right exact sequences in C then there exists SpecA
s
− − → Xsuch that Γ ≃ (s∗)∨.
The functor PC : X − → FibX, C is an equivalence of stacks and, if Y is a category ﬁbered in
groupoids, the functor
Hom(Y, X ) − →FibX, C(Y), (Y
f
− − → X) ↦− →f ∗
|C : C − →Loc(Y)
is an equivalence of categories.
Notice that the two conclusions in the last statement are equ ivalent. In the case C = Loc X ,
the functor PLoc(X ) has already been proved to be an equivalence in the neutral ca se, that is
X = BRG, where G is a ﬂat and aﬃne group scheme over R (see [Bro13, Theorem 1.2], where R
is a Dedekind domain, and [ Sch13, Theorem 1.3.2] for general rings R), for particular quotient
stacks over a ﬁeld (see [ Sav06] and 5.12) and for quasi-compact and quasi-separated schemes (see
[BC12, Proposition 1.8]). We also show an almost converse of Theor em above:
Theorem. [5.7] Let X be a quasi-compact category ﬁbered in groupoids over R admitting a
surjective (on equivalence classes of geometric points) map X − → X from a scheme whose
connected components are open (e.g. a connected or Noetheria n algebraic stack) and let C ⊆
Loc X be a full monoidal subcategory with duals such that Symn E ∈ C for n ∈ N and E ∈ C if
E has local rank not invertible in R (e.g. C = Loc(X ) or C consists of invertible sheaves). Then
FibX, C is a quasi-compact stack in groupoids for the fpqc topology o ver R with aﬃne diagonal
and with a collection of tautological locally free sheaves {GE }E∈C generating QCoh(FibX, C) and
such that P ∗
CGE ≃ E .
For instance it follows that X − → FibX, Loc(X ) is universal among the maps w : X − → Y where
Y is a quasi-compact stack over R with quasi-aﬃne diagonal and the resolution property.
There are also variants of theory above where Loc (−) is replaced by Coh(−) or QCoh(−) or the
derived category D(−) (see [Lur04, Sch12, BC12, Bra14, Bha14]). Although not explicitly stated
elsewhere, for stacks with the resolution property and with aﬃne diagonal (which is automatic
in the algebraic case, see [ Tot04]) those results and the fact that PLoc(X ) is an equivalence can
be proved to be equivalent: one can pass from quasi-coherent sheaves to locally free sheaves via
dualizable objects and, for the converse, extend functors f rom Loc (−) to QCoh (−) following the
proof of [Bha14, Corollary 3.2]. We complete this picture by showing that in general the resolution
property implies the aﬃneness of the diagonal (see 5.13). One of the ingredients in the proof is
the classiﬁcation of quasi-compact stacks whose quasi-coh erent sheaves are generated by global
sections, called pseudo-aﬃne. In the algebraic case those c oincide with quasi-aﬃne schemes
(see [ Gro13, Proposition 3.1]), while, in general, we prove they are (ar bitrary) intersection of
quasi-compact open subschemes (thought of as sheaves) of aﬃ ne schemes (see 5.6).
The proof of Tannaka’s reconstruction we present does not re duce to the case of quasi-coherent
sheaves as explained above but it follows a diﬀerent path. It is obtained by developing a theory
of sheaﬁﬁcation functors which I think is interesting on its own and it is the heart of the paper.
In what follows A will denote an R-algebra, X a category ﬁbered in groupoids over R and C a
full subcategory of QCoh X . The idea is simple: if s : SpecA − → X is a map (say quasi-aﬃne
so that s∗ preserves quasi-coherency) then we have natural isomorphi sms of A-modules
s∗E ≃ HomA(s∗E ∨,A ) ≃ HomX (E ∨,s ∗OSpecA)
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 3
By passing from covariant functors to contravariant ones we can always deﬁne
Ω F : C − →ModA, Ω F
E = HomX (E, F ) for F ∈ QCoh(X × A)
which are R-linear contravariant functors. If L R(C,A ) is the category of contravariant R-linear
functors C − →ModA we obtain a functor
Ω ∗ : QCoh(X × A) − →LR(C,A )
Quite surprisingly (since we started from group schemes as m otivation) we recover also this well
known situation (see 2.2 for details). If X is a quasi-projective and quasi-compact scheme over R
with very ample invertible sheaf OX (1) consider CX = {OX (n)}n∈Z, set SX for the homogeneous
coordinate ring of (X, OX (1)) and use GMod (−) to denote the category of graded modules. We
have that LR(CX,A ) is equivalent to GMod (SX ⊗RA) and Ω ∗ corresponds to
Γ ∗ : QCoh(X ×A) − →GMod(SX ⊗RA), Γ ∗(F ) =
⨁
n∈Z
H0(X, F (n))
It is a classical result, at least over a ﬁeld, that the above f unctor is fully faithful. Thus in general
we can ask under what conditions the functor Ω ∗ : QCoh(X × A) − →LR(C,A ) is fully faithful
as well. Another property that the functor Γ ∗ has is the existence of a left adjoint, namely the
homogeneous sheaﬁﬁcation functor ~− : GMod(SX ⊗RA) − →QCoh(X ×A). It turns out that
also Ω ∗ : QCoh(X × A) − →LR(C,A ) has a left adjoint F∗, C : LR(C,A ) − →QCoh(X × A) when
C is essentially small: by analogy we call this functor a sheaﬁﬁcation functor.
In the context of Tannaka’s reconstruction we also have that sheaves of algebras correspond
to (lax) monoidal functors Loc GR − → ModA. This is true in general. If C is a monoidal
subcategory of QCoh X , MLR(C,A ) denotes the category of R-linear, contravariant and monoidal
functors C − → ModA and QAlg (X × A) the category of quasi-coherent sheaves of algebras on
X then Ω ∗ extends to a functor Ω ∗ : QAlg(X × A) − →MLR(C,A ) and, if C is essentially small,
F∗, C extends to A∗, C : MLR(C,A ) − →QAlg(X × A), which is still a left adjoint of Ω ∗.
Coming back to the fully faithfulness of Ω ∗ we prove the following.
Theorem (3.12,3.18). Let X be a pseudo-algebraic category ﬁbered in groupoids over R and
C ⊆ QCoh X be a full subcategory generating QCoh X . Then the functor Ω ∗ : QCoh(X ×A) − →
LR(C,A ) is fully faithful and, if C is essentially small, then F∗, C : LR(C,A ) − →QCoh(X × A) is
exact and the natural map G − → FΩ G, C is an isomorphism.
If X is quasi-projective then it is a classical fact that CX = {OX (n)}n∈Z generates QCoh X
and thus we recover the classical properties of Γ ∗ : QCoh(X ×A) − →GMod(SX ⊗RA). Theorem
above when C consists of a single object is a rephrasing of classical Gabr iel-Popescu’s theorem
for the category QCoh X (see 3.19). When C is monoidal and generates QCoh X we also have
that Ω ∗ : QAlg(X × A) − →MLR(C,A ) is fully faithful (see 3.34).
The second problem we address is to describe the essential im age of Ω ∗. The main idea behind
this description is that Hom X (−, F ) for F ∈ QCoh X is a left exact functor. Since the domain
C of the functors Ω F is not abelian we need an ad hoc deﬁnition of exactness. A test sequence
in C is an exact sequence
T∗ :
⨁
k∈K
Ek
α
− − →
⨁
i∈I
Ei − → E − →0 where E, Ei, Ek ∈ C and I,J are sets
such that α(Ek) is contained in a ﬁnite sum for all k ∈ K. A test sequence is called ﬁnite if K
and I are ﬁnite sets. Given Γ ∈ LR(C,A ) we will say that Γ is exact on a test sequence T∗ in C
if the complex of A-modules (see 3.9)
0 − →Γ E − →
∏
i∈I
Γ Ei − →
∏
k∈K
Γ Ek
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 4
is exact. We denote by Lex R(C,A ) the full subcategory of L R(C,A ) of functors which are exact
an all test sequences. We have the following:
Theorem (3.18, 3.26). Let X be a pseudo-algebraic category ﬁbered in groupoids over R and
C ⊆ QCoh X be a full subcategory generating QCoh X . Then LexR(C,A ) is the essential image
of the (fully faithful) functor Ω ∗ : QCoh(X × A) − →LR(C,A ). If X is quasi-compact and all
sheaves in C are ﬁnitely presented then LexR(C,A ) is the subcategory of LR(C,A ) of functors
which are exact on ﬁnite test sequences.
In particular, when C is essentially small, Ω ∗ : QCoh(X ×A) − →LexR(C,A ) and F∗, C : LexR(C,A ) − →
QCoh(X × A) are quasi-inverses of each other. The two theorems above app ly in the following
situations (see 3.29, 3.30 and 3.31): if C = QCoh X then LexR(QCoh X,A ) is the category of
contraviant,R-linear and left exact functors QCoh X − → ModA which transform direct sums
into products, if C = Coh(X ) (resp. C = Loc(X )) and X is a notherian algebraic stack (resp. X
is quasi-compact and has the resolution property) then Lex R(C,A ) is the category of contraviant,
R-linear and left exact functors C − →ModA.
When C is essentially small there is another cohomological charac terization of the functors
in LexR(C,A ). A collection of maps U = {Ei − → E} in C is called jointly surjective if the map⨁
i∈I Ei − → E is surjective. Given such a collection U we set ∆ U = Im(⨁
i∈I Ω Ei − →Ω E ) ∈
LR(C,R ). Denote by C⊕ the subcategory of QCoh X consisting of all possible ﬁnite direct sums
of sheaves in C. We have:
Theorem (3.24, 3.26 and 3.28). Let X be a pseudo-algebraic category ﬁbered in groupoids over R
and C ⊆ QCoh X be a full and essentially small subcategory generating QCoh X . Then LexR(C,A )
is the full subcategory of LR(C,A ) of functors Γ satisfying
HomLR(C,R )(Ω E/∆ U, Γ) = Ext1
LR(C,R )(Ω E/∆ U, Γ) = 0
for all jointly surjective collections of maps U = {Ei − → E}i∈I in C. If X is quasi-compact and
the sheaves in C are ﬁnitely presented we can consider only ﬁnite collection s U.
We have LexR(C⊕,A ) ≃ LexR(C,A ) via the restriction C − → C ⊕ and, if C is additive and
J is the smallest Grothendieck topology on C containing the sieves ∆ U for all jointly surjective
collections U = {Ei − → E}i∈I in C, then LexR(C,A ) coincides with the category of sheaves of
A-modules Cop − →ModA on the site (C, J ) which are R-linear.
Besides Tannaka’s reconstruction problem, theory above ha s two other applications. The ﬁrst,
which is also the original motivation, is the theory of Galoi s cover. More precisely in my Ph.D.
thesis [ Ton13b] I have worked out theory above in the case X = BG and C = Loc X , where G is
a ﬁnite, ﬂat and ﬁnitely presented group scheme over R. Notice that B G satisﬁes the resolution
property in this case (see 4.3). The proof presented in [ Ton13b] makes use of representation
theory and can not be generalized to arbitrary categories ﬁb ered in groupoids. The goal was to
look at Galois covers with group G as particular monoidal functors, as G-torsors can be thought
of as particular strong monoidal functors, and the motivati on was the study of non-abelian Galois
covers, where a direct approach as in the abelian case (see [ Ton13a]) fails due to the complexity
of the representation theory.
A second application is to the theory of Cox rings and homogen eous sheaﬁﬁcations. The idea
is to consider CH = {L}L∈H ⊆ Loc X whereH is a subgroup of Pic X . As in the projective case
we have a homogeneous coordinate ring
SH =
⨁
L∈H
H0(X, L)
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 5
(opportunely deﬁned), L R(CH,A ) is equivalent to GMod (SH ⊗RA), the category of H-graded
(SH ⊗RA)-modules, Ω ∗ corresponds to
Γ ∗ : QCoh(X × A) − →GMod(SH ⊗RA), Γ ∗(F ) =
⨁
L∈H
H0(X, F ⊗ L )
and its adjoint F∗, CH behaves like a homogeneous sheaﬁﬁcation. Moreover in more c oncrete
geometric situations, e.g. when X is a normal variety, there are analogous constructions for
reﬂexive sheaves of rank 1. We expect that this theory covers all known cases where Γ ∗ is proved
to be fully faithful (see for instance [ CLS11, Appendix of Chapter 6] and [ Kaj98, Section 2]).
Applications above are not described in the present paper, b ut, hopefully, they will be subjects
of future ones.
The outline of the paper is the following. The ﬁrst section in troduces the notion and the basic
properties of quasi-coherent sheaves on ﬁbered categories , while the second one is a general study
of sheaﬁﬁcation functors. In the third section we study the f ully faithfulness and the essential
image of the functor Ω ∗ : QCoh(X × A) − →LR(C,A ). In the fourth section we rewrite the
results obtained in the case of the stack of G-torsor in terms of the representation theory of G
and ﬁnally, in the last section, we prove the non-neutral Tan naka’s reconstruction.
