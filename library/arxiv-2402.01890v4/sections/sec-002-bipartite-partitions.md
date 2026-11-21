---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-002-bipartite-partitions
section_title: "Bipartite partitions"
section_number: null
pages: 3-6
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
and introduce the corresponding diagrammatic representations. For b ∈BiPark, we further recall the lexicographic
normal form N(b) and Garsia and Gessel’s normal form GG(b) from [23]. In section 4 we recall the partition algebra
Pk and introduce the spherical partition algebra SPk, the main protagonist of our paper. In section 5 we show that
rkC[x]SPk = bpk, by constructing a concrete basis for SPk. This uses diagrammatic arguments involving the normal
form N(b) from section 3. In section 6 we construct commuting actions of SPk(n) and CSn on SkVn and show
that they satisfy a double centralizer property. Motivated by a recent paper of Benkart, Halverson and Harman,
see [7], we find a direct sum decomposition of SkVn in terms of permutation modules for CSn, which allows us to
determine the dimension of the irreducible SPk(n)-modules Gk(λ) that appear in SkVn.
In section 7 we show that SPk is a cellular algebra, determine a basis for its cell modules and determine the
parametrizing poset for SPk. Using Garsia and Gessel’s normal form for bipartite partitions, we further construct
a Robinson-Schensted-Knuth type bijection for SPk. Finally, we show that SPk(t) is quasi-hereditary when t̸ = 0.
In section 8 we obtain the main Theorems involving the decomposition numbers for SPk(t) and finally, in section
9, we obtain the Loewy structure of the indecomposable projective modules and tilting modules.
Acknowledgements
The authors would like to express their gratitude to Stephen Griffeth and Luc Lapointe for insightful comments
on the results of the paper. They are especially grateful to Alexander Wilson for pointing out the connection to
the multiset partition algebra and for mentioning the references [40], [42] and [50]. Finally, they wish to express
their gratitude to the anonymous referee for indicating several research projects related to the present work and
for communicating detailed suggestions that helped them improve substantially the clarity and presentation of the
paper.
2
Basic notation
In this section we quickly fix the relevant notation concerning partitions, Young tableaux, and so on.
For k ∈N we let Park be the set of integer partitions of k, that is weakly decreasing positive integer sequences
λ = (λ1, λ2, . . . , λp) such that λ1+λ2+. . .+λp = k. The length of λ is defined to be ℓ(λ) = p and its order is defined
as |λ| = k. The set of partitions in Park of length less then or equal to l is denoted Par≤l
k
and the set of partitions
in Park of length equal to l is denoted Parl
k. Using the convention Par0 = ∅we define Par = S∞
k=0 Park and
Par≤l = S∞
k=0 Par≤l
k . We sometimes write λ ∈Park in the form λ = (λa1
1 , λa1
2 , . . . , λap
p ) where λ1 > λ1 > . . . > λp
and where ai is the multiplicity of λi in λ.
More generally, for k ∈N we let Compk be the set of compositions of k, that is positive integer sequences λ =
(λ1, λ2, . . . , λp) such that λ1 +λ2 +. . .+λp = k. For µ = (µ1, µ2, . . . , µp) ∈Compk and ν = (ν1, ν2, . . . , νq) ∈Compl
we define µ · ν = (µ1, µ2, . . . , µp, ν1, ν2, . . . , νq) ∈Compk+l. For µ = (µ1, µ2, . . . , µp) ∈Compk we let ord(µ) ∈Park
be the partition obtained from µ by reordering the µi’s.
We identify λ ∈Park, and more generally λ ∈Compk, with its Young diagram, for example
(5, 3, 2) =
,
(2, 3, 5) =
.
(2.1)
We use matrix convention to label the boxes, also called nodes, of λ. Thus, (1, 1), (1, 2), . . . , (1, λ1) are the nodes of
the first row of λ, etc. We write u ∈λ if u is a node of λ. For λ ∈Compk, a λ-tableau s is a filling of the nodes of λ
with the numbers {1, 2, . . . , k}, each number occurring exactly once. A λ-tableau s, is called row/column standard
if the numbers in each row/column are increasing from left to right/top to bottom, and is called standard if it is
both row and column standard. The set of all λ-tableaux is denoted Tab(λ) and the set of all standard λ-tableaux
is denoted Std(λ). For s ∈Tab(λ) we define shape(s) = λ. Below are examples of a row standard and a standard
λ-tableau, for λ = (5, 3, 2).
1
2
3
5
6
7
8
9
10
,
1
2
3
4
5
6
7
8
9
10
.
(2.2)
Suppose that λ ∈Compk. For s, t ∈Tab(λ) we write s ∼t if s can be obtained from t by permuting the numbers
within the rows of t. This defines an equivalence relation on Tab(λ). The equivalence classes under ∼are called
λ-tabloids and the tabloid represented by t is denoted {t}. We let {Tab(λ)} denote the set of λ-tabloids.
Let Sk be the symmetric group on {1, 2, . . . , k} and let λ ∈Park. Then there is a natural left Sk-action on
Tab(λ), with σ ∈Sk acting on the entries of s ∈Tab(λ). For example, if λ = (4, 3, 2) and σ = (1, 3, 2)(4, 6, 5) in
cycle notation, then
σ



