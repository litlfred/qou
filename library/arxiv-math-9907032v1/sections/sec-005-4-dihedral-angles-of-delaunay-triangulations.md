---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-005-4-dihedral-angles-of-delaunay-triangulations
section_title: "Dihedral angles of Delaunay triangulations"
section_number: 4
pages: 9-11
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#dihsec label="dihsec"}

In the preceding section it was shown that in order for the linear program $L$ to have a solution, it is necessary and sufficient that the putative dihedral angles $\delta(e)$ satisfy the inequalities [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"} and [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}. Below, we use these to derive another set of necessary conditions [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}, and show that under the additional assumption that the original dihedral angles do not exceed $\pi$, these are equivalent to the inequalities [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}. The virtue of the inequalities [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"} is that it is easier to interpret them geometrically. A special case of them is one of the main results of [@steiner] -- the connection will be explained in section [\[ideal\]](#ideal){reference-type="ref" reference="ideal"}.

First, some definitions (these are the analogs of the definitions of section [\[oldstuff\]](#oldstuff){reference-type="ref" reference="oldstuff"} without reference to face angles) -- as before $T$ is a triangulation of $S$, $V(T)$ is the set of vertices of $T$, $E(T)$ is the set of edges, and $F(T)$ is the set of faces. We assume that each edge $e\in E(T)$ is given a weight $\delta(e)\in \mathbf{R}$. The weight $\delta(e)$ will be called the dihedral angle at $e$. The quantity $\delta^\prime(e)=\pi - \delta(e)$ will be called the *exterior dihedral angle* at $e$.

If $v$ is a vertex of $T$, then the *cone angle* $C_v$ is defined to be $$C_v = \sum_{\mbox{$e$ incident to $v$}}
\delta^\prime(e),$$ while the *curvature* $\kappa_v$ is defined to be $\kappa_v = 2\pi - C_v.$

*Note.* The cone angle of a boundary point is, thus, not the same as the boundary angle (in the language of section [\[oldstuff\]](#oldstuff){reference-type="ref" reference="oldstuff"}, but smaller by $\pi$.

Below, it will often be useful to talk of the *Poincaré dual* of $T$. Recall that this is the complex $T^*$, such that the set of vertices of $T^*$ is in one-to-one correspondence with the set of faces of $T$, the set of edges of $T^*$ are in one to one correspondence with the edges of $T$ -- two vertices of $T^*$ are joined by an edges if and only if the corresponding faces of $T$ share an edge, and finally the faces of $T^*$ correspond to the vertices of $T$ -- the vertices of a face $v^*$ of $T^*$ correspond to the faces of $T$ incident to the corresponding vertex $v$.

::: definition
A subcomplex $\mathcal{F}$ of $T$ is *closed*, if whenever a cell $t$ is in $\mathcal{F}$, then so are all of the lower-dimensional cells incident to $t$.
:::

::: definition
The *total curvature* of a subcomplex $\mathcal{F}$ of $T$ is defined as $$K(\mathcal{F}) = \sum_{v\in V(\mathcal{F})} \kappa_v.$$
:::

*Notation.* Let $\mathcal{F}$ be a subcomplex of $T$, and let $E^\prime(\mathcal{F})$ be the set of those edges $e$ of $T$ which are not edges of faces of $\mathcal{T}$, but such that at least one endpoint of $e$ belongs to $\mathcal{T}$. For each edge $e$ of $T$, define $n_{\mathcal{F}}(e)$ to be the number of endpoints of $e$ which belong to $\mathcal{F}$.

For example, if $e\in E(\mathcal{F})$, then $n_{\mathcal{F}}(e) = 2$; if $e \notin E(\mathcal{F}) \cup E^\prime(\mathcal{F})$, then $n_{\mathcal{F}}(e) = 0$.

::: theorem
[]{#kappaineq label="kappaineq"} For every non-empty subcomplex $\mathcal{F}$ of $T$ the following are equivalent:

\(a\)

:   $$\sum_{e\in E^\prime(\mathcal{F})} n_{\mathcal{F}}(e)
    \delta^\prime(e)\geq  2\pi \chi (\mathcal{F})- K(\mathcal{F}),$$ with equality if and only if $\mathcal{F} = T.$

\(b\)

:   Conditions [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"} and [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} hold.
:::

::: proof
*Proof.* We will show that (b) $\Rightarrow$ (a); the converse is immediate. $$\label{kappasum}
K(\mathcal{F}) = \sum_{v\in V(\mathcal{F})} 
(2\pi - \sum_{\mbox{$v\in e$}} \delta^\prime(e))=
2\pi |V(\mathcal{F})| - \sum_{v\in V(\mathcal{F})}\sum_{\mbox{$v \in e$}}  
\delta^\prime(e).$$ The last sum of equation [\[kappasum\]](#kappasum){reference-type="ref" reference="kappasum"} can be rewritten thus: $$\label{kappa2}
\sum_{v\in V(\mathcal{F})}\sum_{\mbox{$e$ incident to $v$}}
\delta^\prime(e) = 2 \sum_{e\in E(\mathcal{F})} \delta^\prime(e) +
\sum_{e\in E^\prime(\mathcal{F})}  n_{\mathcal{F}}(e) \delta^\prime
(e).$$

Finally, using the definition of $\delta^\prime(e)$, and combining equations [\[kappasum\]](#kappasum){reference-type="ref" reference="kappasum"} and [\[kappa2\]](#kappa2){reference-type="ref" reference="kappa2"} it follows that $$\label{kappaeq}
K(\mathcal{F}) = 2\pi \chi(\mathcal{F}) + 
2(\sum_{e\in E(\mathcal{F})} \delta(e) -\pi |F(\mathcal{F})|)
 - \sum_{e\in E^\prime(\mathcal{F})} \delta^\prime(e).$$ Now, assume that the dihedral angles satisfy the inequalities [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}. This means that the middle term on the right hand side of equation [\[kappaeq\]](#kappaeq){reference-type="ref" reference="kappaeq"} is non-negative (and strictly positive unless $\mathcal{F} = T$). ◻
:::
