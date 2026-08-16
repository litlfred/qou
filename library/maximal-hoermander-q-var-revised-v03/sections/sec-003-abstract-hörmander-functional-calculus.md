---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-003-abstract-hörmander-functional-calculus
section_title: "Abstract Hörmander functional calculus"
section_number: null
pages: 11-13
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
doc_brief: "HAL Id: hal-04526930 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 10 sections: Introduction"
---
We recall the necessary background on functional calculus that we will treat in this article.
Let−A be a generator of an analytic semigroup(Tz)z∈Σδon some Banach spaceX, that is,
δ∈(0, π
2 ], Σδ={z∈C\{0}: |argz|<δ}, the mappingz↦→Tz from Σδto B(X) is analytic,
Tz+w = TzTw for any z,w ∈Σδ, and limz∈Σδ′,|z|→0Tzx = x for any x∈X and any strict
subsector Σδ′of Σδ. We assume that(Tz)z∈Σδis a bounded analytic semigroup, which means
supz∈Σδ′‖Tz‖<∞for anyδ′<δ.
It is well-known [EN, Theorem 4.6, p. 101] that this is equivalent toA being ω-sectorial for
ω= π
2−δ,that is,
1. A is closed and densely deﬁned onX;
2. The spectrumσ(A) is contained inΣω(in [0,∞) if ω= 0);
3. For anyω′>ω,we havesupλ∈C\Σω′‖λ(λ−A)−1‖<∞.
We say thatA is stronglyω-sectorial if it isω-sectorial and has moreover dense range. IfA is
ω-sectorial and does not have dense range, butX is reﬂexive, which will always be the case in
this article, then we may take the injective partA0 of A on R(A)⊆X [KW04, Proposition
15.2], which then does have dense range and is stronglyω-sectorial. Here,R(A) stands for the
range ofA.Then−A generates an analytic semigroup onX if and only if so does−A0 onR(A).
Forθ∈(0,π), let
H∞(Σθ) ={f : Σθ→C : f analytic and bounded}
equipped with the uniform norm‖f‖∞,θ= supz∈Σθ|f(z)|.Let further
H∞
0 (Σθ) =
{
f∈H∞(Σθ) : ∃C,ϵ>0 such that|f(z)|⩽C min(|z|ϵ,|z|−ϵ)
}
.
10
For anω-sectorial operatorA and θ∈(ω,π), one can deﬁne a functional calculusH∞
0 (Σθ)→
B(X), f↦→f(A) extending the ad hoc rational calculus, by using a Cauchy integral formula.
Moreover, if there exists a constantC <∞such that‖f(A)‖⩽C‖f‖∞,θ, thenA is said to have
a boundedH∞(Σθ) calculus and ifA has a dense range, the above functional calculus can be
extended to a bounded Banach algebra homomorphismH∞(Σθ)→B(X).If A has a bounded
H∞(Σθ) calculus, and does not have dense range, butX is reﬂexive, then forf∈H∞(Σθ) such
that f(0) is well-deﬁned, we can deﬁne
f(A) =

f(A0) 0
0 f(0)PN(A)