1
2
3
4
5
6
7
8
9


=
1
2
3
4
5
6
7
8
9
.
(2.3)
Note that Tab(λ) ∼= Sk, where Sk acts on Sk via left multiplication. Note also that the left Sk-action on
Tab(λ) induces a left Sk-action on {Tab(λ)}. Let M(λ) be the free C-vector space on {Tab(λ)}. Then the left
Sk-action on {Tab(λ)} gives rise to a left CSk-module structure on M(λ). This is the permutation module for CSk.
We have
dim M(λ) =

k
λ1, λ2, . . . , λp

where

k
λ1, λ2, . . . , λp

is the multinomial coefficient.
(2.4)
The irreducible CSk-modules are the Specht modules {S(λ) | λ ∈Park}, see for example [26]. We have dim S(λ) =
Std(λ).
Let λ ∈Park and let µ = (µ1, µ2. . . . , µq) ∈Compk. Then a semistandard λ-tableau s of type µ is a filling of
the nodes of λ, with the number 1 occurring µ1 times, the number 2 occurring µ2 times and so on, such that the
numbers in each row of s are weakly increasing from left to right, whereas the numbers in each column of s are
strictly increasing from top to bottom. For example, if λ = (4, 3, 2) and µ = (3, 3, 3), the following are the two
possible semistandard λ-tableaux of type µ
1
1
1
2
3
2
2
3
3
,
1
1
1
2
3
2
2
3
3
.
(2.5)
The set of semistandard λ-tableaux of type µ is denoted SStd(λ, µ) and its cardinality |SStd(λ, µ)| is the Kostka
number Kλµ. For example, for λ = (4, 3, 2) and µ = (3, 3, 3) we have Kλµ = 2, as can be read off from (2.5).
Let [M(µ) : S(λ)] be the multiplicity of S(λ) in M(µ). Then we have that
[M(µ) : S(λ)] = Kλµ.
(2.6)
If ν = (ν1, . . . , νl) ∈Compk is obtained from µ = (µ1, . . . , µl) ∈Compk via νi = µσ(i) for some σ ∈Sl, then there
exists an isomorphism M(µ) ∼= M(ν) of CSk-modules. This is reflected in (2.6), since Kλµ = Kλν in that case.
4
3 BIPARTITE PARTITIONS

In this section we recall the notion of bipartite partitions and introduce the spherical partition algebra.

