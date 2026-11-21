---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-000-1-statement-of-results
section_title: "Statement of results"
section_number: 1
pages: 2-4
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.95
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
[]{#sec:results label="sec:results"}

Consider the configuration space $$\mathrm{Conf}_3S^3\subset S^3 \times S^3 \times S^3$$ of ordered triples $(x,y,z)$ of distinct points in the unit $3$-sphere $S^3$ in $\mathbb R^4$. Since $x$, $y$ and $z$ are distinct, they span a $2$-plane in $\mathbb R^4$. Orient this plane so that the vectors from $x$ to $y$ and from $x$ to $z$ form a positive basis, and then move it parallel to itself until it passes through the origin. The result is an element $G(x,y,z)$ of the Grassmann manifold $\mathrm{G}_2\mathbb R^4$ of all oriented 2-planes through the origin in $\mathbb R^4$. This defines the ***Grassmann map*** $$G: \mathrm{Conf}_3S^3\longrightarrow \mathrm{G}_2\mathbb R^4.$$ It is equivariant with respect to the diagonal $O(4)$ action on $S^3 \times S^3 \times S^3$ and the usual $O(4)$ action on $\mathrm{G}_2\mathbb R^4$.

<figure id="fig:gras">
<p><embed src="FgGR.pdf" style="height:1.66667in" /> (-70,27)<span><span class="math inline"><em>G</em>(<em>x</em>,<em>y</em>,<em>z</em>)</span></span> (-135,95)<span><span class="math inline"><em>x</em></span></span> (-108,86)<span><span class="math inline"><em>y</em></span></span> (-85,80)<span><span class="math inline"><em>z</em></span></span> (-140,75)<span><span class="math inline"><em>X</em></span></span> (-114,55)<span><span class="math inline"><em>Y</em></span></span> (-80,55)<span><span class="math inline"><em>Z</em></span></span> (-125,15)<span><span class="math inline"><em>S</em><sup>3</sup></span></span> (-190,23)<span><span class="math inline">ℝ<sup>4</sup></span></span></p>
<figcaption>The Grassmann map</figcaption>
</figure>

The Grassmann manifold $\mathrm{G}_2\mathbb R^4$ is isometric (up to scale) to the product $S^2 \times S^2$ of two unit 2-spheres. Let $\pi\colon\mathrm{G}_2\mathbb R^4\to S^2$ denote orthogonal projection to either factor.

Given any ordered oriented link $L$ in $S^3$ with three parametrized components $$X = \{x(s) \ | \ s \in S^1\} \ , \ Y = \{y(t) \ | \ t \in S^1 \} \ \ \text{and}\ \  Z = \{z(u) \ | \ u \in S^1 \},$$ where $S^1$ is the unit circle in $\mathbb{R}^2$, we define the ***characteristic map*** of $L$ $$g_L\colon T^3 = S^1 \times S^1 \times S^1 \longrightarrow S^2$$ by $g_L(s,t,u) = \pi(G(x(s),y(t), z(u)))$. In Section [\[sec:characteristicmap\]](#sec:characteristicmap){reference-type="ref" reference="sec:characteristicmap"} we give an explicit formula for this map as the unit normalization of a vector field on $T^3$ whose components are quadratic polynomials in the components of $x(s)$, $y(t)$ and $z(u)$.

The homotopy class of $g_L$ is unchanged under any ***link homotopy*** of $L$, meaning a deformation during which each component may cross itself, but different components may not intersect.

::: theorem
[]{#thm:A label="thm:A"} **The pairwise linking numbers , $q$ and $r$ of the link $L$ are equal to the degrees of its characteristic map $g_L$ on the 2-dimensional coordinate subtori of $T^3$, while twice Milnor's $\mu$-invariant for $L$ is equal to Pontryagin's $\nu$-invariant for $g_L$.**
:::

::: remark
Milnor's $\mu$-invariant, typically denoted $\overline{\mu}_{123}$, is descriptive of a *single* three-component link. In contrast, Pontryagin's $\nu$-invariant is the cohomology class of a difference cocycle comparing *two* maps from $T^3$ to $S^2$ that are homotopic on the $2\text{-skeleton}$ of $T^3$. In particular, it assigns to any pair $g$, $g'$ of such maps whose degrees on the coordinate 2-tori are $p$, $q$ and $r$, an integer $\nu(g,g')$ that is well-defined modulo $2\gcd(p,q,r)$. With this understanding, the last statement in Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} asserts that $$2(\mu(L) - \mu(L')) \ \equiv \ \nu(g_L,g_{L'}) \mod{2\gcd(p,q,r)},$$ for any two links $L$ and $L'$ with the same pairwise linking numbers $p$, $q$ and $r$.
:::

We will sketch here two quite different proofs of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, a topological one in Section [\[sec:top_proof\]](#sec:top_proof){reference-type="ref" reference="sec:top_proof"} using framed cobordism of framed links in the 3-torus, and an algebraic one in Section [\[sec:alg_proof\]](#sec:alg_proof){reference-type="ref" reference="sec:alg_proof"} using the group of link homotopy classes of three-component string links and the fundamental groups of spaces of maps of the 2-torus to the 2-sphere.

To state the integral formula for Milnor's $\mu$-invariant when the pairwise linking numbers are zero, let $\omega$ denote the Euclidean area 2-form on $S^2$, normalized so that the total area is 1 instead of $4\pi$. Then $\omega$ pulls back under the characteristic map $g_L$ to a closed 2-form on $T^3$, which can be converted in the usual way to a divergence-free vector field $V_L$ on $T^3$. In Section [\[sec:thmB\]](#sec:thmB){reference-type="ref" reference="sec:thmB"} we give explicit formulas for $V_L$, and also for the fundamental solution $\varphi$ of the scalar Laplacian on the 3-torus as a Fourier series in three variables. These are the key ingredients in the integral formula below.

::: theorem
[]{#thm:B label="thm:B"}
:::

Here $\nabla_\sigma$ indicates the gradient with respect to $\sigma$, the difference $\sigma - \tau$ is taken in the abelian group structure of the torus, and $d\sigma$ and $d\tau$ are volume elements. The integrand is invariant under the action of the group $SO(4)$ of orientation-preserving rigid motions of $S^3$ on the link $L$, attesting to the naturality of the formula. We will see in the next section that the integral above expresses the "helicity" of the vector field $V_L$ on $T^3$.
