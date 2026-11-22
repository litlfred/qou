---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-001-11-the-3d-index-of-dimofte-gaiotto-gukov
section_title: "The 3D index of Dimofte-Gaiotto-Gukov"
section_number: 1.1
pages: 2-3
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.983
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.DGG label="sub.DGG"}

The goal of this paper is to convert the index of an ideal triangulation $\mathcal{T}$ (a remarkable collection of Laurent series in $q^{1/2}$ introduced by Dimofte-Gaiotto-Gukov [@DGG1; @DGG2] and further studied in [@Ga:index]) to a topological invariant of oriented cusped hyperbolic 3-manifolds $M$. Our goal will be achieved in two steps.

The first step identifies the existence of an index structure of $\mathcal{T}$ (a necessary and sufficient condition for the existence of the index of $\mathcal{T}$; see [@Ga:index]) with the non-existence of sphere or non vertex-linking torus *normal surfaces* of $\mathcal{T}$; see Theorem [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"} below. Such ideal triangulations are called 1-efficient in [@JR; @KR2]. The unexpected connection between the index of an ideal triangulation (a recent quantum object) and the classical theory of normal surfaces places restrictions on the topology of $M$; see Remark [\[rem.1\]](#rem.1){reference-type="ref" reference="rem.1"} below.

The second step constructs a canonical collection $\mathcal X_M^{\mathrm{EP}}$ of triangulations of the Epstein-Penner ideal cell decomposition of a cusped hyperbolic 3-manifold $M$, such that the index behaves well with respect to 2--3 and 0--2 moves that connect any two members of $\mathcal X_M^{\mathrm{EP}}$. The index of those triangulations then gives the desired topological invariant of $M$; see Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"} below.

We should point out that normal surfaces were also used by Frohman-Bartoczynska [@FK] in an attempt to construct topological invariants of 3-manifolds, in the style of a Turaev-Viro TQFT. Strict angle structures (a stronger form of an index structure) play a role in quantum hyperbolic geometry studied by Baseilhac-Benedetti [@BB1; @BB2]. In the recent work of Andersen-Kashaev [@AK], strict angle structures were used as sufficient conditions for convergence of analytic state-integral invariants of ideal triangulations. The latter invariants are expected to depend on the underlying cusped 3-manifold and to form a generalization of the Kashaev invariant [@Ka]. The $q$-series of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"} below are $q$-holonomic, of Nahm-type and, apart from a meromorphic singularity at $q=0$, admit analytic continuation in the punctured unit disc.

Before we get to the details, we should stress that the origin of the 3D index is the exciting work of Dimofte-Gaiotto-Gukov [@DGG1; @DGG2] (see also [@holo-blocks]) who studied gauge theories with $N=2$ supersymmetry that are associated to an ideal triangulation $\mathcal{T}$ of an oriented 3-manifold $M$ with at least one cusp. The low-energy limit of these gauge theories gives rise to a partially defined function, the so-called *3D index* $$\label{eq.ICT}
I: \{\text{ideal triangulations}\}
\longrightarrow\mathbb Z((q^{1/2}))^{H_1(\partial M;\mathbb Z)}, \qquad \mathcal{T}\mapsto 
I_{\mathcal{T}}([\varpi]) \in \mathbb Z((q^{1/2}))$$ for $[\varpi] \in H_1(\partial M;\mathbb Z)$.[^1] The function $I$ is only partially defined because the expression for the 3D index may not converge. The above gauge theories provide an analytic continuation of the coloured Jones polynomial and play an important role in Chern-Simons perturbation theory and in categorification. Although the gauge theory depends on the ideal triangulation $\mathcal{T}$, and the 3D index in general may not be defined, physics predicts that the gauge theory ought to be a topological invariant of the underlying 3-manifold $M$. Recall that any two ideal triangulations of a cusped 3-manifold are related by a sequence of 2-3 moves [@Ma1; @Ma2; @Pi]. In [@Ga:index] the following was shown. For the definition of an index structure, see Section [\[sec.definitions\]](#sec.definitions){reference-type="ref" reference="sec.definitions"}.

::: thm
[]{#thm.00 label="thm.00"} (a) $I_{\mathcal{T}}$ is well-defined if and only if $\mathcal{T}$ admits an *index structure*. (b) If $\mathcal{T}$ and $\mathcal{T}'$ are related by a 2--3 move and both admit an index structure, then $I_{\mathcal{T}}=I_{\mathcal{T}'}$.
:::

[^1]: Here and below we will use the notation $M$ for both a cusped hyperbolic 3-manifold and the corresponding compact manifold with boundary $\partial M$ consisting of a disjoint union of tori; the intended meaning should be clear from the context.
