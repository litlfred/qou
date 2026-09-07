---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-028-36-the-chern-simons-series-of-con
section_title: "The Chern-Simons series of con"
section_number: 3.6
pages: 57-60
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
guration space integrals
Question 3.12 (C. Lescop) Is the Kontsevich integral of a (zero-framed)
knot equal to the Chern-Simons series of con
guration space integrals of the
same knot (with Gauss integral 0)?
The (normalized) Chern-Simons series of con
guration space integrals is a uni-
versal Vassiliev knot invariant that admits a natural and beautiful symmetric
de
nition that will be given below before describing the present situation of
this question that was 
rst raised by Kontsevich in [225].
In 1833, Carl Friedrich Gauss de
ned the 
rst example of a con
guration space
integral for an oriented two-component link. Let us formulate his de
nition in
a modern language. Consider an embedding
L :S1
1tS1
2 ,!R3
of the disjoint union of two circles S1 =fz2C s.t. jzj =1g intoR3 .W i t ha n
element (z1;z 2)o f S1
1S1
2 that will be called a con
guration, we may associate
the oriented direction Ψ(( z1;z 2)) of the vector −−−−−−−!L(z1)L(z2). Ψ(( z1;z 2))2 S2 .
Thus, we have associated a map
Ψ: S1
1S1
2 −!S2
from a compact oriented 2-manifold to another one with our embedding. This
map has an integral degree deg(Ψ) that can be de
ned in several equivalent
ways. For example, it is the number of preimages of a regular value of Ψ
counted with signs that can easily be computed from a regular diagram of our
two-component link as
deg(Ψ) = ] 12 −] 21 =] 21 −] 12 :
It can also be de
ned as the following con
guration space integral
deg(Ψ) =
Z
S1S1
Ψ(!)
where ! is the homogeneous volume form on S2 such that
R
S2 ! =1 . I ti s
obvious that this integral degree, that depends continuously on our embedding,
is an isotopy invariant; and the reader has recognized that deg(Ψ) is nothing
but the linking number of the two components of L.
Section 3.6 was written by C. Lescop.
Geometry &TopologyMonographs, Volume 4 (2002)
430 T. Ohtsuki (Editor)
We can again follow Gauss and associate the following similar Gauss integral
I(K)t oa C1 embedding K :S1 ,!R3 . Here, we consider the con
guration
space C =S1]0; 2[, and the map
Ψ: C−!S2
that maps (z1; ) to the oriented direction of
−−−−−−−−−−!
K(z1)K(z1ei), and we set
I(K)=
Z
C
Ψ(!):
This Gauss integral is NOT an isotopy invariant, and it can be seen as an
exercise that it takes any real value on any given isotopy class of knots.
However, we can follow Guadagnini, Martellini and Mintchev and associate
con
guration space integrals to our embedding K and to any Jacobi diagram
on the circle Γ without small loop like .A con
guration of such a diagram
is an embedding c of the set U[T of its vertices into R3 whose restriction
to the set U of univalent vertices factors through the knot embedding K so
that the factorization induces the cyclic order of U . Denote the set of these
con
gurations by C(K;Γ ). C(K; Γ) is an open submanifold of (S1)U (R3)T .
Denote the set of dashed edges of Γ byE, and 
x an orientation for these edges.
Then we can de
ne the map Ψ : C(K;Γ )−!
(
S2E whose projection to the S2
factor indexed by an edge from a vertex v1 to a vertex v2 is the direction of−−−−−−!c(v1)c(v2). This map Ψ is again a map between two orientable manifolds that
have the same dimension, namely the number of dashed half-edges of Γ, and
we can write the con
guration space integral:
I(K;Γ )=
Z
C(K;Γ)
Ψ(E!):
For example, if  denotes the Jacobi diagram ,t h e nI(K;)= I(K). Bott
and Taubes have proved that this integral is convergent [65]. Thus, this integral
is well-de
ned up to sign. In fact, an orientation of the trivalent vertices of Γ
provides I(K; Γ) with a well-de
ned sign14 such that the product I(K;Γ ) [ Γ ]2
A(S1;R) does not depend on the vertex orientation of Γ.
14Since S2 is equipped with its standard orientation, it is enough to orient C(K;Γ )
(S1)U  (R3)T in order to de
ne this sign. This will be done by providing the set of the
natural coordinates of (S1)U (R3)T with some order up to an even permutation. This set is
in one-to-one correspondence with the set of dashed half-edges of Γ, and the vertex-orientation
of the trivalent vertices provides a natural preferred such one-to-one correspondence up to some
(even!) cyclic permutations of three half-edges meeting at a trivalent vertex. Fix an order on
E , then the set of half-edges becomes ordered by (origin of the 
rst edge, endpoint of the 
rst
e d g e ,o r i g i n o ft h es e c o n de d g e , ...,e n d p o i n to ft h el a s t e d g e ) ,a n dt h i so r d e r o r i e n t sC(L;Γ ).
As an exercise, check that the sign of I(K; Γ)[Γ] does depend neither on our choices nor on
the vertex orientation of Γ.
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 431
Now, the perturbative expansion of the Chern-Simons theory for knots in R3
is the following sum running over all the Jacobi diagrams without small loops
and without vertex orientation:
ZCS(K)=
XI(K;Γ )
]AutΓ [Γ] 2A (S1;R)
where ]AutΓ is the number of automorphisms of Γ as a uni-trivalent graph
whose univalent vertices are cyclically ordered, but without vertex-orientation
for the trivalent vertices. The degree one part of ZCS is I(K;)
2 and therefore
ZCS is not invariant under isotopy. However, the evaluation 15 of ZCS at rep-
resentatives of knots with null Gauss integral is an isotopy invariant that is
a universal Vassiliev invariant of knots [65, 5, 381, 328]. Now, the still open
question raised by Kontsevich in [225] is: Is the Kontsevich integral of a zero
framed representative of a knot K equal to the above series of con
guration
space integrals of a representative of K with Gauss integral 0?
This question has been reduced by Sylvain Poirier [328] to the computation of
the following constant in A(S1;R)= A([0; 1];R) that is called the Bott and
Taubes anomaly. In order to de
ne the anomaly, replace the above knot K
by a straight line D, and consider a Jacobi diagram Γ on the oriented line.
De
ne C(D; Γ) and Ψ as before. Let ^C(D; Γ) be the quotient of C(D;Γ )
by the translations parallel to D and by the positive homotheties, then Ψ
factors through ^C(D; Γ) that has two dimensions less. Now, allow D to run
among all the oriented lines through the origin of R3 and de
ne ^C(Γ) as the
total space of the 
bration over S2 where the 
ber over the direction of D is
^C(D; Γ). Ψ becomes a map between two smooth oriented 16 manifolds of the
same dimension. Then we can again de
ne
I(Γ) =
Z
^C(Γ)
Ψ(E!):
Now, the anomaly is the following sum running over all Jacobi diagrams on the
oriented lines (again without vertex-orientation and without small loop):

 =
X I(Γ)
]AutΓ [Γ] 2A ([0; 1];R):
15Actually, this evaluation is equal to ZCS(K)e x p (−I(K;)
2 
) for any representative K ,
where 
2A ([0; 1];R) is the Bott and Taubes anomaly.
16 ^C(Γ) carries a natural smooth structure and can be oriented as follows: orient C(D;Γ )
as before, orient ^C(D;Γ ) s o t h a tC(D; Γ) is locally homeomorphic to the oriented product
(translation vector of the oriented line, ratio of homothety) ^C(D;Γ ) a n do r i e n t^C(Γ) as the
local product base 
ber.
Geometry &TopologyMonographs, Volume 4 (2002)
432 T. Ohtsuki (Editor)
Its degree one part is

1 = :
It is not hard to see that for any integer n, 
2n = 0. In [328], Sylvain Poirier
proved that if all 
i vanish for i 2, then the answer to the above Kontsevich
question is YES, and he computed 
3 = 0. He also computed 
5 = 0 with the
help of Maple. In [252], it is proved that 
 is a combination of diagrams with
two univalent vertices. Poirier also gave an equivalent de
nition of the anomaly
that allows one to see that, for any i> 1, 
i is a combination of diagrams with
at least 6 univalent vertices.
As a corollary, all coecients of the HOMFLY polynomial properly normalized
that are Vassiliev invariants of degree less than seven can be explicitly written
as combinations of the above con
guration space integrals. A positive answer
to the Kontsevich question would allow one to express any canonical Vassiliev
invariant as an explicit combination of the above con
guration space integrals.
G. Kuperberg and D. Thurston have constructed a universal 
nite type invari-
ant for homology spheres as a series of con
guration space integrals similar to
the above Chern-Simons series in [237]. Their construction yields two natural
questions that are stated in Question 11.9.
