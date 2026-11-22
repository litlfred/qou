---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-005-22-abstract-polymer-models
section_title: "Abstract Polymer Models"
section_number: 2.2
pages: 8-11
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
In the following we want to consider the setup of abstract polymers [1, 8], in which the
two classical conditions above—Kotecký–Preiss and Fernández–Procacci—were ﬁrst intro-
duced.
Let X be a countable set (the set of polymers), let X be the powerset of X and let λ
simply be given by the counting measure. Moreover, let R ⊂X × X be a symmetric and
reﬂexive relation. We write x ≁y for (x, y) ∈R (and say that x and y are incompatible)
and x ∼y for (x, y) /∈R (and say that x and y are compatible). Moreover, we call a subset
X ⊂X compatible if x ∼y for all x̸ = y ∈X and write X ∼z for z ∈X if z ∼x for
all x ∈X. We set 	(x) := {y ∈X| y ≁x} for any x ∈X and extend this notation to
	(X) := ∪x∈X{y ∈X| y ≁x} for any X ⊂X. Notice that we do not require 	(x) to be
ﬁnite sets and that x ∈	(x) for every x ∈X. Finally, we consider hard-core interactions
corresponding to Mayer’s f function given by f (x, y) := −1l{x≁y}.
In this setting we prove a new, improved sufﬁcient condition for absolute convergence of
the activity expansions ρ.
Cluster Expansions: Necessary...
Page 9 of 47
33
Proposition 2.4 Let z be a non-negative activity function and assume that there exists μ :
X →[0, ∞) such that for all x ∈X
z(x)
⎛
⎜⎜⎝1 +

k≥1

Y={y1,...,yk}
yi≁x, yi∼y j

μ(yi)

w∈	(Y)
eμ(w)
⎞
⎟⎟⎠≤μ(x)

w∈	(x)
eμ(w),
(2.11)
where the inner sum on the left-hand side runs over compatible subsets Y = {y1, ..., yk} ⊂
	(x). Then the activity expansions ρn(x1, . . . , xn; z) converge absolutely and the bounds
ρn(x1, . . . , xn; z) ≤

1≤i< j≤n
1{xi∼x j}
n

i=1
μ(xi)

w∈	({x1,...,xn})
eμ(w)
hold for all n ∈N and all (x1, . . . , xn) ∈Xn.
The proof of the proposition essentially exploits the following auxiliary result:
Lemma 2.5 Let μ : X →[0, ∞). Then the following holds for every x1 ∈X, n ∈N and
X = {x2, ..., xn} ⊂X such that x1 ∼xi for all i ∈{2, . . . , n}:
μ(x1)

w∈	(x1)
eμ(w)
1 + 
k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
k
i=1
μ(yi)

w∈	(Y)
eμ(w)
≤
μ(x1)

w∈	(x1)∩	(X)C
eμ(w)
1 + 
k≥1

Y={y1,...,yk}
yi≁x1, yi∼y j
yi∼X
k
i=1
μ(yi)

w∈	(Y)∩	(X)C
eμ(w)
,
(2.12)
where 	(W) is given by ∪n
i=1	(wi) for any n ∈N and W = {w1, ..., wn} ⊂X. The inner sum
in the denominator on the left-hand side runs over compatible subsets Y = {y1, . . . , yk} ⊂
	(x1); the inner sum in the denominator on the right-hand side runs over all such subsets Y
which additionally satisfy the constraint Y ∩	(X) = ∅, i.e., yi ∼X for all i ∈{1, . . . , k}.
The lemma is of rather technical nature; for the interested reader, the proof is to be found in
Appendix A.
Remark 2.5 The general idea behind the proof of Proposition 2.4 is to argue as in the proofs
of the classical conditions presented in the previous section (Corollaries 2.2 and 2.3)—but
to choose a sequence of ansatz functions ξ which, heuristically speaking, encode more of
the structure of the exact solution to the Kirkwood–Salsburg equations (i.e., of the activity
expansions ρ) than the ansatz functions chosen in the proof of those corollaries. The intuition
thereby is that “less multiplicative” ansatz functions ξ provide better convergence criteria.
Proof of Proposition 2.4 Assume that (2.11) holds and deﬁne ξ = (ξn)n∈N, ξn : Xn →
[0, ∞), by setting
ξn(x1, ..., xn) :=

1≤i< j≤n
1{xi∼x j}
n

i=1
μ(xi)

w∈	({x1,...,xn})
eμ(w)
(2.13)
33
Page 10 of 47
S. Jansen, L. Kolesnikov
for some μ satisfying (2.11), for any n ∈N and every (x1, .., xn) ∈Xn. Thereby we
again use the convention 	({w1, . . . , wn}) = ∪n
i=1	(wi) for {w1, ..., wn} ⊂X. As in the
preceeding proofs of the classical sufﬁcient conditions, we show that our choice of ξ =
(ξn)n∈N satisﬁes the system of Kirkwood–Salsburg inequalities (2.5) from Theorem 2.1. To
lighten the notation, we choose the same selection rule s as in the proof of Lemma 2.3 and
denote by X the set {x2, ..., xn}. Notice that the left-hand side of (2.5) is equal to
z(x1)

1≤i< j≤n
1{xi∼x j}
n

i=2
μ(xi)

w∈	(X)
eμ(w)
×
⎛
⎜⎜⎝1 +

k≥1

Y={y1,...,yk}
k
j=1
1{y j≁x1}

2≤i≤n
1≤j≤k
1{xi∼y j}

1≤i< j≤k
1{yi∼y j}
k
j=1
μ(y j)

w∈	(Y)∩	(X)C
eμ(w)
⎞
⎠.
By Lemma 2.5, the assumption that z satisﬁes the condition (2.11) implies that z also
satisﬁes the inequality
z(x1)
⎛
⎜⎜⎝1 +

k≥1

Y={y1,...,yk}
k
j=1
1{y j≁x1}

2≤i≤n
1≤j≤k
1{xi∼y j}

1≤i< j≤k
1{yi∼y j}
k
j=1
μ(y j)

w∈	(Y)∩	(X)C
eμ(w)
⎞
⎠
≤μ(x1)

w∈	(x1)∩	(X)C
eμ(w)
and thus, for our choice of ξ, the left-hand side of (2.5) is bounded from above by

1≤i< j≤n
1{xi∼x j}
n

i=1
μ(xi)

w∈	(X)
eμ(w)

w∈	(x1)∩	(X)C
eμ(w)
=

1≤i< j≤n
1{xi∼x j}
n

i=1
μ(xi)

w∈	(X∪{x1})
eμ(w) = ξn(x1, ..., xn),
which—by Theorem 2.1—yields the claim of the proposition.
⊓⊔
Example 2.1 Consider non-overlapping (hard-core interactions) cubes on Z2 of side-length
2 with translationally invariant activity z. The sufﬁcient condition on z for the absolute
convergence of ρ(z) given by the Fernández–Procacci criterion provides the bound
z ≤max
μ≥0
μ
1 + 9μ + 16μ2 + 8μ3 + μ4 ≈0.057271,
while our condition from Proposition 2.4 provides
z ≤max
μ≥0
μe9μ
1 + 9e9μμ + (6e15μ + 8e16μ + 2e17μ)μ2 + 8e21μμ3 + e25μμ4 ≈0.060833.
Cluster Expansions: Necessary...
Page 11 of 47
33
This corresponds to an improvement of approximately 6%.
