---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-024-53-volume-estimates
section_title: "Volume estimates"
section_number: 5.3
pages: 32-34
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.93
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
For sufficiently long generic $3$--braids, the methods of the previous sections estimate hyperbolic volume.

::: theorem
[]{#thm:3braid-volume label="thm:3braid-volume"} Let $K= \hat{w}$ be the closure of a generic 3--braid $w \sim C^k
\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $p_i$, $q_i$ are all positive and $w \nsim
\sigma_1^p\sigma_2^{-q}$. Then $K$ is hyperbolic, and $$\label{eq:3braid-volume}
4v_3 \, s - 276.6 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 4v_8 \, s.$$ Furthermore, the multiplicative constants in both the upper and lower bounds are sharp.
:::

::: proof
*Proof.* Let $A$ be the braid axis of $K$. Then $M_w = S^3 {\smallsetminus}(K \cup
A)$ is a 4--punctured sphere bundle with monodromy $$\Omega = L^{p_1} R^{q_1} \cdots L^{p_s} R^{q_s}.$$

Futer and Guéritaud showed [@gf:two-bridge Corollary B.2] that the length of $\Omega$ coarsely determines the volume of $M$: $$\label{eq:bundle-volume}
4 v_3 \, s \: \leq \: {\rm vol}(M_w) \: < \: 4v_8 \, s,$$ where both the upper and lower bounds are sharp. That is: there exist $4$--punctured sphere bundles that realize the lower bound, and other bundles that are $\varepsilon$--close to the upper bound. Since $S^3
{\smallsetminus}K$ is obtained by Dehn filling on $M_w$, the same upper bound applies to the volume of $S^3 {\smallsetminus}K$. Furthermore, by choosing an extremely long filling slope (which will happen when ${\left\vert k \right\vert} \to \infty$), one can arrange for ${\rm vol}(S^3 {\smallsetminus}K)$ to be arbitrarily close to $4 v_8 \, s$.

For the lower bound on volume, we rely on Theorem [\[thm:4ps-area\]](#thm:4ps-area){reference-type="ref" reference="thm:4ps-area"}. That theorem states that the meridian of $A$ (which will be transverse to the fibers) has length at least $8\sqrt{3} \, s/147$. In particular, when $s \geq 67$, the meridian will be longer than $2\pi$. Thus we may apply Theorem 1.1 of [@fkp-07], which estimates the change in volume under Dehn filling along slopes longer than $2\pi$. For all $s \geq 67$, we obtain $$\begin{array}{l l l l l}
{\rm vol}(S^3 {\smallsetminus}K) 
&\geq&  \left(1-\left(\dfrac{2\pi}{8\sqrt{3} \, s/147}\right)^2\right)^{3/2} {\rm vol}(M_w), 
& \mbox{by \cite[Thm 1.1]{fkp-07} and Thm \ref{thm:4ps-area} }\\
&\geq&  \left(1-\dfrac{7203  \, \pi^2 }{16 \, s^2} \right)^{3/2} 4 v_3 \, s,
& \mbox{by inequality (\ref{eq:bundle-volume})}
\end{array}$$ Note that by calculus, $$\left(1-\dfrac{7203 \, \pi^2}{16\,s^2}\right)^{3/2} 4 v_3 \, s -
4v_3\,s$$ has a minimum of $-276.52\cdots$ for $s\geq 67$. Thus ${\rm vol}(S^3
{\smallsetminus}K) > 4v_3\,s - 276.6$.

On the other hand, if $s \leq 67$, then $4v_3 \, s - 276.6 < 0$, hence the volume estimate is trivially true. Thus the lower bound on volume holds for all hyperbolic $3$--braids.

Finally, to show sharpness of the multiplicative constant in the lower bound, consider $3$--braids of the form $w=(\sigma_1
\sigma_2^{-1})^s$. In the proof of Theorem B.1 of [@gf:two-bridge], it was shown that for the closures of these braids, ${\rm vol}(M_w) = 4v_3s$. Since ${\rm vol}(S^3{\smallsetminus}K) < {\rm vol}(M_w)
= 4v_3s$ for this sequence of knots, the multiplicative constant $4v_3$ must be sharp. ◻
:::

We close this section with an interesting side comment. Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} compares in an intriguing way to prior results that estimate the volume of a link complement in terms of the twist number of a diagram. (See Section [\[sec:diagram-intro\]](#sec:diagram-intro){reference-type="ref" reference="sec:diagram-intro"} and the introduction of [@fkp:coils] for definitions and background.) In the braid word $w$, each term $\sigma_1^{p_i}$ or $\sigma_2^{-q_i}$ corresponds to a twist region involving a pair of strands of $K$. Meanwhile, when $k \neq 0$, the term $C^k$ defines a single *generalized twist region*, in which we perform $k$ full twists on all three strands of the braid. Altogether, the braid word $w$ defines a diagram with either $2s$ or $2s+1$ generalized twist regions -- including $2s$ ordinary twist regions twisting on two strands of $K$. As a result, Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} can be reformulated in the following way.

::: corollary
[]{#cor:3braid-twists label="cor:3braid-twists"} Let $K$ be a hyperbolic closed 3--braid, and let $D(K)$ be the braid diagram corresponding to the Schreier normal form for $K$. If ${t_{\mathrm{gen}}(D)}$ denotes the number of generalized twist regions in the diagram $D$, then $$2v_3 \, {t_{\mathrm{gen}}(D)}- 279 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 2v_8 \,
{t_{\mathrm{gen}}(D)}.$$
:::

::: proof
*Proof.* By Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}, $K$ must be represented by a generic word $w = C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots
\sigma_1^{p_s} \sigma_2^{-q_s}$. Substituting $2s \leq {t_{\mathrm{gen}}(D)}\leq 2s+1$ into Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} gives the desired volume estimate. ◻
:::

::: remark
In [@fkp:coils Corollary 3.2], we show that the twist number alone, as opposed to the generalized twist number, is not a good measure of the volume of 3--braids. Thus the single generalized twist region from the term $C^k$ is important in the corollary above.
:::
