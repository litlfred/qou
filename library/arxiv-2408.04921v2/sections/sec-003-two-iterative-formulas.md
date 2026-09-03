---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING"
section_id: sec-003-two-iterative-formulas
section_title: "Two Iterative Formulas"
section_number: 3
pages: 7-13
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING — 5 sections: Introduction; Irreducible characters of Ck ≀ Sn; X ij"
---
Using techniques of vertex operators, we have the following commutation
relations for the vertex operators (cf. [11]):
zXi (z)Xi (w) + wXi (w)Xi (z) = 0,
(3.1)
w
A∗i (z)Xi (w) = Xi (w)A∗i (z) +
Xi (w),
(3.2)
z−w
w
X ∗ (z).
(3.3)
Xi∗ (z)Ai (w) = Ai (w)Xi∗ (z) +
z−w i
Taking the coefficients of z m wn , we derive the following commutation relations among the components.
Proposition 3.1. For m, n ∈ N,i ∈ I, we have
Xim Xin = −Xi(n−1) Xi(m+1) ,
∗
Xim
.1 = 0,

a∗−im .1 = 0,
a∗−im Xin = Xin a∗−im + Xi(n−m) ,
∗
∗
∗
Xim
a−in = a−in Xim
+ Xi(m−n)
.

(3.4)
(3.5)
(3.6)
(3.7)

Recall that for two partitions µ ⊂ λ, if the skew partition λ − µ is connected and contains no 2∗2 boxes, we call λ−µ a rim hook or border strip. The
height of λ−µ is defined to be one less than the number of rows occupied, denoted by ht(λ−µ) or ht(λ/µ). For example, take λ = (5, 3, 2, 2), µ = (2, 1, 1),
then λ − µ can be depicted as

which is a 8-rim hook of λ with height 3. Note that a hook is a special case
of the rim hook.
If ξ is a rim hook contained in a Young diagram λ, then λ \ ξ denotes
the subdiagram of λ obtained by removing ξ. It is clear that λ \ ξ is also a
Young diagram, so we also use it refer to the associated partition. In the


8

HUIMIN GAO AND NAIHUAN JING

above example, ξ = (5, 3, 2, 2) − (2, 1, 1) is the rim hook, and the difference
partition is
λ \ ξ = (2, 1, 1).
(3.8)
(i)
A colored partition λ = (λ ) is contained in a colored partition µ =
(i)
(µ ), denoted by λ ⊂ µ, if each constituent partition λ(i) ⊂ µ(i) . The
difference ξ = λ − µ is called a rim-hook if one of the constituents λ(i) − µ(i)
is a rim-hook and all other constituents are identical, i.e., the colored rimhook ξ is only supported at the ith constituent.
For an integral l-tuple µ = (µ1 , . . . , µl ), we define the lowering operator
Tn (1 ≤ n ≤ l − 1) by
Tn :

(µ1 , · · · µn , µn+1 , · · · µl ) 7→ (µ1 , · · · µn+1 − 1, µn + 1, · · · µl ).

Now we give a characterization of m-rim hook η by using lowering operators.
Let ξ = (λ1 , · · · , λi−1 , λi − m, λi+1 , · · · , λl ) be the integral l-tuple obtained
by the action (3.6) of vertex operators.
Lemma 3.2. Any m-rim hook η can be written as a difference of a partition λ and ht(η) applications of Ti to the integral l-tuple (λ1 , . . . , λi−1 , λi −
m, λi+1 , . . . , λl ).
Proof. Assume that a m-rim hook η begins at the i-th row of λ. If its height
is 0, i.e., it only occupies the i-th row of λ. Then m ≤ λi − λi+1 , or λi − m ≥
λi+1 , so ξ is already a partition and η = λ − ξ. Suppose now ht(η) = 1 and
that it occupies the i-th and (i+ 1)-th rows of λ. By definition of a rim hook,
λi − λi+1 + 2 ≤ m ≤ λi − λi+2 + 1, so λi+2 − 1 ≤ λi − m ≤ λi+1 − 2. Hence
η = λ − Ti (ξ) and Ti (ξ) is a partition. In general, if the height of an m-rim
hook is r ≥ 1, one has
r−1
X

