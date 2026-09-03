---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual Sn characters"
section_id: sec-000-define-the-virtual-sn-character-n-as-follows
section_title: "Define the virtual Sn character \u03c8\u03bd,n as follows:"
section_number: 4
pages: 3-11
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
doc_brief: "The Murnaghan-Nakayama rule and some virtual Sn characters — 1 sections: Define the virtual Sn character ψν"
---
ψν,n :=

n−k
X

(−1)j+1 χν∗Sj .

(2)

j=1

5. We say that ν ∗ S ”has a tail” if ν ∗ S = µ = (µ1 , µ2 , . . .) where µ1 ≥ ν1 + 1.
The following unique-decomposition lemma is crucial here.
Lemma 2.4. Let n ≥ 2k + 2. For i = 1, 2 let ν (i) ⊢ k, and let S (i) be a rim of ν (i) ∗ S (i) of
length n − k.
If ν (1) ∗ S (1) = ν (2) ∗ S (2)

then

ν (1) = ν (2)

and S (1) = S (2) .

Note that Example 2.6 below shows that the condition n ≥ 2k + 2 is necessary.
Proof. Denote η = ν (1) ∗ S (1) = ν (2) ∗ S (2) . There are three cases to consider.
Case 1: S (1) covers an upper part of ν (1) (and has a North-East tail).
case 2: The conjugate of case 1.
Case 3: S (1) completely covers ν (1) (and might have a North-East and/or South-East tails).
Case 1: Here the rim of ν (1) ∗ S (1) contains S (1) and possibly an additional part which is a
part of ν (1) . Assume η = ν (1) ∗ S (1) = ν (2) ∗ S (2) with ν (1) 6= ν (2) . Then ν (2) contains a cell
of S (1) . This cell splits S (1) into two parts: the North-East part of S (1) and the South-East
part (which contains the South-East part of S (1) ). Let S̃ denote the South-East part of S (1)
together with the lower part of the rim of ν (2) . We need to show that neither the North-East
part of S (1) , nor S̃ can be S (2) .
The North-East part is properly contained in S (1) hence has length strictly less than |S (1) | =
n − k, thus this part cannot be S (2) .
Since we are in case 1, the part S̃ is a part of ν (2) . But ν (2) ⊢ k, hence S̃ is of length
|S̃| ≤ k < n − k, hence this part cannot be S (2) either.
So case 1 is impossible. By conjugation, case 2 is also impossible.
Case 3. The argument here is similar: A cell of ν (2) on S (1) splits the rim of ν (1) ∗ S (1)
(namely S (1) ) into two parts, each of length strictly less than n − k, hence neither can be
S (2) . Thus case 3 is also impossible, and the proof follows.


Lemma 2.5. Let ν ⊢ k and let n ≥ 2k + 2. As in Definition 2.3, construct the sequence of
partitions ν ∗ S1 , ν ∗ S2 , . . . , ν ∗ Sn−k . Then h(Sj ) = j for 1 ≤ j ≤ n − k.
Here also, Example 2.6 shows that the condition n ≥ 2k + 2 is necessary.
Proof. Analogue to the height h(S), we also define the width w(S) (which is the height of
the conjugate rim S ′ ). By projecting S on the axes (see also (1.7) in [2]), it follows that
|S| = h(S) + w(S) − 1.

(3)

