---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-011-adjunction-as-a-2-functor
section_title: "Adjunction as a 2-functor."
section_number: null
pages: 17-17
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.984
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#subsec:adj2functors label="subsec:adj2functors"} As shown in Section [\[subsec:leftrightadjoints\]](#subsec:leftrightadjoints){reference-type="ref" reference="subsec:leftrightadjoints"}, in the 2-category ${\mathscr{V}\textsf{ar}}$ every 1-morphism, that is every kernel, $\Phi\colon X\to Y$ has a right adjoint $\Sigma_X\circ \Phi^{\scriptscriptstyle\vee}$. This can be extended to a 'right adjunction 2-functor' $\tau_R\colon
{\mathscr{V}\textsf{ar}}^\text{coop}\to {\mathscr{V}\textsf{ar}}$, where ${\mathscr{V}\textsf{ar}}^\text{coop}$ means the contra-opposite 2-category of ${\mathscr{V}\textsf{ar}}$, which is the 2-category with the same collections of objects, morphisms and 2-morphisms, but in which the direction of the morphisms and the 2-morphisms are reversed.

Before defining $\tau_R$, however, it is perhaps useful to think of the more familiar situation of a one-object 2-category with right adjoints, i.e., a monoidal category with (right) duals. So if $\mathscr{C}$ is a monoidal category in which each object $a$ has a dual $a^{\scriptscriptstyle\vee}$ with evaluation map $\epsilon_a\colon a^{\scriptscriptstyle\vee}\otimes a\to \mathbf{1}$ and coevaluation map $\eta_a\colon \mathbf{1}\to a\otimes a^{\scriptscriptstyle\vee}$, then for any morphism $f\colon a\to b$ define $f^{\scriptscriptstyle\vee}\colon b^{\scriptscriptstyle\vee}\to a^{\scriptscriptstyle\vee}$ to be the composite: $$b^{\scriptscriptstyle\vee}\xrightarrow{\mathsf {Id}\otimes \eta} b^{\scriptscriptstyle\vee}\otimes a\otimes
a^{\scriptscriptstyle\vee}\xrightarrow{\mathsf {Id}\otimes f\otimes \mathsf {Id}} b^{\scriptscriptstyle\vee}\otimes b\otimes
a^{\scriptscriptstyle\vee}\xrightarrow{\epsilon\otimes \mathsf {Id}} a^{\scriptscriptstyle\vee}.$$ This gives rise to a functor $(-)^{\scriptscriptstyle\vee}\colon \mathscr{C}^\text{op}\to \mathscr{C}$.

Now return to the case of interest and define $\tau_R\colon
{\mathscr{V}\textsf{ar}}^\text{coop}\to {\mathscr{V}\textsf{ar}}$ as follows. On spaces define $\tau_R(X):=X$. On a kernel $\Phi\colon X\to Y$ define $\tau_R(\Phi):=\Sigma_X\circ \Phi^{\scriptscriptstyle\vee}$. Finally, on morphisms of kernels define it as illustrated: $$\tau_R\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}.$$ It is a nice exercise for the reader to check that this is a 2-functor.

Clearly a left adjoint 2-functor $\tau_L\colon {\mathscr{V}\textsf{ar}}^\text{coop}\to
{\mathscr{V}\textsf{ar}}$ can be similarly created by defining it on a kernel $\Phi\colon
X\to Y$ by $\tau_L(\Phi):=\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y$ and by defining it on morphisms of kernels by $$\tau_L\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}.$$
