---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-011-46-the-degree-of-i
section_title: "The degree of I"
section_number: 4.6
pages: 13-13
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.degDI label="sub.degDI"}

::: proof
*Proof.* (of Lemma [\[lem.degID\]](#lem.degID){reference-type="ref" reference="lem.degID"}) Consider the fan $F$ of $\mathbb R^2$ with rays $(1,0)$, $(0,1)$ and $(1,-1)$. Observe that the linear transformation $(m,e)\mapsto(e,-e-m)$ (which appears in Definition [\[def.Sf\]](#def.Sf){reference-type="ref" reference="def.Sf"}) rotates the three cones of the fan $F$, and preserves the piece-wise quadratic polynomial that appears in Lemma [\[lem.degID\]](#lem.degID){reference-type="ref" reference="lem.degID"}. Since $I_{\Delta}\in V$ (by Section [\[sub.isindex\]](#sub.isindex){reference-type="ref" reference="sub.isindex"}) and $V$ is pointwise invariant under $S$ (by Proposition [\[prop.S3\]](#prop.S3){reference-type="ref" reference="prop.S3"}), it suffices to compute $\delta(m,e)$ when $(m,e)$ lies in the cone $m \leq 0, e \geq 0$. In that case, Equation [\[eq.ID\]](#eq.ID){reference-type="eqref" reference="eq.ID"} gives $$I_{\Delta}(m,e)=\sum_{n=0}^\infty (-1)^n \frac{q^{\frac{1}{2}n(n+1)
-\left(n+\frac{1}{2}e\right)m}}{(q)_n(q)_{n+e}}$$ If $\delta(m,e,n)$ denotes the degree of the summand, using $m \leq 0$, $n \geq 0$ we get $$\delta(m,e,n)=\frac{1}{2}\left(n(n+1)\right) -\left(n+\frac{1}{2}e\right)m 
\geq -\frac{em}{2}\,,$$ with equality achieved uniquely at $n=0$. It follows that the degree of $I(m,e)$ in this cone is given by $-em/2$. ◻
:::
