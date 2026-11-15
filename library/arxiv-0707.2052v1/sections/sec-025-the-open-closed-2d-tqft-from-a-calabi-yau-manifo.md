---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-025-the-open-closed-2d-tqft-from-a-calabi-yau-manifo
section_title: "The open-closed 2d TQFT from a Calabi-Yau manifold."
section_number: null
pages: 28-29
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.992
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
Associated to a Calabi-Yau manifold $X$ there are two standard 2d TQFTs coming from string theory, imaginatively named the A-model and the B-model: it is the B-model we will be interested in here. In the B-model the boundary conditions are supposed to be "generated" by complex submanifolds of $X$ so the boundary conditions are taken to be complexes of coherent sheaves on $X$; the open string category is then supposed to be the derived category of coherent sheaves on $X$. This is indeed a Calabi-Yau category, which is why such categories are so named: for each ${\mathscr E}$ and ${\mathscr F}$, the requisite pairing $\mathop{\mathrm{Hom}}^\bullet_{\mathbf{D}(X)}({\mathscr E},{\mathscr F})\otimes \mathop{\mathrm{Hom}}^\bullet_{\mathbf{D}(X)}({\mathscr F},{\mathscr E})\to
\textsf{k}[-\dim X]$ comes from the Serre pairing as a Calabi-Yau manifold is precisely a manifold with a trivial canonical bundle.

According to the physics, the closed string state space $\textsf{C}$ should be $\mathop{\mathrm{Hom}}^\bullet_{\mathbf{D}(X\times X)}({\mathscr O}_\Delta,{\mathscr O}_\Delta)$, in other words, the Hochschild cohomology algebra $\mathop{\mathrm{HH}}^\bullet(X)$.

As $X$ is Calabi-Yau, a trivialization of the canonical bundle induces an isomorphism between Hochschild cohomology and Hochschild homology, up to a shift. This means that the closed string space $\textsf{C}$ has both the cohomological product and the Mukai pairing, and these make $\textsf{C}$ into a Frobenius algebra.

We need to specify the algebra maps $i_{\mathscr E}\colon \textsf{C}\to
\textsf{O}_{{\mathscr E}{\mathscr E}}$. These are maps $$i_{\mathscr E}\colon \mathop{\mathrm{Hom}}^\bullet({\mathscr O}_\Delta,{\mathscr O}_\Delta)\to
\mathop{\mathrm{Hom}}^\bullet({\mathscr E},{\mathscr E})$$ which can be given by interpreting ${\mathscr E}$ as a kernel ${\mathsf{pt}}\to X$ and taking $i_{\mathscr E}$ to be convolution with the identity on ${\mathscr E}$. This is given diagrammatically on an element $\varphi\in\mathop{\mathrm{Hom}}^\bullet({\mathscr O}_\Delta,{\mathscr O}_\Delta)$ as follows. $$\raisebox{-.45\height}{}\quad\mapsto\quad \raisebox{-.45\height}{}.$$

At this point it should be noted that $\textsf{C}$ is to be thought of as the centre of the category $\textsf{O}$. The notion of centre is generalized from algebras to categories by taking the centre of a category to be the natural transformations of the identity functor; however, in a 2-category an appropriate notion of the centre of an object is the set of 2-endomorphisms of the identity morphism on that object. This means that $\textsf{C}$ is the centre, in this sense, of the category $\textsf{O}$ in the 2-category ${\mathscr{V}\textsf{ar}}$.

The map going the other way, $i^{\mathscr E}\colon \mathop{\mathrm{Hom}}^\bullet({\mathscr E},{\mathscr E})\to
\mathop{\mathrm{Hom}}^\bullet({\mathscr O}_\Delta,{\mathscr O}_\Delta)$ is given by taking the trace, namely for $e\in \mathop{\mathrm{Hom}}_{\mathbf{D}(X)}({\mathscr E},{\mathscr E})$ the map is given by $$\raisebox{-.45\height}{}\quad\mapsto \quad\raisebox{-.45\height}{}.$$ This definition relies on the fact that $X$ is Calabi-Yau, so that the Serre kernel is, up to a shift, just the identity 1-morphism $\mathsf {Id}_X$.

An argument similar to Proposition [\[prop:iotasadjoint\]](#prop:iotasadjoint){reference-type="ref" reference="prop:iotasadjoint"} shows that $i_{\mathscr E}$ and $i^{\mathscr E}$ are adjoint. In order to argue that we indeed have an open-closed TQFT it remains to show that the Cardy Condition holds. In fact, we will prove a more general statement, the Baggy Cardy Condition.
