---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-004-abstract-hörmander-functional-calculus
section_title: "Abstract Hörmander functional calculus"
section_number: null
pages: 11-13
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 12 sections: Front matter; Introduction; R-boundedness"
---
Abstract Hörmander functional calculus
We recall the necessary background on functional calculus that we will treat in this article.
Let −A be a generator of an analytic semigroup (Tz)z∈Σδ on some Banach space X, that is,
δ ∈(0, π
2 ], Σδ = {z ∈C\{0} : | arg z| < δ}, the mapping z 7→Tz from Σδ to B(X) is analytic,
Tz+w = TzTw for any z, w ∈Σδ, and limz∈Σδ′, |z|→0 Tzx = x for any x ∈X and any strict
subsector Σδ′ of Σδ. We assume that (Tz)z∈Σδ is a bounded analytic semigroup, which means
supz∈Σδ′ ∥Tz∥< ∞for any δ′ < δ.
It is well-known [EN, Theorem 4.6, p. 101] that this is equivalent to A being ω-sectorial for
ω = π
2 −δ, that is,
1. A is closed and densely deﬁned on X;
2. The spectrum σ(A) is contained in Σω (in [0, ∞) if ω = 0);
3. For any ω′ > ω, we have supλ∈C\Σω′ ∥λ(λ −A)−1∥< ∞.
We say that A is strongly ω-sectorial if it is ω-sectorial and has moreover dense range. If A is
ω-sectorial and does not have dense range, but X is reﬂexive, which will always be the case in
this article, then we may take the injective part A0 of A on R(A) ⊆X [KW04, Proposition
15.2], which then does have dense range and is strongly ω-sectorial. Here, R(A) stands for the
range of A. Then −A generates an analytic semigroup on X if and only if so does −A0 on R(A).
For θ ∈(0, π), let
H∞(Σθ) = {f : Σθ →C : f analytic and bounded}
equipped with the uniform norm ∥f∥∞,θ = supz∈Σθ |f(z)|. Let further
H∞
0 (Σθ) =

f ∈H∞(Σθ) : ∃C, ϵ > 0 such that |f(z)| ⩽C min(|z|ϵ, |z|−ϵ)
	
.
10
For an ω-sectorial operator A and θ ∈(ω, π), one can deﬁne a functional calculus H∞
0 (Σθ) →
B(X), f 7→f(A) extending the ad hoc rational calculus, by using a Cauchy integral formula.
Moreover, if there exists a constant C < ∞such that ∥f(A)∥⩽C∥f∥∞,θ, then A is said to have
a bounded H∞(Σθ) calculus and if A has a dense range, the above functional calculus can be
extended to a bounded Banach algebra homomorphism H∞(Σθ) →B(X). If A has a bounded
H∞(Σθ) calculus, and does not have dense range, but X is reﬂexive, then for f ∈H∞(Σθ) such
that f(0) is well-deﬁned, we can deﬁne
f(A) =

f(A0)
0
0
f(0)PN(A)

: R(A) ⊕N(A) →R(A) ⊕N(A),
where PN(A) denotes the projection onto the null-space of A along the decomposition X =
R(A) ⊕N(A). This calculus also has the property fz(A) = Tz for fz(λ) = exp(−zλ), z ∈
Σ π
2 −θ. For further information on the H∞calculus, we refer e.g. to [KW04]. We now turn to
Hörmander function classes and their calculi.
Deﬁnition 2.11 Let α > 1
2. We deﬁne the Hörmander class by
Hα
2 =

f : [0, ∞) →C is bounded and continuous on (0, ∞), |f(0)| + sup
R>0
∥φf(R ·)∥W α
2 (R)
|
{z
}
=:∥f∥Hα
2
< ∞
	
