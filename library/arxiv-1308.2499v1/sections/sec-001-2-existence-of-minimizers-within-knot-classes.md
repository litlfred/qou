---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-001-2-existence-of-minimizers-within-knot-classes
section_title: "Existence of minimizers within knot classes"
section_number: 2
pages: 11-19
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
The arguments here are quite similar as for the tangent-point energies [5], however, we
provide full proofs for the readers’ convenience.
Using Theorem 1 together with the Arzel `a-Ascoli theorem, we see that sets of curves
in C1
ia(R/Z, Rn) with a uniform bound on the energy are sequentially compact inC1. To
this end we need the following result.
Proposition 2.1 (Uniform bi-Lipschitz estimate). For every M<∞ and (0.6) there
is a constant C(M, p, q) > 0 such that every curve γ∈ C1
ia(R/Z, Rn) parametrized by
arc-length with
intM(p,q)(γ)≤ M (2.1)
11
γ′
1(0)
γ1(0)
γ2(0)
γ′
2(0)
Figure 3: A pair of curves (γ1,γ 2)∈ Mµ deﬁned in Lemma 2.2. Note that the arcs γ1,
γ2 cannot intersect each other.
satisﬁes the bi-Lipschitz estimate
|u−v|≤ C(M, p, q)|γ(u)−γ(v)| for all u,v∈ R/Z. (2.2)
The proof is based on the following lemma. To be able to state it, we set for two
arc-length parametrized curvesγi : Ii→ R, i = 1, 2, I1, I2 open intervals,
intM(p,q)(γ1,γ 2) := intM(p,q)(γ1) + intM(p,q)(γ2) +
+
$
I2
1×I2
⏐⏐⏐γ′
1(u1)
⏐⏐⏐
⏐⏐⏐γ′
1(u2)
⏐⏐⏐
⏐⏐⏐γ′
2(u3)
⏐⏐⏐
R(p,q)(γ1(u1),γ 1(u2),γ 2(u3)) du1 du2 du3
+
$
I1×I2
2
⏐⏐⏐γ′
1(u1)
⏐⏐⏐
⏐⏐⏐γ′
2(u2)
⏐⏐⏐
⏐⏐⏐γ′
2(u3)
⏐⏐⏐
R(p,q)(γ1(u1),γ 2(u2),γ 2(u3)) du1 du2 du3.
Lemma 2.2. Letα∈ (0, 1). Forµ> 0 we let Mµ denote the set of all pairs (γ1,γ 2) of
curvesγi∈ C1
ia([−1, 1], Rn) satisfying
(i) |γ1(0)−γ2(0)| = 1,
(ii) γ′
1(0)⊥ (γ1(0)−γ2(0))⊥γ′
2(0),
(iii) ‖γ′
i‖C0,α≤µ, i = 1, 2.
Then there is a c = c(α,µ )> 0 such that
intM(p,q)(γ1,γ 2)≥ c for all (γ1,γ 2)∈ Mµ.
Proof. It is easy to see that intM (p,q)(γ1,γ 2) is zero if and only if both γ1 and γ2 are
part of one single straight line. We will show that intM(p,q)(·,·) attains its minimum on
Mµ. As Mµ does not contain straight lines by (i), (ii), this minimum is strictly positive
which thus proves the lemma.
Let (γ(n)
1 ,γ (n)
2 ) be a minimizing sequence in Mµ, i.e. we have
lim
n→∞
intM(p,q)(γ(n)
1 ,γ (n)
2 ) = inf
Mµ
intM(p,q)(·,·).
12
Subtractingγ1(0) from both curves, i.e. setting
˜γ(n)
i (τ) :=γ(n)
i (τ)−γ1(0), i = 1, 2,
and using Arzel`a-Ascoli we can pass to a subsequence such that
˜γ(n)
i → ˜γi in C1.
Furthermore, (˜γ1, ˜γ2)∈ Mµ since Mµ is closed under convergence in C1. Since, by
Fatou’s lemma, the functional intM (p,q) is lower semi-continuous with respect to C1
convergence, we obtain
intM(p,q)(˜γ1, ˜γ2)≤ lim
n→∞
intM(p,q)(˜γ(n)
1 , ˜γ(n)
2 ) = lim
n→∞
intM(p,q)(γ(n)
1 ,γ (n)
2 ) = inf
Mµ
intM(p,q)(·,·).
□
Let us use this lemma to give the
Proof of Proposition 2.1. Applying Theorem 1 to (2.1) we obtain‖γ′‖C0,α≤ C(M) for
α = 3 p−1
q − 2∈ (0, 1− 1
q). As an immediate consequence there is a δ = δ(α, M) > 0
such that
|u−v|≤ 2|γ(u)−γ(v)| (2.3)
for all u,v∈ R/Z with|u−v|≤ δ. Let now
S := inf
{
|γ(u)−γ(v)|
⏐⏐⏐⏐ u,v∈ R/Z,|u−v|≥δ
}
≤ 1
2.
We will complete the proof by estimating S from below. Using the compactness of
{u,v∈ R/Z,|u−v|≥δ}, there are s, t∈ R/Z with|s− t|≥ δ and|γ(s)−γ(t)| = S . If
now|s− t| =δ we obtain
2S = 2|γ(s)−γ(t)|
(2.3)
≥δ
and hence
|u−v|≤ 1
2≤ S
δ ≤|γ(u)−γ(v)|
δ(α, M)
for all u,v ∈ R/Z with|u−v|≥ δ. This proves the proposition in this case. If on the
other hand|s− t|>δ then we infer using the minimality of|γ(s)−γ(t)|
γ′(s)⊥ (γ(s)−γ(t))⊥γ′(t).
We deﬁne forτ∈ [−1, 1]
γ1(τ) := 1
Sγ(s + Sτ) and γ2(τ) := 1
Sγ(t + Sτ).
Since‖γ′
i‖C0,α≤‖γ′‖C0,α≤ C(M) we may apply Lemma 2.2 which yields
intM(p,q)(γ1,γ 2)≥ c(α, M)> 0.
Together with intM(p,q)(γ1,γ 2)≤ S 3p−2q−3intM(p,q)(γ) this leads to
S≥
( c(α, M)
intM(p,q)(γ)
) 1
3p−2q−3
≥
(c(α, M)
M
) 1
3p−2q−3
.
Hence,|u−v|≤ 1
2≤ |γ(u)−γ(v)|
2S ≤ C(M, p, q)|γ(u)−γ(v)| for all u,v∈ R/Z with|u−v|≥
δ. □
13
We are now in the position to prove the compactness result which is crucial both to
the existence of minimizers in any knot class and to the self-avoiding behavior of the
energies.
Proposition 2.3 (Sequential compactness). For each M<∞ the set
AM :=
{
γ∈ C1
ia(R/Z, Rn)
⏐⏐⏐ intM(p,q)(γ)≤ M
}
is sequentially compact in C1 up to translations.
Proof. By Theorem 1 there are C(M) <∞ and α = α(p, q) > 0 such that ‖γ′‖Cα ≤
C(M) for allγ∈ AM and hence
‖˜γ‖C1,α≤ C(M) + 1
where ˜γ(u) :=γ(u)−γ(0). By Proposition 2.1, the bi-Lipschitz estimate (2.2) holds.
Let nowγn∈ AM. Then
‖˜γn‖C1,α≤ C(M) + 1
and hence after passing to suitable subsequence we have ˜γn→γ0 in C1. Since γn was
parametrized by arc-length, γ0 is still parametrized by arc-length and the bi-Lipschitz
estimate carries over to γ0. So, especially, γ0 ∈ C1
ia(R/Z, Rn). From lower semi-
continuity with respect to C1 convergence we infer
intM(p,q)(γ0)≤ lim inf
n→∞
intM(p,q)(γn)≤ M.
Soγ0∈ AM. □
We may now pass to the
Proof of Theorem 2. Let (γk)k∈N∈ C1
ia be a minimal sequence for intM (p,q) in a given
knot class K, i.e. let
lim
k→∞
intM(p,q)(γk) = inf
C1
ia∩K
intM(p,q).
After passing to a subsequence and suitable translations, we hence get by Proposi-
tion 2.3 a γ0∈ C1
ia with γk→ γ0 in C1. As the intersection of every knot class with
C1 is an open set in C1 [1, Cor. 1.5] (see [30] for an explicit construction), the curveγ0
belongs to the same knot class as the elements of the minimal sequence (γk)k∈N. The
lower semi-continuity of intM(p,q) furthermore implies
inf
C1
ia∩K
intM(p,q)≤ intM(p,q)(γ0)≤ lim
n→∞
intM(p,q)(γn) = inf
C1
ia∩K
intM(p,q).
Hence,γ0 is the minimizer we have been searching for. □
By the same reasoning one derives the existence of a global minimizer of intM(p,q).
Let us conclude this section by deriving that the generalized integral Menger curvature
are in fact knot energies (in the sub-critical range).
14
Proposition 2.4 (intM( p,q) is a strong knot energy [36, Cor. 2.3]). Let (0.6) hold.
(i) If (γk)k∈N is a sequence of embedded W (3p−2)/q−1,q-curves uniformly converg-
ing to a non-injective curve γ∞ ∈ C0,1 parametrized by arc-length then
intM(p,q)(γk)→∞ .
(ii) For given E, L> 0 there are only ﬁnitely many knot types having a representa-
tive with intM(p,q) < E and length = L.
Proof. The ﬁrst statement immediately follows from the bi-Lipschitz estimate in Propo-
sition 2.1, as a sequence with bounded energy would be sequentially compact inC1
ia and
thus cannot uniformly converge to a non-injective curve.
To show the second statement, let us assume that it was wrong, i.e., that there are curves
(γk)k∈N of length L, all belonging to diﬀerent knot classes, with energy less than E. Of
course we can assume that L = 1. After applying suitable transformations and passing
to a subsequence, Proposition 2.3 guarantees the existence ofγ0∈ AM withγk→γ0 in
C1. Again by [1, 30] this implies that almost allγk belong to the same knot class asγ0,
which is a contradiction. □
3 Di ﬀerentiability
Recall that we have forv,w∈ D
|v|,|w|≤| v−w|≤ 2
3.
Hence, we obtain for a each curve γ∈ C0,1
ia (R/Z) with intM (p,q)(γ) <∞ due to the
bi-Lipschitz estimate
|γ(u +v)−γ(u)|≃| v|, |γ(u +w)−γ(u)|≃| w|, |γ(u +v)−γ(u +w)|≃| v−w|
for all (u,v,w )∈ R/Z× D. (Here a≃ b is an abbreviation for the existence of uniform
constants 0< c≤ C <∞ with cb≤ a≤ Cb.)
We derive the following form for the ﬁrst variation which is at ﬁrst site much more
complicated than the formula derived by Hermes [17], but due to the special structure
of D it is easier to do estimates using this formula. We abbreviate
Rp,q(u1, u2, u3) := R(p,q)(γ(u1),γ (u2),γ (u3))
and we still use
∆v,w• :=•(u +v)−• (u +w). (0.9)
In contrast to O’Hara’s knot energies, we can use a rather direct argument to deduce that
the integral Menger curvature is Gˆateaux diﬀerentiable by investigating the integrand,
i.e. by looking at the Lagrangian
L(γ)(u,v,w ) :=
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|q|∆v,0γ|q|∆v,wγ|q|γ′(u)||γ′(u +v)||γ′(u +w)|.
Forγ, h∈ W(3p−2)/q−1,q as in the statement of the lemma andγτ :=γ+τh one calculates
δL(γ; h)(u,v,w ) := ∂
∂τ
(
Lγτ(u,v,w )
)⏐⏐⏐⏐⏐τ=0
15
=
{
q
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q−2
⟨∆w,0γ∧∆ v,0γ,∆w,0h∧∆ v,0γ +∆w,0γ∧∆ v,0h⟩
|∆w,0γ|p|∆v,0γ|p|∆v,wγ|p
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p+2|∆v,0γ|p|∆v,wγ|p· ⟨∆w,0γ,∆w,0h⟩
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p|∆v,0γ|p+2|∆v,wγ|p· ⟨∆v,0γ,∆v,0h⟩
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p|∆v,0γ|p|∆v,wγ|p+2· ⟨∆v,wγ,∆v,wh⟩
+ Rp,q(u, u +w, u +v)
⟨ γ′(u)
|γ′(u)|, h′(u)
|γ′(u)|
⟩
+ Rp,q(u, u +w, u +v)
⟨ γ′(u +v)
|γ′(u +v)|, h′(u +v)
|γ′(u +v)|
⟩
+ Rp,q(u, u +w, u +v)
⟨ γ′(u +w)
|γ′(u +w)|, h′(u +w)
|γ′(u +w)|
⟩}
|γ′(u +w)||γ′(u +v)||γ′(u)|.
For future reference, we denote the seven terms one obtains from this formula after
factoring out the outermost bracket byδL1,...,δ L7.
Lemma 3.1. Let (0.6) hold and γ ∈ W(3p−2)/q−1,q(R/Z, Rn) be an injective regular
curve. Then intM(p,q) is Gˆ ateaux diﬀerentiable inγ and the ﬁrst variation in direction
h∈ W(3p−2)/q−1,q(R/Z, Rn) is given by
δintM(p,q)(γ; h) = 6
$
R/Z×D
δL(γ; h)(u,v,w ) dw dv du (3.1)
and (0.10) holds.
Proof. Let U be a neighborhood of γ in W(3p−2)/q−1,q ⊂ C(3p−3)/q−1 ⊂ C1 consisting
only of regular curves with
inf
˜γ∈U,u∈R/Z
|˜γ′(u)| =: M1 > 0
and
sup
˜γ∈U,u,v∈R/Z
|˜γ(u)− ˜γ(v)|
|u−v| =: M2 <∞.
Using
⟨∆w,0γ
w ∧∆v,0γ
v ,∆w,0h
w ∧∆v,0γ
v +∆w,0γ
w ∧∆v,0h
v
⟩
=
⟨(∆w,0γ
w −∆v,0γ
v
)
∧∆v,0γ
v ,
(∆w,0h
w −∆v,0h
v
)
∧∆v,0γ
v +
(∆w,0γ
w −∆v,0γ
v
)
∧∆v,0h
v
⟩
,
∆0,wγ
w ∧∆0,vγ
v =
(∆0,wγ
w −∆0,vγ
v
)
∧∆0,vγ
v ,
and
Rp,q(u,v,w ) =
⏐⏐⏐⏐
(∆0,wγ
w − ∆0,vγ
v
)
∧∆ 0,vγ
⏐⏐⏐⏐
q
|w|−q
⏐⏐⏐∆0,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p ⏐⏐⏐∆v,wγ
⏐⏐⏐p
16
together with the bi-Lipschitz estimate we infer for ˜γ∈ U
|δL(˜γ; h)(u,v,w )|≤ C
|∆w,0 ˜γ
w − ∆v,0 ˜γ
v |q‖h′‖L∞ +|∆w,0 ˜γ
w − ∆v,0 ˜γ
v |q−1|∆w,0h
w − ∆v,0h
v |
|w|p−q|v|p−q|v−w|p . (3.2)
So for 0<|τ|≤ 1 so small thatγτ∈ U
⏐⏐⏐⏐⏐
∂
∂τ L(γτ)(u,v,w )
⏐⏐⏐⏐⏐
≤ C
|∆w,0γ
w − ∆v,0γ
v |q‖h′‖L∞ +|∆w,0h
w − ∆v,0h
v |q‖h′‖L∞ +|∆w,0γ
w − ∆v,0γ
v |q−1|∆w,0h
w − ∆v,0h
v | +|∆w,0h
w − ∆v,0h
v |q
|w|p−q|v|p−q|v−w|p
=:g(u,v,w )
(3.3)
whereg does not depend onτ and C depends on M1, M2, p, q only.
For f∈ W(3p−2)/q−1,q(R/Z, Rn), we have
$
R/Z×D
|∆w,0 f
w − ∆v,0 f
v |q
|w|p−q|v|p−q|v−w|p dv dw du
=
$
R/Z×D
⏐⏐⏐⏐
∫ 1
0 ( f′(u +θw)− f′(u +θv)) dθ
⏐⏐⏐⏐
q
|w|p−q|v|p−q|w−v|p dw dv du
≤ C
∫ 1
0
$
R/Z×D
| f′(u +θ(w−v))− f′(u)|q
|w|p−q|v|p−q|w−v|p dw dv du dθ
(1.3)
≤ C‖ f‖q
W(3p−2)/q−1,q.
(3.4)
Hence,
$
R/Z×D
|g(u,v,w )| dw dv du
≤ C [γ]q
W(3p−q−2)/q,q‖h′‖L∞ + [h]q
W(3p−q−2)/q,q
(
1 +
‖‖‖h′‖‖‖L∞
)
+ C