(λi+j − λi+j+1 + 1) + 1 ≤ m

j=0

≤

r−1
X
(λi+j − λi+j+1 + 1) + (λi+r − λi+r+1 ).

(3.9)

j=0

Then λi+r+1 − r ≤ λi − m ≤ λi+r − (r + 1), and we obtain η = λ −
Ti+r−1 · · · Ti (ξ).

Lemma 3.3. For each j ∈ I, any partition λ = (λ1 , λ2 , · · · λl ), and any
m ∈ N, we have
X
(−1)ht(λ/µ) sjµ,
(3.10)
a∗−jm sjλ =
µ

summed over all partitions µ such that λ − µ is an m-rim hook.
Proof. Repeatedly using (3.6) we have that
a∗−jm sjλ =

l
X
i=1

Xjλ1 · · · Xjλi −m · · · Xjλl .1.

(3.11)


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

9

The vector Xjλ1 · · · Xjλi −m · · · Xjλl .1 is the Schur function associated with
integral l-tuple (λ1 , . . . , λi−1 , λi − m, λi+1 . . . , λl ). If λi − m < λi+1 , we need
to straighten out the integral l-tuple to partition. We use (3.4) to rewrite
Xjλ1 · · · Xjλi −m · · · Xjλl .1 = −Xjλ1 · · · Xjλi+1 −1 Xjλi −m+1 · · · Xjλl .1.
If λi − m + 1 = λi+1 , then the term vanishes. If λi − m + 1 < λi+2 , then we
repeat the swapping (λi − m + 1, λi+2 ) → (λi+2 − 1, λi+2 − m + 2) until we
have a partition. Suppose after r steps, we reach the partition
ξ = (λ1 , · · · , λi−1 , λi+1 − 1, · · · , λi+r − 1, λi − m + r, λi+r+1 , · · · , λl ).
Then the skew partition
λ − ξ = (0i−1 , λi − λi+1 + 1, . . . , λi+r − λi + m − r, λi+r+1 , . . . , λl )
is a m-rim hook and sjλ = (−1)r sjξ .
Conversely, suppose ξ is a partition such that λ−ξ is a horizontal m-strip.
By Lemma 3.2 the term sξ appears in the expansion of a∗−jm sjλ . Therefore
(3.10) is proved.

Example 3.4.
a∗−1,4 s1(5,3,2) = s1(1,3,2) + s1(5,−1,2) + s1(5,3,−2)
= −s1(2,2,2) − s1(5,1,0)
Similarly, a colored partition µ ⊂ λ such that λ − µ is a colored rim hook
if and only if one of its constituents is a rim hook and the others are φ. The
height of λ − µ is exactly the height of its nonempty constituent, denoted
by ht(λ − µ) or ht(λ/µ). For example, if λ = ((2, 1), (5, 3, 2, 2), (4)), and
µ = ((2, 1), (2, 1, 1), (4)), then λ − µ is an 8-rim hook colored at the second
constituent with height 3.

{∅,

, ∅}

If ξ is a colored rim hook contained in a colored Young diagram λ, then
λ \ ξ denotes the colored subdiagram of λ obtained by removing ξ. Similarly
we also use λ \ ξ to denote the associated colored partition.
Now we are ready to give a vertex algebraic proof of the MurnaghanNakayama rule for the generalized symmetric group Ck ≀ Sn . The formula
(3.12) was first proved by group theoretical method in [2].
Theorem 3.5. Given colored partitions λ = (λ(0) , λ(1) , · · · , λ(k−1) ) and ρ =
(s)
(s)
(s)
(ρ(0) , ρ(1) , · · · , ρ(k−1) ) of n, where ρ(s) = (ρ1 , · · · , ρm , · · · , ρl(s) ). Then the
value of the irreducible character χλ of Ck ≀ Sn at the class ρ is given by
χλ
ρ =

