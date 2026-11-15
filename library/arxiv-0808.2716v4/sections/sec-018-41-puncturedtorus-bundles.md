---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-018-41-puncturedtorus-bundles
section_title: "Punctured–torus bundles"
section_number: 4.1
pages: 21-25
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.986
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
We shall prove the following result:

::: theorem
[]{#thm:ptorus-area label="thm:ptorus-area"} Let $M$ be a punctured--torus bundle with monodromy $$\Omega = \pm R^{p_1}L^{q_1} \cdots R^{p_s}L^{q_s}.$$

Let $C$ be a maximal horoball neighborhood about the cusp of $M$. Then $$0.1885 \, s \: \approx \: \frac{16 \sqrt{3}}{147}  \, s \: \leq \:  {\rm area}({\partial}C) \:<\: 2
\sqrt{3} \, \frac{v_8}{v_3} \, s \: \approx \: 12.505 \, s.$$

Furthermore, if $\gamma$ is any simple closed curve on ${\partial}C$ that is transverse to the fibers, then its length $\ell(\gamma)$ satisfies $$\ell(\gamma) \: \geq \: \frac{4\sqrt{6}}{147} \,  s.$$
:::

::: remark
Extensive numerical experiments support the conjecture that ${\rm area}({\partial}C)/s$ is monotonic under the operation of adding more letters to existing syllables of the monodromy word $\Omega$. (It is not hard to show using the method of angled triangulations [@gf:two-bridge] that the volume of $M$ behaves in a similarly monotonic fashion.) This conjecture would imply that the quantity ${\rm area}({\partial}C)/s$ is lowest when all syllables have length 1 and $M$ is a cover of the figure--8 knot complement, while ${\rm area}({\partial}C)/s$ approaches its upper bound as the syllable lengths approach $\infty$ and the geometry of $M$ converges to a cover of the Borromean rings. The cusp area of the figure--8 knot complement is $2\sqrt{3}$, and the cusp area of one component of the Borromean rings is $8$. Thus, if the monotonicity conjecture is correct, it would follow that $$2\sqrt{3} \, s \: \leq \: {\rm area}({\partial}C) \:<\: 8 \, s.$$ Compared to the values in Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, this represents a modest improvement of the upper bound but a dramatic improvement of the lower bound.
:::

The main idea of the proof of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} is to pack the horospherical torus ${\partial}C$ with disjoint disks that are shadows of large horospheres. Recall from Definition [\[def:fibered-meridian\]](#def:fibered-meridian){reference-type="ref" reference="def:fibered-meridian"} that we denote the length of a meridian in the maximal cusp of a punctured--torus bundle by $2\mu$. By Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}, every zigzag on ${\partial}C$ will contain two horospheres of diameter at least $\mu^2/7$, corresponding to the two endpoints of the same edge of the zigzag. When we project one of these horospheres to ${\partial}C$, we obtain a disk whose radius is at least $\mu^2/14$.

To turn this into an effective estimate on the area of ${\partial}C$, we need to employ a somewhat subtle procedure for choosing which horospheres to count and which ones to discard. We choose the horospheres in the following manner:

1.  Let $E$ be the set of all edges of $M$ whose length outside the maximal cusp is at most $\ln(7/\mu^2)$. These are exactly the edges that lead to horospheres of diameter $\geq \mu^2/7$. Thus, by Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}, every pleated surface in $M$ contains an edge in $E$.

