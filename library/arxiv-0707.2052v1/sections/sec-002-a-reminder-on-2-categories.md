---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-002-a-reminder-on-2-categories
section_title: "A reminder on 2-categories."
section_number: null
pages: 7-10
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.987
---
We will review the notion of a 2-category at the same time as introducing the notation we will be using. Recall that a 2-category consists of three levels of structure: objects; 1-morphisms between objects; and 2-morphisms between 1-morphisms. It is worth mentioning a few examples to bear in mind during the following exposition.

-   The first example is the 2-category ${\mathscr{C}\textsf{at}}$ of categories, functors and natural transformations.

-   The second example is rather a family of examples. There is a correspondence between 2-categories with one object $\star$ and monoidal categories. For any monoidal category the objects and morphisms give respectively the 1-morphisms and 2-morphisms of the corresponding 2-category.

-   The third example is the 2-category ${\mathscr{A}\textsf{lg}}$ with algebras over some fixed commutative ring as its objects, with the set of $A$-$B$-bimodules as its 1-morphisms from $A$ to $B$, where composition is given by tensoring over the intermediate algebra, and with bimodule morphisms as its 2-morphisms.

There are various ways of notating 2-categories: the most common way is to use *arrow diagrams*, however the most convenient way for the ideas in this paper is via *string diagrams* which are Poincaré dual to the arrow diagrams. In this subsection we will draw arrow diagrams on the left and string diagrams on the right to aid the reader in the use of string diagrams.

Recall the idea of a 2-category. For any pair of objects $X$ and $Y$ there is a collection of morphisms $\mathop{\mathrm{1\mbox{-}Hom}}(X,Y)$; if $\Phi\in\mathop{\mathrm{1\mbox{-}Hom}}(X,Y)$ is a 1-morphism then it is drawn as below. $$\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}$$ These 1-dimensional pictures will only appear as the source and target of 2-morphism, i.e., the top and bottom of the 2-dimensional pictures we will be using. In general 1-morphisms will be denoted by their identity 2-morphisms, see below.

If $\Phi,\Phi'\in\mathop{\mathrm{1\mbox{-}Hom}}(X,Y)$ are parallel 1-morphisms --- meaning simply that they have the same source and target --- then there is a set of 2-morphisms $\mathop{\mathrm{{2\mbox{-}Hom}}}(\Phi,\Phi')$ from $\Phi$ to $\Phi'$. If $\alpha\in\mathop{\mathrm{{2\mbox{-}Hom}}}(\Phi,\Phi')$ is a 2-morphism then it is drawn as below. $$\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}$$ At this point make the very important observation that diagrams are read from right to left and from bottom to top.

There is a *vertical composition* of 2-morphisms so that if $\alpha\colon\Phi\Rightarrow\Phi'$ and $\alpha'\colon\Phi'\Rightarrow\Phi''$ are 2-morphisms then the vertical composite $\alpha'\circ_{\text{v}}\alpha\colon\Phi\Rightarrow\Phi''$ is defined and is denoted as below. $$\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}$$ This vertical composition is strictly associative so that $(\alpha''\circ_{\text{v}}\alpha')\circ_{\text{v}}\alpha
=\alpha''\circ_{\text{v}}(\alpha'\circ_{\text{v}}\alpha)$ whenever the three 2-morphisms are composable. Moreover, there is an identity 2-morphism $\mathsf {Id}_\Phi\colon \Phi\Rightarrow \Phi$ for every 1-morphism $\Phi$ so that $\alpha\circ_{\text{v}}\mathsf {Id}_\Phi=\alpha=\mathsf {Id}_{\Phi'}\circ_{\text{v}}\alpha$ for every 2-morphism $\alpha\colon\Phi\Rightarrow\Phi'$. This means that for every pair of objects $X$ and $Y$, the 1-morphisms between them are the objects of a category $\mathop{\mathrm{\textbf{\textsf{Hom}}}}(X,Y)$, with the 2-morphisms forming the morphisms. In the string notation the identity 2-morphisms are usually just drawn as straight lines. $$\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}$$

There is also a composition for 1-morphisms, so if $\Phi\colon X\to Y$ and $\Psi \colon Y\to Z$ are 1-morphisms then the composite $\Psi\circ
\Phi\colon X\to Z$ is defined and is denoted as below. $$\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}$$ Again, these pictures will only appear at the top and bottom of 2-morphisms. This composition of 1-morphisms is not required to be strictly associative, but it is required to be associative up to a *coherent* 2-isomorphism. This means that for every composable triple $\Theta$, $\Psi$ and $\Phi$ of 1-morphisms there is a specified 2-isomorphism $(\Theta\circ\Psi)\circ\Phi
\stackrel\sim\Longrightarrow\Theta\circ(\Psi\circ\Phi)$ and these 2-isomorphisms have to satisfy the so-called pentagon coherency condition which ensures that although $\Theta\circ\Psi\circ\Phi$ is ambiguous, it can be taken to mean either $(\Theta\circ\Psi)\circ\Phi$ or $\Theta\circ(\Psi\circ\Phi)$ without confusion. The up-shot of this is that parentheses are unnecessary in the notation.

