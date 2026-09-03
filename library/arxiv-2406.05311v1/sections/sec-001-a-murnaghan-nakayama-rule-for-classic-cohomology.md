---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-001-a-murnaghan-nakayama-rule-for-classic-cohomology
section_title: "A Murnaghan\u2013Nakayama rule for (classic) cohomology"
section_number: 2
pages: 2-8
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
---
We review combinatorial models for the cohomology ring of the flag manifold. We omit
the precise definitions of the flag manifold and its cohomology as the combinatorial models
will suffice for our purposes; the interested reader can consult [16].


QUANTUM MURNAGHAN–NAKAYAMA RULE

3

Then we deduce a formula for the product of a Schubert polynomial and a hook Schur
function from which we deduce the Murnaghan–Nakayama rule in the cohomology of the flag
manifold, resulting in a different proof than that given by Morrison and Sottile [28]. Our
proof of the Murnaghan–Nakayama rule in quantum cohomology is analogous.
2.1. Cohomology of the flag manifold. Let n ∈ N be a positive integer and write Fℓn
for the manifold of complete flags in Cn . We let H ∗ Fℓn denote its cohomology ring with
coefficients in Z. This is a free Z-module with a distinguished basis {Sw }w∈Sn of Schubert
classes which are indexed by elements of the symmetric group Sn . Borel [10] described the
ring structure of H ∗ Fℓn as a quotient of a polynomial ring,
H ∗ Fℓn ≃ Z[x1 , . . . , xn ]/In ,

In =

ea (x1 , . . . , xn ) | a ∈ [n] ,

(2.1)

where ea is the ath elementary symmetric polynomial and [n] := {1, . . . , n}. Lascoux and
Schützenberger [21] defined a set of polynomials in Z[x1 , . . . , xn ] called Schubert polynomials
that correspond to the Schubert classes Sw under Borel’s isomorphism. We write Sw (x) for
the Schubert polynomial corresponding to Sw on the set of variables x := {x1 , . . . , xn }.
Every Schur polynomial sλ (x1 , . . . , xk ) is a Schubert polynomial. Let w ∈ Sn be a permutation with a unique descent at position k. Then the sequence (w(k)−k, . . . , w(2)−2, w(1)−1)
is a partition contained in the rectangular partition Rk,n−k of k(n−k) into k parts with
each part of size n−k. This is a bijection and for λ ⊆ Rk,n−k we write v(λ, k) ∈ Sn for the
corresponding permutation. Then Sv(λ,k) (x) = sλ (x1 , . . . , xk ). For example, when n = 7,
v((3, 1, 0), 3) = 136 2457

and

v((1, 0, 0, 0), 4) = 1235 467 = (4, 5) .

(2.2)

Observe that we may write permutations using both one-line and cycle notation. The “ ” is
written after the k-th position in a permutation in one-line notation.
It remains an important open problem in Schubert calculus to find a combinatorial rule
expressing Su ·Sv in terms of the basis {Sw }w∈Sn of H ∗ Fℓn . That is, one seeks a combinatorial
rule for the coefficients cw
u,v ∈ Z in the product
X
cw
(2.3)
Su · Sv =
u,v Sw .
w

A remarkable property of Schubert polynomials is that this computation can be performed
directly in the polynomial ring as the resulting coefficients cw
u,v are the same.
Although this problem remains open in general, several special cases are known. Monk’s
Formula [26] treats the case where v is the simple transposition (k, k+1). For any u ∈ Sn ,
X
Su(i,j)(x) ,
(2.4)
Su (x) · S(k,k+1)(x) =
1≤i≤k<j≤n
ℓ(u)+1=ℓ(u(i,j))

where ℓ(u) := #{i < j | u(i) > u(j)} denotes the length of the permutation u. In this case,
S(k,k+1)(x) = s(1) (x1 , . . . , xk ). Proposition 2.4 below describes the special case of multiplying
by s(b,1a−1 ) (x1 , . . . , xk ) in terms of the k-Bruhat order, which we define next. Here, (b, 1a−1 )
is the hook partition of a+b−1 into a parts, the first of size b, and the remaining all of size 1.
2.2. k-Bruhat order. The terms appearing in Monk’s Formula (2.4) define a partial order
on Sn graded by ℓ(u). Define the k-Bruhat order ≤k by the covering relation
u ⋖k u(i, j)

