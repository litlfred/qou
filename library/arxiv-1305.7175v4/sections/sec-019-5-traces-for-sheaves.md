---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-019-5-traces-for-sheaves
section_title: "Traces for sheaves"
section_number: 5
pages: 29-30
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.911
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
[]{#sect shvs label="sect shvs"}

In this section, we spell out how to apply the abstract formalism of traces of Section [\[sect cat\]](#sect cat){reference-type="ref" reference="sect cat"} and its geometric incarnation of Section [\[sect geom\]](#sect geom){reference-type="ref" reference="sect geom"} to categories of sheaves. Recall Definition [\[sheaf def intro\]](#sheaf def intro){reference-type="ref" reference="sheaf def intro"}:

::: defn
A *sheaf theory* is a symmetric monoidal functor of $(\infty,2)$-categories $$\xymatrix{
\ul{\cS}:\ul{Corr}_k^{prop}\ar[r] &  \ul{dgCat}_k
}$$ from correspondences of stacks (with 2-morphisms given by proper maps of correspondences) to dg categories. We denote by $$\xymatrix{
\cS:Corr_k\ar[r] &  dgCat_k
}$$ the underlying 1-categorical sheaf theory, i.e. the symmetric monoidal functor on $(\infty,1)$-categories obtained by forgetting noninvertible morphisms.
:::

Applying a sheaf theory to the geometric descriptions of traces of correspondences, one immediately deduces trace formulas for dg categories. We first spell out the consequences of the 1-categorial structure of a sheaf theory $\cS$, then the trace formulae arising from its 2-categorical enhancement $\uS$, and finally in Section [\[actual sheaf theory\]](#actual sheaf theory){reference-type="ref" reference="actual sheaf theory"} explain how to use the results of [@finiteness; @GR] to deduce applications of this formalism.