Note that n − k ≥ ν1 + ν1′ + 1. Indeed, k ≥ ν1 + ν1′ − 1, so n − k ≥ k + 2 ≥ ν1 + ν1′ + 1.
As in Definition 2.3.2, construct the sequence ν ∗ S1 , ν ∗ S2 , . . .. For the first ν1′ + 1 steps, by
construction and induction, h(Sj ) = j, 1 ≤ j ≤ ν1′ + 1 (since |S| = n − k, while the number
of boxes in S except those in the first row of ν ∗ S is ≤ ν1 + ν1′ ≤ k). After ν1′ + 1 steps, ν is
”covered”, with ν1 + ν1′ + 1 out of the n − k cells are covering ν. Since n − k ≥ ν1 + ν1′ + 1, at
that stage there still is a ”tail” of added boxes in the first (i.e. top) row of ν ∗ Sj , j = ν1′ + 1.
For the remaining steps we consider the conjugate construction. Then, applying (3) together
with the above argument, the proof follows.
Example 2.6. Counter examples when n 6≥ 2k + 2.
1. Let k = 3, n = 6, η = (3, 3), ν (1) = (3), ν (2) = (2, 1). Let S (i) , i = 1, 2, satisfy
(3, 3) = ν (1) ∗ S (1) = ν (2) ∗ S (2) .
Then clearly S (1) 6= S (2) , as well as ν (1) 6= ν (2) .
2. Again let k = 3, n = 6. Let ν = (3) and construct the sequence of partitions
ν ∗ S1 , ν ∗ S2 , ν ∗ S3 . . . Then h(S2 ) = 1 6= 2.
We proceed with the general case.
Corollary 2.7. Let ν ⊢ k, and let n ≥ 2k + 2, then
ψν,n =

X

S, ν∗S⊢n

(−1)

h(S)+1 ν∗S

χ

=

n−k
X

(−1)h(Sj )+1 χν∗Sj .

j=1

Proof. This follows from Equation (2) (which defines ψν,n ) and from Lemma 2.5.


3

A formula for ψν,n (µ)