Each object $X$ also comes with an identity 1-morphism $\mathsf {Id}_X$, but again, in general, one does not have equality of ${\mathsf {Id}_Y}\circ \Phi$, $\Phi$ and $\Phi\circ\mathsf {Id}_X$, but rather the identity 1-morphisms come with coherent 2-isomorphisms ${\mathsf {Id}_Y}\circ\Phi\stackrel\sim
\Rightarrow\Phi$, and $\Phi\circ\mathsf {Id}_X\stackrel\sim\Rightarrow\Phi$. Again this means that in practice the identities can be neglected in the notation: so although we could denote the identity 1-morphism with, say, a dotted line, we choose not to. This is illustrated below. $$\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}$$

A *strict* 2-category is one in which the coherency 2-isomorphisms for associativity and identities are themselves all identities. So the 2-category ${\mathscr{C}\textsf{at}}$ of categories, functors and natural transformations is a strict 2-category.

The last piece of structure that a 2-category has is the *horizontal composition* of 2-morphisms. If $\Phi,\Phi'\colon
X\to Y$ and $\Psi,\Psi'\colon Y\to Z$ are 1-morphisms, and $\alpha\colon \Phi\Rightarrow\Phi'$ and $\beta\colon
\Psi\Rightarrow\Psi'$ are 2-morphisms, then $\beta\circ_{\text{h}}\alpha\colon
\Psi\circ\Phi\Rightarrow\Psi'\circ\Phi'$ is defined, and is notated as below. $$\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}\quad\raisebox{-.45\height}{}\equiv\raisebox{-.45\height}{}$$ The horizontal and vertical composition are required to obey the *interchange law*. $$(\beta'\circ_{\text{v}}\beta)\circ_{\text{h}}(\alpha'\circ_{\text{v}}\alpha)=
(\beta'\circ_{\text{h}}\alpha')\circ_{\text{v}}(\beta\circ_{\text{h}}\alpha).$$ This means that the following diagrams are unambiguous. $$\raisebox{-.45\height}{}\qquad\raisebox{-.45\height}{}$$ It also means that 2-morphisms can be 'slid past' each other in the following sense. $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{}$$

From now on, string diagrams will be drawn without the grey borders, and labels will be omitted if they are clear from the context.

## The 2-category ${\mathscr{V}\textsf{ar}}$.

The 2-category ${\mathscr{V}\textsf{ar}}$, of spaces and integral kernels, is defined as follows. The objects are spaces, as defined in the introduction, and the hom-category $\mathop{\mathrm{\textbf{\textsf{Hom}}}}_{\mathscr{V}\textsf{ar}}(X,Y)$ from a space $X$ to a space $Y$ is the derived category $\mathbf{D}(X\times Y)$, which is to be thought of as the category of integral kernels from $X$ to $Y$. Explicitly, this means that the 1-morphisms in ${\mathscr{V}\textsf{ar}}$ from $X$ to $Y$ are objects of $\mathbf{D}(X\times Y)$ and the 2-morphisms from $\Phi$ to $\Phi'$ are morphisms in $\mathop{\mathrm{Hom}}_{\mathbf{D}(X\times Y)}(\Phi,\Phi')$, with vertical composition of 2-morphisms just being usual composition in the derived category.

Composition of 1-morphisms in ${\mathscr{V}\textsf{ar}}$ is defined using the convolution of integral kernels: if $\Phi\in \mathbf{D}(X\times Y)$ and $\Psi\in
\mathbf{D}(Y\times Z)$ are 1-morphisms then define the convolution $\Psi\circ\Phi\in\mathbf{D}(X\times Z)$ by $$\Phi\circ \Psi := \pi^{}_{XZ, *} ( \pi_{YZ}^* \Psi \otimes
\pi_{XY}^* \Phi),$$ where $\pi_{XZ}$, $\pi_{XY}$ and $\pi_{YZ}$ are the projections from $X\times Y\times Z$ to the appropriate factors. The horizontal composition of 2-morphisms is similarly defined. Finally, the identity 1-morphism $\mathsf {Id}_X\colon X\rightarrow X$ is given by ${\mathscr O}_{\Delta}\in \mathbf{D}(X\times X)$, the structure sheaf of the diagonal in $X\times X$.

The above 2-category is really what is at the heart of the study of integral transforms, and it is entirely analogous to ${\mathscr{A}\textsf{lg}}$, the 2-category of algebras described above. For example, the Hochschild cohomology groups of a space $X$ arise as the second homotopy groups of the 2-category ${\mathscr{V}\textsf{ar}}$, at $X$: $$\begin{aligned}
  \mathop{\mathrm{HH}}^\bullet(X) &:=\mathop{\mathrm{Ext}}_{X\times X}^\bullet({\mathscr O}_\Delta,{\mathscr O}_\Delta)
  \cong \mathop{\mathrm{Hom}}^\bullet_{D(X\times X)}({\mathscr O}_\Delta,{\mathscr O}_\Delta)\\
  &=:\mathop{\mathrm{{2\mbox{-}Hom}}}_{{\mathscr{V}\textsf{ar}}}(\mathsf {Id}_X,\mathsf {Id}_X).
\end{aligned}$$

There is a 2-functor from ${\mathscr{V}\textsf{ar}}$ to ${\mathscr{C}\textsf{at}}$ which encodes integral transforms: this 2-functor sends each space $X$ to its derived category $\mathbf{D}(X)$, sends each kernel $\Phi\colon X\to Y$ to the corresponding integral transform $\overline \Phi\colon D(X)\to D(Y)$, and sends each map of kernels to the appropriate natural transformation. Many of the statements about integral transforms have better formulations in the language of the 2-category ${\mathscr{V}\textsf{ar}}$.
