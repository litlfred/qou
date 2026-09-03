---
doc_id: arxiv-2504.18825v2
doc_title: "MURNAGHAN\u2013NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU"
section_id: sec-010-murnaghan-nakayama-rule-for-the-cyclotomic-hecke
section_title: "Murnaghan\u2013Nakayama rule for the cyclotomic Hecke algebra"
section_number: 3
pages: 12-18
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
doc_brief: "MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU — 16 sections: Introduction; Preliminaries; Murnaghan–Nakayama rule for the cy"
---
In this section, we will present our Murnaghan–Nakayama rule for the cyclotomic Hecke
algebra.
3.1. Murnaghan–Nakayama rule. A skew diagram λ/µ is a vertical (resp. horizontal)
strip if each row (resp. column) contains at most one box. We say a skew diagram of
λ/µ is a ribbon (also known as border strip or rim hook) if it is connected and contains
no 2 × 2 blocks . The height (denoted by ht(λ/µ)) of a ribbon λ/µ is defined as the
number of the rows in λ/µ minus 1. More generally, a generalized ribbon is a skew diagram
without 2 × 2 blocks (not necessarily connected). Any generalized ribbon is a union of
its connected components, each of which is a ribbon. For a generalized ribbon λ/µ with
connected components ξ1 , ξ2 , · · · , ξm , define thePheight of λ/µ as the sum of the heights of
connected components of λ/µ, i.e., ht(λ/µ) = m
i=1 ht(ξi ), and use cc(λ/µ) to denote the
number of connected components of λ/µ. Define the weight of a generalized ribbon λ/µ by
wt(λ/µ; t) := (1 − t)cc(λ/µ) (−t)ht(λ/µ) .

(3.1)

The following lemma is essential for us to obtain our Murnaghan–Nakayama rule, with
part of the proof techniques inspired by [HR95, (6.7)].


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
13

∗ hhhh
v hhh
v
v
∗
v
v
∗
Figure 1. λ is obtained from µ by adding a horizontal strip (to get ν) and
then adding a vertical strip (to ν).
Lemma 3.1. Let k be a non-negative integer, then
X
qk (x; t)sµ =
wt(λ/µ; t)sλ

(3.2)

λ

summed over all partitions λ ⊢ |µ| + k such that λ/µ is a generalized ribbon.
Proof. Recall
the identity in [JL24, Corollary 3.2] q = t = 0, a = (1, 0, · · · ) and b =

(t, 0, · · · ) that
X

sλ/µ (1 − t)sλ (x).
(3.3)
σ k (1 − t)X sµ (x) =
µ⊂λ

By (2.20), it suffices to prove sλ/µ (1 − t) = wt(λ/µ; t) if λ/µ is a generalized ribbon and 0
otherwise. By (2.22), we have
X
sν/µ (1)sλ/ν (−t) (by sum rule)
sλ/µ (1 − t) =
ν

X
t
t
=
(−1)|λ/ν| sν/µ (1)sλ /ν (t) (by duality rule)
ν

X
t
t
=
(−t)|λ/ν| sν/µ (1)sλ /ν (1) (by homogeneity).
ν