$
R/Z×D
|∆w,0γ
w − ∆v,0γ
v |q
|w|p−q|v|p−q|v−w|p dw dv du

1− 1
q

$
R/Z×D
|∆w,0h
w − ∆v,0h
v |q
|w|p−q|v|p−q|v−w|p dw dv du

1
q
≤ C
([γ]q
W(3p−2)/q−1,q + [h]q
W(3p−2)/q−1,q
)(
1 +
‖‖‖h′‖‖‖L∞
)
+ C [γ]q−1
W(3p−q−2)/q,q [h]q
W(3p−q−2)/q,q.
(3.5)
So δL(γτ; h) has a uniform L1-majorant for τ suﬃciently small. Therefore, by Lebe-
gue’s theorem of dominanted convergence, we ﬁnally can use the fundamental theorem
of calculus to write forτ small
intM(p,q)(γ +τh)− intM(p,q)(γ)
τ = 6
$
R/Z×D
∫ 1
0
δL(γsτ; h)(u,v,w ) ds du dv dw
τ→0
−−−→6
$
R/Z×D
δL(γ; h)(u,v,w ) du dv dw.
17
Consequently, the ﬁrst variation exists and has the form (3.1).
Using once more the symmetry of the integrand, we can bring this into the form (0.10)
as follows. Due to the symmetry of the integrand we have L◦ Pσ = L for any permu-
tation matrix Pσ,∈ S3. So we obtain
6
$
R/Z×D
δL(γ; h) =
∑
σ∈S3
$
Pσ(R/Z×D)
δL(γ; h) =
$
(R/Z)3
δL(γ; h).
The symmetry of R(p,q) now leads to the desired.
Furthermore, by (3.2), the ﬁrst variation deﬁnes a bounded linear operator onW(3p−2)/q−1,q.
Hence intM(p,q) is Gˆateaux diﬀerentiable. □
In fact, we can even show that intM (p,q) is C1, though we will not use this fact in the
rest of this article.
Lemma 3.2. The functional intM(p,q) is C1 on the subspace of all regular embedded
W(3p−2)/q−1,q-curves.
Proof. We will prove by contradiction thatδintM(p,q) is a continuous map from embed-
ded regular W(3p−2)/q−1,q-curves to
(
W(3p−2)/q−1,q
)∗
. So let us assume thatδintM(p,q)was
not continuous inγ0. Consequently, there are someε0 > 0 and sequences(γk)k∈N, (hk)k∈N⊂
W(3p−2)/q−1,q,γk→γ0 in W(3p−2)/q−1,q,‖hk‖W(3p−2)/q−1,q≤ 1, with
|δintM(p,q)(γk; hk)− intM(p,q)(γ; hk)|≥ ε0. (3.6)
As in the proof of Lemma 3.1, we can exploit the embedding W(3p−2)/q−1,q ↪→ C1 and
the openness of the set of regular embedded curves inC1, to ﬁnd an open neighborhood
U ofγ0 consisting only of embedded curves, such that
inf
˜γ∈U,u∈R/Z
|˜γ′(u)| =: M1 > 0
and
sup
˜γ∈U
‖˜γ‖W(3p−2)/q−1,q + sup
˜γ∈U,u,v∈R/Z
|˜γ(u)− ˜γ(v)|
|u−v| =: M2 <∞.
After passing to a subsequence we may assume(γk)k∈N⊂ U and hk→ h0∈ W(3p−2)/q−1,q
in C1 due to the compactness of the embedding W(3p−2)/q−1,q ↪→ C1 which then also
gives
δL(γk; hk)−δL(γ0; h0)→ 0
pointwise almost everywhere on R/Z× D and hence in measure, i.e., for all ε >0 we
have
lim
k→∞
L3 (Aε,k
) = 0, (3.7)
whereL3 denotes the Lebesgue measure and
Aε,k :=
{
(u,v,w )∈ R/Z× D
⏐⏐⏐⏐
⏐⏐⏐δL(γk; hk)(u,v,w )−δL(γ0; h0)(u,v,w )
⏐⏐⏐≥ε
}
.
18
For allε> 0 we can deduce from (3.2) using Young’s inequality that there is aCε > 0
with
|δL(γk; hk)(u,v,w )|≤ Cε
|∆w,0γk
w − ∆v,0γk
v |q
|w|p−q|v|p−q|v−w|p +ε
|∆w,0hk
w − ∆v,0hk
v |q
|w|p−q|v|p−q|v−w|p
=: Cεg(1)
k (u,v,w ) +εg(2)
k (u,v,w )
(3.8)
for all k∈ N∪{0}. Since the ﬁrst summand converges in L1 as k→∞ , it is uniformly
integrable, so there is a δε > 0 such thatL3(E)≤ δε for any measurable subset E⊂
R/Z× D implies $
E
g(1)
k ≤ ε
Cε
for all k∈ N∪{0}. (3.9)
Furthermore we infer from (1.3)
$
R/Z×D
g(2)
k du dv dw≤ C‖hk‖W(3p−2)/q−1,q≤ C.
By (3.7) there is some k0 = k0(ε)∈ N with
L3 (Aε,k
)≤δε for all k≥ k0
which yields for k≥ k0 and Bε,k := R/Z× D\ Aε,k
1
6|δintM(p,q)(γk; hk)−δintM(p,q)(γ0; h0)|
≤
$
Aε,k
|δL(γk; hk)−δL(γ0; h0)| +
$
Bε,k
|δL(γk; hk)−δL(γ0; h0)|
≤
$
Aε,k
(
Cεg(1)
k +εg(2)
k
)
+
$
Aε,k
(
Cεg(1)
0 +εg(2)
0
)
+L3(Bε,k)ε
≤ Cε.
Hence,
ε0
(3.6)
≤
⏐⏐⏐δintM(p,q)(γk; hk)− intM(p,q)(γ; hk)
⏐⏐⏐
≤
⏐⏐⏐δintM(p,q)(γk; hk)− intM(p,q)(γ; h)
⏐⏐⏐ +
⏐⏐⏐δintM(p,q)(γ; hk)− intM(p,q)(γ; h)
⏐⏐⏐
≤ Cε + C‖hk− h‖W(3p−2)/q−1,q
for allε> 0 and k≥ k0(ε) which leads to a contradiction. □
