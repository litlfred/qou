---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
2 F oundations of the T ransport F unctor F ormalism 6
2.1 The Path 2-Groupoid of a Smooth Manifold . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Local Trivializations and Descent Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Smooth 2-Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Transport Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 T ransport 2-F unctors 12
3.1 Smooth Descent Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 Transport 2-Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3 Some Features of Transport 2-Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4 Curvature 2-Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4 T ransport 2-F unctors are Non-Abelian Gerbes 25
4.1 Diﬀerential Non-Abelian Cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2 Abelian Bundle Gerbes with Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.3 Non-Abelian Bundle Gerbes with Connection . . . . . . . . . . . . . . . . . . . . . . . . 36
4.4 2-Bundles with Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5 Surface Holonomy 46
5.1 Markings and Fundamental Bigons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2 Reduced Surface Holonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
5.3 Properties of Reduced Surface Holonomy . . . . . . . . . . . . . . . . . . . . . . . . . . 52
References 56
1 Introduction
Giraud introduced gerbes in order to achieve a geometrical unders tanding of non-abelian cohomology
[Gir71]. However, already abelian gerbes turned out to be interesting: Brylinski introduced the not ion
of a connection on an abelian gerbe, and showed that these represent classes in a c ertain diﬀerential
cohomology theory, namely Deligne cohomology [Bry93]. Deligne cohom ology in degree two has before
been related to two-dimensional conformal ﬁeld theory by Gaw¸ ed zki [Gaw88]. This relation is estab-
lished by means of the surface holonomy of a connection on an abelian gerbe, which provides a term
in the action functional of the ﬁeld theory.
Surface holonomy of connections on abelian gerbes is today well und erstood; see [Wal10, FNSW08]
for reviews. While deﬁnitions of connections on non-abelian gerbes have appeared [BM05, ACJ05], it
remained unclear what the surface holonomy of these connections is supposed to be, how it is deﬁned,
and how it can be used.
In the present article we propose a general and systematic appro ach to connections on non-abelian
gerbes, including notions of parallel transport and surface holono my. Our approach is general in the
sense that it works for gerbes whose band is an arbitrary Lie 2-gro upoid, and whose ﬁbres are modelled
by an arbitrary 2-category. Our approach is systematic in the sense that it is solely based on axioms
for parallel transport along surfaces, formulated in terms of gluin g laws and smoothness conditions.
The whole theory of connections on non-abelian gerbes is then deriv ed as a consequence.
In order to illustrate how this axiomatic formulation works we shall br ieﬂy review a corresponding
formulation in a more familiar setting, namely the one of connections o n ﬁbre bundles; see [SW09].
It shows that for a Lie group G the category of principal G-bundles with connection over a smooth
manifold X is equivalent to a category consisting of functors
F : P1(X) /d47/d47 G-Tor. (1.1)
These functors are deﬁned on the path groupoid P1(X) of the manifold X; its objects are the points
of X, and its morphisms are (certain classes of) paths in X. The functors (1.1) take values in the
category of G-torsors, i.e. smooth manifolds with a free and transitive G-action.
The correspondence between principal G-bundles with connection and functors (1.1) is established
by letting the functor F assign to points the ﬁbres of a given bundle, and to paths the corre sponding
parallel transport maps. The gluing laws of parallel transport are precisely the axioms of a functor.
The smoothness conditions of parallel transport are more involved; they can be encoded in the functors
(1.1) by requiring smooth descend data with respect to an open cover of X. Functors (1.1) with smooth
descend data are called transport functors with G-structure – they constitute an axiomatic formulation
of the parallel transport of connections in G-bundles.
In Sections 2 and 3 of the present article we generalize this axiomatic formulation to connections on
gerbes. Our formulation does not use any existing concept of a ger be with connection — such concepts
are an output of our approach. It is based on 2-functors deﬁned on the path 2-groupoid P2(X) of X,
with values in some “target” 2-category T ,
F : P2(X) /d47/d47 T . (1.2)
– 2 –
In Section 2.1 we review the path 2-groupoid: it is like the path groupo id but with additional 2-
morphisms, which are essentially ﬁxed-end homotopies between pat hs.
For example, if T is the 2-category of algebras (over some ﬁxed ﬁeld), bimodules, an d intertwiners,
a 2-functor (1.2) provides for each point x ∈ X an algebra F (x), which is supposed to be the ﬁbre
of the gerbe at the point x. Further, it provides for each path γ from x to y a F (x)-F (y)-bimodule
F (γ), which is supposed to be the parallel transport of the connection on that gerbe along the curve
parameterized by γ. Finally, it provides for each homotopy Σ between paths γ and γ′ an intertwiner
F (Σ) : F (γ) /d47/d47 F (γ′),
which is supposed to be the parallel transport of the connection on that gerbe along the surface
parameterized by Σ. The axioms of the 2-functor (1.2) describe ho w these parallel transport structures
are compatible with the composition of paths and gluing of homotopies . These axioms and all other
2-categorical structure we use can be looked up in [SW, Appendix A].
Apart from the evident generalization from functors to 2-functo rs, more work has to be invested into
the generalization of the smoothness conditions. Imposing smooth ness conditions relies on a notion of
local triviality for 2-functors deﬁned on path 2-groupoids. A 2-functor
F : P2(X) /d47/d47 T
is considered to be trivializable, if it factors through a prescribed 2- functor i : Gr /d47/d47 T , with
Gr a strict Lie 2-groupoid. The Lie 2-groupoid Gr plays the role of the “typical ﬁbre”, and the 2-
functor i indicates how the typical ﬁbre is realized in the target 2-category T . A local trivialization
of the 2-functor F is a cover of X by open sets Uα, a collection of locally deﬁned “trivial” 2-functors
trivα : P2(Uα) /d47/d47 Gr and of equivalences
tα :F |Uα
∼= /d47/d47i ◦ trivα
between 2-functors deﬁned on Uα. Local trivializations lead to descend data, generalizing the transition
functions of a bundle. The descent data of a 2-functor with a local trivialization consists of the 2-
functors trivα, of transformations
gαβ :i ◦ trivα /d47/d47 i ◦ trivβ
between 2-functors over Uα ∩Uβ, and of higher coherence data that we shall ignore for the purpos es
of this introduction. The theory of local trivializations and descent data for 2-functors is developed in
our paper [SW] and reviewed in Section 2.2.
The smoothness conditions we want to formulate are imposed with re spect to descent data; they
are the content of Section 3. First of all, we require that the 2-fun ctors trivα are smooth. This makes
sense since they take values in the Lie 2-groupoid Gr. For certain Lie 2-groupoids, a theory developed
in our paper [SW11] identiﬁes the smooth functors triv α with certain 2-forms Bα onUα — the curving
of the gerbe connection. In order to treat the transformations gαβ, we apply an observation in abstract
2-category theory: the transformations gαβ can be regarded as a collection of functors
F (gαβ) : P1(Uα ∩Uβ) /d47/d47 ΛT ,
for Λ T a certain category of diagrams in T . The smoothness condition that we impose for the trans-
formation gαβ is that the functors F (gαβ) are transport functors. According to the before-mentioned
– 3 –
correspondence between transport functors and ﬁbre bundles with connection, we thus obtain a smooth
ﬁbre bundle F (gαβ) with connection over two-fold overlaps Uα ∩Uβ — a signiﬁcant feature of a gerbe.
Summarizing this overview, our axiomatic formulation of connections on gerbes consists of transport
2-functors: 2-functors F : P2(X) /d47/d47 T that are locally trivializable with respect to a typical ﬁbre
i : Gr /d47/d47 T , and have smooth descent data.
In Section 4 of this article we test our axiomatic formulation by choos ing examples of target 2-
categories T and 2-functors i : Gr /d47/d47 T . In these examples the Lie 2-groupoids are “deloopings” of
strict Lie 2-groups, Gr = BG; these Lie 2-groups G play the same role for gerbes as Lie groups for
principal bundles. We ﬁnd the following results:
(i) For a general Lie 2-group G and the identity 2-functor
i = id BG : BG /d47/d47 BG
we prove (Theorem 4.1.6) that there is a bijection
h0TransBG(X, BG) ∼= ˆH 2(X, G)
between isomorphism classes of transport 2-functors and the de gree two diﬀerential non-abelian
cohomology of X with coeﬃcients in G. These cohomology groups have been explored in [BM05]
and [BS07]; they are an extension of Giraud’s non-abelian cohomology by diﬀerential form data.
Upon setting G = BS1 it reduces to Deligne cohomology.
(ii) The Lie 2-group BS1 has a monoidal functor BS1 /d47/d47 S1-Tor to the monoidal category of S1-
torsors, by sending the single objects of BS1 to S1 considered as a torsor over itself. Delooping
yields a 2-functor
i : BBS1 /d47/d47 B(S1-Tor).
We prove (Theorem 4.2.1) that there is an equivalence of 2-categor ies
TransBBS1(X, B(S1-Tor)) ∼=
{
S1-bundle gerbes with
connection over X
}
.
Bundle gerbes have been introduced by Murray [Mur96]. The equivale nce arises by realizing
that the transport functor F (gαβ) in the descent data corresponds in the present situation to an
S1-bundle with connection.
(iii) Let H be a Lie group and let AUT( H) be the automorphism 2-group of H. It has a monoidal
functor AUT(H) /d47/d47 H-BiTor to the monoidal category of H-bitorsors. Delooping yields a
2-functor
i : BAUT(H) /d47/d47 B(H-BiTor).
We prove (Theorem 4.3.1) that there is an equivalence of 2-categor ies
TransBAUT(H)(X, B(H-BiTor)) ∼=
{
Non-abelian H-bundle gerbes
with connection over X
}
.
Non-abelian bundle gerbes are a generalization of S1-bundle gerbes introduced in [ACJ05], and
the above equivalence arises by proving that the transport funct or F (gαβ) corresponds in the
present situation to a “principal H-bibundle with twisted connection”.
– 4 –
The relations (i) to (iii) show that all these existing concepts of gerb es with connection ﬁt into our
axiomatic formulation.
Apart from these relations to existing gerbes with connection, tra nsport 2-functors are able to
determine systematically new concepts in cases when only the targe t 2-category T and the 2-group G
are given. We demonstrate this in Section 4.4 with the examples of con nections on vector 2-bundles,
string 2-bundles, and principal 2-bundles.
Finally, we discuss in Section 5 the notion of parallel transport along s urfaces, which is manifestly
included in the concept of a transport 2-functor. We introduce a n otion of surface holonomy for
transport 2-functors, deﬁned for closed oriented surfaces wit h a marking, i.e. a certain presentation
of its fundamental group. It is obtained by evaluating the transpo rt 2-functor on a homotopy that
realizes the single relation in this presentation.
The existing notion of surface holonomy for abelian gerbes takes values in S1 [Gaw88, Mur96],
while our notion of surface holonomy takes values in the 2-morphisms of the target 2-category T . In
order to compare the two notions, we propose a “reduction” proc edure which can be applied in the
case that typical ﬁbre of the transport 2-functor is of the form i : BG /d47/d47 T , where G is a Lie 2-group.
The ﬁrst part of this procedure is the deﬁnition of an abelian group Gred which can be formed for
any Lie 2-group G (Deﬁnition 5.2.2). Heuristically, it generalizes the abelianization of an o rdinary Lie
group. As the second part of the reduction procedure, we show ( Proposition 5.2.5) that the surface
holonomy of every transport 2-functor with BG-structure can consistently be reduced to a function
with values in Gred.
Our main results in Section 5 concern this reduced surface holonomy of transport 2-functors with
BG-structure. We prove in Theorem 5.3.2 a rigidity result for reduced s urface holonomy, namely that
it depends only on the isomorphism class of the transport 2-functo r, and only on the equivalence
class of the marking. The isomorphism invariance allows us to transfe r the reduced surface holonomy
from transport 2-functors through the equivalences (i), (ii), an d (iii) described above. In particular,
we equip non-abelian G-gerbes with a well-deﬁned notion of a Gred-valued surface holonomy; such a
concept was not known before.
Finally, we show that our new concept of reduced surface holonomy is compatible with the existing
notion of S1-valued surface holonomy of abelian gerbes. Namely, in the case G = BS1 we ﬁnd for
the reduction ( BS1)red = S1, so that both concepts take values in the same set. We prove then in
Proposition 5.3.3 that the two concepts indeed coincide. Thus, our n ew notion of (reduced) surface
holonomy consistently extends the existing notion from abelian to no n-abelian gerbes.
Acknowledgements. The project described here has some of its roots in ideas of John Ba ez and in
his joint work with US, and we are grateful for all discussions and su ggestions. We are also grateful
for opportunities to give talks about this project at an unﬁnished s tate, namely at the Fields Institute,
at the VBAC 2007 meeting in Bad Honnef, at the MedILS in Split and at t he NTNU in Trondheim.
In addition, we thank the Hausdorﬀ Research Institute for Mathe matics in Bonn for kind hospitality
and support during several visits.
– 5 –
