---
doc_id: arxiv-q-alg-9702017v2
doc_title: "Idempotents of Hecke algebras of type A"
section_id: sec-001-2-the-hecke-algebra-and-homfly-skein-theory
section_title: "The Hecke algebra and Homfly skein theory"
section_number: 2
pages: 3-6
source_pdf: 9702017v2.pdf
source_sha256: 282c911abb2a54e9
toc_source: outline
doc_brief: "Idempotents of Hecke algebras of type A — We use a skein-theoretic version of the Hecke algebras of type A to present three-dimensional diagrammatic views of Gyoja’s idempotent el- ements, based"
---
The Hecke algebra and Homﬂy skein theory
We give a brief description of skein theory based on planar pieces of knot diagrams
and a framed version of the Homﬂy polynomial. The ideas go back to Conway
and have been substantially developed by Lickorish and others. A fuller version
of this account can be found in [13]. At a later stage we shall expand our view
from diagrams to actual pieces of knot lying in controlled regions of 3-dimensional
space, under suitable equivalence.
We shall work with the framed Homﬂy polynomial X . This is an invariant
of framed oriented links, constructed from the Homﬂy polynomial by setting
X (L) = (xv−1)ω(D)P(L). Here ω(D) is the writhe (the sum of the signs of the
crossings) of any diagram D of the framed link L which realises the chosen framing
by means of the ‘blackboard parallel’. It is determined, up to a scalar, by the
skein relations in Fig. 1 for conventionally framed link diagrams which diﬀer only
as shown. We will normalise X to take the value 1 on the empty knot, taking
X = v−1 −v
z
for the unknot with zero framing.
Let F be a planar surface and ﬁx a (possibly empty) set of distinguished points
on the boundary. We consider diagrams in F, consisting of oriented arcs joining
any distinguished boundary points and oriented closed curves, up to Reidemeister
moves II and III. They carry the implicit framing deﬁned by the parallel curves in
the diagram. Deﬁne the framed Homf ly skein of F, denoted by S(F), to consist
of linear combinations of diagrams in F modulo the skein relations in Fig. 2 As a
consequence, the relation in Fig. 3 holds in S(F), for any diagram D, where the
oriented circle denotes a null homotopic loop.
We are interested in three speciﬁc cases, namely when F is the whole plane
R2, the annulus S1 × I or the rectangle Rn
n ∼= I × I with n distinguished points
on its top and bottom edge. In the last case we insist that any arcs in Rn
n enter at
Idempotents of the Hecke algebra.
4
x−1
−
x
=
z
,
=
(xv−1)
.
Figure 2: The skein relations for the Homﬂy skein of a surface
D ⊔
=
v−1 −v
z
D ,
Figure 3: The skein relation for a null homotopic loop
the top and leave at the bottom. Diagrams in Rn
n are termed oriented n-tangles,
and include the case of n-string braids.
A positive permutation braid is deﬁned for each permutation π ∈Sn. It is the
n-string braid, ωπ, uniquely determined by the properties
i) all strings are oriented from top to bottom
ii) for i = 1, . . . , n the ith string joins the point numbered i at the top of the
braid to the point numbered π(i) at the bottom of the braid,
iii) all the crossings occur with positive sign and each pair of strings cross at
most once.
These were ﬁrst deﬁned by Elrifai and Morton [6]. We can think of the braid
strings as sitting in layers, with the ﬁrst string at the back and the nth string at
the front.
We deﬁne the negative permutation braid for π in exactly the same manner
as the positive permutation braid except that we demand that all the crossing
be negative. We shall denote this braid by ωπ. The inverse of ωπ is the negative
permutation braid with permutation π−1, thus ω−1
π
= ωπ−1.
The skein S(R2) is just the set of linear combinations of framed link diagrams,
modulo the skein relations. Every diagram D represents a scalar multiple of the
empty diagram, with the multiple being simply X (D).
It is shown in [16] that the skein S(Rn
n) is spanned by the n! positive permu-
tation braids, and that these are linearly independent. The elementary braid σi,
which is the positive permutation braid for the transposition (i i+1), satisﬁes the
relation x−1σi −xσ−1
i
= z in the skein. The skein forms an algebra over Λ with
multiplication derived from the concatenation of diagrams. As is conventional for
braids, we write ST for the diagram given by placing diagram S above diagram
T. The resulting algebra is a quotient of the braid-group algebra. It is shown
in [16] that the algebra S(Rn
n) is isomorphic to the Hecke algebra Hn of type A,
Idempotents of the Hecke algebra.
5
...
...
...
Figure 4: The wiring of S(Rn
n) into S(S1 × I)
with the explicit presentation
Hn
=
*
σi
:
i = 1, . . . , n −1

σiσj = σjσi : |i −j| > 1
σiσi+1σi = σi+1σiσi+1
x−1σi −xσ−1
i
= z ,
+
.
There are various presentations of the Hecke algebra in the literature. Here
we have used a coeﬃcient ring Λ with 3 variables x, v and z.
The variable
v is needed in the skein when we want to write a general tangle in terms of
the basis of permutation braids, but it does not appear in the relations. The
variable x keeps track of the writhe of a diagram, and can be dropped without
aﬀecting the algebraic properties. Deﬁne an algebra Hn(1, z), obtained from Hn
by setting x = 1, in terms of generators ρi where the quadratic relation is given
by ρi −ρ−1
i
= z.
In algebra texts such as [12, 5] the Hecke algebra is usually presented with a
quadratic relation whose roots are q and −1. We will denote this presentation
by Hq(n). With generators τi, the quadratic relation is τ 2
i = (q −1)τi + q. Note
that these presentations are all isomorphic.
Hn
∼=
Hn(1, z)
∼=
Hq(n)
σi
7→
xρi
ρi
7→
s−1τi
where we relate q and z by setting z = s −s−1 and q = s2.
In what follows we shall generally use the skein form S(Rn
n) of Hn, but the re-
sults can be transferred immediately to the other versions by these isomorphisms.
A wiring W of a surface F into another surface F ′ is a choice of inclusion of F
into F ′ and a choice of a ﬁxed diagram of curves and arcs in F ′−F whose bound-
ary is the union of the distinguished sets of F and F ′. A wiring W determines
naturally a Λ-linear map S(W) : S(F) →S(F ′).
We can wire the rectangle Rn
n into the annulus as indicated in Fig. 4. The
resulting diagram in the annulus is called the closure of the oriented tangle. We
shall also use the term ‘closure’ for the Λ-linear map from each Hecke algebra Hn
to the skein of the annulus induced by this wiring.
Idempotents of the Hecke algebra.
6
The skein S(S1 × I) of the annulus itself forms an algebra, whose product
is given by stacking the annuli one inside the other. This product is obviously
commutative (lift the inner annulus up and stretch it so that the outer one will
ﬁt on the inside of it). Write C for S(S1 ×I) regarded as a Λ-algebra in this way.
Let C+ be the sub-algebra spanned by the closures of oriented tangles. Turaev
[19] showed that C+ is freely generated as an algebra by {Am, m ∈N}, where
Am is the closure of the positive permutation braid for the cycle (1 2 . . . m).
Write C(n) for the linear subspace spanned by the closures of oriented n-
tangles. This is spanned by all terms of the form (Ai1)j1(Ai2)j2 · · · (Aip)jp where
ik, jk ∈N and Pp
k=1 ikjk = n. Hence the algebra C+ is graded as
C+ =
∞
M
n=0
C(n) ,
and each subspace C(n) is the image of the Hecke algebra Hn under the closure
map.
