---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in represent"
section_id: sec-001-2-self-equivalences
section_title: "Self-equivalences"
section_number: 2
pages: 1-2
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
doc_brief: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in representation theory, for co"
---
them possess some interesting structure.
Let W be a Coxeter group and C a triangulated category. We consider gradually stronger
actions of W or its braid group BW :
(i) W acting on K0(C)
(ii) a morphism from BW to the group of isomorphism classes of invertible functors of C
(iii) an action of BW on C.
We construct a strict monoidal category BW categorifying (conjecturally) BW and we propose
an even stronger form of action :
(iv) a morphism of monoidal categories BW → Hom(C, C)
The ﬁrst section is devoted to a construction of a self-equivalence of a triangulated category,
generalizing various constructions in representation theory and a lgebraic geometry. This should
be viewed as a categoriﬁcation of an action of Z/2.
In section §3, we construct a monoidal category categorifying (a quotient of ) the braid group.
It is a full subcategory of a homotopy category of complexes of bim odules over a polynomial
algebra. The setting here is that of Soergel’s bimodules.
Section §4 is devoted to the category O of a semi-simple complex Lie algebra. There are
classical functors that induce an action of type (i). We show how to use the constructions of
§3, via results of Soergel, to get a genuine action of the braid group a nd even the stronger type
(iv).
The case of ﬂag varieties is considered in §5. There again, there is a classical action up to
isomorphism of the braid group on the derived category of constru ctible sheaves (type (ii)).
Using a result of Deligne and checking some compatibilities for general kernel transforms (Ap-
pendix in §6), one gets a genuine action of the braid group (type (iii)). Now, us ing the link
with modules over the cohomology ring, we get another proof of this and even the stronger (iv).
In a work in preparation we study presentations by generators an d relations, homological
vanishings and relation with the cohomology of Deligne-Lusztig variet ies.
A few talks have been given in 1998–2000 on the main results of this wo rk (Freiburg, Paris,
Yale, Luminy) and I apologize for the delay in putting them on paper.
I would like to thank I. Frenkel, M. Kashiwara, M. Khovanov and W. So ergel for useful
discussions.
Date: Septembre 2004.
1
2 RAPHA ¨EL ROUQUIER
2. Self-equivalences
We describe a categoriﬁcation of the notion of reﬂection with respe ct to a subspace. The
ambient space is K0 of a triangulated category, the subspace is another triangulated category
and the embeddings and projections are given by functors. We act ually allow an automorphism
of the “subspace” category, which allows to categorify the q-analog of a reﬂection.
We present here how a functor from a given triangulated category gives rise to a self-
equivalence of that category, when the functor satisﬁes some co nditions. Then, we give three
special “classical” cases. The ﬁrst one concerns constructible sh eaves on a P1-ﬁbration (it oc-
curs typically with ﬂag varieties, cf §5). The second one deals with the case where the target
category is the derived category of vector spaces, where we rec over the theory of spherical ob-
jects and twist functors (it arises as counterparts of Dehn twist s via mirror symmetry). The
last application essentially concerns derived categories of ﬁnite dime nsional algebras (it occurs
in particular within rational representation theory, cf §4).
All functors between additive (resp. triangulated) categories ar e assumed to be additive
(resp. triangulated).
Given an additive category C, we denote by K(C) the homotopy category of complexes of
objects of C.
Given an algebra A over a ﬁeld k, we denote by A-mod the category of ﬁnitely generated left
A-modules. We put Aen = A ⊗k Aopp, where Aopp is the opposite algebra.
Given a graded algebra A, we denote by A-modgr the category of ﬁnitely generated graded
A-modules.