: R(A)⊕N(A)→R(A)⊕N(A),
where PN(A) denotes the projection onto the null-space ofA along the decomposition X =
R(A)⊕N(A). This calculus also has the property fz(A) = Tz for fz(λ) = exp(−zλ), z∈
Σ π
2−θ.For further information on theH∞calculus, we refer e.g. to [KW04]. We now turn to
Hörmander function classes and their calculi.
Deﬁnition 2.11Letα>1
2.We deﬁne the Hörmander class by
Hα
2 =
{
f : [0,∞)→C is bounded and continuous on(0,∞),|f(0)|+ sup
R>0
‖φf(R·)‖Wα
2 (R)
/rcehtipupleft/rcehtipdownright/rcehtipdownleft/rcehtipupright
=:‖f‖Hα
2
<∞
}
.
Here φis any C∞
c (0,∞) function diﬀerent from the constant 0 function (diﬀerent choices of
functions φresulting in equivalent norms) andWα
2 (R) is the classical Sobolev space.
The term|f(0)|is not needed in the functional calculus applications ofHα
2 ifA is in addition
injective. We can base a Hörmander functional calculus on theH∞calculus by the following
procedure. Note that for anyα>1
2 and anyθ∈(0,π), H∞(Σθ) injects continuously intoHα
2.
Deﬁnition 2.12We say that a0-sectorial operatorA has a boundedHα
2 calculus if for some
θ∈(0,π) and anyf∈H∞(Σθ),‖f(A)‖⩽C‖f‖Hα
2 (⩽C′(‖f‖∞,θ+|f(0)|)).In this case, the
H∞(Σθ) calculus can be extended to a bounded Banach algebra homomorphismHα
2 →B(X)
[KrW3]. We say thatA has anR-boundedHα
2 calculus, if it has a boundedHα
2 calculus and{
m(A) : ‖m‖Hα
2 ⩽ 1
}
is R-bounded.
The Hörmander norm is dilation invariant, i.e.‖f(t·)‖Hα
2 =‖f‖Hα
2 for anyt> 0. Therefore,
the following family of (discrete) dilates of aC∞
c (R+) function will play an important role.
Deﬁnition 2.13Let ϕ0 ∈C∞
c (R+) such that supp(ϕ0)⊆[ 1
2, 2]. We deﬁne forn∈Z the
dilates ϕn(t) = ϕ0(2−nt) so that supp(ϕn)⊆[ 1
2·2n, 2·2n]. Assume that∑
n∈Zϕn(t) = 1 for
any t> 0. Then we call(ϕn)n∈Z a dyadic partition ofR+ = (0,∞). For the existence of such
a dyadic partition, we refer to [BeL, 6.1.7 Lemma].
In the course of the main theorems 3.3 and 5.1, we need to decompose general spectral
multipliers by means of special spectral multiplier pieces involving the above dyadic partition.
To reassemble the pieces together, mere boundedness of the pieces is not suﬃcient, and we will
need the following self-improvement of a Hörmander functional calculus.
Proposition 2.14 Let A be a 0-sectorial operator on a Banach spaceX with property (α).
If A has a boundedHα
2 calculus, then it has an R-boundedHγ
2 calculus for any parameter
γ >α+ 1
typeX− 1
cotypeX such thatγ>α+ 1
2. IfX is a Hilbert space andA has a boundedHα
2
calclus, thenA has anR-boundedHα
2 calculus.
11
Proof : This follows from [KrW3, Lemma 3.9 (3), Theorem 6.1 (2)], noting that theHβ
r class
there is larger than ourHγ
2 class forγ=β. The last sentence follows from Remark 2.2.
The following lemmata concerning decomposition/expansion of spectral multipliers will be
used in the proof of Theorem 3.3. Here, Lemma 2.17 is sometimes called Paley-Littlewood
equivalence.
Lemma 2.15 Let A be a 0-sectorial operator withHα
2 calculus. Let (ϕn)n∈Z be a dyadic par-
tition of R+. Then for any x∈R(A) (e.g. x = m(A)y for some y∈X and m∈Hα
2 with
m(0) = 0), we havex =∑
n∈Zϕn(A)x (convergence inX).
Proof : See [KrPhD, Corollary 4.20].
InthesettingoftheaboveLemma2.15, weobtainthat DA :={φ(A)x :x∈X,φ∈C∞
c (R+)}
is a dense subspace ofR(A). In [KrW3],DA is called the calculus core ofA.
Lemma 2.16 Let A be a 0-sectorial operator having aHα
2 calculus. Let m∈Wα
2 (R) with
compact support inR+. Then for anyx belonging to the calculus coreDA, we have
m(A)x = 1
2π

R
ˆm(s) exp(isA)xds,
where the integral is a Bochner integral inX.
Proof : This follows from [KrW3, Proof of Lemma 4.6 (3)].
Lemma 2.17 LetA be a0-sectorial operator withHα
2 calculus for someα>1
2. Let (ϕn)n∈Z be
a dyadic partition ofR+. Then we have the following so-called Paley-Littlewood decomposition
for x∈R(A):
‖x‖X∼= E
‖‖‖‖‖
∑
n∈Z
εnϕn(A)x
‖‖‖‖‖
X
,
where the series∑
n∈Zϕn(A)x converges unconditionally inX.
Proof : See [KrW2, Theorem 4.1], together with the fact that the restriction ofA toR(A) is a
strongly 0-sectorial operator having aHα
2 calculus, hence aMβcalculus [KrPhD, Proposition
4.9] needed in this reference.
