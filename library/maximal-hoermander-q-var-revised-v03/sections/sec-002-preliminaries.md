---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hormander functional calculus and Schrodinger and wave maximal estimates"
section_id: sec-002-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 8-11
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
doc_brief: "q-variational Hormander functional calculus and Schrodinger and wave maximal estimates — 10 sections: Introduction; R-boundedness; Preliminaries"
---
In this section, we recall the notions on Banach space geometry and functional calculus that we
need in this paper. For the Hörmander functional calculus, we only need few facts that we will
use as an abstract blackbox in the remainder of the article.
2.1 R-boundedness
Deﬁnition 2.1Let X,Y be Banach spaces. We recall that a familyτ⊆B(X,Y ) is called
R-bounded, if for a sequence(εk)k of independent Rademacher random variables, taking the
value 1 and−1 with equal probability1
2, a constantC >0, anyn∈N, anyx1,...,xn∈X and
any T1,...,Tn∈τ, we have
E
‖‖‖‖‖
n∑
k=1
εkTkxk
‖‖‖‖‖
Y
⩽CE
‖‖‖‖‖
n∑
k=1
εkxk
‖‖‖‖‖
X
.
In this case, the inﬁmum over all admissibleC is denoted by theR-boundR(τ).
Remark 2.2 Clearly, R({T}) = ‖T‖B(X,Y ) if τ={T}is a singleton. In general, we have
R(τ) > supT∈τ‖T‖B(X,Y ) above. IfX and Y are (isomorphic to) Hilbert spaces, then a family
τ⊂B(X,Y ) isR-bounded if and only ifτis bounded, the latter meaning thatsupT∈τ‖T‖B(X,Y ) <
∞.
Deﬁnition 2.3LetX be a Banach space and(εn)n be a sequence of independent Rademacher
variables.
7
1. We say thatX has Pisier’s property(α) if there are constantsc1,c 2 > 0 such that for
any array(xn,k)N
n,k=1 in X,(ε′
k)k a second sequence of independent Rademacher variables
independent of(εn)n, and(ε′′
n,k)n,k a doubly indexed sequence of independent Rademacher
variables, the following equivalence holds:
c1EE′
‖‖‖‖‖‖
N∑
k,n=1
εnε′
kxn,k
‖‖‖‖‖‖
X
⩽ E′′
‖‖‖‖‖‖
N∑
k,n=1
ε′′
n,kxn,k
‖‖‖‖‖‖
X
⩽c2EE′
‖‖‖‖‖‖
N∑
k,n=1
εnε′
kxn,k
‖‖‖‖‖‖
X
.
2. Let p∈[1, 2] and q∈[2,∞]. We say thatX has typep if for some constantc >0 and
any sequence(xn)N
n=1 in X, we have
E
‖‖‖‖‖
N∑
n=1
εnxn
‖‖‖‖‖
X
⩽c
( N∑
n=1
‖xn‖p
( 1
p
.
In this case, we writetype (X) =p (not uniquely determined value). We say thatX has
cotypeq if for some constantc> 0 and any sequence(xn)N
n=1 in X, we have
( N∑
n=1
‖xn‖q
( 1
q
⩽cE
‖‖‖‖‖
N∑
n=1
εnxn
‖‖‖‖‖
X
.
In this case, we writecotype (X) =q (not uniquely determined value).
2.2 UMD lattices
In this article, UMD lattices, i.e. Banach lattices which enjoy the UMD property, play a
prevalent role. For a general treatment of Banach lattices and their geometric properties, we
refer the reader to [LTz, Chapter 1]. We recall now deﬁnitions and some useful properties. A
Banach spaceY is called UMD space if the Hilbert transform
H :Lp(R)→Lp(R), Hf(x) = lim
ϵ→0

|x−y|>ϵ
1
x−yf(y)dy
extends to a bounded operator onLp(R,Y ), for some (equivalently for all)1<p< ∞[HvNVW,
Theorem 5.1]. The importance of the UMD property in harmonic analysis was recognized
for the ﬁrst time by Burkholder [Bur81, Bur83], see also his survey [Bur01]. He settled a
geometric characterization via a convex functional [Bur81] and together with Bourgain [Bou83],
they showed that the UMD property can be expressed by boundedness ofY-valued martingale
sequences. A UMD space is super-reﬂexive [Al79], and hence (almost by deﬁnition) B-convex.
Recall that a Banach spaceX is called B-convex iﬀ for someϵ >0 and some natural number
n, it holds true that wheneverx1,...,xn are elements in the closed unit ball ofX, then there
is a choice of signsα1,...,αn∈{−1, 1}such that‖∑n
i=1αixi‖⩽ (1−ϵ)n. As a survey for
UMD lattices and their properties in connection with results in harmonic analysis, we refer the
reader to [RdF].
A Köthe function spaceY is a Banach lattice consisting of equivalence classes of locally
integrable functions on someσ-ﬁnite measure space(Ω′,µ′) with the additional properties
1. If f : Ω ′→C is measurable andg∈Y is such that|f(ω′)|⩽|g(ω′)|for almost every
ω′∈Ω′, thenf∈Y and‖f‖Y ⩽‖g‖Y.
8
2. The indicator function1A is inY wheneverµ′(A)<∞.
3. Moreover, we will assume thatY has theσ-Fatou property: if a sequence(fk)k of non-
negativefunctionsin Y satisﬁesfk(ω′)↗f(ω′)foralmostevery ω′∈Ω′and supk‖fk‖Y <
∞, thenf∈Y and‖f‖Y = limk‖fk‖Y.
Note that for example, anyLp(Ω′) space with 1 ⩽p ⩽∞is such a Köthe function space.
Lemma 2.4 Let Y be a UMD lattice. Then it has theσ-Levi property: any increasing and
norm-bounded sequence(xn)n in Y has a supremum inY. It also has the Fatou-property and
hence theσ-Fatou property. Note that if1<p< ∞and (Ω,µ) is aσ-ﬁnite measure space, then
Lp(Ω,Y ) is again a UMD lattice, so has the aboveσ-Levi andσ-Fatou properties.
Proof : Note that a UMD lattice is reﬂexive. Then we refer to [Lin, Proposition B.1.8].
Assumption 2.5 In the rest of the paper,Y = Y (Ω′) will always be a UMD space which is
also a Köthe function space, unless otherwise stated.
Deﬁnition 2.6We deﬁne
Λβ:= Λβ
2,2 := Λβ
2,2(R+) :={f : R+→C : f◦exp belongs toWβ
2 (R)},
whereWβ
2 (R) denotes the usual Sobolev space deﬁned e.g. via the Fourier transform. We equip
the space with the obvious norm‖f‖Λβ
2,2
:=‖f◦exp‖Wβ
2 (R). The space Λβ
2,2(R+) is a Hilbert
space and imbeds into the (non-UMD) latticeC0(R+) for β >1
2. Indeed, this follows from the
Sobolev embeddingWβ
2 (R),→C0(R) for β >1
2.
Let E be any Banach space. We can consider the vector valued latticeY (E) ={F : Ω′→
E : F is strongly measurable andω′↦→‖F (ω′)‖E ∈Y}with norm‖F‖Y (E) =
‖‖‖F (·)‖E
‖‖.
From [RdF, Corollary p. 214], we know that ifY is UMD and E is UMD, then alsoY (E)
is UMD. Moreover, we shall consider speciﬁcally in this article spacesLp(Ω,Y (E)), with e.g.
E = Λ βas above. For the natural identityLp(Ω,Y )(E) = Lp(Ω,Y (E)) guaranteed e.g. by
reﬂexivity ofY, we refer to [Lin, Sections B.2.1, B.2.2, Theorem B.2.7].
Remark 2.7 The Λβnorm is dilation and inversion invariant, that is, for anyf∈Λβand
t >0,‖f(t·)‖Λβ=‖f‖Λβand
‖‖‖f
(
1
(·)
{‖‖‖
Λβ
=‖f‖Λβ. Suppose f : R+→C is measurable and
has compact support inR+. Thenf belongs to Λβiﬀf belongs toWβ
2 (R) and in this case, we
have‖f‖Λβ∼=‖f‖Wβ
2 (R), where the equivalence constants depend on the compact support.
Proof : See [DK, Remark 2.7].
Lemma 2.8 LetY =Y (Ω′) be a UMD lattice and(ϵk)k an i.i.d. Rademacher sequence. Then
we have the norm equivalence
(2.1) E
‖‖‖‖
n∑
k=1
ϵkyk
‖‖‖‖
Y
∼=
‖‖‖‖
( n∑
k=1
|yk|2
{1
2
‖‖‖‖
Y
uniformly inn∈N. In particular, this also applies toLp(Ω,Y ), 1<p< ∞.
9
Proof : As Y is a UMD lattice, it is B-convex. The result thus follows from [Ma74]. For the
last sentence, we only need to recall thatLp(Ω,Y ) will also be a B-convex Banach lattice.
In the following, we will make use tacitly of the following Lemma 2.9.
Lemma 2.9 1. Let T : Y →Z be a bounded (linear) operator, whereY (Ω′) and Z(Ω′′)
are B-convex Banach lattices. Then its tensor extensionT⊗Id𝓁2, initially deﬁned on
Y (Ω′)⊗𝓁2⊂Y (Ω′,𝓁2) is again boundedY (Ω′,𝓁2)→Z(Ω′′,𝓁2).Also ifH is any Hilbert
space isometric to𝓁2, thenT⊗IdH extends to a bounded operatorY (Ω′,H )→Z(Ω′′,H ).
In particular, ifY (Ω′) is a UMD lattice, thenY (Ω′,𝓁2) is also a UMD lattice.
2. LetY (Ω′) be a B-convex Banach lattice andH a Hilbert space. ThentypeY (H) = typeY
and cotypeY (H) = cotypeY, where type∈(1, 2] and cotype∈[2,∞).
Proof : See [DK, Lemma 2.9]. In 1., for the boundedness ofT⊗IdH, it suﬃces to consider an
isometry Ψ : 𝓁2→H and to writeT⊗IdH = (IdZ⊗Ψ)(T⊗Id𝓁2)(IdY⊗Ψ−1) and to note that
IdZ⊗Ψ and IdY⊗Ψ−1 are again isometries.
The following lemma will be used in combination with Proposition 2.14 to follow.
Lemma 2.10 Let Y be a UMD lattice andp∈(1,∞). Then Lp(Ω,Y ) has Pisier’s property
(α).
Proof : Note thatLp(Ω,Y ) is a UMD lattice, so it has Pisier’s property(α), see [HvNVW2,
Proposition 7.5.4 and Theorem 7.5.20].
