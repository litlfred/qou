---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-007-18-another-birational-motivation
section_title: "Another birational motivation"
section_number: 1.8
pages: 7-7
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
[]{#Sec:BirModel label="Sec:BirModel"} There is another description of $\EuScript{M}(\Sigma_2) = Q_0 \cap Q_1 \subset {\mathbb P}^5$ which, whilst not used in this paper, is undoubtedly related to the $g=2$ case of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"}, and provided motivation for the result. Let's say that a line $l \subset Q_0\cap Q_1$ is *generic* if its normal bundle is holomorphically trivial $\mathcal{O} \oplus \mathcal{O}$ (rather than $\mathcal{O}(i) \oplus \mathcal{O}(-i)$. Recall that a genus 2 curve, whilst not a complete intersection, admits an embedding as a $(2,3)$-curve on a quadric hypersurface ${\mathbb P}^1\times {\mathbb P}^1 \subset {\mathbb P}^3$.

::: Lemma
The blow-up $W \rightarrow \EuScript{M}(\Sigma_2)$ at a generic line inside $Q_0\cap Q_1$ is isomorphic to the blow-up $W' \rightarrow {\mathbb P}^3$ along an embedded genus 2 curve of degree 5.
:::

A proof is given in [@GH]. The diagram ${\mathbb P}^3 \leftarrow Bl_C({\mathbb P}^3) = Bl_l(Q_0\cap Q_1) \rightarrow Q_0\cap Q_1$ is also the simplest of the "flip-diagrams\" constructed using stable pairs by Thaddeus in [@Thaddeus] (in this special case there are actually no flips, see *op. cit.* section 3.19; the map to $Q_0\cap Q_1$ is his non-abelian Abel-Jacobi map).

If one believes that Fukaya categories should behave well under birational transformations -- a view espoused by Katzarkov and his collaborators, see for instance [@KKOY], and encouraged by the particular cases treated in this paper -- then one expects $\EuScript{F}(W)$ to be built out of $\EuScript{F}({\mathbb P}^1)$, which has two semisimple summands, and of $\EuScript{F}(\EuScript{M}(\Sigma_2))$, whilst $\EuScript{F}(W')$ should be assembled from $\EuScript{F}({\mathbb P}^3)$ (four semisimple summands) and $\EuScript{F}(\Sigma_2)$. Equating $\EuScript{F}(W)$ and $\EuScript{F}(W')$ would quickly give Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} in the case $g=2$. Whilst the argument we give is more roundabout, it seems technically simpler (because of its appeal to the special geometric features of Lefschetz fibrations), and also applies in greater generality ($g \geq 2$).