Our aim is to prove the following formula.
Theorem 3.1. Let ν = (ν1 , ν2 , . . .) ⊢ k, n ≥ 2k + 2 . Let µ = (µ1 , µ2 , . . .) ⊢ n, and denote
µ̄ = (µ2 , µ3 , . . .), so µ1 = n − k if and only if µ̄ ⊢ k. Then
(
χν (µ̄) · (n − k) if µ1 = n − k
ψν,n (µ) =
0
if µ1 6= n − k

(4)

The proof is given below.
Let n ≥ 2k + 2 and let ν ⊢ k, so (n − k, ν) is a partition of n. Let λ ⊢ n and assume
χλ(n−k,ν) 6= 0, then, by the Murnaghan-Nakayama (M-N) rule, λ can be written, probably
in several ways, as λ = ρ ∗ S where ρ ⊢ k, S is part of the rim of λ and |S| = n − k. By
Lemma 2.4 this decomposition, with |ρ| = k, is unique, hence we can write λ ↔ (ρλ , Sλ ).
Again by the M-N rule,with λ = ρ ∗ S,
χλ(n−k,ν) = (−1)h(S)+1 χρν = (−1)h(Sλ )+1 χρνλ .

(5)

Lemma 2.4 allows us to prove the following formula.
Proposition 3.2. Let ν ⊢ k and let n ≥ 2k + 2. Then
X
X
χρν · ψρ,n .
χλ(n−k,ν) χλ =
ρ⊢k

λ⊢n

Proof. We just saw that
{λ ⊢ n} = {ρ ∗ S ⊢ n | ρ ⊢ k, |S| = n − k} ∪ {λ ⊢ n | χλ(n−k,ν) = 0},
and by Lemma 2.4 we have the bijection
{ρ ∗ S ⊢ n | ρ ⊢ k, |S| = n − k} ←→ {(ρ, S) | ρ ⊢ k, |S| = n − k

and ρ ∗ S ⊢ n}.

We denote
Ak,n = {(ρ, S) | ρ ⊢ k, |S| = n − k

and ρ ∗ S ⊢ n}.

By (5)
X

χλ(n−k,ν) χλ =

λ⊢n

X

(−1)h(S)+1 χρν · χλ =

(ρ,S)∈Ak,n

X
ρ⊢k

X
ρ⊢k

X

(−1)h(S)+1 χρν · χρ∗S =

S, ρ∗S⊢n

χρν

X

S, ρ∗S⊢n

The last equality applied corollary 2.7.

(−1)h(S)+1 χρ∗S =

X
ρ⊢k

χρν · ψρ,n .


Remark 3.3.
Let d = |{P ar(k)}|. Note that in matrix form, Proposition 3.2 can be written as follows:
"
#
X
[χρν ] [ψρ,n ] =
(6)
χλ(n−k,ν) · χλ .
λ⊢n

Here [χρν ] is the d × d character table of Sk , and [ψρ,n ] is a column of height d. Of course, the
locations of the entries of both [χρν ] and [ψρ,n ] depend on how we order P ar(k). Applying (6)
on µ ⊢ n we get
"
#
X
ρ
λ
λ
[χν ] [ψρ,n (µ)] =
(7)
χ(n−k,ν) · χµ
λ⊢n

Recall the classical column-orthogonality-relations for the Sn characters.
Theorem 3.4. (The column-orthogonality-relations)
(
X
|ZSn (η)| if µ = η
χλη χλµ =
0
if µ 6= η,
λ⊢n

(8)

of η in Sn (i.e the centralizer of π ∈ Sn with
where λ, η, µ ⊢ n, and ZSn (η) is the centralizer
 
cycle structure η). Let K = K (n) = χθη denote the character table of Sn , then (8) can be
written as
KK T = diag(|ZSn (η)|, | η ⊢ n).

(9)

Then numbers |ZSn (η)| are calculated through the following well known formula.
Theorem 3.5. Let η ⊢ n, η = (1m1 , 2m2 , . . .), and let ZSn (η) denote the centralizer in Sn of
σ ∈ Sn where η is the cycle structure of σ. Then
Y
(imi · mi !).
|ZSn (σ)| = |ZSn (η)| =
i

Remark 3.6. Let ν ⊢ k, n ≥ 2k + 2. Then (n − k, ν) is a partition (of n), and
|ZSn (n − k, ν)| = |ZSk (ν)| · (n − k).
This follows from Theorem 3.5 since n−k is strictly larger than any component of ν. Together
with (8) this implies
Corollary 3.7. Let ν ⊢ k, n ≥ 2k + 2, µ = (µ1 , µ2 , . . .) ⊢ n and let µ̄ = (µ2 , µ3 , . . .). Then
(
X
|ZSk (ν)| · (n − k) if µ̄ = ν
(10)
χλ(n−k,ν) χλµ =
0
if
µ
=
6
η.
λ⊢n


3.1

The proof of Theorem 3.1

Apply (7) and Corollary 3.7: With ρ and ν denoting partitions of k and µ partitions of n
we have
# "(
#
"
X
|Z
(ν)|
·
(n
−
k)
if
µ̄
=
ν
Sk
=
[χρν ] [ψρ,n (µ)] =
χλ(n−k,ν) · χλµ =
0
if
µ̄
=
6
ν.
λ⊢n
"(
#
|ZSk (ν)| if µ̄ = ν
=
· (n − k)
0
if µ̄ 6= ν.

(11)

Restrict now to partitions µ = (n − k, µ̄) (so µ is given by µ̄), then (11) becomes

[χρν ] [ψρ,n (n − k, µ̄)] =

"
X

χλ(n−k,ν) · χλ(n−k,µ̄)

λ⊢n

#

"(
#
|ZSk (ν)| · (n − k) if µ̄ = ν
=
=
0
if µ̄ 6= ν.

#
"(
|ZSk (ν)| if µ̄ = ν
· (n − k).
=
0
if µ̄ 6= ν

(12)

Note that each side of (12) is a column of height d = |{P ar(k)}|, parametrized by the
partitions µ̄ ∈ P ar(k). Thus, if ν = µ̄(j) is the jth element in P ar(k) then the transpose of
the corresponding column of (12) is
(0, . . . , 0, |ZSk (µ̄(j) )|, 0, . . . , 0) · (n − k).
The columns [ψρ,n (n − k, µ̄)] of height d is parametrized by ρ ∈ P ar(k), with µ̄ fixed. From
these columns we form the d × d matrix


M = ψρ,n (n − k, µ̄(1) ), ψρ,n (n − k, µ̄(2) ), . . . , ψρ,n (n − k, µ̄(d) ) .
Also denote K = [χρν ] and D = diag(|ZSk (µ̄(1) )|, . . . , |ZSk (µ̄(d) )|). By (12) we get

[χρν ] M = KM = D · (n − k) = diag(|ZSk (µ̄(1) )|, . . . , |ZSk (µ̄(d) )|) · (n − k),
and by (9)
KK T = D = diag(|ZSk (µ̄(1) )|, . . . , |ZSk (µ̄(d) )|).
Thus we have KM = KK T · (n − k).
Note that K is the character table of Sk , hence is invertible. Left cancelation of K implies
that M = K T · (n − k), so M = (the character table of Sk ) · (n − k). This completes the
proof of Theorem 3.1.


3.2

Applications

Pn−1
j
(−1)j χ(n−j,1 ) . Theorem 3.1
Example 3.8. 1. In Example 2.2.1 we saw that ψ∅,n = j=0
with k = 0 then implies that
(
n−1
X
n if µ = (n)
j
(13)
ψ∅,n (µ) =
(−1)j χ(n−j,1 ) (µ) =
0 if µ 6= (n)
j=0
2. Similarly, by Example 2.2.2, ψ(1),n = χ(n) +
we get

Pn−4

j=0 (−1)

j+1 (n−2−j,2,1j )

χ

n

+ (−1)n χ(1 ) , and

ψ(1),n (µ) =

(n)

=χ

(µ) +

n−4
X

(−1)

j+1 (n−2−j,2,1j )

χ

n (1n )

(µ) + (−1) χ

(µ) =

j=0

(

n − 1 if µ = (n − 1, 1)
(14)
0
if µ 6= (n − 1, 1)

Clearly, there are infinitely many identities that can be deduced this way.
3. Consider the first column {f λ | λ ⊢ n} in the charcter table of Sn . Let n ≥ 2k + 2, fix
some ν ⊢ k, then construct the sequence of partitions of n: ν ∗ S1 , ν ∗ S2 , . . .. Finally, form
the corresponding alternating sum, then always
n−k
X

(−1)j f ν∗Sj = 0.

(15)

j=1

This follows from Theorem 3.1, since this corresponds to µ = (1n ), so µ1 = 1 6= n − k. When
k = 0 this is the well known identity
 
n
X
j n
= 0,
(−1)
j
j=1

(16)

see (13). Thus, (15) can be seen as a generalization of (16).
Remark 3.9. In [3] a formula is proved for the values
X
i
χ(n−i,1 ) (µ), µ ⊢ n.
i≥0

Of course, here we deduced a formula for the values for the corresponding alternating sum
X
i
(−1)i χ(n−i,1 ) (µ), µ ⊢ n.
i≥0


Adding, we get a formula for
X

χ(n−i,1 ) (µ),

i

µ ⊢ n,

X

χ(n−i,1 ) (µ),

i

µ ⊢ n.

i even

hence also for

i odd

We leave the details for the reader.

4

Final remarks

Remark 4.1. Let n ≥ 4 and let An be the set of partitions obtained by walking around
ν = (1):
An = {(n), (1n )} ∪ {(r, 2, 1n−2−r ) | 2 ≤ r ≤ n − 2}.
Then
X

f λ = (n − 4) · 2n−2 + 4.

(17)

λ∈An

Proof. Let λ = (r, 2, 1n−2−r ), then


n(n − 2)(n − 3) n − 4
n!
.
=
f =
r−2
(r − 2)!(n − 2 − r)!r(n − r)(n − 1)
r(n − r)
λ

Thus, omitting λ ∈ {(n), (1n )}, we need to show that


n−4
X
n(n − 2)(n − 3) n − 4
r=0

r(n − r)

r−2

= (n − 4) · 2n−2 + 2.

(18)

This can be proved by the Zeilberger Algorithm [5], and is implemented in Maple (function
SumTools[Hypergeometric][Zeilberger]).
Here is a direct proof.
Zeilberger. Note that
1
1
=
r(n − r)
n



1
1
+
r n−r



,

so the sum in (18) equals
(n − 2)(n − 3)


n−2 
X
1 n−4
r=2

r r−2

n−2
X



1
n−4
+ (n − 2)(n − 3)
.
n−r r−2
r=2


By symmetry these two summands are equal, so this equals

n−2 
X
1 n−4
=
2(n − 2)(n − 3)
r r−2
r=2
n−2 Z 1
X



n−4
=
2(n − 2)(n − 3)
x dx
r−2
0
r=2


n−2 Z 1
X
n−4
r−1
=
2(n − 2)(n − 3)
x dx
r−2
0
r=2


n−4 Z 1
X
n−4
r+1
=
x dx
2(n − 2)(n − 3)
r
0
r=0
Z 1
2(n − 2)(n − 3)
x(1 + x)n−4 dx =
0
Z 1

Z 1
n−3
n−4
2(n − 2)(n − 3)
(1 + x) dx −
(1 + x) dx =
r−1

0

0

= (n − 4)2

n−2

+ 2.

Here is a second, combinatorial proof [Zeilberger].
Let f (n) be the number of standard Young tableaux of shape (r, 2, 1n−2−r ) for some 2 ≤ r ≤
n − 2, and look at the location of n.
Case 1: It is at the rightmost cell of the top row. Deleting it gives something counted by
f (n − 1).
Case 2. The conjugate case, also yielding f (n − 1).
Case 3: n is in the (2, 2) cell. Deleting it gives a tableau of strict hook shape (namely, not
(n − 1) nor (1n−1 )). Clearly, the number of these tableaux is 2n−1 − 2.
So we have the recurrence f (n) = 2f (n−1)+2n−1 −2. Since f (4) = 2, it follows by induction
that f (n) = (n − 4)2n−2 + 2.

4.1

The polynomials pν,n(t)

Recall Equation (15), replace minus 1 by t and get the polynomials
pν,n (t) =

n−k
X

f ν∗Sj · tj .

(19)

j=1

In the case ν is empty we get p∅,n (t) = (t+1)n−1 . Denote p(1),n (t) = pn (t) in the case ν = (1).
By direct computations we got the following polynomials, for 1 ≤ n ≤ 9.


p4 (t) = (t + 1)2
p5 (t) = (t + 1)(t2 + 4t + 1)
p6 (t) = (t + 1)2 (t2 + 7t + 1)
p7 (t) = (t + 1)(t4 + 13t3 + 22t2 + 13t + 1)
p8 (t) = (t + 1)2 (t4 + 18t3 + 27t2 + 18t + 1)
p9 (t) = (t + 1)(t6 + 26t5 + 79t4 + 110t3 + 79t2 + 26t + 1)
p10 (t) = (t + 1)2 (t6 + 33t5 + 93t4 + 131t3 + 93t2 + 33t + 1)
By (15) pn (t) is divisible by t + 1 for all n.
Conjecture 4.2. We conjecture that when n is even, the highest power of t+1 which divides
pn (t) is 2, while when n is odd, the highest power on t + 1 which divides pn (t) is 1.
One also conjectures positiveness and unimodality on the coefficients of these polynomials.
Additional conjecture is as follows. Denote p2k+1 (t) = (t + 1) · q2k+1 (t), then q2k+1 (−1) = −2.

References
[1] G. James and A. Kerber, The Representation Theory of the Symmetric Group, Encyclopedia of Math. Vol. 16, Addison-Wesley Publishing Company.
[2] I. G. Macdonald, Symmetric Functions and Hall Polynomials, Second Edition (1995).
[3] A. Regev, Lie superalgebras and some characters of Sn , to appean in Israel J. Math
(2013).
[4] B. E. Sagan, The Symmetric Group, Graduate Text in Mat. Second Edition (2000).
[5] D. Zeilberger, The method of creative telescoping, J. Symbolic Computation 11, 195-204
(1991).
