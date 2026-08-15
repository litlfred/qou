---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-002-bipartite-partitions
section_title: "Bipartite partitions"
section_number: null
pages: 3-6
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
doc_brief: "On the spherical partition algebra — For k ∈ N we introduce an idempotent subalgebra, the spherical partition algebra SP k, of the partition algebra Pk, that we define using an embedding associated"
---
and introduce the corresponding diagrammatic representations. For b∈ BiPark, we further recall the lexicographic
normal form N(b) and Garsia and Gessel’s normal formGG(b) from [23]. In section 4 we recall the partition algebra
Pk and introduce the spherical partition algebraSPk, the main protagonist of our paper. In section 5 we show that
rkC[x]SPk =bpk, by constructing a concrete basis forSPk. This uses diagrammatic arguments involving the normal
form N(b) from section 3. In section 6 we construct commuting actions of SPk(n) and CSn on SkVn and show
that they satisfy a double centralizer property. Motivated by a recent paper of Benkart, Halverson and Harman,
see [7], we find a direct sum decomposition of SkVn in terms of permutation modules for CSn, which allows us to
determine the dimension of the irreducible SPk(n)-modules Gk(λ) that appear in SkVn.
In section 7 we show that SPk is a cellular algebra, determine a basis for its cell modules and determine the
parametrizing poset forSPk. Using Garsia and Gessel’s normal form for bipartite partitions, we further construct
a Robinson-Schensted-Knuth type bijection forSPk. Finally, we show thatSPk(t) is quasi-hereditary when t̸= 0.
In section 8 we obtain the main Theorems involving the decomposition numbers forSPk(t) and finally, in section
9, we obtain the Loewy structure of the indecomposable projective modules and tilting modules.
Acknowledgements
The authors would like to express their gratitude to Stephen Griffeth and Luc Lapointe for insightful comments
on the results of the paper. They are especially grateful to Alexander Wilson for pointing out the connection to
the multiset partition algebra and for mentioning the references [40], [42] and [50]. Finally, they wish to express
their gratitude to the anonymous referee for indicating several research projects related to the present work and
for communicating detailed suggestions that helped them improve substantially the clarity and presentation of the
paper.
2 Basic notation
In this section we quickly fix the relevant notation concerning partitions, Young tableaux, and so on.
Fork∈ N we let Park be the set of integer partitions of k, that is weakly decreasing positive integer sequences
λ = (λ1,λ 2,...,λ p) such thatλ1+λ2+... +λp =k. The length of λ is defined to beℓ(λ) =p and its order is defined
as|λ| =k. The set of partitions in Par k of length less then or equal to l is denoted Par≤l
k and the set of partitions
in Park of length equal to l is denoted Par l
k. Using the convention Par 0 =∅ we define Par = S∞
k=0 Park and
Par≤l =S∞
k=0 Par≤l
k . We sometimes write λ∈ Park in the form λ = (λa1
1 ,λa1
2 ,...,λ ap
p ) where λ1 > λ1 > ... > λp
and where ai is the multiplicity of λi in λ.
More generally, for k∈ N we let Compk be the set of compositions of k, that is positive integer sequences λ =
(λ1,λ 2,...,λ p) such thatλ1 +λ2 +... +λp =k. For µ = (µ1,µ 2,...,µ p)∈ Compk andν = (ν1,ν 2,...,ν q)∈ Compl
we define µ·ν = (µ1,µ 2,...,µ p,ν 1,ν 2,...,ν q)∈ Compk+l. For µ = (µ1,µ 2,...,µ p)∈ Compk we let ord(µ)∈ Park
be the partition obtained from µ by reordering the µi’s.
3
We identifyλ∈ Park, and more generally λ∈ Compk, with its Young diagram, for example
(5, 3, 2) =
,
(2, 3, 5) =
.
(2.1)
We use matrix convention to label the boxes, also called nodes, of λ. Thus, (1, 1), (1, 2),..., (1,λ 1) are the nodes of
the first row of λ, etc. We write u∈λ ifu is a node of λ. For λ∈ Compk, a λ-tableau s is a filling of the nodes of λ
with the numbers{1, 2,...,k }, each number occurring exactly once. A λ-tableau s, is called row/column standard
if the numbers in each row/column are increasing from left to right/top to bottom, and is called standard if it is
both row and column standard. The set of all λ-tableaux is denoted Tab(λ) and the set of all standard λ-tableaux
is denoted Std(λ). For s∈ Tab(λ) we define shape( s) = λ. Below are examples of a row standard and a standard
λ-tableau, for λ = (5, 3, 2).
1
2
3
4
5
6
7
8 9 10
,
1
2
3
4
5
6
7
8
9 10 .
(2.2)
Suppose thatλ∈ Compk. For s, t∈ Tab(λ) we write s∼ t if s can be obtained from t by permuting the numbers
within the rows of t. This defines an equivalence relation on Tab( λ). The equivalence classes under ∼ are called
λ-tabloids and the tabloid represented by t is denoted{t}. We let{Tab(λ)} denote the set of λ-tabloids.
Let Sk be the symmetric group on {1, 2,...,k } and let λ∈ Park. Then there is a natural left Sk-action on
Tab(λ), with σ∈ Sk acting on the entries of s∈ Tab(λ). For example, if λ = (4, 3, 2) and σ = (1, 3, 2)(4, 6, 5) in
cycle notation, then
σ


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
 =
