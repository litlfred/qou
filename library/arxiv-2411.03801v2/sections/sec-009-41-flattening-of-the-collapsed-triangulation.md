---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-009-41-flattening-of-the-collapsed-triangulation
section_title: "Flattening of the collapsed triangulation"
section_number: 4.1
pages: 14-17
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.911
---
[]{#sec.flat label="sec.flat"}

In this subsection, we find an explicit flattening ${\boldsymbol f}=(f,f',f'')$ of $\mathcal T_{\mathring{D}}$. Recall from Section [\[sec.OL\]](#sec.OL){reference-type="ref" reference="sec.OL"} that ${\boldsymbol f}$ consists of integer triples ${\boldsymbol f}_j=(f_j,f'_j,f''_j) \in \mathbbm Z^3$, one for each tetrahedron $\Delta_j$ of $\mathcal T_{\mathring{D}}$ and is required to satisfy $f_j + f'_j +f''_j =1$ for each $\Delta_j$ and $$\label{eqn.flat}
e_i : \quad \sum_{j} G_{ij} f_j +  G'_{ij} f'_j  + G''_{ij} f''_j  =2$$ for each edge $e_i$. We denote by $\langle {\boldsymbol f}, e_i \rangle$ the left-hand side of Equation [\[eqn.flat\]](#eqn.flat){reference-type="eqref" reference="eqn.flat"}.

We fix a quad type of each $\Delta_j$ so that $f_j$ is assigned to the vertical and horizontal edges of $\Delta_j$ (the edges $\overline{0\infty}$ and $\overline{xy}$ in Figure [\[fig.crossing2\]](#fig.crossing2){reference-type="ref" reference="fig.crossing2"}). Denoting $\Delta_j$ with a corner of $\mathring{D}$, we choose an integer triple ${\boldsymbol f}_j$ as follows. $$\label{eqn.fl1}
{\boldsymbol f}_j  =
\begin{cases}
(1,0,0) & \textrm{for the N and S-corners of a crossing} \\
(0,1,0) & \textrm{for the E and W-corners of a positive crossing} \\
(0,0,1) & \textrm{for the E and W-corners of a negative crossing} \, .
\end{cases}$$ Here N, E, S or W indicates the position of a corner with respect to the nearby crossing. Note that each tetrahedron has two edges assigned with 1 and four edges assigned with 0. When we compute $\langle {\boldsymbol f}, e \rangle$, the ones with 0 have no influence, and thus it suffices to consider the ones with $1$, which are marked by red in Figure [1](#fig.octahedronatd){reference-type="ref" reference="fig.octahedronatd"}.

<figure id="fig.octahedronatd">

<figcaption>A choice of <span class="math inline"><strong>f</strong></span>.</figcaption>
</figure>

Recall from Section [\[sec.octa\]](#sec.octa){reference-type="ref" reference="sec.octa"} that $\mathcal T_{\mathring{D}}$ has four edge-types: C, R, O and U-edges. We first compute $\langle {\boldsymbol f}, e \rangle$ for C and R-edges. As these edges recieve contributions only from $f_j$'s (not from $f'_j$'s and $f''_j$'s), only N and S-corners are involved in the computation. For simplicity we call a segment with $\kappa \in \{ 0,1,\infty\}$ assigned a $\kappa$-segment.

::: lemma
[]{#lem.C label="lem.C"} We have $\langle {\boldsymbol f}, e \rangle=2$ for all C-edges $e$.
:::

::: proof
*Proof.* Recall that a C-edge corresponds to a crossing with no adjacent $0$ and $\infty$-segments. Thus a corner around it is essential, unless adjacent segments are both 1-segments. Given that $\mathring{D}$ is given as in Figure [\[fig.planardiagram\]](#fig.planardiagram){reference-type="ref" reference="fig.planardiagram"}, both the N and S-corners are essential and contribute 1 to $\langle {\boldsymbol f}, e \rangle$. This proves that $\langle {\boldsymbol f}, e \rangle=2$. ◻
:::

::: lemma
[]{#lem.R label="lem.R"} We have $\langle {\boldsymbol f}, e \rangle=2$ for all R-edges $e$.
:::

::: proof
*Proof.* Let us consider a region of $\mathring{D}$ that corresponds to an R-edge $e$. The S-corner of the topmost crossing contributes 1 to $\langle {\boldsymbol f}, e \rangle$. Similarly, the N-corner of the bottommost crossing contributes 1 to $\langle {\boldsymbol f}, e \rangle$. The other crossings that are neither top nor bottom ones have no contribution; see Figure [1](#fig.octahedronatd){reference-type="ref" reference="fig.octahedronatd"}. This proves that $\langle {\boldsymbol f}, e \rangle=2$. ◻
:::

We now compute $\langle \boldsymbol f  , e \rangle$ for O and U-edges. Recall that O and U-edges correspond to over and under-arcs of $\mathring{D}$, respectively. In what follows, for simplicity we confuse an over or under-arc of $\mathring{D}$ with the corresponding O or U-edge of $\mathcal T_{\mathring{D}}$. In addition, we assume that starting from the top endpoint of $\mathring{D}$, we underpass the first crossing (thus from the bottom endpoint, we overpass the first crossing). The opposite case can be proved similarly by exchanging the roles of $\infty$ and $0$.

The diagram $\mathring{D}$ has one cap, and we choose one crossing $c_\infty$ and one segment $s_\infty$ around it shown as in Figure [2](#fig.infty){reference-type="ref" reference="fig.infty"}. Similarly, we choose one crossing $c_0$ and one segment $s_0$ around the cup of $\mathring{D}$ as in Figure [2](#fig.infty){reference-type="ref" reference="fig.infty"}. We denote by $o_\kappa$ and $u_\kappa$ for $\kappa = 0,\infty$ the over and under-arcs containing the segment $s_\kappa$, respectively.

<figure id="fig.infty">

<figcaption>Cap and cup of <span class="math inline"><em>D̊</em></span>.</figcaption>
</figure>

::: lemma
[]{#lem.O label="lem.O"} For an O or U-edge $e$, we have $$\langle \boldsymbol f, e \rangle
=\begin{cases}
3 & \textrm{if } e =  u_\infty \textrm{ or } o_0 \,,\\
1 & \textrm{if } e = o_\infty \textrm{ or }  u_0 \,,\\  
2 & \textrm{otherwise} \,.
\end{cases}$$
:::

::: proof
*Proof.* Following the diagram from the top endpoint, we encounter all over and under-arcs. Thus for each O and U-edge we can think of a crossing where it starts or ends. Except for the four edges $u_0,u_\infty, o_0$ and $o_\infty$, every O and U-edge $e$, $\langle \boldsymbol f \, , e \rangle$ receives one from the crossing where it starts and another one from where it ends; see Figure [1](#fig.octahedronatd){reference-type="ref" reference="fig.octahedronatd"}. This proves that $\langle \boldsymbol f \, , e \rangle=2$. Note that this includes the case when an O-edge and a U-edge are identified. Such identification happens when they meet at the W or E-corner lying in the unbounded region, and the fact that we do not have a tetarhedron at that corner preserves the fact $\langle \boldsymbol f \, , e \rangle=2$.

For $e = u_\infty$, it receives one from the crossing where it starts and another one from where it ends, as before. However, as the face-gluing around $c_\infty$ is different from other crossings, i.e., as the vertical edge at $c_\infty$ is identified with $u_\infty$, it receives one additional contribution from $c_\infty$.

It follows that $\langle \boldsymbol f \, , e \rangle=3$. We deduce the same for $e=u_0$ similarly.

For $e = o_\infty$, $\infty$-segments make corners around the crossing where it starts not essential. This results in a tetrahedron being missing at the E or W-corner of its start crossing, and thus $\langle \boldsymbol f \, , e \rangle =1$. We deduce the same for $e =u_0$ similarly. ◻
:::

::: lemma
[]{#lem.overunder label="lem.overunder"} Let $e_i$ and $e_j$ be two edges of $\mathcal T_{\mathring{D}}$ that correspond to consecutive under or over-arcs. Then there is a triple $\boldsymbol g=(g,g', g'')$ of vectors such that $g_j + g'_j + g_j''=0$ and $$\langle {\boldsymbol f + \boldsymbol g} ,  e \rangle -\langle {\boldsymbol f}, e \rangle
=\begin{cases}
-1 & \textrm{if } e = e_i \\
1 & \textrm{if } e = e_j \\
0 & \textrm{otherwise}\, .
\end{cases}$$ In addition, such $\boldsymbol g$ can be chosen independently of $\boldsymbol f$ .
:::

::: proof
*Proof.* Let $a_1$ and $a_2$ be the over or under-arcs corresponding to the edges $e_i$ and $e_j$, respectively. As they are adjacent, there is a common crossing. If $a_1$ and $a_2$ are under-arcs, then we define $\boldsymbol g$ by assigning integer triples to the corners at the common crossing as in Figure [3](#fig.crossing4){reference-type="ref" reference="fig.crossing4"} (left); if $a_1$ and $a_2$ are over-arcs, then as in Figure [3](#fig.crossing4){reference-type="ref" reference="fig.crossing4"} (right). Then one can easily check that $\boldsymbol g$ satisfies the desired condition.

<figure id="fig.crossing4">

<figcaption>A choice of <span class="math inline"><strong>g</strong></span>.</figcaption>
</figure>

 ◻
:::

::: remark
[]{#rmk.ratio label="rmk.ratio"} In the proof of Lemma [\[lem.overunder\]](#lem.overunder){reference-type="ref" reference="lem.overunder"}, we used two tetrahedra that are below the arcs $a_1$ and $a_2$, but one may use two tetrahedra that are above the arcs. This implies that a choice of $\boldsymbol g$ is not unique. However, regardless of a choice of $\boldsymbol g$, the product $${\boldsymbol \zeta}^{\boldsymbol g}:=
\prod_{j}\zeta_j^{g_j} {\zeta_j'}^{g_j'} {\zeta_j''}^{g_j''}$$ is invariant: if there are two choices $\boldsymbol g_1$ and $\boldsymbol g_2$, then for any flattening $\boldsymbol f$ of $\mathcal T_{\mathring{D}}$, $\boldsymbol f + \boldsymbol g_1 - \boldsymbol g_2$ is also a flattening, and thus $${\boldsymbol \zeta}^{\boldsymbol f + \boldsymbol g_1 -\boldsymbol g_2} =
  {\boldsymbol \zeta}^{\boldsymbol f}  \quad \Rightarrow \quad
  {\boldsymbol \zeta}^{\boldsymbol g_1 }= {\boldsymbol \zeta}^{\boldsymbol g_2} \,.$$ Explicitly, ${\boldsymbol \zeta}^{\boldsymbol g}$ agrees with $z_1z_2$ for Figure [\[fig.crossing3\]](#fig.crossing3){reference-type="ref" reference="fig.crossing3"} (left) and with $1/(z_1z_2)$ for Figure  [\[fig.crossing3\]](#fig.crossing3){reference-type="ref" reference="fig.crossing3"} (right) where $z_1$ and $z_2$ are shape parameters placed at the corners shown as in Figure [\[fig.crossing3\]](#fig.crossing3){reference-type="ref" reference="fig.crossing3"}.
:::

Roughly speaking, Lemma  [\[lem.overunder\]](#lem.overunder){reference-type="ref" reference="lem.overunder"} allows us to take one contribution from an arc, either over or under, and give it to the next arc, and thus to any arc by applying the lemma multiple times. We take one contribution from $o_0$ (resp., $u_\infty$) and give it to $o_\infty$ (resp., $u_0$). This results in a triple $\boldsymbol g$ such that (see Lemma [\[lem.O\]](#lem.O){reference-type="ref" reference="lem.O"}) $$\langle \boldsymbol f+\boldsymbol g , e \rangle  = 2$$ for all edges $e$. Namely, $\boldsymbol f+\boldsymbol g$ is a flattening of $\mathcal T_{\mathring{D}}$.
