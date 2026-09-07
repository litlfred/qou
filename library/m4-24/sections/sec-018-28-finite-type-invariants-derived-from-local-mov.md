---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-018-28-finite-type-invariants-derived-from-local-mov
section_title: "Finite type invariants derived from local moves"
section_number: 2.8
pages: 40-43
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
One aspect of the study of knot invariants is the study of the set of knots. A
local move and 
nite type invariants derived from it might give an approach of
this study.
A local move is a move between two knots, which are identical except for a ball,
where they di
er as shown in both sides of a move in Figure 10. Let R be a
commutative ring with 1, and K the set of isotopy classes of oriented knots,
as before. For a local move m, we de
ne Fd(RK;m) as follows. Let K be an
oriented knot with d disjoint balls B1;B 2; ;Bd such that K is as shown in
o n es i d eo fm in each Bi . For any subset Sf 1; 2; ;dg,w ed e n o t eb yKS
the knot obtained from K by applying m in each Bi for i2 S. We de
ne
Fd(RK;m) to be the submodule of RK spanned by
X
S
(−1)#SKS (13)
for any K with d balls, where #S denotes the number of elements of S,a n d
the sum runs over all subsets S off1; 2; ;dg. Then, we have a descending
series of submodules,
RK =F0(RK;m) F 1(RK;m) F 2(RK;m)  :
Note that Fd(RK)= Fd(RK;) for a crossing change \". An R-homomor-
phism v :RK!R is called a 
nite type invariant of m-degreed,o ra n m 
nite
type invariant of degree d,i f vjFd+1(RK;m) =0 .
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 413
A crossing change \" :  !
A double crossing change \" :  !
A#m o v e:  !
Ap a s sm o v e:  !
Am o v e:  !
A doubled delta move  :  !
An n-gon move :  !
Figure 10: Some local moves among oriented knots. The strands of both sides of a 
move and an n-gon move have any orientations such that corresponding strands from
opposite sides of the moves are oriented in the same way. Each side of an n-gon move
has n strands.
It is a fundamental problem of 
nite type invariants to calculate the correspond-
ing graded spaces, which would enable us to identify 
nite type invariants in
some sense.
Problem 2.18 CalculateFd(ZK;m)=Fd+1(ZK;m), letting m be a local move
such as
(1) a # move,
(2) ap a s sm o v e ,
(3) a  move,
(4) an n-gon move.
Geometry &TopologyMonographs, Volume 4 (2002)
414 T. Ohtsuki (Editor)
Remark It is known that crossing change, double crossing change, # move
(see [289]),  move (see [298]), n-gon move (see [2]) are unknotting operations,
i.e. any oriented knot can be related to the trivial knot by a sequence of isotopies
and each of these moves. Hence, F0(ZK;m)=F1(ZK;m)=Z for these moves
m.
It is known [202] that Arf invariant gives the bijection
fknotsg=(pass move)−!Z=2Z:
Hence,F0(ZK; pass move)=F1(ZK; pass move)=ZZ.
Remark  
nite type invariants were introduced in [280]; see also [372].
Remark (K. Habiro) The following relations hold,
F2d(ZK;) F d(ZK; ) F 3d(ZK;);
Fd(ZK;) F d(ZK; #) F d(ZK; ):
These relations imply that m 
nite type invariants are Vassiliev invariants, and
Vassiliev invariants are m 
nite type invariants, for m =# ; . Further, the
rank ofFd(ZK;m)=Fd+1(ZK;m) is 
nite for these m.
Remark For the Kontsevich invariant Z (introduced in Chapter 3), we have
that
Z
 
−Z
 
= +

terms of
higher degrees

;
where two tangles in the left hand side are related by a  move. Hence, the
image of
Fd(QK; )−!F2d(QK)−!F2d(QK)=F2d+1(QK)=A(S1;Q)(2d)
is equal to the subspace of A(S1;Q)(2d) spanned by Jacobi diagrams on S1
whose uni-trivalent graphs are disjoint unions of d dashed Y graphs.
Remark Finite type invariants derived from a double crossing change were
introduced in [13], to study 
nite type invariants of links with a 
xed linking
matrix. For knots, they are equal to Vassiliev invariants, that is,Fd(ZK;)=
Fd(ZK;).
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 415
The surgery on is de
ned to be the surgery along :
Figure 11: De
nition of the surgery on a Y graph. Dotted lines imply strands possibly
knotting and linking. Three circles (partially dotted) in the left picture are called
leaves.
(Y. Ohyama) In the case all arcs in a  move are contained in the same
component, it is called a self  move. If two links can be transformed into
each other by a 
nite sequence of self  moves, they are said to be  link
homotopic.
Problem 2.19 (Y. Ohyama) Find necessary and sucient conditions for two
-component links (> 2)t ob e  link homotopic.
Remark (Y. Ohyama) For a -component link K =K1[K2[::: [K ,l e t
1 =a−1(K)a n d2 =a+1(K)−a−1(K) (P
i=1a2(Ki)f o rt h ec o e  c i e n t
ai(K) of the term zi in the Conway polynomial of K .
It is known [278, 298] that two knots (or links) can be transformed into each
other by a 
nite sequence of  moves if and only if they have the same number
of components, and, for properly chosen orders and orientations, they have the
same linking numbers between the corresponding components. In particular, if
two links are  link homotopic, then their 1 coincide. Further, it is known
[306] that if two component links are  link homotopic, then their2 coincide.
These are necessary conditions of this problem.
Moreover, for 2-component links, a pair of 1 and 2 is a faithful invariant of 
link homotopy. Namely, for two 2-component links, they are  link homotopic
if and only if their 1 and 2 coincide [307]. This gives a required condition of
this problem for 2-components links.
