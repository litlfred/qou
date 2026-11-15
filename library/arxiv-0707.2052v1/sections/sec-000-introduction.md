---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.962
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#sec:intro label="sec:intro"}

The purpose of the present paper is to introduce the Mukai pairing on the Hochschild homology of smooth, proper spaces. This pairing is the natural analogue, in the context of Hochschild theory, of the Poincaré pairing on the singular cohomology of smooth manifolds.

Our approach is categorical. We start with a geometric category, whose objects will be called *spaces*. For a space $X$ we define its Hochschild homology which is a graded vector space $\mathop{\mathrm{HH}}_\bullet(X)$ equipped with the non-degenerate *Mukai pairing*. We show that this structure satisfies a number of properties, the most important of which are *functoriality* and *adjointness*.

The advantage of the categorical approach is that the techniques we develop apply in a wide variety of geometric situations, as long as an analogue of Serre duality is satisfied. Examples of categories for which our results apply include compact complex manifolds, proper smooth algebraic varieties, proper Deligne-Mumford stacks for which Serre duality holds, representations of a fixed finite group, and compact "twisted spaces" in the sense of [@Cal]. We expect the same construction to work for categories of Landau-Ginzburg models [@Orl], but at the moment it is not known whether Serre duality holds for these.

## The Hochschild structure {#subsec:hochstr}

In order to define the Hochschild structure of a space we need notation for certain special kernels which will play a fundamental role in what follows. For a space $X$, denote by $\mathsf {Id}_X$ and $\Sigma_X^{-1}$ the objects of $\mathbf{D}(X\times X)$ given by $$\mathsf {Id}_X := \Delta_* {\mathscr O}_X \quad\mbox{and}\quad \Sigma_X^{-1} :=
\Delta_* \omega_X^{-1}[-\dim X],$$ where $\Delta:X \rightarrow X\times X$ is the diagonal map, and $\omega_X^{-1}$ is the anti-canonical line bundle of $X$. When regarded as kernels, these objects induce the identity functor and the inverse of the Serre functor on $\mathbf{D}(X)$, respectively. We shall see in the sequel that $\mathsf {Id}_X$ can be regarded as the identity 1-morphism of $X$ in a certain 2-category ${\mathscr{V}\textsf{ar}}$.

The *Hochschild structure* of the space $X$ then consists of the following data:

-   the graded ring $\mathop{\mathrm{HH}}^\bullet(X)$, the Hochschild cohomology ring of $X$, whose $i$-th graded piece is defined as $$\mathop{\mathrm{HH}}^i(X) := \mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^i(\mathsf {Id}_X, \mathsf {Id}_X);$$

-   the graded left $\mathop{\mathrm{HH}}^\bullet(X)$-module $\mathop{\mathrm{HH}}_\bullet(X)$, the Hochschild homology module of $X$, defined as $$\mathop{\mathrm{HH}}_i(X) := \mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^{-i}(\Sigma_X^{-1}, \mathsf {Id}_X);$$

-   a non-degenerate graded pairing ${\ensuremath{\left\langle {-},\, {-}\right\rangle_{\rm M}}}$ on $\mathop{\mathrm{HH}}_\bullet(X)$, the *generalized Mukai pairing*.

The above definitions of Hochschild homology and cohomology agree with the usual ones for quasi-projective schemes (see [@CalHH2]). The pairing is named after Mukai, who was the first to introduce a pairing satisfying the main properties below, on the total cohomology of complex K3 surfaces [@MukK3].

## Properties of the Mukai pairing

