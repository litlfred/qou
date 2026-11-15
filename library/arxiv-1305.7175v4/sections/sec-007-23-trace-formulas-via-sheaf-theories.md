---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-007-23-trace-formulas-via-sheaf-theories
section_title: "Trace formulas via sheaf theories"
section_number: 2.3
pages: 12-16
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.978
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
[]{#sheaf intro label="sheaf intro"}

Given any sufficiently functorial method of measuring derived stacks, the preceding calculations of geometric dimensions, traces and their functoriality immediately lead to trace and character formulas. To formalize the functoriality needed, we will use the language of sheaf theories. Broadly speaking, a sheaf theory is a representation (symmetric monoidal functor out) of a correspondence category in the way a topological field theory is a representation of a cobordism category.[^1] It provides an approach to encoding the standard operations on coherent sheaves and $\D$-modules, developed by Gaitsgory and Rozenblyum in the book [@GR] (following a suggestion of Lurie and previous versions in [@koszul; @indcoh; @finiteness; @crystals]).

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

# Traces in category theory {#sect cat}

[^1]: Indeed a typical mechanism to construct "Lagrangian\" field theories is as the composition of a sheaf theory with a "classical field theory\" as in [@FHLT; @haugsengspan], a symmetric monoidal functor from a cobordism category to a correspondence category.
