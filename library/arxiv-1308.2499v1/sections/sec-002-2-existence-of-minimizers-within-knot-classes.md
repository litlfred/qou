---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-002-2-existence-of-minimizers-within-knot-classes
section_title: "Existence of minimizers within knot classes"
section_number: 2
pages: 11-15
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
toc_source: outline
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
Existence of minimizers within knot classes
The arguments here are quite similar as for the tangent-point energies [5], however, we
provide full proofs for the readers’ convenience.
Using Theorem 1 together with the Arzel`a-Ascoli theorem, we see that sets of curves
in C1
ia(R/Z, Rn) with a uniform bound on the energy are sequentially compact in C1. To
this end we need the following result.
Proposition 2.1 (Uniform bi-Lipschitz estimate). For every M < ∞and (0.6) there
is a constant C(M, p, q) > 0 such that every curve γ ∈C1
ia(R/Z, Rn) parametrized by
arc-length with
intM(p,q)(γ) ≤M
(2.1)
11
γ′
1(0)
γ1(0)
γ2(0)
γ′
2(0)
Figure 3: A pair of curves (γ1, γ2) ∈Mµ deﬁned in Lemma 2.2. Note that the arcs γ1,
γ2 cannot intersect each other.
satisﬁes the bi-Lipschitz estimate
|u −v| ≤C(M, p, q) |γ(u) −γ(v)|
for all u, v ∈R/Z.
(2.2)
The proof is based on the following lemma. To be able to state it, we set for two
arc-length parametrized curves γi : Ii →R, i = 1, 2, I1, I2 open intervals,
intM(p,q)(γ1, γ2) := intM(p,q)(γ1) + intM(p,q)(γ2) +
+
$
I2
1×I2

γ′
1(u1)

γ′
1(u2)

γ′
2(u3)

R(p,q)(γ1(u1), γ1(u2), γ2(u3)) du1 du2 du3
+
$
I1×I2
2

γ′
1(u1)

γ′
2(u2)

γ′
2(u3)

R(p,q)(γ1(u1), γ2(u2), γ2(u3)) du1 du2 du3.
Lemma 2.2. Let α ∈(0, 1). For µ > 0 we let Mµ denote the set of all pairs (γ1, γ2) of
curves γi ∈C1
ia([−1, 1], Rn) satisfying
(i) |γ1(0) −γ2(0)| = 1,
(ii) γ′
1(0) ⊥(γ1(0) −γ2(0)) ⊥γ′
2(0),
(iii) ∥γ′
i∥C0,α ≤µ,
i = 1, 2.
Then there is a c = c(α, µ) > 0 such that
intM(p,q)(γ1, γ2) ≥c
for all (γ1, γ2) ∈Mµ.
Proof. It is easy to see that intM(p,q)(γ1, γ2) is zero if and only if both γ1 and γ2 are
part of one single straight line. We will show that intM(p,q)(·, ·) attains its minimum on
Mµ. As Mµ does not contain straight lines by (i), (ii), this minimum is strictly positive
which thus proves the lemma.
Let (γ(n)
1 , γ(n)
2 ) be a minimizing sequence in Mµ, i.e. we have
lim
n→∞intM(p,q)(γ(n)
1 , γ(n)
2 ) = inf
Mµ intM(p,q)(·, ·).
12
Subtracting γ1(0) from both curves, i.e. setting
˜γ(n)
i (τ) := γ(n)
i (τ) −γ1(0),
i = 1, 2,
and using Arzel`a-Ascoli we can pass to a subsequence such that
˜γ(n)
i
→˜γi
in C1.
Furthermore, (˜γ1, ˜γ2) ∈Mµ since Mµ is closed under convergence in C1. Since, by
Fatou’s lemma, the functional intM(p,q) is lower semi-continuous with respect to C1
convergence, we obtain
intM(p,q)(˜γ1, ˜γ2) ≤lim
n→∞intM(p,q)(˜γ(n)
1 , ˜γ(n)
2 ) = lim
n→∞intM(p,q)(γ(n)
1 , γ(n)
2 ) = inf
Mµ intM(p,q)(·, ·).
□
Let us use this lemma to give the
Proof of Proposition 2.1. Applying Theorem 1 to (2.1) we obtain ∥γ′∥C0,α ≤C(M) for
α = 3 p−1
q −2 ∈(0, 1 −1
q). As an immediate consequence there is a δ = δ(α, M) > 0
such that
|u −v| ≤2|γ(u) −γ(v)|
(2.3)
for all u, v ∈R/Z with |u −v| ≤δ. Let now
S := inf

|γ(u) −γ(v)|

 u, v ∈R/Z, |u −v| ≥δ

