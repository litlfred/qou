---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-005-6-application-i-regev-type-formula
section_title: "Application I: Regev-type formula"
section_number: 6
pages: 25-43
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
In this section, as the first application of our Murnaghan–Nakayama rule, we are de-
voted to giving the Regev formula for the cyclotomic Hecke algebra Hm,n(q, u). Once the
Murnaghan–Nakayama rule is set up right, the proof of the Regev formula, which is based
on the classical deep work on symmetric groups and Hecke algebras in type A, is remark-
ably natural. To proceed with it, we initially, in accordance with [Zha24a], review the
permutation super representation of the cyclotomic Hecke algebra Hm,n(q, u), as well as
the Schur–Sergeev duality that exists between a certain quantum superalgebra Uq(g) and
Hm,n(q, u).
We refer to a superspace W as a Z2-graded vector space with decomposition W =
W¯0 ⊕W¯1. An element w ∈W is homogeneous with degree ¯i if w ∈W¯i, i = 0, 1. We also
define the dimension of W by dim(W) := dim(W¯0)|dim(W¯1).
Let V represent a direct sum of m superspaces, denoted as V = Lm
i=1 V (i). In this context,
we assume dim(V (i)) = ki|li and {v(i)
1 , v(i)
2 , · · · , v(i)
ki , v(i)
ki+1, · · · , v(i)
ki+li} forms a homogeneous
basis of V (i). Evidently, dim(V ) = k|l with k = P ki and l = P li. Additionally, B :=
{v1, v2, · · · , vk+l} constitutes a homogeneous basis for V with vd = v(s)
t
if d = Ps
i=1(ki +
li) + t. The entity c(vi) = r is defined contingent upon the condition vi ∈V (r). The term
c(·) is occasionally referred to as the color function.
26
NAIHUAN JING AND NING LIU
Introduce the linear map ω :
V −→V defined by ω(vi) = uc(vi)vi. Define the linear
operators π, σ : V ⊗V −→V ⊗V by
π(vi ⊗vj) =





