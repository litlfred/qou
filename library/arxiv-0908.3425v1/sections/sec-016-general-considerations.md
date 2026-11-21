---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-016-general-considerations
section_title: "General considerations"
section_number: null
pages: 21-22
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.986
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsec_gc label="subsec_gc"} Let us consider a physical system described by a Lagrangian which is invariant under a compact Lie group $G$. We assume the ground state of the system to be invariant under only a subgroup $H$ of $G$, giving rise to $n=n_G-n_H$ Goldstone bosons. Each of these Goldstone bosons will be described by an independent field $\phi_i$ which is a smooth real function on Minkowski space $M^4$. These fields are collected in an $n$-component vector $\Phi=(\phi_1,\cdots,\phi_n)$, defining the vector space $M_1$. Our aim is to find a mapping $\varphi$ which uniquely associates with each pair $(g,\Phi)\in G\times M_1$ an element $\varphi(g,\Phi)\in M_1$ with the following properties: $$\begin{aligned}
\label{4:2:condmap1}
&&\varphi(e,\Phi)=\Phi\,\,\forall\,\,\Phi\in M_1,\, e\,\,
\mbox{identity of}\,\, G,\\
\label{4:2:condmap2}
&&\varphi(g_1,\varphi(g_2,\Phi))=\varphi(g_1 g_2,\Phi)\,\,\forall\,\,
g_1,g_2\in G,\,\forall\,\Phi\in M_1.
\end{aligned}$$ Such a mapping defines an *operation* of the group $G$ on $M_1$. The construction proceeds as follows [@Leutwyler:1991mz:2:2]. Let $\Phi=0$ denote the "origin" of $M_1$ which, in a theory containing Goldstone bosons only, loosely speaking corresponds to the ground state configuration. Since the ground state is supposed to be invariant under the subgroup $H$ we require the mapping $\varphi$ to be such that all elements $h\in H$ map the origin onto itself. In this context the subgroup $H$ is also known as the little group of $\Phi=0$.

We will establish a connection between the Goldstone boson fields and the set of all left cosets $\{gH|g\in G\}$ which is also referred to as the quotient $G/H$. For a subgroup $H$ of $G$ the set $gH=\{gh|h\in H\}$ defines the left coset of $g$ (with an analogous definition for the right coset) which is one element of $G/H$. For our purposes we need the property that cosets either completely overlap or are completely disjoint, i.e, the quotient is a set whose elements themselves are sets of group elements, and these sets are completely disjoint. Under all elements of a given coset $gH$ the origin is mapped onto the same vector in ${\mathbbm R}^n$: $$\varphi(gh,0)=\varphi(g,\varphi(h,0))
=\varphi(g,0)\,\,\forall\,\, g\in G\,
\mbox{and}\, h\in H.$$ Secondly, the mapping is injective with respect to the elements of $G/H$. Consider two elements $g$ and $g'$ of $G$ where $g'\not\in g H$. Let us assume $\varphi(g,0)=\varphi(g',0)$: $$0=\varphi(e,0)=\varphi(g^{-1}g,0)
=\varphi(g^{-1},\varphi(g,0))
=\varphi(g^{-1},\varphi(g',0))=\varphi(g^{-1}g',0).$$ However, this implies $g^{-1}g'\in H$ or $g'\in gH$ in contradiction to the assumption $g'\not\in g H$ and therefore $\varphi(g,0)=\varphi(g',0)$ cannot be true. In other words, the mapping can be inverted on the image of $\varphi(g,0)$. The conclusion is that there exists an *isomorphic mapping* between the quotient $G/H$ and and the Goldstone boson fields. Of course, the Goldstone boson fields are not constant vectors in ${\mathbbm R}^n$ but functions on Minkowski space. This is accomplished by allowing the cosets $gH$ to also depend on $x$.

Now let us discuss the transformation behavior of the Goldstone boson fields under an arbitrary $g\in G$ in terms of the isomorphism established above. To each $\Phi$ corresponds a coset $\tilde{g}H$ with appropriate $\tilde{g}$. Let $f=\tilde{g}h\in \tilde{g}H$ denote a representative of this coset such that $$\Phi=\varphi(f,0)=\varphi(\tilde{g}h,0).$$ Now apply the mapping $\varphi(g)$ to $\Phi$: $$\varphi(g,\Phi)=\varphi(g,\varphi(\tilde{g}h,0))
=\varphi(g\tilde{g}h,0)=\varphi(f',0)=\Phi',\quad
f'\in g(\tilde{g}H).$$ In order to obtain the transformed $\Phi'$ from a given $\Phi$ we simply need to multiply the left coset $\tilde{g}H$ representing $\Phi$ by $g$ in order to obtain the new left coset representing $\Phi'$: $$\begin{aligned}
\Phi &\stackrel{g}{\to} &\Phi'\\
\downarrow&&\uparrow\\
\tilde g H&\stackrel{g}{\to}&g\tilde g H
\end{aligned}$$ This procedure uniquely determines the transformation behavior of the Goldstone bosons up to an appropriate choice of variables parameterizing the elements of the quotient $G/H$.
