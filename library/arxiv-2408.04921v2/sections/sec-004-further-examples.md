---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING"
section_id: sec-004-further-examples
section_title: "Further examples"
section_number: 4
pages: 13-24
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING — 5 sections: Introduction; Irreducible characters of Ck ≀ Sn; X ij"
---
For completeness, we first calculate the degree of any irreducible character
of Ck ≀ Sn [7]. Recall that the inner product in V is given by:
ha−λ , a−µ i =

k−1
Y

ha−λ(i) , a−µ(i) i = δλµ

k−1
Y

zλ(i) .

(4.1)

i=0

i=0

Under this inner product the wreath Schur functions are orthonormal:
hsλ , sµ i =

k−1
Y

hsλ(i) , sµ(i) i = δλµ .

i=0

(4.2)


14

HUIMIN GAO AND NAIHUAN JING

Then we have
hsλ , a−µ i =

k−1
Y

hsλ(i) , a−µ(i) i.

(4.3)

i=0

The following result is well-known for the wreath products and is included
here using the vertex operator approach.
Theorem 4.1. [20] For any colored partition λ = (λ(0) , λ(1) , · · · , λ(k−1) ) of
n, the degree of the irreducible character χλ of Ck ≀ Sn is given by
n!
χλ (1) = Qk−1
,
(i)
i=0 h(λ )

(4.4)

where 1 = ((1n ), ∅, · · · , ∅) and h(λ(i) ) is the hook length of λ(i) .
Pk−1
Proof. By definition, χλ (1) = hsλ , (e
a−01 )n i = hsλ , ( j=0
a−j1 )n i. The nonzero items are only
hsλ ,

k−1
Y

|λ(j) |

a−j1 i =

k−1
Y

|λ(j) |

hsλ(j) , a−j1 i =

j=0

j=0

k−1
Y

