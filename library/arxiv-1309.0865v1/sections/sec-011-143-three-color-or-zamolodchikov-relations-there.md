---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-011-143-three-color-or-zamolodchikov-relations-there
section_title: "Three color or “Zamolodchikov” relations: There is one relation for each ﬁnite par-"
section_number: 1.4.3
pages: 8-10
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
abolic subgroup of rank 3, generalizing the so-called Zamol odchikov tetrahedron
equation. We feel this interesting topic deserves some intr oduction of its own. In
braided monoidal categories a fundamental role is played by the Yang-Baxter equa-
tion or braid relation, which guarantees that one obtains an action of the braid group
on the tensor powers of any object. In the setting of braided m onoidal 2-categories,
the role of the Yang-Baxter equation is played by the Yang-Ba xter isomorphism, and
the consistency relation between these isomorphisms is kno wn as the Zamolodchikov
tetrahedron equation.1 Instead of describing this theory in its original context, w e give
a description using the combinatorics of Coxeter groups.
1There are also higher Zamolodchikov relations governing br aided monoidal n-categories. These
will not be considered in this paper.
SOERGEL CALCULUS 9
Consider a Coxeter system W of type A3 with simple reﬂections s,t,u such that s
andu commute. The vertices of the following graph encode the redu ced expressions
for the longest element w0 of W , and the edges indicate the application of a braid
relation (the dashed lines correspond to the “boring” braid relationssu ↔us):
stsuts stusts
tstuts stutst
tsutus sutust
tsutsu tustus
tustsu
sutsut ustust
ustsut
tutstu utstut
utustu utsutu
In the setting of braided monoidal 2-categories each vertex encodes a 1-morphism,
and each edge gives a 2-morphism between these 1-morphisms ( or rather, each edge
gives a pair of inverse 2-isomorphisms), so that a path gives a 2-morphism by com-
position. It is an easy consequence of the axioms for braided monoidal 2-categories
that the two dashed squares commute. The Zamolodchikov tetr ahedron equation
is the requirement that the 2-morphism obtained by followin g a non-trivial loop
around this graph is the identity 2-morphism.
For any element w ∈ W of type An, one can draw a “reduced expression graph”
as above, and obtain a 2-morphism for any path in this graph. T he Zamolodchikov
relation is already sufﬁcient to imply that any non-trivial loop yields the identity
morphism, which explains its great importance. In fact, for any element of any Cox-
eter group, the loops in its reduced expression graph are (in a suitable sense) gen-
erated by the loops in the reduced expression graph of the lon gest element in any
ﬁnite parabolic subgroup of rank 3. Thus, in addition to the A3 Zamolodchikov re-
lation discussed above, there are Zamolodchikov-style rel ations in type B3,H3, and
A1 ×I2(m) form< ∞ (though in typeA1 ×I2(m) things are not very exciting, which
is why we ignored A1 ×A2 andA1 ×A1 ×A1 in the type An discussion earlier).
Let us explain how analogous relations arise for morphisms between Bott-Samelson
bimodules. A vertex w of a reduced expression graph is associated with a Bott-
Samelson bimodule Bw, and edges give morphisms ( 2mst-valent vertices) between
these bimodules. Unlike the Yang-Baxter situation, the edg es are not isomorphisms
(unlessmst = 2), but are only projections to a common summand, so that one sh ould
not expect a loop to be equal to the identity . For general reas ons (which will be
discussed later in this paper), two paths with the same start and endpoint will be
equal “modulo lower terms,” i.e. modulo morphisms which fac tor throughBy for a
sequencey strictly shorter than w.
What is miraculous (and currently lacking a satisfying expl anation) is that, for
A3 andB3 (and more trivially , for A1 ×I2(m)), one can choose an “orientation” on
