---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-004-2-overview
section_title: "Overview"
section_number: 2
pages: 7-16
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.961
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
[]{#overview label="overview"}

## Traces in category theory

We highlight structures arising in the general theory of dualizable objects in symmetric monoidal higher categories (see also [@doldpuppe; @may; @PS]). For legibility, we suppress all $\oo$-categorical notations and complications from the introduction. We rely on [@GR] for the theory of symmetric monoidal $(\oo,2)$-categories, though only the formal outline of the theory is in fact needed for this paper. See [@TV; @HSS] for thorough treatments of the theory of traces in higher category theory.

The basic notion in the theory is that of *dimension* of a dualizable object of a symmetric monoidal category $\cA$. By definition, for such an object $A$ there exists another $A^\vee$ together with a coevaluation map $\eta_A$ and evaluation map $\epsilon_A$ satisfying standard identities. By definition, the dimension of $A$ is the endomorphism of the the unit $1_\cA$ given by the composition $$\xymatrix{ 1_\cA\ar[rr]^-{\eta_A}\ar@/_2pc/^-{\dim(A)}[rrrr] &&
  A\ot A^\vee \ar[rr]^-{\epsilon_A}&& 1_\cA}$$

::: example
For $V$ a vector space, $V^\vee =\Hom_k(V, k)$ is the vector space of functionals, $\epsilon_V: V\otimes V^\vee \to k$ is the usual evaluation of functionals, $\eta_V:k\to \End(V)\simeq V\ot V^\vee$ is the identity map (which exists only for $V$ finite-dimensional), and $\dim(V)$ can be regarded as an element of the ground field (by evaluating it on the multiplicative unit).
:::

::: remark
It is a useful technical observation that the notion of dualizability in the setting of $\oo$-categories is a "naive\" one: it is a property of an object that can be checked in the underlying homotopy category. As a result, all of the categorical and 2-categorical calculations in this paper are similarly naive and explicit (and analogous to familiar unenriched categorical assertions), involving only small amounts of data that can be checked by hand.
:::

The notion of dimension is a special case of the *trace* of an endomorphism $\Phi$ of a dualizable object $A$. By definition, the trace of $\Phi$ is the endomorphism of the unit $1_\cA$ given by the composition $$\xymatrix{1_{\cA}\ar[r]^-{\eta_A}\ar@/_2pc/^-{\Tr(\Phi)}[rrrr]& A \otimes A^\vee\ar[rr]^-{\Phi \otimes \id_{A^\vee}} &&  A\ot A^{\vee}
\ar[r]^-{\epsilon_A}& 1_\cA}$$ which recovers the dimension for $\Phi = \id_{A}$.

A key feature of dimensions and traces is their *cyclicity*, which at the coarsest level is expressed by a canonical equivalence $$\xymatrix{m(\Phi,\Psi):\Tr(\Phi\circ\Psi)\ar[r]^-{\sim}& \Tr(\Psi\circ\Phi),}$$ see Proposition [\[cyclic trace\]](#cyclic trace){reference-type="ref" reference="cyclic trace"}. At a much deeper level, an important corollary of the cobordism hypothesis [@TFT] is the existence of an $S^1$-action on $\dim(A)$ for any dualizable object $A$ (and an analogous structure for general traces, see Remark [\[full trace\]](#full trace){reference-type="ref" reference="full trace"}).

::: remark
[]{#dim local label="dim local"} It is useful for applications to note that the notion of dualizability and the definition of dimension and are local in the category $\cA$. Namely, they only require knowledge of the objects $1_{\cA},A,A^\vee, A\ot A^{\vee}$, the morphisms $\eta_A,\epsilon_A$, and standard tensor product and composition identities among them. Likewise, the notion of trace only requires the additional endomorphism $\Phi$ along with a handful of additional identities.
:::

### Functoriality of traces

Now suppose the ambient symmetric monoidal category $\cA$ underlies a 2-category, so there is the possibility of noninvertible 2-morphisms. This allows for the notion of left and right adjoints to morphisms. Let us say a morphism $A\to B$ is *continuous*, or *right dualizable*, if it has a right adjoint. (The terminology derives from the setting of presentable categories, where the adjoint functor theorem guarantees the existence of right adjoints for colimit preserving functors.)

Here are natural functoriality properties of dimensions and traces.

::: prop
Let $A,B$ denote dualizable objects of $\cA$ and $f_*:A\to B$ a continuous morphism with right adjoint $f^!$.

1.  There is a canonical map on dimensions $$\xymatrix{\dim(A)\ar@/_2pc/^-{\dim(f_*)}[rrrrr] \ar[r]^-{=}&\Tr(\Id_A) \ar[r] & \Tr(f^! f_*) \ar[r]^-\sim & \Tr(f_* f^!) \ar[r] & \Tr(\Id_B)\ar[r]^-{=}&\dim(B)}$$ compatible with compositions of continuous morphisms.

2.  Given endomorphisms $\Phi\in\End(A)$, $\Psi\in \End(B)$, and a *commuting structure* $$\xymatrix{\alpha:f_*\circ\Phi\ar[r]^-{\sim}& \Psi\circ f_*}$$ there is a canonical map on traces $$\xymatrix{
    \Tr(f_*,\alpha): \Tr(\Phi)\ar[r] & \Tr(\Psi)
    }$$ compatible with compositions of continuous morphisms with commuting structures.
:::

We refer to the compatibility with compositions stated in the proposition as *abstract Grothendieck-Riemann-Roch*. To see its import more concretely, let us restrict the generality and focus on an *object* of $A$ in the sense of a morphism $V:1_\cA\to A$.

::: corollary
Let $A,B$ denote dualizable objects of $\cA$ and $f_*:A\to B$ a continuous morphism. For $V:1_\cA\to A$ an object of $A$, we obtain a map on dimensions $$\xymatrix{\dim(V):1_\cA \simeq \dim(1_\cA)\ar[r] & \dim(A)
}$$ called the *character* of $V$ and alternatively denoted by $[V]$. It satisfies abstract Grothendieck-Riemann-Roch in the sense

that the following diagram commutes $$\xymatrix{ 1_\cA\ar[rr]^-{[V] }\ar@/_2pc/^-{[f_*V]}[rrrr] &&
  \dim(A)  \ar[rr]^-{\dim(f_*)}&& \dim(B)}$$
:::

::: remark
[]{#functoriality local label="functoriality local"} As in Remark [\[dim local\]](#dim local){reference-type="ref" reference="dim local"}, it is useful to note that the functoriality of dimension is local, depending only on a handful of objects, morphisms and identities, along with the additional adjunction data $(f_*,f^!)$. A similar observation applies to the functoriality of traces.
:::

::: remark
It follows from the cobordism hypothesis with singularities [@TFT] (see [@TV]) that the morphism $\dim(f_*)$ is $S^1$-equivariant, and hence the character $[V]$ is $S^1$-invariant, though we will not elaborate on this structure here. We refer to [@HSS] for a thorough study of the functoriality and cyclicity of traces.
:::

::: example
Let $dgCat_k$ denote the symmetric monoidal $\oo$-category of presentable $k$-linear differential graded categories (or alternatively, stable presentable $k$-linear $\oo$-categories), see e.g. [@GR]. In this setting, any compactly generated category $A$ is dualizable, and its dimension is the Hochschild chain complex $\dim(A)=HH_*(A)$. The $S^1$-action on $\dim(A)$ corresponds to Connes' cyclic structure on $HH_*(A)$, so that in particular, the localized $S^1$-invariants of $\dim(A)$ form the periodic cyclic homology of $A$.

More generally, the trace of an endofunctor $\Phi:A\to A$ is the Hochschild homology $\Tr(\Phi)=HH_*(A,\Phi)$. For example, if $A=R\module$ for a dg algebra $R$, then $\Phi$ is represented by an $R$-bimodule $M$, and we recover the Hochschild homology $HH_*(R,M)$.

Any compact object $M\in A$ defines a continuous functor $$\xymatrix{1_{dgCat_k}=dgVect_k\ar[r]^-{M} & A}$$ whose character is a vector $$\dim(M)\in HH_*(A)$$ in Hochschild homology (with refinement in cyclic homology). The abstract Grothendieck-Riemann-Roch theorem expresses the natural functoriality of characters in Hochschild homology (or their refinement in cyclic homology). In fact, the construction of characters factors through the canonical Dennis trace map $$\xymatrix{
A_{cpt}\ar[r] & K(A)\ar[r] & HH_*(A)
}$$ from the space $A_{cpt}$ of compact objects of $A$.
:::

## Traces in geometry

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

## Trace formulas via sheaf theories {#sheaf intro}

Given any sufficiently functorial method of measuring derived stacks, the preceding calculations of geometric dimensions, traces and their functoriality immediately lead to trace and character formulas. To formalize the functoriality needed, we will use the language of sheaf theories. Broadly speaking, a sheaf theory is a representation (symmetric monoidal functor out) of a correspondence category in the way a topological field theory is a representation of a cobordism category.[^2] It provides an approach to encoding the standard operations on coherent sheaves and $\D$-modules, developed by Gaitsgory and Rozenblyum in the book [@GR] (following a suggestion of Lurie and previous versions in [@koszul; @indcoh; @finiteness; @crystals]).

We will take the target of our sheaf theories to be the linear setting of the symmetric monoidal $(\oo,2)$-category $\ul{dgCat}_k$ of presentable $k$-linear differential graded categories with continuous functors and natural transformations. (Recall from Setting [\[stack conventions\]](#stack conventions){reference-type="ref" reference="stack conventions"} that for applications all stacks are assumed to be QCA or ind-inf-schemes. Also all proper maps can be replaced by ind-proper ones at no cost.)

::: defn
[]{#sheaf def intro label="sheaf def intro"} A *sheaf theory* is a symmetric monoidal functor of $(\infty,2)$-categories $$\xymatrix{
\ul{\cS}:\ul{Corr}_k^{prop}\ar[r] &  \ul{dgCat}_k
}$$ from correspondences of stacks (with 2-morphisms given by proper maps of correspondences) to dg categories. We denote by $$\xymatrix{
\cS:Corr_k\ar[r] &  dgCat_k
}$$ the underlying 1-categorical sheaf theory, i.e. the symmetric monoidal functor on $(\infty,1)$-categories obtained by forgetting noninvertible morphisms.
:::

Let us first spell out some of the structure encoded in a 1-categorical sheaf theory $\cS$.

The graph of a map of stacks $f:X\to Y$ provides a correspondence from $X$ to $Y$ and a correspondence from $Y$ to $X$. We denote the respective induced maps by $f_{*}:\cS(X)\to \cS(Y)$ and $f^!:\cS(Y)\to \cS(X)$. For $\pi:X\to pt = \Spec k$, we denote by $\omega_{X}=\pi^! k\in \cS(X)$ the $\cS$-analogue of the dualizing sheaf, and by $\omega(X)=\pi_{*}\omega_{X} \in \cS(pt) = dgVect_k$ the $\cS$-analogue of "global volume forms\". We adopt traditional notations whenever possible, for example writing $\Gamma(X, \cF)=\pi_{*}(\cF)$, for $\cF\in \cS(X)$

The functoriality of $\cS$ concisely encodes base change for $f_{*}$ and $f^!$. Its symmetric monoidal structure provides equivalences $$\cS(X\times Y)\simeq \cS(X)\ot \cS(Y),$$ as well as a symmetric monoidal structure on $\cS(X)$ for any $X$ (using pullback along diagonal maps). The 2-categorical extension $\ul{\cS}$ further encodes an identification of $f^!$ with the right adjoint of $f_*$ for $f$ proper.

Since a sheaf theory $\cS$ is symmetric monoidal, it is automatically compatible with dimensions and traces: for any $X\in Corr_k$, and any endomorphism $Z\in Corr_k(X,X)$, we have $$\xymatrix{
\dim (\cS(X)) \simeq \cS(\dim (X))   & \Tr(\cS(Z)) \simeq \cS(\Tr(Z)) 
}$$ Let us combine this with the calculation of the right hand sides and highlight specific examples of interest.

::: prop
[]{#intro HH description label="intro HH description"} Fix a sheaf theory $\cS:Corr_k\to dgCat_k$.

\(1\) The $\cS$-dimension $\dim(\cS(X)) =HH_*(\cS(X))$ of any $X\in Corr_k$ is $S^1$-equivariantly equivalent with $\cS$-global volume forms on the loop space $$\dim(\cS(X))\simeq \omega(\cL X).$$

In particular, for $G$ an affine algebraic group, characters of $\cS$-valued $G$-representations are adjoint-equivariant $\cS$-global volume forms $$\dim(\cS(BG))\simeq \omega(G/G)$$

\(2\) The $\cS$-trace of any endomorphism $Z\in Corr_k(X,X)$ is equivalent to $\cS$-global volume forms on the restriction to the diagonal $$\Tr(\cS(Z)) \simeq \omega(Z|_{\Delta})$$

In particular, the $\cS$-trace of a self-map $f:X\to X$ is equivalent to $\cS$-volume forms on the $f$-fixed point locus $$\Tr(f_{*})\simeq \omega(X^f)$$
:::

::: remark
[]{#local sheaf theory label="local sheaf theory"} To apply this proposition, far less structure than a full sheaf theory is required. We only need the data of the functor $\cS$ on the handful of objects and morphisms involved in the construction of dimensions and traces as in Remark [\[dim local\]](#dim local){reference-type="ref" reference="dim local"}. In particular, we only need base change isomorphisms for pullback and pushforward along specific diagrams, rather than the general base change provided by a functor out of $Corr_k$. This is often easy to verify in practice, in particular for the examples $\cQ$, $\cQ^!$ and $\D$ (see for example [@BFN] for the quasicoherent setting).
:::

### Examples of sheaf theories

As we explain in Section [\[sect shvs\]](#sect shvs){reference-type="ref" reference="sect shvs"}, the work [@GR] (combined with essential results from [@finiteness]) construct two sheaf theories $\cQ^!$ and $\cD$:

$\bullet$ Theory $\cQ^!$: the theory of ind-coherent sheaves $\cQ^!(X)$. This is the "large\" version $\cQ^!(X)=\Ind \mathit{Coh}(X)$ of the category of coherent sheaves, which by definition are the compact objects in $\cQ^!(X)$. (For smooth $X$, ind-coherent and quasicoherent sheaves are equivalent.) Maps are given by the standard pushforward $f_*$ and exceptional pullback $f^!$. The $\cQ^!$-dualizing sheaf is the usual dualizing complex $\omega_X$, and (for $X$ proper) the $\cQ^!$-global volume forms are its sections $R\Gamma(X,\omega_X)=R\Gamma(X,\cO_X)^*.$ The $K$-theory of $\cQ^!(X)$ is algebraic $G$-theory $G(X)$, the homological version of algebraic $K$-theory for potentially singular spaces suited to Grothendieck-Riemann-Roch theorems.

$\bullet$ Theory $\D$: the theory of $\D$-modules $\D(X)$ with the standard functors $f_*$ and $f^!$. The compact objects are necessarily coherent $\D$-modules (this suffices for $X$ a scheme; see [@finiteness] for a characterization in the case of a stack). The $\cD$-dualizing sheaf is the Verdier dualizing complex $\omega_X$, and the $\cD$-global volume forms (for $X$ smooth) are the Borel-Moore homology $R\Gamma(X_{dR},\omega_X)=H_{dR}(X)^*$.

::: remark
More precisely, [@GR] construct the sheaf theories $\cQ^!$ and $\cD$ as lax symmetric monoidal functors on a much broader class of stacks, with pullbacks allowed for arbitrary maps but pushforward only for schematic morphisms. The strictness follows from results of [@finiteness], as we explain in Section [\[QCA section\]](#QCA section){reference-type="ref" reference="QCA section"}, as does the definition of pushforwards for arbitrary maps of QCA stacks (without the functorial apparatus of [@GR] but sufficient for all the "local\" constructions we need, in the sense of Remarks [\[dim local\]](#dim local){reference-type="ref" reference="dim local"}, [\[functoriality local\]](#functoriality local){reference-type="ref" reference="functoriality local"} and [\[local sheaf theory\]](#local sheaf theory){reference-type="ref" reference="local sheaf theory"}).
:::

::: remark
The theory of quasicoherent sheaves $X\mapsto\cQ(X)$ behaves similarly with respect to 1-categorical properties. It also defines a symmetric monoidal functor out of the $(\infty,1)-$category of correspondences of stacks, using standard pullback $f^*$ and pushforward $f_*$ functors. Assuming $X$ is perfect (in the sense of [@BFN]), the compact objects of $\cQ(X)$ form the subcategory of perfect complexes $\mathit{Perf}(X)$, and we have $\cQ(X) = \Ind\mathit{Perf}(X)$. The analog of the dualizing sheaf is the structure sheaf $\cO_X$, and the $\cQ$-"global volume forms\" are the global functions $R\Gamma(X,\cO_X)$. The $K$-theory of $\cQ(X)$ is the usual algebraic $K$-theory $K(X)$. However while we have $(f^*,f_*)$ adjunction and $f^*$ preserves perfection for arbitrary morphisms, proper pushforward does not preserve perfection and we do not have proper adjunction of the form $(f_*,f^*)$ (unless we add smoothness and twisting by relative dualizing sheaves). In other words, $\cQ$ and $K$-theory are better adapted to pullback, while $\cQ^!$ and $G$-theory are better adapted to integration and character formulas.
:::

::: remark
[]{#Cinfty label="Cinfty"} It is tempting to think of sheaf theories in algebraic geometry as analogues of elliptic operators or complexes in differential topology. In particular, the theory $\cQ^!(X)$ for a smooth variety $X$ is a natural setting for the study of the Dolbeault $\overline{\del}$-operator coupled to vector bundles, while the theory $\D(X)$ is similarly a natural setting for the study of the de Rham operator $d$ coupled to vector bundles. The pushforward operation is the analogue of the index. In this direction, it would be interesting to develop sheaf theories on derived manifolds, for example $C^\infty$-schemes and stacks. Quasicoherent sheaves in the sense of Joyce [@joyce] are a natural candidate. Another interesting setting is categories of elliptic complexes on manifolds. The general results below would then provide an approach to generalizations of the classical Atiyah-Singer and Atiyah-Bott theorems.
:::

Let us spell out the main ingredients of Proposition [\[intro HH description\]](#intro HH description){reference-type="ref" reference="intro HH description"} for our examples. Recall that for $X$ a smooth scheme, $\cL X\simeq \Spec_X \Sym(\Omega_X[1])$, and for $BG$ a classifying stack, $\cL(BG) \simeq G/G$.

$\bullet$ Theory $\cQ$: For $X$ a smooth scheme, we have the HKR identification of functions on the loop space (or the Hochschild chain complex) with differential forms, $\dim(\cQ(X)) \simeq \Gamma(X,\Sym(\Omega_X[1]))$, or more generally, $\cQ$-global volume forms on $X^f$ are the coherent cohomology $\cO(X^f)$. For $BG$ a classifying stack, $\cQ$-global volume forms on $\cL (BG)$ are the coherent cohomology $\cO(G/G)$, which for $G$ reductive are the underived invariants $\cO(T)^W$.

$\bullet$ Theory $\cQ^!$: For $X$ smooth, we have $\cQ(X)\simeq \cQ^!(X)$, and so we recover the above descriptions. For $X$ proper, $\cQ$-global volume forms on $\cL X$ are the dual of the Hochschild chain complex (see [@toly]).

$\bullet$ Theory $\D$: For $X$ a smooth scheme, $\D$-global volume forms on $\cL X$ are the de Rham cochains $\dim(\D(X)) \simeq C^*_{dR}(X)$, or more generally, $\D$-global volume forms on $X^f$ are the de Rham cochains $C^*_{dR}(X^f)$, or equivalently those of the underlying underived scheme of $X^f$. For $BG$ a classifying stack, $\D$-global volume forms on $\cL (BG)$ are the Borel-Moore homology of $G/G$.

### Integration formulas for traces {#integration section}

Now let us turn to the functoriality of dimensions and traces, which is reflected in integration of volume forms along proper maps.

For a sheaf theory $$\uS:\uCorr^{prop}_k\to \udg_k,$$ the counit of the $(f_*,f^!)$ adjunction for a proper map $f:X\to Y$ gives rise to a canonical integration map $$\xymatrix{
\int_f: \omega(X)\ar[r] & \omega(Y)
}$$

::: thm
Fix a sheaf theory $\uS:\uCorr_k\to \udg_k$.

\(1\) For any proper map $f:X\to Y$, the induced map on dimensions $$\xymatrix{
\dim(f_*):\dim(\cS(X))\ar[r] & \dim(\cS(Y))
}$$ is identified ($S^1$-equivariantly) with integration along the loop map $$\xymatrix{
\dim(f_*)\simeq \int_{\cL f}:\omega(\cL X) \ar[r] & \omega(\cL Y)
}$$

\(2\) Given a proper map $f:X\to Y$ regarded as a correspondence from $X$ to $Y$, and self-correspondences $Z\in\ul{Corr}_k(X, X)$ and $W \in\ul{Corr}_k(Y, Y)$, together with an identification $$\xymatrix{
\alpha: Z  \ar[r]^-\sim  & X\times_Y W  
}$$ of correspondences from $X$ to $Y$, the induced trace map is identified with integration along the natural map $$\xymatrix{
\Tr(f_*,\alpha) \simeq \int_{\tau(f, s)} : \omega( Z|_{\Delta_X}) \ar[r] & \omega(W|_{\Delta_Y} )
}$$
:::

::: remark
Similarly, in the case of the theory $\cQ$ of quasicoherent sheaves, the standard adjunction $(f^*,f_*)$ leads to the evident contravariant functoriality of dimensions under arbitrary maps, given by pullback of functions on loop spaces.
:::

::: remark
For applications to categorical representation theory, in particular the geometric Langlands program, it is interesting to have character formulas for group actions on categories. Such formulas would follow from a good formalism of "stack theories\", the higher unstable analogs of sheaf theories, such as the assignment $X\to ShvCat_k(X)$. Such stack theories could be formulated as symmetric monoidal functors $\uS:\uCorr_k\to\cA$ out of a correspondence $(\infty,2)$ (or more naturally $(\infty,3)$) category with values in a category $\cA$ such as that of module categories for $dgCat_k$. Namely, we are interested in categorified analogues of $\cD$ and $\cQ$, taking values in the $\oo$-category $\Pr^L$ of presentable $\oo$-categories, in which we assign to a scheme or stack $X$ the $\infty$-category of quasicoherent sheaves of module categories over $\D$ or $\cQ$. Since such theories have not been fully constructed yet, we will only briefly sketch the idea.

For any stack $X$ and sheaf theory $\cS$, the category of sheaves $\cS(X)$ is naturally symmetric monoidal, and so we may consider its $\oo$-category of (presentable, stable) module categories $\cS(X)\module$. To obtain a more meaningful geometric theory we should sheafify this construction. For example, strong or Harish-Chandra $G$-categories (in other words, module categories over $\D(G)$ with convolution) are identified with sheaves of categories over the de Rham stack of $BG$. However, in the quasicoherent case, the "1-affineness\" theorem of Gaitsgory [@1affine] identifies $\cQ(X)$-modules with sheaves of categories on $X$ for a large class of stacks (specifically, for $X$ an eventually coconnective quasi-compact algebraic stack of finite type with an affine diagonal over a field of characteristic 0). In particular, $\cQ(BG)$-modules are identified with algebraic $G$-categories.

In the quasicoherent case, the general formalism of this paper should provide an $S^1$-equivariant equivalence $\dim(\cQ(X)\module)=\cQ(\cL X)$, identifying the class $[\cQ(X)]$ of the structure stack with the structure sheaf $\cO(\cL X)$. In particular, the characters of quasicoherent $G$-categories are given by $\cQ(G/G)$. The induced map on dimensions $\dim(f_*):\dim(\cQ(X)\module)\to \dim(\cQ(Y)\module)$ is identified $S^1$-equivariantly with the morphism given by pushforward along the loop map $$\xymatrix{
\dim(f_*)=\cL f_*:\cQ(\cL X) \ar[r] &  \cQ(\cL Y)
}$$ In particular, for an algebraic group $G$ and $G$-space $X$ with $\pi:X/G\to BG$, the character of the $G$-category $\cQ(X/G)$ is given by the pushforward $\cL\pi_* \cO(\cL X/G)\in \cQ(G/G)$. Analogous results are expected for strong or Harish-Chandra $G$-categories (module categories for $\D(G)$ with convolution) using the sheafification of the theory of $\D(X)$-module categories. We hope to return to these applications in future works.
:::

[^1]: Likewise, if we wish to make a space $n$-dualizable for any $n$ we may simply consider it as an object of a higher correspondence category as in Remark [\[correspondences are bimodules\]](#correspondences are bimodules){reference-type="ref" reference="correspondences are bimodules"}, since $E_n$-(co)algebras are $n+1$-dualizable objects of the corresponding Morita category. In other words, a space $X$ defines a topological field theory of any dimension valued in the appropriate correspondence category.

[^2]: Indeed a typical mechanism to construct "Lagrangian\" field theories is as the composition of a sheaf theory with a "classical field theory\" as in [@FHLT; @haugsengspan], a symmetric monoidal functor from a cobordism category to a correspondence category.
