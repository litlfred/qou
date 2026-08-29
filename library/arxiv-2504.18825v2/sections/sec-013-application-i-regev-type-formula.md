---
doc_id: arxiv-2504.18825v2
doc_title: "MURNAGHAN\u2013NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU"
section_id: sec-013-application-i-regev-type-formula
section_title: "Application I: Regev-type formula"
section_number: 6
pages: 25-34
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
doc_brief: "MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU — 16 sections: Introduction; Preliminaries; Murnaghan–Nakayama rule for the cy"
---
In this section, as the first application of our Murnaghan–Nakayama rule, we are devoted to giving the Regev formula for the cyclotomic Hecke algebra Hm,n (q, u). Once the
Murnaghan–Nakayama rule is set up right, the proof of the Regev formula, which is based
on the classical deep work on symmetric groups and Hecke algebras in type A, is remarkably natural. To proceed with it, we initially, in accordance with [Zha24a], review the
permutation super representation of the cyclotomic Hecke algebra Hm,n (q, u), as well as
the Schur–Sergeev duality that exists between a certain quantum superalgebra Uq (g) and
Hm,n (q, u).
We refer to a superspace W as a Z2 -graded vector space with decomposition W =
W0̄ ⊕ W1̄ . An element w ∈ W is homogeneous with degree ī if w ∈ Wī , i = 0, 1. We also
define the dimension of W by dim(W) := dim(W0̄ )|dim(W1̄ ). L
(i)
Let V represent a direct sum of m superspaces, denoted as V = m
. In this context,
i=1 V
(i)
(i)
(i)
(i)
(i)
(i)
we assume dim(V ) = ki |li and {v1 , v2 , · · · , vki , vki +1 , · · · , vki +li } forms a homogeneous
P
P
basis of V (i) . Evidently, dim(V ) = k|l with k =
ki and l =
li . Additionally, B :=
P
(s)
{v1 , v2 , · · · , vk+l } constitutes a homogeneous basis for V with vd = vt if d = si=1 (ki +
li ) + t. The entity c(vi ) = r is defined contingent upon the condition vi ∈ V (r) . The term
c(·) is occasionally referred to as the color function.


26

NAIHUAN JING AND NING LIU

Introduce the linear map ω : V −→ V defined by ω(vi ) = uc(vi ) vi . Define the linear
operators π, σ : V ⊗ V −→ V ⊗ V by

īj̄
−1

(q − q )vi ⊗ vj + (−1) vj ⊗ vi , if i < j;
ī (q+q −1 )
−1
π(vi ⊗ vj ) = (q−q )+(−1)
(6.1)
vi ⊗ v i ,
if i = j;
2