1
23
4
5
6 7
8
9
.
(2.3)
Note that Tab(λ)∼= Sk, where Sk acts on Sk via left multiplication. Note also that the left Sk-action on
Tab(λ) induces a left Sk-action on {Tab(λ)}. Let M(λ) be the free C-vector space on {Tab(λ)}. Then the left
Sk-action on{Tab(λ)} gives rise to a left CSk-module structure onM(λ). This is the permutation module for CSk.
We have
dimM(λ) =
 k
λ1,λ 2,...,λ p

where
 k
λ1,λ 2,...,λ p

is the multinomial coefficient. (2.4)
The irreducible CSk-modules are the Specht modules{S(λ)|λ∈ Park}, see for example [26]. We have dimS(λ) =
Std(λ).
Let λ∈ Park and let µ = (µ1,µ 2....,µ q)∈ Compk. Then a semistandard λ-tableau s of type µ is a filling of
the nodes of λ, with the number 1 occurring µ1 times, the number 2 occurring µ2 times and so on, such that the
numbers in each row of s are weakly increasing from left to right, whereas the numbers in each column of s are
strictly increasing from top to bottom. For example, if λ = (4, 3, 2) and µ = (3, 3, 3), the following are the two
possible semistandard λ-tableaux of type µ
1 1 1
2 32
2
3 3
,
1 1 1
2
3
2 2
3 3 .
(2.5)
The set of semistandard λ-tableaux of type µ is denoted SStd(λ,µ ) and its cardinality |SStd(λ,µ )| is the Kostka
numberKλµ. For example, for λ = (4, 3, 2) and µ = (3, 3, 3) we have Kλµ = 2, as can be read off from (2.5).
Let [M(µ) :S(λ)] be the multiplicity of S(λ) in M(µ). Then we have that
[M(µ) :S(λ)] =Kλµ. (2.6)
If ν = (ν1,...,ν l)∈ Compk is obtained from µ = (µ1,...,µ l)∈ Compk via νi =µσ(i) for some σ∈ Sl, then there
exists an isomorphism M(µ)∼=M(ν) of CSk-modules. This is reflected in (2.6), since Kλµ =Kλν in that case.
4
3 Bipartite partitions
In this section we recall the notion of bipartite partitions and introduce the spherical partition algebra.
For k ∈ N, we let BiPar k be the set of bipartite partitions of k. That is, BiPar k is the set of multisets
b = {[x1,y 1], [x2,y 2],..., [xa,ya]} of pairs [ xi,yi] such that xi and yi are nonnegative integers, not both zero,
satisfying
aX
i=1
xi =
aX
i=1
yi =k. (3.1)
Let bpk be the cardinality of BiPark. Then bp1 = 2, since BiPar1 consists of the multisets
{[1, 1]},{[1, 0], [0, 1]}. (3.2)
Similarly,bp2 = 9, since BiPar2 consists of the multisets
{[2, 2]},{[1, 0], [1, 2]},{[2, 1], [0, 1]},{[1, 1], [1, 1]},{[2, 0], [0, 2]},{[2, 0], [0, 1], [0, 1]}
{[1, 0], [1, 0], [0, 2]},{[1, 1], [1, 0], [0, 1]},{[1, 0], [1, 0], [0, 1], [0, 1]}. (3.3)
We use the convention that bp0 = 1. The sequence
(bp0,bp 1,bp 2,bp 3,bp 4,bp 5,... ) = (1, 2, 9, 31, 109, 339,... ) (3.4)
is A002774 in the OEIS.
Bipartite partitions in BiPark are also known as vector partitions of [k,k ]. Their history goes back to the work
of Macmahon, and their combinatorics have been studied for example in [3], [23] and [30].
Forb ={[x1,y 1], [x2,y 2],..., [xa,ya]}∈ BiPark we represent each part [ xi,yi] of b via two parallel horizontal
lines of points, the top row containing xi points and the bottom row containing yi points, that are joined via a
propagating line from the leftmost top point to the leftmost bottom point, for example
[5, 3] =
/Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet . (3.5)
We represent b itself diagrammatically by concatenating the diagrams of the parts [ xi,yi] from left to right, for
example for b ={[3, 1], [2, 2], [3, 2], [0, 4], [2, 1]} we have
b7→
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet . (3.6)
Note that since elements of BiPar k are multisets, this diagrammatic representation of b∈ BiPark is not unique,
since any permutation of the parts of b∈ BiPark does not change b. For example we have
{[2, 1], [1, 2]}7→
/Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet
/Bullet/Bullet/Bullet
/Bullet/Bullet/Bullet
= . (3.7)
In order to remediate this nonuniqueness, we introduce for b ∈ BiPark the normal form N(b), using the ap-
propriate lexicographic order. To be precise, suppose that b = {[x1,y 1], [x2,y 2],..., [xa,ya]}. Then we define
N(b) =
 
