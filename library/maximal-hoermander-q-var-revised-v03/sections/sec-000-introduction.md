---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-8
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
doc_brief: "HAL Id: hal-04526930 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 10 sections: Introduction"
---
2 Preliminaries 7
2.1 R-boundedness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 UMD lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Abstract Hörmander functional calculus . . . . . . . . . . . . . . . . . . . . . . . 10
Mathematics subject classiﬁcation:42A45, 42B25, 47A60.
Key words: Spectral multiplier theorems, UMD valuedLp spaces, maximal estimates.
1
3 q-variational inequalities 12
4 q-variation for spherical and euclidean ball means inRd 15
5 Schrödinger and wave maximal estimates 20
6 Pointwise continuity of time paths for abstract Schrödinger and wave equa-
tions 27
7 Examples and concluding remarks 34
8 Acknowledgments 35
1 Introduction
This article is a follow-up of our work [DK] concerning maximal estimates for Hörmander
spectral multipliers onLp spaces and UMD lattices. Let us recall the setting in the context
of the euclidean Laplacian which provides in fact the leading example for what follows. The
operator−∆ (deﬁned e.g. as Fourier multiplier with symbol|ξ|2) is a self-adjoint operator on
L2(Rd). As such, it has a functional calculus allowing to insert it into a bounded Borel function
m : R+ →C and to obtain a bounded operatorm(−∆) on L2(Rd). Then one can ask for
which functions, the operatorm(−∆) is bounded onLp(Rd) for ﬁxed1<p< ∞. Hörmander’s
theorem [Hor, Theorem 2.5], based on Mihlin’s work [Mi56] gives the suﬃcient condition
(1.1) ‖m‖2
Hα
2
:= max
k=0,1,...,α
sup
R>0
1
R
 2R
