---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-006-22-traces-in-geometry
section_title: "Traces in geometry"
section_number: 2.2
pages: 9-12
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.979
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
To apply the preceding formalism to geometry, it is useful to organize spaces and maps within a suitable categorical framework. We then arrive at loop spaces and fixed point loci as nonlinear expressions of dimensions and traces. This simple observation provides the core of the paper. Throughout the discussion, we continue to suppress all $\oo$-categorical notations and complications. Our reference for the correspondence 2-category of stacks is Section V of [@GR] (see also [@haugsengspan]).

To begin, consider the general setup of the symmetric monoidal category $Corr(\cC)$ of correspondences, or spans, in a category $\cC$ such as stacks (or formally a symmetric monoidal $\infty$-category with finite limits; see [@barwick; @haugsengspan]). Here the objects $X\in Corr(\cC)$ are the objects of $\cC$, the morphisms $Corr_\cC(X,Y)$ are arbitrary spans in $\cC$, $$\xymatrix{
&Z\ar[ld]\ar[rd]&\\
X&&Y}$$ (more generally one can require the left and right legs to live in specified subcategories of $\cC$ as in [@GR]). The composition of morphisms $Z\in Corr_\cC(X,Y)$ and $W\in Corr_\cC(Y,U)$ is given by fiber product $$\xymatrix{&&Z\times_Y W\ar[ld]\ar[rd]&&\\
&Z\ar[ld]\ar[rd]&&W\ar[ld]\ar[rd]& \\
X&&Y&&U}$$ and the symmetric monoidal structure is given in terms of that on $\cC$ (Cartesian product in the case of stacks). For the purpose of calculating dimensions and traces, we need not require any further properties of the spaces of $Corr(\cC)$, since we need only the modest local data discussed in Remarks [\[dim local\]](#dim local){reference-type="ref" reference="dim local"} and [\[functoriality local\]](#functoriality local){reference-type="ref" reference="functoriality local"}. (See [@TFT] and [@FHLT], where the higher categories $Fam_n$ of iterated correspondences of manifolds are constructed and applied.)

With applications in mind, we will specialize to the correspondence category $Corr_k=Corr(St_k)$ of derived stacks over $k$. It would also be interesting to work with smooth manifolds instead, for example through the theory of $C^\infty$-stacks [@joyce] (see Remark [\[Cinfty\]](#Cinfty){reference-type="ref" reference="Cinfty"}).

It is natural to enhance $Corr(\cC)$ to a 2-category $\ul{Corr}(\cC)$ by allowing non-invertible maps, or more generally correspondences, between correspondences (see Section V of [@GR] or [@haugsengspan] for full details), so that maps from $X$ to $Y$ form the category of objects over $X\times Y$. Our constructions naturally fit into the 2-category $\ul{Corr}^{prop}_k$ with non-invertible 2-morphisms restricted to be *proper* (or more generally ind-proper) maps of correspondences.

::: remark
[]{#correspondences are bimodules label="correspondences are bimodules"}

It is useful to view the correspondence category $Corr$ within the framework of coalgebras in symmetric monoidal categories. The diagonal map $X\to X\times X$ makes any space or stack into a cocommutative coalgebra object with respect to the Cartesian product monoidal structure (or commutative coalgebra in the opposite category). Moreover, a map $Z\to X$ is equivalent to an $X$-comodule structure on $Z$. Thus correspondences from $X$ to $Y$ may be interpreted as $X-Y$-bicomodules, with composition of correspondences given by tensor product of bicomodules.

Furthermore, it is natural to enhance $Corr$ to a 2-category by allowing non-invertible maps between correspondences. This can be viewed as a special case of the Morita category of coalgebras in a symmetric monoidal category. The 2-category $\ul{Corr}$ of spaces, correspondences, and maps of correspondences is the Morita category on spaces regarded as coalgebra objects. (In particular, the cocommutativity of the coalgebra objects implies they are canonically self-dual, and the transpose of a correspondence is the same correspondence read backwards.) If we further keep track of the $E_n$-coalgebra structure of spaces and consider the corresponding Morita $(n+1)$-category, we recover the $(n+1)$-category of iterated correspondences of correspondences. (See [@haugsengspan; @haugsengEn] for a thorough treatment of categories of spans and Morita categories of $E_n$ algebras; see also for example the category $Fam_n$ of [@TFT] and [@FHLT] in the topological setting.)
:::

### Geometric dimensions and loop spaces

A crucial feature of the category $Corr_k$ is that any object $X\in Corr_k$ is dualizable (in fact, canonically self-dual), thanks to the diagonal correspondence.[^1] Note for this it is crucial that we allow all maps, including the map $\pi_X:X\to pt$ for any $X$, as possible legs in a span.

We have the following calculations of dimensions and their functoriality. Note that the point $pt=\Spec k$ is the unit of $Corr_k$. We keep track of properness of maps of correspondences for the later application of sheaf theory.

::: prop
Let $Corr_k$ be the category of derived stacks and correspondences, and $\ul{Corr}^{prop}_k$ the 2-category of derived stacks, correspondences, and proper maps of correspondences.

\(1\) Any derived stack $X$ is dualizable as an object of $Corr_k$, and its dimension $\dim(X)$ is identified with the loop space $$\cL X= X^{S^1}\simeq X\times_{X\times X} X$$ regarded as a self-correspondence of $pt=\Spec k$.

\(2\) A map $f:X\to Y$ regarded as a correspondence from $X$ to $Y$ is continuous in $\ul{Corr}^{prop}_k$ if and only if $f$ is proper. Given a proper map $f:X\to Y$, its induced map $$\xymatrix{
\dim(f):\dim(X)\ar[r] & \dim(Y)
}$$ is identified with the loop map $$\xymatrix{
\cL f:\cL X \ar[r] & \cL Y
}$$
:::

::: remark
All of the objects and maps of the proposition have natural $S^1$-actions, on the one hand coming from loop rotation, on the other hand coming from the cyclic symmetry of dimensions. One can check that the identifications of the proposition are $S^1$-equivariant (see Remark [\[rem: cyclic\]](#rem: cyclic){reference-type="ref" reference="rem: cyclic"}).
:::

::: remark
Recall [@Toen; @conns] that for a derived scheme $X$, the loop space $\cL X\simeq T_X[-1]$ is the total space of the shifted tangent complex. The action map of the $S^1$-rotation action is encoded by the de Rham differential. For an underived stack $X$, the loop space is a derived enhancement of the inertia stack $IX=\{x\in X, \gamma\in Aut(x)\}.$ The action map of the $S^1$-rotation action is manifested by the "universal automorphism\" of any sheaf on $\cL X$.
:::

::: example
Let $G$ denote an algebraic group and $BG=pt/G$ its classifying space. There is a canonical identification $\cL BG\simeq G/G$ of the loop space and adjoint quotient.

Suppose we are given a $G$-derived stack $X$, or equivalently a morphism $\pi:X/G\to BG$, from which one recovers $X\simeq X/G \times_{BG} pt$. (Note that if we want $\pi$ proper we should take $X$ itself proper.)

Let us explain how the loop map $\cL \pi:\cL(X/G) \to \cL(BG)$ captures the fixed points of $G$ acting on $X$. For any self-map $g: X\to X$, let us write $X^g$ for the derived fixed point locus given by the derived intersection $$X^g= \Gamma_g \times_{X\times X} X.$$ of the graph $\Gamma_g\subset  X\times X$ with the diagonal. Then $\cL \pi$ map fits into a commutative square $$\xymatrix{
\ar[d]_-\sim \cL(X/G)  \ar[r]^-{\cL \pi} & \cL(BG) \ar[d]_-\sim \\
 \{g\in G, x\in X^g\}/G \ar[r]^-p & G/G
}$$ where $p$ projects to the group element.

In particular, fix a group element $g\in G$, with conjugacy class $\OO_g\subset G$, and centralizer $\cZ_G(g)\subset G$, so that $\OO_g/G\simeq B\cZ_G(g) \in G/G$. Then the corresponding fiber of $\cL \pi$ is the equivariant fixed point locus $X^g_G=X^g/\cZ_G(g)$, or in other words we have a fiber diagram $$\xymatrix{
\ar[d]  X^g_G \ar[r] & \OO_g/G \ar[d] \\
 \cL(X/G)  \ar[r]^-{\cL \pi} & \cL(BG)  
 }$$

Let us specialize to the case of a subgroup $K\subset G$, and the quotient $X=G/K$, so that we have a map of classifying stacks $\pi: BK \simeq G\backslash (G/K)\to BG$. Here the loop map $\cL \pi$ realizes the familiar geometry of the Frobenius character formula $$\xymatrix{
\ar[d]_-\sim \cL(BK) \ar[r]^-{\cL \pi} &  \cL(BG)\ar[d]_-\sim\\
  K/K \simeq  \{g\in G, x\in (G/K)^g\}/G
 \ar[r]^-p &  G/G
 }$$ The equivariant fixed point loci express the equivariant inclusion of conjugacy classes.

Specializing further, for $G$ a reductive group, $B\subset G$ a Borel subgroup, and $X=G/B$ the flag variety, we recover the group-theoretic Grothendieck-Springer resolution $$\xymatrix{
\ar[d]_-\sim \cL(BB) \ar[r]^-{\cL \pi} &  \cL(BG)\ar[d]_-\sim\\
  B/B \simeq \{g\in G, x\in (G/B)^g\}/G
 \ar[r]^-p &  G/G
 }$$
:::

### Geometric traces of correspondences

More generally, we have the following calculations of traces and their functoriality.

::: prop
Let $Corr_k$ be the category of derived stacks and correspondences, and $\ul{Corr}^{prop}_k$ the 2-category of derived stacks, correspondences, and proper maps of correspondences.

\(1\) The trace of a self-correspondence $Z\in \ul{Corr}^{prop}_k(X,X)$ is its fiber product with the diagonal $$\Tr(Z) \simeq Z|_{\Delta}=Z\times_{X\times X} X\simeq Z\times_X\cL X$$

In particular, for the graph $\Gamma_f\to X\times X$ of a self-map $f:X\to X$, its trace is the fixed point locus of the map $$\Tr(\Gamma_g)  \simeq X^f=\Gamma_f\times_{X\times X} X$$

\(2\) Given a proper map $f:X\to Y$ regarded as a correspondence from $X$ to $Y$, and self-correspondences $Z\in\ul{Corr}^{prop}_k(X, X)$ and $W \in\ul{Corr}^{prop}_k(Y, Y)$, together with an identification $$\xymatrix{
\alpha: Z  \ar[r]^-\sim  & X\times_Y W  
}$$ of correspondences from $X$ to $Y$, the induced abstract trace map $$\xymatrix{
\Tr(f,\alpha):\Tr(Z) \ar[r] & \Tr(W)
}$$ is equivalent to the induced geometric map $$\xymatrix{
\tau(f, \alpha): Z|_{\Delta_X}\ar[r] &  W|_{\Delta_Y}
}$$
:::

[^1]: Likewise, if we wish to make a space $n$-dualizable for any $n$ we may simply consider it as an object of a higher correspondence category as in Remark [\[correspondences are bimodules\]](#correspondences are bimodules){reference-type="ref" reference="correspondences are bimodules"}, since $E_n$-(co)algebras are $n+1$-dualizable objects of the corresponding Morita category. In other words, a space $X$ defines a topological field theory of any dimension valued in the appropriate correspondence category.
