---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-002-skew-characters
section_title: "Skew characters"
section_number: 3
pages: 9-18
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
In this section we state and prove a result on the values of skew characters
on elements of the form gnα (Theorem 3.3). First, we give the necessary
combinatorial definitions. In several arguments we shall refer to James’
abacus notation for partitions, as described in [8, page 78].
3.1. Quotients of skew-partitions. We shall define n-quotients and nsigns for the following class of skew-partitions.
Definition 3.1. Let m, n ∈ N. We say that a skew-partition λ/µ of mn
is n-decomposable if there exists a border-strip tableau of shape λ/µ and
type (nm ).
Definition 3.2. Let m, n ∈ N and let λ/µ be an n-decomposable skewpartition of mn. Let Γ(λ) be an abacus display for λ on an n-runner abacus
using tn beads for some t ∈ N. Let Γ(µ) be the abacus display for µ obtained
by performing an appropriate sequence of m upward bead moves on Γ(λ).
(This is possible since λ/µ is n-decomposable.) Let (λ(0) , . . . , λ(n−1) ) and
(µ(0) , . . . , µ(n−1) ) be the n-quotients of λ and µ corresponding to Γ(λ) and
Γ(µ), respectively. The n-quotient of λ/µ is defined to be
(λ(0) /µ(0) , . . . , λ(n−1) /µ(n−1) ).
We define the n-sign of λ/µ, denoted εn (λ/µ) to be the sign of any borderstrip tableau of shape λ/µ and type (nm ).
To avoid cumbersome restatements, we adopt the convention that λ(i) /µ(i)
always has the meaning of Definition 3.2 above. It is clear from the abacus
that µ(i) is a subpartition of λ(i) for each i ∈ {0, . . . , n − 1}, and so the


10

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

n-quotient is well-defined. It follows from Proposition 3.13 in [15], or our
Proposition 3.6 below, that the n-sign of a skew-partition is well defined.
See §3.4 below for an example of these definitions and all the results in this
section.
We remark that it appears to be impossible to define the n-core of an
arbitrary skew-partition. The example λ/µ = (2, 2)/(1) and n = 2 illustrates
the obstacles that arise. Representing λ on a 2-runner abacus as
◦ ◦
• •
we see that either bead may be moved up, giving two different skew-partitions
from which no border strip of length 2 can be removed, namely (2)/(1)
and (1, 1)/(1). The 2-quotients corresponding to these bead moves, namely
((1), ∅) and (∅, (1)), are also different.
Theorem 3.3 (Farahat). Let m, n ∈ N and let λ/µ be a skew-partition
of mn. Let α be a partition of m. If λ/µ is not n-decomposable then
χλ/µ (gnα ) = 0. If λ/µ is n-decomposable and (λ(0) /µ(0) , . . . , λ(n−1) /µ(n−1) )
is its n-quotient, then
χλ/µ (gnα ) = εn (λ/µ) IndSSm
` ×···×S`
0

(0) /µ(0)

χλ
n−1

× · · · × χλ

(n−1) /µ(n−1)



(gα )

where |λ(i) /µ(i) | = `i .
This result, stated in the alternative language of star diagrams, was first
proved in [5, Section 4]. The special case where µ is the n-core of λ also
follows from the correction by Thrall and Robinson [21] to Section 7 of
Robinson [18] or, alternatively, from Littlewood’s result in [11, Section 2].
Farahat’s proof depends on an algebraic argument using Schur functions. A
character-theoretic proof is given by Kerber, Sänger, and Wagner: see [10,
Equation 3.6]. In the remainder of this section, we give a shorter charactertheoretic proof of Theorem 3.3, expressing each side of the theorem as a sum,
and then constructing a bijection between the summands. An example to
illustrate this bijection is given in §3.4. (Our bijection is similar to that
defined using Brettspiele in [10].)

3.2. A model for induction from a Young subgroup. The following
general result on the values of a character induced from a Young subgroup
will be used in the proof of Theorem 3.3. (The notation is chosen to be
consistent with this later use.)


CHARACTER DEFLATIONS

11

Lemma 3.4. Let (`0 , . . . , `n−1 ) be a composition of m ∈ N. For each i ∈
{0, . . . , n − 1}, let ϑi be a character of S`i . If g ∈ Sm then
X
(ϑ
×
·
·
·
×
ϑ
)(g)
=
ϑ0 (gα0 (t) ) . . . ϑn−1 (gαn−1 (t) )
IndSSm
0
n−1
×···×S
`
`
0

