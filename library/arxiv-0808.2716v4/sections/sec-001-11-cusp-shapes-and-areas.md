---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-001-11-cusp-shapes-and-areas
section_title: "Cusp shapes and areas"
section_number: 1.1
pages: 1-3
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.985
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
In a finite--volume hyperbolic 3--manifold $M$, a horoball neighborhood of a torus boundary component becomes a *cusp*, homeomorphic to $T^2\times[0,\infty)$. Mostow--Prasad rigidity implies that each cross-sectional torus $T^2$ is endowed with a flat metric, or *cusp shape*, that is determined up to similarity by the topology of $M$. When $M$ has a single torus boundary component, we may expand a horoball neighborhood until it meets itself. This *maximal horoball neighborhood* completely determines a flat metric on the torus, and one can measure lengths of curves and area on the torus using this metric. We will refer to such a metric as a *maximal cusp metric*. Similarly, when a 3--manifold has multiple cusps, a maximal horoball neighborhood is given by expanding a collection of horoball neighborhoods until none can be exapanded further while keeping their interiors disjoint. In the case of multiple cusps, the choice of horoball neighborhoods is no longer unique. However, if we are required to expand the cusp neighborhoods in a fixed order, this expansion recipe once again determines a collection of maximal cusp metrics.

It is known, due to Nimershiem, that the set of similarity classes of tori that can be realized as cusps of hyperbolic 3--manifolds is dense in the moduli space of 2--tori [@nimershiem:flat-tori]. However, in general it is not known how to determine the cusp shape of a manifold. For simple manifolds, for example those built of a small number of ideal tetrahedra, or links with a small number of crossings, Weeks' computer program SnapPea will determine shapes of cusps and maximal cusp metrics [@weeks:snappea]. For other, larger classes of 3--manifolds, some bounds on cusp shape have been obtained. Aitchison, Lumsden, and Rubinstein found cusp shapes of certain alternating links, but the metrics they used were singular [@alr:alternating]. For non-singular hyperbolic metrics, Adams *et al.* found upper bounds on the cusp area of knots, in terms of the crossing number of a diagram [@adams-students:cusp-area]. Purcell found that for "highly twisted" knots, the lengths of shortest arcs on a maximal cusp metric are bounded above and below in terms of the twist number of a diagram [@purcell:cusps]. These results were obtained using cusp estimates on a class of links called fully augmented links, whose cusp shapes and lengths of slopes on maximal cusp metrics were also worked out by Purcell [@purcell:cusps] and Futer and Purcell [@futer-purcell].

In this paper, we prove explicit, readily applicable bounds on cusp shapes and maximal cusp metrics of punctured torus bundles and 4--punctured sphere bundles, as well as of 2--bridge knot complements. These manifolds have a natural ideal triangulation, first discovered for punctured torus bundles by Floyd and Hatcher [@floyd-hatcher], and later studied by many others [@akiyoshi; @aswy; @gueritaud:thesis; @lackenby:punct]. One feature that makes these 3--manifolds particularly attractive is that their geometry can be described in terms of the combinatorics of the Farey tessellation of ${\mathbb{H}}^2$. Hence, we refer to these manifolds as *Farey manifolds*.

To state an example of our results in this direction, let $M$ be a hyperbolic once--punctured torus bundle. The monodromy of $M$ can be thought of as a conjugacy class in $SL_2({\mathbb{Z}})$. As such, it has a (unique up to cyclic permutation of factors) presentation of the form $$\pm \begin{bmatrix} 1 & a_1 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ b_1& 1 \end{bmatrix} \cdots \cdots \cdots
\begin{bmatrix} 1 & a_s \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ b_s & 1\end{bmatrix},$$

where $a_i$, $b_i$ are positive integers. The integer $s$ is called the *length* of the monodromy.

::: named
Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} Let $M$ be a punctured--torus bundle with monodromy of length $s$. Let $C$ be a maximal horoball neighborhood about the cusp of $M$. Then $$\frac{16 \sqrt{3}}{147} \, s \: \leq \: {\rm area}({\partial}C) \:<\: 2
\sqrt{3} \, \frac{v_8}{v_3} \, s,$$

where $v_3 = 1.0149...$ is the volume of a regular ideal tetrahedron and $v_8 = 3.6638...$ is the volume of a regular ideal octahedron.

Furthermore, if $\gamma$ is a non-trivial simple closed curve on ${\partial}
C$ (that is, any simple closed curve that is transverse to the fibers), then its length $\ell(\gamma)$ satisfies $$\ell(\gamma) \: \geq \: \frac{4\sqrt{6}}{147} \, s.$$
:::

The proof of Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} contains two main steps. First, we derive an estimate for the size of horoballs in the universal cover of punctured torus bundles (see Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}). Then, we pack the cusp torus with the shadows of these horoballs.

Our estimate on horoball size should be compared with Jørgensen's work on quasifuchsian punctured torus groups, which appears in a well--known but unfinished manuscript [@jorgensen]. A careful exposition of Jørgensen's work was given by Akiyoshi, Sakuma, Wada, and Yamashita [@aswy-book]. Jørgensen's results can be applied in our setting to show that the universal cover of a punctured torus bundle contains a number of maximal horoballs whose size is bounded from below (see [@jorgensen Lemma 4.3] and [@aswy-book Lemma 8.1.1]). Jørgensen conjectured the existence of a much better lower bound for this horoball size; and indeed, our Proposition 3.6 improves Jørgensen's lower bound by a factor of more than $10$. This improvement is very important in our setting, since a 10--fold improvement in horoball size yields a 100--fold improvement in the cusp area estimate. See the end of Section [\[subsec:large-horosphere\]](#subsec:large-horosphere){reference-type="ref" reference="subsec:large-horosphere"} for a more detailed discussion.