(q −q−1)vi ⊗vj + (−1)¯i¯jvj ⊗vi,
if i < j;
(q−q−1)+(−1)¯i(q+q−1)
2
vi ⊗vi,
if i = j;
(−1)¯i¯jvj ⊗vi,
if i > j.
(6.1)
σ(vi ⊗vj) =
(
π(vi ⊗vj),
if c(vi) = c(vj);
(−1)¯i¯jvj ⊗vi,
if c(vi)̸ = c(vj).
(6.2)
We can demonstrate π2 = (q −q−1)π + 1, which implies π is invertible and π−1 = π −(q −
q−1)Id. We canonically extend π and σ to linear maps πi, σi(i = 1, 2, · · · , n−1) : V ⊗n −→
V ⊗n by
π±1
i
:= Id⊗(i−1) ⊗π±1 ⊗Id⊗(n−i−1)
(6.3)
σi := Id⊗(i−1) ⊗σ ⊗Id⊗(n−i−1)
(6.4)
ωi := Id⊗(i−1) ⊗ω ⊗Id⊗(n−i).
(6.5)
Furthermore, we define π0 := π−1
1 π−1
2 · · · π−1
n−1σn−1 · · · σ1ω1. As is shown in [Zha24a, Theo-
rem 3.6], the map
Ξu,q
k|l;n : Hm,n(q, u) −→EndKV ⊗n
gi 7−→πi−1,
i = 1, 2, · · · , n.
gives a (super) representation of Hm,n(q, u), called permutation super representation of
Hm,n(q, u). We denote by χu,q
k|l;n(g(µ)) the value of the character χu,q
k|l;n of Ξu,q
k|l;n on the
standard element g(µ).
Let k = (k1, k2, · · · , km) and l = (l1, l2, · · · , lm) be two compositions. For a given non-
negative integer n, we define the set C(n; k | l) of pairs of m-multicompositions associated
with k and l by
C(n; k|l) :=

(α, β)

α = (α(1), · · · , α(m)) with l(α(i)) ≤ki
β = (β(1), · · · , β(m)) with l(β(i)) ≤li
and |α| + |β| = n

.
The main result in this section is the following formula for χu,q
k|l;n(g(µ)), which is referred
to as Regev’s formula.
Theorem 6.1. Let µ be a m-multipartition of n, then the value of the character of the
permutation super representation on the standard element g(µ) is given by
χu,q
k|l;n(g(µ))
=qn−l(µ)
m
Y
r=1
l(µ(r))
Y
j=1
X
(α;β)∈C(µ(r)
j
;k|l)
ur−
→l (α;β)(1 −q−2)l(α;β)−1(−q−2)|β|−l(β)
m
Y
i=1

ki
l(α(i))

li
l(β(i))

(6.6)
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
27
where −→l (α; β) := max{1 ≤i ≤m | l(α(i)) + l(β(i)) > 0} and l(α; β) := l(α) + l(β).
Remark 6.2. In a recent development, Zhao [Zha24b] has proposed an alternative method
to derive Theorem 6.1. It should be noted that his formulation is slightly different from ours,
due to a distinct choice of presentation of Hm,n(q, u), as well as the standard elements g(µ).
Next we will introduce a series of notations. Let λ be a m-multipartition with diagram
D(λ). A (k, l)-semistandard tableau Tλ of shape λ is a m-tuple of (ki, li)-semistandard
tableaux (cf. [BR87]) obtained by filling each component D(λ(i)) of D(λ) with variables
{a(i)
1 < a(i)
2 < · · · < a(i)
ki < b(i)
1 < b(i)
2 < · · · < b(i)
li , i = 1, 2, · · · , m}, satisfying
(1) the cells filled with a(i)
j ’s form a tableau;
(2) a(i)
j ’s are nondecreasing in rows, strictly increasing in columns;
(3) b(i)
j ’s are nondecreasing in columns, strictly increasing in rows.
Denote sk,l(λ) := #{(k, l)-semistandard tableaux of shape λ}. For a given (α, β) ∈C(n; k|l),
we say that a (k, l)-semistandard tableau Tλ is of weight (α, β) if the number of a(i)
j
(resp.
b(i)
j ) in Tλ equals α(i)
j
(resp. β(i)
j ). Furthermore, denote by s(α,β)(λ) the number of all
(k, l)-semistandard tableaux of shape λ with weight (α, β). Clearly we have
sk,l(λ) =
X
(α,β)∈C(n;k|l)
s(α,β)(λ)
(6.7)
for any m-multipartition λ of n.
Define H(k|l; n) := {λ ⊢n | λk+1 ≤l}. An element in H(k|l; n) is called a (k, l)-hook
partition. More generally, a multipartition is called a (k, l)-hook multipartition if each λ(i)
is a (ki, li)-hook partition for i = 1, 2, · · · , m. Denote by H(k|l; n) the set of all (k, l)-hook
multipartitions of n. Clearly, H((1m)|(1m); n) consists of all multipartitions λ of n such
that each component of λ is a hook partition. Note that the assertion in [BR87, Definition
2.4] implies that sk,l(λ)̸ = 0 if and only if λ ∈H(k|l; n) for a multipartition λ of n.
Now we will express χu,q
k|l;n as a linear combination of irreducible characters χλ us-
ing the above notations. To continue with this development, the Schur–Sergeev duality
between Hm,n(q, u) and the quantum superalgebra Uq(g) is needed. Where Uq(g) :=
Uq(gl(k1|l1)) ⊗· · · ⊗Uq(gl(km|lm)), among which Uq(gl(ki|li)), introduced in [BKK00],
is the quantum enveloping superalgebra of gl(ki|li). V can be a representation of Uq(g),
referred to as vector presentation. The Hopf structure of Uq(g) induces an action on V ⊗n,
denoted by Θn. As is demonstrated in [BKK00], the irreducible summands of the rep-
resentation V ⊗n of Uq(gl(k, l)) are indexed by the (k, l)-hook partitions of n, with each
irreducible summand possessing the dimension sk,l(λ). Consequently, the irreducible sum-
mands of the representation (Θn, V ⊗n) of Uq(g) are characterized by the (k, l)-hook par-
titions of n, with each irreducible summand affording the dimension sk,l(λ).
It is confirmed in [Zha24a, Theorem 4.9] that (Ξu,q
k|l;n, V ⊗n) and (Θn, V ⊗n) satisfy the
Schur–Sergeev duality, i.e.,
Ξu,q
k|l;n(Hm,n(q, u)) = EndUq(g)V ⊗n,
Θn(Uq(g)) = EndHm,n(q,u)V ⊗n
(6.8)
28
NAIHUAN JING AND NING LIU




•
•
,
•
• •
,
•
•
• • 



Figure 2. SE(λ/µ) consists of the green boxes. The subset formed by the
boxes with bullets is an element of R9(λ/µ).
Moreover, as a (Uq(g), Hm,n(q, u)-bimodule,
V ⊗n ∼=
M
λ∈H(k|l;n)
Wλ ⊗W λ,
(6.9)
where Wλ (resp. W λ) is the irreducible module of Uq(g) (resp. Hm,n(q, u)) indexed by λ.
This gives the following decomposition:
V ⊗n ∼=
M
λ∈H(k|l;n)
sk,l(λ)W λ,
(6.10)
which is equivalent to
χu,q
k|l;n =
X
λ∈H(k|l;n)
sk,l(λ)χλ.
(6.11)
Now we introduce the skew characters of Hm,n(q, u) via the Jacobi–Trudi rule. Let µ ⊂λ
be two m-multipartitions (with |µ| ≤|λ|). For each 1 ≤r ≤m and a ∈Z, set
h(r)
a
:=





χεa
r,
a ≥1,
1,
a = 0,
0,
a < 0,
where 1 denotes the unit character (for the degree 0 algebra). We define
χλ/µ :=
[
m
O
r=1
det
1≤i,j≤l(λ(r))
 h(r)
λ(r)
i
−i−µ(r)
j
+j

,
(6.12)
where the determinant is taken in the character ring with multiplication given by the outer
product.
Next, we will restate our Murnaghan–Nakayama rule in terms of the skew characters.
Before that, we need some terminologies about skew diagrams. Let λ/µ be a m-multi
skew diagram, denote by SE(λ/µ) the subset of λ/µ consisting of the southeast ribbon
which starts from the northeastmost box and ends at the southeastmost box in each con-
nected component in D(λ/µ). We identify a box in the a-th row and the b-th column of
D(λ(i)/µ(i)) with the coordinate (a(i), b(i)), i = 1, 2, · · · , m. Let Rt(λ/µ) be the set of all
subsets R of SE(λ/µ) satisfying
• R has size t;
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
29








,








Figure 3. An example for Rα,β where α = ((2, 3), (3, 2, 2)) and β =
((2, 2), (3)). The corresponding skew character can be written as χ(α,β) =
χ(2) ˆ⊗χ(3) ˆ⊗χ(12) ˆ⊗χ(12) ˆ⊗χ(3) ˆ⊗χ(2) ˆ⊗χ(2) ˆ⊗χ(13).
• For any (a(i), b(i)) ∈R and (x(i), y(i)) ∈SE(λ/µ) \ R, we have either x(i) < a(i) or
y(i) < b(i).
Figure 2 presents an example for SE(λ/µ) and Rt(λ/µ). It is not hard to see that for
any m-multi skew diagram D(λ/µ) and R ∈Rt(λ/µ), D(λ/µ) \ R is still a m-multi skew
diagram. For R ∈Rt(λ/µ), denote by cc(R) the number of connected components of R.
If R has d connected components R1, R2, · · · , Rd, define ht(R) := Pd
i=1 ht(Ri).
Let ν ∈P|λ|−|µ|,m, and fix 1 ≤r ≤m, 1 ≤j ≤l(ν(r)). Then we have the following
skew-diagram version of the Murnaghan–Nakayama rule:
χλ/µ
ν
= qν(r)
j
−1
X
R∈R
ν(r)
j
(λ/µ)
ur−
→
R(1 −q−2)cc(R)−1(−q−2)ht(R)χ(λ/µ)\R
ν\ν(r)
j
.
(6.13)
Here
−→
R := max{1 ≤i ≤m | there exists at least one box of R in λ(i)/µ(i)}.
Equation (6.13) can be deduced from Corollary 3.4 using arguments similar to those in
[JK81, Chap. 2.4] (see also [Zha19, Theorem 5.2]). More precisely, one applies Corollary
3.4 to the terms arising from the Jacobi–Trudi determinant expansion defining χλ/µ, and
then regroups the resulting terms according to the subsets R ∈Rν(r)
j (λ/µ) of SE(λ/µ).
The regrouped terms are precisely the skew characters χ(λ/µ)\R.
For (α, β) ∈C(n; k|l), denote by Rα,β some (any) m-multi skew diagrams D(λ/µ) (This
is not unique!) such that the connected components of D(λ(i)/µ(i)) are horizontal strips
H(i)
1 , H(i)
2 , · · · , H(i)
ki and vertical strips V (i)
1 , V (i)
2 , · · · , V (i)
li
(i = 1, 2, · · · , m) satisfying
(H(i)
1 , H(i)
2 , · · · , H(i)
ki ) = (α(i)
1 , α(i)
2 , · · · , α(i)
ki ),
(V (i)
1 , V (i)
2 , · · · , V (i)
li ) = (β(i)
1 , β(i)
2 , · · · , β(i)
li ).
(6.14)
For Rα,β, define the character related to Rα,β by
χ(α;β) := [
O
1≤i≤m
 
χ(α(i)
1 ) ˆ⊗· · · ˆ⊗χ(α(i)
ki ) ˆ⊗χ(1β(i)
1 ) ˆ⊗· · · ˆ⊗χ(1
β(i)
li )
!
.
(6.15)
See Figure 3 for an example for Rα,β.
30
NAIHUAN JING AND NING LIU
Due to [BR87, Lemma 3.23] (see also [Tay17, Lemma 3.2], [Zha19, Corollary 5.5]), we
have the following decomposition for χ(α;β) in terms of irreducible characters.
χ(α;β) =
X
λ∈H(k|l;n)
s(α,β)(λ)χλ.
(6.16)
Now we restate our skew version of the Murnaghan–Nakayama rule in a special case.
Rα,β is a m-multi skew diagram as mentioned above. Then
Rt(Rα,β) = {Rγ,δ | (γ, δ) ⊂(α, β), |γ| + |δ| = t}.
(6.17)
Furthermore, if Rγ,δ ∈Rt(Rα,β), then we have cc (Rγ,δ) = l(γ)+l(δ) = l(γ; δ), ht(Rγ,δ) =
|δ| −l(δ) and −−→
Rγ,δ = −→l (γ; δ). We can restate (6.13) in the following special setting.
χ(α;β)
ν
= qν(r)
j
−1
X
(γ,δ)⊂(α,β)
|γ|+|δ|=ν(r)
j
ur−
→l (γ,δ)(1 −q−2)l(γ;δ)−1(−q−2)|δ|−l(δ)χ(α;β)\(γ;δ)
ν\ν(r)
j
.
(6.18)
We are ready to prove Theorem 6.1.
Proof of Theorem 6.1.
χu,q
k|l;n(g(µ))
=
X
λ∈H(k|l;n)
sk,l(λ)χλ
(by (6.11))
=
X
λ∈H(k|l;n)
X
(α,β)∈C(n;k|l)
s(α,β)(λ)χλ
(by (6.7))
=
X
(α,β)∈C(n;k|l)
χ(α;β)
(by (6.16))
=
X
(α,β)∈C(n;k|l)
qµ(r)
j
−1
X
(γ,δ)⊂(α,β)
|γ|+|δ|=µ(r)
j
ur−
→l (γ,δ)(1 −q−2)l(γ;δ)−1(−q−2)|δ|−l(δ)χ(α;β)\(γ;δ)
µ\µ(r)
j
(by (6.18)).
For a given (α
′, β
′) ∈C(n −µ(r)
j ; k|l), if (α, β) \ (γ, δ) = (α
′, β
′), then the number of
(γ, δ)’s contributing the coefficient
qµ(r)
j
−1ur−
→l (γ,δ)(1 −q−2)l(γ;δ)−1(−q−2)|δ|−l(δ)
is exactly
m
Y
i=1

ki
l(γ(i))

li
l(δ(i))

.
Therefore,
χu,q
k|l;n(g(µ))
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
31
=



X
(γ,δ)∈C(µ(r)
j
;k|l)
qµ(r)
j
−1ur−
→l (γ,δ)(1 −q−2)l(γ;δ)−1(−q−2)|δ|−l(δ)
m
Y
i=1

ki
l(γ(i))

li
l(δ(i))




×
X
(α′,β′)∈C(n−µ(r)
j
;k|l)
χ(α
′;β
′)
µ\µ(r)
j
.
An induction argument completes the proof.
□
Next, we consider the special case (k|l) = ((1m)|(1m)). It follows from the proof of
Theorem 6.1 that
χu,q
(1m)|(1m);n =
X
(α,β)∈C(n;(1m)|(1m))
χ(α;β).
(6.19)
Note that every (α, β) in C(n; (1m)|(1m)) has the form
(α, β) = ((α1), (α2), · · · , (αm), (β1), (β2), · · · , (βm))
with Pm
i=1(αi + βi) = n. So
RHS of (6.19) =
X
c1+c2+···+cm=n
ci≥0
[
O
1≤i≤m
ci
X
αi=0
χ(αi;ci−αi).
(6.20)
By [Tay17, Remark 3.3],
ci
X
αi=0
χ(αi;ci−αi) =
(
1
if ci = 0;
2 Pci−1
αi=0 χ(ci−αi,1αi)
if ci ≥1.
(6.21)
Substituting this into (6.20) gives that
RHS of (6.19) =
X
λ∈H((1m)|(1m);n)
2L(λ)χλ.
(6.22)
Recall that H((1m)|(1m); n) consists of all m-multipartitions λ of n such that each com-
ponent λ(i) is a hook partition. Here L(λ) := #{1 ≤i ≤m | λ(i)̸ = ∅}.
On the other hand, by (6.6),
χu,q
(1m)|(1m);n(g(µ)) = qn−l(µ)
m
Y
r=1
l(µ(r))
Y
j=1
X
(α;β)
ur−
→l (α;β)(1 −q−2)l(α)+l(β)−1(−q−2)|β|−l(β)
(6.23)
the inner sum runs over all pairs of m-compositions (α; β) with |α| + |β| = µ(r)
j .
32
NAIHUAN JING AND NING LIU
Note that
X
(α;β)
|α|+|β|=µ(r)
j
ur−
→l (α;β)(1 −q−2)l(α)+l(β)−1(−q−2)|β|−l(β)
=
1
1 −q−2
X
c1+c2+···+cm=µ(r)
j
ci≥0
ur−
→c
X
(α;β)
|α|+|β|=ci
(1 −q−2)
Pm
i=1(2−δβi,ci−δβi,0)(−q−2)
Pm
i=1(βi+δβi,0−1)
=
1
1 −q−2
X
c1+c2+···+cm=µ(r)
j
ci≥0
ur−
→c
X
(α;β)
|α|+|β|=ci
m
Y
i=1
(1 −q−2)2−δβi,ci−δβi,0(−q−2)βi+δβi,0−1
=
1
1 −q−2
X
c1+c2+···+cm=µ(r)
j
ci≥0
ur−
→c
m
Y
i=1
ci
X
βi=0
(1 −q−2)2−δβi,ci−δβi,0(−q−2)βi+δβi,0−1
=
X
c1+c2+···+cm=µ(r)
j
ci≥0
ur−
→c 2#c(1 −q−2)#c−1
m
Y
i=1
[ci]−q−2,
(6.24)
where −→c := max{1 ≤i ≤m | ci̸ = 0}, c := {1 ≤i ≤m | ci̸ = 0} and [k]q := 1−qk
1−q (Here
k ≥0 and [0]q := 1) is the standard q-integer. The last equation holds for the following
identity:
ci
X
βi=0
(1 −q−2)2−δβi,ci−δβi,0(−q−2)βi+δβi,0−1 =
(
2(1 −q−2)[ci]−q−2
if ci > 0
1
if ci = 0.
We say that a m-tuple of matrices (M (1), M (2), · · · , M (m)) is a m-multimatrix if each
M (i) has m columns with entries nonnegative integers. Denote by Mm the set of all m-
multimatrices. For a m-multimatrix M = (M (1), M (2), · · · , M (m)), define
r(M) :=
m
X
i=1
r(M (i)),
uM :=
m
Y
i=1
r(M(i))
Y
j=1
ui−
→r j(M(i)).
Here we use the notations r(M (i)) and −→r j(M (i)) to present the number of rows in matrix
M (i) and the j-th row vector of matrix M (i), respectively. Thus u−
→r j(M(i)) = ufij with fij
the column containing the first non-zero element from right to left in the jth row of M (i).
For instance, if
M =



3
2
0
0
1
6

,


2
0
0
0
4
2
8
0
0

,
 2, 2, 0

.
(6.25)
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
33
We have marked the last non-zero element in each row in orange. Thus,
(fij) =



2
3

,


1
3
1

,
 2

,
uM = u4
1u4
2u3
3.
Substituting (6.24) into (6.23) gives that
χu,q
(1m)|(1l);n(g(µ)) =
X
M
uM2#M(q −q−1)#M−l(µ)
Y
m(r)
ij ∈M
[m(r)
ij ]−q−2,
(6.26)
summed over all m-multimatrices (M (1), · · · , M (m)) ∈Mm such that the j-th row sum of
M (r) equals µ(r)
j . Where #M is the number of nonzero entries in M.
Now we have obtained the following result.
Corollary 6.3. Let µ be a multipartition of n. Then we have the following combinatorial
formula, which is also referred as the Regev formula.
X
λ⊢n
all λ(i) hook
2L(λ)χλ
µ =
X
M
uM2#M(q −q−1)#M−l(µ)
Y
m(r)
ij ∈M
[m(r)
ij ]−q−2,
(6.27)
summed over all m-multimatrices (M (1), · · · , M (m)) such that the jth row sum of M (r)
equals µ(r)
j .
Proof. It follows from (6.19), (6.22) and (6.26) by noticing that H((1m)|(1m); n) consists
of all multipartitions λ of n with each component λ(i) being hook shape.
□
Remark 6.4. We remark that Zhao [Zha24b] obtained an asymptotic formula for the LHS
of (6.27). It is pertinent to point out that an alternative proof for Corollary 6.3 is presented
by establishing a connection between the irreducible characters of Hm,n(q, u) and those of
Hecke algebra in type A. This proof relies on the Regev formula for Hecke algebra in type
A. To prevent redundancy, we leave this proof in the appendix A.
Recall that Hm,n(q, u) will reduce to Hecke algebra Hn(q) (resp. complex reflection group
Wm,n) when m = 1, u1 = 1 (resp. q = 1, u = {1, ζ, · · · , ζm−1}). Here ζ is the primitive
m-th root of unity. Before closing this section, we want to examine how the Regev formula
adapts in these two special cases. To do so, we will analyze each case individually. For the
first case, i.e., m = 1, u1 = 1, it is easy to see (6.27) is degraded to
X
λ hook
ψλ
µ = 2l(µ)−1
l(µ)
Y
i=1
[µi]−q−2.
(6.28)
Where ψλ is the irreducible character of Hn(q) indexed by λ. This is exactly the Regev
formula for the Hecke algebra in type A established in [JL22, Zha19]. For the second case,
34
NAIHUAN JING AND NING LIU
i.e., q = 1, u = {1, ζ, · · · , ζm−1}, we have
X
M
uM2#M(q −q−1)#M−l(µ)
Y
m(r)
ij ∈M
[m(r)
ij ]−q−2 =



P
M
uM2l(µ)
if all µ(r)
j ’s are odd
0
otherwise
summed over all m-multimatrices M such that j-th row of M (r) has only one nonzore
entry µ(r)
j . Moreover, if all µ(r)
j ’s are odd, then
X
M
uM2l(µ) =
m
Y
r=1
l(µ(r))
Y
j=1
2
m
X
i=1
ζ(r−1)i =
(
(2m)l(µ(1)),
if µ = (µ(1), 0, · · · , 0);
0,
otherwise.
The last equation holds for the following identity:
m
X
i=1
ζ(r−1)i =
(
m,
if r = 1;
0,
if 1 < r ≤m.
We have reached the Regev formula for Wm,n.
Corollary 6.5. Suppose µ is a m-multipartition of n, then
X
λ⊢n
λ(i) hook
ϕλ
µ =
(
(2m)l(µ(1)),
if µ = (µ(1), 0, · · · , 0) with all parts odd;
0,
otherwise.
(6.29)
Where ϕλ is the irreducible character of Wm,n indexed by multipartition λ.
7. Application II: L¨ubeck–Prasad–Adin–Roichman-type formula
In this section, as the second application of our Murnaghan–Nakayama rule, we will es-
tablish a L¨ubeck–Prasad–Adin–Roichman formula for the cyclotomic Hecke algebra Hm,n(q, u).
To proceed with this, We will present an algorithm for χ(λ(1),λ(2),··· ,λ(m))
µ
using the corre-
sponding single partition λ with empty m-core and (λ(1), λ(2), · · · , λ(m)) as its m-quotient.
Finally, we will explain how our formula recovers the Adin-Roichman formula for the com-
plex reflection group Wm,n [AR22], and particularly the L¨ubeck-Prasad formula for the
hyperoctahedral group [LP21].
7.1. A restatement of the Murnaghan–Nakayama rule. In this subsection, we re-
state the Murnaghan–Nakayama rule established in Section 3 in terms of ηλ
τ;r defined as
below.
Definition 7.1. Let λ = (λ(1), λ(2), · · · , λ(m)) ∈Pn,m, τ = (τ (1), τ (2), · · · , τ (t)) be a t-tuple
of partitions with each partition having at most m parts and r be a positive integer. Define
ηλ
τ;r as the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(2) If l(τ (t)) < m, add 0’s to the tail to make sure τ (t) has m components.
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
35
 
!
 
!
 
!












Figure 4. Four possible removal processes for η(3,1),(2,1,1),(2,2)
(2,1);r
. Here t =
1 and we choose σ = id. The sum terms they contribute are respec-
tively ur
2(1 −q−2)3(−q−2)0, ur
2(1 −q−2)3(−q−2)0, ur
2(1 −q−2)2(−q−2)0 and
ur
2(1 −q−2)2(−q−2)0.
(3) Choose a permutation σ ∈Sm. Remove a τ (t)
σ(j)-generalized ribbon θj from λ(j) for
all j = 1, 2, · · · , m. If there is no such σ to do the removal process, set ε = 0 and
end the program.
(4) Multiply ε by ur
m(1 −q−2)−1+Pm
j=1 cc(θj)(−q−2)
Pm
j=1 ht(θj), where cc(θj) (resp. ht(θj))
is the number of connected components (resp. the height) of θj. And m := max{1 ≤
j ≤m | τ (t)
σ(j)̸ = 0}.
(5) Redefine τ := (τ (1), τ (2), · · · , τ (t−1)) and t := t −1.
(6) Return to step (1).
Figure 4 presents four possible removal processes.
For a partition µ = (µ1, µ2, · · · , µt) (µt > 0), define Pm(µ) := {(τ (1), τ (2), · · · , τ (t)) |
τ (j) ⊢µj and l(τ (j)) ≤m, 1 ≤j ≤t}. Let λ, µ ∈Pn,m. Then we have the following
restatement of the Murnaghan–Nakayama rule:
χλ
µ = qn−l(µ)
m
X
r=1
X
τ∈Pm(µ(r))
ηλ
τ;r.
(7.1)
7.2. A L¨ubeck–Prasad–Adin–Roichman-type formula. Now, we will identify a par-
tition λ with its boundary sequence ∂(λ), which is a finite 0/1 sequence constructed as
follows: commence at the southwestern vertex of the diagram of λ, and traverse along the
edges of the southeastern boundary proceeding towards the northeastern vertex; represent
36
NAIHUAN JING AND NING LIU
Figure 5. λ = (7, 7, 7, 6, 3, 3, 2, 1), the boundary of λ is marked by arrows.
Thus, ∂(λ) = 10101001 | 1101000 and the anchor of ∂(λ) is 8.
each horizontal movement by a 1, and each vertical movement by a 0. Clearly, λ is de-
termined by its boundary sequence ∂(λ) and invariant under adding 0’s (resp. 1’s) to the
head (resp. tail) of ∂(λ). We define the anchor of ∂(λ) = (s1, s2, · · · , st) is the position i
such that #{1 ≤j ≤i | sj = 1} = #{i + 1 ≤j ≤t | sj = 0}. We usually insert a vertical
line “|” into ∂(λ) to indicate the anchor. See Figure 5 for an example.
Now we describe the bijection Ψm between the set of m-multipartitions of n (denoted
by Pn,m) and the set of partitions of mn with empty m-core (denoted by P0
mn). Here, the
m-core of a partition λ is obtained by removing as many m-ribbons from λ as possible.
Definition 7.2. For a given λ = (λ(1), λ(2), · · · , λ(m)) ∈Pn,m, suppose ∂(λ(i)) = (s(i)
1 , · · · , s(i)
d ),
i = 1, 2, · · · , m. Here we add the leading 0’s and trailing 1’s to make ∂(λ(i)) have the same
length d and the same anchor for all 1 ≤i ≤m. We let Ψm(λ) be the unique partition
such that ∂(Ψm(λ)) is
s(1)
1 , s(2)
1 , · · · , s(m)
1
, s(1)
2 , s(2)
2 , · · · , s(m)
2
, · · · , s(1)
d , s(2)
d , · · · , s(m)
d
.
We claim Ψm is a bijection. Indeed, λ = (λ(1), λ(2), · · · , λ(m)) is the m-quotient of Ψm(λ).
Moreover, we have |Ψm(λ)| = m|λ| (see also [AR22, Remark 2.9]).
Example 7.3. We choose λ as follows:




,
,



.
The boundary sequence of each component of λ is 10 | 110, 100 | 10 and 11 | 00, respectively.
Add the leading 0’s and tailing 1’s to make sure they have the same length and the same
anchor. So their boundary sequences can be presented as follows:
010 | 110
100 | 101
011 | 001
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
37
1
3
2
3
2
1
2
3
Figure 6. ˜∂(λ) = 010101001 | 110100011, k(˜∂(λ)) = 9 and the row-color
sequence is marked in the leftmost column. Thus, the green generalized rib-
bon is colored by 1.
Therefore, the boundary sequence of Ψm(λ) is 010101001 | 110100011. This is exactly the
partition in Figure 5 when remove the leading 0’s and the tailing 1’s.
Lemma 7.4. Let λ = (λ1, · · · , λl) (λl ≥0) be a partition with its boundary sequence
∂(λ) = (s1, s2, · · · ). We collect the following facts from [AR22]:
(1) Removing a k-ribbon from λ is equivalent to exchanging si = 1 with si+k = 0, for
some i.
(2) The position in ∂(λ) of the zero corresponding to λi is equal to λi + l −i + 1.
For a given partition λ with empty m-core and length l, denote by ˜∂(λ) the boundary
sequence given by Definition 7.2 (before removing the leading 0’s and the tailing 1’s).
Note that ˜∂(λ) relies on the choice of ∂(λ(1)), ∂(λ(2)), · · · , ∂(λ(m)). Define k(˜∂(λ)) := #{j |
˜∂(λ)j = 0}. We define the row-color sequence a(λ) of λ by a(λ) := (a1, · · · , al), where
1 ≤ai ≤m and ai ≡λi + k(˜∂(λ)) −i + 1 (mod m), i = 1, 2, · · · , l.3 We claim that
a(λ) is independent of the choice of ˜∂(λ). Indeed, if we have another boundary sequence
ˆ∂(λ) obtained from Definition 7.2 via distinct choice of ∂(λ(1)), ∂(λ(2)), · · · , ∂(λ(m)), then
m | (k(˜∂(λ)) −k(ˆ∂(λ))), which implies they gives the same a(λ) by definition.
We say the starting point (resp. ending point) of a ribbon is the northeastmost (resp.
southwestmost) box of the ribbon. A ribbon is colored by i if the row-color of the row
containing the starting point of the ribbon equals i. That is, if the starting point is in the
j-th row then aj = i. More generally, We say a generalized ribbon is colored by i if all of
its connected components are colored by i. See Figure 6 for an example.
Proposition 7.5. Let λ be a partition with empty m-core and m-quotient (λ(1), λ(2), · · · , λ(m)).
We have that removing a k-generalized ribbon with p connected components from λ(i) is
3We remark that the definition of the row-color sequence is slightly different from that in [AR22,
Definition 3.3].
38
NAIHUAN JING AND NING LIU
equivalent to removing a km-generalized ribbon with p connected components colored by i
from λ.
Proof. Suppose ∂(λ(i)) = (s(i)
1 , s(i)
2 , · · · ) is the boundary sequence of λ(i) and ˜∂(λ) =
(s1, s2, · · · ) is the boundary sequence given by Definition 7.2. By Lemma 7.4 (1), removing
a k-generalized ribbon with p connected components from λ(i) is equivalent to exchanging
s(i)
i1 = 1 with s(i)
j1 = 0, s(i)
i2 = 1 with s(i)
j2 = 0, · · · , s(i)
ip = 1 with s(i)
jp = 0 in ∂(λ(i)) for
some i1 < j1 < i2 < j2 < · · · < ip < jp such that Pp
a=1(ja −ia) = k. It follows from
the definition of Ψm that this is further equivalent to exchanging su1 = 1 with sv1 = 0,
su2 = 1 with sv2 = 0, · · · , sup = 1 with svp = 0 such that Pp
a=1(va −ua) = km and
ua ≡va ≡i (mod m), 1 ≤a ≤p. Lemma 7.4 (1) implies that this is equivalent to re-
moving a km-generalized ribbon with p connected components from λ. If we assume the
starting points of the connected components of this km-generalized ribbon are respectively
in the row t1, t2, · · · , tp in λ, then Lemma 7.4 (2) yields that λta + k(˜∂(λ)) −ta + 1 = va,
1 ≤a ≤p. So λta + k(˜∂(λ)) −ta + 1 ≡i (mod m), 1 ≤a ≤p, i.e., this km-generalized
ribbon is colored by i, which completes the proof.
□
Example 7.6. If we remove the generalized ribbon (its two components are in color yellow
and green) from λ(2) = (2, 1, 1) as follows:




,
,



.
This is equivalent to removing the following generalized ribbon colored by 2 (its two com-
ponents are in color yellow and green) from (7, 7, 7, 6, 3, 3, 2, 1):
1
3
2
3
2
1
2
3
For any finite sequence a = (a1, a2, · · · ), we define its inversion number by
inv(a) := #{(i, j) | i < j, ai > aj}.
Let a(λ) = (a1, a2, · · · , al) be the row-color sequence of λ. Define its m-inversion number
by
invm(λ) := inv(a(λ)).
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
39
For any finite sequence a = (a1, · · · , ad), we assume that b = (b1, · · · , bd) is a permutation
of a. Define I(a; b) by
I(a; b) := min{inv(σ) | σ ∈Sd, such that ai = bσ(i) for all i = 1, 2, · · · , d}.
Here the permutation σ is viewed as a word (or sequence). For instance, σ = (13254) is
identified with the word 35214 for the reason that
σ =

1
2
3
4
5
3
5
2
1
4

.
For example, we choose a = (1, 2, 5, 1, 3, 2, 7), b = (2, 5, 1, 3, 2, 7, 1). Then the permutation
σ with the minimal inversion number satisfying ai = bσ(i) is 3127456. So I(a; b) = 5.
Remark 7.7. I(a; b) can be computed graphically. Indeed, I(a; b) is equal to the minimal
value of all possible applications of the following process:
(1) Put sequences a and b in two rows and align them;
(2) Connect the same number in the generic manner: no three lines intersect at one
point;
(3) Count the intersection number of the lines.
In the above example, we can draw the lines, which produce the minimal intersection number
as follows:
1
2
5
1
3
2
7
2
5
1
3
2
7
1
So I(a; b) = 5.
Lemma 7.8. Let λ
′ be a partition obtained from λ by removing a generalized ribbon with
connected components ξ1, ξ2, · · · , ξp. Suppose ui and vi are respectively the indices of the
rows in λ containing the starting point and ending point of ξi (1 ≤i ≤p) such that
u1 < v1 < u2 < v2 < · · · < up < vp. If we assume the row-color sequence of λ is
a(λ) = (· · · , au1, · · · , av1
|
{z
}
v1−u1+1
, · · · , au2, · · · , av2
|
{z
}
v2−u2+1
, · · · , aup, · · · , avp
|
{z
}
vp−up+1
, · · · ).
Then we have
a(λ
′) = (· · · , au1+1, · · · , av1, au1
|
{z
}
v1−u1+1
, · · · , au2+1, · · · , av2, au2
|
{z
}
v2−u2+1
, · · · , aup+1, · · · , avp, aup
|
{z
}
vp−up+1
, · · · );
(7.2)
I(λ/λ
′) := I(a(λ); a(λ
′)) =
p
X
i=1
#{j | ui < j ≤vi, aj̸ = aui};
(7.3)
(−1)invm(λ)−invm(λ
′) = (−1)I(λ/λ
′).
(7.4)
40
NAIHUAN JING AND NING LIU
Proof. (7.2) can be obtained by using the same arguments as those in [AR22, Lemma 3.5].
(7.3) follows from (7.2) by definition (or Remark 7.7). Now we show (7.4). It follows from
(7.2) that
invm(λ) −invm(λ
′) =
p
X
i=1
 #{j | ui < j ≤vi, aj < aui} −#{j | ui < j ≤vi, aj > aui}

,
which has the same parity as I(λ/λ
′) by (7.3). This completes the proof.
□
Definition 7.9. Let λ be a partition of mn, τ = (τ (1), τ (2), · · · , τ (t)) be a t-tuple of parti-
tions with each partition having at most m parts and r be a positive integer. Define ηλ
τ;r as
the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(2) If l(τ (t)) < m, add 0’s to the tail to make sure τ (t) has m components.
(3) Choose a permutation σ ∈Sm. Remove a mτ (t)
σ(1)-generalized ribbon θ
′
1 colored by
1 from λ, and then remove a mτ (t)
σ(2)-generalized ribbon θ
′
2 colored by 2 from λ/θ
′
1.
Continue this process until we remove a mτ (t)
σ(m)-generalized ribbon θ
′
m colored by m
from λ/(θ
′
1 ∪· · · ∪θ
′
m−1). If there is no such σ to do the removal process, set ε = 0
and end the program.
(4) Multiply ε by ur
m(1 −q−2)−1+Pm
j=1 cc(θ
′
j)(−q−2)
Pm
j=1(ht(θ
′
j)−I(θ
′
j)), where cc(θ
′
j) (resp.
ht(θ
′
j)) is the number of connected components (resp. the height) of θ
′
j. And m :=
max{1 ≤j ≤m | τ (t)
σ(j)̸ = 0}.
(5) Redefine τ := (τ (1), τ (2), · · · , τ (t−1)) and t := t −1.
(6) Return to step (1).
Now we are ready to give a L¨ubeck–Prasad–Adin–Roichman formula for the cyclotomic
Hecke algebra, computing the irreducible characters by using partitions instead of m-
multipartitions.
Theorem 7.10. Let λ = (λ(1), λ(2), · · · , λ(m)), µ ∈Pn,m. We assume that λ is the unique
partition with empty m-core and (λ(1), λ(2), · · · , λ(m)) as its m-quotient. Then we have
χλ
µ = qn−l(µ)
m
X
r=1
X
τ∈Pm(µ(r))
ηλ
τ;r,
(7.5)
Proof. By (7.1), Definition 7.1 and Proposition 7.5, it suffices to show that ηλ
τ;r = ηλ
τ;r, for
which it is sufficient to verify that the factors of corresponding removal process under the
bijection established in Proposition 7.5 differ by some power of −q−2. To be precise, if we
remove a k-generalized ribbon θi with height ht(θi) from λ(i), which, due to Proposition
7.5, is equivalent to removing a km-generalized ribbon θ
′
i colored by i with height ht(θ
′
i)
from λ, then we need to verify ht(θi) = ht(θ
′
i) −I(θ
′
i). For the sake of argument, we make
the following assumptions:
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
41
• θi (resp. θ
′
i) has p connected components ξ1, ξ2, · · · , ξp (resp. ξ
′
1, ξ
′
2, · · · , ξ
′
p).
• Let u1 < v1 < u2 < v2 < · · · < up < vp (resp. u(i)
1 < v(i)
1
< u(i)
2 < v(i)
2
< · · · < u(i)
p <
v(i)
p ) be the indices of rows in λ (resp. λ(i)) such that the uq-th (resp. u(i)
q -th) row
and the vq-th (resp. v(i)
q -th) row contain respectively the starting point and ending
point of ξ
′
q (resp. ξq), q = 1, 2, · · · , p.
• Let b1 < d1 < b2 < d2 < · · · < bp < dp (resp. b(i)
1 < d(i)
1 < b(i)
2 < d(i)
2 < · · · < b(i)
p <
d(i)
p ) be the indices of positions in ∂(λ) (resp. ∂(λ(i))) such that we swap sbq = 1
with sdq = 0 (resp. si
b(i)
q = 1 with s(i)
d(i)
q = 0) when remove ξ
′
q (resp. ξq) from λ (resp.
λ(i)).
Thus, with the above notations in hand, we have
ht(ξ
′
q) = #{t | st = 0, bq ≤t < dq},
ht(ξq) = #{t | s(i)
t
= 0, b(i)
q ≤t < d(i)
q }.
By the definition of Ψm, we hence have
#{t | s(i)
t
= 0, b(i)
q ≤t < d(i)
q } = #{t | st = 0, bq ≤t < dq, t ≡i (mod m)}.
Therefore,
ht(θ
′
i) −ht(θi) =
p
X
q=1
 ht(ξ
′
q) −ht(ξq)

=
p
X
q=1
#{t | st = 0, bq ≤t < dq, t̸ ≡i (mod m)}
=
p
X
q=1
#{t | uq < t ≤vq, at̸ = auq}
(by the definition of a(λ))
=I(θ
′
i)
(by Lemma 7.8).
This finishes the proof.
□
Example 7.11. Figure 7 presents four removal processes corresponding to those of Figure
4. Let us take the leftmost one as an example. We firstly remove a 6-generalized ribbon
θ
′
1 colored by 1, which has two connected components. So ht(θ
′
1) = 2 + 1 = 3. As we
can see, a(λ) = (1, 3, 2, 3, 2, 1, 2, 3) and a(λ \ θ
′
1) = (3, 2, 1, 3, 2, 2, 1, 3). So I(θ
′
1) = 3.
Similarly, we have ht(θ
′
2) = 2 and I(θ
′
2) = 2. Thus, this process contribute the sum term
ur
2(1 −q−2)3(−q−2)0.
7.3. Specialization to Wm,n case. This subsection aims to explain how our result (The-
orem 7.10) reduces to the special case for Wm,n, which was considered in [AR22]. As we
mentioned in section 4, the irreducible character ϕλ can be obtained from χλ by special-
izing u = ζ = (1, ζ, ζ2, · · · , ζm−1) and q = 1, where ζ is the primitive m-th root of unity.
In this case, ηλ
τ;m = 0 unless each partition τ (i) (1 ≤i ≤l(µ(m))) has only one row, i.e.,
τ (i) = (µ(m)
i
). Moreover, only those processes of removing ribbons (not generalized ribbons)
42
NAIHUAN JING AND NING LIU
1
3
2
3
2
1
2
3
3
2
1
3
2
2
1
3
3
2
3
1
2
1
2
3
3
1
3
2
2
2
1
3
3
2
1
3
2
3
3
2
1
2
1
2
3
3
2
3
1
2
1
1
Remove generalized ribbons colored by 1
Remove generalized ribbons colored by 2
Figure 7. Four removal processes corresponding to those in Figure 4. The
sum terms they contribute are same as those in Figure 4.
from λ can contribute the summation. Therefore, if τ ∈Pm(µ(m)), then ηλ
τ;m

u=ζ
q=1
equals
the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(2) Remove a mµ(m)
t
-ribbon θ from λ. If we can not find such a ribbon, set ε = 0 and
end the program.
(3) Multiply ε by (−1)ht(θ)−I(θ).
(4) Redefine τ :=
 (µ(m)
1
), (µ(m)
2
), · · · , (µ(m)
t−1)

and t := t −1.
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
43
(5) Return to step (1).
Let ∅= λ(0) ⊂λ(1) ⊂· · · ⊂λ(r) = λ be a chain such that λ(i+1)/λ(i) is a ribbon. Then
it follows from equation (7.4) that (−1)
Pr−1
i=0 I(λ(i+1)/λ(i)) = (−1)
Pr−1
i=0
 invm(λ(i+1))−invm(λ(i))

=
(−1)invm(λ)−invm(∅). This, together with the above algorithm, implies that
ηλ
τ;m

u=ζ
q=1
= (−1)invm(λ)−invm(∅)γλ
mµ(m).
(7.6)
Here γλ is the irreducible character of the symmetric group indexed by the partition λ
with λ = (λ(1), λ(2), · · · , λ(m)) as its m-quotient, mµ(m) = (mµ(m)
1
, mµ(m)
2
, · · · ) and τ ∈
Pm(µ(m)).
Summarizing above, we get the special case of Theorem 7.10 as below, which firstly
appears in [AR22, Theorem 3.1].
Corollary 7.12. Let λ ⊢mn, µ ⊢n. Suppose the m-quotient of λ is (λ(1), λ(2), · · · , λ(m)).
Then we have
ϕ(λ(1),λ(2),··· ,λ(m))
(∅,··· ,∅,µ)
= (−1)invm(λ)−invm(∅)γλ
mµ,
(7.7)
where ϕ(λ(1),λ(2),··· ,λ(m)) (resp. γλ) is the irreducible character of the complex reflection group
(resp. the symmetric group) indexed by (λ(1), λ(2), · · · , λ(m)) (resp. λ).
Proof. Taking specialization u = ζ, q = 1 and µ = (∅, · · · , ∅, µ) on both sides of (7.5)
gives that
ϕ(λ(1),λ(2),··· ,λ(m))
(∅,··· ,∅,µ)
= ηλ
((µ(m)
1
),(µ(m)
2
),··· ,);m

u=ζ
q=1
,
(7.8)
which, together with (7.6), yields (7.7). As desired.
□
Remark 7.13. It would be interesting to find a representation-theoretic interpretation of
P
τ∈Pm(µ(m)) ηλ
τ;m (up to an explicit normalization factor, e.g. involving qn−l(µ(m)) and possi-
bly a power of −q−2), for λ with empty m-core and m-quotient (λ(1), λ(2), · · · , λ(m)). More
precisely, one may ask whether this quantity arises as the value of a natural character (or
virtual character) associated with a suitable algebra related to Hm,n(q, u), for example a
subalgebra, a corner algebra, or a quotient/subquotient, evaluated at an element correspond-
ing to g((∅, · · · , ∅, µ(m))). In the Wm,n case, this interpretation is given by the symmetric
group Sn.