R
⏐⏐⏐tk dk
dtkm(t)
⏐⏐⏐
2
dt< ∞,
whereαis an integer strictly larger thand
2. Later on, Hörmander’s theorem has been strength-
ened to the following maximal estimate:
(1.2)
‖‖‖‖sup
t>0
|m(−t∆)f|
‖‖‖‖
Lp(Rd)
⩽C‖f‖Lp(Rd).
This cannot hold true for all functionsm with‖m‖Hα
2
<∞[CGHS] even for large values ofα,
so that one has to restrict to a subclass of spectral multipliers for which (1.2) holds. Admissible
spectral multipliers typically have to have a somewhat higher order of diﬀerentiability than
α >d
2 and to decay at∞in a prescribed order. Early results for the euclidean Laplacian are
due to [Crb, DaTr, RdF2, See].
Hörmander’s classical and paramount result (1.1) of Fourier multipliers has found many
generalizations over the last 60 years. First, we will use in this article also a version for non-
integerα, in which (1.1) is replaced by a Sobolev norm. Second, theLp-boundedness question
makes literally sense for any self-adjoint operatorA, and in fact, a theorem of Hörmander type
holds true for many elliptic diﬀerential operatorsA, including sub-Laplacians on Lie groups
of polynomial growth, Schrödinger operators and elliptic operators on Riemannian manifolds,
see [Alex, Christ, Duong, DuOS]. More recently, spectral multipliers have been studied for
operators acting on Lp(Ω) only for a strict subset of (1,∞) of exponents p [Bl, CDY, CO,
COSY, KuUhl, KU2, SYY]. Third, another generalization of spectral multipliers is to bring
a UMD Banach spaceY into the picture and ask for the boundedness ofm(A)⊗IdY on the
Bochner spaceLp(Ω,Y ). In the case of euclidean LaplacianA =−∆ , this has been developed
by Hytönen [Hy1, Hy2] and Girardi and Weis [GiWe], and in the case of self-adjoint semigroups
2
admitting (generalised) Gaussian estimates, withY a UMD lattice, by Kemppainen and the
authors [DKK]. Fourth, in view of (1.2), one can ask whether the following maximal estimate
holds true:
(1.3)
‖‖‖‖sup
t>0
|m(tA)f|
‖‖‖‖
Lp(Ω,Y )
⩽C‖f‖Lp(Ω,Y ),
and for which functionsm : R+→C.
In this work as in its predecessor [DK], we considerA to ﬁt into the following quite general
framework of semigroup generators, which captures all the situations above. That is, we assume
thatA generates ac0-semigroup onLp(Ω,Y ) whereY is a UMD Banach lattice (which englobes
the two important particular casesY = CandA =A0⊗IdY for some semigroup generatorA0 on
Lp(Ω), for which the results in this article are already new). Moreover, we assume the semigroup
to be analytic onC+, so thatA is assumed0-sectorial, thus allowing the machinery ofH∞(Σω)
calculus for any angleω∈(0,π). Finally, we assume that thisH∞(Σω) calculus ofA extends
a priori to aHα
2 calculus on Lp(Ω,Y ). All these assumptions are satisﬁed for (diﬀerential)
operators on doubling manifolds that are self-adjoint and have (generalised) Gaussian estimates,
withY = C and also withA =A0⊗IdY for general UMD latticesY in case that(Tt)t is lattice
positive or regular contractive. This englobes:
1. TheheatsemigrouponacompleteRiemannianmanifoldwithnon-negativeRiccicurvature
[LY], [GriTel, p. 3/70 (1.3)], [Sal], [Fen, Theorem 4.2.1 & p. 45], [DKK, Proposition 4.8].
2. SchrödingeroperatorsonconnectedandcompleteRiemannianmanifoldswithnon-negative
Ricci curvature and locally integrable, positive potential [DuOS, Section 7.4, (7.8)], [DKK,
Proposition 4.8].
3. Other Schrödinger and elliptic diﬀerential operators acting onL2(Ω), where Ω ⊆Rd is
an open subset of homogeneous type [Ouh06], [Ouh, Section 6.4, in particular Theorems
6.10, 6.11].
4. Sub-laplacians on Lie groups with polynomial volume growth [Sal, Theorem 4.2, Example
2], [Gri], [DKK, Corollary 4.9].
5. Heat semigroups on fractals [GriTel, (1.4)], [DuOS, Section 7.11].
6. For a discussion of many further examples, we refer to [DuOS, Section 7], see also [DKK,
Subsection 5.1].
We refer to [DK, Section 4] for further examples of operatorsA and to Section 7 for relevant
UMD lattices other thanLp spaces. This section contains also an example of a non-selfadjoint
operator A which still has aHα
2 calculus on L2(Ω) and on Lp(Ω). Then the following main
result from [DK, Theorem 1.1] gives a suﬃcient condition for (1.3).
Theorem 1.1 ([DK])Let Y = Y (Ω′) be a UMD lattice, 1 < p <∞and (Ω,µ) a σ-ﬁnite
measure space. LetA be a 0-sectorial operator onLp(Y ). Assume that A has aHα
2 calculus
on Lp(Y ) for some α >1
2. Let m ∈Wc
2 (R) be a spectral multiplier withm(0) = 0 and
c>α+ max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 1 such that
(1.4)
∑
n∈Z
‖m(2n·)ϕ0‖Wc
2 (R) <∞
3
for some ϕ0 ∈C∞
c (0,∞) with ϕ0(t) = 1 for t ∈(1, 2). Then for a.e. (x,ω) ∈Ω×Ω′,
t↦→m(tA)f(x,ω) belongs toC0(R+) and
(1.5) ‖sup
t>0
|m(tA)f|‖Lp(Y ) ≲
∑
n∈Z
‖m(2n·)ϕ0‖Wc
2 (R)‖f‖Lp(Y ).
In this article, we extend the above maximal estimate in two ways. First, we replace the
supremum by theq-variation norm.
Deﬁnition 1.2Letq∈[1,∞]. For a functiona : R+→C, we deﬁne theq-variation
‖a‖Vq = sup

}

