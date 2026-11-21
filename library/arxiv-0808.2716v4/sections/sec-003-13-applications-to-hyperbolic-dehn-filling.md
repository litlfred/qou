---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-003-13-applications-to-hyperbolic-dehn-filling
section_title: "Applications to hyperbolic Dehn filling"
section_number: 1.3
pages: 4-5
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
The shapes of the cusps and their actual metrics give information not just on the 3--manifold itself, but also on the Dehn fillings of that manifold.

For example, modulo the geometrization conjecture, several theorems imply that Dehn fillings on slopes of sufficient length yield hyperbolic manifolds (these are the $2\pi$--Theorem, due to Gromov and Thurston [@bleiler-hodgson]; the 6--Theorem, due to Agol [@agol:bounds] and Lackenby [@lackenby:word]; and the $7.515$--Theorem, due to Hodgson and Kerckhoff [@hk:univ]). When we combine these theorems with the results on maximal cusp areas and slope lengths above, we find that Farey manifolds with long monodromy admit no non-trivial Dehn fillings, where "long" is explicit.

In particular, Bleiler and Hodgson [@bleiler-hodgson] note that the work of Jørgensen [@jorgensen] combined with the $2\pi$--Theorem implies that there is a constant $N$ such that every non-trivial Dehn filling of a punctured torus bundle with monodromy length $s>N$ gives a hyperbolic 3--manifold. However, they remark on the lack of an explicit value for the constant $N$. Now Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, coupled with the 6--Theorem, allows the estimate $N\leq 90$.

More recently, the authors proved a result that bounds the volume of manifolds obtained by Dehn filling along a slope of length at least $2\pi$, in terms of the length of that slope [@fkp-07]. Thus we may combine Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} with this recent result to estimate the volumes of the manifolds obtained by Dehn filling. For example, if $M$ is a punctured--torus bundle with monodromy of length $s>94$, then the length of any non-trivial slope $\gamma$ on the cusp of $M$ (i.e. any slope transverse to the fibers) will be at least $2\pi$. Then by [@fkp-07 Theorem 1.1], the volume of the manifold $M(\gamma)$ obtained by Dehn filling $M$ along $\gamma$ will be bounded explicitly below. See Corollary [\[cor:ptorus-volume\]](#cor:ptorus-volume){reference-type="ref" reference="cor:ptorus-volume"}.

One large class of examples obtained by Dehn filling 4--punctured sphere bundles is the class of closed 3--braids, which has been extensively studied by others (see e.g. Murasugi [@murasugi:3braids], Birman and Menasco [@birman-menasco:3braids]). In this paper, we classify the hyperbolic links that are closed 3--braids (see Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}), and obtain the first estimates on volumes of these links.

<figure id="fig:3braid-generators">
<div class="center">
<embed src="figures/Fig_braid-generators.eps" />
</div>
<figcaption>Braid group generators <span class="math inline"><em>σ</em><sub>1</sub></span> and <span class="math inline"><em>σ</em><sub>2</sub></span>.</figcaption>
</figure>

To state these results, let $\sigma_1$, $\sigma_2$ denote the generators for $B_3$, the braid group on three strands, as in Figure [1](#fig:3braid-generators){reference-type="ref" reference="fig:3braid-generators"}. Let $C= (\sigma_1 \sigma_2)^3$. It is known, by work of Schreier [@schreier], that most $3$--braids are conjugate to words of the form $w = C^k \sigma_1^{p_1} \sigma_2^{-q_1}
\cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $p_i$, $q_i$ are all positive. In particular, all $3$--braids with hyperbolic closures are of this form, as we shall show in Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}. Following Birman and Menasco [@birman-menasco:3braids], we call such braids *generic*.

::: named
Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} Let $K= \hat{w}$ be the closure of a generic 3--braid $w = C^k
\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $C= (\sigma_1 \sigma_2)^3$, and $p_i$, $q_i$ are all positive. Suppose, furthermore, that $w$ is not conjugate to $\sigma_1^{p}
\sigma_2^q$ for arbitrary $p$, $q$. Then $K$ is hyperbolic, and $$4v_3 \, s - 277 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 4v_8 \, s,$$

where $v_3 = 1.0149...$ is the volume of a regular ideal tetrahedron and $v_8 = 3.6638...$ is the volume of a regular ideal octahedron. Furthermore, the multiplicative constants in both the upper and lower bounds are sharp.
:::
