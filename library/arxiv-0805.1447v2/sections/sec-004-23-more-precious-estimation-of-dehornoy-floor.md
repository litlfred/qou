---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-004-23-more-precious-estimation-of-dehornoy-floor
section_title: "More precious estimation of Dehornoy floor"
section_number: 2.3
pages: 7-8
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.975
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
For later use, we prove slightly more precious estimation of Dehornoy floor than proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1).

::: prop
[]{#prop:newestimation label="prop:newestimation"} If a braid $\beta$ is conjugate to a braid $\alpha$ which is represented by braid word which contains $s$ occurrence of $\sigma_{1}$ and $k$ occurrence of $\sigma_{1}^{-1}$, then $[\beta]_{D} < max\{s,k\}$.
:::

::: proof
*Proof.* We show $\beta < \Delta^{2k}$. The proof of $\Delta^{-2s}< \beta$ is identical. By assumption, we can write $\beta = \gamma^{-1}(W_{0}\sigma_{1}W_{1}\sigma_{1}\cdots W_{k})\gamma$ where $W_{i}$ is a braid word which contains no $\sigma_{1}$ and $\gamma \in B_{n}$. We remark that we can assume $W_{0}$ is empty because we can amalgamate $W_{0}$ into conjugating element $\gamma$.

Let $\Delta' = (\sigma_{2}\sigma_{3}\cdots \sigma_{n-1})^{n-1}$. From property S, we can find a braid $\beta' = \gamma^{-1}(\sigma_{1}\Delta'^{2p}_{(1)}\sigma_{1}\cdots \Delta'^{2p}_{(k)})\gamma > \beta$ by inserting $\sigma_{1},\cdots \sigma_{n-1}$ to braid $\beta$, for sufficiently large $p>0$. We show $\beta' <\Delta^{2k}$, that is equivalent to an inequality $(\sigma_{1}\Delta'^{2p}_{(1)}\sigma_{1}\cdots \Delta'^{2p}_{(k)})\gamma < \Delta^{2k} \gamma$. First we consider the case $k=1$. We use the geometric interpretation of Dehornoy ordering. Let $D'$ be a sub-disc of $D_{n}$ which contains $2,\cdots n$-th puncture of $D_{n}$. Since $\Delta'^{2p}$ is p-times twists around $\partial D'$ and $\Delta^{2}$ is a rotation along $\partial D_{n}$, we conclude that the image of $\Delta^{2}\gamma(\Gamma)$ moves more left than $\sigma_{1}\Delta'^{2p}\gamma(\Gamma)$ for all $p$, thus $\sigma_{1}\Delta'^{2p}\gamma <\Delta^{2}\gamma$. Induction about $k$ gives desired result. ◻
:::

This proposition gives more accurate estimation of Dehornoy floor than using lemma [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1).

::: rem
Proposition [\[prop:newestimation\]](#prop:newestimation){reference-type="ref" reference="prop:newestimation"} makes results in [@mn] a bit stronger form because in [@mn] they use estimation via lemma [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1). Especially, we conclude that if $\widehat{\beta}$ admit destabilization or exchange move, then $[\beta_{D}]=0$.
:::