|λ(j) |!
,
(j) )
h(λ
j=0

where the second equality has used the degree formula of irreducible charQk−1 |λ(j) |
Pk−1
a−j1 in ( j=0
a−j1 )n equals
acters in Sλ(j) . Since the coefficient of j=0
to
(0) |

Cn|λ

and the theorem is proved.

n!
|λ(1) |
Cn−|λ(0) | · · · = Qk−1
,
(j)
j=0 |λ |!



Corollary 4.2. Given colored partitions λ = (λ(0) , λ(1) , · · · , λ(k−1) ) of n,
let κj be a colored partition supported only at the j-th constituent (1n ), and
ω be the k-th primitive root of unity. Then we have
ω −deg(λ)j n!
,
χλ
κj = Qk−1
(i) )
h(λ
i=0

(4.5)

where deg(λ) is defined as the sum of i|λ(i) |.

In the dual case, one has the following result.
Proposition 4.3. Given a colored partition ρ = (ρ(0) , ρ(1) , · · · , ρ(k−1) ) of
n, the irreducible character value is
j

−η(ρ)j
χκ
(−1)l(ρ)+n ,
ρ =ω

(4.6)

where κj is a colored partition
only at the j-th constituent (1n ),
P supported
(i)
η(ρ) is the weighted length i il(ρ ).


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

15

aρ i is
Proof. In view of (4.3), the only nonzero factor of hsκj , e
hsj(1n ) ,

k−1
Y

(i) |

ω −ij|ρ

a−jρ(i) i

i=0

Qk−1
since |λ(j) | exhausts n. Note that i=0
a−jρ(i) can be written as a−jρ , where
ρ is the rearrangement of ρ.
(1n )
For the character value χρ , we apply Theorem 3.10 with induction on
(1)
n. First χ(1) = 1 is clear. The inductive hypothesis says that
(1n−1 )

χ(ρ\µ)∪τ = (−1)l(ρ)−l(µ)+l(τ )+n−1 .
Note that

X 1
λ⊢n

Then

zλ

n

= 1.

)
χ(1
= (−1)l(ρ)+n−1
ρ

X

(−1)l(µ) ,

µ⊳ρ,|µ|≥1

where the sum is over all nonempty subpartitions µ ⊳ ρ, which is an alternating sum of binomial coefficients:


l(ρ)
X
l(ρ)
0
(−1)k
= −Cl(ρ)
= −1,
k
k=1

Qk−1 −ij|ρ(i) |
(1n )
= (−1)l(ρ)+n . Obviously l(ρ) = l(ρ), and i=0
Therefore χρ
ω
j
equals to ω −η(ρ)j , subsequently we have shown χκ
is
given
as
stated.

ρ
Next we move on to study a relationship between irreducible character
values of Ck ≀ Sn and those of Skn mod k. Note that k does not have to be
a prime.
Recall that the k-core γλ of partition λ = (λ1 , λ2 , · · · , λl ) is defined by
removing all k-rim hooks of λ. For example, let λ = (4, 2, 1), k = 3,

→ × ×
×

× × ×
→ × ×
×

then the 3-core of λ is (1).
Let T = T (λ) be the set of paths from partition λ to its core γλ , where
each path is a procedure of removing k-rim hooks. For each path t ∈ T ,
denote by ht(t) the sum of heights of k-rim hooks in path t. It is known
that σλ := (−1)ht(t) is well defined and independent of the paths in T (λ)
[16, Prop. 2.2]. For example, the 3-core of λ = (5, 4, 3, 2) is (2). Consider
two paths t1 , t2 ∈ T as follows. t1 has ht(t1 ) = 5:


16

HUIMIN GAO AND NAIHUAN JING

→

× ×
×

× ×
×

× ×
×
→

× × ×
× × ×
× × ×
→ × × × ×
× ×
× × ×
×
× ×

while t2 has ht(t2 ) = 3:
× × ×
×
×
×
×
×
×
×
×
× ×
→
→
→
× ×
× × ×
× × ×
× ×
× ×
× ×
so σλ equals to −1.
The k-quotient β λ of λ can be constructed as follows. Choose m as a
multiple of k such that m ≥ l(λ), let δm = (m−1, m−2, · · · , 1, 0), ξ = λ+δm ,
which is a strict partition. For each 0 ≤ r ≤ k − 1, suppose there are mr
parts ξi that are congruent to r mod k. Each of these ξi (1 ≤ i ≤ mr ) is
divided by k and reordered as
× ×
×

ξi = k · ξs(r) + r
(r)

(r)

(r)

such that ξ1 > ξ2 > · · · > ξmr ≥ 0. So for each 0 ≤ r ≤ k − 1, we
(r)
(r)
(r) (r)
(r)
obtain a partition λ(r) = (λ1 , λ2 , · · · , λmr ) by letting λs = ξs − mr + s
(1 ≤ s ≤ mr ). Now the colored partition (λ(0) , λ(1) , . . . , λ(k−1) ) = β λ is the
k-quotient of λ.
For example, given λ = (4, 2, 1) and k = 3 as above. Take m = 3, then
ξ = (6, 3, 1), m0 = 2, m1 = 1 and m2 = 0. We have
(0)

λ1 = 2 − 2 + 1 = 1,

(0)

λ2 = 1 − 2 + 2 = 1;

(1)

λ1 = 0 − 1 + 1 = 0,

thus the 3-quotient of λ is ((1, 1), ∅, ∅).
The above procedure shows that any partition λ determines its k-core γλ
and k-quotient β λ uniquely. Moreover,
|λ| = k · kβ λ k + |γλ |.
In fact, λ also can be determined uniquely by γλ and βλ conversely (cf. [15,
I.I. Ex. 8]).
For convenience, we define the standard form of an irreducible character
value of Ck ≀ Sn . According to Theorem 3.5, each χλ
ρ can be written as
c0 + c1 ω + · · · + ck−1 ω k−1 , ci ∈ Z
since the coefficients of the recursive formula lie in Z[ω]. However, k-tuple
(c0 , c1 , · · · , ck−1 ) is not unique due to 1 + ω + · · · + ω k−1 = 0. Indeed,
c0 + c1 ω + · · · + ck−1 ω k−1 = c′0 + c′1 ω + · · · + c′k−1 ω k−1


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

17

if and only if c0 − c′0 = c1 − c′1 = · · · = ck−1 − c′k−1 . For example, the values
(∅,(2),(1))

of χ(∅,(1),(1,1)) can be
..
.
2 + ω + 3ω 2
1 + 2ω 2
−ω + ω 2
...
The standard form is the unique form such that the sum of ci lies in the
color set I = {0, 1, . . . , k − 1}. We also denote by d(χλ
ρ ) the sum of ci in the
2
standard form. Then −ω + ω is the standard form in the above example,
(∅,(2),(1))
and d(χ(∅,(1),(1,1)) ) = 0.
Theorem 4.4. (Relation between Ck ≀ Sn and Skn ) Given colored partitions
λ and ρ of n. Let λ be the partition of kn with the k-core ∅ and k-quotient
λ, and let ρ be the rearrangement of kρ. Then
λ
d(χλ
ρ ) = σλ (χρ

mod

k).
(0)

Proof. Let P be the set of paths from λ to ∅ that remove colored |ρ1 |(0)
(k−1)
rim hooks, colored |ρ2 |-rim hooks,..., colored |ρl(k−1)−1 |-rim hooks, colored
(k−1)

|ρl(k−1) |-rim hooks. By Theorem 3.5 it follows that the irreducible character
value χλ
ρ of Ck ≀ Sn can be written as
X
χλ
σp ω(p),
ρ =
p∈P

where the sum is over all paths p ∈ P and σp := (−1)ht(p) with ht(p) being
the sum of all colored rim-hook heights in path p. Note that ω(p) equals to
some power of ω depending on p. Suppose the standard form of χλ
ρ is of the
Pk−1
i
following form: i=0 ci ω .
On the other hand, let P̃ be the set of paths from λ to ∅ that remove
k|ρ1 |-rim hooks, k|ρ2 |-rim hooks,..., and k|ρl(λ) |-rim hooks. By the ordinary
Murnaghan-Nakayama rule of Skn , we have that
X
χλρ =
σp̃ ,
p̃∈P̃

where σp̃ = (−1)ht(p̃) is defined similarly as σp . It is known that σp and σp̃
are related by the fundamental relation [20]:
σp = σλ σp̃ .

(4.7)
P
and there is a bijection between the sets P and P̃ . This implies that i ci
in the standard form equals to σλ · χλρ mod k, which finishes the proof. 


18

HUIMIN GAO AND NAIHUAN JING

Finally we discuss how to implement our iterative formulas using the
SageMath program.
An algorithm design for Theorem 3.5 to display all coefficients of the MN
rule is as follows:
Step 1) Given two colored partitions of length k and weight n, named λ and
ρ;
Step 2) Assume the largest part (of weight m) in ρ be removed (to reduce
the times of iterations), list all colored partitions of weight n − m included
in λ;
Step 3) Filter out colored partitions λj such that skew partition λ − λj is
a rim hook, and compute the corresponding coefficient.
An algorithm outline of listing all coefficients for Theorem 3.9 goes as
follows.
Step 1) Given two colored partitions of length k and weight n, named λ and
ρ;
Step 2) Identify and remove the largest part in λ (of weight s), filter out subpartitions µ of ρ with weight less than or equal to n − s, and corresponding
partitions τ of size n − s − |µ|, then compute the corresponding coefficients;
Step 3) List all possible colored partitions τ corresponding τ , also compute
each of coefficient.
To end this section, we list the character tables of C3 ≀ S1 , C3 ≀ S2 , C3 ≀ S3 ,
we denote by ω the 3-rd primitive root of unity.
Table 1. C3 ≀ S1
γ\c c1 c2 c3
γ1
1
1 1
γ2 ω ω 2 1
γ3 ω 2 ω 1
where γ1 = c3 = ((1), ∅, ∅); γ2 = c2 = (∅, (1), ∅); γ3 = c1 = (∅, ∅, (1)).
Table 2. C3 ≀ S2
γ\c c1
c2
γ1
1
1
γ2
1
-1
γ3 2ω
0
γ4 2ω 2 0
γ5 ω 2
ω
γ6 ω 2 -ω
γ7
2
0
γ8
ω
ω2
γ9
ω -ω 2

