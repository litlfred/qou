---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-024-71-edge-degenerate-edge-sets
section_title: "Edge-degenerate edge sets"
section_number: 7.1
pages: 16-18
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 0.949
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Let $E\in\mathop{\mathrm{T}}(\mathcal T)$ be edge-degenerate. Then each face of $\mathcal T$ has at most one zero-edge.

::: proposition
[]{#prop:RecoverDec label="prop:RecoverDec"} Let $c$ be a Ptolemy assignment on a simplex $\Delta$. If each face has at most one Ptolemy coordinate which is zero, then $c$ is the Ptolemy assignment of a unique decoration.
:::

::: proof
*Proof.* By reordering the vertices if necessary, we may assume that $c_{01}$, $c_{12}$ and $c_{23}$ are nonzero. Let $$g_0=I,\quad g_1=q(c_{01}),\quad g_2=g_1x(\frac{c_{02}}{c_{01}c_{12}})q(c_{12}),\quad g_3=g_2x(\frac{c_{13}}{c_{12}c_{23}})q(c_{23}).$$ The Ptolemy coordinates of the decoration $(g_0P,g_1P,g_2P,g_3P)$ then agree with $c$ as is shown by explicitly computing $\det\big(g_{i}\left(\begin{smallmatrix}1\\0\end{smallmatrix}\right),g_{j}\left(\begin{smallmatrix}1\\0\end{smallmatrix}\right)\big)$. Uniqueness follows from Corollary [\[cor:LocalOneToOne\]](#cor:LocalOneToOne){reference-type="ref" reference="cor:LocalOneToOne"} since the natural cocycle is determined up to coboundaries by the Ptolemy coordinates (Proposition [\[prop:ConcreteFormula\]](#prop:ConcreteFormula){reference-type="ref" reference="prop:ConcreteFormula"}). ◻
:::

Let $C(E)$ be a union of disjoint cylindrical neighborhoods of the zero-edges of $E$. The space $M\setminus C(E)$ decomposes as a union of truncated simplices with the zero-edges being "chopped" (see Figure [\[fig:ChoppedCocycle\]](#fig:ChoppedCocycle){reference-type="ref" reference="fig:ChoppedCocycle"}).

::: corollary
[]{#cor:ChoppedCocycle label="cor:ChoppedCocycle"} A Ptolemy assignment $c$ of type $E$ canonically determines a $G$-cocycle on the space $M\setminus C(E)$.
:::

::: proof
*Proof.* By Proposition [\[prop:RecoverDec\]](#prop:RecoverDec){reference-type="ref" reference="prop:RecoverDec"} and Corollary [\[cor:LocalOneToOne\]](#cor:LocalOneToOne){reference-type="ref" reference="cor:LocalOneToOne"}, $c$ determines up to coboundaries a Bruhat cocycle on each truncated simplex. By Proposition [\[prop:ConcreteFormula\]](#prop:ConcreteFormula){reference-type="ref" reference="prop:ConcreteFormula"}, all the long edges are canonically determined by the Ptolemy coordinates, but a short edge near a zero-edge is only determined up to the coboundary action. However, as shown in Figure [\[fig:ChoppedCocycle\]](#fig:ChoppedCocycle){reference-type="ref" reference="fig:ChoppedCocycle"}, each chopped truncated simplex inherits canonical edge labelings. The fact that the chopped cocycles match up follows from the identification relations. ◻
:::

<figure id="fig:RemoveCylinder">
<p><br />
</p>
<figcaption>The cocycle extends if and only if the edge relation holds.</figcaption>
</figure>

The link of each zero-edge is a complex $K$ as in Section [\[sec:EdgeRelations\]](#sec:EdgeRelations){reference-type="ref" reference="sec:EdgeRelations"} (embedded in $\scalerel*{\widehat{\widetilde M}}{\widetilde{M^2}}$) and since $E$ is only edge-degenerate, the top and bottom edges of $K$ are all nonzero. Hence, for a Ptolemy assignment of type $E$ the edge relations (Definition [\[def:EdgeRelation\]](#def:EdgeRelation){reference-type="ref" reference="def:EdgeRelation"}) around each zero-edge are well defined.

::: definition
[]{#def:PtolemyMild label="def:PtolemyMild"} Let $E$ be edge-degenerate. The Ptolemy variety $P(\mathcal T,E)$ is the quasi-affine algebraic set defined by the usual relations (as in Definition [\[def:PtolemyVariety\]](#def:PtolemyVariety){reference-type="ref" reference="def:PtolemyVariety"}) together with the edge relations [\[eq:EdgeRelations\]](#eq:EdgeRelations){reference-type="eqref" reference="eq:EdgeRelations"} around zero-edges and the relations $c_e=0$ if $e$ is a zero-edge and $c_e\neq 0$ otherwise.
:::

Note that each element in $P(\mathcal T,E)$ is a Ptolemy assignment of type $E$.

::: theorem
[]{#thm:OneOneMild label="thm:OneOneMild"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be edge-degenerate. There is a one-to-one correspondence $$\label{eq:OneOneMild}
\left\{\txt{Decorated, boundary-unipotent\\representations of type $E$}\right\}\overset{\text{1:1}}{\longleftrightarrow}P(\mathcal T,E)\overset{\text{1:1}}{\longleftrightarrow}\left\{\txt{Bruhat cocycles of type $E$\\ up to coboundaries}\right\}$$
:::

::: proof
*Proof.* By Theorem [\[thm:OneToOneGeneral\]](#thm:OneToOneGeneral){reference-type="ref" reference="thm:OneToOneGeneral"} all we need to prove is that a Ptolemy assignment of type $E$ determines a Bruhat cocycle. By Corollary [\[cor:ChoppedCocycle\]](#cor:ChoppedCocycle){reference-type="ref" reference="cor:ChoppedCocycle"}, we have a canonical cocycle on $M\setminus C(E)$. By the van Kampen theorem this extends to a Bruhat cocycle on $M$ if and only if the product of the labelings around each cylinder is $I$, which is a consequence of the edge relations. The freedom in the choice of extension is exactly the coboundary action (see e.g. Remark [\[rm:CoboundaryAction\]](#rm:CoboundaryAction){reference-type="ref" reference="rm:CoboundaryAction"}). ◻
:::

::: definition
For $\sigma\in H^2(\widehat M;\mathbb Z/2\mathbb Z)$ define $P^\sigma(\mathcal T,E)$ as in Definition [\[def:PtolemyMild\]](#def:PtolemyMild){reference-type="ref" reference="def:PtolemyMild"}, but using the identification relations [\[eq:EdgeIdentificationsSigma\]](#eq:EdgeIdentificationsSigma){reference-type="eqref" reference="eq:EdgeIdentificationsSigma"}.
:::

::: theorem
[]{#thm:OneOneMildSigma label="thm:OneOneMildSigma"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be edge-degenerate. There is a one-to-one correspondence $$\label{eq:OneOneMildSigma}
\xy*[c]\xybox{\xymatrix{
\left\{\txt{Type $E$ decorated\\boundary-unipotent\\$\pi_1(M)\to\mathop{\mathrm{PSL}}(2,\mathbb C)$}\right\}\ar@/_1pc/@{<->}[rr]_-{1:1}&P^\sigma(\mathcal T,E)\ar[l]_-{1:k}\ar[r]^-{k:1}&\left\{\txt{Bruhat $\mathop{\mathrm{PSL}}(2,\mathbb C)$-cocycles\\type $E$, obstruction class $\sigma$\\up to coboundaries}\right\},}}\endxy$$
:::

::: proof
*Proof.* As in the proof of Theorem [\[thm:OneOneMild\]](#thm:OneOneMild){reference-type="ref" reference="thm:OneOneMild"} an element in $P^\sigma(\mathcal T,E)$ determines a Bruhat cocycle up to coboundaries. The fact that this map is $k:1$ follows from the elementary fact that two Ptolemy assignments determine the same Bruhat cocycle if and only if they differ by an element in $Z^1(\widehat M;\mathbb Z/2\mathbb Z)$. ◻
:::

::: definition
For $M$ as in Section [\[sec:Enhanced\]](#sec:Enhanced){reference-type="ref" reference="sec:Enhanced"} define the enhanced Ptolemy variety $\mathcal EP(\mathcal T,E)$ as in Definition [\[def:PtolemyMild\]](#def:PtolemyMild){reference-type="ref" reference="def:PtolemyMild"} using the identification relations from Definition [\[def:EnhancedPtolemy\]](#def:EnhancedPtolemy){reference-type="ref" reference="def:EnhancedPtolemy"} and the edge relations [\[eq:EdgeEquationsEnhanced\]](#eq:EdgeEquationsEnhanced){reference-type="eqref" reference="eq:EdgeEquationsEnhanced"}.
:::

::: theorem
[]{#thm:OneOneMildEnhanced label="thm:OneOneMildEnhanced"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be edge-degenerate and $M$ as in Section [\[sec:Enhanced\]](#sec:Enhanced){reference-type="ref" reference="sec:Enhanced"}. There is a one-to-one correspondence $$\label{eq:OneOneMildEnhanced}
\left\{\txt{Decorated representations\\of type $E$}\right\}\overset{\text{1:1}}{\longleftrightarrow}\mathcal EP(\mathcal T,E)\overset{\text{1:1}}{\longleftrightarrow}\left\{\txt{Fattened Bruhat cocycles of type $E$\\ up to coboundaries}\right\}$$
:::

::: proof
*Proof.* The proof is identical to that of Theorem [\[thm:OneOneMild\]](#thm:OneOneMild){reference-type="ref" reference="thm:OneOneMild"} using the fattened decomposition and the geometric interpretation of the edge relations [\[eq:EdgeEquationsEnhanced\]](#eq:EdgeEquationsEnhanced){reference-type="eqref" reference="eq:EdgeEquationsEnhanced"} given in Figure [\[fig:FatEdgeRelationTop\]](#fig:FatEdgeRelationTop){reference-type="ref" reference="fig:FatEdgeRelationTop"}. ◻
:::