if 1 ≤ i ≤ k < j ≤ n and ℓ(u) + 1 = ℓ(u(i, j)) .


QUANTUM MURNAGHAN–NAKAYAMA RULE

4

That is, u ⋖k u(i, j) if and only if Su(i,j)(x) appears in the product Su (x) · S(k,k+1)(x). Since
ℓ(u) + 1 = ℓ(u(i, j)) if and only if u(i) < u(j) and there does not exist l such that i < l < j
and u(i) < u(l) < u(j), we obtain the following equivalence.
Proposition 2.1. Let u and w be two permutations. Then u ⋖k w if and only if
(1) w = u(i, j) for some i ≤ k < j such that u(i) < u(j); and
(2) there does not exist l such that i < l < j and u(i) < u(l) < u(j).
Write [u, w]k for the interval between u and w in the k-Bruhat order. We may label each
cover relation u ⋖k u(i, j) with i ≤ k < j by u(i) and write
u(i)

u −−→ u(i, j)
l

u ⋖k u(i, j) with i ≤ k < j .

if

l

l

r
1
2
A saturated chain γ : u −
→
u1 −
→
··· −
→
ur in this poset has length r and we denote its
maximal element by end(γ) = ur . If in addition there exists a number a such that l1 > · · · >
la < la+1 < · · · < lr , then we say that γ is a peakless chain of height a and length r.
Figure 1 shows two labeled intervals, one in the 5-Bruhat order on S8 and the other in

627 4135
4

68357 421
2

68257 431
4

68347 521
2

68247 531
3

68237 541
5

5

5

68345 721
2

68245 731
3

68235 741

427 6135 624 7135

3

4

4

6

3

327 6145 426 7135 623 7145
6

3

3

4

1

326 7145 423 7165 621 7345
4

1

4

324 7165 421 7365
1

3

321 7465

Figure 1. Two intervals in k-Bruhat orders on Sn .
the 3-Bruhat order on S7 . The interval on the left has a peakless chain (colored in blue); its
‘middle’ chain has labels 5, 3, 2, 4, so it is peakless of height 3, but the other interval has no
peakless chains.
2.3. Grassmannian–Bruhat order. We will make use of a second partial order on Sn that
is defined using the k-Bruhat order. Define the Grassmannian–Bruhat order on Sn by
ηζ

if

there exists u ∈ Sn and 1 ≤ k < n with u ≤k ηu ≤k ζu.

This is a graded partial order on Sn with minimal element the identity permutation e. Its
rank function is L(ζ) := ℓ(ζu) − ℓ(u) for any u ∈ Sn and k ∈ N with u ≤k ζu. The cover
relations inherit a labeling from the k-Bruhat orders. As shown in [6, Sect. 3.2], neither ,
L, nor the labeling depend on the choice of k or u. For a permutation ζ ∈ Sn , its height is
ht(ζ) := #{i ∈ [n] | i < ζ(i)} and its support is supp(ζ) = {i ∈ [n] | ζ(i) 6= i}. Then for any
ζ ∈ Sn and k satisfying ht(ζ) ≤ k ≤ n − # supp(ζ) + ht(ζ), there is a u ∈ Sn with u ≤k ζu [6,
Thm. 3.1.5], which among other things implies that e  ζ.
The order  enjoys another symmetry. Permutations ζ ∈ Sn and η ∈ Sm are shapeequivalent if we have supp(ζ) ⊆ {i1 < · · · < ir } and supp(η) ⊆ {j1 < · · · < jr } and
for all a, b, ζ(ia ) = ib if and only if η(ja ) = jb . For example, the cycles (2, 3, 5, 7, 4) and
(1, 2, 4, 5, 3) are shape-equivalent. Shape-equivalence induces an isomorphism on intervals [6,


QUANTUM MURNAGHAN–NAKAYAMA RULE

5

Thm. 3.2.3(v)]. It also preserves the relative order of labels on chains, so that a chain in one
interval is peakless if and only if the corresponding chain in a shape-equivalent interval is
peakless.
We illustrate this. The intervals in Figure 1 correspond to the permutations ζ1 = (2, 3, 5, 7, 4)
and ζ2 = (1, 7, 4)(3, 6) under the map that associates the permutation vu−1 with the interval [u, v]. Figure 2 shows labeled intervals [e, ζi ] for these two permutations, as well as for
η = (1, 2, 4, 5, 3), which is shape-equivalent to ζ1 . The commas are omitted in the cycles for
display purposes. The peakless chains in the intervals [e, ζ1 ] and [e, η] are highlighted.
(174)(36)
4