c3 c4
c5
c6
c7 c8
1
1
1
1
1
1
1
1
-1
1
1
1
-1 2ω 2 0 -ω 2 -ω 2
-1 2ω
0
-ω -ω 2 2
1
ω
ω2
ω
ω2 1
2
1
ω -ω
ω
ω2 1
-1 2
0
-1
-1 2
2
2
1 ω
ω ω
ω
1
1 ω 2 -ω ω 2
ω
1

c9
1
-1
0
0
1
-1
0
1
-1


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

19

where γ1 = c9 = ((2), ∅, ∅); γ2 = c8 = ((1, 1), ∅, ∅); γ3 = c7 = ((1), (1), ∅);
γ4 = c6 = ((1), ∅, (1)); γ5 = c5 = (∅, (2), ∅); γ6 = c4 = (∅, (1, 1), ∅); γ7 =
c3 = (∅, (1), (1)); γ8 = c2 = (∅, ∅, (2)); γ9 = c1 = (∅, ∅, (1, 1)).

Table 3. C3 ≀ S3
γ\c

c1

c2

c3

c4

c5

c6

c7

c8

c9

c10

c11

c12

c13

c14

c15

c16

c17

c18

c19

c20 c21 c22

γ1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

γ2

2

0

-1

2

0

2

0