k−1 X
X
λ\ξj
,
(−1)ht(ξj ) ω −sj χ (s)
j=0 ξj

ρ\ρm

(3.12)


10

HUIMIN GAO AND NAIHUAN JING
(s)

where ξj runs through all colored ρm -rim hooks contained in λ that are
supported at the j-th constituent.
Proof. Fixing j ∈ I, it follows from (2.6) that:
a∗

(s)

−jρm

siλ(i) = 0,

if i 6= j. Then nonzero contributions only come from
∗
(s) s (j) ) · · · s(k−1)λ(k−1) .
(s) sλ = s0λ(0) · · · (a
−jρm jλ
−jρm
By Lemma 3.3, a∗ (s) sλ is expanded into an alternating sum of sλ\ξj such
−jρm
(s)
that ξj is a colored ρm -rim hook supported at the j-th constituent. By

a∗

Theorem 2.2 and converting back to the basis e
a−sρ(s) , using
m

e
a−sρ(s) =
m

we have shown the theorem.

k−1
X

ω −sj a−jρ(s) ,
m

j=0



Example 3.6. In the group C3 ≀ S12 , we have
((4,1),(3,1,1),(2))

((4,1),∅,(2))

(∅,(3,1,1),(2))

χ((5,2),(3),(1,1)) = −χ((2),(3),(1,1)) + χ((2),(3),(1,1)) .
Similarly in C3 ≀ S14 , one has
((3,2),(4,2,1),(2))

((3,2),(1,1,1),(2))

((1),(4,2,1),(2))

χ((2,1),(4,3),(3,1)) = −χ((2,1),(3),(3,1)) − ω 2 χ((2,1),(3),(3,1)) ,
where ω is the 3-rd primitive root of unity.
Similar to the symmetric group, we have the following result by applying
Theorem 3.5. Recall that a colored hook is a special colored partition if and
only if one of its constituent is a hook and the others are ∅. The length of
arm and leg of a colored hook are exactly those of its nonempty constituent
respectively. Obviously a colored hook is a special colored rim hook.
Proposition 3.7. Let κi be a colored partition supported only at the i-th
constituent (n) and ω the k-th primitive root of unity. Then the irreducible
character χλ of Ck ≀ Sn satisfies
χλ (κi ) = (−1)r ω −ij

or

0

(3.13)

according as λ is a colored hook or not, where j is the index of its non-empty
constituent and r is its length of leg.
Now we study how to decompose the irreducible characters using the dual
vertex operator in the other direction.
For each partition ρ = (ρ1 , ρ2 , · · · , ρl ), a subpartition denoted by µ ⊳ ρ is
µ = ∅ or µ = (ρi1 , ρi2 , · · · , ρis ), for some 1 ⩽ i1 < · · · < is ⩽ l. Obviously,
there are 2l(ρ) subpartitions µ such that µ ⊳ ρ and ρ\µ is also a partition.
For example, if ρ = (4, 2, 2, 1), and µ = (2, 1), then µ ⊳ ρ and ρ\µ = (4, 2).
Moreover, µ ∪ τ of partitions µ and τ , is defined as the union of parts of µ
and τ in the descending order.


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

11

Lemma 3.8. For any partition ρ = (ρ1 , ρ2 , · · · , ρl ), m ∈ N, and i, j ∈ I,
one has that
X
∗
∗
ω −ij·(l(µ)) e
a−iρ\µ Xj(m−|µ|)
,
Xjm
e
a−iρ =
µ⊳ρ

summed over all subpartitions of ρ.

Proof. For each 1 ≤ s ≤ l, it follows from the linearity of e
a−iρs and the
action of (3.7) that
∗
∗
∗
Xjm
e
a−iρs = e
a−iρs Xjm
+ ω −ij Xj(m−ρ
.
s)

(3.14)

In the case of length 2 partition, the expression becomes
∗
∗
∗
∗
e
a−iρ Xjm
+ ω −ij e
a−iρ1 Xj(m−ρ
+ ω −ij e
a−iρ2 Xj(m−ρ
+ ω −ij·2 Xj(m−|ρ|)
.
2)
1)

Using induction on l(ρ), we get the lemma.



For two colored partitions µ and ρ, if for each i ∈ I, such that µ(i) ⊳ ρ(i) ,
we write µ ⊳ ρ. The set minus ρ\µ (removing the empty rows) is also
a colored partition. For example, if ρ = ((5, 3, 1), (4, 2, 2, 1), (4)), and µ =
((3), (2, 1), (4)), then µ ⊳ ρ and ρ\µ = ((5, 1), (4, 2), ∅).
A colored partition ρ naturally gives rise to a partition by forgetting the
colors, we call this partition the rearrangement of ρ. For example, take ρ =
((5, 1), ∅, (4, 2)), it can be rearranged into a regular partition (5, 4, 2, 1). We
also define the length of a colored partition l(ρ) as the sum of l(ρ(i) ). Recall
P
that the weighted length η(ρ) is defined as i il(ρ(i) ). The juxtaposition
µ ∪ τ of two colored partitions is defined as (µ(i) ∪ τ (i) ).
Now we are ready to give our second main result–the dual MaunaghanNakayama rule for the generalized symmetric group.
Theorem 3.9. Given colored partitions λ = (λ(0) , λ(1) , · · · , λ(k−1) ) and
ρ = (ρ(0) , ρ(1) , · · · , ρ(k−1) ) of n. Then for any fixed j ∈ I, the irreducible
character value of Ck ≀ Sn is given by
χλ
ρ =

X

ω (η(τ )−η(µ))j

(j)
µ⊳ρ,kµk≥λ1
(j)
τ ⊢kµk−λ1

(−1)l(τ ) λ\λ(j)
χ 1
kl(τ ) zτ (ρ\µ)∪τ

(3.15)

where the sum is over colored partitions µ and τ such that µ ⊳ ρ, with weight
(j)
(j)
bigger than λ1 , and τ of weight kµk − λ1 . zτ is defined in (2.10), τ is
P
the rearrangement of τ , and η(τ ), η(µ) are the weighted lengths i il(τ (i) ),
P
(i)
i il(µ ) respectively.
Proof. Applying Lemma 3.8 repeatedly, one has
X
∗
∗
Xjm
e
a−ρ =
ω −η(µ)j e
a−ρ\µ Xj(m−kµk)
.1,
µ⊳ρ

(3.16)


12

HUIMIN GAO AND NAIHUAN JING

summed over all colored partitions µ such that µ ⊳ ρ. By (3.5), nonzero
items survive only when m − kµk ≤ 0. Taking the coefficient of z n in Xj (z)∗ ,
we have that
∗
Xjn
.1 =

X (−1)l(ρ)
zρ

ρ⊢n

a−jρ

f or

n ≥ 0.

(3.17)

By (2.9) and (2.11), for a partition τ = (τ1 , τ2 , · · · , τl(τ ) ) we have
a−jτ =
=

l(τ )
1 Y

kl(τ ) s=1
1

kl(τ )

k−1
X

is =0

X

ω jis e
a−is τs

(i1 ,···il(τ ) )∈I l(τ )

!

(3.18)

ω |i|j e
a−i1 τ1 · · · e
a−il(τ ) τl(τ ) ,

where (i1 , · · · il(τ ) ) runs through the Cartesian product I l(τ ) and |i| = i1 +
· · · + il(τ ) . We rewrite the kl(τ ) summands by reordering factors according to
their colors, where the pairs (i1 , τ1 ), (i2 , τ2 ), . . . , (il(τ ) , τl(τ ) ) are rearranged
according to their colors. Then the composition (τ1 , τ2 , . . . , τl(τ ) ) becomes
a colored partition τ and the summation of its colors |i| = i1 + · · · + il(τ )
becomes η(τ ). Therefore
a−jτ =

1 X

kl(τ )

ω jη(τ ) ã−τ ,

(3.19)

τ

where the sum runs through all colored partitions arising from τ . Plugging
(3.19) into (3.18) and using (3.16) and (3.17), we have derived the recurrence
formula.

We remark that the dual Murnaghan-Nakayama rule of Ck ≀ Sn offers a
different iterative route from the Ariki-Koike version by directly simplifying
the indexing colored-partition of the irreducible representation by removing
the largest row in a fixed constituent, while the usual Murnaghan-Nakayama
rule is iterated by removing all possible rim-hooks from the indexing partition in all constituents.
When k = 1, we have the following dual Maunaghan-Nakayama rule for
the symmetric group, which seems new to the authors’ knowledge.
Theorem 3.10. The irreducible character value of Sn is given by
χλρ =

X

µ⊳ρ,|µ|≥λ1
τ ⊢|µ|−λ1

(−1)l(τ ) λ\λ1
χ(ρ\µ)∪τ ,
zτ

(3.20)

summed over partitions µ and τ such that µ is a subpartition of ρ with weight
bigger than λ1 , and τ of weight |µ| − λ1 .


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

13

Example 3.11. Using the recurrence relation, we see that in C2 ≀ S4
1 ((1),∅) 1 ((1),∅)
((1),(3))
χ((2,1),(1)) = − χ((1),∅) + χ(∅,(1)) .
2
2
Similarly in C3 ≀ S8 , we have
8 ((2),∅,(1)) 1 ((2),∅,(1)) 1
((2),(5),(1))
((2),∅,(1))
χ((3,1),(2),(2)) = χ((3),∅,∅) − ωχ(∅,(3),∅) − ω 2 χ(∅,∅,(3))
9
9
9
5
5
1 ((2),∅,(1))
((2),∅,(1))
((2),∅,(1))
− χ((2,1),∅,∅) − ω 2 χ(∅,(2,1),∅) − ωχ(∅,∅,(2,1))
9
18
18
1
1
5 ((2),∅,(1))
((2),∅,(1))
((2),∅,(1))
+ ωχ((2),(1),∅) + ω 2 χ((2),∅,(1)) − χ(∅,(2),(1))
18
18
18
5 ((2),∅,(1))
5 ((2),∅,(1)) 5
((2),∅,(1))
+ ωχ((1),(2),∅) + ω 2 χ((1),∅,(2)) − χ(∅,(1),(2))
9
9
18
4 ((2),∅,(1))
1 ((2),∅,(1))
1 ((2),∅,(1))
+ χ((1,1,1),∅,∅) −
−
χ
χ
81
162 (∅,(1,1,1),∅) 162 (∅,∅,(1,1,1))
5
1
5
((2),∅,(1))
((2),∅,(1))
((2),∅,(1))
+ ωχ((1,1),(1),∅) + ω 2 χ((1,1),∅,(1)) − ωχ(∅,(1,1),(1))
54
54
54
1
1
1
((2),∅,(1))
((2),∅,(1))
((2),∅,(1))
− ω 2 χ(∅,(1),(1,1)) + ω 2 χ((1),(1,1),∅) + ωχ((1),∅,(1,1))
54
27
27
2 ((2),∅,(1))
+ χ((1),(1),(1)) ,
27
where ω is the 3-rd primitive root of unity. For example, in the expansion of
((2),∅,(1))
χ(∅,(2,1),∅) , there are only two terms: µ = ((3, 1), ∅, (2)), τ = (∅, (1), ∅) and
µ′ = ((3, 1), (2), (2)), τ ′ = (∅, (2, 1), ∅). Therefore its coefficient is a sum of
two terms.
The following is a special case of a direct consequence of Theorem 3.9.
Proposition 3.12. Let κi be a colored partition supported only at the ith
constituent (n). Then for any colored partition ρ = (ρ(0) , ρ(1) , · · · , ρ(k−1) ) of
n, we have that
−η(ρ)i
i
χκ
,
ρ =ω
P
where η(ρ) is the weight length i il(ρ(i) ).

(3.21)
