---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-004-24-on-the-topological-invariance-of-the-index
section_title: "On the topological invariance of the index"
section_number: 2.4
pages: 7-8
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.984
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.invariance label="sub.invariance"}

Physics predicts that when defined, the 3D index $I_{\mathcal T}$ depends only on the underlying 3-manifold $M$. Recall that [@HRS] prove that every hyperbolic 3-manifold $M$ that satisfies $$\label{eq.H12}
H_1(M,\mathbb Z/2)\to H_1(M,\partial M,\mathbb Z/2) \qquad \text{is the zero map}$$ (eg. a hyperbolic link complement) admits an ideal triangulation with a strict angle structure, and conversely if $M$ has an ideal triangulation with a strict angle structure, then $M$ is irreducible, atoroidal and every boundary component of $M$ is a torus [@LT].

A simple way to construct a topological invariant using the index, would be a map $$M \mapsto \{I_{\mathcal T} \,\,|\,\, \mathcal T\in \mathcal S_M \}$$ where $M$ is a cusped hyperbolic 3-manifold with at least one cusp and $\mathcal S_M$ is the set of ideal triangulations of $M$ that support an index structure. The latter is a nonempty (generally infinite) set by [@HRS], assuming that $M$ satisfies [\[eq.H12\]](#eq.H12){reference-type="eqref" reference="eq.H12"}. If we want a finite set, we can use the subset $\mathcal S^{\mathrm{EP}}_M$ of ideal triangulations $\mathcal T$ of $M$ which are a refinement of the Epstein-Penner cell-decomposition of $M$. Again, [@HRS] implies that $\mathcal S^{\mathrm{EP}}_M$ is nonempty assuming [\[eq.H12\]](#eq.H12){reference-type="eqref" reference="eq.H12"}. But really, we would prefer a single 3D index for a cusped manifold $M$, rather than a finite collection of 3D indices.

It is known that every two combinatorial ideal triangulations of a 3-manifold are related by a sequence of *2-3 moves* [@Ma1; @Ma2; @Pi]. Thus, topological invariance of the 3D index follows from invariance under 2-3 moves.

Consider two ideal triangulations $\mathcal T$ and $\widetilde{\mathcal T}$ with $N$ and $N+1$ tetrahedra related by a $2-3$ *move* shown in Figure [1](#fig.23){reference-type="ref" reference="fig.23"}.

<figure id="fig.23">
<div class="center">
<embed src="draws/23naked.pdf" />
</div>
<figcaption>A 2–3 move: a bipyramid split into <span class="math inline"><em>N</em></span> tetrahedra for <span class="math inline">𝒯</span> and <span class="math inline"><em>N</em> + 1</span> tetrahedra for <span class="math inline">$\widetilde{\mathcal T}$</span>.</figcaption>
</figure>

::: proposition
[]{#prop.3.2.index label="prop.3.2.index"} If $\widetilde{\mathcal T}$ admits a strict angle structure structure, so does $\mathcal T$ and $I_{\widetilde{\mathcal T}}=I_{\mathcal T}$.
:::

For the next proposition, a special index structure on $\mathcal T$ is given in Definition [\[def.special.index\]](#def.special.index){reference-type="ref" reference="def.special.index"}.

::: proposition
[]{#prop.2.3.index label="prop.2.3.index"} If $\mathcal T$ admits a special strict angle structure, then $\widetilde{\mathcal T}$ admits a strict angle structure and $I_{\widetilde{\mathcal T}}=I_{\mathcal T}$.
:::

::: remark
[]{#rem.23curious label="rem.23curious"} The asymmetry in Propositions [\[prop.3.2.index\]](#prop.3.2.index){reference-type="ref" reference="prop.3.2.index"} and [\[prop.3.2.index\]](#prop.3.2.index){reference-type="ref" reference="prop.3.2.index"} is curious, but also necessary. The origin of this asymmetry is the fact that 3-2 moves always preserve strict angle structures but 2-3 moves sometimes do not. If 2-3 moves always preserved strict angle structures, then all ideal triangulations of a fixed manifold would admit strict angle structures as long as one of them does. On the other hand, an ideal triangulation that contains an edge which belongs to exactly one (or two) ideal tetrahedra does not admit a strict angle structure since the angle equations around that edge should add to $2$. Such triangulations are easy to construct, even for hyperbolic 3-manifolds (eg. the $4_1$ knot).
:::
