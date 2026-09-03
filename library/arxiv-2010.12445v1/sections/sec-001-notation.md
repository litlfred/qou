---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-001-notation
section_title: "Notation"
section_number: null
pages: 3-4
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect"
---
In this paper we work over a base commutative, associative ri ng R with unity. If not stated
otherwise a ﬁber category will be a category ﬁbered in groupo ids over Aﬀ /R , the category of
aﬃne schemes over Spec R, or, equivalently, the opposite of the category of R-algebras. An fpqc
stack will be a stack for the fpqc topology.
A map f : X ′ − → X of ﬁbered categories is called representable if for all maps T − → X from
an aﬃne scheme (or an algebraic space) the ﬁber product T ×X X ′ is (equivalent to) an algebraic
space.
Given a ﬂat and aﬃne group scheme G overR we denote by B RG (or simply B G when the
base ring is clear) the stack of G-torsors for the fpqc topology, which is an fpqc stack with aﬃne
diagonal. When G − →SpecR is ﬁnitely presented (resp. smooth) then B RG coincides with the
stack of G-torsors for the fppf (resp. étale) topology.
By a “subcategory” of a given category we mean a “full subcate gory” if not stated otherwise.
We assume the notations, deﬁnition and results of [ Ton20, Section 1]. In particular: the notion
of pseudo-algebraic and quasi-compact ﬁbered categories o r maps between them; ﬂat maps of
ﬁbered categories; quasi-coherent sheaves and their funct oriality; quasi-coherent sheaves on a
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 4
ﬁbered category. In particular QCoh (X ) and QAlg (X ) denotes the category of quasi-coherent
sheaves and quasi-coherent algebras on X respectively.
If Yi fori ∈I is a set of ﬁbered categories over R then ⊔iYi is deﬁned as the ﬁbered category
overR whose objects over an R-algebraA are tuples consisting of a decomposition Spec A = ⊔iUi
into open and closed subsets and yi ∈ Y i(Ui). In particular if X is a ﬁbered category with maps
Yi → X then a map
⨆
i∈I
Yi → X
is well deﬁned provided that X is a Zariski stack.
If E is a vector bundle over a category ﬁbered in groupoids X then the locus Xn → X where
E has rank n is an open and closed immersion. Moreover there is a map X → ⊔ nXn (which is an
equivalence if X is a Zariski stack) and if X is quasi-compact, then all Xn are empty but ﬁnitely
many.
If E is a vector bundle on a ﬁbered category X we can deﬁne det E as
det E = (
⨁
n∈N
Λ n(E|Xn))|X
which is compatible with the usual notion of determinant for vector bundles of ﬁxed rank.