2.  Order the letters of the monodromy word $\Omega$: $\alpha_1,
    \ldots, \alpha_m$. Recall, from Section [\[sec:ptorus\]](#sec:ptorus){reference-type="ref" reference="sec:ptorus"}, that each $\alpha_i$ corresponds to a pleated surface $T_{\alpha_i}$.

3.  Find the smallest index $i$ such that all three edges in the pleating of $T_{\alpha_i}$ belong to $E$. (It is possible that such an $i$ does not exist.) If such a $T_{\alpha_i}$ occurs, remove the longest of the those three edges from $E$, breaking ties at random.

4.  Repeat step (3) inductively. In the end, the set $E$ will contain at most two edges from each pleated surface.

At the end of step (4), if a pleated surface $T$ contains one edge of $E$, that edge is the shortest in $T$. If $T$ contains two edges of $E$, they are the two shortest edges in $T$.

::: lemma
[]{#lemma:edge-count label="lemma:edge-count"} The set $E$, constructed as above, contains at least $2s/3$ distinct edges.
:::

::: proof
*Proof.* By Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}, every pleated surface in $M$ contains an edge whose length is at most $\ln(7/\mu^2)$. Thus, at the end of step (1) in the selection procedure above, the set $E$ contained at least one edge from every pleated surface. Now, observe that two different pleated surfaces $T_\alpha$ and $T_\beta$, corresponding to letters $\alpha$ and $\beta$ in $\Omega$, will share an edge if and only if the corresponding triangles in the Farey graph share a vertex. As Figure [1](#fig:farey){reference-type="ref" reference="fig:farey"} illustrates, this can only happen if the letters $\alpha$ and $\beta$ come from the same syllable, neighboring syllables, or syllables that share a neighbor. Therefore, at the end of step (1), the set $E$ contained at least one edge for every consecutive string of three syllables, hence at least $2s/3$ distinct edges in total.

<figure id="fig:farey">
<div class="center">

</div>
<figcaption>The only possible words between two triangles that share a vertex are <span class="math inline"><em>S</em> <em>R</em><em>R</em>⋯<em>R</em> <em>F</em></span> and <span class="math inline"><em>S</em> <em>L</em><em>L</em>⋯<em>L</em> <em>F</em></span>, where <span class="math inline"><em>S</em></span> and <span class="math inline"><em>F</em></span> (start and finish) can both be either <span class="math inline"><em>L</em></span> or <span class="math inline"><em>R</em></span>. </figcaption>
</figure>

Now, consider what happens when we begin removing edges in step (3). Suppose that all three edges in a pleated surface $T_\alpha$ belong to $E$. Then, just as above, for any pleated surface $T_\beta$ that shares an edge with $T_\alpha$, the letters $\alpha$ and $\beta$ must come from the same syllable, neighboring syllables, or syllables that share a neighbor. There are at most five such syllables altogether (the syllable containing $\alpha$, plus two on each side). Thus, after we remove the longest edge of $T_\alpha$ from $E$, the set $E$ still contains two edges from a string of five consecutive syllables.

At the end of the selection procedure, every pleated surface in $M$ belongs either to a string of 3 syllables containing at least one edge of $E$, or to a string of 5 syllables containing at least two edges of $E$. In either scenario, there are at least $2s/3$ edges belonging to $E$. ◻
:::

::: lemma
[]{#lemma:disjoint-disks label="lemma:disjoint-disks"} Let $M$ be a punctured--torus bundle with monodromy $$\Omega = \pm R^{p_1}L^{q_1} \cdots R^{p_s}L^{q_s},$$

Then the maximal cusp boundary ${\partial}C$ contains $4s/3$ disjoint disks, each of radius at least $$\min \left\{ \frac{1}{4}, \, \frac{\sqrt{2} \, \mu^2}{14}
\right\}.$$
:::

::: proof
*Proof.* Consider the edge set $E$, as above. By Lemma [\[lemma:edge-count\]](#lemma:edge-count){reference-type="ref" reference="lemma:edge-count"}, $E$ contains at least $2s/3$ edges of length at most $\ln(7/\mu^2)$. Now, lift everything to the universal cover ${\mathbb{H}}^3$, in such a way that ${\partial}C$ lifts to the horizontal plane at height $1$. In a single fundamental domain for ${\partial}C$, each edge $e \in E$ corresponds to two horospheres: one horosphere for each endpoint of $e$. Hence ${\partial}
C$ contains $4s/3$ shadows of disjoint horospheres, each of which has radius at least $\mu^2/14$. If two disjoint horospheres have the same size, then they also have disjoint projections. Thus, by shrinking each horosphere to radius $\mu^2/14$, we conclude that ${\partial}C$ contains $4s/3$ disjoint disks of radius $\mu^2/14$.

Next, we claim that the disks on ${\partial}C$ can be enlarged considerably while staying disjoint. Let $x$ and $y$ be the centers of two of these disks. In other words, $x \in {\partial}C \cap e_i$ and $y \in {\partial}
C \cap e_j$ for some $e_i, e_j \in E$. The two edges $e_i, e_j$ lead to horospheres $H_i$ and $H_j$. Let $f$ be the geodesic that connects $H_i$ directly to $H_j$. Consider the length of $f$ outside $H_i$ and $H_j$. There are two cases:

[Case 1: the length of $f$ is at least $\ln(2)$.]{.underline} In this case, the midpoint of $f$ lies at distance at least $\ln(2)/2$ from both $H_i$ and $H_j$. If we apply an isometry $I$ that sends ${\partial}
H_i$ to the horosphere at Euclidean height $1$, the midpoint of $I(f)$ will lie at height at most $1/\sqrt{2}$. In other words, the horosphere $I(H_i)$ can be expanded by a factor of $\sqrt{2}$ without hitting the midpoint of $I(f)$, and similarly for $H_j$. Of course, this still holds true before applying the isometry $I$: each of $H_i$ and $H_j$ can be expanded by a factor of $\sqrt{2}$ while staying disjoint from each other. Since each of $H_i$ and $H_j$ has radius at least $\mu^2/14$, the disks of radius $\sqrt{2}\mu^2/14$ centered at $x$ and $y$ in ${\partial}C$ are disjoint from each other.

[Case 2: $f$ is shorter than $\ln(2)$.]{.underline} Then, by Lemma [\[lemma:length-non-canonical\]](#lemma:length-non-canonical){reference-type="ref" reference="lemma:length-non-canonical"}, $f$ must be an edge of the canonical triangulation. Since $e_i$ and $e_j$ are also edges of the canonical triangulation, these three edges bound an ideal triangle contained in some pleated surface $T_\alpha$. Now, recall that at the end of our selection procedure for the set $E$, if two distinct edges of $T_\alpha$ belong to $E$, then they are the shortest edges in $T_\alpha$. Thus both $e_i$ and $e_j$ are shorter than $\ln(2)$. Since the edges $e_i$ and $e_j$ are already vertical in ${\mathbb{H}}^3$ and meet the cusp at Euclidean height $1$, the horospheres $H_i$ and $H_j$ must have diameter at least $1/2$. Thus $H_i$ and $H_j$ project to disjoint disks of radius at least $1/4$ centered at $x$ and $y$ on ${\partial}C$.

In every case, the points $x,y \in {\partial}C$ are the centers of disjoint disks of radius at least $$\min \left\{ \frac{1}{4}, \, \frac{\sqrt{2} \, \mu^2}{14}
\right\}.$$

There are $4s/3$ such disks, completing the proof. ◻
:::

We may now estimate the area of ${\partial}C$.

::: lemma
[]{#lemma:cusp-area-mu label="lemma:cusp-area-mu"} Let $M$ be a punctured--torus bundle with monodromy $$\Omega = \pm R^{p_1}L^{q_1} \cdots R^{p_s}L^{q_s}.$$

Let $C$ be a maximal horoball neighborhood about the cusp of $M$. Then $$\frac{16 \sqrt{3}}{147} \, s \; \leq \; \sqrt{3}\, s \, \min\left\{
\frac{1}{6}, \, \frac{4 \mu^4}{147} \right\} \; \leq \; {\rm area}({\partial}C)
\;<\; 2 \sqrt{3} \,\, \frac{v_8}{v_3} \, s.$$
:::

::: proof
*Proof.* There are three inequalities in the statement, and we consider them in turn.

[First inequality.]{.underline} This follows immediately from Lemma [\[lemma:meridian\]](#lemma:meridian){reference-type="ref" reference="lemma:meridian"}, which gives $\mu \geq \sqrt{2}$. Note that with our definition of $\mu$ (see Definition [\[def:fibered-meridian\]](#def:fibered-meridian){reference-type="ref" reference="def:fibered-meridian"}), the conclusion of Lemma [\[lemma:meridian\]](#lemma:meridian){reference-type="ref" reference="lemma:meridian"} transfers perfectly from $4$--punctured sphere bundles to punctured torus bundles.

[Second inequality.]{.underline} By Lemma [\[lemma:disjoint-disks\]](#lemma:disjoint-disks){reference-type="ref" reference="lemma:disjoint-disks"}, ${\partial}C$ contains $4s/3$ disjoint disks of equal radius, whose total area is at least $$\frac{4s}{3} \cdot \pi \min\left\{\frac{1}{16}, \, \frac{\mu^4}{98}
\right\}.$$

Now, a classical result (see e.g. [@boroczky Theorem 1]) states that a packing of the plane by circles of equal size has density at most $\pi/(2 \sqrt{3})$. This gives the desired inequality.

[Third inequality.]{.underline} A result of Agol gives that ${\rm vol}(M) <
2v_8 \, s$ (see [@gf:two-bridge Theorem B.1] for a direct proof). Also, a horosphere packing theorem of Böröczky [@boroczky Theorem 4] states that a maximal cusp in a hyperbolic $3$--manifold contains at most $\sqrt{3}/(2v_3)$ of the volume of $M$. Putting these results together gives $${\rm vol}(C) \:<\: \sqrt{3} \,\, \frac{v_8}{v_3} \, s, \quad
\mbox{hence} \quad 
{\rm area}({\partial}C) \:<\: 2 \sqrt{3} \,\, \frac{v_8}{v_3} \, s.$$ ◻
:::

::: remark
In the proof of Lemma [\[lemma:disjoint-disks\]](#lemma:disjoint-disks){reference-type="ref" reference="lemma:disjoint-disks"}, we also showed that ${\partial}C$ contains $4s/3$ disjoint disks of radius $\mu^2/14$. Plugging this estimate into the proof of Lemma [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"} gives $${\rm area}({\partial}C) \: \geq  \: \frac{2 \sqrt{3} \, \mu^4}{147} \, s.$$

This statement, although apparently weaker than Lemma [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"}, will prove useful for estimating the lengths of slopes on ${\partial}C$.
:::

::: lemma
[]{#lemma:ptorus-slope-length label="lemma:ptorus-slope-length"} Let $M$ be a punctured--torus bundle with monodromy $$\Omega = \pm R^{p_1}L^{q_1} \cdots R^{p_s}L^{q_s}.$$

Let $C$ be a maximal horoball neighborhood about the cusp of $M$. If $\gamma$ is any simple closed curve on ${\partial}C$ that is transverse to the fibers, $\ell(\gamma) \geq 4\sqrt{6} \, s/147$.
:::

::: proof
*Proof.* Define the *height* of the cusp to be $h := {\rm area}({\partial}C)/2\mu$. Then $\ell(\gamma) \geq h$. Note that by Lemma [\[lemma:meridian\]](#lemma:meridian){reference-type="ref" reference="lemma:meridian"}, $\mu \geq \sqrt{2}$. Also, since a maximal horocycle in a punctured torus has length at most $6$, it follows that $\mu \leq 3$. We consider three possibilities for the values of $\mu$ in the range $[\sqrt{2}, 3]$.

If $\sqrt{2} \leq \mu \leq \sqrt{7}/ 2^{3/4}$, then $4 \mu^4/147 \leq
1/6$. Thus, by Lemma [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"}, $${\rm area}({\partial}C) \, \geq \, \frac{4 \sqrt{3} \, \mu^4}{147} \, s,
 \quad \mbox{hence} \quad \ell(\gamma) \, \geq \, \frac{2\sqrt{3} \,
 \mu^3}{147} \, s \, \geq \, \frac{4\sqrt{6} \,s}{147} \, \approx \,
 0.066652 \, s.$$

If $\sqrt{7}/ 2^{3/4} \leq \mu \leq 2$, then $1/6 \leq 4
\mu^4/147$. Thus, by Lemma [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"}, $${\rm area}({\partial}C) \, \geq \, \frac{\sqrt{3} \, s}{6}, \quad
 \mbox{hence} \quad \ell(\gamma) \, \geq \, \frac{\sqrt{3} \, s}{12
 \mu} \, \geq \, \frac{\sqrt{3} \, s}{24} \, \approx \, 0.072168 \,
 s.$$

If $2 \leq \mu \leq 3$, then by the remark following Lemma [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"}, $${\rm area}({\partial}C) \, \geq \, \frac{ 2\sqrt{3} \, \mu^4}{147} \, s,
 \quad \mbox{hence} \quad \ell(\gamma) \, \geq \, \frac{\sqrt{3} \,
 \mu^3}{147} \, s \, \geq \, \frac{8 \sqrt{3} \,s}{147} \, \approx \,
 0.094261 \, s.$$

Therefore, for all possible values of $\mu$, we have $\ell(\gamma)
\geq 4\sqrt{6} \, s/147$. ◻
:::

Lemmas [\[lemma:cusp-area-mu\]](#lemma:cusp-area-mu){reference-type="ref" reference="lemma:cusp-area-mu"} and [\[lemma:ptorus-slope-length\]](#lemma:ptorus-slope-length){reference-type="ref" reference="lemma:ptorus-slope-length"} complete the proof of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}.

Combining the results of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} with our work in [@fkp-07 Theorem 1.1], we obtain the following immediate corollary for volumes of Dehn fillings of punctured torus bundles.

::: corollary
[]{#cor:ptorus-volume label="cor:ptorus-volume"} Let $M$ be a punctured--torus bundle with monodromy of length $s>94$. Let $C$ be a maximal horoball neighborhood about the cusp of $M$. For any simple closed curve $\gamma$ on ${\partial}C$ that is transverse to the fibers, let $M_{\gamma}$ denote the 3--manifold obtained from $M$ by Dehn filling ${\partial}C$ along $\gamma$. Then $M_{\gamma}$ is hyperbolic, and $$\left(1-\dfrac{7203 \, \pi^2 }{8 \, s^2} \right)^{3/2} 2 v_3 \, s\:
 \leq \: {\rm vol}(M_{\gamma}) \: < \: 2v_8 \, s,$$ where $v_3 = 1.0149...$ is the volume of a regular ideal tetrahedron and $v_8 = 3.6638...$ is the volume of a regular ideal octahedron.
:::

::: proof
*Proof.* By Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, the slope length of $\gamma$ will be at least $2\pi$ when $s\geq 95$. For such slopes, by [@fkp-07 Theorem 1.1] we know the volume of the manifold obtained by Dehn filling along the slope of length $\ell(\gamma)$ is at least $${\rm vol}(M_{\gamma}) \geq \left( 1-\left(\frac{2\pi}{\ell(\gamma)}
\right)^2 \right)^{3/2}{\rm vol}(M).$$

Hence, using the volume bound for such manifolds given by [@gf:two-bridge Theorem B.1], and the estimate on slope length of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, we have $${\rm vol}(M_{\gamma}) \geq \left(1-\dfrac{7203\,\pi^2}{8\, s^2}\right)^{3/2}
2 v_3 \, s.$$

For the upper bound, recall that volume only decreases under Dehn filling [@thurston:notes], and so the result follows immediately from [@gf:two-bridge Theorem B.1]. ◻
:::

## 4--punctured sphere bundles

::: theorem
[]{#thm:4ps-area label="thm:4ps-area"} Let $N$ be a $4$--punctured sphere bundle with monodromy $$\Omega = R^{p_1}L^{q_1} \cdots R^{p_s}L^{q_s},$$

and with the property that the monodromy fixes one preferred boundary circle of the $4$--holed sphere. Let $D$ be the maximal horoball neighborhood of the cusp corresponding to this preferred puncture, and let $\gamma$ be any simple closed curve on ${\partial}D$ that is transverse to the fibers. Then $${\rm area}({\partial}D) \: \geq \: \frac{16 \sqrt{3}}{147} \, s \quad \mbox{and}
\quad \ell(\gamma) \: \geq \: \frac{8\sqrt{3}}{147} \, s.$$
:::

::: proof
*Proof.* As described in Section [\[sec:4ps\]](#sec:4ps){reference-type="ref" reference="sec:4ps"}, the $4$--punctured sphere bundle $N$ is commensurable to a punctured--torus bundle $M$ with the same monodromy $\Omega$. (The common cover is a $4$--punctured torus bundle $P$.) Let $C$ be the maximal cusp neighborhood in $M$. Then, by lifting $C$ to a cusp neighborhood in $P$ and projecting down to $N$, we obtain a maximal *equivariant* neighborhood of the cusps of $N$.

Let $B$ be the cusp neighborhood of the preferred puncture in the equivariant expansion of the cusps of $N$. Because the cusp neighborhood $C \subset M$ lifts to 4 distinct cusps in $P$, and one of those cusps double--covers $B$, Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} implies that $$2 \cdot {\rm area}({\partial}B) \: = \: {\rm area}({\partial}C) \: \geq \: \frac{16
\sqrt{3}}{147} \, s.$$

Observe that in the canonical triangulation of $N$, every edge lies in a pleated fiber, and connects two distinct punctures of the $4$--punctured sphere. Thus no edge of the canonical triangulation has both endpoints inside $B$. By Lemma [\[lemma:length-non-canonical\]](#lemma:length-non-canonical){reference-type="ref" reference="lemma:length-non-canonical"}, this means that the shortest arc from $B$ to $B$ has length at least $\ln(2)$, and we may expand $B$ by a factor of at least $\sqrt{2}$ before it bumps into itself. Therefore, every linear measurement on ${\partial}D$ is at least a factor of $\sqrt{2}$ greater than on ${\partial}B$, and $${\rm area}({\partial}D) \: \geq \: 2 \cdot {\rm area}({\partial}B) \: = \: {\rm area}({\partial}
C) \: \geq \: \frac{16 \sqrt{3}}{147} \, s.$$

By the same argument, every simple closed curve on ${\partial}D$ is at least a factor of $\sqrt{2}$ longer than the corresponding loop on ${\partial}B$. Thus, if $\gamma$ is transverse to the fibers of $N$, $\ell(\gamma) \geq 8\sqrt{3} \, s/147$. ◻
:::

We remark that by Theorem [\[thm:4ps-area\]](#thm:4ps-area){reference-type="ref" reference="thm:4ps-area"}, an analogue of Corollary [\[cor:ptorus-volume\]](#cor:ptorus-volume){reference-type="ref" reference="cor:ptorus-volume"} also holds for fillings of 4--punctured sphere bundles. One important class of manifolds obtained by Dehn filling (one cusp of) a $4$--punctured sphere bundle is the class of closed 3--braids in $S^3$. We shall focus on these manifolds below, in Section [\[sec:volume3braids\]](#sec:volume3braids){reference-type="ref" reference="sec:volume3braids"}.
