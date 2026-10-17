---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-002-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 8-11
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 11 sections: Front matter; Introduction; R-boundedness"
---
Preliminaries
In this section, we recall the notions on Banach space geometry and functional calculus that we
need in this paper. For the Hörmander functional calculus, we only need few facts that we will
use as an abstract blackbox in the remainder of the article.
2.1
R-boundedness
Deﬁnition 2.1 Let X, Y be Banach spaces. We recall that a family τ ⊆B(X, Y ) is called
R-bounded, if for a sequence (εk)k of independent Rademacher random variables, taking the
value 1 and −1 with equal probability 1
2, a constant C > 0, any n ∈N, any x1, . . . , xn ∈X and
any T1, . . . , Tn ∈τ, we have
E

n
X
k=1
εkTkxk

Y
⩽CE

n
X
k=1
εkxk

X
.
In this case, the inﬁmum over all admissible C is denoted by the R-bound R(τ).
Remark 2.2 Clearly, R({T}) = ∥T∥B(X,Y ) if τ = {T} is a singleton. In general, we have
R(τ) ⩾supT ∈τ ∥T∥B(X,Y ) above. If X and Y are (isomorphic to) Hilbert spaces, then a family
τ ⊂B(X, Y ) is R-bounded if and only if τ is bounded, the latter meaning that supT ∈τ ∥T∥B(X,Y ) <
∞.
Deﬁnition 2.3 Let X be a Banach space and (εn)n be a sequence of independent Rademacher
variables.
7
1. We say that X has Pisier’s property (α) if there are constants c1, c2 > 0 such that for
any array (xn,k)N
n,k=1 in X,(ε′
k)k a second sequence of independent Rademacher variables
independent of (εn)n, and (ε′′
n,k)n,k a doubly indexed sequence of independent Rademacher
variables, the following equivalence holds:
c1EE′

N
X
k,n=1
εnε′
kxn,k

X
⩽E′′

N
X
k,n=1
ε′′
n,kxn,k

X
⩽c2EE′

N
X
k,n=1
εnε′
kxn,k

X
.
2. Let p ∈[1, 2] and q ∈[2, ∞]. We say that X has type p if for some constant c > 0 and
any sequence (xn)N
n=1 in X, we have
E

N
X
n=1
εnxn

X
⩽c
 N
X
n=1
∥xn∥p
! 1
p
.
In this case, we write type (X) = p (not uniquely determined value). We say that X has
cotype q if for some constant c > 0 and any sequence (xn)N
n=1 in X, we have
 N
X
n=1
∥xn∥q
! 1
q
⩽cE

N
X
n=1
εnxn

X
.
In this case, we write cotype (X) = q (not uniquely determined value).
2.2
UMD lattices
In this article, UMD lattices, i.e.
Banach lattices which enjoy the UMD property, play a
prevalent role. For a general treatment of Banach lattices and their geometric properties, we
refer the reader to [LTz, Chapter 1]. We recall now deﬁnitions and some useful properties. A
Banach space Y is called UMD space if the Hilbert transform
H : Lp(R) →Lp(R), Hf(x) = lim
ϵ→0
Z
|x−y|⩾ϵ
1
x −y f(y) dy
extends to a bounded operator on Lp(R, Y ), for some (equivalently for all) 1 < p < ∞[HvNVW,
Theorem 5.1].
The importance of the UMD property in harmonic analysis was recognized
for the ﬁrst time by Burkholder [Bur81, Bur83], see also his survey [Bur01].
He settled a
geometric characterization via a convex functional [Bur81] and together with Bourgain [Bou83],
they showed that the UMD property can be expressed by boundedness of Y -valued martingale
sequences. A UMD space is super-reﬂexive [Al79], and hence (almost by deﬁnition) B-convex.
Recall that a Banach space X is called B-convex iﬀfor some ϵ > 0 and some natural number
n, it holds true that whenever x1, . . . , xn are elements in the closed unit ball of X, then there
is a choice of signs α1, . . . , αn ∈{−1, 1} such that ∥Pn
i=1 αixi∥⩽(1 −ϵ)n. As a survey for
UMD lattices and their properties in connection with results in harmonic analysis, we refer the
reader to [RdF].
A Köthe function space Y is a Banach lattice consisting of equivalence classes of locally
integrable functions on some σ-ﬁnite measure space (Ω′, µ′) with the additional properties
1. If f : Ω′ →C is measurable and g ∈Y is such that |f(ω′)| ⩽|g(ω′)| for almost every
ω′ ∈Ω′, then f ∈Y and ∥f∥Y ⩽∥g∥Y .
8
2. The indicator function 1A is in Y whenever µ′(A) < ∞.
3. Moreover, we will assume that Y has the σ-Fatou property: if a sequence (fk)k of non-
negative functions in Y satisﬁes fk(ω′) ↗f(ω′) for almost every ω′ ∈Ω′ and supk ∥fk∥Y <
∞, then f ∈Y and ∥f∥Y = limk ∥fk∥Y .
Note that for example, any Lp(Ω′) space with 1 ⩽p ⩽∞is such a Köthe function space.
Lemma 2.4 Let Y be a UMD lattice. Then it has the σ-Levi property: any increasing and
norm-bounded sequence (xn)n in Y has a supremum in Y . It also has the Fatou-property and
hence the σ-Fatou property. Note that if 1 < p < ∞and (Ω, µ) is a σ-ﬁnite measure space, then
Lp(Ω, Y ) is again a UMD lattice, so has the above σ-Levi and σ-Fatou properties.
Proof : Note that a UMD lattice is reﬂexive. Then we refer to [Lin, Proposition B.1.8].
Assumption 2.5 In the rest of the paper, Y = Y (Ω′) will always be a UMD space which is
also a Köthe function space, unless otherwise stated.
Deﬁnition 2.6 We deﬁne
Λβ := Λβ
2,2 := Λβ
2,2(R+) := {f : R+ →C : f ◦exp belongs to W β
2 (R)},
where W β
2 (R) denotes the usual Sobolev space deﬁned e.g. via the Fourier transform. We equip
the space with the obvious norm ∥f∥Λβ
2,2 := ∥f ◦exp ∥W β
2 (R). The space Λβ
2,2(R+) is a Hilbert
space and imbeds into the (non-UMD) lattice C0(R+) for β > 1
2. Indeed, this follows from the
Sobolev embedding W β
2 (R) ,→C0(R) for β > 1
2.
Let E be any Banach space. We can consider the vector valued lattice Y (E) = {F : Ω′ →
E : F is strongly measurable and ω′ 7→∥F(ω′)∥E ∈Y } with norm ∥F∥Y (E) =

