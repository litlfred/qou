---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-007-8-results
section_title: "Results"
section_number: 8
pages: 20-21
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.995
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:results label="sec:results"}

Our implementation of the algorithm in Section [\[sec:algo\]](#sec:algo){reference-type="ref" reference="sec:algo"} is available at [@veriClosedRepo]. Lists of all knots and links from Theorem [\[thm:hyperbolicBranchedDoubleCovers\]](#thm:hyperbolicBranchedDoubleCovers){reference-type="ref" reference="thm:hyperbolicBranchedDoubleCovers"} as well as the isomorphism signatures of the finite triangulations we used are available at [@veriClosedData].

To produce the input to the algorithm, we used SnapPy [@SnapPy] to produce a finite triangulation of a manifold and Orb [@orb] to find unverified floating point edge parameters. Note that there are finite triangulations that admit hyperbolic structures but Orb is unable to find one. However, for all examples of hyperbolic manifolds considered here, we are always able to make Orb succeed in finding edge parameters by randomizing the finite triangulation in SnapPy several times.

We were able to verify a hyperbolic structure on a finite triangulation of each of the 11031 orientable closed manifolds in the Hodgson-Weeks census [@hwcensus] and the 21962 genus 2 surface bundles and 3100 genus 3 surface bundles in the census by Bell [@bellBundleCensus]. In particular, we have an independent proof of [@hikmot Theorem 5.2] that all manifolds in SnapPy's `OrientableClosedCensus` are hyperbolic.

To prove Theorem [\[thm:hyperbolicBranchedDoubleCovers\]](#thm:hyperbolicBranchedDoubleCovers){reference-type="ref" reference="thm:hyperbolicBranchedDoubleCovers"}, we went through all knots and links up to 15, respectively, 14 crossings tabulated by Hoste-Thistlethwaite[^1] and used SnapPy to produce the branched double cover. We either used the above method to prove that the resulting manifold is hyperbolic or used Regina [@Regina] to prove that it is not hyperbolic by

-   finding the triangulation in Regina's census or

-   recognizing that the triangulation has a structure fitting one of Regina's\
    `StandardTriangulation`'s making it, e.g., a Seifert fiber space, or

-   finding an essential torus using normal surface theory.

Note that the first two methods sometimes require some randomizations and simplifications of the triangulation in SnapPy to work and that the last method can be quite expensive.

The number of tetrahedra in the triangulations used to prove hyperbolicity was between 9 and 46. Most triangulations are single vertex, few have two vertices, and only one had three vertices.

Testing the algorithm on the bundle census and branched double covers was suggested by Nathan Dunfield since the geodesics isotopic to the components of the branching locus tend to be long and spun triangulations spinning about one of these geodesics very often fail to be geometric. By filling and drilling the triangulation, Dunfield found geometric spun triangulations (about a different geodesic) for the branched double covers of 42367 non-alternating knots and links up to 14 crossings, missing 1593.

::: remark
[]{#remark:experimentEdgePartition label="remark:experimentEdgePartition"} We also investigate how the occurrence of gimbal lock depends on the edge partition $E^{\sim}\cup E^==E(\mathcal{T})$ with $|E^{\sim}|=3o$ where $o$ is number of vertices. For this, we fix a triangulation and a hyperbolic structure and check numerically whether the derivative $Dg$ of the gimbal function has singular values close to zero for different partitions (exhausting all partitions when $o\leq 2$ and sampling otherwise). We did this for several triangulations of orientable closed census manifolds including some with three and four vertices obtained by performing 1-4 moves. This lead to Conjecture [\[conjecture:main\]](#conjecture:main){reference-type="ref" reference="conjecture:main"}.
:::

[^1]: See `HTLinkExteriors`, `AlternatingKnotExteriors`, and `NonalternatingKnotExteriors` in SnapPy.