īj̄
(−1) vj ⊗ vi ,
if i > j.
(
π(vi ⊗ vj ),
if c(vi ) = c(vj );
(6.2)
σ(vi ⊗ vj ) =
īj̄
(−1) vj ⊗ vi , if c(vi ) ̸= c(vj ).
We can demonstrate π 2 = (q − q −1 )π + 1, which implies π is invertible and π −1 = π − (q −
q −1 )Id. We canonically extend π and σ to linear maps πi , σi (i = 1, 2, · · · , n − 1) : V ⊗n −→
V ⊗n by
πi±1 := Id⊗(i−1) ⊗ π ±1 ⊗ Id⊗(n−i−1)

(6.3)

σi := Id⊗(i−1) ⊗ σ ⊗ Id⊗(n−i−1)

(6.4)

ωi := Id⊗(i−1) ⊗ ω ⊗ Id⊗(n−i) .

(6.5)

−1
Furthermore, we define π0 := π1−1 π2−1 · · · πn−1
σn−1 · · · σ1 ω1 . As is shown in [Zha24a, Theorem 3.6], the map
⊗n
Ξu,q
k|l;n : Hm,n (q, u) −→ EndK V

gi 7−→ πi−1 ,

i = 1, 2, · · · , n.

gives a (super) representation of Hm,n (q, u), called permutation super representation of
u,q
u,q
Hm,n (q, u). We denote by χu,q
k|l;n (g(µ)) the value of the character χk|l;n of Ξk|l;n on the
standard element g(µ).
Let k = (k1 , k2 , · · · , km ) and l = (l1 , l2 , · · · , lm ) be two compositions. For a given nonnegative integer n, we define the set C(n; k | l) of pairs of m-multicompositions associated
with k and l by


α = (α(1) , · · · , α(m) ) with l(α(i) ) ≤ ki
C(n; k|l) := (α, β)
and |α| + |β| = n .
β = (β (1) , · · · , β (m) ) with l(β (i) ) ≤ li
The main result in this section is the following formula for χu,q
k|l;n (g(µ)), which is referred
to as Regev’s formula.
Theorem 6.1. Let µ be a m-multipartition of n, then the value of the character of the
permutation super representation on the standard element g(µ) is given by
χu,q
k|l;n (g(µ))
(r)

=q

n−l(µ)

m l(µ
Y
Y)

X

r=1 j=1 (α;β)∈C(µ(r) ;k|l)
j

→
ur−
(1 − q −2 )l(α;β)−1 (−q −2 )|β|−l(β)
l (α;β)



m 
Y
ki
li
l(α(i) ) l(β (i) )
i=1
(6.6)


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
27

→
−
where l (α; β) := max{1 ≤ i ≤ m | l(α(i) ) + l(β (i) ) > 0} and l(α; β) := l(α) + l(β).
Remark 6.2. In a recent development, Zhao [Zha24b] has proposed an alternative method
to derive Theorem 6.1. It should be noted that his formulation is slightly different from ours,
due to a distinct choice of presentation of Hm,n (q, u), as well as the standard elements g(µ).
Next we will introduce a series of notations. Let λ be a m-multipartition with diagram
D(λ). A (k, l)-semistandard tableau Tλ of shape λ is a m-tuple of (ki , li )-semistandard
tableaux (cf. [BR87]) obtained by filling each component D(λ(i) ) of D(λ) with variables
(i)
(i)
(i)
(i)
(i)
(i)
{a1 < a2 < · · · < aki < b1 < b2 < · · · < bli , i = 1, 2, · · · , m}, satisfying
(i)

(1) the cells filled with aj ’s form a tableau;
(i)
(2) aj ’s are nondecreasing in rows, strictly increasing in columns;
(i)
(3) bj ’s are nondecreasing in columns, strictly increasing in rows.
Denote sk,l (λ) := #{(k, l)-semistandard tableaux of shape λ}. For a given (α, β) ∈ C(n; k|l),
(i)
we say that a (k, l)-semistandard tableau Tλ is of weight (α, β) if the number of aj (resp.
(i)
(i)
(i)
bj ) in Tλ equals αj (resp. βj ). Furthermore, denote by s(α,β) (λ) the number of all
(k, l)-semistandard tableaux of shape λ with weight (α, β). Clearly we have
X
sk,l (λ) =
s(α,β) (λ)
(6.7)
(α,β)∈C(n;k|l)

for any m-multipartition λ of n.
Define H(k|l; n) := {λ ⊢ n | λk+1 ≤ l}. An element in H(k|l; n) is called a (k, l)-hook
partition. More generally, a multipartition is called a (k, l)-hook multipartition if each λ(i)
is a (ki , li )-hook partition for i = 1, 2, · · · , m. Denote by H(k|l; n) the set of all (k, l)-hook
multipartitions of n. Clearly, H((1m )|(1m ); n) consists of all multipartitions λ of n such
that each component of λ is a hook partition. Note that the assertion in [BR87, Definition
2.4] implies that sk,l (λ) ̸= 0 if and only if λ ∈ H(k|l; n) for a multipartition λ of n.
λ
Now we will express χu,q
usk|l;n as a linear combination of irreducible characters χ
ing the above notations. To continue with this development, the Schur–Sergeev duality
between Hm,n (q, u) and the quantum superalgebra Uq (g) is needed. Where Uq (g) :=
Uq (gl(k1 |l1 )) ⊗ · · · ⊗ Uq (gl(km |lm )), among which Uq (gl(ki |li )), introduced in [BKK00],
is the quantum enveloping superalgebra of gl(ki |li ). V can be a representation of Uq (g),
referred to as vector presentation. The Hopf structure of Uq (g) induces an action on V ⊗n ,
denoted by Θn . As is demonstrated in [BKK00], the irreducible summands of the representation V ⊗n of Uq (gl(k, l)) are indexed by the (k, l)-hook partitions of n, with each
irreducible summand possessing the dimension sk,l (λ). Consequently, the irreducible summands of the representation (Θn , V ⊗n ) of Uq (g) are characterized by the (k, l)-hook partitions of n, with each irreducible summand affording the dimension sk,l (λ).
⊗n
It is confirmed in [Zha24a, Theorem 4.9] that (Ξu,q
) and (Θn , V ⊗n ) satisfy the
k|l;n , V
Schur–Sergeev duality, i.e.,
⊗n
Ξu,q
,
k|l;n (Hm,n (q, u)) = EndUq (g) V

Θn (Uq (g)) = EndHm,n (q,u) V ⊗n

(6.8)


28

NAIHUAN JING AND NING LIU

• •






• •
•

•
•

•

,

•

,






Figure 2. SE(λ/µ) consists of the green boxes. The subset formed by the
boxes with bullets is an element of R9 (λ/µ).
Moreover, as a (Uq (g), Hm,n (q, u)-bimodule,
M
V ⊗n ∼
=

Wλ ⊗ W λ ,

(6.9)

λ∈H(k|l;n)

where Wλ (resp. W ) is the irreducible module of Uq (g) (resp. Hm,n (q, u)) indexed by λ.
This gives the following decomposition:
M
V ⊗n ∼
sk,l (λ)W λ ,
(6.10)
=
λ

λ∈H(k|l;n)

which is equivalent to
χu,q
k|l;n =

X

sk,l (λ)χλ .

(6.11)

λ∈H(k|l;n)

Now we introduce the skew characters of Hm,n (q, u) via the Jacobi–Trudi rule. Let µ ⊂ λ
be two m-multipartitions (with |µ| ≤ |λ|). For each 1 ≤ r ≤ m and a ∈ Z, set
 a
ε

χ r , a ≥ 1,
h(r)
1,
a = 0,
a :=

0,
a < 0,
where 1 denotes the unit character (for the degree 0 algebra). We define
χλ/µ :=

m
[
O
r=1

det

1≤i,j≤l(λ(r) )

(r)

h (r)
λi


(r)
−i−µj +j

,

(6.12)

where the determinant is taken in the character ring with multiplication given by the outer
product.
Next, we will restate our Murnaghan–Nakayama rule in terms of the skew characters.
Before that, we need some terminologies about skew diagrams. Let λ/µ be a m-multi
skew diagram, denote by SE(λ/µ) the subset of λ/µ consisting of the southeast ribbon
which starts from the northeastmost box and ends at the southeastmost box in each connected component in D(λ/µ). We identify a box in the a-th row and the b-th column of
D(λ(i) /µ(i) ) with the coordinate (a(i) , b(i) ), i = 1, 2, · · · , m. Let Rt (λ/µ) be the set of all
subsets R of SE(λ/µ) satisfying
• R has size t;


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
29




















,

Figure 3. An example for Rα,β where α = ((2, 3), (3, 2, 2)) and β =
((2, 2), (3)). The corresponding skew character can be written as χ(α,β) =
ˆ (13 ) .
ˆ (2) ⊗χ
ˆ (2) ⊗χ
ˆ (3) ⊗χ
ˆ (12 ) ⊗χ
ˆ (12 ) ⊗χ
ˆ (3) ⊗χ
χ(2) ⊗χ
• For any (a(i) , b(i) ) ∈ R and (x(i) , y (i) ) ∈ SE(λ/µ) \ R, we have either x(i) < a(i) or
y (i) < b(i) .
Figure 2 presents an example for SE(λ/µ) and Rt (λ/µ). It is not hard to see that for
any m-multi skew diagram D(λ/µ) and R ∈ Rt (λ/µ), D(λ/µ) \ R is still a m-multi skew
diagram. For R ∈ Rt (λ/µ), denote by cc(R) the number of connected components of R.
P
If R has d connected components R1 , R2 , · · · , Rd , define ht(R) := di=1 ht(Ri ).
Let ν ∈ P|λ|−|µ|,m , and fix 1 ≤ r ≤ m, 1 ≤ j ≤ l(ν (r) ). Then we have the following
skew-diagram version of the Murnaghan–Nakayama rule:
X
(r)
(λ/µ)\R
−2 cc(R)−1
→ (1 − q )
χλ/µ
= q νj −1
ur−
(6.13)
(−q −2 )ht(R) χ (r) .
ν
R
ν\νj

R∈R (r) (λ/µ)
ν
j

Here

→
−
R := max{1 ≤ i ≤ m | there exists at least one box of R in λ(i) /µ(i) }.
Equation (6.13) can be deduced from Corollary 3.4 using arguments similar to those in
[JK81, Chap. 2.4] (see also [Zha19, Theorem 5.2]). More precisely, one applies Corollary
3.4 to the terms arising from the Jacobi–Trudi determinant expansion defining χλ/µ , and
then regroups the resulting terms according to the subsets R ∈ Rν (r) (λ/µ) of SE(λ/µ).
j

(λ/µ)\R

The regrouped terms are precisely the skew characters χ
.
For (α, β) ∈ C(n; k|l), denote by Rα,β some (any) m-multi skew diagrams D(λ/µ) (This
is not unique!) such that the connected components of D(λ(i) /µ(i) ) are horizontal strips
(i)
(i)
(i)
(i)
(i)
(i)
H1 , H2 , · · · , Hki and vertical strips V1 , V2 , · · · , Vli (i = 1, 2, · · · , m) satisfying
(i)

(i)

(i)

(i)

(i)

(i)

(i)

(H1 , H2 , · · · , Hki ) = (α1 , α2 , · · · , αki ),

(i)

(i)

(i)

(i)

(i)

(V1 , V2 , · · · , Vli ) = (β1 , β2 , · · · , βli ).
(6.14)

For Rα,β , define the character related to Rα,β by
χ(α;β) :=

O
[

χ

(i)
(α1 )

(i)
(αk )
i

ˆ · · · ⊗χ
ˆ
⊗

1≤i≤m

See Figure 3 for an example for Rα,β .

(i)
(1β1 )

ˆ
⊗χ

(i)
(1 li )

ˆ · · · ⊗χ
ˆ
⊗

β

!
.

(6.15)


30

NAIHUAN JING AND NING LIU

Due to [BR87, Lemma 3.23] (see also [Tay17, Lemma 3.2], [Zha19, Corollary 5.5]), we
have the following decomposition for χ(α;β) in terms of irreducible characters.
X
χ(α;β) =
s(α,β) (λ)χλ .
(6.16)
λ∈H(k|l;n)

Now we restate our skew version of the Murnaghan–Nakayama rule in a special case.
Rα,β is a m-multi skew diagram as mentioned above. Then
Rt (Rα,β ) = {Rγ,δ | (γ, δ) ⊂ (α, β), |γ| + |δ| = t}.

(6.17)

Furthermore, if Rγ,δ ∈ Rt (Rα,β ), then we have cc (Rγ,δ ) = l(γ) + l(δ) = l(γ; δ), ht(Rγ,δ ) =
−
−−→ →
|δ| − l(δ) and Rγ,δ = l (γ; δ). We can restate (6.13) in the following special setting.
X
(r)
(α;β)\(γ;δ)
→
χ(α;β)
= q νj −1
ur−
(1 − q −2 )l(γ;δ)−1 (−q −2 )|δ|−l(δ) χ (r)
.
(6.18)
ν
l (γ,δ)
ν\νj

(γ,δ)⊂(α,β)
(r)
|γ|+|δ|=νj

We are ready to prove Theorem 6.1.
Proof of Theorem 6.1.
χu,q
k|l;n (g(µ))
X
=
sk,l (λ)χλ

(by (6.11))

λ∈H(k|l;n)

=

X

X

s(α,β) (λ)χλ

(by (6.7))

λ∈H(k|l;n) (α,β)∈C(n;k|l)

=

X

χ(α;β)

(by (6.16))

(α,β)∈C(n;k|l)

=

X

(r)

q µj −1

(α,β)∈C(n;k|l)

X

(α;β)\(γ;δ)

→
ur−
(1 − q −2 )l(γ;δ)−1 (−q −2 )|δ|−l(δ) χ
l (γ,δ)

′

(r)

′

(r)

µ\µj

(γ,δ)⊂(α,β)
(r)
|γ|+|δ|=µj
′

′

(by (6.18)).

For a given (α , β ) ∈ C(n − µj ; k|l), if (α, β) \ (γ, δ) = (α , β ), then the number of
(γ, δ)’s contributing the coefficient
(r)

→
q µj −1 ur−
(1 − q −2 )l(γ;δ)−1 (−q −2 )|δ|−l(δ)
l (γ,δ)

is exactly


m 
Y
ki
li
.
(i) )
(i) )
l(γ
l(δ
i=1
Therefore,
χu,q
k|l;n (g(µ))


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
31


(r)

X


=

→
q µj −1 ur−
(1 − q −2 )l(γ;δ)−1 (−q −2 )|δ|−l(δ)
l (γ,δ)

i=1

(r)

(γ,δ)∈C(µj ;k|l)
′

X

×
′

′

m 
Y

χ
(r)

ki
l(γ (i) )





li


(i)
l(δ )

′

(α ;β )
(r)
µ\µj

.

(α ,β )∈C(n−µj ;k|l)

An induction argument completes the proof.
□
m
m
Next, we consider the special case (k|l) = ((1 )|(1 )). It follows from the proof of
Theorem 6.1 that
X
χu,q
=
χ(α;β) .
(6.19)
m
m
(1 )|(1 );n
(α,β)∈C(n;(1m )|(1m ))

Note that every (α, β) in C(n; (1m )|(1m )) has the form
(α, β) = ((α1 ), (α2 ), · · · , (αm ), (β1 ), (β2 ), · · · , (βm ))
with

Pm

i=1 (αi + βi ) = n. So

X

RHS of (6.19) =

ci
O X
[

χ(αi ;ci −αi ) .

(6.20)

if ci = 0;
if ci ≥ 1.

(6.21)

c1 +c2 +···+cm =n 1≤i≤m αi =0
ci ≥0

By [Tay17, Remark 3.3],
(
1
Pci −1 (ci −αi ,1αi )
χ(αi ;ci −αi ) =
2
αi =0 χ
α =0
ci
X
i

Substituting this into (6.20) gives that
RHS of (6.19) =

X

2L(λ) χλ .

(6.22)

λ∈H((1m )|(1m );n)

Recall that H((1m )|(1m ); n) consists of all m-multipartitions λ of n such that each component λ(i) is a hook partition. Here L(λ) := #{1 ≤ i ≤ m | λ(i) ̸= ∅}.
On the other hand, by (6.6),
(r)

n−l(µ)
χu,q
(1m )|(1m );n (g(µ)) = q

m l(µ
Y
Y) X

→
ur−
(1 − q −2 )l(α)+l(β)−1 (−q −2 )|β|−l(β)
l (α;β)

r=1 j=1 (α;β)
(r)

the inner sum runs over all pairs of m-compositions (α; β) with |α| + |β| = µj .

(6.23)


32

NAIHUAN JING AND NING LIU

Note that
X

→
(1 − q −2 )l(α)+l(β)−1 (−q −2 )|β|−l(β)
ur−
l (α;β)

(α;β)
(r)
|α|+|β|=µj

=

1
1 − q −2

X
(r)

X

X

→
ur−
c
(r)

c1 +c2 +···+cm =µj
ci ≥0

X

=

(−q −2 )

Pm

i=1 (βi +δβi ,0 −1)

i=1
(α;β)
|α|+|β|=ci

(r)

1
1 − q −2

i=1 (2−δβi ,ci −δβi ,0 )

m
Y
(1 − q −2 )2−δβi ,ci −δβi ,0 (−q −2 )βi +δβi ,0 −1

X

→
ur−
c

c1 +c2 +···+cm =µj
ci ≥0

=

(1 − q −2 )

(α;β)
|α|+|β|=ci

c1 +c2 +···+cm =µj
ci ≥0

1
=
1 − q −2

Pm

X

→
ur−
c

ci
m X
Y

(1 − q −2 )2−δβi ,ci −δβi ,0 (−q −2 )βi +δβi ,0 −1

i=1 βi =0

#c
−2 #c−1
→
ur−
c 2 (1 − q )

m
Y
[ci ]−q−2 ,
i=1

(r)

c1 +c2 +···+cm =µj
ci ≥0

(6.24)
−c := max{1 ≤ i ≤ m | c ̸= 0}, c := {1 ≤ i ≤ m | c ̸= 0} and [k] := 1−q (Here
where →
i
i
q
1−q
k ≥ 0 and [0]q := 1) is the standard q-integer. The last equation holds for the following
identity:
(
ci
X
2(1 − q −2 )[ci ]−q−2 if ci > 0
(1 − q −2 )2−δβi ,ci −δβi ,0 (−q −2 )βi +δβi ,0 −1 =
1
if ci = 0.
β =0
k

i

We say that a m-tuple of matrices (M (1) , M (2) , · · · , M (m) ) is a m-multimatrix if each
M (i) has m columns with entries nonnegative integers. Denote by Mm the set of all mmultimatrices. For a m-multimatrix M = (M (1) , M (2) , · · · , M (m) ), define
r(M ) :=

m
X
i=1

(i)

r(M (i) ),

uM :=

m r(M
Y
Y)
i=1

ui−
→
r j (M (i) ) .

j=1

−
Here we use the notations r(M ) and →
r j (M (i) ) to present the number of rows in matrix
→
M (i) and the j-th row vector of matrix M (i) , respectively. Thus u−
r j (M (i) ) = ufij with fij
the column containing the first non-zero element from right to left in the jth row of M (i) .
For instance, if






2 0 0

3 2 0
2, 2, 0  .
M =
, 0 4 2 ,
(6.25)
0 1 6
8 0 0
(i)


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
33

We have marked the last non-zero element in each row in orange. Thus,

 

 
1

2
2  , uM = u41 u42 u33 .
(fij ) = 
, 3 ,
3
1
Substituting (6.24) into (6.23) gives that
Y
X
(r)
#M
−1 #M −l(µ)
[mij ]−q−2 ,
(g(µ))
=
u
2
(q
−
q
)
χu,q
M
m
l
(1 )|(1 );n
M

(6.26)

(r)
mij ∈M

summed over all m-multimatrices (M (1) , · · · , M (m) ) ∈ Mm such that the j-th row sum of
(r)
M (r) equals µj . Where #M is the number of nonzero entries in M .
Now we have obtained the following result.
Corollary 6.3. Let µ be a multipartition of n. Then we have the following combinatorial
formula, which is also referred as the Regev formula.
X
X
Y
(r)
uM 2#M (q − q −1 )#M −l(µ)
(6.27)
[mij ]−q−2 ,
2L(λ) χλµ =
λ⊢n
all λ(i) hook

M

(r)

mij ∈M

summed over all m-multimatrices (M (1) , · · · , M (m) ) such that the jth row sum of M (r)
(r)
equals µj .
Proof. It follows from (6.19), (6.22) and (6.26) by noticing that H((1m )|(1m ); n) consists
of all multipartitions λ of n with each component λ(i) being hook shape.
□
Remark 6.4. We remark that Zhao [Zha24b] obtained an asymptotic formula for the LHS
of (6.27). It is pertinent to point out that an alternative proof for Corollary 6.3 is presented
by establishing a connection between the irreducible characters of Hm,n (q, u) and those of
Hecke algebra in type A. This proof relies on the Regev formula for Hecke algebra in type
A. To prevent redundancy, we leave this proof in the appendix A.
Recall that Hm,n (q, u) will reduce to Hecke algebra Hn (q) (resp. complex reflection group
Wm,n ) when m = 1, u1 = 1 (resp. q = 1, u = {1, ζ, · · · , ζ m−1 }). Here ζ is the primitive
m-th root of unity. Before closing this section, we want to examine how the Regev formula
adapts in these two special cases. To do so, we will analyze each case individually. For the
first case, i.e., m = 1, u1 = 1, it is easy to see (6.27) is degraded to
X
λ hook

ψµλ = 2l(µ)−1

l(µ)
Y
[µi ]−q−2 .

(6.28)

i=1

Where ψ λ is the irreducible character of Hn (q) indexed by λ. This is exactly the Regev
formula for the Hecke algebra in type A established in [JL22, Zha19]. For the second case,


34

NAIHUAN JING AND NING LIU

i.e., q = 1, u = {1, ζ, · · · , ζ m−1 }, we have
X

#M

uM 2

M

−1 #M −l(µ)

(q − q )

Y

(r)
[mij ]−q−2 =

(r)
mij ∈M

P
 uM 2l(µ)

(r)

if all µj ’s are odd

M

0

otherwise

summed over all m-multimatrices M such that j-th row of M (r) has only one nonzore
(r)
(r)
entry µj . Moreover, if all µj ’s are odd, then
(
(r)
(1)
m l(µ
m
X
Y
Y) X
(2m)l(µ ) , if µ = (µ(1) , 0, · · · , 0);
l(µ)
(r−1)i
uM 2
=
2
ζ
=
0,
otherwise.
r=1 j=1
i=1
M
The last equation holds for the following identity:
(
m
X
m, if r = 1;
ζ (r−1)i =
0, if 1 < r ≤ m.
i=1
We have reached the Regev formula for Wm,n .
Corollary 6.5. Suppose µ is a m-multipartition of n, then
(
(1)
X
(2m)l(µ ) , if µ = (µ(1) , 0, · · · , 0) with all parts odd;
λ
ϕµ =
0,
otherwise.
λ⊢n

(6.29)

λ(i) hook

Where ϕλ is the irreducible character of Wm,n indexed by multipartition λ.