∥F(·)∥E

.
From [RdF, Corollary p. 214], we know that if Y is UMD and E is UMD, then also Y (E)
is UMD. Moreover, we shall consider speciﬁcally in this article spaces Lp(Ω, Y (E)), with e.g.
E = Λβ as above. For the natural identity Lp(Ω, Y )(E) = Lp(Ω, Y (E)) guaranteed e.g. by
reﬂexivity of Y , we refer to [Lin, Sections B.2.1, B.2.2, Theorem B.2.7].
Remark 2.7 The Λβ norm is dilation and inversion invariant, that is, for any f ∈Λβ and
t > 0, ∥f(t·)∥Λβ = ∥f∥Λβ and

f

1
(·)


Λβ = ∥f∥Λβ. Suppose f : R+ →C is measurable and
has compact support in R+. Then f belongs to Λβ iﬀf belongs to W β
2 (R) and in this case, we
have ∥f∥Λβ ∼= ∥f∥W β
2 (R), where the equivalence constants depend on the compact support.
Proof : See [DK, Remark 2.7].
Lemma 2.8 Let Y = Y (Ω′) be a UMD lattice and (ϵk)k an i.i.d. Rademacher sequence. Then
we have the norm equivalence
(2.1)
E

n
X
k=1
ϵkyk

Y
∼=

 n
X
k=1
|yk|2 1
2 

Y
uniformly in n ∈N. In particular, this also applies to Lp(Ω, Y ), 1 < p < ∞.
9
Proof : As Y is a UMD lattice, it is B-convex. The result thus follows from [Ma74]. For the
last sentence, we only need to recall that Lp(Ω, Y ) will also be a B-convex Banach lattice.
In the following, we will make use tacitly of the following Lemma 2.9.
Lemma 2.9
1. Let T : Y →Z be a bounded (linear) operator, where Y (Ω′) and Z(Ω′′)
are B-convex Banach lattices. Then its tensor extension T ⊗Idℓ2, initially deﬁned on
Y (Ω′) ⊗ℓ2 ⊂Y (Ω′, ℓ2) is again bounded Y (Ω′, ℓ2) →Z(Ω′′, ℓ2). Also if H is any Hilbert
space isometric to ℓ2, then T ⊗IdH extends to a bounded operator Y (Ω′, H) →Z(Ω′′, H).
In particular, if Y (Ω′) is a UMD lattice, then Y (Ω′, ℓ2) is also a UMD lattice.
2. Let Y (Ω′) be a B-convex Banach lattice and H a Hilbert space. Then type Y (H) = type Y
and cotype Y (H) = cotype Y , where type ∈(1, 2] and cotype ∈[2, ∞).
Proof : See [DK, Lemma 2.9]. In 1., for the boundedness of T ⊗IdH, it suﬃces to consider an
isometry Ψ : ℓ2 →H and to write T ⊗IdH = (IdZ ⊗Ψ)(T ⊗Idℓ2)(IdY ⊗Ψ−1) and to note that
IdZ ⊗Ψ and IdY ⊗Ψ−1 are again isometries.
The following lemma will be used in combination with Proposition 2.14 to follow.
Lemma 2.10 Let Y be a UMD lattice and p ∈(1, ∞). Then Lp(Ω, Y ) has Pisier’s property
(α).
Proof : Note that Lp(Ω, Y ) is a UMD lattice, so it has Pisier’s property (α), see [HvNVW2,
Proposition 7.5.4 and Theorem 7.5.20].
