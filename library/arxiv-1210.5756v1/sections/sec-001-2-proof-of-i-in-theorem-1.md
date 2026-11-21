---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-001-2-proof-of-i-in-theorem-1
section_title: "Proof of (i) in Theorem 1"
section_number: 2
pages: 3-6
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Proof of (i) in Theorem 1
The proof presented in this section follows the ideas of the proof of (i) of Theorem 1.1 in [2] with some
proper modiﬁcations based on the recent breakthrough results of Hales [6]. The details are as follows.
Let B denote the (closed) unit ball centered at the origin o of E3 and let P := {c1+B, c2+B, . . . , cn+B}
denote the packing of n unit balls with centers c1, c2, . . . , cn in E3 having the largest number C(n) of touching
pairs among all packings of n unit balls in E3. (P might not be uniquely determined up to congruence in
which case P stands for any of those extremal packings.) Now, let ˆr := 1.58731. The following statement
shows the main property of ˆr that is needed for our proof of Theorem 1.
Theorem 4. Let B1, B2, . . . , B13 be 13 diﬀerent members of a packing of unit balls in E3. Assume that each
ball of the family B2, B3, . . . , B13 touches B1. Let ˆBi be the closed ball concentric with Bi having radius ˆr,
1 ≤i ≤13. Then the boundary bd( ˆB1) of ˆB1 is covered by the balls ˆB2, ˆB3, . . . , ˆB13, that is,
bd( ˆB1) ⊂∪13
j=2 ˆBj .
Proof. Let oi be the center of the unit ball Bi, 1 ≤i ≤13 and assume that B1 is tangent to the unit balls
B2, B3, . . . , B13 at the points tj ∈bd(Bj) ∩bd(B1), 2 ≤j ≤13.
Let α denote the measure of the angles opposite to the equal sides of the isosceles triangle △o1pq with
dist(o1, p) = 2 and dist(p, q) = dist(o1, q) = ˆr, where dist(·, ·) denotes the Euclidean distance between the
corresponding two points. Clearly, cos α = 1
ˆr with α < π
3 .
o1
p
α
α
q
≈78°
Figure 1: The isosceles triangle △o1pq.
Lemma 1. Let T be the convex hull of the points t2, t3, . . . , t13. Then the radius of the circumscribed circle
of each face of the convex polyhedron T is less than sin α.
Proof. Let F be an arbitrary face of T with vertices tj, j ∈IF ⊂{2, 3, . . . , 13} and let cF denote the center
of the circumscribed circle of F. Clearly, the triangle △o1cF tj is a right triangle with a right angle at cF
and with an acute angle of measure βF at o1 for all j ∈IF . We have to show that βF < α. We prove this by
contradiction. Namely, assume that α ≤βF . Then either π
3 < βF or α ≤βF ≤π
3 . First, let us take a closer
look of the case π
3 < βF . Reﬂect the point o1 about the plane of F and label the point obtained by o′
1.
Clearly, the triangle △o1o′
1oj is a right triangle with a right angle at o′
1 and with an acute angle of
measure βF at o1 for all j ∈IF . Then reﬂect the point o1 about o′
1 and label the point obtained by o′′
1
furthermore, let B′′
1 denote the unit ball centered at o′′
1. As π
3 < βF therefore dist(o1, o′′
1) < 2 and so,
one can simply translate B′′
1 along the line o1o′′
1 away from o1 to a new position say, B′′′
1 such that it is
tangent to B1. However, this would mean that B1 is tangent to 13 non-overlapping unit balls namely, to
3
`
oj
o1
o1
`
o1
CF
t j
βF
`
Figure 2: The plane reﬂections to obtain o′
1 and o′′
1.
B′′′
1 , B2, B3, . . . , B13, clearly contradicting to the well-known fact ([14]) that this number cannot be larger
than 12. Thus, we are left with the case when α ≤βF ≤π
3 . By repeating the deﬁnitions of o′
1, o′′
1, and B′′
1,
the inequality βF ≤π
3 implies in a straightforward way that the 14 unit balls B1, B′′
1, B2, B3, . . . , B13 form
a packing in E3. Moreover, the inequality α ≤βF yields that dist(o1, o′′
1) ≤4 cos α = 4
ˆr = 2.51998... < 2.52.
Finally, notice that the latter inequality contradicts to the following recent result of Hales [6].
Theorem 5. Let B1, B2, . . . , B14 be 14 diﬀerent members of a packing of unit balls in E3. Assume that
each ball of the family B2, B3, . . . , B13 touches B1. Then the distance between the centers of B1 and B14 is
at least 2.52.
This completes the proof of Lemma 1.
Now, we are ready to prove Theorem 4. First, we note that by projecting the faces F of T from the
center point o1 onto the sphere bd( ˆB1) we get a tiling of bd( ˆB1) into spherically convex polygons ˆF. Thus,
it is suﬃcient to show that if F is an arbitrary face of T with vertices tj, j ∈IF ⊂{2, 3, . . . , 13}, then its
central projection ˆF ⊂bd( ˆB1) is covered by the closed balls ˆBj, j ∈IF ⊂{2, 3, . . . , 13}. Second, in order to
achieve this it is suﬃcient to prove that the projection ˆcF of the center cF of the circumscribed circle of F
from the center point o1 onto the sphere bd( ˆB1) is covered by each of the closed balls ˆBj, j ∈IF ⊂{2, 3, . . . ,
13}. Indeed, if in the triangle △o1ojˆcF the measure of the angle at o1 is denoted by βF , then Lemma 1
implies in a straighforward way that βF < α. Hence, based on dist(o1, oj) = 2 and dist(o1, ˆcF ) = ˆr, a
simple comparison of the triangle △o1ojˆcF with the triangle △o1pq yields that dist(oj, ˆcF ) < ˆr holds for
all j ∈IF ⊂{2, 3, . . . , 13}, ﬁnishing the proof of Theorem 4.
Next, let us take the union Sn
i=1 (ci + ˆrB) of the closed balls c1 + ˆrB, c2 + ˆrB, . . . , cn + ˆrB of radii ˆr
centered at the points c1, c2, . . . , cn in E3.
Theorem 6.
nvol3(B)
vol3 (Sn
i=1 (ci + ˆrB)) < 0.7547,
where vol3(·) refers to the 3-dimensional volume of the corresponding set.
Proof. First, partition Sn
i=1 (ci + ˆrB) into truncated Voronoi cells as follows. Let Pi denote the Voronoi cell
of the packing P assigned to ci + B, 1 ≤i ≤n, that is, let Pi stand for the set of points of E3 that are not
farther away from ci than from any other cj with j̸ = i, 1 ≤j ≤n. Then, recall the well-known fact (see
for example, [5]) that the Voronoi cells Pi, 1 ≤i ≤n just introduced form a tiling of E3. Based on this it
is easy to see that the truncated Voronoi cells Pi ∩(ci + ˆrB), 1 ≤i ≤n generate a tiling of the non-convex
container Sn
i=1 (ci + ˆrB) for the packing P. Second, as
√
2 < ˆr therefore the following very recent result
of Hales [6] (see Lemma 9.13 on p. 228) applied to the truncated Voronoi cells Pi ∩(ci + ˆrB), 1 ≤i ≤n
implies the inequality of Theorem 6 in a straightforward way.
4
Figure 3: Voronoi cells of a packing with yellow ci + B’s and blue ci + ˆrB’s.
Theorem 7. Let F be an arbitrary (ﬁnite or inﬁnite) family of non-overlapping unit balls in E3 with the unit
ball B centered at the origin o of E3 belonging to F. Let P stand for the Voronoi cell of the packing F assigned
to B. Let Q denote a regular dodecahedron circumscribed B (having circumradius
√
3 tan π
5 = 1.2584...).
Finally, let r :=
√
2 = 1.4142... and let rB denote the ball of radius r centered at the origin o of E3. Then
vol3(B)
vol3(P) ≤
vol3(B)
vol3(P ∩rB) ≤vol3(B)
vol3(Q) < 0.7547.
This ﬁnishes the proof of Theorem 6.
The well-known isoperimetric inequality [11] applied to Sn
i=1 (ci + ˆrB) yields
Lemma 2.
36πvol2
3
 n
[
i=1
(ci + ˆrB)
!
≤svol3
2
 
bd
 n
[
i=1
(ci + ˆrB)
!!
,
where svol2(·) refers to the 2-dimensional surface volume of the corresponding set.
Thus, Theorem 6 and Lemma 2 generate the following inequality.
Corollary 1.
15.159805n
2
3 < 15.15980554...n
2
3 =
4π
(0.7547)
2
3 n
2
3 < svol2
 
bd
 n
[
i=1
(ci + ˆrB)
!!
.
Now, assume that ci + B ∈P is tangent to cj + B ∈P for all j ∈Ti, where Ti ⊂{1, 2, . . . , n} stands
for the family of indices 1 ≤j ≤n for which dist(ci, cj) = 2. Then let ˆSi := bd(ci + ˆrB) and let ˆcij be
the intersection of the line segment cicj with ˆSi for all j ∈Ti. Moreover, let C ˆSi(ˆcij, π
6 ) (resp., C ˆSi(ˆcij, α))
denote the open spherical cap of ˆSi centered at ˆcij ∈ˆSi having angular radius π
6 (resp., α with 0 < α < π
2
and cos α = 1
ˆr). Clearly, the family {C ˆSi(ˆcij, π
6 ), j ∈Ti} consists of pairwise disjoint open spherical caps of
ˆSi; moreover,
P
j∈Ti svol2

C ˆSi(ˆcij, π
6 )

svol2

∪j∈TiC ˆSi(ˆcij, α)
 =
P
j∈Ti Sarea
 C(uij, π
6 )

Sarea (∪j∈TiC(uij, α)) ,
(1)
where uij := 1
2(cj −ci) ∈S2 := bd(B) and C(uij, π
6 ) ⊂S2 (resp., C(uij, α) ⊂S2) denotes the open spherical
cap of S2 centered at uij having angular radius π
6 (resp., α) and where Sarea(·) refers to the spherical area
measure on S2. Now, Moln´ar’s density bound (Satz I in [10]) implies that
P
j∈Ti Sarea
 C(uij, π
6 )

Sarea (∪j∈TiC(uij, α)) < 0.89332 .
(2)
5
In order to estimate
svol2
 
bd
 n
[
i=1
(ci + ˆrB)
!!
from above let us assume that m members of P have 12 touching neighbours in P and k members of P have
at most 9 touching neighbours in P. Thus, n−m−k members of P have either 10 or 11 touching neighbours
in P. (Here we have used the well-known fact that τ3 = 12, that is, no member of P can have more than 12
touching neighbours.) Without loss of generality we may assume that 4 ≤k ≤n −m.
First, we note that Sarea
 C(uij, π
6 )

= 2π(1 −cos π
6 ) = 2π(1 −
√
3
2 ) and svol2

C ˆSi(ˆcij, π
6 )

= 2π(1 −
√
3
2 )ˆr2. Second, recall Theorem 4 according to which if a member of P say, ci + B has exactly 12 touching
neighbours in P, then ˆSi ⊂S
j∈Ti(cj + ˆrB). These facts together with (1) and (2) imply the following
estimate.
Corollary 2. svol2 (bd (Sn
i=1 (ci + ˆrB))) < 24.53902
3
(n −m −k) + 24.53902k .
Proof.
svol2
 
bd
 n
[
i=1
(ci + ˆrB)
!!
<
 
4πˆr2 −10 · 2π(1 −
√
3
2 )ˆr2
0.89332
!
(n −m −k) +
 
4πˆr2 −3 · 2π(1 −
√
3
2 )ˆr2
0.89332
!
k
< 7.91956(n −m −k) + 24.53902k < 24.53902
3
(n −m −k) + 24.53902k .
Hence, Corollary 1 and Corollary 2 yield in a straightforward way that
1.85335n
2
3 −3k < n −m −k .
(3)
Finally, as the number C(n) of touching pairs in P is obviously at most
1
2 (12n −(n −m −k) −3k) ,
therefore (3) implies that
C(n) ≤1
2 (12n −(n −m −k) −3k) < 6n −0.926675n
2
3 < 6n −0.926n
2
3 ,
ﬁnishing the proof of (i) in Theorem 1.
