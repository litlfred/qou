---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-081-2422-multisummability
section_title: "Multisummability"
section_number: 24.2.2
pages: 128-129
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 1.0
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
::: prop
Let $\lambda$, $\mu\in{\mathbf C}^*$ and let $f\in{\mathbb A}_q^{[\lambda]}$ and $g\in_q^{[\mu]}$.

1.  If $[\lambda] = [\mu]$, then $fg \in {\mathbb O}_{([\lambda],\lambda])}^{2[\lambda]}$.

2.  If $[\lambda] \neq [\mu]$, then, generically $fg \notin 
    {\mathbb O}_{([\lambda],[\mu])}^{[\lambda]+[\mu]}\cup 
    {\mathbb O}_{([\mu],[\lambda])}^{[\lambda]+[\mu]}$.
:::

::: proof
*Proof.* Write $f = F/\theta_\lambda$, $g=G/\theta_\mu$; from theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}, one gets $F \in {\mathbb E}_0^{[\lambda]}$ and $G\in {\mathbb E}_0^{[\mu]}$. (The functions $\theta_\lambda$, $\theta_\mu$ were introduced just before the statement of theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}.)\
If $[\lambda] = [\mu]$, then $FG$ represents an analytic function near $0$ in ${\mathbf C}^*$, with $q$-Gevrey growth of null order on the $q$-spiral $[\lambda]$ at $0$ and $q$-Gevrey growth of order $2$ globally. To obtain the $q$-Gevrey growth order of its values on $2[\lambda]/[\lambda]$ at $0$, write: $$(FG)'(\lambda q^{-n}) = F'(\lambda q^{-n}) G(\lambda q^{-n}) +
F(\lambda q^{-n}) G'(\lambda q^{-n}),$$ which will provide the $q$-Gevrey order. Using theorem [\[theo:mniveaux\]](#theo:mniveaux){reference-type="ref" reference="theo:mniveaux"}, we get the first statement.\
For the second statement, just note that, generally, $FG$ has null $q$-Gevrey order at $0$ neither on $[\lambda]$, nor on $[\mu]$; indeed, the sequences $(F(\mu q^{-n}))$ and $(G(\lambda q^{-n}))$ have $q$-Gevrey order one. ◻
:::

Let $\lambda$, $\mu \notin [1] = q^{\mathbf Z}$. Write $f_\lambda$, resp. $f_\mu$, the solutions of the $q$-Euler equation satisfied by $\text{\tencyr\cyracc Ch}$ in ${\mathbb A}_q^{[\lambda]}$, resp. in ${\mathbb A}_q^{[\mu]}$. If $[\lambda] = [\mu]$, from the proposition above, one has: $$(f_\lambda)^2 \in {\mathbb O}_{([\lambda],\lambda])}^{2[\lambda]},$$ and this is the solution provided by theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} for equation [\[equation:carre\]](#equation:carre){reference-type="eqref" reference="equation:carre"} with $\Lambda=2[\lambda]$ and $\Lambda_1=\Lambda_2=[\lambda]$. However, if $[\lambda] \neq [\mu]$, then $f_\lambda f_\mu$ is *not* the solution provided by that theorem with $\Lambda = [\lambda]+[\mu]$ and $\{\Lambda_1,\Lambda_2\} =\{[\lambda],[\mu]\}$.
