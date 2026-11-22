---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-018-5-the-edge-relations
section_title: "The edge relations"
section_number: 5
pages: 13-14
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.967
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:EdgeRelations label="sec:EdgeRelations"} We now define a relation among the Ptolemy coordinates of a decorated (boundary-unipotent) representation. This relation is a consequence of the Ptolemy relations in the case when all Ptolemy coordinates are nonzero, but if some Ptolemy coordinates are zero, this relation is independent of the Ptolemy relations. Hence, when defining the invariant Ptolemy variety this relation must be imposed in addition to the Ptolemy relations.

Let $K$ be the space obtained by cyclically gluing together ordered simplices $\Delta_0,\dots,\Delta_{N-1}$ along a common edge. We order the vertices of each simplex such that the common edge is the $01$ edge of each simplex, and such that the orientations induced by the orderings agree (see Figure [\[fig:EdgeNbh\]](#fig:EdgeNbh){reference-type="ref" reference="fig:EdgeNbh"}). We refer to the edges (other than the common edge) as *top*, *bottom*, and *center* edges respectively.

::: lemma
[]{#lemma:edgeRelationEquivalence label="lemma:edgeRelationEquivalence"} Let $c$ be a Ptolemy assignment on $K$ where all the Ptolemy coordinates of the top and bottom edges of $K$ are nonzero. We then have $$\label{eq:EdgeRelations}
\sum_{k=0}^{N-1} \frac{c_{23,k}}{c_{12,k}c_{13,k}}=0\iff\sum_{k=0}^{N-1}\frac{c_{23,k}}{c_{02,k}c_{03,k}}=0.$$ Moreover, if the Ptolemy coordinate $c_{01}$ of the interior edge is also nonzero, both equations are satisfied.
:::

::: proof
*Proof.* We first assume that $c_{01}\neq 0$. We have $$\label{eq:First}
\begin{aligned}
c_{01}\sum_{k=0}^{N-1} \frac{c_{23,k}}{c_{12,k}c_{13,k}}&=\sum_{k=0}^{N-1} \frac{c_{02,k}c_{13,k}-c_{03,k}c_{12,k}}{c_{12,k}c_{13,k}}\\
&=\sum_{k=0}^{N-1} \frac{c_{03,k-1}c_{13,k}-c_{03,k}c_{13,k-1}}{c_{13,k-1}c_{13,k}}\\
&=\sum_{k=0}^{N-1}\Big(\frac{c_{03,k-1}}{c_{13,k-1}}-\frac{c_{03,k}}{c_{13,k}}\big)\\
&=0.
\end{aligned}$$ Here, the first equality follows from the Ptolemy relations [\[eq:PtolemyRelation\]](#eq:PtolemyRelation){reference-type="eqref" reference="eq:PtolemyRelation"}, and the second from the identification relations $c_{12,k}=c_{13,k-1}$ and $c_{02,k}=c_{03,k-1}$ (indices modulo $N$). By a similar computation, one also has $$\label{eq:Second}
c_{01}\sum_{k=0}^{N-1} \frac{c_{23,k}}{c_{02,k}c_{03,k}}=0.$$ Since we are assuming that $c_{01}\neq 0$, [\[eq:First\]](#eq:First){reference-type="eqref" reference="eq:First"} and [\[eq:Second\]](#eq:Second){reference-type="eqref" reference="eq:Second"} together prove the second statement.

If $c_{01}=0$, the Ptolemy relations become $c_{03,k}c_{12,k}=c_{02,k}c_{13,k}$, which together with the identification relations $c_{12,k}=c_{13,k-1}$ and $c_{02,k}=c_{03,k-1}$ imply that the ratio between $c_{12,k}c_{13,k}$ and $c_{02,k}c_{03,k}$ is independent of $k$. This concludes the proof. ◻
:::

<figure id="fig:EdgeRelationTop">
<p><br />
</p>
<figcaption>Bruhat cocycle on <span class="math inline">$\overline K$</span> (near top vertex).</figcaption>
</figure>

::: definition
[]{#def:EdgeRelation label="def:EdgeRelation"} We call the (equivalent) relations [\[eq:EdgeRelations\]](#eq:EdgeRelations){reference-type="eqref" reference="eq:EdgeRelations"} *edge relations* around the center edge of $K$.
:::

::: remark
When all Ptolemy coordinates are nonzero, the fundamental correspondence provides a natural cocycle on the space $\overline K$ obtained from $K$ by truncating the simplices. In this case, the edge relations are equivalent to the relation coming from the fact that the product of short edges around the top and bottom is $I$ (see Figure [1](#fig:EdgeRelationTop){reference-type="ref" reference="fig:EdgeRelationTop"}). When some of the Ptolemy coordinates are zero this relation is no longer automatically satisfied and must be imposed.
:::

## Edge relations for $\mathop{\mathrm{PSL}}(2,\mathbb C)$ Ptolemy assignments

The obvious analogue of Lemma [\[lemma:edgeRelationEquivalence\]](#lemma:edgeRelationEquivalence){reference-type="ref" reference="lemma:edgeRelationEquivalence"} for $\mathop{\mathrm{PSL}}(2,\mathbb C)$ Ptolemy assignments still holds and we define the edge relations for $\mathop{\mathrm{PSL}}(2,\mathbb C)$ Ptolemy assignments by the exact same formula [\[eq:EdgeRelations\]](#eq:EdgeRelations){reference-type="ref" reference="eq:EdgeRelations"}.
