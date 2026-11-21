---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-016-the-mukai-pairing-and-adjoint-kernels
section_title: "The Mukai pairing and adjoint kernels"
section_number: null
pages: 20-21
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#sec:adjoint label="sec:adjoint"}

In this section we define the Mukai pairing on the Hochschild homology of a space and show that the push-forwards of adjoint kernels are themselves adjoint linear maps with respect to this pairing.

First observe from Section [\[subsec:adj2functors\]](#subsec:adj2functors){reference-type="ref" reference="subsec:adj2functors"} that we have two isomorphisms: $$\tau_R,\tau_L\colon\mathop{\mathrm{HH}}_\bullet(X) = \mathop{\mathrm{Hom}}^{-\bullet}(\Sigma_X^{-1}, \mathsf {Id}_X) \xrightarrow{\sim}\mathop{\mathrm{Hom}}^\bullet(\mathsf {Id}_X, \Sigma_X),$$ given by $$\tau_R\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}\qquad\text{and} \quad
\tau_L\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}.$$ Note that this differs slightly from the given definition, but we have used the uniqueness of adjoints. The above isomorphisms allow the definition of the Mukai pairing as follows.

::: Definition
The *Mukai pairing* on the Hochschild homology of a space $X$ is the map $${\ensuremath{\left\langle {-},\, {-}\right\rangle_{\rm M}}} \colon \mathop{\mathrm{HH}}_\bullet(X) \otimes \mathop{\mathrm{HH}}_\bullet(X) \rightarrow\textsf{k},$$ defined by $${\ensuremath{\left\langle v,\, v'\right\rangle_{\rm M}}}:= \mathop{\mathrm{Tr}}\left(\tau_R(v) \circ \tau_L(v')\right).$$ Diagrammatically, this is $${\ensuremath{\left\langle \raisebox{-.45\height}{},\, \raisebox{-.45\height}{}\right\rangle_{\rm M}}}:=
  \mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\raisebox{-.45\height}{}\right).$$
:::

Observe that as $\tau_R$ and $\tau_L$ are both isomorphisms and as the Serre pairing is non-degenerate, it follows that the Mukai pairing is non-degenerate.

We can now easily show that adjoint kernels give rise to adjoint maps between the corresponding Hochschild homology groups.

::: Theorem
[]{#thm:adjointness label="thm:adjointness"} If $\Phi\colon X\to Y$ and $\Psi\colon Y\to X$ are adjoint kernels, $\Psi\dashv\Phi$, then the corresponding push forwards are adjoint with respect to the Mukai pairing in the sense that for all $w\in
  \mathop{\mathrm{HH}}_\bullet(X)$ and $v\in \mathop{\mathrm{HH}}_\bullet(Y)$ we have $${\ensuremath{\left\langle \Psi_*(v),\, w\right\rangle_{\rm M}}}={\ensuremath{\left\langle v,\, \Phi_*(w)\right\rangle_{\rm M}}}.$$
:::

::: Proof
Note first that $\Psi_*=\Phi^*$, by Theorem [\[thm:adjadj\]](#thm:adjadj){reference-type="ref" reference="thm:adjadj"}. Thus $$\begin{aligned}
    {\ensuremath{\left\langle \Psi_*(v),\, w\right\rangle_{\rm M}}}&={\ensuremath{\left\langle \Phi^*(v),\, w\right\rangle_{\rm M}}}
    =\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\raisebox{-.45\height}{}\right)\\
    &=\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\raisebox{-.45\height}{}\raisebox{-.45\height}{}\right)
    =\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\raisebox{-.45\height}{}\right)\\
    &={\ensuremath{\left\langle v,\, \Phi_*(w)\right\rangle_{\rm M}}}.\qedhere
  
\end{aligned}$$
:::

::: Corollary
If the integral kernel $\Phi\colon X \rightarrow Y$ induces an equivalence on derived categories, then $\Phi_*\colon\mathop{\mathrm{HH}}_\bullet(X) \rightarrow
  \mathop{\mathrm{HH}}_\bullet(Y)$ is an isometry.
:::

::: Proof
If $\Phi$ induces an equivalence, then it has a left adjoint $\Psi\colon Y\to X$ which induces the inverse, so $\Psi\circ\Phi\cong \mathsf {Id}_X$, and we know that $(\mathsf {Id}_X)_*$ is the identity map. Thus $${\ensuremath{\left\langle \Phi_* v,\, \Phi_* w\right\rangle_{\rm M}}} = {\ensuremath{\left\langle \Psi_* \Phi_* v,\, w\right\rangle_{\rm M}}} =
  {\ensuremath{\left\langle (\Psi\circ \Phi)_* v,\, w\right\rangle_{\rm M}}}= {\ensuremath{\left\langle v,\, w\right\rangle_{\rm M}}}.\qedhere$$
:::
