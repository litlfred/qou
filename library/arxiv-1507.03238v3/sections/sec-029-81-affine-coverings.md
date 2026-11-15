---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-029-81-affine-coverings
section_title: "Affine coverings"
section_number: 8.1
pages: 20-21
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.99
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
A priori, the invariant Ptolemy varieties are only unions of quasi-affine subsets of $A(V(M))$.

::: proposition
[]{#prop:ProofAffine label="prop:ProofAffine"} The invariant Ptolemy varieties are indeed varieties. Changing the triangulation changes the varieties by biregular isomorphisms.
:::

::: proof
*Proof.* We prove this for $\overline P(\mathcal T)$; the proof for the other variants are identical. We must prove that $\overline P(\mathcal T)$ has an open affine cover. For each transitive edge set $(\mathcal T,E)$ consider the triangulation $T(E)$ defined as follows: if $E$ is non-degenerate or edge-degenerate, $T(E)=\mathcal T$; if $E$ is moderately, or simplex-degenerate, define $T(E)$ to be a triangulation $\mathcal T'$ as in Definitions [\[def:PtolemyModerate\]](#def:PtolemyModerate){reference-type="ref" reference="def:PtolemyModerate"} or [\[def:PtolemyWild\]](#def:PtolemyWild){reference-type="ref" reference="def:PtolemyWild"}, respectively. By definition, the invariant Ptolemy variety $\overline P(\mathcal T)$ is then given by $$\overline P(\mathcal T)=\bigcup_{\substack{E\in \mathop{\mathrm{T}}(\mathcal T)\setminus\{0\}\\F\in\mathop{\mathrm{T}}(T(E)),\,F_{|\mathcal T}=E}}\!\!\!\!P(T(E),F).$$ Note that all transitive edge sets $(T(E),F)$ in the above union are (at worst) edge-degenerate. Let $W\in V(M)$ be the union of all $V(T(E))$, i.e. $W$ is the set of virtual edges $e$ such that $e$ is an edge of one of the $T(E)$. By Proposition [\[prop:Embeddings\]](#prop:Embeddings){reference-type="ref" reference="prop:Embeddings"}, we may regard $\overline\mathcal P(\mathcal T)$ as a subset of the finite dimensional affine space $A(W)$. Recall that $A(W)$ is given by a coordinate $c_e$ for each virtual edge in $W$. For a transitive edge set $(\mathcal T',E')$ let $$U_{(\mathcal T',E')}=\big\{\prod_{e\in E_{\neq 0}'}c_e\neq0\big\}\in A(V(M)),$$ where $E_{\neq 0}'$ denotes the set of nonzero edges of $(\mathcal T',E')$. Clearly, $U_{(\mathcal T',E')}$ is Zariski open, and $$(\mathcal T',E')\subset(\mathcal T',E'')\iff U_{(\mathcal T',E')}\subset U_{(\mathcal T',E'')}.$$ Also, for any transitive edge sets $(T',E')$ and $(\mathcal T'',E'')$ we clearly have $$E'_{=0}\cap E''_{\neq 0}\neq \emptyset  \implies P(\mathcal T',E')\cap U_{(\mathcal T'',E'')}=\emptyset.$$ From this it follows that for any $E\in\mathop{\mathrm{T}}(\mathcal T)$ and any $F\in\mathop{\mathrm{T}}(T(E))$, we have $$\label{eq:OpenIntersect}
\overline P(\mathcal T)\cap U_{(T(E),F)} = \big(\bigcup_{(\mathcal T,E')\leq(\mathcal T,E)} P(\mathcal T,E')\big)\cap U_{(T(E),F)}\subset A(W).$$ By Proposition [\[prop:Embeddings\]](#prop:Embeddings){reference-type="ref" reference="prop:Embeddings"} the right-hand side of [\[eq:OpenIntersect\]](#eq:OpenIntersect){reference-type="eqref" reference="eq:OpenIntersect"} canonically embeds in $A(V(T(E)))$. Let $X$ be the affine variety in $A(V(T(E)))$ cut out by the Ptolemy relations, identification relations, and edge orientation relations for $T(E)$ together with the edge relations around zero-edges of $F$. Since $(T(E),F))$ is (at worst) edge-degenerate, there are no points in $X\cap U_{(T(E),F)}$ that violate transitivity, so all points in $X\cap U_{(T(E),F)}$ are in $P(\mathcal T,E')$ for some $E'\in\mathop{\mathrm{T}}(\mathcal T)$ with $(\mathcal T,E')<(\mathcal T,E)$. It thus follows from [\[eq:OpenIntersect\]](#eq:OpenIntersect){reference-type="eqref" reference="eq:OpenIntersect"} that $X\cap U_{(T(E),F)}$ equals $\overline P(\mathcal T)\cap U_{(T(E),F)}$. Since $U_{(T(E),F)}$ is the non-vanishing set of a single polynomial, $X\cap U_{(T(E),F)}$ is affine. This concludes the proof of existence of an affine cover of $\overline P(\mathcal T)$.

Given another triangulation $\mathcal T'$, $\overline P(\mathcal T)$ and $\overline P(\mathcal T')$ are clearly isomorphic as sets since both parametrize non totally degenerate decorations. The fact that they are also equal as varieties follows from the fact that the images of $\overline P(\mathcal T)$ and $\overline P(\mathcal T')$ in $A(V(M))$ are equal (see the proof of Proposition [\[prop:Embeddings\]](#prop:Embeddings){reference-type="ref" reference="prop:Embeddings"}). ◻
:::