(
|at0|q +
∞∑
k=1
|atk−atk−1|q
( 1
q


{,
where the supremum runs over all increasing sequences(tk)k∈N in R+. In case ofq =∞, the
∞-variation is the usual maximal function. Then the spaceVq consisting of all functions with
ﬁniteq-variation is a Banach space [LMX, Section 1].
Note thatVq ,→L∞(R+) [BLCS, Proposition 5]. Then our ﬁrst main result reads as follows.
Theorem 1.3 (See Theorem 3.3)Assume thatA and m satisfy the hypotheses of Theorem
1.1 above. Letq >2. Then
‖‖t↦→m(tA)f‖Vq‖Lp(Y ) ≲‖f‖Lp(Y ).
This theorem provides an abstract framework for results for the euclidean Laplacian and
Laplace type operators, and shows aq-variational estimate only out of Hörmander calculus.
This seems to the best of our knowledge to be the ﬁrst result onq-variation of general spectral
multipliers, even in the caseA =−∆ . We refer to Theorem 3.3 for the more general statement
allowing for m(0)⁄= 0. We hereby generalise recent results of [LMX] (in case thatA = A0
generates a positive contractive semigroup onLp(Ω, C)), [HoMa1, HoMa2] (in case thatA =
A0⊗IdY on Lp(Ω,Y ) generates an analytic contractively regular semigroup) and of [BMSW,
HHL] (in case thatA = (−∆)
1
2 is the square root of the euclidean laplacian), from the speciﬁc
function m(λ) =e−λto other spectral multipliers.
One such spectral multiplier ism(λ) = 2π
|λ|
d−2
2
Jd−2
2
(2πλ) (see (4.7)) that represents in the
case of the euclidean LaplacianA =−∆ on Lp(Rd,Y ) the spherical mean
m(−t∆)f =Atf = 1
|Sd|

Sd
f(x−ty)dσ(y),
where Sd ={y∈Rd : |y|= 1}is the euclidean unit sphere equipped with surface measureσ.
We then obtain, hereby extending the result [JSW, Theorem 1.4(i)] from the scalar caseY = C
to the UMD lattice case:
Theorem 1.4 (see Theorem 4.2)Let 1 < p <∞and 2 < q <∞. There exists a minimal
dimension d0∈N depending onp and the geometry ofY such that for anyd > d0, there is
Cp,q,d,Y <∞such that for anyf∈S(Rd)⊗Y, we have
(1.6) ‖‖t↦→Atf‖Vq‖Lp(Rd,Y ) ⩽Cp,q,d,Y‖f‖Lp(Rd,Y ).
4
Note that a certain minimal dimension in (1.6) is known to be necessary even in the scalar
case [JSW, Theorem 1.4(i)]. Then by the method of rotation, we partly recover also a very
recent estimate from [HHL, Theorem 1.1], namely
(1.7) ‖‖t↦→Mtf‖Vq‖Lp(Rd,Y ) ⩽Cp,q,Y‖f‖Lp(Rd,Y )
for the usual euclidean ball meanMtf(x) = 1
|Bd|

Bd
f(x−ty)dy and from the same dimension
d > d0 on (see Proposition 4.4). The feature here is that we obtain a dimension free constant
Cp,q,Y.
Second, we return to the maximal estimate as in (1.5), but allow the elementf to which
the operator is applied, itself to depend ont. In order to formulate the main result in this part,
Theorem 1.5 below, we need to replace the supremum by the norm ofΛβ= Λβ
2,2(R+) ={f :
R+→C : f◦exp∈Wβ
2 (R)}, whereWβ
2 (R) is the usual Sobolev space. The reason is that
the method of our proofs uses Banach space geometric arguments, and with this respect, the
Hilbert space Λβis much nicer thanL∞(R+) and its norm supt>0|ft|. Yet Λβembeds into
C0(R+)⊆L∞(R+) for β >1
2. Note that Theorem 1.5 uses the spaceWc
1 (R) in contrast to the
space Wc
2 (R) in Theorem 1.1.
Theorem 1.5 (see Theorem 5.1)LetY be a UMD lattice,1<p< ∞and (Ω,µ) a σ-ﬁnite
measure space. Letβ> 0. Let A be a 0-sectorial operator onLp(Y ). Assume that A has a
Hα
2 calculus onLp(Y ) for someα>1
2. Letm be a spectral multiplier withm(0) = 0 such that∑
n∈Z‖m(2n·)ϕ0‖Wc
1 (R) <∞, with
c>α+ max
(1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 1 +β.
Then forft∈Lp(Y (Λβ
2,2(R+))), we have
‖t↦→m(tA)ft‖Lp(Y (C0(R+))) ⩽C′‖t↦→m(tA)ft‖Lp(Y (Λβ
2,2(R+)))(1.8)
⩽C
∑
n∈Z
‖m(2n·)ϕ0‖Wc
1 (R)‖t↦→ft‖Lp(Y (Λβ
2,2(R+))).
This seems to the best of our knowledge to be the ﬁrst maximal estimate when the element
f =ft is itself allowed to depend ont, even for the caseA =−∆ the euclidean Laplacian.
In the main Theorems 1.3 resp. 1.5, it is assumed thatm(0) = 0. However, we also have
variants of these results in casem(0)⁄= 0. For the latter, we additionally need the assumption
that theq-variational resp. maximal estimate holds fore−tAf onLp(Ω,Y ) . This is guaranteed
e.g. ifA =A0⊗IdY where e−tA0 is lattice positive and contractive.
We deduce from Theorem 1.5 certain maximal estimates for the Schrödinger and wave
solution propagator, in case that the semigroup generator has the formA = A0⊗IdY and
under the hypothesis ofHα
2 calculus of A and lattice positivity as well as contractivity of
exp(−tA0) on Lp(Ω) (see Corollary 5.3). Then we consider the following abstract version of a
problem by Carleson [Car, Theorem p. 24]. Consider the abstract initial value problem
(1.9)
{
−i ∂
∂tu(t,x,ω) = Axu(t,x,ω)
u(0,x,ω) = f(x,ω),
where the solutionu depends on timet, space variablex∈Ω in whichA =Ax acts, and a mute
variableω∈Ω′. If A =−∆ is the euclidean Laplacian onΩ = Rd, then (1.9) is a Schrödinger
5
equation and exp(itA)f is at least formally the solution of (1.9). IfA =
√
−∆ , then exp(itA)f
is the solution of a wave equation. The solution for general initial valuef belonging, say, to
L2(Rd) is in general not continuous int∈[0,∞) for ﬁxed(x,ω)∈Ω×Ω′. For the Schrödinger
equation and withoutY component, Carleson asked for which diﬀerentiability parameterδ >0,
f belonging toHδ(Rd) (L2 Sobolev space) implies this continuity. Ford = 1, he foundδ >1
4
suﬃcient andδ> 1
8 necessary. Since then, Carleson’s problem has been considered by many
other authors, see [BeGo, Bou91, Bou92, Bou13, Bou16, DaKe, DeGu, DGL, DGLZ, KPV, Lee,
LuRo, MVV1, MVV2, RV1, RV2, Rog, Sjo, Sj1, Sj2, Tao, TV, TVV, Veg] and references therein.
In this paper, we provide an abstract approach and consider equation (1.9) for lattice positive
and contractive semigroups having a Hörmander calculus onLp(Ω,Y ). Based on Theorem 1.5,
we show
Theorem 1.6 [see Theorem 6.1] LetY be a UMD lattice,1 < p <∞and (Ω,µ) a σ-ﬁnite
measure space. Let A = A0⊗IdY have aHα
2 calculus on Lp(Y ) for some α >1
2, and A0
generate a lattice positive and contractive semigroup onLp(Ω). Pick
δ >α+ max
(1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 3
2.
Then for anyf∈D(Aδ), for a.e. (x,ω)∈Ω×Ω′, the function
{
(0,∞) ↦−→C
t ↦−→exp(itA)f(x,ω)
is continuous. Similarly, for a.e.x∈Ω, the function
{
(0,∞) ↦−→Y
t ↦−→exp(itA)f(x,·)
is continuous.
See also Corollary 6.5 for a version where continuity on the real line (in particular int = 0)
in place of on(0,∞) is obtained. Note that the domainD(Aδ) reduces toH2δ(Rd) in Carleson’s
original problemA =−∆ on L2(Rd). The method of proof is to exploit an a priori maximal
estimate (see Corollary 5.3)
‖‖‖‖‖sup
t∈[a,b]
|exp(itA)f|
‖‖‖‖‖
Lp(Y )
≲
‖‖(1 +A)δf
‖‖
Lp(Y )
which in turn is a consequence of Theorem 1.5. Note that our method is very general in that
it allows an abstract operatorA. The drawback is that there is no reason to hope that the
parameter δis optimal. Thus our approach does not reprove the recent solutions to Carleson’s
problem in the way he stated it originally. However, we obtain several corollaries on variants of
Carleson’s problem, one of which improves the recent result [Zh, Theorem 1.2] for dimensions
d> 8.
Corollary 1.7 (see Corollary 6.8)Let 0<a< 2, d∈N and s> 2a. LetA = (−∆) a/2 and
f∈Hs(Rd). Then for a.e. x∈Rd, R→C, t↦→exp(itA)f(x) is a continuous function. In
particular, exp(itA)f(x)→f(x) as t→0 for a.e.x∈Rd.
6
See also the end of Section 6 for other applications on Carleson’s continuity problem, with
A being a Fourier multiplier or an operator acting on an open domainΩ⊆Rd.
We end this introduction with an overview of the article. In Section 2 we introduce the
