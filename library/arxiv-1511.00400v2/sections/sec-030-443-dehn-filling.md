---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-030-443-dehn-filling
section_title: "Dehn filling"
section_number: 4.4.3
pages: 34-35
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.768
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
The following is a generalization to other representations of the formula for Dehn filling in Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}. In particular the same context and notation is used.

::: prop
[]{#prop:SFh label="prop:SFh"} Let $M^3$ be as above. For $\vert p\vert +\vert q\vert$ sufficiently large:

(a) For $k_1$ or $k_2$ odd, $$\tau^{k_1,k_2}(M_{p/q}^3,\sigma)=  
     {\mathbb{T}_M^{k_1,k_2}(\chi_{p/q,\sigma} )}{ 
    \prod_{i_1=0}^{k_1}\prod_{i_2=0}^{k_2}  
     \frac 1{ 1-(\lambda_{p/q})^{2 i_1-k_1} (\overline {\lambda}_{p/q})^{2 i_2-k_2} 
    } } \, .$$

(b) For $k_1$ and $k_2$ even, $k_1\neq k_2$, $$\tau^{k_1,k_2}(M_{p/q}^3)=  
     {\mathbb{T}_{M,pm+ql}^{k_1,k_2}(\chi_{p,q} )}{ 
        \prod_{(i_1,i_2)\in \mathcal I}
     \frac 1{ 1-(\lambda_{p/q})^{2 i_1-k_1} (\overline {\lambda}_{p/q})^{2 i_2-k_2} 
    } } \, ,$$ where $(i_1,i_2)\in \mathcal I$ if $0\leq i_1 \leq {k_1}$, $0\leq i_2\leq {k_2}$, and $i_1\neq \frac{k_1}{2}$ or $i_2\neq \frac{k_2}{2}$.
:::

::: cor
$$\lim_{p^2+q^2} \vert \tau^{2k}(M_{p/q}^3,\sigma)\vert =+\infty \, .$$
:::

::: proof
*Proof.* Use first Proposition [\[prop:propslift\]](#prop:propslift){reference-type="ref" reference="prop:propslift"} [\[item:ratiocurves\]](#item:ratiocurves){reference-type="eqref" reference="item:ratiocurves"} . Since the character $\chi_{p,q}$ converges to $\chi_\varrho$, $\mathbb{T}_{M,m}^{2k}(\chi_\varrho)\neq 0$, and $\vert\operatorname{cs}(pm+ql ,m )\vert=\vert p+q\,\operatorname{cs}(l,m)\vert\to\infty$, one has $$\vert {\mathbb{T}_{M,pm+ql}^{2 k}(\chi_{p,q} )}\vert \to\infty \, .$$ As $\vert\lambda_{p/q}\vert\to 1$, the surgery formula in Proposition [\[prop:SFh\]](#prop:SFh){reference-type="ref" reference="prop:SFh"} yields the result. ◻
:::

The same proof as Corollary [\[cor:dense\]](#cor:dense){reference-type="ref" reference="cor:dense"} yields:

::: cor
[]{#cor:denseh label="cor:denseh"} Given a spin structure, The set of modules of the torsions $\vert \tau^{2k_1+1,k_2}(M_{p/q}^3,\sigma)\vert$ obtained by Dehn filling on $M^3$, so that $\sigma$ can be extended, is dense in $$\left[ \frac14{\left\vert \tau^{2k_1+1,k_2} (M^3,\sigma)\right\vert},+\infty\right).$$
:::

When $k_1+k_2$ is even and $k_1 k_2\neq 0$, then $\mathbb{T}^{k_1,k_2}_M(\chi_\varrho)=0$ (for $k_i$ odd) and $\mathbb{T}^{k_1,k_2}_{M,\gamma}(\chi_\varrho)=0$ (for $k_i$ even). In this case, we cannot get conclusions from the surgery formula.
