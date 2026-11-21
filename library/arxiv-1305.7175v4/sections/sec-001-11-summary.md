---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-001-11-summary
section_title: "Summary"
section_number: 1.1
pages: 2-6
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.897
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
[]{#summary label="summary"} We now describe the main theorem, extending classical trace and dimension formulas to a very general setting in derived algebraic geometry (including equivariance for arbitrary Lie algebroids or affine algebraic groups) without any smoothness or transversality assumptions, while emphasizing that the main contribution of the paper is the simple geometric formalism underlying these formulas. For our general and formal nonlinear results, we need not assume anything about what classes of derived stacks and morphisms we work with. For applications, we need to be in a setting in which the powerful mechanism of sheaf theory is fully developed [@indcoh; @finiteness; @GR].

::: setting
[]{#stack conventions label="stack conventions"} Throughout this paper, we work over a field $k$ of characteristic zero. A *stack* $X$ connotes either

1.  a QCA derived stack in the sense of [@finiteness]. In other words $X$ is quasicompact with affine diagonal and the underived inertia of $X$ is finite presentation over the underlying underived stack $X_{cl}$.

2.  an ind-inf-scheme, in the sense of [@GR]. These include (derived) schemes of finite (or locally almost of finite) type and ind-schemes built out of unions of the former along closed embeddings, as well as their quotients by arbitrary Lie algebroids, or equivalently formal groupoids.

By a *proper* map we indicate a proper and schematic map, while for ind-proper indicates ind-proper and ind-inf-schematic. All appearances of proper maps in this paper may be replaced by ind-proper ones.
:::

Thus the class of spaces we consider includes all $k$-derived schemes of finite type and their quotients by either Lie algebroids or finite type affine group schemes.

Given a derived stack $\pi_X:X\to \Spec k$, we denote by $\pi_{\cL X}:\cL X = \Map(S^1, X) \to \Spec k$ its derived loop space. In general, the derived loop space is a derived thickening of the inertia stack. For a map $f:X\to Y$, we will denote by $\cL f:\cL X\to \cL Y$ the induced map on loops.

::: example
[]{#intro ex label="intro ex"} For many applications, the following two special cases are noteworthy.

When $X$ is a smooth scheme, $\cL X\simeq  \BT_X[-1]$ is the total space of the shifted tangent space by the HKR theorem. The same holds for an arbitrary scheme, if we replace the tangent space by the tangent *complex*, see for example [@conns]. For $f:X\to Y$ a map of schemes, $\cL f :\BT_X[-1]\to \BT_Y[-1]$ is (the shift of) the usual tangent map.

When $Y =BG$ is a classifying stack, $\cL Y\simeq G/G$ is the adjoint quotient. For $X$ a $G$-scheme, and $f:X/G\to BG$ the corresponding classifying map, $\cL f:\cL (X/G)\to \cL BG \simeq G/G$ is the universal family of derived fixed point loci. More precisely, for any element $g\in G$, the derived fixed point locus $X^g \subset X$ is precisely the derived fiber $X^g \simeq \cL(X/G) \times_{G/G} \{g\}$
:::

We will measure stacks $X$ by differential graded (dg) enhancements of derived categories of sheaves.

The most familiar is the assignment $X\mapsto\cQ(X)$ of the (unbounded) category of quasicoherent sheaves. However, we will make essential use of Grothendieck-Serre duality, in the guise of an adjunction $(f_*,f^!)$ between push-forward and extraordinary pullback for proper maps $X$. This duality is most naturally expressed in the setting of *ind-coherent sheaves* $X\mapsto \cQ^!(X)$ as developed in [@indcoh; @GR]. Ind-coherent sheaves agree with quasicoherent sheaves for smooth schemes but differ on singular schemes, where \[bounded complexes of\] coherent sheaves (the compact objects of $\cQ^!$) differ from perfect complexes (the compact objects of $\cQ$). In other words, ind-coherent sheaves are to coherent sheaves and $G$-theory (the setting of Grothendieck-Riemann-Roch theorems) as quasicoherent sheaves are to perfect complexes and $K$-theory.

Another sheaf theory to which the general formalism developed in [@GR] applies is the theory of $\cD$-modules $X\to \cD(X)$, which for smooth schemes agrees with the classical notion of quasicoherent complexes of modules for the sheaf of differential operators $\cD_X$ (i.e. with compact objects given by bounded coherent complexes of $\cD_X$-modules). In general [@crystals; @GR] $\cD(X)$ is defined as the category of crystals, i.e., as ind-coherent complexes on the de Rham space of $X$ $$\cD(X):=\cQ^!(X_{dR}).$$ The compact objects in $\cD(X)$ for $X$ a scheme are the coherent $\cD$-modules, while for $X$ a stack they form a smaller class, the *safe* $\cD$-modules of [@finiteness].

The book [@GR] develops the theories $\cQ^!$ and $\cD$ in particular as functors out of 2-categories of correspondences of schemes and stacks, with 1-morphisms from $X$ to $Y$ given by correspondences representable over $Y$ and 2-morphisms given by ind-proper ind-schematic morphisms of correspondences. This theory encodes a huge amount of structure, including in particular pullback and pushforward functors $f^!$ and $f_*$ satisfying base change, as well as the $(f_*,f^!)$ adjunction for proper (or even ind-proper) maps. They also establish symmetric monoidal properties of the sheaf theory.[^1] (See Sections [\[sheaf intro\]](#sheaf intro){reference-type="ref" reference="sheaf intro"} and [\[sect shvs\]](#sect shvs){reference-type="ref" reference="sect shvs"} for more background and precise statements.)

Let $\cS=\cQ^!$ or $\cS=\cD$ denote either of these sheaf theories.

We let $\omega_X =\pi_X^!\cO_{\Spec k}\in \cS(X)$ denote the appropriate dualizing sheaf. Thus for ind-coherent sheaves, $\omega_X\in \cQ^!(X)$ is the algebraic dualizing sheaf, and for $\D$-modules, $\omega_X\in \D(X)$ is the Verdier dualizing sheaf. Let $\omega(X)=\pi_{X*}\omega_X$ denote the corresponding complex of global volume forms: for ind-coherent sheaves, $\omega(X)\in k\module$ consists of algebraic volume forms, and for $\D$-modules, $\omega(X)\in k\module$ consists of locally constant distributions (Borel-Moore chains) for $X$ a scheme.

For $X$ a stack we use the continuous "renormalized\" pushforward functor on $\cD$-modules of [@finiteness], which roughly replaces equivariant cohomology (derived invariants) by a shift of equivariant homology (derived coinvariants, see [@finiteness Example 9.1.6]), so that $\omega(Y/G)$ for a $G$-variety $Y$ is given by a shift of $G$-coinvariants on Borel-Moore chains on $Y$. (Note that even for $X=BG$ this differs from the standard definition of equivariant Borel-Moore homology, which is identified in this case with equivariant cohomology.)

For a proper (or ind-proper) map $f:X\to Y$, adjunction provides an integration map $\int_f:\omega(X)\to \omega(Y)$.

::: example
Let us continue with the special cases of Example [\[intro ex\]](#intro ex){reference-type="ref" reference="intro ex"}, and focus in particular on algebraic distributions $\omega_{\cL X} \in \cQ^!(\cL X)$ on the loop space.

When $X$ is a smooth scheme, $\cL X \simeq  \BT_X[-1]$ is naturally Calabi-Yau, and its global volume forms are identified with differential forms $\omega( \BT_X[-1]) \simeq \cO( \BT_X[-1]) \simeq \Sym(\Omega_X[1])$.

The canonical "volume form\" on $\cL X$ is given by the Todd genus (as explained by Markarian [@markarian]): the resulting integration of functions on $\cL X$ differs from the integration of differential forms on $X$ by the Todd genus.

When $Y =BG$ is a classifying stack, $\cL Y \simeq G/G$ is naturally Calabi-Yau, and its global volume forms are invariant functions $\omega(G/G) \simeq \cO(G/G) \simeq \cO(G)^G$. If $G$ is reductive with Cartan subgroup $T\subset G$ and Weyl group $W$, the naive invariants $\cO(G)^G \simeq \cO(T)^W$ are equivalent to the derived invariants, but in general there may be higher cohomology.
:::

::: thm
[]{#main label="main"} Let $\cS=\cQ^!$ or $\cS=\cD$ denote either the theory of ind-coherent sheaves or $\D$-modules. Recall our conventions for stacks and morphisms, Setting [\[stack conventions\]](#stack conventions){reference-type="ref" reference="stack conventions"}.

$\bullet$ For a stack $X$, there is a canonical identification $HH_*(\cS(X))\simeq \omega(\cL X)$ of the Hochschild homology of sheaves on $X$ with distributions (or renormalized Borel-Moore chains) on the loop space.

$\bullet$ For a proper (or ind-proper) map of stacks $f:X\to Y$ the induced map $HH_*(\cS(X))\to HH_*(\cS(Y))$ is given by integration along the loop map $\cL f:\cL X\to \cL Y$.

$\bullet$ **Grothendieck-Riemann-Roch:** In particular, for any compact object $M\in \cS(X)$ (coherent sheaf or safe coherent $\cD$-module) with character $[M]\in HH_*(\cS(X))\simeq \omega(\cL X)$, there is a canonical identification $$[f_*\cM]\simeq\int_{\cL f}[M]\in HH_*(\cS(Y))\simeq\omega(\cL Y)$$ In other words, the character of a pushforward along a proper map is the integral of the character along the induced loop map.

$\bullet$ **Atiyah-Bott-Lefschetz:** Let $G$ be an affine group, and $X$ a proper stack with $G$-action, or equivalently, a proper map $f:X/G\to BG$. Then for any compact object $M\in \cS(X/G)$ ($G$-equivariant coherent sheaf or safely equivariant coherent $\cD$-module on $X$), and element $g\in G$, there is a canonical identification $$[f_*M]|_g \simeq \int_{\cL f} [M]|_{X^g}$$ In other words, under the identification of invariant functions and volume forms on the group, the value of the character of an induced representation at a group element is given by the integral of the original character along the corresponding fixed point locus of the group element.

$\bullet$ **Extension to traces:** The trace $Tr(\cS(Z))$ of the endofunctor of $\cS(X)$ given by a self-correspondence (e.g. a self-map) $X\leftarrow Z\rightarrow X$ is given by distributions on the fixed points $\omega(Z|_{\Delta})$.

$\bullet$ For a map $f:(X,Z)\to (Y,W)$ of stacks with self-correspondences[^2], the induced map $Tr(\cS(Z))\to Tr(\cS(W))$ is given by integration along fixed points $Z|_{\Delta_X}\to W_{\Delta_Y}$.
:::

::: example
Here is a reminder of a well-known application of the Atiyah-Bott-Lefschetz formula in representation theory.

$\bullet$ If $G$ is a finite group, and $X=G/K$ is a homogeneous set, and $M=k[G/K]$ the ring of functions, one recovers the Frobenius character formula for the induced representation $k[G/K]$.

$\bullet$ If $G$ is a reductive group, $X=G/B$ is the flag variety, $X/G=pt/B\to pt/G$. The loop map $$\cL(X/G)=B/B\simeq \wt{G}/G\to G/G$$ is the (group) Grothendieck-Springer simultaneous resolution, with fibers giving fixed point loci on the flag variety. For $M=\cL$ an equivariant line bundle on $G/B$, and $g\in G$ runs over a maximal torus, one recovers the Weyl character formula for the induced representation $H^*(G/B, \cL)$.
:::

::: remark
The reader will note no explicit appearance of the Todd genus in the above formulas. In other words as for K-theory, pushforward of sheaves naturally agrees with the pushforward in Hochschild homology. The Todd genus arises in comparing these natural pushforwards with the pushforward in cohomology, i.e., integration of forms. It arises when one unwinds the integration map $\int_{\cL f}:\omega(\cL X) \to \omega(\cL Y),$ given by Grothendieck duality, in terms of functions (or differential forms) using the Hochschild-Kostant-Rosenberg theorem. In particular, the familiar denominators in the Atiyah-Bott formula are implicit in the integration measure on the fixed point locus.

For instance, as mentioned above, when $X$ is a smooth scheme, a geometric version of the HKR theorem asserts that the loop space is the total space of the shifted tangent complex $\cL X \simeq \BT_X[-1]$, and global volume forms are canonically functions $\omega(\cL X)  \simeq \cO( \BT_X[-1]) \simeq \Sym(\Omega_X[1])$. Under this identification (as explained by Markarian [@markarian]), the resulting integration of functions on $\cL X$ differs from the integration of differential forms on $X$ by the Todd genus.
:::

::: remark
The paper [@KP] carries out the program described in this paper (i.e. recovering classical identities from non-linear ones) by calculating explicitly the derived contributions in the case of the Atiyah-Bott formula.
:::

::: remark
The main contribution of this paper is hidden in the statement of this theorem: we establish nonlinear versions of character formulas in the setting of derived stacks, and deduce classical formulas and new higher categorical analogues formally by applying suitable sheaf theories. Thanks to the great generality of sheaf theory in derived algebraic geometry [@GR], the resulting applications hold with remarkably few assumptions.

We are particularly interested in the higher categorical variants where one considers sheaves of categories, in particular Frobenius-Weyl character formulas for group actions on categories. Since the requisite foundations are not yet fully developed, we postpone details of this to future works. Applications include an identification of the character of the category of $\D$-modules on the flag variety with the Grothendieck-Springer sheaf, and of the trace of a Hecke functor on the category of $\D$-modules on the moduli of bundles on a curve with the cohomology of a Hitchin space.
:::

[^1]: We will also need from [@finiteness] the construction of continuous pushforward functors for all maps of QCA stacks (such as the non-representable projection $\pi_X:X\to pt$ from a stack) and their base-change property.

[^2]: i.e., we lift $f$ to an identification $Z\simeq X\times_Y W$ of correspondences from $X$ to $Y$
