---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-004-14-braids-and-matrix-factorizations
section_title: "Braids and matrix factorizations"
section_number: 1.4
pages: 6-7
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.973
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Our construction of the complex of sheaves $\bbS_\beta\in D^{per}_{T_{sc}}(\Hilb_{1,n}^{free})$ is based on a homomorphism from the braid group $\Brgr_n$ to the convolution algebra of $T_{sc}$-equivariant and (weakly) $B^2$-equivariant matrix factorizations $\MF_{B^2}(\calXr_2(G_n),\Wr)$ on the space $\SymbolPrint{\calXr_2(G_n)}:=\frb\times G_n\times \frn$ with the potential $$\SymbolPrint{\Wr}=\Tr(X\Ad_g(Y)),$$ where $X\in \frb$ in upper triangular, $Y\in \frn$ is strictly upper triangular and $\SymbolPrint{G_n}=GL_n$[^1]. The potential $\Wr$ has degree $t^2$ with respect to $T_{sc}$ so we also assume that the differentials of the matrix factorizations from $\MF_{B^2}(\calXr_2( G_n),\Wr)$ have degree $t$.

In the section [\[sec: inc fun gens\]](#sec: inc fun gens){reference-type="ref" reference="sec: inc fun gens"} we prove the following

::: theorem
[]{#thm: braid realization label="thm: braid realization"} The homotopic category $\MF_{B^2}(\calXr_2(G_n),\Wr)$ has a natural monoidal structure and there is a homomorphism $$\Brgr_n\to  \MF_{B^2}(\calXr_2(G_n),\Wr),\quad \beta\mapsto \SymbolPrint{\bcalC_\beta}$$ defined by an explicit choice of images of braid generators.
:::

The construction of the homomorphism from the theorem is similar in spirit to the construction of Bezrukavnikov and Riche [@BR],

though we do not rely on the results of [@BR]

and our methods differ from their approach, mainly because we try to make our construction as explicit as it possible. Let us also remark that recently Arkhipov and Kanstrup [@AK] provided a construction of braid group action on categories matrix factorizations. We discovered our construction independently and our methods differ from theirs.

There is a similar homomorphism $\Brgr_n\to \MF_{B^2}(\calXr_2(G_n),-\Wr)$, $\beta\mapsto \bcalC'_\beta$ and, in particular, $\bcalC'_\parallel$ is the complex of the identity braid. Informally, the complex $\bbS_\beta$ should be thought as sheaf homology of the $2$-periodic complex $\bcalC_\beta\otimes \bcalC'_\parallel\in \MF_{B^2}(\calXr_2(G_n),0)$ followed by the restriction to the stable part of $\calXr_2(G_n)$ and extracting $B$ invariant part of the product ($B$ is embedded diagonally inside $B^2$).

To turn this informal definition into a rigorous mathematical construction, in section [\[sec: link inv\]](#sec: link inv){reference-type="ref" reference="sec: link inv"} we introduce an auxiliary space $\calX_\ell(G_n)$ and work with matrix factorizations on this space.

[^1]: The space $\calXr_2(G_n)$ appears naturally in the context on the Kapustin-Saulina-Rozansky topological field theory, we describe this physical theory in the forthcoming paper.
