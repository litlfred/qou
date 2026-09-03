---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-001-categorical-data
section_title: "Categorical data"
section_number: null
pages: 3-5
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
defect surfaces of genusg≥ 1, but only for the simple categorical data underlying Dijkgraaf-Witten models
[DW90]. Here, we consider spherical fusion categoriesVecG and VecG′ of graded vector spaces over finite
groupsG,G′, equipped with trivial cocycles, and bimodule categories defined by finite transitiveG×G′op-sets,
also equipped with the trivial cocycle. For this data, it is simple to compute the state sums of a 3-manifold
M = [0, 1]× Σ and of a 3-ball with a defect surfaceΣ of general genus in the interior. This shows that the
state sum detects properties of the bimodule categories labeling the defect surface as well as its genus.
We also compute the state sum for a 3-sphere with an embedded torus labeled by a trivialG-set and show
that it gives the number of conjugacy classes of group homomorphisms from the fundamental group of its
complement intoG. This shows that the state sum is sensitive to the embedding of the surface.
Our last examples are framed links or ribbon links. They are realised as defect graphs on trivial defect surfaces
that are labeled by a spherical fusion categoryC as a bimodule category over itself. In this case, bimodule
functors labeling defect lines and bimodule natural transformations labeling defect vertices correspond to
objects and morphisms of the categorical centreZ(C).
In this setting, ribbons or framed links can be realised in two ways. The first is a ribbon diagram on a defect
surface, in which line segments are labeled by objects ofZ(C) and crossings are viewed as defect vertices
labeled by braidings. The second is an embedded ribbon link labeled by objects ofZ(C) without vertices.
We show that in both cases, the state sum is the product of the evaluation of the ribbon link with the usual
Turaev-Viro-Barrett-Westbury state sum for the manifold without defects. This reproduces the results by
Turaev and Virelizier [TV10, TV17] on ribbon links in graph TQFTs.
Structure of the article
In Section 1 we introduce the categorical data for the state sum model and summarise the relevant background
from the literature.
Section 2 develops the diagrammatic calculus underlying generalised 6j symbols. After recalling diagrams
for spherical fusion categories and pivotal 2-categories, we introduce mixed diagrams, in which diagrams for
spherical fusion categories overlap with diagrams labeled by bimodule functors and natural transformations.
By labeling segments and line endpoints at their boundaries with objects and morphisms in bimodule
categories we then obtain the polygon diagrams that are the building blocks of the state sum.
In Section 3 we show that these polygon diagrams satisfy the usual cutting and gluing identities for polygon
presentations of surfaces.
3
The state sum of a triangulated 3-manifold with defect surfaces, defect lines and defect points is introduced
in Section 4. After discussing the labeling of defects and of the triangulation with algebraic data, we define
the generalised 6j symbol of a tetrahedron with defects. We then introduce the state sum, which reduces
to the usual Turaev-Viro Barrett-Westbury state sum in the absence of defects, and show that it can be
computed by gluing 3-manifolds with defects.
In Section 5 we establish the triangulation independence of the state sum. We first summarise some background
from PL topology and introduce certain neighbourhoods of defect surfaces required for our constructions. We
then prove that the state sum of a 3-ball bisected by a defect disc is the evaluation of the polygon diagram
obtained by projecting the dual graph of the boundary triangulation on the disc. This implies that the
state sum is invariant under bistellar moves that involve only generic transversal tetrahedra. We then prove
triangulation independence by refining the triangulation and decomposing it into neighbourhoods of defect
surfaces and 3-manifolds without defects.
In Section 6 we compute examples and discuss the results.
1 Categorical data
1.1 Spherical fusion categories
We work overC and follow the conventions of Etingof et al. in [EGNO]. A multitensor categoryis a
locally finite, C-linear abelian rigid monoidal categoryC with a tensor product⊗ :C×C→C that is bilinear
on the morphisms. Atensor categoryis an indecomposable multitensor category withEndC(e)∼= C, where
e is the tensor unit. A(multi)fusion categoryis a finite semisimple (multi)tensor category.
For all categoriesC we denote byCop the opposite category and for all monoidal categoriesC byCrev the
categoryC with the opposite monoidal structure. We define aleft rigidmonoidal category as a category in
which every objectx has a left dualx∗ and evaluation and coevaluation morphisms
evL
x :x∗⊗x→e, coevL
x :e→x⊗x∗ (1)
that satisfy the identities
(1x⊗ evL
x )◦ (coevL
x⊗ 1x) = 1x (evL
x⊗ 1x∗)◦ (1x∗⊗ coevL
x ) = 1x∗, (2)
up to associators and unit constraints. We denote by∗ :C→C op,rev the induced monoidal functor, see the
end of Section 2.10 in [EGNO]. Apivotal monoidal categoryC is a left rigid monoidal categoryC with a
monoidal isomorphismω :∗∗⇒ idC. Every pivotal category is right rigid with
evR
x = evL
x∗◦ (ω−1
x ⊗ 1x∗) :x⊗x∗→e, coevR
x = (1x∗⊗ω)◦ coevL
x∗ :e→x∗⊗x, (3)
and the left and right trace of a morphismα∈ EndC(x) are given by
trL(α) = evL
x◦ (1x∗⊗α)◦ coevR
x, trR(α) = evR
x◦ (α⊗ 1x∗)◦ coevL
x. (4)
A pivotal categoryC is spherical if trL(α) = trR(α) for all endomorphismsα inC. In this case we write
tr(α) = trL(α) = trR(α) and dim(x) = tr(1x) = tr(1x∗) = dim(x∗) for allα∈ EndC(x) and x∈ ObC. The
dimension of a spherical fusion categoryC is
dim(C) =
∑
i∈I
dim(i)2, (5)
where I is a set of representatives of the isomorphism classes of simple objects.
Example 1.1. [EGNO, Ex. 2.3.6]
LetG be a finite group andω :G×G×G→ C× a normalised 3-cocycle. The fusion categoryVecω
G has
• as objects finite-dimensionalG-graded vector spacesV =⊕g∈GVg,
• as morphisms linear mapsf :V →W with f(Vg)⊂Wg for allg∈G,
• simple objectsδg for g∈G with (δg)g = C and (δg)h = 0 for g̸=h,
• the tensor productV⊗W =⊕g∈G(⊕hk=gVh⊗Wk),
4
• the associator given byaδg,δh,δk =ω(g,h,k )idδghk on the simple objects,
• dual objectsV∗ =⊕g∈GV∗
g−1 with the usual (co)evaluation for finite-dimensional vector spaces,
• pivotal structures that are in bijection with charactersκ :G→ C×.
A pivotal structure is spherical iffκ(g)∈{ 1,−1} for allg∈ G. In particular, the trivial characterκ≡ 1
determines a spherical structure onVecω
G, itsstandard spherical structure.
