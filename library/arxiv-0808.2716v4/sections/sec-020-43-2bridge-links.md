---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-020-43-2bridge-links
section_title: "2–bridge links"
section_number: 4.3
pages: 26-27
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.98
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
::: theorem
[]{#thm:2bridge label="thm:2bridge"} Let $K$ be a 2--bridge link in $S^3$, whose reduced alternating diagram has twist number $t$. Let $C$ be a maximal neighborhood about the cusps of $S^3 {\smallsetminus}K$, in which the two cusps have equal volume if $K$ has two components. Then $$\frac{8\sqrt{3}}{147}\,(t-1) \: \leq \: {\rm area}({\partial}C) \: <\:
2\sqrt{3}\,\, \frac{v_8}{v_3}\,(t-1).$$

Furthermore, if $K$ is a knot, let $\gamma$ be any non-trivial arc that starts on a meridian and comes back to the same meridian (for example, a non-meridional simple closed curve). Then its length satisfies $$\ell(\gamma) \: \geq \: \frac{4\sqrt{6\sqrt{2}}}{147}\, (t-1).$$
:::

::: proof
*Proof.* Let $\mu$ denote the length of a meridian of $K$ on ${\partial}C$. By Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}, every pleated surface $S_i$ in $S^3
{\smallsetminus}K$ contains at least one edge of length at most $\ln(\mu^2/7)$. Furthermore, opposite edges in $S_i$ have the same length, because the geometry of each pleated surface is preserved by the full symmetry group of its triangulation. Thus, if $S_i$ is embedded in $S^3 {\smallsetminus}K$, it contains *two* edges of length at most $\ln(\mu^2/7)$. The only pleated surfaces that are not embedded are the folded surfaces $S_1$ or $S_c$ at the ends of the product region of $K$; each of these surfaces will contain at least one short edge. (See [@gf:two-bridge Figure 19] for a description of how surfaces are folded in the construction of a 2--bridge link.)

Now, we retrace the proof of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}. We construct the set of short edges $E$ exactly as above, except that we are now counting *pairs* of edges. Thus, if all three pairs of edges in a pleated surface are initially part of $E$, we remove the longest pair.

By the same argument as in Lemma [\[lemma:edge-count\]](#lemma:edge-count){reference-type="ref" reference="lemma:edge-count"}, $E$ contains at least $t/3$ distinct edge pairs. The two paired edges on a pleated surface $S$ will be distinct unless $S$ is $S_1$ or $S_c$. Thus, if both $S_1$ and $S_c$ contribute edges to $E$, the minimum possible number of edges (not pairs) is $2(t-1)/3$.

The proof of Lemma [\[lemma:disjoint-disks\]](#lemma:disjoint-disks){reference-type="ref" reference="lemma:disjoint-disks"} goes through without modification. As a result, ${\partial}C$ contains $4(t-1)/3$ disjoint disks, of radius at least $$r \geq \min \left\{ \frac{1}{4}, \, \frac{\sqrt{2} \, \mu^2}{14}
\right\}, \qquad \mbox{hence total area} \quad \geq \frac{4(t-1)}{3}
\cdot \pi \min\left\{\frac{1}{16}, \, \frac{\mu^4}{98} \right\}.$$ Dividing by the maximal density $\pi/2\sqrt{3}$ of a circle packing in the plane gives $$\label{eqn:2bridge-area}
 {\rm area}({\partial}C) \geq 8(t-1) \, \frac{\sqrt{3}}{3} \,
\min\left\{\frac{1}{16}, \, \frac{\mu^4}{98} \right\}.$$

To complete the proof of the lower bound, we note that for all 2--bridge links except the figure--8 knot and $5_2$ knot, the meridian $\mu$ is at least $\sqrt[4]{2}$, by work of Adams [@adams:waist2]. Thus the area is at least $8\sqrt{3}\,(t-1)/147$. Meanwhile, the figure--8 and $5_2$ knots have twist number $t=2$, hence the estimate $8\sqrt{3}/147$ is vastly lower than their true cusp area (note a standard horosphere packing argument implies the area of any cusp is at least $\sqrt{3}$).

For the upper bound, Futer and Guéritaud [@gf:two-bridge Theorem B.3] found that the volume of a hyperbolic 2--bridge knot satisfies ${\rm vol}(S^3{\smallsetminus}K) < 2v_8(t-1)$. Again, combining this with the theorem of Böröczky [@boroczky Theorem 4], that a maximal cusp contains at most $\sqrt{3}/(2v_3)$ of the volume of $M$, we find $${\rm vol}(C) \: < \: \sqrt{3}\,\, \frac{v_8}{v_3}\,(t-1), \quad
\mbox{hence} \quad {\rm area}({\partial}C) \:<\: 2 \sqrt{3}\,\,
\frac{v_8}{v_3}\,(t-1).$$

Finally, for the result on arc length, note that the shortest non-trivial arc $\gamma$ that starts and ends on the same meridian has length equal to ${\rm area}({\partial}C)/\mu$. Again using the estimate of Adams [@adams:waist2; @adams:2-gen], the length of a meridian of $K$ satisfies $\sqrt[4]{2} \leq \mu \leq 2$, except if $K$ is the figure--8 or $5_2$ knot. Combining Adams's estimates with inequality ([\[eqn:2bridge-area\]](#eqn:2bridge-area){reference-type="ref" reference="eqn:2bridge-area"}) and arguing as in Lemma [\[lemma:ptorus-slope-length\]](#lemma:ptorus-slope-length){reference-type="ref" reference="lemma:ptorus-slope-length"} gives the desired lower bound on $\ell(\gamma)$. (As above, the figure--8 and $5_2$ knots need to be checked separately.) ◻
:::
