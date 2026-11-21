---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-009-22-path-integral-formalism
section_title: "Path-integral formalism"
section_number: 2.2
pages: 16-17
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
There are two main approaches to the non-Abelian Stokes theorem in the framework of the path-integral formalism: coherent-state approach and holomorphic approach. In the literature, the both approaches occur in few, a bit different, incarnations. Also, the both have found applications in different areas of mathematical and/or theoretical physics, and therefore the both are usefull. The first one is formulated more in the spirit of group theory, whereas the second one follows from traditional path-integral formulation of quantum mechanics or rather quantum field theory. Similarly to the situation in quantum theory, the path-integral formalism is easier in some applications and more intuitive then the operator formalism but traditionally it is mathematically less rigorous. In the same manner as quantum mechanics, initially formulated in the operator language and next reformulated into the path-integral one, we can translate the operator form of the non-Abelian Stokes theorem into the path-integral one.

In order to formulate the non-Abelian Stokes theorem in the path-integral language we will make the following three steps:

1.  We will determine a coherent-state/holomorphic path-integral representation for the parallel-transport operator deriving an appropriate transition amplitude (a path-integral counterpart of the LHS in Eq.[\[op.NAST\]](#op.NAST){reference-type="ref" reference="op.NAST"});

2.  For a closed curve $C$ we will calculate the trace of the path-integral form of the parallel-transport operator, quantum theory in an external gauge field $A$;

3.  We will apply the Abelian Stokes theorem to the exponent of the integrand of the path integral yielding the RHS of the non-Abelian Stokes theorem (a counterpart of RHS in Eq. 2.8).

#### Preliminary formulas

Since the both path-integral derivations of the transition amplitude have a common starting point that is independent of the particular approach, we present it here: $${\rm P}\exp\left[i\int_{t'}^{t''}A(t)dt\right]=
    \lim_{N\rightarrow\infty}\prod_{n=1}^{N}
    \left(1+i\epsilon A_n\right),
    \label{prel.form.}$$ where $$A_n=A(t_n),\qquad
    \epsilon=\frac{t''-t'}{N},\qquad
    t_n=n\epsilon+t',\qquad
    t_N=t'',\quad t_0=t'.
    \nonumber$$ From this moment the both approaches differ.
