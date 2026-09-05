---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-041-52-jones-wenzl-morphisms-presenting-the-bott-sam
section_title: "Jones-Wenzl morphisms. Presenting the Bott-Samelson category in rank 2 is"
section_number: 5.2
pages: 42-45
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
the topic of [Elib]. The calculations and proofs are too long to duplicate or fully
discuss in this paper. If the reader is willing to accept the J ones-Wenzl morphisms
as black boxes 3, satisfying the properties stated in this section and the ne xt, then
the reader need not consult [Elib]. We assume the reader is fa miliar with quantum
numbers and Temperley-Lieb algebras; background can be fou nd in [Elib].
Fixm< ∞. Consider the Temperley-Lieb algebraTL over Z[z] withm − 1 strands,
where the circle is evaluates to −z. In any k[z]-algebra we will use quantum numbers
to indicate the images of certain polynomials in z, where [2] is the image of z. For
instance, [3] is the image ofz2−1. When we say thatq is specialized to a primitive 2m-
th root of unity in a Z[z]-algebra, we mean that m satisﬁes the minimal polynomial
of [2] at this root of unity , which equates to the statements that [m] = 0 , [k] ⁄= 0 for
0<k <m , and [m − 1] = 1 .
After inverting some quantum numbers, Temperley-Lieb alge bras contain ele-
ments known as Jones-Wenzl projectors, and the Jones-Wenzl projector onm−1 strands
JW m−1 is known to be negligible and rotation-invariant when q is specialized to a
primitive 2m-th root of unity . The Jones-Wenzl projectorJW m can be deﬁned when-
ever certain quantum binomial coefﬁcients are invertible. Using diagrammatics for
the Temperley-Lieb algebra, the Jones-Wenzl projector can be described as a linear
combination of crossingless matchings.
Example 5.8.
+
+ +
+ +
= =
=
1
[2]
1
[3]
1
[3]
[2]
[3]
[2]
[3]
JW 1 JW 2
JW 3
3no pun intended!
SOERGEL CALCULUS 43
Any crossingless matching will divide the planar strip into 2(m−1) regions, which
can be colored (say , red and blue) so that colors always alternate across a strand. This
gives rise to the two-colored T emperley-Lieb algebra, which is an endomorphism alge-
bra appearing inside a 2-category with 2 objects, red and blu e. In this algebra, the
value of a blue circle surrounded by red and a red circle surro unded by blue can be
different scalars; so we deﬁne this algebra over the ring Z[x,y ]. Jones-Wenzl projec-
tors still exist, but each comes in two ﬂavors with different coefﬁcients, depending
on whether blue or red appears on the far right. The other ﬂavo r is obtained by
switching the colors and switching x andy.
Example 5.9.
+
+ +
+ +
= =
=
1
x
1
xy−1
1
xy−1
x
xy−1
y
xy−1
JW 1 JW 2
JW 3
Choose two indices s,t ∈ S. Given a 2-colored crossingless matching, we obtain
a Soergel graph on the planar disc as follows: deformation re tract each region into a
tree composed out of trivalent and univalent vertices, and c olor these trees appropri-
ately . The result will always be a Soergel graph of degree +2. In order for this map
to be well-deﬁned, not just for crossingless matchings but a lso for diagrams with
embedded circles, one must specialize Z[x,y ] to k under the map sending x ↦→ast
and y ↦→ats. The reader should convince themselves that this makes sens e, using
(5.2), (5.1), and (5.5) until the scalar ∂s(αt) = ast appears. Associated to the Jones-
Wenzl projector we have a linear combination of Soergel grap hs, which we call the
Jones-Wenzl morphism. It comes in two color-ﬂavors, as before.
Example 5.10. + +
+ +
=
+= = 1
x
1
xy−1
1
xy−1
x
xy−1
y
xy−1
JW 1 JW 2
JW 3
The coefﬁcients in these Jones-Wenzl projectors are ration al functions in the 2-
colored quantum numbers, as in Deﬁnition 3.5. When [m]x = [m]y = 0 , one can
show thatJW m−1 is well-deﬁned within Z[x,y ] (i.e. no denominators are necessary).
If either m is odd or if m is even and [m − 1] = 1 ,JW m−1 will be rotation-invariant
44 BEN ELIAS AND GEORDIE WILLIAMSON
(under color-preserving rotations). Ifm is even and [m−1] = 1 , it is also the case that
rotating the left-blue-aligned Jones-Wenzl morphism by on e strand yields the left-
red-aligned Jones-Wenzl morphism. If m is odd, this holds if and only if [m − 1]x =
[m − 1]y = 1; this is the feature behind the deﬁnition of a balanced reali zation. Using
the examples above, the reader should convince themselves o f these rotational facts
whenm = 4 (sinceastats = 2) or when m = 3 andast =ats = ±1. More discussion of
the non-balanced case is found in Section 5.6.
The Jones-Wenzl Soergel graph above is not technically a mor phism in D, because
it lives on the planar disc, but it can be plugged into another diagram to produce a
planar strip graph. This is done in relation (5.7), where the rotation-invariantJW m−1
is used. An implication of (5.7) and (5.6) is the following re lation.
(5.16)
m=5m=4
= = JWJW
Note that here and henceforth, we will only use JW m−1 whenms,t = m, which we
abbreviate asJW .
On the RHS of (5.16), we took the Jones-Wenzl in the two-color ed Temperley-Lieb
algebra, transformed it into a degree 2 Soergel graph on the disc, and then trans-
formed it again into a degree 0 endomorphism of a color-alternating Bott-Samelson
in D, by placing trivalent vertices on each side. This general pr ocedure can be ap-
plied to any two-colored crossingless matching, giving a ma p from the two-colored
Temperley-Lieb algebra to a certain endomorphism ring in D. This map is a homo-
morphism. becauseJW m−1 is idempotent inTL , the RHS of (5.16) is also idempotent.
The 2m-valent vertex is thus “half an idempotent.”
The deﬁning properties of the Jones-Wenzl projectors in TL correspond to the fol-
lowing two properties in Soergel graphs. The ﬁrst is that the coefﬁcient of a certain
graph is 1, as can be seen from the examples above. This is the graph whic h, when
trivalent vertices are attached to make a degree 0 morphism, becomes the identity
map. The second property is called death by pitchfork :
(5.17)
= 0JW
Now let us note some properties of any (m − 1,m − 1) crossingless matching,
transformed into a Soergel graph. When viewed as a degree +2 graph on the disc,
there will be a boundary dot on at least one of any m − 1 adjacent strands. When
viewed as a degree +0 endomorphism of a length m color-alternating object Bs ⊗
Bt ⊗... in D, it can be given a negative-positive decomposition . That is, we say the
initial width of the map is m, the number of strands on the boundary . Reading from
SOERGEL CALCULUS 45
bottom to top, we may ﬁrst apply all negative maps (i.e. botto m boundary dots,
merging trivalents, and caps) which are the maps which decre ase the width. Then
we can apply all positive maps (i.e. cups, splitting trivale nts, top boundary dots),
increasing the width back up to m. The morphism will factor through a length k
color-alternating object Bs ⊗Bt ⊗... for some k ≤ m which is the minimal width
reached. Whenever the crossingless matching is not the iden tity map, we have k <
m. These properties will be used in Chapter 7.
Remark 5.11. Consider the usual Temperley-Lieb category over a Z[z]-algebra where
[m] = 0 and [k] ⁄= 0 for 0 < k < m. Then the Temperley-Lieb algebra with k
strands is isomorphic to (an integral form of) the endomorph ism ring of the Uq(sl2)-
representationV ⊗k