n−1

t

where the sum is over all (`0 , . . . , `n−1 )-tabloids t such that gt = t, and αi (t)
is the cycle type of the permutation induced by g on the entries of row i + 1
of t.
Proof. Let t1 , . . . , tN be the (`0 , . . . , `n−1 )-tabloids. Let s be a (`0 , . . . , `n−1 )tabloid fixed by the Young subgroup S`0 × · · · × S`n−1 . For each j such that
1 ≤ j ≤ N , choose xj ∈ Sm such that tj = xj s. Let ϑ = ϑ0 × · · · × ϑn−1 .
For each g ∈ Sm we have
X

ϑ
(g)
=
ϑ(x−1
IndSSm
j gxj )
×···×S
`
`
0

n−1

j

where the sum is over all j such that
x−1
j gxj ∈ S`0 × · · · × S`n−1 ,
or, equivalently, over all j such that gtj = tj . If ∆1 , . . . , ∆q are the orbits
−1
−1
of g on row i + 1 of tj , then x−1
j ∆1 , . . . , xj ∆q are the orbits of xj gxj on
row i + 1 of s. Hence x−1
j gxj acts with cycle type αi (tj ) on row i + 1 of s
and so
ϑ(x−1
j gxj ) = ϑ0 (gα0 (tj ) ) . . . ϑn−1 (gαn−1 (tj ) ).
The lemma follows.