For k € N, we let BiPar; be the set of bipartite partitions of k. That is, BiPar; is the set of multisets
b = {[r1,y1], [v2, yol,---,[va; yal} of pairs [x;,y;] such that x; and y; are nonnegative integers, not both zero,

satisfying
a a
Soa = Sou Hk. (3.1)
i=l i=1
Let bp; be the cardinality of BiPar;. Then bp; = 2, since BiPar; consists of the multisets

{{1, U3. {[1, 0], (0, Hy}. (3.2)

Similarly, bp2 = 9, since BiPar2 consists of the multisets

{(2,2]}, {{1,0], (1,2)}, (2, U,
{[1, 0], [1,0], (0, 2]}, {1 1, [

We use the convention that bp) = 1. The sequence

0-2 {2.0} 0.1) 0. 3)

Ss
fay
—
“A
—
-
ra
fia
A
N
=
i
nN

(bpo, bp1, bpe, bps, bpa, bps, ...) = (1, 2, 9,31, 109, 339, ...) (3.4)
is A002774 in the OEIS.

Bipartite partitions in BiPar, are also known as vector partitions of [k,k]. Their history goes back to the work
of Macmahon, and their combinatorics have been studied for example in [3], [23] and [30].

For b = {[1, 91], [v2, y2],---, [as Ya]} € BiPar, we represent each part [2;,y;] of b via two parallel horizontal
lines of points, the top row containing x; points and the bottom row containing y; points, that are joined via a
propagating line from the leftmost top point to the leftmost bottom point, for example

(5,3)= Fr (3.5)

We represent 6 itself diagrammatically by concatenating the diagrams of the parts [x;,y;] from left to right, for
example for b = {[3, 1], [2,2], [3, 2], [0, 4], [2, 1]} we have

TABS a0

Note that since elements of BiPar; are multisets, this diagrammatic representation of b € BiPar;, is not unique,
since any permutation of the parts of b € BiPar, does not change b. For example we have

abies T= LS (3.7)

In order to remediate this nonuniqueness, we introduce for b € BiPar, the normal form N(b), using the ap-
propriate lexicographic order. To be precise, suppose that b = {[21,y:], (v2, y2],..-,[%a,Yal}- Then we define
N(b) = ([o(1)s Yo(1)], [2o(2)sYo(2)]+-+ +> (ola): Yo(a))) where o € G, is chosen such that if i > j then either
Lo(i) < Loy) OT (ois) = Loy) AN Yo(s) S Yo(j)). For example, we have

N({(1, 2], (2, 1], (4, 1), (0, 2], (0, 1]. (1,2), (1, 1), (3, 2)}) = ((4, 1, (3, 2], (2, 2), [2,2], [1,2], [11]. [0,2]. [0,1]). (3.8)
Using the normal form N(b), elements of BiPar; may be viewed as sequences of pairs [z;, y;] rather than multisets

of such pairs. For N(b) applied to 6 as in (3.6) we have

12 3 4 5 67 8 9 10
N(b) 6 C. (3.9)
Voy 3 4 5! 6 7 8! 9! 10°

In [23], Garsia and Gessel gave another characterization of BiPar,, that we shall need. Let \ = (Ai, A2,...,A1) €
Par, and o = (01,02,..., ,o1) € G be a symmetric group element written in permutation notation, by which we
mean that o; € {1,2,...,/} and that o maps i to 9; for all i. Then ) is said to be o-compatible if 4; = Ai41 implies
Oi < Oi41-

Suppose now that 6 = {[1, y:], [v2, y2],.-.,[%a,Ya]} € BiPar, and consider a diagrammatic representation for
b as in (3.6). Define \'?? as the partition obtained from the nonzero 2;’s via reordering, and define similarly \°.
Next reorder the top points and bottom points of the diagram in such a way that there are no crossings between
the propagating lines leaving parts of the same length in A!??, and similarly for \°?', and let GG(b) be the resulting
diagram. Define \'°??'° to be the partition extracted from \'°? by eliminating the parts with no propagating lines,
and define similarly \°?"?, Then '?P'° and PT? are partitions of the same length, say 1, and so we may
define o = (01,09,...,01) € G; by the condition that Apotpre is connected to Aipppre whereas Notpre is connected
to AepPPre | and so on. With this notation, Theorem 2.1 of [23] states that \°°4?"? is o-compatible whereas \'?:?"?
is o~!-compatible, and that BiPar; is characterised by these properties. In other words, the diagram GG(b) is
another normal form for b € BiPar,. For example, for b as in (3.6), we have

1 2

3 4
co) > SSS (3.10)
2 3°04

1

and so \!P-Prey = (3,3, 2,2), \bbProP = (2,2,1,1) and o = (1,3,2,4).

We define the propagating part of GG(b) to be the diagram obtained from GG(b) by removing all components
that are completely contained in the top line or in the bottom line of points. For example, for GG(b) as in (3.10),
the propagating part is

1 2 3 4
: a (3.11)
1 2 304 .
