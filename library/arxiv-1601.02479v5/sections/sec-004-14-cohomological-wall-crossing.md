---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-004-14-cohomological-wall-crossing
section_title: "Cohomological wall-crossing"
section_number: 1.4
pages: 8-8
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.99
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson– Thomas theory for Jacobi algebras and"
---
Our second main result is a (relative) cohomological lift of the following incarnation of the wall crossing formula, with $\int$ denoting the Kontsevich--Soibelman integration map: $$\label{WCI}
\int[\mathfrak{M}^{\mathcal{S}},\upphi_{\mathop{\mathrm{Tr}}(W)}]=\prod_{\infty\xrightarrow{\upmu}-\infty}\int[\mathfrak{M}^{\upzeta\mathop{\mathrm{-ss}},\mathcal{S}}_{\upmu},\upphi_{\mathop{\mathrm{Tr}}(W)}].$$ This is an identity in the completed motivic quantum torus of finite-dimensional modules of the Jacobi algebra for the pair $(Q,W)$. Instead of defining any of the terms in ([\[WCI\]](#WCI){reference-type="ref" reference="WCI"}) we refer the reader to [@JoyceMF] and [@KS1] for more details on motivic Hall algebras and integration maps in the general theory of motivic Donaldson--Thomas invariants, or [@DaMe4] for the specific case of the motivic Hall algebra of representations of a Jacobi algebra.

We define $$\begin{aligned}
\label{relCA}
\mathop{\mathrm{\mathcal{H}}}(\mathcal{A}_W)\colonequals &\mathop{\mathrm{\mathcal{H}}}\left(\bigoplus_{\mathop{\mathrm{\mathbf{d}}}\in\mathbb{N}^{Q_0}}(\mathfrak{M}_{\mathop{\mathrm{\mathbf{d}}}}\rightarrow\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}})_*\upphi_{\mathfrak{Tr}(W)_{\mathop{\mathrm{\mathbf{d}}}}}\mathbb{Q}_{\mathfrak{M}_{\mathop{\mathrm{\mathbf{d}}}}}\otimes\mathbb{L}^{-\dim(\mathfrak{M}_{\mathop{\mathrm{\mathbf{d}}}})/2}\right)
\end{aligned}$$ where $\mathfrak{M}_{\mathop{\mathrm{\mathbf{d}}}}$ is the stack of $\mathop{\mathrm{\mathbf{d}}}$-dimensional $\mathbb{C}Q$-representations, and $\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}}$ is the coarse moduli space of $\mathop{\mathrm{\mathbf{d}}}$-dimensional $\mathbb{C}Q$-representations, the closed points of which are in bijection with $\mathop{\mathrm{\mathbf{d}}}$-dimensional semisimple $\mathbb{C}Q$-representations.

::: thmx
[]{#CWCT label="CWCT"} There is an isomorphism $$\label{gthmd}
\mathop{\mathrm{\mathcal{H}}}(\mathcal{A}_W)\cong\mbox{\larger[3]{$\boxtimes$}}_{\oplus, \infty\xrightarrow{\upmu} -\infty}^{\mathop{\mathrm{tw}}} \mathop{\mathrm{\mathcal{H}}}(\mathcal{A}_{W,\upmu}^{\upzeta}).$$ inside $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}))$. Here the product $\boxtimes_{\oplus,\infty \xrightarrow{\upmu}-\infty}^{\mathop{\mathrm{tw}}}$ is an ordered product, taken over descending slopes. Similarly, there is an isomorphism $$\label{gthmad}
\mathop{\mathrm{H}}(\mathcal{A}^{\mathcal{S}}_W)\cong \mbox{\larger[3]{$\boxtimes$}}_{+,\infty \xrightarrow{\upmu}-\infty}^{\mathop{\mathrm{tw}}} \mathop{\mathrm{H}}(\mathcal{A}^{\upzeta,\mathcal{S}}_{W,\upmu})$$ inside $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathbb{N}^{Q_0}))$.
:::

Note that in general, the individual terms in the tensor products on the right hand sides of ([\[gthmd\]](#gthmd){reference-type="ref" reference="gthmd"}) and ([\[gthmad\]](#gthmad){reference-type="ref" reference="gthmad"}) will depend on the stability condition, while the terms on the left hand side do not. The fact that very different sheaves can give rise to the same tensor product is explained by the fact that in contrast with the product $\boxtimes_{\oplus}$, the product $\boxtimes^{\mathop{\mathrm{tw}}}_{\oplus}$ is not symmetric; this is the categorification of the fact that the quantum torus utilized in [@KS1] as the target of the integration map from the motivic Hall algebra is generally not commutative.
