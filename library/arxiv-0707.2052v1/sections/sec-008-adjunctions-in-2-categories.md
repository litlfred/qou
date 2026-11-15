---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-008-adjunctions-in-2-categories
section_title: "Adjunctions in 2-categories."
section_number: null
pages: 12-14
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
The notion of an adjunction in a 2-category simultaneously generalizes the notion of an adjunction between functors and the notion of a duality between objects of a monoidal category. As it is the former that arises in the context of integral transforms, we will use that as the motivation, but will come back to the latter below.

The most familiar definition of adjoint functors is as follows. For categories $\mathbf{C}$ and $\mathbf{D}$, an adjunction $\Psi\dashv \Phi$ between functors $\Psi\colon \mathbf{D}\to \mathbf{C}$ and $\Phi\colon \mathbf{C}\to \mathbf{D}$ is the specification of a natural isomorphism $$t_{a,b}\colon \mathop{\mathrm{Hom}}_\mathbf{C}(\Psi(a),b)\xrightarrow{\sim}
\mathop{\mathrm{Hom}}_\mathbf{D}(a,\Phi(b))$$ for any $a\in \mathbf{D}$ and $b\in\mathbf{C}$.

It is well known (see [@GelfandManin page 91]) that this definition is equivalent to an alternative definition of adjunction which consists of the specification of unit and counit natural morphisms, namely $$\eta\colon \mathsf {Id}_\mathbf{D}\Rightarrow \Phi\circ \Psi
\quad\text{and}\quad \epsilon\colon \Psi\circ \Phi\Rightarrow
\mathsf {Id}_\mathbf{C},$$ such that the composite natural transformations $$\Psi \stackrel{\mathsf {Id}_\Psi\circ\eta}\Longrightarrow
\Psi\circ\Phi\circ\Psi \stackrel{\epsilon\circ\mathsf {Id}_\Psi}\Longrightarrow
\Psi \quad\text{and}\quad \Phi
\stackrel{\eta\circ\mathsf {Id}_\Phi}\Longrightarrow \Phi\circ\Psi\circ\Phi
\stackrel{\mathsf {Id}_\Phi\circ\epsilon}\Longrightarrow \Phi$$ are respectively the identity natural transformation on $\Psi$ and the identity natural transformation on $\Phi$.

It is straight forward to translate between the two different definitions of adjunction. Given $\eta$ and $\epsilon$ as above, define $t_{a,b}\colon\mathop{\mathrm{Hom}}_\mathbf{C}(\Psi(a),b)\xrightarrow{\sim}
\mathop{\mathrm{Hom}}_\mathbf{D}(a,\Phi(b))$ by $t_{a,b}(f):=\Phi(f)\circ \eta_a$. The inverse of $t_{a,b}$ is defined similarly using the counit $\epsilon$. Conversely, to get the unit and counit from the natural isomorphism of hom-sets, define $\eta_a:=t_{a,\Psi(a)}(\mathsf {Id}_{\Psi(a)})$ and define $\epsilon$ similarly.

The definition involving the unit and counit is stated purely in terms of functors and natural transformations --- without mentioning objects --- thus it generalizes immediately to arbitrary 2-categories.

::: Definition
If $\mathscr{C}$ is a 2-category, $X$ and $Y$ are objects of $\mathscr{C}$, and $$\Phi\colon X \rightarrow Y\quad \text{and}\quad \Psi\colon Y \rightarrow X$$ are 1-morphisms, then an *adjunction* between $\Phi$ and $\Psi$ consists of two 2-morphisms $$\eta\colon \mathsf {Id}_Y \Rightarrow \Phi\circ\Psi \quad\text{and}\quad
\epsilon\colon \Psi\circ\Phi \Rightarrow \mathsf {Id}_X,$$ such that $$(\epsilon\circ_{\text{h}}\mathsf {Id}_\Psi)\circ_{\text{v}}(\mathsf {Id}_\Psi\circ_{\text{h}}\eta)=\mathsf {Id}_\Psi
\quad\text{and}\quad(\mathsf {Id}_\Phi\circ_{\text{h}}\epsilon)\circ_{\text{v}}(\eta\circ_{\text{h}}\mathsf {Id}_\Phi)=\mathsf {Id}_\Phi.$$ Given such an adjunction we write $\Psi\dashv\Phi$.
:::

It is worth noting that this also generalizes the notion of duality in a monoidal category, that is to say two objects are dual in a monoidal category if and only if the corresponding 1-morphisms are adjoint in the corresponding 2-category-with-one-object. Indeed, taking this point of view, May and Sigurdsson [@MaySigurdsson] refer to what is here called adjunction as duality.

It is at this point that the utility of the string diagram notation begins to be seen. Given an adjunction $\Psi\dashv\Phi$ the counit $\epsilon \colon \Psi\circ \Phi \Rightarrow\mathsf {Id}$ and the unit $\eta\colon \mathsf {Id}\Rightarrow\Phi\circ \Psi$ can be denoted as follows: $$\raisebox{-.45\height}{};\qquad \text{and}\qquad
\raisebox{-.45\height}{}.$$ However, adopting the convention of denoting the identity one-morphism by omission, it is useful just to draw the unit and counit as a cup and a cap respectively: $$\raisebox{-.45\height}{}:=\raisebox{-.45\height}{};\qquad
\text{and}\qquad \raisebox{-.45\height}{}:= \raisebox{-.45\height}{}.$$ The relations become the satisfying $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{}\quad\text{and}\quad\raisebox{-.45\height}{}=\raisebox{-.45\height}{}.$$

Adjunctions in 2-categories, as defined above, do correspond to isomorphisms of certain hom-sets but in a different way to the classical notion of adjunction. Namely, if $\Theta\colon Z\to Y$ and $\Xi\colon Z\to X$ are two other 1-morphisms, then an adjunction $\Psi\dashv \Phi$ as above gives an isomorphism $$\begin{aligned}
  \mathop{\mathrm{{2\mbox{-}Hom}}}(\Psi\circ\Theta,\Xi)&\xrightarrow{\sim}\mathop{\mathrm{{2\mbox{-}Hom}}}(\Theta,
  \Phi\circ \Xi)\\
  \raisebox{-.45\height}{}&\mapsto \raisebox{-.45\height}{}
\end{aligned}$$ The inverse isomorphism uses the counit in the obvious way.

In a similar fashion, for $\widehat\Theta\colon Y\to Z$ and $\widehat\Xi\colon
X\to Z$ two 1-morphisms, one obtains an isomorphism $$\mathop{\mathrm{{2\mbox{-}Hom}}}(\widehat\Theta\circ\Phi,\widehat\Xi)\xrightarrow{\sim}\mathop{\mathrm{{2\mbox{-}Hom}}}(\widehat\Theta,
\widehat\Xi\circ\Psi),$$ for which the reader is encouraged to draw the relevant pictures. It is worth noting that with respect to the previous isomorphism, $\Psi$ and $\Phi$ have swapped sides in all senses.

Adjunctions are unique up to a canonical isomorphism by the usual argument. This means that if $\Psi$ and $\Psi'$ are, say, both left adjoint to $\Phi$, then there is a canonical isomorphism $\Psi\stackrel{\sim}\Longrightarrow\Psi'$. This is pictured below and it is easy to check that this is an isomorphism. $$\raisebox{-.45\height}{}$$

Adjunctions are natural in the sense that they are preserved by 2-functors, so, for instance, given a pair of adjoint kernels in ${\mathscr{V}\textsf{ar}}$, the corresponding integral transforms are adjoint functors.
