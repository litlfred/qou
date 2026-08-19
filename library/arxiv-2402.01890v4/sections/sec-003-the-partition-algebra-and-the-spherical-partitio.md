---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-003-the-partition-algebra-and-the-spherical-partitio
section_title: "The partition algebra and the spherical partition algebra"
section_number: null
pages: 6-7
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
doc_brief: "On the spherical partition algebra — For k ∈ N we introduce an idempotent subalgebra, the spherical partition algebra SP k, of the partition algebra Pk, that we define using an embedding associated"
---
We next recall the partition algebra Pk; it was introduced by the second named author via considerations in
statistical mechanics, see [32]. Let SetPar k be the set of set partitions on {1, 2...,k }, that is the set of equivalence
relationsd on{1, 2...,k }. For even subscript 2k we shall usually think of SetPar2k as set partitions on{1, 2...,k }∪
{1′, 2′...,k ′}. If d∈ SetPark we write d ={d1,d 2,...,d a} where the di’s are the classes, or blocks, of d. If
furthermore d∈ SetPar2k, we represent d diagrammatically using two parallel horizontal lines of points, just as for
elements of BiPark, but this time labeling the top points{1, 2,...,k } and the bottom points{1′, 2′,...,k ′}, from left
to right. We draw lines between these points in such a way that the connected components, in the graph-theoretic
sense, of the corresponding graph are exactly the blocks of d, for example
{{1},{2, 3, 7, 8, 9, 6′, 7′, 8′},{4, 5, 6, 1′, 2′},{3′, 4′, 5′},{9′}}7→
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2 3 4 5 6 7 8 9
1′ 2′ 3′ 4′ 5′ 6′ 7′ 8′ 9′ . (4.1)
Note that, just as for elements of BiPar k, this diagrammatic representation of d∈ SetPar2k is not unique.
For d ={d1,d 2,...,d a}∈ SetPar2k, we say that a block di is propagating if di∩{ 1, 2,...,k }̸ =∅ and di∩
{1′, 2′,...,k ′}̸ =∅. If di∩{ 1, 2,...,k }̸ =∅ we say that di∩{ 1, 2,...,k } is an intersection top block for d and if
di∩{ 1′, 2′,...,k ′}̸ =∅ we say that di∩{ 1′, 2′,...,k ′} is an intersection bottom block for d.
We definePk as the C[x]-algebra that, as a C[x]-module, is free on SetPar2k, and that has multiplication defined
as follows. For elements d,d 1∈ SetPar2k, let d◦1d1 be the concatenation of d and d1 with d on top of d1. There
may be one or several ‘internal’ connected components ofd◦1d1, that is components that do not intersect any of the
top or bottom points of d◦1d1. Let d◦2d1 be the diagram obtained from d◦1d1 by removing theseN, say, internal
components. There may still one or several ‘internal points’ of d◦2d1, that is points that are neither top or bottom
points of d◦2d1, and we let d◦3d1 be the diagram obtained from d◦2d1 by eliminating these points. We may now
viewd◦3d1 as the diagram of a set partition and the product in Pk ofd andd1 is defined as dd1 =xNd◦3d1. The
product of two general elements of Pk is defined by the linear extension of the multiplicative operation we have
defined.
For example, if
d =
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2 3 4 5 6 7
1′ 2′ 3′ 4′ 5′ 6′ 7′ , d 1 =
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2 3 4 5 6 7
1′ 2′ 3′ 4′ 5′ 6′ 7′ (4.2)
6
we have that
dd1 =
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2 3 4 5 6 7/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1′ 2′ 3′ 4′ 5′ 6′ 7′ = x3
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2 3 4 5 6 7
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1′ 2′ 3′ 4′ 5′ 6′ 7′
. (4.3)
One checks that this rule gives rise to a well-defined associative multiplication on Pk, in other words, dd1 does not
depend on the choices of diagrammatic representations for d and d1.
For anyt∈ C we define the specialized partition algebraPk(t) =Pk⊗C[x] C where C is made into an C[x]-algebra
via x7→t.
As is well known, Sk is a Coxeter group on generatorsS ={s1,s 2,...,s k−1} wheresi is the simple transposition
si = (i,i + 1). Let C[x]Sk be the group algebra for Sk over C[x]. Then there is a natural algebra inclusion
ιk : C[x]Sk ,− →Pk given by
si7→
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1 2
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
1′ 2′
/Bullet /Bullet /Bullet /Bullet /Bullet /Bullet
i
i′
n
n′ . (4.4)
Let ek = ιk
 
1
k!
X
σ∈Sk
σ
!
. Then ek is an idempotent of Pk. We use it to introduce the protagonist of the present
paper.
Definition 1. The spherical partition algebra SPk is defined as the idempotent truncation of Pk with idempotent
ek, that is
SPk =ekPkek. (4.5)
Similarly, for t∈ C we define the specialized spherical partition algebra SPk(t) asSPk(t) =ekPk(t)ek.
Note that SPk is a subalgebra of Pk, but not a unital subalgebra, since the one-element for SPk is ek, and
similarly forSPk(t).
