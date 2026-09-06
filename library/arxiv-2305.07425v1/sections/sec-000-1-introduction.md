---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
A ﬁxed group G will admit many diﬀerent cobounded actions on diﬀerent hyperb olic metric
spaces. Abbott, Balasubramanya, and Osin in [ABO19] show th at the set of equivalence
classes of cobounded hyperbolic actions of a group G carries a natural partial order; see
Section 2.1. The resulting poset is called the poset of hyperbolic structures on G, denoted
H(G). Roughly speaking, one action is larger than another if the smaller space can be formed
by equivariantly collapsing some subspaces of the larger. T he motivation is that the larger
an action is in this partial order, the more information abou t the geometry of the group it
should provide.
The posets H(G) remain mysterious, especially for groups with features of non-positive
curvature, which tend to have uncountable posets of hyperbo lic structures [ABO19]. First
steps towards understanding these posets were made in [Bal2 0], [AR19], and [AR19b]. While
[Bal20] and [AR19b] give complete descriptions of H(G) for the groups in question, it appears
essentially impossible to do this, given current technolog y, for groups with strong features
of non-positive curvature. Nonetheless, one aspect of the p oset that can be understood in
many instances is the (non-)existence of a largest element of H(G), that is, an element that
is greater than or equal to every other element of the poset. W hen a largest element exists,
we say that the group G is H–accessible; otherwise, the group is H–inaccessible. The ﬁrst
and third authors show that many groups with features of non- positive curvature are H–
inaccessible [AR19b]. In this paper, we follow this directi on by extending these results to a
large class of 3-manifold groups.
We ﬁrst consider fundamental groups of non-geometric 3–man ifolds with empty or toroidal
boundary. If M is a compact, orientable, irreducible non-geometric 3-man ifold, then there
exists a non-empty minimal union T of disjoint essential tori in M such that each connected
component of M \ T is Seifert ﬁbered or hyperbolic. This is called the torus decomposition
of M , and the connected components of M \ T are called pieces. Our ﬁrst result shows
that if M contains certain types of pieces, then π1(M ) is H–inaccessible. To describe these
pieces, we introduce the class of non-elementary Seifert ﬁbered manifolds, which are those
whose base orbifolds are orientable and hyperbolic. Non-el ementary graph manifolds are
Date: May 15, 2023.
2010 Mathematics Subject Classiﬁcation. 57M50, 20F65, 20F67.
1
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 2
those whose Seifert pieces are non-elementary, and a mixed m anifold is non-elementary if all
of its Seifert ﬁbered pieces and maximal graph manifold comp onents are non-elementary. Any
graph manifold or Seifert ﬁbered manifold is ﬁnitely covere d by a non-elementary one. See
Section 4 for a more in-depth discussion.
Theorem 1.1. LetM be a non-geometric 3-manifold with empty or toroidal bounda ry. If the
torus decomposition of M contains any of the following, then π1(M ) is H–inaccessible:
(1) a hyperbolic piece which contains a boundary torus of M ;
(2) two hyperbolic pieces glued along a torus;
(3) an isolated non-elementary Seifert ﬁbered piece; or
(4) a non-elementary maximal graph manifold component.
We note a straightforward corollary of Theorem 1.1.
Corollary 1.2. IfM is one of the following types of 3-manifolds, then π1(M ) is H–inaccessible:
(a) a ﬁnite non-trivial connected sum of ﬁnite volume cusped hyperbolic 3-manifolds;
(b) a non-elementary mixed manifold.
Proof. Part (a) follows from Theorem 1.1(1). For part (b), observe t hat a mixed manifold
must contain either: two hyperbolic pieces glued along a tor us, an isolated non-elementary
Seifert ﬁbered piece, or a non-elementary graph manifold co mponent with boundary. In these
cases, we apply Theorem 1.1 (2), (3), or (4), respectively. □
The ﬁrst and third author give a straightforward criterion t o show that a group is H–
inaccessible [AR19, Lemma 1.4]; see Lemma 2.3. In this paper , we show in Lemma 4.3 that if
a peripheral subgroup of a relatively hyperbolic group sati sﬁes this criterion, then the group
itself also satisﬁes the criterion. There is a natural relat ively hyperbolic structure on π1(M ) in
which the peripheral subgroups are fundamental groups of ce rtain tori, Seifert ﬁbered pieces,
and graph manifolds. The proof Theorem 1.1 proceeds by showi ng that, in each case, there is
a peripheral subgroup that is H–inaccessible because it satisﬁes Lemma 2.3, and then apply ing
Lemma 4.3. The key step is the following theorem.
Theorem 1.3. If M is a non-elementary graph manifold or a non-elementary Seif ert ﬁbered
manifold, then π1(M ) is H–inaccessible.
Theorem 1.3 generalizes [AR19, Theorem 1.1], in which the ﬁr st and third authors show
that ﬂip graph manifold groups, a special class of graph mani fold groups, are H–inaccessible.
The class of non-elementary graph manifold groups belongs t o a larger class of graphs of
groups called Croke-Kleiner admissible groups that were introduced by Croke and Kleiner in
[CK02]. Roughly speaking, Croke-Kleiner admissible group s are modeled on the JSJ structure
of graph manifolds where the (fundamental groups of the) Sei fert ﬁbered pieces are replaced
by central extensions G of general hyperbolic groups H:
1 →Z(G) = Z →G →H → 1.
In some sense, Croke-Kleiner admissible groups are the simp lest interesting groups con-
structed algebraically from a ﬁnite number of hyperbolic gr oups. The H–inaccessibility of
non-elementary graph manifold groups follows from the foll owing result for Croke-Kleiner
admissible groups.
Theorem 1.4. Every Croke-Kleiner admissible group has a subgroup of index at most 2 which
is H–inaccessible.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 3
A non-geometric 3-manifold M always has a double cover in which all Seifert ﬁbered pieces
are non-elementary, and hence passing to a further ﬁnite cov er if necessary, we obtain a ﬁnite
coverM ′ →M such that M ′ is either a non-elementary graph manifold or a non-elementa ry
mixed manifold. Combining Theorems 1.1 and 1.3 yields the fo llowing corollary.
Corollary 1.5. If M is a non-geometric 3-manifold then π1(M ) has a ﬁnite index subgroup
H such that every ﬁnite index subgroup K ≤H is H–inaccessible.
So far, we have only discussed non-geometric 3–manifolds. I n some cases, we can also
