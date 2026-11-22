---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-016-42-bruhat-cocycles
section_title: "Bruhat cocycles"
section_number: 4.2
pages: 11-13
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.868
latex_coverage_ratio: 0.947
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:BruhatCocycle label="sec:BruhatCocycle"}

::: definition
A *Bruhat cocycle* is a natural cocycle as in Definition [\[def:NaturalCocycle\]](#def:NaturalCocycle){reference-type="ref" reference="def:NaturalCocycle"}, but where long edges may be either diagonal or counter-diagonal. A zero-cochain $\eta\colon V(\overline\mathcal T)\to P$ *preserves* a Bruhat cocycle $\tau$ if $\eta\tau$ is again a Bruhat cocycle.
:::

The motivation for our definition is the following corollary of the Bruhat decomposition theorem.

::: lemma
[]{#lemma:Bruhat label="lemma:Bruhat"} Let $gP$ and $hP$ be cosets. If $gB\neq hB$ there are unique coset representatives $gx_0$ and $hx_1$ such that $(gx_0)^{-1}hx_1$ is counterdiagonal. If $gB=hB$ there are (not unique) coset representatives such that $(gx_0)^{-1}hx_1$ is diagonal.
:::

::: proof
*Proof.* By Bruhat decomposition, every $g\in G$ can be decomposed as $b_1wb_2$, where $w$ is either $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ or $\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)$ and $b_i\in B$. The result is an elementary consequence. ◻
:::

::: corollary
[]{#cor:LocalOneToOne label="cor:LocalOneToOne"} For every decoration $D=(g_0P,g_1P,g_2P,g_3P)$ of a simplex $\Delta$ there exists a Bruhat cocycle $\tau$ on the corresponding truncated simplex $\overline\Delta$ compatible with $D$. Moreover $\tau$ is unique up to coboundaries preserving $\tau$.
:::

::: proof
*Proof.* Lemma [\[lemma:Bruhat\]](#lemma:Bruhat){reference-type="ref" reference="lemma:Bruhat"} provides the existence of a map $\eta\colon V(\overline\Delta)\to G$ such that $\delta\eta$ is a Bruhat cocycle (see Figure [1](#fig:NaturalCocycleDefn){reference-type="ref" reference="fig:NaturalCocycleDefn"}). Uniqueness up to coboundaries and compatiblity with $D$ is immediate from the construction. ◻
:::

The following is the global analogue of Corollary [\[cor:LocalOneToOne\]](#cor:LocalOneToOne){reference-type="ref" reference="cor:LocalOneToOne"}.

::: theorem
[]{#thm:OneToOneGeneral label="thm:OneToOneGeneral"} There is a one-to-one correspondence $$\label{eq:OneToOneGeneral}
\left\{\txt{Decorated boundary-unipotent\\
$\mathop{\mathrm{SL}}(2,\mathbb C)$-representations}\right\}\overset{1:1}{\longleftrightarrow}\left\{\txt{Bruhat cocycles $\tau$ up to\\coboundaries preserving $\tau$}\right\}.$$
:::

::: proof
*Proof.* We must show that given a decoration $D$ there exists a Bruhat cocycle $\tau$ compatible with $D$ and that $\tau$ is unique up to the action by coboundaries preserving $\tau$. A decoration $D\colon I(\widetilde M)\to\mathop{\mathrm{SL}}(2,\mathbb C)/P$ of a representation $\rho$ determines a map $\Gamma\colon V(\scalerel*{\widetilde{\overline\mathcal T}}{\widetilde{T^2}})\to \mathop{\mathrm{SL}}(2,\mathbb C)/P$ defined by taking a vertex near an ideal vertex $v$ to the coset assigned to $v$. We shall construct a $\rho$-equivariant lift of $\Gamma$ to a map $\eta\colon V(\scalerel*{\widetilde{\overline\mathcal T}}{\widetilde{T^2}})\to \mathop{\mathrm{SL}}(2,\mathbb C)$ such that $\tilde\tau=\delta\eta$ is a natural cocycle on $\scalerel*{\widetilde{\overline\mathcal T}}{\widetilde{T^2}}$ descending to a natural cocycle $\tau$ on $\overline\mathcal T$. Any cocycle compatible with $D$ arises from this construction (since $\widetilde M$ is simply connected all lifts are coboundaries). Fix an orientation of each long edge $e$ of $\overline\mathcal T$, and a lift $\tilde e$ of $e$. Each vertex of $\scalerel*{\widetilde{\overline\mathcal T}}{\widetilde{T^2}}$ is then in the $\pi_1$ orbit of exactly one of the vertices $\tilde e_0$ and $\tilde e_1$. By $\rho$-equivariance it is thus enough to define $\eta$ on the set of endpoints $\tilde e_0$ and $\tilde e_1$. Now define $\eta(\tilde e_i)=g_ix_i$, where $\Gamma(\tilde e_i)=g_iP$ and $x_i\in P$ is an element as provided by Lemma [\[lemma:Bruhat\]](#lemma:Bruhat){reference-type="ref" reference="lemma:Bruhat"}. By construction, $\delta\eta$ is a Bruhat cocycle descending to a Bruhat cocycle on $\overline\mathcal T$. The freedom in the choice of $\eta$ is exactly the action by coboundaries preserving $\tau$. This proves the result. ◻
:::

### Explicit formulas via Ptolemy coordinates

Note that the labelings of the long edges are canonically determined, whereas a short edge is canonically determined if and only if it connects two counter diagonal long edges. The result below, generalizing the correspondence in Figure [\[fig:FundamentalCorrespondence\]](#fig:FundamentalCorrespondence){reference-type="ref" reference="fig:FundamentalCorrespondence"}, gives explicit formulas for the canonically determined edges in terms of Ptolemy coordinates when at most one Ptolemy coordinate per face is zero (the edge-degenerate case; see Definition [\[def:PartitionType\]](#def:PartitionType){reference-type="ref" reference="def:PartitionType"}). For $a\in\mathbb C$ and $b\in\mathbb C\setminus\{0\}$ let $$x(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad q(b)=\begin{pmatrix}0&-b^{-1}\\b&0\end{pmatrix}, \qquad d(b)=\begin{pmatrix}b&0\\0&b^{-1}\end{pmatrix}.$$

::: proposition
[]{#prop:ConcreteFormula label="prop:ConcreteFormula"} Let $\alpha_{ij}$ and $\beta^k_{ij}$ be the labelings of long and short edges of a Bruhat cocycle coming from a decoration $(g_0P,g_1P,g_2P,g_3P)$. If $c_{ij}$ are the Ptolemy coordinates, we have $$\begin{aligned}
\alpha_{ij}&=q(c_{ij})\text{ if } c_{ij}\neq 0.\\
\beta_{ij}^k&=x(\frac{c_{ij}}{c_{ik}c_{kj}}) \text{ if }c_{ik}c_{kj}\neq 0.\\
\alpha_{ij}&=-d(c_{ik}^{-1}c_{kj}) \text{ if } c_{ij}=0\text{ and } c_{ik}c_{kj}\neq 0.
\end{aligned}$$
:::

::: proof
*Proof.* The first formula only involves a single edge and is thus independent of whether or not the remaining Ptolemy coordinates are zero. The second only involves the face $ijk$ and holds by the fundamental correspondence if $c_{ij}\neq 0$ and for $c_{ij}=0$ as well by analytic continuation. The third is a consequence of the first two using the cocycle condition. ◻
:::

::: remark
[]{#rm:CoboundaryAction label="rm:CoboundaryAction"} Identifying $P$ with $\mathbb C$ via $\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)\leftrightarrow x$ allows us to view the labelings of the short edges near an ideal vertex $v$ of $M$ as complex vectors. The action of a coboundary taking a vertex $v$ to $x\in\mathbb C$ (keeping all other vertices fixed) then corresponds to moving $v$ by $x$ (see Figure [\[fig:CoboundaryAction\]](#fig:CoboundaryAction){reference-type="ref" reference="fig:CoboundaryAction"}).
:::

<figure id="fig:NaturalCocycleDefn">
<p><br />
</p>
<figcaption>The natural cocycle from a decoration.</figcaption>
</figure>

## $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representations

The analogue of Theorem [\[thm:OneToOneGeneral\]](#thm:OneToOneGeneral){reference-type="ref" reference="thm:OneToOneGeneral"} for $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representations and $\mathop{\mathrm{PSL}}(2,\mathbb C)$ Bruhat cocycles also holds. The proof is identical to that of Theorem [\[thm:OneToOneGeneral\]](#thm:OneToOneGeneral){reference-type="ref" reference="thm:OneToOneGeneral"} using the obvious analogues of Lemma [\[lemma:Bruhat\]](#lemma:Bruhat){reference-type="ref" reference="lemma:Bruhat"} and Corollary [\[cor:LocalOneToOne\]](#cor:LocalOneToOne){reference-type="ref" reference="cor:LocalOneToOne"} for $\mathop{\mathrm{PSL}}(2,\mathbb C)$.

## Non-boundary-unipotent representations

Let $M$ be as in Section [\[sec:Enhanced\]](#sec:Enhanced){reference-type="ref" reference="sec:Enhanced"}. Recall that a decoration of $\rho\colon\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$ is a $\rho$-equivariant assignment of $P$-cosets to the triangular faces of $\scalerel*{\widetilde{\overline\mathcal T}}{\widetilde{T^2}}$. A *fattened Bruhat cocycle* is a cocycle on the fattened decomposition restricting to a Bruhat cocycle on each truncated simplex and labeling each face pairing edge by diagonal elements.

::: theorem
There is a one-to-one correspondence between decorated $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations and fattened Bruhat cocycles.
:::

::: proof
*Proof.* The proof is similar to that of Theorem [\[thm:OneToOneGeneral\]](#thm:OneToOneGeneral){reference-type="ref" reference="thm:OneToOneGeneral"} using the fattened decomposition instead of the regular one. ◻
:::
