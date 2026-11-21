---
doc_id: arxiv-q-alg-9504020v1
doc_title: "A link invariant from quantum dilogarithm"
section_id: sec-002-3-invariants-of-links-in-three-sphere
section_title: "Invariants of Links in Three-Sphere"
section_number: 3
pages: 4-5
source_pdf: 9504020v1.pdf
source_sha256: 0baef40fa9934c91
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "A link invariant from quantum dilogarithm — The link invariant, arising from the cyclic quantum dilogarithm via the particular R-matrix construction, is proved to coincide with the invariant of"
---
[]{#sec2 label="sec2"}

Let link $L$ in $S^3$ is given by a two-strand tangle. Consider some non-singular (i.e. with only simple intersection points) planar projection of this tangle. Denote by $V,E,F$ the sets of vertices, edges, and faces, respectively, in the planar graph. We will write $v\in f$, for some vertex $v$ and face $f$ if $v$ lies in the boundary of $f$. There are two distinguished elements $e_1$ and $e_2$ in $E$, corresponding to the two strands of the tangle, and one distinguished element $f_0$ in $F$, corresponding to the outer region in the plane. Define the following two maps: $$j\colon E\to Z_N,\quad a\colon V\times F\to Z_N,\label{ja-maps}$$ where we identified $Z_N$ with the set $\{0,\ldots,N-1\}$. Impose the restrictions on $j$: $$j(e_1)=j(e_2)=0,\label{boundary}$$ and on $a$: $$a(v,f_0)=0;\quad v\not\in f\Rightarrow a(v,f)=0,\quad  v\in V; f\in F,$$ $$\sum_{f\in F}a(v,f)=\sum_{v\in V}a(v,f)=1,\quad f\ne f_0.$$ Using these maps, associate with each vertex the Boltzmann weight according to Sect. [\[sec1\]](#sec1){reference-type="ref" reference="sec1"}. This gives us one more map: $$r_{j,a}\colon V\to C.$$ Consider now the "partition" function: $$\langle L\rangle=\sum_j \prod_{v\in V}r_{j,a}(v)\prod_{e\in E}\omega^{j(e)}.
\label{inv}$$

::: {#theo .theorem}
**Theorem 1**. *(1) The quantity $\langle L\rangle^N$ is an ambient isotopy invariant of the link $L$ in three-sphere; (2) for odd $N$ the following equality holds: $$\langle L\rangle^N=Q(S^3,L),$$ where $Q(M,L)$ is the invariant of triangulated link $L$ in three-manifold $M$ defined in [@K].*
:::

The first part of the theorem is a consequence of the identities, satisfied by the $R$-symbols (see Sect. [\[sec1\]](#sec1){reference-type="ref" reference="sec1"}). There is a freedom in choosing the second map in ([\[ja-maps\]](#ja-maps){reference-type="ref" reference="ja-maps"}). In fact, different choices lead to one and the same partition function ([\[inv\]](#inv){reference-type="ref" reference="inv"}) up to $N$-th roots of unity. Note that the face indices are nothing else but the angle dependent data, corresponding to "enhanced" vertex models [@BKW; @Jo; @W]. This becomes evident after Fourier transformation over the edge indices. The face index - angle correspondence is described by the formula: $$\phi=\pi-2\pi a,$$ where $\phi$ is the angle between the adjoining straight edges in the diagram, corresponding to $R$-symbol (see Sect. [\[sec1\]](#sec1){reference-type="ref" reference="sec1"}), and $a$ is the face index associated with the sector bounded by these edges.

The proof of the second part of the theorem is given in the next section.

Note that the two strand tangle representation of links has been used in [@Kauf] to construct the state sum for Alexander-Conway polynomial [@Alex; @Conw], because the latter is zero for disjoint union of links. This is also true for the invariant ([\[inv\]](#inv){reference-type="ref" reference="inv"}): $$\langle L_1\sqcup L_2\rangle=0.\label{vanish}$$ In the language of quantum group theory, property ([\[vanish\]](#vanish){reference-type="ref" reference="vanish"}) reflects the vanishing quantum dimension. In the three-dimensional definition given in [@K] ( see also the next section) no tangle description is needed.
