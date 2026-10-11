---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-003-14-statement-of-results
section_title: "Statement of results"
section_number: 1.4
pages: 3-5
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.909
---
We briefly state our main results about the triangulation independent Ptolemy varieties. A summary of their definition is given in Section [0.1](#sec:Algorithm){reference-type="ref" reference="sec:Algorithm"}, and explicit computations are given in Section [\[sec:Examples\]](#sec:Examples){reference-type="ref" reference="sec:Examples"}. Let $M$ be a compact, orientable $3$-manifold with non-empty boundary, and let $\mathcal T$ be a topological ideal triangulation of $M$.

Any $P$-decorated boundary-unipotent representation $\rho\colon\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$ assigns Ptolemy coordinates to the edges of $\mathcal T$ (see Section [\[sec:PtDecCocReview\]](#sec:PtDecCocReview){reference-type="ref" reference="sec:PtDecCocReview"}). If all Ptolemy coordinates are zero, we say that the decorated representation is *totally degenerate*. This notion turns out to be independent of the (ideal) triangulation and implies that the representation is reducible (see Section [\[sec:TotallyDegenerate\]](#sec:TotallyDegenerate){reference-type="ref" reference="sec:TotallyDegenerate"}).

Recall that although the set of representations of $\pi_1(M)$ is a variety, the set of representations up to conjugation is not a variety in general. The same holds for decorated representations. However, if we discard the totally degenerate decorations, we get a variety:

::: theorem
[]{#thm:MainResult label="thm:MainResult"} The conjugation action on the set of non totally degenerate decorated boundary-unipotent representations has a geometric quotient. For each triangulation $\mathcal T$ of $M$, the invariant Ptolemy variety $\overline P(\mathcal T)$ provides explicit coordinates, i.e. we have an isomorphism of varieties $$\label{eq:MainResult}
\overline P(\mathcal T)\cong\left\{\txt{Not totally degenerate, $P$-decorated, \\boundary-unipotent $\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}.$$ In particular, $\overline P(\mathcal T)$ is independent of the triangulation. Morever, $P(\mathcal T)$ embeds in $\overline P(\mathcal T)$ as a Zariski open subset. 0◻
:::

::: definition
A representation is *boundary-nondegenerate* if its restriction to $\pi_1(\partial_i M)$ is non-trivial for each boundary component $\partial_i M$ of $M$.
:::

Theorems [\[thm:OneToOneOverNonDegenerate\]](#thm:OneToOneOverNonDegenerate){reference-type="ref" reference="thm:OneToOneOverNonDegenerate"}, [\[thm:MainThmPSL\]](#thm:MainThmPSL){reference-type="ref" reference="thm:MainThmPSL"} and [\[thm:MainThmEnhanced\]](#thm:MainThmEnhanced){reference-type="ref" reference="thm:MainThmEnhanced"} below are elementary corollaries of Theorem [\[thm:MainResult\]](#thm:MainResult){reference-type="ref" reference="thm:MainResult"} and its analogues for the modified variants. They were previously known for representations admitting a *generic* decoration (see [@PtolemyField; @GaroufalidisThurstonZickert; @ZickertEnhancedPtolemy]).

::: theorem
[]{#thm:OneToOneOverNonDegenerate label="thm:OneToOneOverNonDegenerate"} The map $$\label{eq:RedOneToOne}
\overline P(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-unipotent\\$\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}$$ induced from [\[eq:MainResult\]](#eq:MainResult){reference-type="eqref" reference="eq:MainResult"} by ignoring the decoration has image containing all irreducible representations and is one-to-one over the set of irreducible boundary-nondegenerate representations.0◻
:::

::: theorem
[]{#thm:MainThmPSL label="thm:MainThmPSL"} Let $k=\big\vert H^1(M,\partial M;\mathbb Z/2\mathbb Z)\big\vert$. The map $$\label{eq:RedkToOne}
\overline P^\sigma(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-unipotent\\$\pi_1(M)\to\mathop{\mathrm{PSL}}(2,\mathbb C)$\\with obstruction class $\sigma$}\right\}\big/\mathop{\mathrm{Conj}}$$ has image containing all irreducible representations and is $k:1$ over the set of irreducible, boundary-nondegenerate representations. 0◻
:::

::: theorem
[]{#thm:MainThmEnhanced label="thm:MainThmEnhanced"} Suppose $M$ has $c$ boundary components, all of which are tori. There is a map $$\label{eq:RedTwoToOne}
\mathcal E\overline P(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-Borel\\$\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}$$ with image containing all irreducible representations. It is generically $2^c:1$ over the irreducible, boundary-nondegenerate representations. Moreover, the projection to the $(m_s,l_s)$ coordinates is the variety of eigenvalues of $\mu_s$ and $\lambda_s$.0◻
:::

This can be used to compute the $A$-polynomial; see Section [\[sec:Apolyexample\]](#sec:Apolyexample){reference-type="ref" reference="sec:Apolyexample"} for an example.

::: remark
The image of [\[eq:RedOneToOne\]](#eq:RedOneToOne){reference-type="eqref" reference="eq:RedOneToOne"}, [\[eq:RedkToOne\]](#eq:RedkToOne){reference-type="eqref" reference="eq:RedkToOne"}, and [\[eq:RedTwoToOne\]](#eq:RedTwoToOne){reference-type="eqref" reference="eq:RedTwoToOne"} may contain reducible representations as well (see e.g. the example in Section [\[sub:Reducible\]](#sub:Reducible){reference-type="ref" reference="sub:Reducible"}), but such are necessarily boundary-degenerate (see Proposition [\[prop:TotallyDegenerate\]](#prop:TotallyDegenerate){reference-type="ref" reference="prop:TotallyDegenerate"}). The preimage over a representation which is not boundary-nondegenerate is typically (although not always; see Remark [\[rm:Freedom\]](#rm:Freedom){reference-type="ref" reference="rm:Freedom"}) higher dimensional.
:::

::: remark
One could detect all representations (including all reducible ones) by performing a single barycentric subdivision [@GaroufalidisThurstonZickert]. The resulting variety, however, is not a topological invariant since each non-ideal vertex (generically) increases the dimension by one. The growth in the number of simplices and the expected dimension also makes computations infeasible. More importantly, invariants such as the loop invariant [@DG], important in quantum topology, are only defined when all vertices are ideal.
:::

::: remark
Our varieties are really schemes over $\mathbb Z$. They are typically not irreducible, and the coordinate rings may have nilpotents.
:::

## Definition and computation of the refined Ptolemy varieties - an overview {#sec:Algorithm}

We consider only $\overline P(\mathcal T)$ here. The modified variants are defined and computed in a similar way. As mentioned earlier, a decorated representation defines Ptolemy coordinates, and thus gives rise to a distinguished set of edges, namely those having Ptolemy coordinate zero. The idea is to consider all possible such sets. It turns out that they have to satisfy a transitivity property.

::: definition
A *transitive edge set* is a set $E$ of edges of $\mathcal T$ satisfying that if any two edges of a face are in $E$, so is the third. The edges in a transitive edge set are called *zero-edges*. We sometimes denote $E$ by $(\mathcal T,E)$ to stress the significance of the triangulation.
:::

There are always at least two transitive edge sets: the *non-degenerate* edge set with no zero-edges, and the *totally degenerate* edge set where all edges are zero-edges. In Section [\[sec:InvariantPtolemy\]](#sec:InvariantPtolemy){reference-type="ref" reference="sec:InvariantPtolemy"} we define for all transitive edge sets $E$ (except the totally degenerate one) a Ptolemy variety $P(\mathcal T,E)$, parametrizing decorated representations whose Ptolemy coordinates are zero exactly at the edges in $E$. The triangulation independent Ptolemy variety $\overline P(\mathcal T)$ is then defined as the union of all the $P(\mathcal T,E)$ (see Definition [\[def:InvariantPtolemy\]](#def:InvariantPtolemy){reference-type="ref" reference="def:InvariantPtolemy"}). For the non-degenerate edge set $P(\mathcal T,E)$ is simply $P(\mathcal T)$. If each face has at most one zero-edge (the *edge-degenerate* case; see Definition [\[def:PartitionType\]](#def:PartitionType){reference-type="ref" reference="def:PartitionType"}), $P(\mathcal T,E)$ is defined by the usual Ptolemy relations together with an *edge relation* [\[eq:EdgeRelations\]](#eq:EdgeRelations){reference-type="eqref" reference="eq:EdgeRelations"} for each zero-edge. If one or more faces consists entirely of zero-edges, one can reduce to the edge-degenerate case by considering an auxilary triangulation $\mathcal T'$ obtained from $\mathcal T$ by performing an explicit sequence of 2-3 moves.

### Algorithm

We describe an algorithm that is guaranteed to find all boundary-unipotent irreducible representations of a manifold, no matter what triangulation $\mathcal T_0$ is used as input. The steps involve triangulations obtained from $\mathcal T_0$ by performing 2-3 moves, but these are purely auxiliary.

A simplex is *degenerate* if all six edges are zero. A face is *degenerate* if all 3 edges are zero.

-   Compute all transitive edge sets $(\mathcal T_0,E_0)$ ignoring the totally degenerate one.

-   If $(\mathcal T,E)$ has a degenerate simplex, replace it by a descendant (Definition [\[def:Descendant\]](#def:Descendant){reference-type="ref" reference="def:Descendant"}) $(\mathcal T',E')$ after performing a 2-3 move at a face adjacent to a non-degenerate and a degenerate simplex. This procedure reduces the number of degenerate simplices by one. Repeat until all simplices are non-degenerate.

-   If $(\mathcal T,E)$ has a degenerate face, replace it by the set of descendants $(\mathcal T',E')$ where $\mathcal T'$ is the triangulation obtained from $\mathcal T$ by performing a 2-3 move on each degenerate face. No descendants have degenerate faces.

-   For each $(\mathcal T,E)$ from step 2 compute the primary decomposition of the reduced Ptolemy variety $P(\mathcal T,E)_{\mathop{\mathrm{red}}}$.

-   For each zero dimensional component of $P(\mathcal T,E)_{\mathop{\mathrm{red}}}$, compute the corresponding boundary-unipotent $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations via the Bruhat cocycle (Section [\[sec:BruhatCocycle\]](#sec:BruhatCocycle){reference-type="ref" reference="sec:BruhatCocycle"}). The output is a matrix of exact algebraic expressions for each generator of $\pi_1(M)$ in the face pairing presentation.

::: remark
If a Ptolemy variety contains a higher dimensional component $C$, one can compute the tautological representation $\pi_1(M)\to \mathop{\mathrm{SL}}(2,F(C))$, where $F(C)$ is the function field of $C$. See Section [\[sub:TautologicalRep\]](#sub:TautologicalRep){reference-type="ref" reference="sub:TautologicalRep"} for an example.
:::

::: remark
Among the 61911 manifolds in the SnapPy census `OrientableCuspedCensus` there is no manifold with more than 53 transitive edge sets (average 16). Most of these edge sets are only edge-degenerate (72%), so steps 1 and 2 above are rarely needed.
:::

::: remark
In case there are only two transitive edge sets it follows immediately from the definition that $\overline P(\mathcal T)=P(\mathcal T)$, so in this case the standard Ptolemy variety is guaranteed to detect all boundary-unipotent representations. Unfortunately, the only manifolds in the SnapPy census `OrientableCuspedCensus` with only two transitive edge sets are: `m003`, `m004`, `m015`, `m016`, `m017`, `m019`, `m118`, `m119`, `m180`, `m185`.
:::