The actual definition of the Mukai pairing is quite complicated and is given in Section [\[sec:adjoint\]](#sec:adjoint){reference-type="ref" reference="sec:adjoint"}. We can, however, extricate the fundamental properties of Hochschild homology and of the Mukai pairing.

::: Description
Integral kernels induce, in a functorial way, linear maps on Hochschild homology. Explicitly, to any integral kernel $\Phi\in \mathbf{D}(X\times Y)$ we associate, in Section [\[def:defmaps\]](#def:defmaps){reference-type="ref" reference="def:defmaps"}, a linear map of graded vector spaces $$\Phi_* \colon \mathop{\mathrm{HH}}_\bullet(X) \rightarrow\mathop{\mathrm{HH}}_\bullet(Y),$$ and this association is functorial with respect to composition of integral kernels (Theorem [\[thm:functorial\]](#thm:functorial){reference-type="ref" reference="thm:functorial"}).

For any adjoint pair of integral kernels $\Psi\dashv\Phi$, the induced maps on homology are themselves adjoint with respect to the Mukai pairing: $${\ensuremath{\left\langle \Psi_* v,\, w\right\rangle_{\rm M}}} = {\ensuremath{\left\langle v,\, \Phi_* w\right\rangle_{\rm M}}}$$ for $v\in \mathop{\mathrm{HH}}_\bullet(Y)$, $w \in \mathop{\mathrm{HH}}_\bullet(X)$ (Theorem [\[thm:adjointness\]](#thm:adjointness){reference-type="ref" reference="thm:adjointness"}).
:::

The following are then consequences of the above basic properties:

::: Description
In all geometric situations there is a naturally defined object ${\mathbf 1}\in \mathop{\mathrm{HH}}_0({\mathsf{pt}})$. An element ${\mathscr E}$ in $\mathbf{D}(X)$ can be thought of as the kernel of an integral transform ${\mathsf{pt}}\rightarrow X$, and using functoriality of homology we define a Chern character map $$\mathop{\mathrm{ch}}\colon\mathop{\mathrm{K}}_0(X) \rightarrow\mathop{\mathrm{HH}}_0(X), \quad \mathop{\mathrm{ch}}({\mathscr E}) = {\mathscr E}_*({\mathbf 1}).$$ For a smooth proper variety the Hochschild-Kostant-Rosenberg isomorphism identifies $\mathop{\mathrm{HH}}_0(X)$ and $\bigoplus_p \mathsf H^{p,p}(X)$; our definition of the Chern character matches the usual one under this identification [@CalHH2].

For ${\mathscr E}, {\mathscr F}\in \mathbf{D}(X)$ we have $${\ensuremath{\left\langle \mathop{\mathrm{ch}}({\mathscr E}),\, \mathop{\mathrm{ch}}({\mathscr F})\right\rangle_{\rm M}}} = \chi({\mathscr E}, {\mathscr F}) = \sum_i (-1)^i \dim
  \mathop{\mathrm{Ext}}_X^i({\mathscr E}, {\mathscr F}).$$

The Hochschild structure appears naturally in the context of open-closed topological quantum field theories (TQFTs). The Riemann-Roch theorem above is a particular case of a standard constraint in these theories, the Cardy Condition. We briefly discuss open-closed TQFTs, and we argue that the natural statement of the Cardy Condition in the B-model open-closed TQFT is always satisfied, even for spaces which are not Calabi-Yau (Theorem [\[thm:cardy\]](#thm:cardy){reference-type="ref" reference="thm:cardy"}).
:::

## The 2-categorical perspective

In order to describe the functoriality of Hochschild homology it is useful to take a macroscopic point of view using a 2-category called ${\mathscr{V}\textsf{ar}}$. One way to think of this 2-category is as something half-way between the usual category consisting of spaces and maps, and ${\mathscr{C}\textsf{at}}$, the 2-category of (derived) categories, functors and natural transformations. The 2-category ${\mathscr{V}\textsf{ar}}$ has spaces as its objects, has objects of the derived category $\mathbf{D}(X\times Y)$ --- considered as integral kernels --- as its 1-morphisms from $X$ to $Y$, and has morphisms in the derived category as its 2-morphisms.

One consequence of thinking of spaces in this 2-category is that whereas in the usual category of spaces and maps two spaces are equivalent if they are isomorphic, in ${\mathscr{V}\textsf{ar}}$ two spaces are equivalent precisely when they are Fourier-Mukai partners. This is the correct notion of equivalence in many circumstances, thus making ${\mathscr{V}\textsf{ar}}$ an appropriate context in which to work.

This point of view is analogous to the situation in Morita theory in which the appropriate place to work is not the category of algebras and algebra morphisms, but rather the 2-category of algebras, bimodules and bimodule morphisms. In this 2-category two algebras are equivalent precisely when they are Morita equivalent, which again is the pertinent notion of equivalence in many situations.

Many facts about integral transforms can be stated very elegantly as facts about the 2-category ${\mathscr{V}\textsf{ar}}$. For example, the fact that every integral transform between derived categories has both a left and right adjoint is an immediate consequence of the more precise fact --- proved exactly the same way --- that every integral kernel has both a left and right adjoint in ${\mathscr{V}\textsf{ar}}$. Here the definition of an adjoint pair of 1-morphisms in a 2-category is obtained from one of the standard definitions of an adjoint pair of functors by everywhere replacing the word 'functor' by the word '1-morphism' and the words 'natural transformation' by the word '2-morphism'.

The Hochschild cohomology of a space $X$ has a very natural description in terms of the 2-category ${\mathscr{V}\textsf{ar}}$: it is the "second homotopy group of ${\mathscr{V}\textsf{ar}}$ based at $X$", which means that it is $\mathop{\mathrm{{2\mbox{-}Hom}}}_{\mathscr{V}\textsf{ar}}(\mathsf {Id}_X,\mathsf {Id}_X)$, the set of 2-morphisms from the identity 1-morphism at $X$ to itself. Unpacking this definition for ${\mathscr{V}\textsf{ar}}$ one obtains precisely $\mathop{\mathrm{Ext}}^\bullet_{X\times X}({\mathscr O}_\Delta,{\mathscr O}_\Delta)$, one of the standard definitions of Hochschild cohomology. By analogy with homotopy groups, given a kernel $\Phi\colon X\to Y$, i.e., a "path" in ${\mathscr{V}\textsf{ar}}$, one might expect an induced map $\mathop{\mathrm{HH}}^\bullet(X)\to
\mathop{\mathrm{HH}}^\bullet(Y)$ obtained by "conjugating with $\Phi$". However, this does not work, as the analogue of the "inverse path to $\Phi$" needed is a simultaneous left and right adjoint of $\Phi$, and such a thing does not exist in general as the left and right adjoints of $\Phi$ differ by the *Serre kernels* of $X$ and $Y$.

The Hochschild homology $\mathop{\mathrm{HH}}_\bullet(X)$ of a space $X$ can be given a similar natural definition in terms of ${\mathscr{V}\textsf{ar}}$ --- it is $\mathop{\mathrm{{2\mbox{-}Hom}}}_{\mathscr{V}\textsf{ar}}(\Sigma^{-1}_X,\mathsf {Id}_X)$ the set of 2-morphisms from the inverse Serre kernel of $X$ to the identity 1-morphism at $X$. In this case, the idea of "conjugating by a kernel $\Phi\colon X \to
Y$" does work as the Serre kernel in the definition exactly compensates the discrepancy between the left and right adjoints of $\Phi$.

The functoriality of Hochschild homology can be expressed by saying that $\mathop{\mathrm{HH}}_\bullet$ is a functor into the category of vector spaces from the Grothendieck category of the 2-category ${\mathscr{V}\textsf{ar}}$ (i.e., the analogue of the Grothendieck group of a 1-category) whose objects are spaces and whose morphisms are *isomorphism classes* of kernels. One aspect of this which we do not examine here is related to the fact that this Grothendieck category is actually a monoidal category with certain kinds of duals for objects and morphisms, and that Hochschild homology is a monoidal functor. The Mukai pairing is then a manifestation of the fact that spaces are self-dual in this Grothendieck category. Details will have to appear elsewhere.

There is an alternative categorical approach to defining Hochschild homology and cohomology. This approach uses the notion of enhanced triangulated categories of Bondal and Kapranov [@BonKap], which are triangulated categories arising as homotopy categories of differential-graded (dg) categories. In [@Toe], Toën argued that the Hochschild cohomology $\mathop{\mathrm{HH}}^\bullet(X)$ of a space $X$ can be regarded as the cohomology of the dg-algebra of dg-natural transformations of the identity functor on the dg-enhancement of $\mathbf{D}(X)$. It seems reasonable to expect that a similar construction can be used to define the Hochschild homology $\mathop{\mathrm{HH}}_\bullet(X)$ as dg-natural transformations from the inverse of the Serre functor to the identity. However, since the theory of Serre functors for dg-categories is not yet fully developed, we chose to use the language of the 2-category ${\mathscr{V}\textsf{ar}}$, where all our results can be made precise.

## String diagram notation

As 2-categories are fundamental to the functoriality, and they are fundamentally 2-dimensional creatures, we adopt a 2-dimensional notation. The most apt notation in this situation appears to be that of *string diagrams*, which generalizes the standard notation used for monoidal categories in quantum topology. String diagrams are Poincaré dual to the usual arrow diagrams for 2-categories. The reader unfamiliar with these ideas should be aware that the pictures scattered through this paper form rigorous notation and are not just mnemonics.

## Note

This paper supersedes the unpublished paper [@CalMPI], in which it was stated that hopefully the correct categorical context could be found for the results therein. This paper is supposed to provide the appropriate context.

## Synopsis

The paper is structured as follows. The first section is devoted to the study of integral transforms and of the 2-category ${\mathscr{V}\textsf{ar}}$. In the next section we review the Serre functor and Serre trace on the derived category, and we use these in Section [\[sec:adjoints\]](#sec:adjoints){reference-type="ref" reference="sec:adjoints"} to study adjoint kernels in ${\mathscr{V}\textsf{ar}}$. In Section [\[sec:defmaps\]](#sec:defmaps){reference-type="ref" reference="sec:defmaps"} we introduce the maps between Hochschild homology groups associated to a kernel, and we examine their functorial properties. The Mukai pairing is defined in Section [\[sec:adjoint\]](#sec:adjoint){reference-type="ref" reference="sec:adjoint"}, where we also prove its compatibility with adjoint functors. In Section [\[sec:chernchar\]](#sec:chernchar){reference-type="ref" reference="sec:chernchar"} we define the Chern character and we prove the Semi-Hirzebruch-Riemann-Roch theorem. We conclude with Section [\[sec:cardy\]](#sec:cardy){reference-type="ref" reference="sec:cardy"} where we review open-closed TQFTs, and we discuss the Cardy Condition. An appendix contains some of the more technical proofs.

## Notation

Throughout this paper $\textsf{k}$ will denote an algebraically closed field of characteristic zero and $\mathbf{D}(X)$ will denote the bounded derived category of coherent sheaves on $X$. Categories will be denoted by bold letters, such as $\mathbf{C}$, and the names of 2-categories will have a script initial letter, such as ${\mathscr{V}\textsf{ar}}$.

## The base category of spaces

We fix for the remainder of the paper a geometric category, whose objects we shall call *spaces*. It is beyond the purpose of this paper to list the axioms that this category needs to satisfy, but the following categories can be used:

-   smooth projective schemes over $\textsf{k}$;

-   smooth proper Deligne-Mumford stacks over $\textsf{k}$;

-   smooth projective schemes over $\textsf{k}$, with an action of a fixed finite group $G$, along with $G$-equivariant morphisms;

-   twisted spaces in the sense of [@Cal], i.e., smooth projective schemes over $\textsf{k}$, enriched with a sheaf of Azumaya algebras.

For any space $X$ as above, the category of coherent sheaves on $X$ makes sense, and the standard functors (push-forward, pull-back, sheaf-hom, etc.) are defined and satisfy the usual compatibility relations.

## Acknowledgments

We have greatly benefited from conversations with Jonathan Block, Tom Bridgeland, Andrew Kresch, Aaron Lauda, Eyal Markman, Mircea Mustaţă, Tony Pantev, Justin Roberts, Justin Sawon, and Sarah Witherspoon. Many of the ideas in this work were inspired by an effort to decipher the little known but excellent work [@Mar] of Nikita Markarian. Greg Moore and Tom Bridgeland suggested the connection between the Semi-Hirzebruch-Riemann-Roch theorem and the Cardy Condition in physics.

AC's initial work on this project was supported by an NSF post-doctoral fellowship, and by travel grants and hospitality from the University of Pennsylvania, the University of Salamanca, Spain, and the Newton Institute in Cambridge, England. AC's current work is supported by the National Science Foundation under Grant No. DMS-0556042. SW has been supported by a WUN travel bursary and a Royal Society Conference grant.
