---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-019-65-an-ideal-triangulation-with-no-index-structur
section_title: "An ideal triangulation with no index structure"
section_number: 6.5
pages: 22-23
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.987
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.noindex label="sub.noindex"}

Consider an ideal triangulation $\mathcal T$ which contains an edge $e$ and a tetrahedron $\Delta_1$ such that goes around $e$ five times with shapes $Z$, $Z'$, $Z'$, $Z''$ and $Z''$. Suppose that no other tetrahedron touches $e$. Then the equation for a generalized angle structure around $e$ reads $$\alpha+ 2 \beta+ 2 \gamma=2, \qquad \alpha+ \beta+ \gamma=1$$ This forces $\alpha=0$ so no generalized angle structure has $\alpha>0$. Note that the corresponding gluing equations around the edge $e$ reads $$z (z')^2 (z'')^2 = 1, \qquad z z' z'' =-1, \qquad z'=(1-z)^{-1} \,$$ which forces $z=1$. Thus the gluing equations have no non-degenerate solution, i.e., no solution with shapes in $\mathbb C\setminus\{0,1\}$.

More complicated examples can be arranged using special configurations of two or more edges and tetrahedra. In all examples that we could generate with no index structure, the triangulation is degenerate.

Of course, the arguments of a shape solution to the gluing equations is a generalized angle structure. The latter, however, need not be an index structure if some of the shapes are real, or have negative imaginary part; see for instance the triangulation of `m064` in Section [\[sub.m064\]](#sub.m064){reference-type="ref" reference="sub.m064"}.

## Invariance under the $2 \leftrightarrow 0$ move {#sub.20move}

The next lemma implies the invariance of the index of an ideal triangulation under a $2\leftrightarrow 0$ move. Such a move is also known as a pillowcase move, described in detail in [@GHRS Sec.6].

::: lemma
[]{#lem.20move label="lem.20move"} For integers $m,e,c$ we have $$\sum_e I_{\Delta}(m,e)I_{\Delta}(m,e+c) q^e=\delta_{c,0} \,.$$
:::

::: proof
*Proof.* Equations [\[eq.QDL\]](#eq.QDL){reference-type="eqref" reference="eq.QDL"} and [\[IDQDL\]](#IDQDL){reference-type="eqref" reference="IDQDL"} imply that $$\sum_e I_{\Delta}(m,e)x^e = 
\frac{(q^{-\frac{m}{2}+1}x^{-1})_\infty}{
(q^{-\frac{m}{2}}x)_\infty} \,.$$ Since $$\frac{(q^{-\frac{m}{2}+1}x^{-1})_\infty}{
(q^{-\frac{m}{2}}x)_\infty} \cdot
\frac{(q^{-\frac{m}{2}+1}(q x^{-1})^{-1})_\infty}{
(q^{-\frac{m}{2}}(q x^{-1}))_\infty} =1 \,,$$ it follows that $$\sum_{e,e'} I_{\Delta}(m,e) x^e I_{\Delta}(m,e') q^{e'} x^{-e'}=1 \,.$$ Therefore, $$\sum_{e,e': e-e'=c} I_{\Delta}(m,e) I_{\Delta}(m,e') q^{e'} =\delta_{c,0} \,.$$ This implies that $$\sum_{e'} I_{\Delta}(m,e'+c) I_{\Delta}(m,e') q^{e'}=\delta_{c,0} \,.$$ The result follows. ◻
:::
