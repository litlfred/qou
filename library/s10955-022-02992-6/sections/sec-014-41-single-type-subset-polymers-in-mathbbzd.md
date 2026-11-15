---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-014-41-single-type-subset-polymers-in-mathbbzd
section_title: "Single-Type Subset Polymers in mathbbZd"
section_number: 4.1
pages: 25-27
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Consider the setup of subset polymers from Chapter 2.4. Suppose there is some ﬁnite non-
empty set S ⊂Zd and a scalar z > 0 such that
z(X) =

z,
X is a translate of S,
0,
otherwise.
(4.1)
We call polymers with non-zero activity active polymers. Deﬁne
V (D) :=
{X ∈X | z(X) > 0, X ∩D̸ = ∅}
,
the number of active polymers intersecting a ﬁnite domain D ⊂Zd. Notice V ({x}) = |S|,
for all x ∈Zd.
Theorem 4.1 Let z(·) be the activity function from (4.1). Suppose there exists α > 0 such
that
|S| eαV (S)z ≤eα|S| −1.
(4.2)
Then T (D; z) is absolutely convergent for all ﬁnite subsets D ⊂Zd, thus the activity expan-
sions ρn(x1, . . . , xn; z) converge absolutely for all n ∈N and all (x1, . . . , xn) ∈Xn.
Remark 4.1 Notice that Theorem 4.1 improves on the upper bounds for the convergence
radii given by Kotecký–Preiss and by Gruber–Kunz. The improvement over the Gruber–
Kunz condition is achieved by a more sophisticated choice of the ansatz function a in the
proof of the theorem. However, although we do not have a general proof that the result by
Fernández–Procacci is stronger, notice that for all non-pathological examples we considered
(e.g., non-overlapping dimers or cubes) Fernández–Procacci provides better bounds than
Theorem 4.1.
Example 4.1 (Hypercubes) If S = {1, . . . , k}d with k ∈N, condition (4.2) becomes
z ≤sup
α>0
exp(αkd) −1
kd exp(α(2k −1)d).
Carrying out the optimization over α yields the condition
(2k −1)dz ≤

1 −
1
(2 −1/k)d
	(2−1/k)d−1
.
33
Page 26 of 47
S. Jansen, L. Kolesnikov
In the limit d →∞at ﬁxed k ≥2, the right-hand side converges from above to the familiar
bound 1/e.
Proof of Theorem 4.1 We apply Theorem 2.7 with a(D) := αV (D). We check that V (·) is
strongly subadditive. Let B, C be ﬁnite subsets of Zd. Then for every polymer X,
1l{X∩B̸=∅} + 1l{X∩C̸=∅} ≥1l{X∩(B∪C)̸=∅} + 1l{X∩(B∩C)̸=∅}.
Indeed if X intersects B but not C (or C but not B), the inequality reads 1 + 0 ≥1 + 0 and
it is true. If X intersects both B and C, the inequality reads 1 + 1 ≥1 + 1l{X∩(B∩C)̸=∅} and
it is true as well. Finally if X intersects neither B nor C, then both sides of the inequality
vanish. Summing over all polymers X, we get
V (B) + V (C) ≥V (B ∪C) + V (B ∩C).
(4.3)
Now we turn to the criterion (i) from Theorem 2.7. Condition (2.18) for D′ = ∅reads
|S| z eαV (S) ≤eαV ({x}) −1,
it is satisﬁed because of V ({x}) = |S| and the assumption (4.2). For non-empty D′, we
bound the left-hand side of condition (2.18) with the help of the strong subadditivity. The
inequality (4.3) applied to B = D′ ∪{x} and C = X yields
V (D′ ∪{x}) + V (X) ≥V (D′ ∪X) + V ({x}),
(4.4)
for x ∈Zd \ D′, x ∈X, and X ∩D′ = ∅, and
V (D′ ∪X) −V (D′) ≤V (D′ ∪{x}) + V (X) −V (D′) −V ({x})
= V (D′ ∪{x}) −V (D′) + V (S) −|S|.
This provides an X-independent bound for the exponent in the left-hand side of condi-
tion (2.18). The number of summands on the left-hand side of condition (2.18) is given by the
number of active polymers intersecting x but not D′, which is equal to V (D′ ∪{x})−V (D′).
Thus to prove (2.18) it sufﬁces to show that

V (D′ ∪{x}) −V (D′)

z eα[V (D′∪{x})−V (D′)+V (S)−|S|] ≤eα[V (D′∪{x})−V (D′)] −1. (4.5)
In view of condition (4.2), the last inequality in turn follows once we check

V (D′ ∪{x}) −V (D′)

eα|S| −1

eα[V (D′∪{x})−V (D′)−|S|] ≤|S|

eα[V (D′∪{x})−V (D′)] −1

or equivalently,
1 −exp(−α|S|)
|S|
≤1 −exp(−αR)
R
,
R := V (D′ ∪{x}) −V (D′).
Because of the subadditivity of V , we have R ≥V ({x}) = |S|. The exponential map
x →exp(−αx) is convex and therefore the difference quotient is monotone increasing, i.e.,
(exp(−αx) −1)/x ≤(exp(−αy) −1))/y whenever 0 ≤x ≤y. We apply the inequality to
x = R and y = |S| and obtain the required bound.
⊓⊔
Cluster Expansions: Necessary...
Page 27 of 47
33