2

0

-1

2

0

2

2

0

2

0

2

0

2

0

-1

γ3

1

-1

1

1

-1

1

-1

1

-1

1

1

-1

1

1

-1

1

-1

1

-1

1

-1

1

γ4

3ω

ω

0

ω-1

ω2

ω 2 -1

ω

3ω 2

ω2

0

ω − ω2

1

0

ω2 − ω

1

1-ω 2

ω

1-ω

ω2

3

1

0

γ5

3ω

-ω

0

ω-1

-ω 2

ω 2 -1

-ω

3ω 2 -ω 2

0

ω − ω2

-1

0

ω2 − ω

-1

1-ω 2

-ω

1-ω

-ω 2

3

-1

0

γ6

3ω 2

ω2

0

ω 2 -1

ω

ω-1

ω2

3ω

ω

0

ω2 − ω

1

0

ω − ω2

1

1-ω

ω2

1-ω 2

ω

3

1

0

γ7

3ω 2 -ω 2

0

ω 2 -1

-ω

ω-1

-ω 2

3ω

-ω

0

ω2 − ω

-1

0

ω − ω2

-1

1-ω

-ω 2

1-ω 2

-ω

3

-1

0

γ8

3ω 2

ω

0

1-ω

ω

1-ω 2

ω2

3ω

ω2

0

ω-1

ω

0

ω 2 -1

ω2

ω − ω2

1

ω2 − ω

1

3

1

0

γ9

3ω 2

-ω

0

1-ω

-ω

1-ω 2

-ω 2

3ω

-ω 2

0

ω-1

-ω

0

ω 2 -1

-ω 2 ω − ω 2

-1

ω2 − ω

-1

3

-1

0

γ10

6

0

0

0

0

0

0

6

0

0

0

0

-3

0

0

0

0

0

6

0

0

γ11

3ω

ω2

0

1-ω 2

ω2

1-ω

ω

3ω 2

ω

0

ω 2 -1

ω2

0

ω-1

ω

ω2 − ω

1

ω − ω2

1

3

1

0

γ12

3ω

-ω 2

0

1-ω 2

-ω 2

1-ω

-ω

3ω 2

-ω

0

ω 2 -1

-ω 2

0

ω-1

-ω

ω2 − ω

-1

ω − ω2

-1

3

-1

0

γ13

1

ω2

ω

ω

1

ω2

1

1

ω

ω2

ω2

ω

1

ω

ω2

ω

ω

ω2

ω2

1

1

1

γ14

2

0

-ω

2ω

0

2ω 2

0

2

0

-ω 2

2ω 2

0

2

2ω

0

2ω

0

2ω 2

0

2

0

-1

γ15

1

-ω 2

ω

ω

-1

ω2

-1

1

-ω

ω2

ω2

-ω

1

ω

-ω 2

ω

-ω

ω2

-ω 2

1

-1

1

γ16

3ω

1

0

ω2 − ω

ω2

ω − ω2

ω

3ω 2

1

0

1-ω

ω

0

1-ω 2

ω2

ω-1

ω2

ω 2 -1

ω

3

1

0

γ17

3ω

-1

0