.
Here φ is any C∞
c (0, ∞) function diﬀerent from the constant 0 function (diﬀerent choices of
functions φ resulting in equivalent norms) and W α
2 (R) is the classical Sobolev space.
The term |f(0)| is not needed in the functional calculus applications of Hα
2 if A is in addition
injective. We can base a Hörmander functional calculus on the H∞calculus by the following
procedure. Note that for any α > 1
2 and any θ ∈(0, π), H∞(Σθ) injects continuously into Hα
2 .
Deﬁnition 2.12 We say that a 0-sectorial operator A has a bounded Hα
2 calculus if for some
θ ∈(0, π) and any f ∈H∞(Σθ), ∥f(A)∥⩽C∥f∥Hα
2 (⩽C′ (∥f∥∞,θ + |f(0)|)) . In this case, the
H∞(Σθ) calculus can be extended to a bounded Banach algebra homomorphism Hα
2 →B(X)
[KrW3]. We say that A has an R-bounded Hα
2 calculus, if it has a bounded Hα
2 calculus and

m(A) : ∥m∥Hα
2 ⩽1
	
is R-bounded.
The Hörmander norm is dilation invariant, i.e. ∥f(t·)∥Hα
2 = ∥f∥Hα
2 for any t > 0. Therefore,
the following family of (discrete) dilates of a C∞
c (R+) function will play an important role.
Deﬁnition 2.13 Let ϕ0 ∈C∞
c (R+) such that supp(ϕ0) ⊆[ 1
2, 2]. We deﬁne for n ∈Z the
dilates ϕn(t) = ϕ0(2−nt) so that supp(ϕn) ⊆[ 1
2 · 2n, 2 · 2n]. Assume that P
n∈Z ϕn(t) = 1 for
any t > 0. Then we call (ϕn)n∈Z a dyadic partition of R+ = (0, ∞). For the existence of such
a dyadic partition, we refer to [BeL, 6.1.7 Lemma].
In the course of the main theorems 3.3 and 5.1, we need to decompose general spectral
multipliers by means of special spectral multiplier pieces involving the above dyadic partition.
To reassemble the pieces together, mere boundedness of the pieces is not suﬃcient, and we will
need the following self-improvement of a Hörmander functional calculus.
Proposition 2.14 Let A be a 0-sectorial operator on a Banach space X with property (α).
If A has a bounded Hα
2 calculus, then it has an R-bounded Hγ
2 calculus for any parameter
γ > α +
1
type X −
1
cotype X such that γ ⩾α + 1
2. If X is a Hilbert space and A has a bounded Hα
2
calclus, then A has an R-bounded Hα
2 calculus.
11
Proof : This follows from [KrW3, Lemma 3.9 (3), Theorem 6.1 (2)], noting that the Hβ
r class
there is larger than our Hγ
2 class for γ = β. The last sentence follows from Remark 2.2.
The following lemmata concerning decomposition/expansion of spectral multipliers will be
used in the proof of Theorem 3.3. Here, Lemma 2.17 is sometimes called Paley-Littlewood
equivalence.
Lemma 2.15 Let A be a 0-sectorial operator with Hα
2 calculus. Let (ϕn)n∈Z be a dyadic par-
tition of R+. Then for any x ∈R(A) (e.g. x = m(A)y for some y ∈X and m ∈Hα
2 with
m(0) = 0), we have x = P
n∈Z ϕn(A)x (convergence in X).
Proof : See [KrPhD, Corollary 4.20].
In the setting of the above Lemma 2.15, we obtain that DA := {φ(A)x : x ∈X, φ ∈C∞
c (R+)}
is a dense subspace of R(A). In [KrW3], DA is called the calculus core of A.
Lemma 2.16 Let A be a 0-sectorial operator having a Hα
2 calculus. Let m ∈W α
2 (R) with
compact support in R+. Then for any x belonging to the calculus core DA, we have
m(A)x = 1
2π
Z
R
ˆm(s) exp(isA)xds,
where the integral is a Bochner integral in X.
Proof : This follows from [KrW3, Proof of Lemma 4.6 (3)].
Lemma 2.17 Let A be a 0-sectorial operator with Hα
2 calculus for some α > 1
2. Let (ϕn)n∈Z be
a dyadic partition of R+. Then we have the following so-called Paley-Littlewood decomposition
for x ∈R(A):
∥x∥X ∼= E

X
n∈Z
εnϕn(A)x

X
,
where the series P
n∈Z ϕn(A)x converges unconditionally in X.
Proof : See [KrW2, Theorem 4.1], together with the fact that the restriction of A to R(A) is a
strongly 0-sectorial operator having a Hα
2 calculus, hence a Mβ calculus [KrPhD, Proposition
4.9] needed in this reference.
