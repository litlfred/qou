---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-002-22-angle-structures
section_title: "Angle structures"
section_number: 2.2
pages: 5-5
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.822
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.angle label="sub.angle"}

In this section we define the 3D index of an ideal triangulation. A *generalized angle structure* on a combinatorial ideal tetrahedron $\Delta$ is an assignment of real numbers (called *angles*) at each edge of $\Delta$ such that the sum of the three angles around each vertex is $1$.[^1] It is easy to see that opposite edges are assigned the same angle, thus a generalized angle structure is determined by a triple $(\alpha,\beta,\gamma)
\in \mathbb R^3$ that satisfies $\alpha+\beta+\gamma=1$; see Figure [1](#fig.angles){reference-type="ref" reference="fig.angles"}.

<figure id="fig.angles">
<div class="center">
<embed src="draws/tetrahedronangles.pdf" />
</div>
<figcaption>Angles of a tetrahedron.</figcaption>
</figure>

A generalized angle structure is *strict* if $\alpha,\beta,\gamma>0$. Let $\mathcal T$ denote an ideal triangulation of an oriented 3-manifold $M$ with torus boundary. A *generalized angle structure* on $\mathcal T$ is the assignment of angles at each tetrahedron of $\mathcal T$ such that the sum of angles around every edge of $\mathcal T$ is $2$. A generalized angle structure on $\mathcal T$ is *strict* if its restriction to each tetrahedron is strict. For a detailed discussion of angle structures and their duality with normal surfaces, see [@HRS; @LT; @Ti]. Generalized angle structures are linearizations of the gluing equations, that may be used to construct complete hyperbolic structures, and intimately connected with the theory of normal surfaces on $M$ [@Jaco].

The existence of a strict angle structure imposes restrictions on the topology of $M$: it implies that $M$ is irreducible, atoroidal and each boundary component of $M$ is a torus; see for example [@LT]. On the other hand, if $M$ is a hyperbolic link complement, then there exist triangulations which admit a strict angle structure, [@HRS]. In fact, such triangulations can be constructed by a suitable refinement of the Epstein-Penner ideal cell decomposition of $M$. Note that not all such triangulations are geometric [@HRS].

[^1]: The sum of the 3 angles around each vertex is traditionally $\pi$.