ω 2 − ω -ω 2 ω − ω 2

-ω

3ω 2

-1

0

1-ω

-ω

0

1-ω 2

-ω 2

ω-1

-ω 2

ω 2 -1

-ω

3

-1

0

γ18

3ω 2

1

0

ω − ω2

ω

ω2 − ω

ω2

3ω

1

0

1-ω 2

ω2

0

1-ω

ω

ω 2 -1

ω

ω-1

ω2

3

1

0

γ19

3ω 2

-1

0

ω − ω2

-ω

ω 2 − ω -ω 2

3ω

-1

0

1-ω 2

-ω 2

0

1-ω

-ω

ω 2 -1

-ω

ω-1

-ω 2

3

-1

0

γ20

1

ω

ω2

ω2

1

ω

1

1

ω2

ω

ω

ω2

1

ω2

ω

ω2

ω2

ω

ω

1

1

1

γ21

2

0

-ω 2

2ω 2

0

2ω

0

2

0

-ω

2ω

0

2

2ω 2

0

2ω 2

0

2ω

0

2

0

-1

γ22

1

-ω

ω2

ω2

-1

ω

-1

1

-ω 2

ω

ω

-ω 2

1

ω2

-ω

ω2

-ω 2

ω

-ω

1

-1

1

0

where γ1 = c22 = ((3), ∅, ∅); γ2 = c21 = ((2, 1), ∅, ∅); γ3 = c20 = ((1, 1, 1), ∅, ∅);
γ4 = c19 = ((2), (1), ∅); γ5 = c18 = ((1, 1), (1), ∅); γ6 = c17 = ((2), ∅, (1));
γ7 = c16 = ((1, 1), ∅, (1)); γ8 = c15 = ((1), (2), ∅); γ9 = c14 = ((1), (1, 1), ∅);
γ10 = c13 = ((1), (1), (1)); γ11 = c12 = ((1), ∅, (2)); γ12 = c11 = ((1), ∅, (1, 1));
γ13 = c10 = (∅, (3), ∅); γ14 = c9 = (∅, (2, 1), ∅); γ15 = c8 = (∅, (1, 1, 1), ∅);
γ16 = c7 = (∅, (2), (1)); γ17 = c6 = (∅, (1, 1), (1)); γ18 = c5 = (∅, (1), (2));
γ19 = c4 = (∅, (1), (1, 1)); γ20 = c3 = (∅, ∅, (3)); γ21 = c2 = (∅, ∅, (2, 1));
γ22 = c1 = (∅, ∅, (1, 1, 1)).

Moreover, by Theorem 4.4, one has


20

HUIMIN GAO AND NAIHUAN JING

Table 4. S9 mod 3
λ\c
(9) (6, 3) (3, 3, 3)
(7, 1, 1)
1
1
1
(4, 1, 1, 1, 1, 1)
2
0
2
(1, 1, 1, 1, 1, 1, 1, 1, 1) 1
2
1
(4, 3, 2)
0
2
0
(2, 2, 2, 1, 1, 1)
0
2
0
(4, 4, 1)
0
1
0
(3, 2, 1, 1, 1, 1)
0
1
0
(5, 2, 2)
0
1
0
(2, 2, 2, 2, 1)
0
1
0
(3, 3, 3)
0
0
0
(6, 2, 1)
0
2
0
(3, 2, 2, 2)
0
2
0
(8, 1)
2
2
2
(5, 1, 1, 1, 1)
1
0
1
(2, 1, 1, 1, 1, 1, 1, 1)
2
1
2
(5, 4)
0
2
0
(3, 3, 1, 1, 1)
0
2
0
(6, 3)
0
1
0
(3, 3, 2, 1)
0
1
0
(9)
1
1
1
(6, 1, 1, 1)
2
0
2
(3, 1, 1, 1, 1, 1, 1)
1
2
1
where λ corresponds to γ1 ∼ γ22 . They are consistient with the elements
in the character table of S9 mod 3.
Acknowledgments
The work is supported in part by the Simons Foundation grant no. MPTSM-00002518 and the National Natural Science Foundation of China grant
nos. 12171303.
References
[1] A. M. Adin, Y. Roichman, On characters of wreath products, Comb. Theory 2 (2022),
no. 2, Paper No. 17, 12 pp.
[2] S. Ariki, K. Koike, A Hecke algebra of Z/rZ ≀ Gn and construction of its irreducible
representations, Adv. Math. 106 (1994), 216-243.
[3] J. Bandlow, A. Schilling, M. Zabrocki, The Murnaghan-Nakayama rule for k-Schur
functions, J. Combin. Theory Ser. A. 118 (2011), 1588-1607.
[4] A. Evseev, R. Paget, M. Wildon, Character deflations and a generalization of the
Murnaghan-Nakayama rule, J. Group Theory 17(2014), 1035-1070.
[5] I. B. Frenkel, N. Jing, W. Wang, Vertex representations via finite groups and the
McKay correspondence, Int. Math. Res. Not. IMRN 4 (2000), 195-222.


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