≤1
2.
We will complete the proof by estimating S from below. Using the compactness of
{u, v ∈R/Z, |u −v| ≥δ}, there are s, t ∈R/Z with |s −t| ≥δ and |γ(s) −γ(t)| = S . If
now |s −t| = δ we obtain
2S = 2|γ(s) −γ(t)|
(2.3)
≥δ
and hence
|u −v| ≤1
2 ≤S
δ ≤|γ(u) −γ(v)|
δ(α, M)
for all u, v ∈R/Z with |u −v| ≥δ. This proves the proposition in this case. If on the
other hand |s −t| > δ then we infer using the minimality of |γ(s) −γ(t)|
γ′(s) ⊥(γ(s) −γ(t)) ⊥γ′(t).
We deﬁne for τ ∈[−1, 1]
γ1(τ) := 1
S γ(s + S τ)
and
γ2(τ) := 1
S γ(t + S τ).
Since ∥γ′
i∥C0,α ≤∥γ′∥C0,α≤C(M) we may apply Lemma 2.2 which yields
intM(p,q)(γ1, γ2) ≥c(α, M) > 0.
Together with intM(p,q)(γ1, γ2) ≤S 3p−2q−3intM(p,q)(γ) this leads to
S ≥
 
c(α, M)
intM(p,q)(γ)
!
1
3p−2q−3
≥
 c(α, M)
M
!
1
3p−2q−3
.
Hence, |u −v| ≤1
2 ≤|γ(u)−γ(v)|
2S
≤C(M, p, q) |γ(u) −γ(v)| for all u, v ∈R/Z with |u −v| ≥
δ.
□
13
We are now in the position to prove the compactness result which is crucial both to
the existence of minimizers in any knot class and to the self-avoiding behavior of the
energies.
Proposition 2.3 (Sequential compactness). For each M < ∞the set
AM :=
n
γ ∈C1
ia(R/Z, Rn)

 intM(p,q)(γ) ≤M
o
is sequentially compact in C1 up to translations.
Proof. By Theorem 1 there are C(M) < ∞and α = α(p, q) > 0 such that ∥γ′∥Cα ≤
C(M) for all γ ∈AM and hence
∥˜γ∥C1,α ≤C(M) + 1
where ˜γ(u) := γ(u) −γ(0). By Proposition 2.1, the bi-Lipschitz estimate (2.2) holds.
Let now γn ∈AM. Then
∥˜γn∥C1,α ≤C(M) + 1
and hence after passing to suitable subsequence we have ˜γn →γ0 in C1. Since γn was
parametrized by arc-length, γ0 is still parametrized by arc-length and the bi-Lipschitz
estimate carries over to γ0. So, especially, γ0 ∈C1
ia(R/Z, Rn). From lower semi-
continuity with respect to C1 convergence we infer
intM(p,q)(γ0) ≤lim inf
n→∞intM(p,q)(γn) ≤M.
So γ0 ∈AM.
□
We may now pass to the
Proof of Theorem 2. Let (γk)k∈N ∈C1
ia be a minimal sequence for intM(p,q) in a given
knot class K, i.e. let
lim
k→∞intM(p,q)(γk) = inf
C1
ia∩K intM(p,q).
After passing to a subsequence and suitable translations, we hence get by Proposi-
tion 2.3 a γ0 ∈C1
ia with γk →γ0 in C1. As the intersection of every knot class with
C1 is an open set in C1 [1, Cor. 1.5] (see [30] for an explicit construction), the curve γ0
belongs to the same knot class as the elements of the minimal sequence (γk)k∈N. The
lower semi-continuity of intM(p,q) furthermore implies
inf
C1
ia∩K intM(p,q) ≤intM(p,q)(γ0) ≤lim
n→∞intM(p,q)(γn) = inf
C1
ia∩K intM(p,q).
Hence, γ0 is the minimizer we have been searching for.
□
By the same reasoning one derives the existence of a global minimizer of intM(p,q).
Let us conclude this section by deriving that the generalized integral Menger curvature
are in fact knot energies (in the sub-critical range).
14
Proposition 2.4 (intM(p,q) is a strong knot energy [36, Cor. 2.3]). Let (0.6) hold.
(i) If (γk)k∈N is a sequence of embedded W(3p−2)/q−1,q-curves uniformly converg-
ing to a non-injective curve γ∞
∈C0,1 parametrized by arc-length then
intM(p,q)(γk) →∞.
(ii) For given E, L > 0 there are only ﬁnitely many knot types having a representa-
tive with intM(p,q) < E and length = L.
Proof. The ﬁrst statement immediately follows from the bi-Lipschitz estimate in Propo-
sition 2.1, as a sequence with bounded energy would be sequentially compact in C1
ia and
thus cannot uniformly converge to a non-injective curve.
To show the second statement, let us assume that it was wrong, i.e., that there are curves
(γk)k∈N of length L, all belonging to diﬀerent knot classes, with energy less than E. Of
course we can assume that L = 1. After applying suitable transformations and passing
to a subsequence, Proposition 2.3 guarantees the existence of γ0 ∈AM with γk →γ0 in
C1. Again by [1, 30] this implies that almost all γk belong to the same knot class as γ0,
which is a contradiction.
□
