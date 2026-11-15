---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules"
section_id: sec-001-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 3-7
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
toc_source: outline
doc_brief: "On the Gram determinants of the Specht modules — For every partition λ of a positive integer n, let Sλ be the corresponding Specht module of the symmetric group Sn, and let det(λ) ∈Z denote the Gram"
---
Preliminaries
We fix a positive integer n. A partition is a sequence λ = (a1, . . . , am) of non-negative
integers such that a1 ≥a2 ≥· · · ≥am. We identify partitions that only differ by a
string of zeros at the end. We say that λ is a partition of n if |λ| := a1+a2+· · ·+am =
n. We denote by Pn the set of partitions of n and by P := S∞
i=0 Pi the set of all
partitions. If µ = (c1, . . . , cl) is another partition of n, we write λ ⊴µ and say that λ
proceeds µ in the dominance (partial) order if and only if a1 +· · ·+ai ≤c1 +· · ·+ci
for all i ≥1. We denote
[λ] = {(i, j) | (i, j) ∈Z × Z, 1 ≤i ≤m, 1 ≤j ≤am}
to be the Young diagram of λ, which we can depict as a set of cells with a1 cells in
the first row, a2 cells in the second row, and so on, see Figure 1. For a cell c ∈[λ],
we denote the hook length hλ(c) to be the number of cells in the hook of c, i.e., the
number of cells below and to the right of c, including itself. The hook diagram of λ
is the Young diagram, where each cell is filled with its hook length.
9
8
7
5
3
2
1
5
4
3
1
3
2
1
Figure 1: Hook diagram of (7, 4, 3), with the hook of the cell c = (1, 2) colored gray.
Note that the entries of the first column of a hook diagram uniquely determine
the underlying partition. Generalizing that observation, a sequence of β-numbers
is a sequence β = (b1, . . . , bm) of non-negative integers such that all its entries
are distinct. For each such sequence, there is a unique σ ∈Sm such that β =
(bσ(1), . . . , bσ(m)) is a strictly decreasing sequence, i.e., bσ(1) > bσ(2) > · · · > bσ(m).
We define the partition
Part(β) := (bσ(1) −m + 1, bσ(2) −m + 2, . . . , bσ(m) −m + m)
3
and say that β is a sequence of β-numbers for Part(β).
Moreover, we say that
ℓ(β) := m is the length of β and define |β| := |Part(β)|.
Let B be the set of all sequences of β-numbers. We define the subsets
Bn := {β ∈B | |β| = n}
of the sequences of β-numbers of n and
B(λ) := {β ∈B | Part(β) = λ}
of the sequences of β-numbers for the partition λ.
Example 2.1. Let λ = (7, 4, 3) as in Figure 1. The first column of its hook diagram
consists of the sequence (9, 5, 3), so (9, 5, 3) is a sequence of β-numbers for λ. Further
sequences of β-numbers for λ include (10, 6, 4, 0), (11, 7, 5, 1, 0) and (1, 0, 6, 8, 12, 2).
Recall that there is a 1-to-1 correspondence between the partitions λ of a positive
integer n and the irreducible characters χλ of the symmetric group Sn. The following
well-known formula gives a convenient way to calculate the degree of each character.
Proposition 2.2. (cf. [7, Theorem 2.3.21]) Let λ be a partition of n. Then
fλ := χλ(1) =
n!
Q
c∈[λ] hλ(c).
We further set f(0) := 1. A partition is said to be odd (resp. even) if and only if fλ
is odd (resp. even).
We say that a partition λ is q-core for some positive integer q if there is no c ∈[λ]
such that q | hλ(c). There is a unique partition coreq(λ), which is q-core, that can
be constructed from [λ] by successively removing hooks of cells with hook lengths
a multiple of q, see also [7, Section 2.7].
This is where sequences of β-numbers
come into play; removing a hook from a Young diagram corresponds to subtracting
a multiple of a unit vector from a sequence of β-numbers for λ.
Example 2.3. Let λ = (7, 4, 3). Then λ is not 8-core, as hλ((1, 2)) = 8. Removing
the corresponding hook, we end up with core8(λ) = (3, 2, 1).
We shall need a criterion on the parity of fλ. Let r be the non-negative integer
such that 2r ≤n < 2r+1.
Lemma 2.4. (cf. [1, Lemma 1]) Let λ be a partition of n. There exists at most
one cell c ∈[λ] such that hλ(c) = 2r. Moreover, λ is odd if and only if such a cell
exists and core2r(λ) is odd.
4
Let ei = (0, 0, . . . , 0, 1, 0, . . . ) be the sequence that has a 1 in position i and 0
everywhere else.
Corollary 2.5. Let λ be a partition of n and let βλ ∈B(λ). Then there is at
most one index i such that βλ −2rei ∈Bn−2r. If such an index, say j, exists, then
βλ −2rej ∈B(core2r(λ)).
Definition 2.6. We define the function D : P →P such that for any partition λ of
n, we have D(λ) := core2r(λ). Moreover, we set D((0)) := (0). Denote D0(λ) := λ
and Dm(λ) := D(Dm−1(λ)) for any positive integer m. We define the oddness rank
of the partition λ by
OddRank(λ) = min{m ∈Z≥0 | Dm+1(λ) = Dm(λ)}.
Corollary 2.7. Let λ be a partition of n. Let n = Pr
i=0 ai2i for ai ∈{0, 1} be the
decomposition of n in binary. Then λ is odd if and only if OddRank(λ) = Pr
i=0 ai.
We now define a distance function for the set of partitions, where the distance
between two partitions is the minimum number of hooks that must be removed and
added to transform one Young diagram into the other.
Definition 2.8.
(i) Let m be a positive integer and let β = (b1, . . . , bm), β′ =
(b′
1, . . . , b′
m) ∈Zm. Let dm : Zm × Zm →Z≥0 be defined by
dm(β, β′) = #{i | 1 ≤i ≤m, bi̸ = b′
j for all 1 ≤j ≤m},
i.e., dm(β, β′) is the number of mismatches of β and β′.
(ii) Let λ, µ be partitions. We choose the positive integer m large enough such
that there are sequences of β-numbers βλ ∈B(λ), βµ ∈B(µ) such that
ℓ(βλ) = ℓ(βµ) = m. We define the distance d : P × P →Z≥0 by
d(λ, µ) := dm(βλ, βµ).
It is clear that the distance between two partitions is well-defined and that (P, d)
is a metric space. Note that for instance if λ is a partition of n with OddRank(λ) > 0,
then d(λ, D(λ)) = 1.
The following definition covers the odd branches of a partition, which are the
main objects we will work with in this paper.
Definition 2.9. Let λ be a partition of n.
(i) Let µ be another partition of n. We say that µ is a branch of λ if λ ⊴µ and
d(λ, µ) = 2. Let Pλ be the set of branches of λ.
5
(ii) Let µ be a branch of λ and let βλ ∈B(λ) (resp. βµ ∈B(µ)) with
βλ = (b1, b2, b3, . . . , bm), βµ = (b′
1, b′
2, b3, . . . , bm),
such that b1 > b2, b′
1 > b′
2. We define
h1
λ(µ) := b1 −b′
2 = b′
1 −b2, h2
λ(µ) := b2 −b′
2 = b′
1 −b1.
Note that there are two cells c1 = (k, j), c2 = (l, j) ∈[λ] with k < l such that
hλ(ci) = hi
λ(µ) for i = 1, 2. Also, (b1, b′
2, b3, . . . , bm) ∈B and the associated
partition corresponds to removing the hook of c2 from the Young diagram of
λ.
(iii) We define
Podd
λ
:= {µ ∈Pλ | µ is odd}
to be the set of odd branches of λ.
We are now ready to give the formula for the Gram determinant of a Specht
module:
Theorem 2.10. (cf. [6]) Let λ be a partition of n. The Gram determinant of the
canonical bilinear form with respect to the standard basis of the Specht module Sλ is
given by
det(λ) :=
Y
µ∈Pλ
h1
λ(µ)
h2
λ(µ)
εµfµ
∈Z,
where εµ ∈{−1, 1}. For any prime p, we define the integer a(p)
λ
such that
det(λ) = m · pa(p)
λ ,
where m is coprime to p.
Remark 2.11. We denote (Q×)2 := {x2 | x ∈Q×} to be the set of invertible rational
squares. Let λ be an even partition of n and let χλ be the character corresponding to
λ. The orthogonal determinant det(χλ) ∈Q×/(Q×)2 in the sense of [10] is defined
to be the rational square class of the Gram determinant of any ρ(Sn)-invariant,
non-degenerate, symmetric bilinear form of any rational representation ρ affording
the character χλ. The obvious choice is the canonical bilinear form for the Specht
module Sλ, and we arrive at
det(χλ) = det(λ) · (Q×)2 =
Y
µ∈Podd
λ
h1
λ(µ)
h2
λ(µ) · (Q×)2.
6
Example 2.12. Let λ = (2, 1(5)) and let µ = (3, 3, 1) be two partitions of 7. Clearly,
λ ⊴µ in the dominance order.
We choose βλ := (7, 5, 4, 3, 2, 1) and βµ = (8, 7, 4, 2, 1, 0) for the sequences of
β-numbers for λ and µ, respectively. Comparing the two sequences, we see that
there are two mismatches, so d(λ, µ) = d6(βλ, βµ) = 2. So µ is in fact a branch of λ;
we calculate that h1
λ(µ) = 5 and h2
λ(µ) = 3.
It is easily seen that µ is odd; indeed, D(µ) = (3) and f(3) = 1, so the oddness
follows by Lemma 2.4.
In particular, µ is an odd branch of λ.
With the same
reasoning we see that λ is even, since D(λ) = (2, 1) and (2, 1) is 2-core.
We further observe that Podd
λ
= {µ, (7), (5, 1, 1), (3, 1(4))} and thus arrive at
det(χλ) = 5
3 · 7
5 · 7
3 · 7
1 · (Q×)2 = 7 · (Q×)2.
7
1
5
4
3
2
1
5
3
2
4
2
1
1
Figure 2: Hook diagrams of (2, 1(5)) and (3, 3, 1).