(23574)

3

2

4

(3574)

(234)(57)

4

2

6

(34)(57)

(234)

(164)

3

5

2

4

(57)

(34)

(1634)
3

3

3

1

e

(12453)
1

3

(2453)

(123)(45)

3

1

3

(1364)
4

(134)

1

(364)

4

(23)(45)

(123)

2

4

1

(34)

(45)

(23)

3

4

1

(14)

(14)(36)

6

(1764)

5

5

(17634)

4

4

e

2

e

Figure 2. Intervals in the Grassmannian–Bruhat order.
2.4. Minimal permutations. A permutation ζ is minimal if L(ζ) = # supp(ζ) − s(ζ),
where s(ζ) is the number of (nontrivial) cycles in the factorization of ζ into disjoint cycles.
Minimality is a central concept in this paper. This terminology (introduced in [6]) arises
from the inequality L(ζ) ≥ # supp(ζ) − s(ζ), so that a minimal permutation has the minimal
possible rank given its cycle structure. For example, ζ1 = (2, 3, 5, 7, 4) is minimal, because
L(ζ1) = ℓ(68357421) − ℓ(68235741) = 22 − 18 = 4 = # supp(ζ1 ) − s(ζ1 );
and ζ2 = (1, 7, 4)(3, 6) is not minimal, because
L(ζ2 ) = ℓ(6274135) − ℓ(3217465) = 12 − 7 = 5 > 3 = # supp(ζ2 ) − s(ζ2 ).
Related to minimality is the notion of crossing. Let l1 < l2 and m1 < m2 be two disjoint
pairs of numbers, and suppose that l1 < m1 . There are three possibilities for l2 . Either l2 < m1
or m1 < l2 < m2 or m2 < l2 . When the second occurs, we say that the pairs are crossing,
otherwise they are noncrossing. This refers to arcs connecting elements of each pair, when
the numbers are marked along a number line.

l1

l2
m1
noncrossing

m2

l1

m1 l2
crossing

m2

l2

m1 m2
noncrossing

l2

Let A, B ⊂ [n] be disjoint and suppose that each has at least two elements. If there exist
a pair of elements of A and a pair of elements of B that are crossing, then A and B are
crossing; otherwise they are noncrossing.
A product ζ · η of two permutations is noncrossing when supp(ζ) and supp(η) are disjoint
and noncrossing. A permutation ζ is irreducible if it cannot be written nontrivially as a noncrossing product. Any permutation factors uniquely as a noncrossing product of irreducible


QUANTUM MURNAGHAN–NAKAYAMA RULE

6

permutations. In [6], s(ζ) counted the number of irreducible factors in the noncrossing factorization of ζ for minimal permutations. By [6, Lem. 3.3.1] we have that s(ζ) is the number
of cycles (this is also explained in the proof below). We give a characterization of minimal
permutations in terms of peakless chains in the Grassmannian–Bruhat order.
(176)(2354)
(176)(354)
(2354)
(176)

(354)

(234)

(16)

(34)

e

e

(176)(234)

(176)(34)
(176)

(16)(2354)

(16)(354)

(16)(234)

(16)(34)
(16)

(2354)

(354)

(234)
(34)
e