3.3. Proof of Theorem 3.3. Let m, n ∈ N and let λ/µ be a skew-partition
of mn. Let α be a partition of m. If there is a border-strip tableau of shape
λ/µ and type nα then it is clear from the abacus that λ/µ is n-decomposable.
Hence if λ/µ is not n-decomposable then, by the Murnaghan–Nakayama
rule, χλ/µ (gnα ) = 0.
We may therefore assume that λ/µ is n-decomposable. Let `i = |λ(i) /µ(i) |
for each i ∈ {0, . . . , n − 1} and let H = S`0 × · · · × S`n−1 . To show that
(0)
(0)
(n−1) /µ(n−1) 
(4)
χλ/µ (gnα ) = εn (λ/µ) IndSHm χλ /µ × · · · × χλ
(gα ),
we shall use the following generalization of border-strip tableaux.
Definition 3.5. Let m, n ∈ N. Let λ/µ be an n-decomposable skewpartition and let α = (α1 , . . . , αk ) be a composition of m. A n-quotient
border-strip tableau of shape λ/µ and type α is an n-tuple (T0 , . . . , Tn−1 ) of
border-strip tableaux such that
(a) for each i ∈ {0, . . . , n − 1}, the shape of Ti is λ(i) /µ(i) , and
(b) for each j ∈ {1, . . . , k}, the boxes in the Ti labelled j lie in a single
tableau, where they form a border strip of length αj .


12

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

By the Murnaghan–Nakayama rule we have
X
χλ/µ (gnα ) =
sgn(T )
where the sum is over all border-strip tableaux of shape λ/µ and type nα.
The bijection in the following proposition implies that
X
(5)
χλ/µ (gnα ) = εn (λ/µ)
sgn(T0 ) . . . sgn(Tn−1 )
where the sum is over all n-quotient border-strip tableaux (T0 , . . . , Tn−1 ) of
shape λ/µ and type α. An illustrative example of the bijection is given in
Figure 2 in §3.4 below.
Proposition 3.6. Let λ/µ be an n-decomposable skew-partition of mn and
let α = (α1 , . . . , αk ) be a partition of m. There is a canonical bijection between border-strip tableaux of shape λ/µ and type nα and n-quotient borderstrip tableaux of shape λ/µ and type α. Under this bijection, if T is mapped
to (T0 , . . . , Tn−1 ), then
sgn(T ) = εn (λ/µ) sgn(T0 ) . . . sgn(Tn−1 ).
Proof. Let T be a border-strip tableau of shape λ/µ and type α. The abacus
gives a canonical bijection between border strips in λ/µ of length n` and
border strips of length ` in the skew-partitions λ(i) /µ(i) for i ∈ {0, . . . , n−1}.
If the border strip of length nαk in T corresponds to a border strip of
length αk in λ(ik ) /µ(ik ) , then we label the corresponding boxes in the Young
diagram of λ(ik ) /µ(ik ) by k. Removing these border strips from the tableaux
concerned and iterating the process with the border strip of length nαk−1 ,
and so on, we obtain a canonical bijection between border-strip tableaux of
shape λ/µ and type nα and n-quotient border-strip tableaux of shape λ/µ
and type α.
It only remains to prove the assertion about signs. Since εn (λ/µ) is the
common sign of any λ/µ-tableau of shape λ/µ and type (nm ), it suffices to
show that if T is a λ/µ-tableau of type nα and U is a λ/µ-tableau of type
nβ then
sgn(T )sgn(U ) = sgn(T0 ) . . . sgn(Tn−1 )sgn(U0 ) . . . sgn(Un−1 ).
Starting from Γ(λ) with the beads numbered in order of their positions,
perform the sequence of bead moves corresponding to T , then perform the
inverse of the sequence of bead moves corresponding to U . Let σ be the
resulting permutation of the beads. Each time a border-strip of height ` is
removed or added, the permutation required to restore the order of numbers
is an ` + 1-cycle. Therefore sgn σ = sgn(T )sgn(U ). On the other hand, σ
permutes the beads on each runner amongst themselves, and a similar argument shows that sgn(σ) = sgn(T0 ) . . . sgn(Tn−1 )sgn(U0 ) . . . sgn(Un−1 ).



CHARACTER DEFLATIONS

13

Comparing Equations (4) and (5) we see that to complete the proof of
Theorem 3.3, it suffices to show that
X
(0)
(0)
(n−1) /µ(n−1) 
(6)
sgn(T0 ) . . . sgn(Tn−1 ) = IndSHm χλ /µ × · · · × χλ
(gα )
where the sum is over all n-quotient border-strip tableaux (T0 , . . . , Tn−1 ) of
shape λ/µ and type α. In fact Equation (6) follows from Lemma 3.4 and
the Murnaghan–Nakayama rule, by some manipulations that are essentially
formal. By Lemma 3.4 we have
(0)
(0)
(n−1) /µ(n−1) 
IndSHm χλ /µ × · · · × χλ
(gα )
X (0) (0)
(n−1) /µ(n−1)
(7)
=
χλ /µ (gα0 (t) ) . . . χλ
(gαn−1 (t) )
t

where the sum is over all (`0 , . . . , `n−1 )-tabloids t such that gα t = t and
αi (t) is the cycle type of the permutation of row i + 1 of t induced by gα .
For such a tabloid t, let
X
f (t) =
sgn(T0 ) . . . sgn(Tn−1 )
where the sum is over all n-quotient border-strip tableaux (T0 , . . . , Tn−1 )
of shape λ/µ and type α, such that Ti has a border strip labelled j (of
length αj ) if and only if the elements of the orbit of gα corresponding to the
part αj lie in row i + 1 of t. The Murnaghan–Nakayama rule implies that if
gα t = t then
χλ

(0) /µ(0)

(gα0 (t) ) . . . χλ

(n−1) /µ(n−1)

(gαn−1 (t) ) = f (t),

and so, by Equation (7),
IndSHm χλ

(0) /µ(0)

(n−1) /µ(n−1)

× · · · × χλ



(gα ) =

X

f (t)

where the sum is over all (`0 , . . . , `n−1 )-tabloids t such that gα t = t. Every
n-quotient border-strip tableau of shape λ/µ and type α corresponds to
some tabloid t such that gα t = t. Thus
X
X
sgn(T0 ) . . . sgn(Tn−1 ) =
f (t)
where the left-hand sum is over all n-quotient border-strip tableaux of shape
λ/µ and type α, and the right-hand sum is over all (`0 , . . . , `n−1 )-tabloids t
such that gα t = t. Equation (6) now follows on comparing the two preceding
equations.
3.4. Example. We give an example of the correspondences used in the
proof of Theorem 3.3. Let λ/µ = (8, 5, 3, 2, 2, 2)/(2, 2, 1, 1, 1). Any borderstrip tableau of shape λ/µ and type (35 ) has either two or four 3-borderstrips of height 1, with the rest of height 0, so ε3 (λ/µ) = 1. Let α =
(2, 1, 1, 1). By the Murnaghan–Nakayama rule, χλ/µ (g3α ) is the sum of the
signs of the four border-strip tableaux of type λ/µ and type 3α = (6, 3, 3, 3)


14

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

1 1 1 1 1 1
2 2 2
3 3
3
4
4 4

1 1 3 4 4 4
1 3 3
1 1
1
2
2 2

1 1 2 4 4 4
1 2 2
1 1
1
3
3 3

1 1 2 3 3 3
1 2 2
1 1
1
4
4 4

 2
3 ,
4

 1
1 ,
2

 1
1 ,
3

 1
1 ,
4


1 1 ,∅


3 4 ,∅


2 4 ,∅


2 3 ,∅

Figure 2. The bijection in Proposition 3.6 between border-strip tableaux
of shape (8, 5, 3, 2, 2, 2)/(2, 2, 1, 1, 1) and type (6, 3, 3, 3) and 3-quotient
border-strip tableaux of the same shape and type (2, 1, 1, 1). The
shapes of the border-strip tableaux forming each 3-quotient border-strip
tableau are given by the 3-quotient of (8, 5, 3, 2, 2, 2)/(2, 2, 1, 1, 1), namely

(1, 1, 1), (3, 1)/(1, 1), ∅ . To make clear the skew-shape, the tableaux of
shape (3, 1)/(1, 1) are drawn as (3, 1)-tableaux with two empty boxes.

shown in Figure 2 above. Their signs are +1, −1, −1, −1, respectively, so
χλ/µ (g3α ) = −2. These tableaux are in bijection with the four 3-quotient
border-strip tableaux of shape λ/µ and type α = (2, 1, 1, 1) shown in Figure 2; since sgn3 (λ/µ) = 1, the bijection is sign preserving.

The 3-quotient of λ/µ is (1, 1, 1), (3, 1)/(1, 1), ∅ , so the characters of S3
and S2 we must consider are the sign character and the trivial character,
respectively. Taking g(2,1,1,1) = (12) ∈ S5 , and following the end of the
proof of Theorem 3.3, we see that there are four (3, 2)-tabloids fixed by
(12), namely
3 4 5 ,
1 2

1 2 3 ,
4 5

1 2 4 ,
3 5

1 2 5,
3 4

in the order corresponding to the tableaux shown in Figure 2. The corresponding values of the function f used in the proof of Theorem 3.3 are +1,
−1, −1, −1 respectively. It should be noted that in general there will be
several tableaux corresponding to each product of character values
χλ

(0) /µ(0)

(gα0 (t) ) . . . χλ

(n−1) /µ(n−1)

(gαn−1 (t) );

it is a special feature of this example that each f (t) has a single summand,
and so the bijection extends all the way to tabloids.
4. Proof of Theorem 1.5
We shall prove Theorem 1.5 by induction on the number of parts of γ.
Most of the work occurs in proving the base case when γ has a single part.
In the first step we combine the results of §3 and §4. For later use in §6, we
state the following proposition for a general deflation map.


CHARACTER DEFLATIONS

15

Proposition 4.1. Let m, n ∈ N, let ϑ be an irreducible character of Sm ,
and let λ/µ be a skew-partition of mn. Let g ∈ Sn be an n-cycle. If λ/µ is
not n-decomposable, then DefresϑSn (g) = 0. If λ/µ is n-decomposable, then
D
E
(0)
(0)
(n−1) /µ(n−1) 
(DefresϑSn χλ/µ )(g) = εn (λ/µ) IndSHm χλ /µ × · · · × χλ
,ϑ ,
where H = S|λ(0) /µ(0) | × · · · × S|λ(n−1) /µ(n−1) | .
Proof. If λ/µ is not n-decomposable then, by Theorem 3.3, χλ/µ (gnα ) = 0 for
all partitions α of m. Hence, by Proposition 2.6(ii), (DefresϑSn χλ/µ )(g) = 0.
If λ/µ is n-decomposable then, using Proposition 2.6(i), we may restate
Theorem 3.3 as
(0)
(0)
(n−1) /µ(n−1) 
(8) ω(ResSm oSn χλ/µ ) = εn (λ/µ) IndSHm χλ /µ × · · · × χλ
.
The result now follows from Proposition 2.6(ii).



It is clear from the condition on row numbers in Equation (1) in Definition 1.4 that if λ/µ is a skew-partition of mn then there is at most one
m-border-strip tableau of shape λ/µ and type (n). The following lemma
gives a more precise condition. Recall that a skew-partition σ/τ is said to
be a horizontal strip if the Young diagram of σ/τ has no two boxes in the
same column.
Lemma 4.2. Let m, n ∈ N and let λ/µ be a skew-partition of mn. If λ/µ
is n-decomposable, and each λ(i) /µ(i) is a horizontal strip, then there is a
unique m-border-strip tableau of shape λ/µ and type (n); this tableau has
sign εn (λ/µ). Otherwise there are no such tableaux.
Proof. Suppose that T is an m-border-strip tableau of type (n) and shape
λ/µ. Then by Definition 3.1, λ/µ is n-decomposable. Let Γ(λ) be an nrunner abacus display for λ using tn beads for some t ∈ N. Let Γ(µ) be
the abacus display for µ obtained from Γ(λ) by an appropriate sequence of
m single bead moves, so that in each move a bead is slid upwards into a
gap immediately above it. We label the positions on the abacus from top
to bottom so that the positions in row r of an abacus display are numbered
(r − 1)n, . . . , rn − 1 (as usual). Observe that the row number of a border
strip of length n in T corresponding to a bead in position p of Γ(λ) is the
number of beads in positions p + 1, p + 2, . . . of Γ(λ). Therefore if p < p0
and the beads in positions p and p0 of Γ(λ) both correspond to border strips
in T , then in the sequence of bead moves corresponding to T , the bead in
position p0 is moved upwards before the bead in position p.
Let i ∈ {0, . . . , n − 1}. Suppose that Γ(λ) has beads in positions nq + i
and nq 0 +i where q < q 0 , and that Γ(µ) has no beads in positions n(q +1)+i,
. . . , nq 0 + i. The bead in position nq + i of Γ(λ) prevents the bead initially


16

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

in position nq 0 + i from reaching its final position in Γ(µ). Therefore the
bead in position nq + i must be moved before the bead in position nq 0 + i
reaches its final position. This contradicts the previous paragraph. Hence
there exist xj ∈ N0 and yj ∈ N0 such that the beads on runner i of Γ(λ)
are in positions {i + nxj : 1 ≤ j ≤ s}, the beads on runner i of Γ(µ) are in
positions {i + nyj : 1 ≤ j ≤ s} and
(9)

y1 ≤ x1 < y2 ≤ x2 < · · · < ys ≤ xs .

It easily follows that λ(i) /µ(i) is a horizontal strip. Then, by Proposition 3.6,
sgn(T ) = εn (λ/µ).
Conversely, suppose that λ/µ is n-decomposable and each λ(i) /µ(i) is a
horizontal strip. Then the inequality (9) on the bead positions in each runner
holds. We now describe a sequence of m single upward bead moves that
transforms Γ(λ) into Γ(µ), and thus corresponds to a border-strip tableau T
of shape λ/µ and type (n)?m . At each step, locate the bead with maximal
position p such that there is no bead in position p of Γ(µ). Slide that bead
up into position p − n. This is possible by inequality (9). The row numbers
of the border strips of length n corresponding to this sequence of moves
are increasing, so T is a m-border-strip tableau of shape λ/µ and type (n).
Uniqueness is clear since there is always at most one m-border strip tableau
of shape λ/µ and type (n).

We can now complete the proof of the base case.
Proposition 4.3. Let m, n ∈ N and let g ∈ Sn be an n-cycle. If λ/µ is a
skew-partition of mn then
(DefresSn χλ/µ )(g) = aλ/µ,(n) .
Proof. If λ/µ is not n-decomposable then aλ/µ,(n) = 0 by Lemma 4.2. Proposition 4.1 implies that the result holds in this case.
Now suppose that λ/µ is n-decomposable. Let `i = |λ(i) /µ(i) | for each
i ∈ {0, . . . , n − 1}. By Proposition 4.1 and Frobenius reciprocity, we have
D (0) (0)
E D (n−1) (n−1)
E
/µ
(DefresSn χλ/µ )(g) = εn (λ/µ) χλ /µ , 1S`0 . . . χλ
, 1S`n−1 .
It follows from [8, Theorem 2.3.13(ii)] that if σ/τ is a skew-partition of `
then

E 1 if σ/τ is a horizontal strip
D
χσ/τ , 1S` =
0 otherwise.
Therefore (DefresSn χλ/µ )(g) = εn (λ/µ) if each λ(i) /µ(i) is a horizontal strip,
and otherwise (DefresSn χλ/µ )(g) = 0. The proposition now follows from
Lemma 4.2.