21

[6] T. Halverson, A. Ram, Murnaghan-Nakayama rules for characters of Iwahori-Hecke
algebras of classical type, Trans. Amer. Math. Soc. 348 (1996), 3967-3995.
[7] F. Ingram, N. Jing, E. Stitzinger, Wreath product symmetric functions, Int. J. Algebra
3 (2009), 1–19.
[8] G. James, A. Kerber, The Representation theory of the symmetric group, Encyclopedia Math. App. 16, 1981.
[9] N. Jing, Vertex operators, symmetric functions, and the spin group Γn , J. Algebra
138 (1991), 340-398.
[10] N. Jing, Vertex operators and Hall-Littlewood symmetric functions, Adv. Math. 87
(1991), 226-248.
b 2 ), Represent. Theory 4 (2000), 46-63.
[11] N. Jing, Symmetric polynomials and Uq (sl
[12] N. Jing, N. Liu, Murnaghan-Nakayama rule and spin bitrace for the Hecke-Clifford
algebra, Int. Math. Res. Not. IMRN 19 (2023), 17060-17099.
[13] B. Kuelshammer, J. B. Olsson, G. Robinson, Generalized blocks for symmetric groups,
Invent. Math.151 (2003), 513-552.
[14] F. Lübeck, D. Prasad, A character relationship between symmetric group and hyperoctahedral group, J. Comb. Theory, Ser. A 179 (2021), 105368, (21pp).
[15] I. G. Macdonald, Symmetric functions and Hall polynomials, Oxford University Press,
1998.
[16] A. O. Morris, J. B. Olsson, On p-quotients for spin characters, J. Algebra 119 (1988),
51-82.
[17] A. Mendes, J. Remmel, J. Wagner, A λ-ring Frobenius characteristic for G ≀ Sn ,
Electron. J. Combin. 11 (2004), no. 1, Research Paper 56, 33 pp.
[18] F. D. Murnaghan, The characters of the symmetric group, Amer. J. Math. 59 (1937),
739-753.
[19] T. Nakayama, On some modular properties of irreducible representations of a symmetric group I, Jap. J. Math. 18 (1941), 89-108.
[20] M. Osima, On the representations of the generalized symmetric group I, Math. J.
Okayama Univ. 4 (1954), 39-56.
[21] G. Pfeiffer, Character tables of Weyl groups in GAP, Bayreuth. Math. Schr. 47 (1994),
165-222.
[22] W. Specht, Eine Verallgemeinerung der symmetrischen Gruppe. Schriften Math. Seminar Berlin 1 (1932), 1-32.
[23] R. Stanley, Enumerative Combinatorics II, Cambridge University Press, Cambridge,
UK, 1999.
[24] J. R. Stembridge, On the eigenvalues of representations of reflection groups and wreath
products, Pacific J. Math. 140 (1989), no. 2, 353-396.
[25] A. Zelevinsky, Representations of finite classical groups, A Hopf algebra approach,
Lecture Notes in Math. 869, Springer, Berlin, 1981.
[26] P. Zimmermann et al, Computational Mathematics with SageMath, 2018.


22

HUIMIN GAO AND NAIHUAN JING

Appendix A. The source code for Theorem 3.5
# Take k=3, n=5
P=PartitionTuples(3,5)
import random
lam=random.choice(P)
rho=random.choice(P)
print(lam,rho)
# Set environment
m=max(max(rho))
j=rho.index(max(rho))
r=Zmod(3)
w=SR.var(’w’)
import numpy
def ht(nums):
return numpy.count_nonzero(nums)-1
# Filter out lam satisfying conditions
for k in range(3):
if lam[k].size()>=m:
tem=Partitions(lam[k].size()-m,outer=lam[k]).list()
for i in tem:
if SkewPartition([lam[k],i]).is_ribbon():
coff =
(-1)^ht(SkewPartition([lam[k],i]).row_lengths())*w^r(-j*k)
l=list(lam)
l[k]=i
print(coff,"new lam:",PartitionTuple(l))

Appendix B. Theorem 3.9
# Take k=3, n=5
P=PartitionTuples(3,5)
import random
lam=random.choice(P)
rho=random.choice(P)
print(lam,rho)
# Set environment


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

23

s=max(max(lam))
j=lam.index(max(lam))
r=Zmod(3)
w=SR.var(’w’)
def sub(nums):
res = [[]]
for num in nums:
res += [ i + [num] for i in res]
return res
import itertools
array1 = sub(rho[0])
array2 = sub(rho[1])
array3 = sub(rho[2])
combs = itertools.product(array1,array2,array3)
# Simulate the path
import copy
class Solution:
def subsets(self, nums):
result = []
path = []
self.backtracking(nums, 0, path, result)
return result
def backtracking(self, nums, startIndex, path, result):
result.append(path[:])
for i in range(startIndex, len(nums)):
path.append(nums[i])
self.backtracking(nums, i + 1, path, result)
path.pop()
# Filter out rho satisfying conditions
for comb in combs:
if sum(comb[0])+sum(comb[1])+sum(comb[2])<=5-s:
box0 = comb[0]
box1 = comb[1]
box2 = comb[2]
taus=
Partitions(5-s-sum(comb[0])-sum(comb[1])-sum(comb[2])).list()
solu=Solution()
result = {}
for tau in taus:
d=Partition(tau).centralizer_size()


24

HUIMIN GAO AND NAIHUAN JING

c=(-1/3)^len(tau)/d*w^r(-(len(rho[1])len(comb[1]))*1*j-(len(rho[2])-len(comb[2]))*2*j)
all_index_3 = list(range(len(tau)))
all_index_1 = solu.subsets(all_index_3)
for i_i in range(len(all_index_1)):
index_2_3 =
list(set(all_index_3)-set(all_index_1[i_i]))
all_index_2_3 = solu.subsets(index_2_3)
box0_i_index = copy.deepcopy(all_index_2_3)
box1_i_index = copy.deepcopy(all_index_2_3)
box2_i_index = copy.deepcopy(all_index_2_3)
for i_i_i in range(len(all_index_2_3)):
box0_i_index[i_i_i] =
list(set(all_index_3)-set(index_2_3))
box1_i_index[i_i_i] =
list(set(index_2_3)-set(all_index_2_3[i_i_i]))
for k_0 in range(len(box0_i_index[i_i_i])):
box0_i_index[i_i_i][k_0] =
tau[box0_i_index[i_i_i][k_0]]
for k_1 in range(len(box1_i_index[i_i_i])):
box1_i_index[i_i_i][k_1] =
tau[box1_i_index[i_i_i][k_1]]
for k_2 in range(len(box2_i_index[i_i_i])):
box2_i_index[i_i_i][k_2] =
tau[box2_i_index[i_i_i][k_2]]
coff =c*( w^r((len(box0_i_index[i_i_i]) * 0 +
len(box1_i_index[i_i_i]) * 1 +
len(box2_i_index[i_i_i]) * 2)*j))
x = box0 + box0_i_index[i_i_i]
y = box1 + box1_i_index[i_i_i]
z = box2 + box2_i_index[i_i_i]
tmp = list()
tmp.append(x)
tmp.append(y)
tmp.append(z)
result["rho"] = tmp
print(coff,"new rho:",result["rho"])
School of Mathematics, South China University of Technology, Guangzhou,
Guangdong 510640, China
Email address: 13144508207@163.com
Department of Mathematics, North Carolina State University, Raleigh,
NC 27695, USA
Email address: jing@ncsu.edu
