---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-014-combinatorics-of-partitions-and-multipartitions
section_title: "Combinatorics of partitions and multipartitions"
section_number: null
pages: 32-34
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
Let l and n be positive integers.
4.1.1 Partitions
A partitionλ = (λ1,...,λ h) is a family of positive integers such that λ1>λ2>... >λh> 1. We call
h the length or height of the partition λ. We write |λ| :=∑h
i=1λi and we say that λ is a partition of n
29
if n =|λ|. We denote by P(n) the set of partitions of n. To each partition λ we associate its β-number,
βλ = (β1,β 2,...,β h), deﬁned by
β1 :=h +λ1− 1,β 2 :=h +λ2− 2,...,β h :=h +λh−h =λh.
Note that β1 >β 2 >··· >β h> 1.
We deﬁne the set of nodes [λ] of λ to be the set
[λ] :={(i,j )| 1⩽i⩽h, 1⩽j⩽λi}.
We identify partitions with their Young diagrams: the Young diagram of λ is a left-justiﬁed array of h
rows such that the i-th row contains λi boxes (nodes) for all i = 1,...,h .
The conjugate partition λ′ = (λ′
1,...,λ ′
h′) of λ is deﬁned by λ′
j := #{i| 1⩽i⩽h such that λi>j}.
We haveh′ =λ1. The Young diagram ofλ′ is the transpose of the Young diagram ofλ. A node (i,j )∈ [λ]
if and only if (j,i )∈ [λ′].
If x = (i,j )∈ [λ] and µ is another partition, we deﬁne the generalised hook length of x with respect
to (λ, µ) to be the integer:
hλ,µ
i,j :=λi−i +µ′
j−j + 1.
Forµ =λ, the above formula becomes the classical hook length formula (giving the length of the hook
of λ that x belongs to). Moreover, we deﬁne the content of x to be the diﬀerence j−i.
Finally, we set
N(λ) :=
h∑
i=1
(i− 1)λi = 1
2
h′
∑
i=1
(λ′
i− 1)λ′
i =
h′
∑
i=1
( λ′
i
2
)
.
4.1.2 Multipartitions
An l-partition (or multipartition) of n is an ordered l-tuple λ = (λ(0),λ (1),...,λ (l−1)) of partitions such
that|λ| :=∑l−1
i=0|λ(i)| =n. We denote byP(l,n ) the set of l-partitions of n. The empty multipartition,
denoted by ∅, is an l-tuple of empty partitions. If λ = (λ(0),λ (1),...,λ (l−1))∈P (l,n ), we denote by λ′
the l-partition (λ(0)′
,λ (1)′
,...,λ (l−1)′
). For i = 0, 1,...,l − 1, we denote by h(i) and β(i) the height and
β-number of λ(i) respectively. Finally, we denote by ¯λ the simple partition of n obtained by writing in
decreasing order all the entries of λ (that is, all the elements of the multiset λ(0)∪λ(1)∪... ∪λ(l−1)).
Example 4.1 Let us take l = 2, n = 6 and λ = ((2, 1), (3)). We have λ′ = ((2, 1), (1, 1, 1)) and
¯λ = (3, 2, 1).
If β = (β1,β 2,...,β h) is a sequence of positive integers such that β1 > β2 >··· > βh and m is a
positive rational number, then the m-shifted of β is the sequence of numbers deﬁned by
β[m] = (β1 +m,β 2 +m,...,β h +m,m− 1,m− 2,...,m − [m] + 1,m− [m]),
where [m] denotes the integer part of m.
From now on, we suppose that we have a given weight system m := (m0,m 1,...,m l−1)∈ Ql. We
deﬁne the (l, m)-charged height of λ to be the family (hc(0),hc (1),...,hc (l−1)), where
hc(0) :=h(0)−m0,hc (1) :=h(1)−m1,...,hc (l−1) :=h(l−1)−ml−1,
and the m-charged height of λ to be the integer
hcλ := max
0⩽i⩽l−1
hc(i).
Fori = 0, 1,...,l − 1 , we set
Bc(i)
λ :=β(i)[hcλ−hc(i)].
We then have
Bc(i)
λ = (bc(i)
j )1⩽j⩽hcλ+[mi] where bc(i)
j =β(i)
j +hcλ−hc(i) =λ(i)
j −j +hcλ +mi
30
(taking β(i)
j =λ(i)
j = 0 for j >h(i)).
The m-charged standard symbol of λ is the family of numbers deﬁned by
Bcλ = (Bc(0)
λ ,Bc (1)
λ ,...,Bc (l−1)
λ ).
It is a tableau of numbers arranged into l rows indexed by the set{0, 1,...,l − 1} such that the i-th row
has length equal to hcλ + [mi]. In general, an m-charged symbol of λ is a family of numbers obtained
from the m-charged standard symbol of λ by shifting all the rows by the same positive rational number.
The m-charged content of λ is the multiset
Contcλ =Bc(0)
λ ∪Bc(1)
λ ∪... ∪Bc(l−1)
λ .
Example 4.2 Let us take l = 2, n = 6, λ = ((2, 1), (3)) and m = (−1, 2). Then
Bcλ =
( 3 1
7 3 2 1 0
)
We have Contcλ ={7, 3, 3, 2, 1, 1, 0}.
Let s∈ Z with s>hcλ. Let Bcs
λ be the m-charged symbol of λ obtained from Bcλ by shifting all
the rows by s−hcλ. Let κ1> κ2>··· > κt, with t = ls +∑l−1
i=0[mi], be the elements of the multiset
Bcs
λ written in decreasing order (if s =hcλ, these are simply the elements of Contc λ). We set
nm(λ) :=
t∑
i=1
(i− 1)κi.
Let r∈ Z>0, By [GeJa2, Proposition 5.5.11], the following element of Q does not depend on the choice
of the integer s:
a(m,r)(λ) :=r (nm(λ)−nm(∅)). (4.3)
We will see in the next section that a(m,r) corresponds to the a-function of an Ariki–Koike algebra.
