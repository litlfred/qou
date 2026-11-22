---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-007-segment-equations
section_title: "Segment equations"
section_number: null
pages: 8-9
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.889
latex_coverage_ratio: 0.981
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Segment equations label="sec:Segment equations"}

The segment parameters have a natural geometric interpretation: they parametrize the locations of the ideal vertices of the octahedral decomposition. Following [@McphailSnyder2024octahedralcoordinateswirtingerpresentation] we obtained the segment parameters from a shadow coloring but one can also work in the opposite direction. An assignment of numbers $b_{i}$ to the segments of $D$ induces a decorated representation of $K$ if and only if the shape parameters satisfy Thurston's gluing equations. These can be summarized in one equation for each segment.

::: definition
[]{#def:segment equations label="def:segment equations"} Choose a meridian eigenvalue $m \in \mathbb{C} \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}$. Assign a variable $b_{i} \in \mathbb{C} \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}$ to every segment of a cut presentation $D$ (with the variables of the boundary segments matching as usual). Use these to assign each corner of the diagram a shape parameter $z_{k}$ as in [\[eq:shape parameters\]](#eq:shape parameters){reference-type="ref" reference="eq:shape parameters"}; we assume that the $b_{i}$ are chosen so that no $z_{k}$ is $1$. Labeling a crossing of sign $\epsilon$ as in [\[eq:crossing
  labeled\]](#eq:crossing
  labeled){reference-type="eqref" reference="eq:crossing
  labeled"} the choice of $m$ and $b_{i}$ determine parameters $a_{i}$ for each segment by $$\label{eq:segment a vars}
    \begin{aligned}
      a_{1}
      &=
      m^{\epsilon}
      \frac{
        1 - z_{\lW}
      }{
        1 - z_{\lN}
      }
      &
      a_{4}
      &=
      m^{-\epsilon}
      \frac{
        1 - z_{\lE}
      }{
        1 - z_{\lN}
      }
      \\
      a_{2}
      &=
      m^{-\epsilon}
      \frac{
        1 - z_{\lS}
      }{
        1 - z_{\lW}
      }
      &
      a_{3}
      &=
      m^{\epsilon}
      \frac{
        1 - z_{\lS}
      }{
        1 - z_{\lE}
      }
    \end{aligned}$$ The construction above assigns every segment *two* parameters $a_{i}$ and $a_{i}'$ from the crossings at both ends. The say that these parameters agree for each segment.
:::

The segment equations were first studied by @arXiv:math/0009165 and are discussed in detail by @Kim2018. Our formulation follows the conventions of [@McphailSnyder2022hyperbolicstructureslinkcomplements; @McphailSnyder2024octahedralcoordinateswirtingerpresentation].

::: proposition
[]{#thm:segment solutions are reps label="thm:segment solutions are reps"} For an open knot diagram $D$ there is a bijection between the sets of

::: thmenum
solutions of the segment equations of $D$ with meridian eigenvalue $m$

shadow-colored decorated representations $(\rho, u)$ with meridian eigenvalue $m$ that are not $D$-pinched
:::
:::

::: proof
*Proof.* Suppose we have a solution of the segment equations with meridian eigenvalue $m$. Then by definition there is a well-defined assignment of parameters $a_{i}$ to the segments of $D$ that give a non-pinched of $D$ in the sense of [@McphailSnyder2022hyperbolicstructureslinkcomplements]. Call the set of such colorings $Y$. A point of $Y$ gives a solution of the segment equations (by forgetting the $a_{i}$) so there is a bijection between set (a) and $Y$. [@McphailSnyder2024octahedralcoordinateswirtingerpresentation Theorem 2.11 and Theorem 1] establish a bijection between $Y$ and the set (b). ◻
:::