[xσ(1),yσ(1)], [xσ(2),yσ(2)],..., [xσ(a),yσ(a)]

where σ ∈ Sa is chosen such that if i ≥ j then either
xσ(i) <x σ(j) or (xσ(i) =xσ(j) and yσ(i)≤yσ(j)). For example, we have
N
 
{[1, 2], [2, 1], [4, 1], [0, 2], [0, 1], [1, 2], [1, 1], [3, 2]}

=
 
[4, 1], [3, 2], [2, 1], [1, 2], [1, 2], [1, 1], [0, 2], [0, 1]

. (3.8)
Using the normal form N(b), elements of BiPark may be viewed as sequences of pairs [ xi,yi] rather than multisets
of such pairs. For N(b) applied to b as in (3.6) we have
N(b)7→
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1
1′
2
2′
3
3′ 4′ 5′ 6′ 7′ 8′ 9′ 10′
4 5 6 7 8 9 10 . (3.9)
In [23], Garsia and Gessel gave another characterization of BiPark, that we shall need. Let λ = (λ1,λ 2,...,λ l)∈
Park and σ = (σ1,σ 2,...,σ l)∈ Sl be a symmetric group element written in permutation notation, by which we
5
mean that σi∈{ 1, 2,...,l } and that σ mapsi toσi for all i. Then λ is said to be σ-compatible ifλi =λi+1 implies
σi <σ i+1.
Suppose now that b ={[x1,y 1], [x2,y 2],..., [xa,ya]}∈ BiPark and consider a diagrammatic representation for
b as in (3.6). Define λtop as the partition obtained from the nonzero xi’s via reordering, and define similarly λbot.
Next reorder the top points and bottom points of the diagram in such a way that there are no crossings between
the propagating lines leaving parts of the same length in λtop, and similarly for λbot, and let GG(b) be the resulting
diagram. Define λtop,pro to be the partition extracted from λtop by eliminating the parts with no propagating lines,
and define similarly λbot,pro. Then λtop,pro and λbot,pro are partitions of the same length, say l, and so we may
defineσ = (σ1,σ 2,...,σ l)∈ Sl by the condition that λbot,pro
1 is connected to λtop,pro
σ1 , whereas λbot,pro
2 is connected
to λtop,pro
σ2 , and so on. With this notation, Theorem 2.1 of [23] states that λbot,pro is σ-compatible whereas λtop,pro
is σ−1-compatible, and that BiPar k is characterised by these properties. In other words, the diagram GG(b) is
another normal form for b∈ BiPark. For example, for b as in (3.6), we have
GG(b)7→
/Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet
/Bullet /Bullet
1 2 3 4
1 2 3 4 (3.10)
and so λtop,prop = (3, 3, 2, 2), λbot,prop = (2, 2, 1, 1) and σ = (1, 3, 2, 4).
We define the propagating part of GG(b) to be the diagram obtained from GG(b) by removing all components
that are completely contained in the top line or in the bottom line of points. For example, for GG(b) as in (3.10),
the propagating part is
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet
/Bullet /Bullet
1 2 3 4
1 2 3 4
.
(3.11)
