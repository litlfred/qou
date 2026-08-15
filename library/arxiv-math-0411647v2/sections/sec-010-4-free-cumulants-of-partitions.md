---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-010-4-free-cumulants-of-partitions
section_title: "Free cumulants of partitions"
section_number: 4
pages: 27-33
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
4.2.1. Moments and cumulants of partitions. Let X be an ordered set. We
deﬁne the moment MP
X (where the letter P stands for partition) by
MP
X =
∑
σ ∈P(X)
σ,
where the sum denotes a formal linear combination and it runs over all
partitions of X.
Let ρ = {ρ1, . . . , ρ r}be a non–crossing partition. Motivated by (4.5) we
deﬁne
MP
ρ =
∏
s
MP
ρ s =
∑
σ 1 ,...,σ r
∏
s
σ s,
where the sum runs over all tuples(σ 1, . . . , σ r) such that σ s is a partition of
the set ρs and products denote ρ–ordered products of partitions.
28 PIOTR ´SNIADY
Proposition 4.2. For every non–crossing partitionρ of the set X we have
(4.4) MP
ρ =
∑
σ ≥ρcomp− 1
σ,
where the sum runs over all partitions σ of the set X such that σ ≥ ρcomp− 1.
Proof. Probably the best way to prove the proposition is to consider the
graphical description of the partition multiplication from Section 3.2.2. We
present an alternative proof below.
From the very deﬁnition of multiplication one can see that every partition
σ which appears in MP
ρ must fulﬁll σ ≥ ρcomp− 1.
To any partition σ of the set X we can assign a tuple (σ 1, . . . , σ r), where
σ s (a partition of the set ρs) is obtained from σ by restriction to the set ρs.
Now it is easy to observe that every σ ≥ ρcomp− 1 appears exactly once in∏
s MP
ρ s, namely in the factor ∏
s σ s. □
The moment map MP gives rise to a sequence of free cumulants which
will be denoted by RP
n.
4.2.2. Moments and cumulants of Jucys–Murphy element. Inspired by
(4.1) we shall denote by MJM
ρ the partition–indexed moments of the Jucys–
Murphy element, deﬁned by
(4.5) MJM
ρ =
∏
1≤s≤r
MJM
|ρ s| =
∏
1≤s≤r
E(J|ρ s |) ∈ C(~S∞),
where ρ = {ρ1, . . . , ρ r}is a non–crossing partition. The moment map MJM
gives rise to a sequence of free cumulants which will be denot ed by RJM
n .
Please note that MJM
1 = E(J) = 0 and therefore also RJM
1 = 0.
4.2.3. The relation between the partitions and the Jucys–Murphy el ement.
The following Claim provides a link between the moments of th e Jucys–
Murphy element and the moments of partitions.
Claim 4.3. Let X be a ﬁnite ordered set, let ρ be a non–crossing partition
of a ﬁnite ordered set and n ≥ 1 be an integer. Then
Σ (MP
X) = MJM
|X|,(4.6)
Σ (MP
ρ) = MJM
ρ ,(4.7)
Σ (RP
n) = RJM
n ,(4.8)
where Σ is the map considered in Section 3.1.1.
We postpone the proof of (4.6) to Theorem 5.12. Equation (4.6 ) implies
(4.7) immediately because Σ is a homomorphism. Equation (4.8) is an im-
mediate consequence of (4.7).
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 29
This result implies that all questions about the moments of t he Jucys–
Murphy element can be easily translated into questions abou t moments of
partitions and the machinery of Section 3 can be applied.
4.2.4. Free cumulants of partitions.
Proposition 4.4. For every n ≥ 1
(4.9) RP
n =
∑
π ∈P(1,2,...,n )
Iπ π,
(4.10) RJM
n =
∑
π ∈P(1,2,...,n )
Iπ Σ π ,
where Iπ ∈ Z, called free index of π, is deﬁned by
(4.11) Iπ =
∑
ρ∈NC(1,2,...,n )
ρ≤π
Moebρ .
Proof. From (4.2) and (4.4) it follows that
RP
n =
∑
ρ∈NC(1,2,...,n )
Moebρcomp
∑
π ∈P(1,2,...,n )
π ≥ρcomp
π =
∑
π ∈P(1,2,...,n )
π
∑
ρ∈NC(1,2,...,n )
ρcomp≤π
Moebρcomp =
∑
π ∈P(1,2,...,n )
π
∑
ρ∈NC(1,2,...,n )
ρ≤π
Moebρ ,
where in the last equality we used the fact that ρ ↦→ ρcomp is a permutation
of the set of non–crossing partitions.
The second identity (4.10) follows now from Claim 4.3. □
4.2.5. Evercrossing partitions. We say that a partition π of a ﬁnite ordered
set X is evercrossing if for any a < c (a, c ∈ X) such that a is connected
with c by π there exist b, d ∈ X such that
(1) elements a, b, c, d are ordered up to a cyclic rotation, i.e. either
a < b < c < d or d < a < b < c ,
(2) elements b and d are connected by π,
(3) elements a, b, c, d are not elements of the same block of π.
Up to some technical details, this means that on the graphical representation
of π every line connecting a pair of elements must be crossed by some other
line. For example, partition from Figure 4.1 is evercrossin g, but partition
from Figure 2.3 is not.
The following result shows that only evercrossing partitions contribute to
sums (4.9) and (4.10).
30 PIOTR ´SNIADY
FIGURE 4.1. Example of an evercrossing partition
Theorem 4.5. If a partition π is not evercrossing then Iπ = 0.
In order to prove this result we will need the following lemma.
Lemma 4.6. Let π = {π 1, . . . , π r}be a partition ofX. Let σ = {π 1, . . . , π s},
τ = {π s+1, . . . , π r}be a decomposition of π into two partitions of disjoint
sets S = π 1 ∪ · · · ∪π s and T = π s+1 ∪ · · · ∪π r such that σ is non–crossing.
For ρ ∈ NC(T ) we shall denote (with a small abuse of notation) by
ρcomp ∈ NC(S) the biggest non–crossing partition with a property that ρ ∪
ρcomp is non–crossing. We denote by σ ∧ ρcomp ∈ NC(S) the biggest non–
crossing partition which is smaller both than σ and ρcomp.
Then the free index of π is given by
(4.12) Iπ =
∑
ρ∈NC(T)
ρ≤τ
(σ ∧ ρcomp) is trivial
Moebρ .
Proof. Since every ρ ∈ NC(X), ρ ≤ π can be decomposed as ρ = ˜ρ ∪ ^ρ,
where ˜ρ ∈ NC(S), ˜ρ ≤ σ and ^ρ ∈ NC(T ), ^ρ ≤ τ it follows from (4.11) that
Iπ =
∑
^ρ∈NC(T)
^ρ≤τ
Moeb^ρ
( ∑
˜ρ∈NC(S)
˜ρ ≤(σ ∧ ^ρcomp)
Moeb ˜ρ
)
.
We apply Lemma 4.1 and observe that the second sum is equal to z ero
unless σ ∧ ^ρcomp is trivial; otherwise it is equal to 1. □
Proof of Theorem 4.5. Let a, c be the vertices which have the property re-
quired for π = {π 1, . . . , π r}not to be evercrossing. By a change of number-
ing of blocks we can always assume that a, c ∈ π 1. Following the notation
of Lemma 4.6 we setS = π 1, T = π 2∪· · ·∪ π r, σ = {π 1}, τ = {π 2, . . . , π r}.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 31
FIGURE 4.2. Example of an evercrossing partition with the
free index equal to 0.
Observe that for every ρ ∈ NC(T ) such that ρ ≤ τ, we have that the
partition ρ ∪
{
{a, c }
}
is non–crossing, therefore ρcomp ≥
{
{a, c }
}
and
ρcomp ∧ σ ≥
{
{a, c }
}
must contain a non–trivial block and the sum in (4.12)
contains no summands. □
Remark. The converse implication is not true, as one can see on an example
from Figure 4.2.
4.3. First–order asymptotics of free cumulants.
Theorem 4.7. Let integers k1, . . . , k t ≥ 2 be given and let us express
RJM
k1 · · · RJM
kt ∈ P as a linear combination of normalized conjugacy class
indicators Σ . Then
(4.13) RJM
k1 · · ·RJM
kt = Σ k1 − 1,...,k t− 1+
(terms of degree at most k1 + · · · + kt − 2),
where the degree is taken with respect to the ﬁltration(2.8).
Proof. Let us consider the case t = 1; we set n = k1. Propositions 3.4 and
3.5 imply that the highest–order terms in the expansion (4.1 0) correspond
to non–crossing partitions and that the degree of all remaining terms will be
at most n − 2; by Theorem 4.5 a partition contributes in the sum (4.10) only
if it is evercrossing. In order to ﬁnd the leading term we need to ﬁnd all
non–crossing partitions of the set {1, 2, . . . , n }which are at the same time
evercrossing. This combination of adjectives sounds oxymo ronic which
suggests that there should not be too many of such partitions and indeed it
32 PIOTR ´SNIADY
is easy to check that the only such partition is the trivial one. Hence
RJM
n = Σ {{1}, {2},..., {n}}+ (terms of degree at most n − 2) =
Σ n− 1 + (terms of degree at most n − 2)
which ﬁnishes the proof of the case t = 1.
The general case follows easily from Corollary 3.8. □
Corollary 4.8. Elements (RJM
k )k≥2 are algebraically free; also elements
(MJM
k )k≥2 are algebraically free and therefore the gradation (2.6) is well–
deﬁned.
Proof. Let P(x2, x 3, . . . ) ⁄= 0 be a polynomial; our goal is to show that
P(RJM
2 , R JM
3 , . . . ) ∈ C(~S∞) is non–zero. In order to show this we express
P(RJM
2 , R JM
3 , . . . ) as a linear combination of conjugacy class indicators Σ
and Theorem 4.7 shows that the highest–order terms do not cancel.
In order to show that (MJM
k )k≥2 are algebraically free we consider a
polynomial Q(x2, x 3, . . . ) ⁄= 0. We apply (4.3) and obtain a polynomial
P(x2, x 3, . . . ) such that Q(MJM
2 , M JM
3 , . . . ) = P(RJM
2 , R JM
3 , . . . ). Equation
(4.2) implies that P(x2, x 3, . . . ) ⁄= 0. It follows that Q(MJM
2 , M JM
3 , . . . ) =
P(RJM
2 , R JM
3 , . . . ) ⁄= 0. □
The following result was proved in [Bia98, IO02].
Theorem 4.9. For every tuple k1, . . . , k t of positive integers there exists a
polynomial Kk1,...,k t (RJM
2 , R JM
3 , . . . ), called Kerov polynomial, such that
Σ k1 ,...,k t = Kk1,...,k t (RJM
2 , R JM
3 , . . . ).
In other words, each of the families (RJM
n )n≥2, (MJM
n )n≥2 and
(Σ k1,...,k m )k1,...,k m≥1 generates the same commutative algebra P.
With respect to the gradation (2.6) the leading term of the Kerov polyno-
mial is given by
(4.14) Σ k1 ,...,k t = RJM
k1 +1 · · · RJM
kt+1+
(terms of degree at most (k1 + 1) + · · · + (kt + 1) − 2)
and
deg Σ k1 ,...,k t = (k1 + 1) + · · · + (kt + 1).
In other words, the ﬁltration (2.8) is induced by gradation (2.6).
Proof. We shall prove this theorem by induction over(k1+1)+· · ·+(kt+1).
Let us express Σ k1 ,...,k t − RJM
k1 +1 · · · RJM
kt+1 as a linear combination of nor-
malized conjugacy class indicatorsΣ . Theorem 4.7 implies that with respect
to the ﬁltration (2.8) all these terms have degree at most (k1 + 1) + · · · +
(kt + 1) − 2 and hence the inductive hypothesis can be applied: every of
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 33
FIGURE 4.3. Partition from Figure 4.1 after the ﬁrst step of
the simpliﬁcation algorithm.
these terms can be expressed by the corresponding Kerov polynomial. Ob-
serve that from the very deﬁnition of free cumulants (4.2) it follows that
deg RJM
k1+1 · · ·RJM
kt+1 = (k1+ 1) +· · ·+ (kt + 1) with respect to the gradation
(2.6) and hence the theorem follows. □
