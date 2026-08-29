---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-002-21-the-lattice-of-partitions
section_title: "The lattice of partitions"
section_number: 2.1
pages: 3-4
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
m < n , we denote by [ m, n] the interval of natural numbers between m
and n, i.e.,
[m, n] := {m, m + 1, m + 2, . . . , n− 1, n}
and [ m] = [1 , m]. For a matrix A = ( aij)N
i,j=1, we denote by Tr the
unnormalized and by tr the normalized trace,
Tr(A) :=
N∑
i=1
aii, tr(A) := 1
N Tr(A).
We say that A = {A1, . . . , Ak} is a partition of the set [1 , n] if the
subsets Ai are disjoint, non-empty, and their union is equal to [1 , n].
We call A1, . . . , Ak the blocks of the partition A. For a permutation
π ∈ Sn we say that a partition A is π-invariant if π leaves invariant each
block Ai. Let 1 n denote that partition of [ n] with one block and P(n)
denote the partitions of [ n]. Given positive integers m and n let 1 m,n
be the partition of [ m + n] with the two blocks: [ m] and [ m + 1, m + n].
If A = {A1, . . . , Ak} and B = {B1, . . . , Bl} are partitions of the same
set, we say that A ≤ B if for every block Ai there exists some block Bj
such that Ai ⊆ Bj. For a pair of partitions A, B we denote by A ∨ B
the smallest partition C such that A ≤ C and B ≤ C.
If we are considering classical random variables on a probability
space, then we denote by E the expectation with respect to the co r-
responding probability measure and by k r the corresponding classical
cumulants (as multi-linear functionals in r arguments); in particular,
k1(a) = E( a) and k 2(a1, a2) = E( a1a2) − E(a1)E(a2).
If a1, . . . , an are random variables and C = {C1, . . . , Ck} is in P(n)
we let
EC(a1, . . . , an) =
k∏
i=1
E
( ∏
j∈Ci
aj
)
4 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
On the lattice P(n) moments to cumulants are related by the M¨ obius
function: M¨ ob. In particular the nth cumulant k n is given by
kn(a1, . . . , ar) =
∑
C∈P(n)
M¨ ob(C, 1r)EC(a1, . . . , an)
where M¨ ob(C, 1n) = ( −1)k−1(k − 1)! and where k is the number of
blocks of C. We shall need the following formula for the second cumu-
lant of the product of random variables, see for example [L, 3.2].
(1) k 2(a1 · · · am, b1 · · · bn) =
∑
τ ∈P(m+n)
τ ∨1m,n=1n
kτ (a1, . . . am, b1, . . . , bn)
The sum is over all partitions of [ m + n] which have at least one block
which connects the two blocks of 1 m,n.
