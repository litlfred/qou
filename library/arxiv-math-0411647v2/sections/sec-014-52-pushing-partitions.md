---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-014-52-pushing-partitions
section_title: "Pushing partitions"
section_number: 5.2
pages: 46-53
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
jugacy classes of permutations and not permutations themse lves. For this
reason we need a method to enumerate in the sums similar to (2. 5) not the
individual summands, but whole classes of summands (summan ds within
each class will be conjugate). Pushing partitions will turn out to be the
suitable objects to enumerate such classes.
We say that a partition π of a ﬁnite ordered set X (by changing the labels
we can assume that X = {1, . . . , n }) is a pushing partition if no neighbors l
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 47
and l + 1 are connected by π for 1 ≤ l ≤ n. It is useful to arrange numbers
1, . . . , n in a circle, therefore the case l = n should be understood that
neighbors n and 1 are not connected by π. In particular, it cannot happen
that n = 1.
We say that p ∼ π if π is a partition of {1, . . . , n }for some n ∈ N and
p = ( p1, . . . , p n) is a sequence of length n such that for every 1 ≤ l, m ≤
n numbers l and m are connected by π iff pl = pm . For every pushing
sequence p there exists a unique pushing partition π such that p ∼ π.
5.2.1. Explicit form of the maps Φ ps
~SA
and Φ ps
as. Let a pushing partition
π = {π 1, . . . , π r} of the set {1, 2, . . . , n } be given. To every block π s of
the partition we assign a label min π s, i.e. the smallest element of π s. To
every element of {1, 2, . . . , n } we assign the label of the block it belongs
to. In this way we constructed a sequence p = ( p1, . . . , p n) such that
p ∼ π. We set ∗ = p1 = 1 and A to be the set of the other labels,
i.e. A = {p1, . . . , p n} \ { ∗} = {min π s : 1 ≤ s ≤ r} \ { 1}. We decorate
on the graph of the fat partitionπ fat all elements of the set A (cf Figure 3.1).
In the following we shall compute Φ ps
~SA
(p) for p deﬁned as above; please
note that Proposition 5.3 allows us to rename the labels and to ﬁnd Φ ps
~SA
(p)
for a general p.
As we already mentioned in Section 3.1.1, we can view the fat p artition
π fat as a bijection π fat : {1 ′, 2 ′, . . . , n ′} → {1, 2, . . . , n }. We also consider
a bijection c : {1, 2, . . . , n } → {1 ′, 2 ′, . . . , n ′} given by . . . , 3 ↦→ 2 ′, 2 ↦→
1 ′, 1 ↦→ n ′, n ↦→ (n − 1) ′, . . . . We consider the cycle decomposition of the
permutation π fat ◦ c ∈ S{1,2,...,n } and remove from this decomposition all el-
ements except the elements of A. In this way we constructed a permutation
(π fat ◦c)|A ∈ SA , called restriction of π fat ◦c to the set A. This operation has
a nice interpretation: on the graphical representation of π fat and c we travel
along the cycles by following the arrows and we write down only decorated
vertices. We equip (π fat ◦ c)|A with a structure of a partial permutation by
setting its support to be A.
For example, for π =
{
{1, 3 }, {2, 5, 7 }, {4}, {6}
}
depicted on Figure 2.3
we have p = (1, 2, 1, 4, 2, 6, 2 ), A = {2, 4, 6 }and the decorations of π fat are
depicted on Figures 3.1, 3.2 and 3.3. The composition π fat ◦ c has a cycle
decomposition (1, 2, 3, 5, 4)(6, 7 ). It follows that (π fat ◦ c)|A = (2, 4)(6).
Theorem 5.4. Let π and p be as above. Then
Φ ps
~SA
(p) = ( π fat ◦ c)|A .
Proof. The equality of permutations follows easily from Lemma 5.5 below
by setting l = 1 and the equality of supports is trivial. □
48 PIOTR ´SNIADY
Lemma 5.5. Let π and p be as above, we set pn+1 := p1 = 1 = ∗ and
let σ 1, . . . , σ n+1 be as in Sections 5.1.4 and 5.1.5. Let x ∈ A ∪ {∗}and let
1 ≤ l ≤ n + 1.
If x = pl then σ l(x) = ∗.
Suppose that x ⁄= pl; let m be the smallest index such thatl ≤ m ≤ n+1
and x = pm . If no such index exist then σ l(x) = x. Otherwise we start
in the vertex m a walk on the graphical representation of π fat and c by
following the arrows until we enter some decorated vertex y (after having
made at least one step, i.e. starting in a decorated vertex do not count as
entering it). The above walk always stops after a ﬁnite number of steps and
σ l(x) = y.
Proof. The shall prove the lemma by backward induction. In the case l =
n + 1 it holds trivially.
Suppose that the statement of lemma is true for all l ′ > l. The ﬁrst part,
σ l(pl) = ∗ follows from the very construction of σ l in (5.4).
Observe that for everyr we have σ r = (ar∗)σ r+1 hence σ r(x) = σ r+1(x)
if x /∈ {σ − 1
r (∗), σ − 1
r+1(∗)}= {pr, p r+1}. This has twofold implications.
Firstly, if x / ∈ {pl, p l+1, . . . , p n, p n+1} then σ l(x) = σ l+1(x) = · · · =
σ n+1(x) = x, which ﬁnishes the proof.
Secondly, when the last case in the lemma statement holds then
σ l(x) = σ l+1(x) = · · · = σ m − 1(x) =
(
(am − 1∗) ◦ σ m 
)
(x) = am − 1,
where we used the fact that pm = x is equivalent to σ m (x) = ∗. Equation
(5.5) implies that σ l(x) = σ m (pm − 1). We denote by π h the block of π =
{π 1, . . . , π r}such that the element m − 1 belongs to it. Let r be the smallest
index such that pm − 1 = pr and m ≤ r ≤ n + 1. If no such index exists
then σ l(x) = σ m (pm − 1) = pm − 1. Otherwise, if such an index exists then
σ l(x) = σ m (pm − 1) = σ m +1(pm − 1) = · · · = σ r(pm − 1) = σ r(pr).
We compare the value ofσ l(x) computed above with the answer given by
the graphical algorithm: we start our trip in vertex m and then go to vertex
(m − 1) ′. If the index r considered above does not exist then m − 1 is the
biggest element of π h and therefore (m − 1) ′ is connected by π fat with the
smallest element of π h which is therefore decorated (the exceptional case
1 ∈ π h is not possible since this would mean that pm − 1 = p1 = ∗ and
in this case pm − 1 = pn+1 and the index r would exist) and the algorithm
terminates giving the answer min π h = pm − 1 which coincides with the
correct value. Otherwise, if the index r exists then (m − 1) ′ is connected by
π fat with the vertex r, l < m + 1 ≤ r ≤ n + 1 (the vertex n + 1 should be
understood as the vertex 1). From the inductive hypothesis it follows that
the algorithm will return the answer σ r(pr) which is again correct. □
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 49
Corollary 5.6. Let π and p be as above, let a = Φ ps
as(p) and let 1 ≤ l ≤ n.
We start in the vertexl a walk on the on the graphical representation ofπ fat
and c by following the arrows until we enter some decorated vertexy (after
having made at least one step).
Then
al = y.
Proof. It is a simple application of (5.5) and Lemma 5.5. □
5.2.2. Maps Φ P
ps and Σ = Φ P
C(~SA). Let us ﬁx the ﬁnite set A and the ex-
tra element ∗. We consider an algebra of pushing sequences in which the
multiplication is as in Section 5.1.7 and the addition is und erstood as an
addition of formal sums. The map Φ ps
~SA
extends naturally to an algebra ho-
momorphism from the algebra of pushing sequences to the alge bra C(~SA )
of partial permutations.
We deﬁne a map from pushing partitions to the algebra of pushi ng se-
quences by
(5.7) Φ P
ps(π ) =
∑
p∼ π
p.
We deﬁne the map Φ P
C(~SA) in the unique way which makes the diagram
below commute. This map is explicitly given by Claim 3.1 whic h will be
proved below.
(5.8)
Theorem 5.7. Claim 3.1 is true. In other words: let π be a partition of the
set {1, 2, . . . , n }and let numbers k1, . . . , k t be given by the above construc-
tion. Then
Σ π := Φ P
C(~S∞ )(π ) = Σ k1 ,...,k t ,
where Σ k1,...,k t ∈ C(~S∞) on the right–hand side should be understood as in
Section 2.1.10.
Proof. Equation (5.7) and requirement that (5.8) commutes imply that
Σ (π ) =
∑
p∼ π
Φ ps
~SA
(p).
By an appropriate renaming of labels Theorem 5.4 allows us to com-
pute each summand Φ ps
~SA
(p). We decompose Φ ps
~SA
(p) = ( π ◦ c)|A ∈
50 PIOTR ´SNIADY
S{p1,p 2 ,...,p n}\{ p1 } into a product of disjoint cycles and we denote by
k1, . . . , k t the lengths of these cycles. It follows that
Σ π = Σ k1 ,...,k t ,
where the right–hand side was deﬁned in (2.7).
From the proof of Theorem 5.4 it follows that for each 1 ≤ s ≤ t the
number ks is equal to the number of decorated elements in the correspond-
ing cycle of the permutationπ fat ◦c. One can easily see that the original def-
inition of the decorated elements is equivalent to the following one: element
m ∈ {1, 2, . . . , n }is decorated if and only if going counterclockwise from
m to (π fat ◦c)− 1(m) one does not cross the line between the marked starting
point between 1 and 1 ′ and the central disc (see Figure 3.1). Therefore ks is
equal to the number of elements in the corresponding cycle ofπ fat ◦ c minus
the number of times this cycle going clockwise crosses the line between the
starting point and the central disc. It follows that the numb ers k1, . . . , k t
deﬁned above coincide with (3.1) which ﬁnishes the proof. □
5.2.3. Multiplication of pushing partitions. In Section 3.2 we deﬁned the
multiplication of partitions. Diagram (5.8) commutes and w e shall prove
that Σ = Φ P
C(~SA) is an algebra homomorphism (we already know that Φ ps
~SA
is an algebra homomorphism; we will not need it but one can sho w that in
a certain sense Φ P
ps is also a homomorphism).
Lemma 5.8. Let 1 ≤ k < l ≤ m, let π 1 be a pushing partition of the set
ρ1 = {l+1, l +2, . . . , m, 1, 2, . . . , k }, let π 2 be a pushing partition of the set
ρ2 = {k + 1, k + 2, . . . , l }. We deﬁne a non–crossing partitionρ = {ρ1, ρ 2}.
Then
Φ P
C(~SA)(π 1 · π 2) = Φ P
C(~SA)(π 1)Φ P
C(~SA)(π 2),
where π 1 · π 2 denotes the ρ–ordered product of partitions π 1 and π 2 as
deﬁned in Section 3.2 and the product on the right–hand side i s the usual
product of the elements of C(~SA ).
Proof. Let us consider a simpler case ρ ′
1 = {1, 2, . . . , k + m − l}, ρ ′
2 =
{k + m − l + 1, k + m − l + 2, . . . , m }. From Proposition 5.2 it follows that
Φ P
ps(π 1)Φ P
ps(π 2) consists of all pushing sequences (p1, . . . , p m ) such that
p1 = pk+m − l+1 = ∗ and (p1, . . . , p k+m − l) ∼ π 1, (pk+m − l+1, . . . , p m ) ∼ π 2.
On the other hand the only non–trivial block ofρ ′
comp− 1 is {1, k + m − l + 1}
and therefore
Φ P
ps(π 1)Φ P
ps(π 2) = Φ P
ps(π 1 · π 2).
To both sides of the equation we apply the map Φ ps
~SA
and use the fact that it
is a homomorphism and the diagram (5.2) commutes.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 51
The general case follows from the observation that the partition ρ can be
obtained from ρ ′ by a cyclic rotation. One can easily see that a product
of rotated partitions is a rotation of the product of the orig inal partitions.
Finally, we apply Proposition 3.2. □
Lemma 5.9. Multiplication of partitions, as deﬁned in Section 3.2, is asso-
ciative. To be precise: let τ = {τ1, . . . , τ r}be a non–crossing partition of
the set {1, 2, . . . , n }. For each s let ˜τs = {τs,1 , . . . , τ s,l s}be a non–crossing
partition of the set τs. We denote by ^τ = ˜τ1 ∪ · · · ∪ ˜τr = {τs,k : 1 ≤
s ≤ r, 1 ≤ k ≤ ls}the non–crossing partition of the set {1, 2, . . . , n }. Let
furthermore π s,k be a pushing partition of the set τs,k for each choice of
1 ≤ s ≤ r and 1 ≤ k ≤ ls.
Then
(5.9)
∏
s
( ∏
k
π s,k
)
=
∏
s,k
π s,k ,
where the left–hand side is aτ–ordered product of ˜τs–ordered products and
the right–hand side is a ^τ–ordered product.
Proof. Probably the best way to prove this lemma is to use the graphical de-
scription of the partition multiplication from Section 3.2.2 since—speaking
informally—cutting holes, gluing discs and merging discs a re all associa-
tive operations. We provide a more detailed proof below.
Observe that every partitionσ which contributes to the left–hand side has
a property that for every a, b ∈ τs,k elements a and b are connected by σ
if and only if they are connected by π s,k . Furthermore since every partition
σ s which contributes in ∏
k π s,k must fulﬁll σ s ≥ ( ˜τs)comp− 1 therefore σ ≥
τcomp− 1 ∨
( ⋃
s( ˜τs)comp− 1
)
= ^τcomp− 1 (for the last equality see Lemma 5.10
below). It follows that every partition which appears on the left–hand side
of (5.9) appears also on the right–hand side.
To show the opposite inclusion, for a summand σ which appears on the
right–hand side of (5.9) we setσ s ∈ P(τs) to be the partition which connects
a, b ∈ τs if and only if a, b are connected by σ. Lemma 5.10 implies that
σ s ≥ ( ˜τs)comp− 1 hence σ s is one of the summands which appear in the
product ∏
k π s,k. By using a similar argument we see that σ is one of the
summands which contribute to the product ∏
s σ s and therefore contributes
to the left–hand side of (5.9). □
Lemma 5.10. We keep the notation from Lemma 5.9. Then
(5.10) τcomp− 1 ∨
( ⋃
s
( ˜τs)comp− 1
)
= ^τcomp− 1 .
Proof. Similarly as in Section 3.2.2 we consider a sphere with a coll ection
of holes, each corresponding to one of the blocks of τ. In the second step
52 PIOTR ´SNIADY
we replace each initial hole τs by a collection of holes ˜τs: in this way we
obtained a large sphere with a collection of holesτs,k . Alternatively we can
treat it as one big hole to which was glued a collection of disc s; every of
these discs corresponds to one of the blocks of ^τcomp− 1 which corresponds
to the right–hand side of (5.10).
On the other hand, we can treat the sphere with the ﬁrst collection of holes
as a sphere with a single hole glued with a collection of discscorresponding
to τcomp− 1. When we replace the hole τs by ˜τs it corresponds to gluing
another collection of discs ( ˜τs)comp− 1. Therefore the whole collection of
discs corresponds to the left–hand side of (5.10). □
Theorem 5.11. Claim 3.6 is true. In other words: let ρ = {ρ1, . . . , ρ r}be a
non–crossing partition of the set {1, 2, . . . , n }and for every 1 ≤ s ≤ r let
π s be a partition of the set ρs. Then
Σ
( ∏
s
π s
)
=
∏
1≤s≤r
Σ π s ,
where the multiplication on the left hand side should be unde rstood as the
ρ–ordered product of partitions and on the right hand side it s hould be
understood as the usual product of commuting elements in C(~S∞).
Proof. We shall use the induction with respect tor, the number of blocks of
the partition ρ. The case r = 1 is of course trivial.
Observe that since ρ is non–crossing therefore at least one blockρh has a
form ρh = {a, a + 1, a + 2, . . . , b }(for example, it is one of the blocks for
which the expression (max ρh − min ρh) takes the minimal value). Lemma
5.9 implies that ∏
s
π s = π h ·
( ∏
s⁄=h
π s)
.
We apply to both sides the map Φ P
C(~SA) = Σ and apply Lemma 5.8 to the
right hand side. The inductive hypothesis can be applied to the second factor
on the right hand side which ﬁnishes the proof. □
5.2.4. Jucys–Murphy element.
Theorem 5.12. Claim 4.3 is true. In other words, let X be a ﬁnite ordered
set, let ρ be a non–crossing partition of a ﬁnite ordered set and n ≥ 1 be
an integer. Then
Σ (MP
X) = MJM
|X|,
Σ (MP
ρ) = MJM
ρ ,
Σ (RP
n) = RJM
n ,
where Σ is the map considered in Section 3.1.1.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 53
Proof. Observe that every pushing sequence of length n appears in
Φ P
ps(MP
{1,2,...,n }) exactly once. The bijection between pushing and admis-
sible sequences together with the deﬁnition (2.5) ﬁnish the proof. □
6. F INAL REMARKS