CHARACTER DEFLATIONS

17

For the inductive step we need the following lemma and proposition. The
former is well-known and can be deduced from [8, 2.3.12]. We write µ ⊆ λ
if µ is a subpartition of λ (i.e. the Young diagram of µ is contained in that
of λ).
Lemma 4.4. Let λ/µ be a skew-partition of r. If 1 ≤ c < r then
X
χτ /µ × χλ/τ
ResSc ×Sr−c χλ/µ =
τ

where the sum is over all partitions τ such that µ ⊆ τ ⊆ λ and |τ /µ| = c.
For later use we state and prove the following proposition for a general
deflation map.
Proposition 4.5. Let m, n ∈ N and let λ/µ be a skew-partition of mn.
Let ϑ be an irreducible character of Sm . Let g ∈ Sn . If g = kh where k ∈ S`
and h ∈ Sn−` , then
X
(DefresϑSn χλ/µ )(g) =
(DefresϑS` χτ /µ )(k)(DefresϑSn−` χλ/τ )(h)
τ

where the sum is over all partitions τ such that µ ⊆ τ ⊆ λ and |τ /µ| = m`.
Proof. Let B be the base group of the wreath product Sm o Sn ≤ Smn .
Choose a subgroup Sm` × Sm(n−`) ≤ Smn containing B. If ψ is a character
of Sm o Sn then it is easily checked that
m oSn
ResS` ×Sn−` (Def ϑSn ψ) = (Def ϑS` × Def ϑSn−` )(ResSSm
oS` ×Sm oSn−` ψ).

Hence
χ)
ResS` ×Sn−` (DefresϑSn χ) = (DefresϑS` × DefresϑSn−` )(ResSSmn
m` ×Sm(n−`)
for any character χ of Smn . The proposition now follows from the expression
for ResSm` ×Sm(n−`) χλ/µ given in Lemma 4.4.

We are now ready to prove Theorem 1.5. Let m, n ∈ N and let λ/µ be
a skew-partition of mn. Let γ = (γ1 , . . . , γd ) be a composition of n. Let
g ∈ Sn have cycle type γ and let h ∈ Sn−γ1 have cycle type (γ2 , . . . , γd ). Note
that, by Lemma 4.2, if τ /µ is a skew-partition of mγ1 then there is at most
one m-border-strip tableau of shape τ /µ and type (γ1 ). We shall denote
this tableau by Tτ /µ when it exists. By Definition 1.4, aτ /µ,(γ1 ) = sgn(Tτ /µ )
(or is zero if no such tableau exists). Therefore Proposition 4.3 may be
restated as (DefresSγ1 χτ /µ )(k) = sgn(Tτ /µ ), where k ∈ Sγ1 is a γ1 -cycle and
(DefresSγ1 χτ /µ )(k) = 0 if no tableau Tτ /µ exists. It therefore follows from
Proposition 4.5 that
X
(10)
(DefresSn χλ/µ )(g) =
sgn(Tτ /µ )(DefresSn−γ1 χλ/τ )(h)
τ


18

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

where the sum is over all partitions τ such that µ ⊆ τ ⊆ λ, |τ /µ| = mγ1
and there is an m-border-strip tableau of shape τ /µ. By induction on the
number of parts of γ we have
X
sgn(Tτ /µ )aλ/τ,(γ2 ,...,γd )
(DefresSn χλ/µ )(g) =
τ

with the same conditions on the sum. It is clear that if T is an m-border-strip
tableau of shape λ/µ and type γ then the border strips in T corresponding to
the m parts of length γ1 in γ ?m form an m-border-strip tableau of shape τ /µ
for some τ . Therefore the right-hand side of the previous equation is aλ/µ,γ .
This completes the proof of Theorem 1.5.
