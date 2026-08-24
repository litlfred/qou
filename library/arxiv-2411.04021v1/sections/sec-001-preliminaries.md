---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules"
section_id: sec-001-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 3-7
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
doc_brief: "On the Gram determinants of the Specht modules — For every partitionλ of a positive integern, letSλ be the corresponding Specht module of the symmetric group Sn, and let det(λ)∈ Z denote the Gram"
---
Wefixapositiveinteger n. Apartition isasequence λ = (a1,...,a m)ofnon-negative
integers such thata1≥a2≥···≥ am. We identify partitions that only differ by a
stringofzerosattheend. Wesaythat λisapartitionof nif|λ| :=a1+a2+··· +am =
n. We denote byPn the set of partitions ofn and by P :=S∞
i=0 Pi the set of all
partitions. Ifµ = (c1,...,c l) is another partition ofn, we writeλ ⊴µ and say thatλ
proceedsµ in thedominance (partial) orderif and only ifa1 +··· +ai≤c1 +··· +ci
for alli≥ 1. We denote
[λ] ={(i,j )| (i,j )∈ Z× Z, 1≤i≤m, 1≤j≤am}
to be theYoung diagramof λ, which we can depict as a set of cells witha1 cells in
the first row,a2 cells in the second row, and so on, see Figure 1. For a cellc∈ [λ],
we denote thehook lengthhλ(c) to be the number of cells in thehook of c, i.e., the
number of cells below and to the right ofc, including itself. Thehook diagramof λ
is the Young diagram, where each cell is filled with its hook length.
9 8 7 5 3 2 1
5 4 3 1
3 2 1
Figure 1: Hook diagram of(7, 4, 3), with the hook of the cellc = (1, 2) colored gray.
Note that the entries of the first column of a hook diagram uniquely determine
the underlying partition. Generalizing that observation, asequence ofβ-numbers
is a sequence β = ( b1,...,b m) of non-negative integers such that all its entries
are distinct. For each such sequence, there is a uniqueσ ∈ Sm such that β =
(bσ(1),...,b σ(m)) is a strictly decreasing sequence, i.e.,bσ(1) > bσ(2) >··· > bσ(m).
We define the partition
Part(β) := (bσ(1)−m + 1,bσ(2)−m + 2,...,b σ(m)−m +m)
3
and say that β is a sequence of β-numbers for Part(β). Moreover, we say that
ℓ(β) :=m is the length ofβ and define|β| :=|Part(β)|.
Let B be the set of all sequences ofβ-numbers. We define the subsets
Bn :={β∈ B||β| =n}
of the sequences ofβ-numbers ofn and
B(λ) :={β∈ B| Part(β) = λ}
of the sequences ofβ-numbers for the partitionλ.
Example 2.1.Letλ = (7, 4, 3) as in Figure 1. The first column of its hook diagram
consists of the sequence(9, 5, 3), so(9, 5, 3) is a sequence ofβ-numbers forλ. Further
sequences ofβ-numbers forλ include (10, 6, 4, 0), (11, 7, 5, 1, 0) and (1, 0, 6, 8, 12, 2).
Recall that there is a 1-to-1 correspondence between the partitionsλ of a positive
integernandtheirreduciblecharacters χλ ofthesymmetricgroup Sn. Thefollowing
well-known formula gives a convenient way to calculate the degree of each character.
Proposition 2.2. (cf. [7, Theorem 2.3.21]) Letλ be a partition ofn. Then
fλ :=χλ(1) = n!Q
c∈[λ]hλ(c).
We further setf(0) := 1. A partition is said to be odd (resp. even) if and only iffλ
is odd (resp. even).
We say that a partitionλ isq-corefor some positive integerq if there is noc∈ [λ]
such thatq| hλ(c). There is a unique partitioncoreq(λ), which isq-core, that can
be constructed from [λ] by successively removing hooks of cells with hook lengths
a multiple of q, see also [7, Section 2.7]. This is where sequences of β-numbers
come into play; removing a hook from a Young diagram corresponds to subtracting
a multiple of a unit vector from a sequence ofβ-numbers forλ.
Example 2.3.Let λ = (7, 4, 3). Thenλ is not 8-core, ashλ((1, 2)) = 8. Removing
the corresponding hook, we end up withcore8(λ) = (3, 2, 1).
We shall need a criterion on the parity offλ. Letr be the non-negative integer
such that 2r≤n< 2r+1.
Lemma 2.4. (cf. [1, Lemma 1]) Letλ be a partition ofn. There exists at most
one cellc∈ [λ] such thathλ(c) = 2 r. Moreover, λ is odd if and only if such a cell
exists and core2r(λ) is odd.
4
Let ei = (0, 0,..., 0, 1, 0,... ) be the sequence that has a1 in position i and 0
everywhere else.
Corollary 2.5. Let λ be a partition ofn and let βλ ∈ B(λ). Then there is at
most one indexi such thatβλ− 2rei∈ Bn−2r. If such an index, sayj, exists, then
βλ− 2rej∈ B(core2r(λ)).
Definition 2.6.We define the functionD : P→ P such that for any partitionλ of
n, we haveD(λ) := core 2r(λ). Moreover, we setD((0)) := (0). Denote D0(λ) := λ
and Dm(λ) := D(Dm−1(λ)) for any positive integerm. We define theoddness rank
of the partitionλ by
OddRank(λ) = min{m∈ Z≥0|Dm+1(λ) = Dm(λ)}.
Corollary 2.7. Let λ be a partition ofn. Let n =Pr
i=0ai2i for ai∈{ 0, 1} be the
decomposition ofn in binary. Thenλ is odd if and only ifOddRank(λ) =Pr
i=0ai.
We now define a distance function for the set of partitions, where the distance
between two partitions is the minimum number of hooks that must be removed and
added to transform one Young diagram into the other.
Definition 2.8. (i) Let m be a positive integer and letβ = (b1,...,b m),β′ =
(b′
1,...,b ′
m)∈ Zm. Letdm : Zm× Zm→ Z≥0 be defined by
dm(β,β′) = #{i| 1≤i≤m, bi̸=b′
j for all 1≤j≤m},
i.e., dm(β,β′) is the number of mismatches ofβ and β′.
(ii) Let λ,µ be partitions. We choose the positive integerm large enough such
that there are sequences of β-numbers βλ ∈ B(λ), βµ ∈ B(µ) such that
ℓ(βλ) = ℓ(βµ) = m. We define the distanced : P× P→ Z≥0 by
d(λ,µ ) := dm(βλ,βµ).
It is clear that the distance between two partitions is well-defined and that(P,d )
isametricspace. Notethatforinstanceif λisapartitionof nwith OddRank(λ)> 0,
then d(λ,D (λ)) = 1.
The following definition covers theodd branches of a partition, which are the
main objects we will work with in this paper.
Definition 2.9.Let λ be a partition ofn.
(i) Let µ be another partition ofn. We say thatµ is a branch ofλ if λ ⊴µ and
d(λ,µ ) = 2. Let Pλ be the set of branches ofλ.
5
(ii) Let µ be a branch ofλ and letβλ∈ B(λ) (resp. βµ∈ B(µ)) with
βλ = (b1,b 2,b 3,...,b m), βµ = (b′
1,b′
2,b 3,...,b m),
such thatb1 >b 2, b′
1 >b′
2. We define
h1
λ(µ) := b1−b′
2 =b′
1−b2, h2
λ(µ) := b2−b′
2 =b′
1−b1.
Note that there are two cellsc1 = (k,j ),c 2 = (l,j )∈ [λ] with k <l such that
hλ(ci) = hi
λ(µ) for i = 1, 2. Also, (b1,b′
2,b 3,...,b m)∈ B and the associated
partition corresponds to removing the hook ofc2 from the Young diagram of
λ.
(iii) We define
P odd
λ :={µ∈ Pλ|µ is odd}
to be the set of odd branches ofλ.
We are now ready to give the formula for the Gram determinant of a Specht
module:
Theorem 2.10. (cf. [6]) Letλ be a partition ofn. The Gram determinant of the
canonical bilinear form with respect to the standard basis of the Specht moduleSλ is
given by
det(λ) :=
Y
µ∈Pλ
h1
λ(µ)
h2
λ(µ)
εµfµ
∈ Z,
whereεµ∈{− 1, 1}. For any primep, we define the integera(p)
λ such that
det(λ) = m·pa(p)
λ ,
wherem is coprime top.
Remark2.11. Wedenote (Q×)2 :={x2|x∈ Q×}tobethesetofinvertiblerational
squares. Letλ be an even partition ofn and letχλ be the character corresponding to
λ. The orthogonal determinantdet(χλ)∈ Q×/(Q×)2 in the sense of [10] is defined
to be the rational square class of the Gram determinant of anyρ(Sn)-invariant,
non-degenerate, symmetric bilinear form of any rational representationρ affording
the characterχλ. The obvious choice is the canonical bilinear form for the Specht
module Sλ, and we arrive at
det(χλ) = det(λ)· (Q×)2 =
Y
µ∈P odd
λ
h1
λ(µ)
h2
λ(µ)· (Q×)2.
6
Example 2.12.Letλ = (2, 1(5)) and letµ = (3, 3, 1) be two partitions of7. Clearly,
λ ⊴µ in the dominance order.
We chooseβλ := (7, 5, 4, 3, 2, 1) and βµ = (8, 7, 4, 2, 1, 0) for the sequences of
β-numbers for λ and µ, respectively. Comparing the two sequences, we see that
there are two mismatches, sod(λ,µ ) = d6(βλ,βµ) = 2. Soµ is in fact a branch ofλ;
we calculate thath1
λ(µ) = 5 and h2
λ(µ) = 3.
It is easily seen thatµ is odd; indeed,D(µ) = (3) and f(3) = 1, so the oddness
follows by Lemma 2.4. In particular, µ is an odd branch ofλ. With the same
reasoning we see thatλ is even, sinceD(λ) = (2, 1) and (2, 1) is 2-core.
We further observe thatP odd
λ ={µ, (7), (5, 1, 1), (3, 1(4))} and thus arrive at
det(χλ) = 5
3· 7
5· 7
3· 7
1· (Q×)2 = 7· (Q×)2.
7 1
5
4
3
2
1
5 3 2
4 2 1
1
Figure 2: Hook diagrams of(2, 1(5)) and (3, 3, 1).
