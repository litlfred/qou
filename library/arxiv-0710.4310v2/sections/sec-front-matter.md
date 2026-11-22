---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
arXiv:0710.4310v2  [math.DG]  20 Jul 2008
On Two-Dimensional Holonomy
Jo˜ao Faria Martins
Centro de Matem´atica da Universidade do Porto
Rua do Campo Alegre, 687, 4169-007 Porto, Portugal
jmartins@math.ist.utl.pt
Roger Picken
Departamento de Matem´atica,
Instituto Superior T´ecnico, TU Lisbon
Av. Rovisco Pais, 1049-001 Lisboa, Portugal
rpicken@math.ist.utl.pt
November 8, 2018
Abstract
We deﬁne the thin fundamental categorical group P2(M, ∗) of a based
smooth manifold (M, ∗) as the categorical group whose objects are rank-1
homotopy classes of based loops on M, and whose morphisms are rank-
2 homotopy classes of homotopies between based loops on M. Here two
maps are rank-n homotopic, when the rank of the diﬀerential of the homo-
topy between them equals n. Let C(G) be a Lie categorical group coming
from a Lie crossed module G = (∂: E →G, ⊲). We construct categorical
holonomies, deﬁned to be smooth morphisms P2(M, ∗) →C(G), by using
a notion of categorical connections, being a pair (ω, m), where ω is a con-
nection 1-form on P, a principal G bundle over M, and m is a 2-form on
P with values in the Lie algebra of E, with the pair (ω, m) satisfying suit-
able conditions. As a further result, we are able to deﬁne Wilson spheres
in this context.
Key words and phrases non-abelian gerbe; 2-bundle, two-dimensional holon-
omy; crossed module; categorical group; Wilson sphere
2000 Mathematics Subject Classiﬁcation 53C29 (primary); 18D05 (sec-
ondary)
1
Contents
1
Preliminaries
4
1.1
Resum´e of results and notation from the theory of principal ﬁbre
bundles
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.1.1
Connections on principal ﬁbre bundles . . . . . . . . . . .
4
1.1.2
Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.1.3
Parallel transport . . . . . . . . . . . . . . . . . . . . . . .
6
1.1.4
The dependence of the parallel transport on a smooth
family of curves - the Ambrose-Singer theorem
. . . . . .
6
1.2
Crossed modules . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
1.2.1
Crossed modules and categorical groups . . . . . . . . . .
11
1.3
The thin fundamental categorical group of a manifold
. . . . . .
12
1.3.1
1-Tracks . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
1.3.2
2-Tracks . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.3.3
Horizontal and vertical compositions of 2-tracks . . . . . .
14
1.3.4
Deﬁnition of the thin fundamental categorical group of a
smooth manifold . . . . . . . . . . . . . . . . . . . . . . .
15
1.3.5
The thin fundamental crossed module of a smooth manifold 15
1.3.6
Two exact sequences . . . . . . . . . . . . . . . . . . . . .
16
2
Two-dimensional holonomies
17
2.1
Categorical connections
. . . . . . . . . . . . . . . . . . . . . . .
17
2.2
The 2-curvature 3-form of a G-categorical connection . . . . . . .
18
2.2.1
Algebraic preliminaries . . . . . . . . . . . . . . . . . . . .
18
2.2.2
The 2-structure equation
. . . . . . . . . . . . . . . . . .
19
2.2.3
The 2-Bianchi identity . . . . . . . . . . . . . . . . . . . .
20
2.2.4
Local form of a categorical connection . . . . . . . . . . .
20
2.3
Categorical holonomy
. . . . . . . . . . . . . . . . . . . . . . . .
22
2.3.1
Deﬁnition of a holonomy.
. . . . . . . . . . . . . . . . . .
22
2.3.2
Deﬁnition of a categorical holonomy . . . . . . . . . . . .
23
2.4
Categorical connections and categorical connection holonomies
.
25
2.4.1
Deﬁning a categorical holonomy from a categorical con-
nection
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.4.2
A well-known lemma . . . . . . . . . . . . . . . . . . . . .
27
2.4.3
The dependence of the surface holonomy on a smooth
family of surfaces . . . . . . . . . . . . . . . . . . . . . . .
27
2.4.4
Re-scaling . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
2.4.5
Veriﬁcation of the axioms for a categorical holonomy . . .
34
2.4.6
2-Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.5
Wilson Spheres . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
2.5.1
The dependence of a categorical connection holonomy on
the elements of the ﬁbre
. . . . . . . . . . . . . . . . . .
39
2.5.2
The dependence of a categorical connection holonomy on
the point in the principal bundle . . . . . . . . . . . . . .
40
2.5.3
Associating 2-holonomies to embedded spheres . . . . . .
41
2
3
Appendix: Technical Lemmas
43
Introduction
Categoriﬁcation is an inﬂuential idea in many areas of mathematics, and in
geometry it is natural to try and think about categorifying the notions of holon-
omy and parallel transport in terms of higher categorical generalisations of the
notions of loop, Lie group and connection on a principal bundle, in the spirit
of Baez and Schreiber [B, BS]. In this article we construct a framework for
2-dimensional, or surface, holonomy along such lines. The based loops on a
manifold M are replaced by what we call the (strict) thin fundamental cate-
gorical group of M, P2(M, ∗), a monoidal category whose objects are rank-1
homotopy classes of based loops on M and whose morphisms are rank-2 ho-
motopy classes of homotopies between based loops (or 1-parameter families of
loops). Here, rank-1 homotopy, at the level of loops, means that the loops are
homotopic in such a way that the rank of the diﬀerential of the homotopy be-
tween them is less than or equal to 1, i.e. the homotopies between loops do not
sweep out area. Similarly, at the level of morphisms, two homotopies between
based loops are rank-2 homotopic, if they themselves are homotopic in such
a way that the rank of the diﬀerential of the homotopy between them is less
than or equal to 2, i.e. the homotopy between homotopies does not sweep out
volume. For precise deﬁnitions, we refer to subsections 1.3.1 and 1.3.2. The Lie
group is replaced by a categorical Lie group, C(G), naturally obtained from a
crossed module of Lie groups G = (∂: E →G, ⊲). The connection on a princi-
pal G-bundle P over M is replaced by what we call a categorical connection,
consisting of a connection 1-form on P with values in g, the Lie algebra of G,
together with a 2-form on P with values in e, the Lie algebra of E, satisfying
some conditions including the well-known “vanishing of the fake curvature”.
Locally these conditions correspond to Baez and Schreiber’s [BS] local formu-
lation for a 2-connection. The Maurer-Cartan structure equation and Bianchi
identity for the curvature of an ordinary connection are shown to have natural
analogues for the curvature 3-form of the categorical connection. Also a variant
of the Ambrose-Singer theorem (which plays a crucial role in our construction
of categorical holonomy) generalises to a higher-order version.
A categorical holonomy is deﬁned to be a (strict monoidal) smooth functor
from P2(M, ∗) to C(G). The main result that we prove (Thm. 39) is how a
categorical connection gives rise to a categorical holonomy.
The underlying
geometrical idea is to lift the 1-parameter family of loops into P, horizontally in
one direction, namely the direction along the loops, and to use this lift to pull
back the forms of the categorical connection, which are then integrated suitably.
Note that the appearance of a principal G-bundle P with a connection is
natural in the context of categorical holonomies. This is because, at the level of
the set of objects of P2(M, ∗), i.e. π1
1(M, ∗), the thin homotopy classes of based
loops on M, any smooth functor P2(M, ∗) →G gives rise to a smooth group
morphism π1
1(M, ∗) →G, and therefore it deﬁnes a principal G-bundle over M
3
with a connection [CP, MP].
The whole construction is carried out using the language and methods of dif-
ferential geometry and principal bundles, thereby avoiding working with inﬁnite-
dimensional path spaces, which was an approach taken in [BS]. The construction
is coordinate-free from the outset, since we use forms deﬁned on P. We remark
that the construction of P2(M, ∗) is of interest in its own right in deﬁning a
strict thin fundamental categorical group of a manifold (previously only a weak
version was known). This part of our construction is very similar to that of
[BHKP, HKK].
We study the relation between our construction and non-abelian gerbes, as in
[BrMe], and 2-bundles, as in [BS], in 2.4.6. Note that each 2-bundle with struc-
ture 2-group coming from a crossed module of the form (Ad: G →Aut(G), ⊲),
where ⊲denotes the obvious left action of Aut(G) in G, is naturally a non-abelian
gerbe. Let G = (∂: E →G, ⊲) be a Lie crossed module. Our construction cor-
responds to a particular case of G-2-bundles, for which the E-valued transition
functions are trivial, and therefore the G-valued transition functions satisfy the
usual cocycle condition for a principal G-bundle.
Although G-2-bundles are
a natural way to approach two-dimensional holonomy, we emphasise that our
main goal is the deﬁnition of categorical group maps P2(M, ∗) →C(G). This is
a very strong condition, and we argue that it should force the G-2-bundle with
connection to be of the special form considered here - see 2.4.6 where this point
is elaborated.
At the end of this article we deﬁne the notion of Wilson sphere, which means
that a categorical holonomy, taking values in the kernel of ∂: E →G, can be
associated to embedded spheres in a manifold, up to acting by an element of
the group G.