Figure 3. If ζ · η is a noncrossing product, then the interval [e, ζ · η] is
isomorphic to the product of the intervals [e, ζ] and [e, η] , and the chains in
[e, ζ · η] are shuffles of chains in each of the factors.
Lemma 2.2. Let ζ be a permutation and ζ = ζ1 · · · ζs its unique factorization into a noncrossing product of irreducible permutations.
(1) L(ζ) = L(ζ1 ) + · · · + L(ζs ).
(2) [e, ζ] ≃ [e, ζ1 ] × · · · × [e, ζs ] .
(3) [e, ζ] has a peakless chain if and only if each interval [e, ζi ] has a peakless chain.
(4) ζ is a minimal permutation if and only if each ζi is a minimal permutation.
(5) If ζ is minimal and irreducible, then ζ is a cycle.
Proof. (1) By [6, Lem. 3.3.1], L(ζ) = L(ζ1) + · · · + L(ζs ) as this is a noncrossing product.
(2) [6, Lem. 3.3.3] implies that [e, ζ] ≃ [e, ζ1 ] × · · · × [e, ζs ] .
(3) If each interval [e, ζi ] has a peakless chain γi , then shuffling these chains appropriately
gives a peakless chain γ in [e, ζ] by (2). Conversely, if γ is a peakless chain in [e, ζ] , restricting it to each [e, ζi ] gives a peakless chain γi . Figure 3 illustrates this for the noncrossing
product of the two minimal permutations ζ = (1, 7, 6) and η = (2, 3, 5, 4). The peakless chains
are indicated, and commas in cycles are omitted for display purposes.
(4) follows from (1) and (2).
(5) Suppose that ζ is minimal and irreducible. If ζ is not a single cycle, then ζ = η·η ′ , where
η and η ′ have disjoint supports that are crossing. By [6, Lem. 3.3.1], L(ζ) > L(η) + L(η ′),
which contradicts that ζ is minimal. This inequality is illustrated by ζ = (1, 7, 4)(3, 6). We
showed that L(ζ) = 5, but L(1, 7, 4) = 2 and L(3, 6) = 1.

Proposition 2.3. A permutation ζ is minimal if and only if the interval [e, ζ] has a peakless

s(ζ)−1
.
chain. The number of peakless chains of height a in [e, ζ] is the binomial coefficient ht(ζ)−a
Proof. We begin by showing that the first statement follows from the corresponding result for
irreducible permutations. Let ζ = ζ1 · · · ζs be the unique factorization of ζ into a noncrossing
product of irreducible permutations. By Lemma 2.2, ζ is minimal if and only if each ζi is


QUANTUM MURNAGHAN–NAKAYAMA RULE

7

minimal. Since ζi is irreducible, ζ is minimal if and only if each interval [e, ζi ] has a peakless
chain. By Lemma 2.2, this holds if and only if [e, ζ] has a peakless chain.
We now prove the result for irreducible permutations. Suppose that ζ is minimal and
irreducible. By Lemma 2.2, ζ is a single cycle. In [8, Lem. 6.7] it is proved that if ζ is a minimal
cycle, then there is a unique peakless chain in the interval [e, ζ] , which proves the forward
direction. Conversely, suppose that [e, ζ] has a peakless chain. Let a be the height of that
chain and set b := L(ζ)−a+1. Replacing ζ by a shape-equivalent permutation if necessary, we
may assume that supp(ζ) = [n] (so that ζ ∈ Sn ) and thus L(ζ) ≥ # supp(ζ) − s(ζ) = n − 1.
Since e  ζ, there is a k < n and u ∈ Sn such that u ≤k ζu and [e, ζ] ≃ [u, ζu]k . By [6,
Thm. 3.1.5], we have
{i | i < ζ(i)} ⊆ {u−1 (1), . . . , u−1 (k)} and {i | i > ζ(i)} ⊆ {u−1(k + 1), . . . , u−1(n)}
so that
ht(ζ) = #{i | i < ζ(i)} ≤ k

and n − ht(ζ) = #{i | i > ζ(i)} ≤ n − k.

Together, these imply that ht(ζ) = k. Since there is a peakless chain in [e, ζ] and [e, ζ] ≃
[u, ζu]k , it follows from Formula (2.6) below that the coefficient cζu
u,v((b,1a−1 ),k) is nonzero. This
a−1
a−1
implies that v((b, 1 ), k) ≤k ζu. As ζu ∈ Sn , we have v((b, 1 ), k) ∈ Sn . Thus a ≤ k < n
and b ≤ n−k, so that L(ζ) = a+b−1 ≤ n−1. This implies that L(ζ) = n−1, a = k, and
b = n−k. As n = # supp(ζ), we conclude that ζ is a minimal cycle and
 that [e, ζ] has a
