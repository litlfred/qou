---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-026-73-face-degenerate-edge-sets
section_title: "Face-degenerate edge sets"
section_number: 7.3
pages: 18-19
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.846
latex_coverage_ratio: 0.971
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
::: definition
[]{#def:Descendant label="def:Descendant"} Let $\mathcal T'$ be a triangulation whose edge set contains that of $\mathcal T$. A *descendant* of $E\in\mathop{\mathrm{T}}(\mathcal T)$ is an element $E'\in\mathop{\mathrm{T}}(\mathcal T')$ such that $E'$ agrees with $E$ on the edges of $\mathcal T$. If $E'\in\mathop{\mathrm{T}}(\mathcal T')$ is a descendent of $E\in\mathop{\mathrm{T}}(\mathcal T)$ we write $E'_{|\mathcal T}=E$.
:::

::: lemma
Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be face-degenerate and suppose that there are $k$ degenerate faces. If $\mathcal T'$ is the triangulation obtained from $\mathcal T$ by performing a 2-3 move at each degenerate face then $E$ has $2^k$ descendants each of which is edge-degenerate.
:::

::: proof
*Proof.* Performing a 2-3 move adds an edge which can be either zero or nonzero without violating transitivity. In either case, none of the new faces are degenerate (see Figure [\[fig:ModerateDescendant\]](#fig:ModerateDescendant){reference-type="ref" reference="fig:ModerateDescendant"}). This concludes the proof. ◻
:::

<figure id="fig:WildDescendant">
<p><br />
</p>
<figcaption>A 2-3 move, simplex-degenerate edge set.</figcaption>
</figure>

::: definition
[]{#def:PtolemyModerate label="def:PtolemyModerate"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be face-degenerate and let $\mathcal T'$ be the triangulation obtained from $\mathcal T$ by performing 2-3 moves between all degenerate faces. Define $$\label{eq:PtolemyVarietyModerate}
P(\mathcal T,E)=\bigcup_{E'_{|\mathcal T}=E}P(\mathcal T',E'),$$ where the (clearly disjoint) union is taken inside $A(V(M))$ or the finite-dimensional $A(W)$ where $W$ is the union of all $V(\mathcal T')$. We define $P^\sigma(\mathcal T,E)$ and $\mathcal EP(\mathcal T,E)$ similiarly.
:::

::: theorem
[]{#thm:OneOneModerate label="thm:OneOneModerate"} The one-to-one correspondences [\[eq:OneOneMild\]](#eq:OneOneMild){reference-type="eqref" reference="eq:OneOneMild"}, [\[eq:OneOneMildSigma\]](#eq:OneOneMildSigma){reference-type="eqref" reference="eq:OneOneMildSigma"}, and [\[eq:OneOneMildEnhanced\]](#eq:OneOneMildEnhanced){reference-type="eqref" reference="eq:OneOneMildEnhanced"} still hold if $E$ is face-degenerate.
:::

::: proof
*Proof.* If $\mathcal T'$ is a decoration with edge set containing $\mathcal T$, the set of decorations of type $E\in\mathop{\mathrm{T}}(\mathcal T)$ is the disjoint union, over the descendants $E'$ of $E$, of the sets of decorations of type $E'$. The result now follows from Theorem [\[thm:OneOneMild\]](#thm:OneOneMild){reference-type="ref" reference="thm:OneOneMild"}. ◻
:::
