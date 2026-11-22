---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
1. Introduction
Geometric approaches to the representation theory of Lie groups G are intimately linked with
the study of D-modules. For example, Harish Chandra established his celebrated regularity results
for distributional characters of admissible representations of real reductive groups by showing that
they satisfy an adjoint-equivariant regular holonomic system of diﬀerential equations. The resulting
D-module is the fundamental example of a character sheaf in the sense of Lusztig and also is the
basic object in Springer theory.
In another direction, Harish Chandra introduced (g, K)-modules to capture the underlying al-
gebraic structure of representations of real reductive groups while avoiding the analytic intricacies
involving function spaces. In turn, Beilinson-Bernstein opened the study of (g, K)-modules to the
powerful sheaf-theoretic techniques of algebraic geometry by establishing a localization theorem
identifying them with K-equivariant D-modules on the ﬂag variety G/B. (More precisely, repre-
sentations with strictly trivial inﬁnitesimal character are identiﬁed with D-modules on G/B, while
representations with generalized trivial inﬁnitesimal character correspond to unipotent monodromic
D-modules on G/N.) Other fundamental categories in representation theory of reductive groups,
such as the highest weight representations of Category O, are similarly equivalent to categories of
(possibly monodromic) D-modules on ﬂag varieties and related spaces.
Going one step further, the natural symmetries of representations, such as the intertwining oper-
ators for principal series representations, correspond to integral transforms acting on D-modules. In
the most basic instance of this, the collection of all integral transforms acting on D-modules on the
ﬂag variety G/B forms the Hecke category of Borel biequivariant D-modules on G. Composition
of integral transforms, geometrically described by convolution of integral kernels, equips the Hecke
category with a monoidal structure which categoriﬁes the classical Hecke algebra associated to the
Weyl group of G. Moreover, other fundamental categories of representations, such as categories of
(g, K)-modules and Category O, are naturally module categories for the Hecke category.
Our main results relate these two classes of categories: on the one hand, the Harish Chandra
system and other character sheaves, and on the other hand, the Hecke category and its module
categories. We ﬁrst establish that the Hecke category, along with its monodromic variant, satis-
ﬁes categoriﬁed analogues of the fundamental properties of the ﬁnite Hecke algebra. Namely, the
Hecke category is a two-dualizable Calabi-Yau monoidal category as the ﬁnite Hecke calgebra is a
ﬁnite-dimensional semi-simple symmetric Frobenius algebra. We then calculate that the monoidal
(Drinfeld) center and trace of the Hecke category, as well as those of its monodromic variant, are
identiﬁed with Lusztig’s unipotent character sheaves. It follows that dualizable Hecke module cate-
gories have characters which are character sheaves, a categoriﬁcation of Harish Chandra’s theory of
characters. (It is possible to go further and apply this perspective to give a geometric construction
of the Harish Chandra characters themselves.)
The technical setting for our work is that of homotopical algebra and derived algebraic geometry.
We apply the powerful tools of this rapidly developing subject to show that operations on the
“function spaces” of algebraic analysis, namely categories of D-modules, are representable by integral
transforms and to analyze the algebraic structure of these operations.
Our main results are perhaps best understood in the framework of extended topological ﬁeld
theory, using Lurie’s proof of the Cobordism Hypothesis [L3]. We explain that there is a topological
ﬁeld theory (TFT), which we call the character theory, that organizes much of the geometric repre-
sentation theory associated to G. (In work in progress with Sam Gunningham, we plan to construct
2
a family of TFTs parametrized by central character – the “moduli of vacua” of the theory – of which
the unipotent character theory discussed here is the ﬁber over the trivial parameter.) The character
theory can be viewed as an extended 3-dimensional TFT, deﬁned on 0, 1 and 2-dimensional mani-
folds, or alternatively, as a categoriﬁed 2-dimensional TFT. It assigns to a point the Hecke category
itself (viewed as an object in a higher Morita category of monoidal categories), or equivalently, its
2-category of modules. It assigns to a circle the category of unipotent character sheaves, which thus
carries the rich operadic structure of TFT (such as a ribbon tensor structure). Moreover, the Koszul
duality of Hecke categories, exchanging the equivariant and monodromic variants, implies that the
character theory satisﬁes a Langlands duality. This can be viewed as a dimensionally reduced form
of the geometric Langlands conjecture, or as S-duality for a maximally supersymmetric gauge theory
in three dimensions.
The remainder of the Introduction is organized as follows. After a brief summary of notation
and conventions, in Section 1.1, we state our main results, summarized in Theorem 1.8, from
the perspective of representation theory; in Section 1.2, we discuss the underlying techniques of
homotopical algebra for D-modules; and in Section 1.3, we explain how our results ﬁt into the
framework of topological ﬁeld theory. Finally, in Section 1.4, we propose a natural extension of the
results of this paper to the context of twisted D-modules.
Notation and conventions. Throughout the paper, G will denote a complex reductive group with
Lie algebra g. We choose a Borel subgroup B ⊂G with unipotent radical N ⊂B. We denote by
H = B/N the universal Cartan torus with Lie algebra h.
We also adopt the following idiosyncratic notation: we write G/ad G to denote the adjoint quotient,
or in other words, the quotient of G by itself acting by conjugation. More generally, for a subgroup
H ⊂G, we will write G/ad H to denote the quotient of G by the subgroup H acting by conjugation.
In this way, we can write G/ad B and not confuse the quotient with the ﬂag variety G/B.
Since our methods and results will involve homotopical algebra and topological ﬁeld theory, we
ﬁnd it most natural to work in the context of diﬀerential graded (dg) and ∞-categories. By a
dg category, we will always mean a pre-triangulated C-linear dg category. Since the homotopy
theory of such categories is identiﬁed with that of stable C-linear ∞-categories, we will use the
terms dg category and stable ∞-category interchangeably. Most of our constructions will take place
within the symmetric monoidal ∞-category StC of stable presentable C-linear ∞-categories with
morphisms continuous (colimit-preserving) functors. We will usually abuse terminology and refer
to its objects as categories. For foundations on ∞-categories (in the sense of Joyal [Jo]), we refer
to the comprehensive work of Lurie [L1, L2]. See Sections 2.1, 2.1.1, 2.2 for a summary of what we
will need of this theory.
By a scheme X, we will always mean a quasicompact, separated derived scheme of ﬁnite type
over C. By a D-module on a smooth scheme X, we will always mean a complex of D-modules,
and all functors will be derived. Thus the category of D-modules D(X) means the dg category of
complexes of D-modules which we can regard as an object of StC.