s(ζ)−1
= ( 00 ) = 1.
unique peakless chain. Note that since s(ζ) = 1 and ht(ζ) = a, we have ht(ζ)−a
Finally, suppose that ζ = ζ1 · · · ζs is the noncrossing factorization of a minimal permutation
ζ into disjoint minimal cycles ζ1 , . . . , ζs . Recall from Lemma 2.2 that [e, ζ] ≃ [e, ζ1 ] × · · · ×
[e, ζs ] . We count the shuffles of peakless chains γi in [e, ζi ] with a given height. We need
only consider the sequence of labels, and note that as the cycles ζi have disjoint supports,
the set of labels on the chains γi are disjoint. Partition a peakless chain (represented by its
labels)
l1 > · · · > la−1 > la < la+1 < · · · < la+b−1
(2.5)
into three subsets. Call l1 > · · · > la−1 the decreasing segment, la the minimum, and la+1 <
· · · < la+b−1 the increasing segment.
In a peakless chain (2.5) of height a in [e, ζ] , its decreasing segment contains the decreasing
segments of each γi , and the same for increasing segments. Its minimum la is the minimum of
all the minima of the γi . The only choices possible are distributing the remaining s−1 minima
between the decreasing and increasing segments of (2.5), which may be done independently.
Since ht(ζ) = ht(ζ1 ) + · · · + ht(ζs ), we see that placing ht(ζ) − a of these remaining minima
in the increasing segment gives a peakless chain of height a. This completes the proof.

2.5. A Murnaghan–Nakayama rule for H ∗ Fℓn . We recall the following special case of
Formula (2.3), which is [36, Cor. 9].
Proposition 2.4. Let u ∈ Sn , a ≤ k, and b ≤ n−k. Then
X
Su (x) · s(b,1a−1 ) (x1 , . . . , xk ) =
Send(γ) (x) ,

(2.6)

γ

the sum over all peakless chains starting at u of height a and length a+b−1 in the k-Bruhat
order.
Using Proposition 2.3, we can explicitly describe the coefficients appearing in (2.6).


QUANTUM MURNAGHAN–NAKAYAMA RULE

Proposition 2.5. Let u ∈ Sn , a ≤ k and b ≤ n−k. Then
X  s(ζ)−1 
Su (x) · s(b,1a−1 ) (x1 , . . . , xk ) =
ht(ζ)−a Sζu (x) ,

8

(2.7)

the sum over all minimal permutations ζ ∈ Sn such that u ≤k ζu and L(ζ) = a + b − 1.

We use Proposition 2.5 to derive a formula for the product of a Schubert polynomial and
a power sum symmetric polynomial. Let pr (x1 , . . . , xk ) := xr1 + · · · + xrk denote the rth power
sum polynomial. Expanded in terms of Schur polynomials [24], we have
pr (x1 , . . . , xk ) = s(r) (x1 , . . . , xk ) − s(r−1,1) (x1 , . . . , xk ) + · · · + (−1)r+1 s(1r ) (x1 , . . . , xk ). (2.8)
Corollary 2.6 (Murnaghan–Nakayama rule for H ∗ Fℓn ). Let u ∈ Sn . Then
X
Su (x) · pr (x1 , . . . , xk ) =
(−1)ht(ζ)+1 Sζu (x) ,
the sum over all minimal cycles ζ ∈ Sn such that u ≤k ζu and L(ζ) = r.

Proof. Expanding the product Su (x) · pr (x1 , . . . , xk ) using Equations (2.7) and (2.8) shows
that the coefficient of Sζu for u ≤k ζu is zero unless L(ζ) = r and ζ is minimal. When ζ is
the noncrossing product of s(ζ) minimal cycles, this coefficient is
(


r
X
s(ζ)
−
1
0,
if s(ζ) 6= 1,
=
(−1)a−ht(ζ)

(−1)ht(ζ)+1
ht(ζ)+1
ht(ζ)
−
a
(−1)
,
if
s(ζ)
=
1.
a=1
This proof differs from that given in [27, 28].
