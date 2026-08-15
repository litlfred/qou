---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-097-41-asymptotics
section_title: "Asymptotics"
section_number: 4.1
pages: 51-53
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
We shall need a q-analogue of asymptotics in the sense of Poincar´ e . In
chapter 5 we shall develop a more restrictive notion of asymp totics.
The underlying idea, coming from the thesis [ 33] of Jose-Luis Martins, is
that an asymptotic theory is related to a dynamical system. I n the “classical”
case of Poincar´ e asymptotics for ordinary diﬀerential equa tions, say locally
at 0 in C∗, the dynamical system is given by the action of the semi-grou p
Σ := e]−∞,0[; in our case, the semi-group is plainly Σ := q−N (in the case of
diﬀerence equations there are two semi-groups: Σ := N and Σ := −N; this
was used by J. Roques in [ 45]). Likewise, the sheaves of functions admitting
an asymptotic expansion will be deﬁned on the horizon, that is on the quotient
space C∗/Σ. In the classical case, this is the circle S1 of directions (rays from
0) in C∗; in our case, this is the elliptic curve Eq = C∗/qZ = C∗/q−N (in the
diﬀerence case this is a pair of cylinders).
4.1.1. q-Asymptotics. — Recall from the introduction that we denote p :
C∗→ Eq the quotient map. We set
Σ :=q−N and, for A⊂ C, Σ(A) :=
⋃
a∈A
q−N{a}.
Let U be an open set of C invariant by the semi-group Σ := q−N, that is,
q−1U ⊂ U (we shall also call it “stable”). We shall say that a Σ-invari ant
subset K of U is a stable strict subset if there exists a compact subset K ′ of
U such that K = Σ(K ′); then K∪{ 0} is compact in C. An invariant subset
46 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
K⊂U is strict if and only if p(K) is a compact subset of Eq.
Let f be a function holomorphic on the Σ-invariant open subset U of C∗
and let ˆf = ∑
n≥0
anzn∈ C[[z]]. We shall say that f is q-asymptotic to ˆf on U
if, for all n∈ N and every Σ-invariant strict subset K⊂U:
z−n(
f(x)−Sn−1 ˆf
)
is bounded on K. Here, Sn−1 ˆf :=
n−1∑
p=0
apzp stands for ”truncation to n
terms” of ˆf. If f admits a q-asymptotic expansion it is plainly unique. In the
following we will say for simplicity “asymptotic expansion ” for “q-asymptotic
expansion”. For n∈ N we shall denote f (n)(0) :=n!an.
We denote:
– A (U) the space of holomorphic functions admitting a q-asymptotic ex-
pansion on U,
– A0(U) the subspace of A (U) made up of (inﬁnitely) ﬂat functions, i.e.
those such that ˆf = 0 and
– B(U) the space of holomorphic functions bounded on every stable strict
subset of U.
Iff is holomorphic onU, thenf∈ A (U) if and only ifz−n(
f(z)−Sn−1 ˆf(z)
)
∈
B(U) for all n∈ N. We check easily that A (U) is a C-algebra and that
A0(U) is an ideal of A (U).
Let again U be a Σ-invariant open subset of C∗ and let U∞ := p(U);
we think of U∞ as the horizon of U. Every open subset of Eq is the
horizon of some Σ-invariant open subset of C∗ (actually, of a great many of
them !) and, from now on, we shall often write U∞ an arbitrary open subset of
Eq andU some adequate Σ-invariant open subset ofC∗ such thatU∞ :=p(U).
We introduce three sheaves on Eq, also denoted A , A0 and B; no confusion
should be caused by this overloading of notations. The reade r is invited to
check that these are indeed sheaves:
– A (U∞) is the direct limit of all A (U),
– A0(U∞) is the direct limit of all A0(U) and
– B(U∞) is the direct limit of all B(U).