It is well known that
(
1 if ν/µ is a horizontal strip
sν/µ (1) =
0 otherwise

and s

λt /ν t

(
1 if λ/ν is a vertical strip
(1) =
,
0 otherwise

which yields that sλ/µ (1 − t) = 0 unless λ is obtained from µ as follows: firstly add a
horizontal strip to µ to obtain ν and then add a vertical strip to ν to get λ, i.e., λ/µ is
a generalized ribbon. In this case, then each box in λ/µ satisfies one of the following (see
Fig. 1):
(i) There is a box of λ/µ immediately to the left (labeled by h);
(ii) There is a box of λ/µ immediately below it (labeled by v);
(iii) Neither (i) nor (ii) holds (labeled by ∗).


14

NAIHUAN JING AND NING LIU

Correspondingly, we have the following observations:
• Each box in case (i) (resp. (ii)) must come from the application of the horizontal
(resp. vertical) strip to µ and thus this box has weight 1 (resp. −t);
• Each connected component (ribbon) ξi in λ/µ has c(ξi ) − 1 (resp. r(ξi ) − 1) boxes
in case (i) (resp. (ii));
• Each connected component (ribbon) in λ/µ has exactly one box in case (iii), in
which case this box has weight 1 − t.
Here c(ξi ) (resp. r(ξi )) presents the number of the columns (resp. rows) in ξi . Thus the
product of these weights is exactly
Y
(1 − t)cc(λ/µ)
1c(ξi )−1 (−t)r(ξi )−1 = wt(λ/µ; t),
i

which completes the proof.

□

Suppose λ, µ ∈ Pn,m and µ ⊂ λ. We say λ/µ = (λ(1) /µ(1) , · · · , λ(m) /µ(m) ) is a generalized m-multi-ribbon if λ(i) /µ(i) is a generalized ribbon for all 1 ≤ i ≤ m. Analogously, we
define
m
m
X
X
(i)
(i)
cc(λ/µ) :=
cc(λ /µ ); ht(λ/µ) :=
ht(λ(i) /µ(i) );
i=1

wt(λ/µ; t, u, r) := urλ/µ

i=1
m
Y

wt(λ(i) /µ(i) ; t) = urλ/µ (1 − t)cc(λ/µ) (−t)ht(λ/µ) ,

(3.4)

i=1

where 1 ≤ r ≤ m, uλ/µ := us and s presents the first non-empty entry in λ/µ from right
to left. For convention, we let uλ/λ := 1. A generalized m-multi-ribbon λ/µ is called a
P
(i)
(i)
k-generalized m-multi-ribbon if m
i=1 |λ /µ | = k. Sometimes we will omit m, saying a
generalized multi-ribbon for a generalized m-multi-ribbon in short.
Example 3.2. λ/µ in (2.2) is an 11-generalized 5-multi-ribbon. In this case, cc(λ/µ) = 6,
ht(λ/µ) = 1 + 1 = 2 and uλ/µ = u5 . Thus, wt(λ/µ; t, u, r) = ur5 t2 (1 − t)6 .
With the above notations in hand, we are now in position to give the Murnaghan–
Nakayama rule for the cyclotomic Hecke algebra, before which the following result is needed.
Theorem 3.3. Let k be a non-negative integer and 1 ≤ r ≤ m, µ ∈ Pn,m . Then
qk X
(r)
qk (x; q, u)sµ =
wt(λ/µ; q −2 , u, r)sλ
−1
q−q
λ

(3.5)

summed over all multipartitions µ ⊂ λ ∈ Pn+k,m such that λ/µ is a k-generalized mmulti-ribbon.
Proof. By definition, we have


m
m
k
X
Y
Y
q
(r)
r
(j) −2 

qk (x; q, u)sµ =
u
q
(x
;
q
)
sµ(i) (x(i) )
cj
c
q − q −1 c∈C
j=1
i=1
k,m


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
15
m
Y
X
qk
r
=
uc
qcj (x(j) ; q −2 )sµ(j) (x(j) )
q − q −1 c∈C
j=1
k,m

!
m
Y
X
X
qk
(j)
(j) −2
(j)
r
uc
wt(λ /µ ; q )sλ(j) (x )
=
q − q −1 c∈C
(j)
j=1

(by Lemma 3.1)

λ

k,m

Swapping the inner summation and the product in the above equation implies that
(r)

qk (x; q, u)sµ =

X X
qk
wt(λ/µ; q −2 , u, r)sλ ,
q − q −1 c∈C
λ
k,m

where λ runs over all multipartitions µ ⊂ λ ∈ Pn+k,m such that λ/µ is a generalized
multi-ribbon and |λ(j) /µ(j) | = cj , j = 1, 2, · · · , m. This deduces (3.5).
□
As a straightforward result, the following corollary is an iterative formula for the irreducible characters, which is referred to as the Murnaghan–Nakayama rule.
Corollary 3.4. Let λ, µ ∈ Pn,m , 1 ≤ r ≤ m, 1 ≤ j ≤ l(µ(r) ), then
(r)

χλµ =

X q µj
wt(λ/ν; q −2 , u, r)χνµ\µ(r)
−1
q
−
q
j
ν

(3.6)

(r)

summed over all multipartitions ν ⊂ λ such that λ/ν is a µj -generalized multi-ribbon,
(r)
where µ \ µj is the multipartition obtained from µ by removing the j-th part from the r-th
partition µ(r) .
Proof. By the Frobenius formula (2.12), we have
X
χνµ\µ(r) sν .
qµ\µ(r) =
j

ν

(3.7)

j

(r)

Multiplying both sides by q (r) yields that
µj

qµ =

X

(r)

χνµ\µ(r) q (r) sν
j

ν

µj

(r)

=

X
ν

X
q µj
χνµ\µ(r)
wt(λ/ν; q −2 , u, r)sλ
−1
j q − q
λ

(by (3.5))

(3.8)

(r)

=

XX
λ

ν

q µj
ν
χµ\µ(r)
wt(λ/ν; q −2 , u, r)sλ
−1
j q − q

Note that {sλ | λ ∈ Pn,m } forms an orthonormal basis in Λ⊗m
Q . Comparing the coefficient
of sλ in (3.8) and (2.12) gives (3.6).
□


16

NAIHUAN JING AND NING LIU

Example 3.5. Suppose λ = ((2, 2), (4)), µ = ((2, 1), (3, 2)). Choose r = j = 2. Then
(r)
µj = 2 and there are 4 ν’s such that λ/ν is a 2-generalized 2-multi-ribbon. They are
 
 
 


.
,
,
,
,
The weights of these 2-generalized 2-multi-ribbons are u21 (1 − t)(−t), u21 (1 − t), u22 (1 − t)
and u22 (1 − t)2 respectively. Therefore,
q2  2
((2,2),(4))
((1,1),(4))
((2),(4))
χ((2,1),(3,2)) =
u1 (1 − q −2 )(−q −2 )χ((2,1),(3)) + u21 (1 − q −2 )χ((2,1),(3))
−1
q−q

((2,2),(2))
((2,1),(3))
+u22 (1 − q −2 )χ((2,1),(3)) + u22 (1 − q −2 )2 χ((2,1),(3)) .
For given λ ∈ Pn,m , a generalized m-multi-ribbon tableau T of shape λ is defined as a
sequence
T:

∅ = λ(0) ⊂ λ(1) ⊂ · · · ⊂ λ(l−1) ⊂ λ(l) = λ

(3.9)

such that λ(i) /λ(i−1) (1 ≤ i ≤ l) is a generalized m-multi-ribbon.
Define an order on the set {ij | i ≥ 1, j ≥ 1} by
ab ≤ cd

⇐⇒

a < c or a = c, b ≤ d.

(3.10)

A generalized m-multi-ribbon tableau T can also be described by a tuple of tableaux,
in which the cells of each partition are marked ij (i ≥ 1, j ≥ 1), satisfying
(i) the numbers ij inserted in the diagram of each partition of T must increase weakly
down each column and along each row from left to right;
(ii) the cells marked same number consist of a generalized m-multi-ribbon.
(i)

The content of T is defined as a multicomposition c = (c(1) , c(2) , · · · ) such that cj equals
the number of cells marked ij in T. For a given T, introduce a map fT : {ij | i ≥ 1, j ≥
1, ij ∈ T} → {1, 2, · · · , m} by
fT : ij 7−→ the rightmost entry in T containing ij .
For a generalized multi-ribbon tableau T of shape λ with content µ, we define the weight
of T by
(i)

wt(T; u, t) := (1 − t)cc(T) (−t)ht(T)

m l(µ
Y
Y)

uifT (ij )

i=1 j=1

where
(i)

cc(T) :=

m l(µ
X
X)
i=1

(i)

cc(ξ(ij )),

ht(T) :=

j=1

and ξ(ij ) is the generalized multi-ribbon marked ij .

m l(µ
X
X)
i=1

j=1

ht(ξ(ij ))

(3.11)


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
17

Example 3.6. Below is a generalized multi-ribbon tableau T of shape λ = ((4, 3), (2), (1, 1))
with content µ = ((3, 2), (4), (2)). In this case, fT (11 ) = 1, fT (12 ) = 1, fT (21 ) = 3,
fT (31 ) = 3.
!
11 11 12 21
21
T=
11 12 21
21 31 ,
31
,
cc(T) = 1 + 2 + 4 + 2 = 9, ht(T) = 1. So wt(T; u, t) = u1 · u1 · u23 · u33 (1 − t)9 (−t) =
u21 u53 (−t)(1 − t)9 .
Corollary 3.7. Suppose λ, µ ∈ Pn,m , we have the following general formula for χλµ in
terms of generalized m-multi-ribbon tableaux as follows:
X
qn
χλµ =
wt(T; u, q −2 )
(3.12)
−1
l(µ)
(q − q )
T
summed over all generalized m-multi-ribbon tableaux of shape λ with content µ.
Proof. It is straightforward by using Corollary 3.4 repeatedly.

□

3.2. Examples and numerical relations. Now we apply our Murnaghan–Nakayama
rule to compute some irreducible characters in special cases and establish an equality
relation. We use the short-hand notation ε1j (resp. εnj ) to present the multipartition with
(1n ) (resp. (n)) in the j-th entry and ∅ anywhere else.
Example 3.8. We list the following simple results coming from our Murnaghan–Nakayama
rule.
(i)
• If we denote by f λ the number of standard Young tableaux of shape λ(i) , which is
given by
fλ

(i)

=Q

|λ(i) |!
x∈λ(i) hx

where hx is the hook length at x. Then we have
m
Y
(i) j|λ(i) |
λ
χ ε1 =
f λ ui
.
j

(3.13)

i=1
(i)

• Denote L(λ) = #{i | λ ̸= ∅} and s = max{i | λ(i) ̸= ∅}. Then
(
P
q n−1 ujs (1 − q −2 )L(λ)−1 (−q −2 ) i bi , if λ(i) = (ai , 1bi ), i = 1, · · · , m
λ
χεnj =
0,
otherwise.
Pm
• Denote Lµµ := i=1 il(µ(i) ).2 Then
ε1

(3.14)

L

(3.15)

χµ =q n−l(µ) uj µµ .

(3.16)

χµj =(−q)l(µ)−n uj µµ ;
εn
j

L

2We adopt this notation to be consistent with that in Theorem 5.3.


18

NAIHUAN JING AND NING LIU

Proposition 3.9. Let µ be an arbitrary m-multipartition of n. Suppose for 1 ≤ j ≤ m
λ = (∅, · · · , ∅, λ(j) , · · · , λ(m) )

and

λ′ = (λ(j) , ∅, · · · , ∅, λ(j+1) , · · · , λ(m) ).

Then
′

χλµ = χλµ
where f

u1 →uj

(3.17)

u1 →uj

means replacing u1 by uj in f .

Proof. We observe that there exists a natural one-to-one correspondence between the set
of generalized multi-ribbon tableaux of shape λ with content µ and those of shape λ′
′
with content µ. Applying Corollary 3.7 to both χλµ and χλµ , we find that the presence
of uj in some monomial M of χλµ is equivalent to the presence of ij exclusively in λ(j) .
Under this one-to-one correspondence, this is further equivalent to the presence of u1 in
′
the corresponding monomial M ′ of χλµ . Moreover, all other factors remain identical. The
only difference between the factors of M and M ′ lies in the replacement of u1 with uj .
′
□
Thus, χλµ can be obtained from χλµ by substituting u1 with uj .
