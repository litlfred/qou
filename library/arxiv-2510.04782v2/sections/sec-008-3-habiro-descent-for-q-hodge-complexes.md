---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-008-3-habiro-descent-for-q-hodge-complexes
section_title: "Habiro descent for q-Hodge complexes"
section_number: 3
pages: 20-20
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.981
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#sec:HabiroDescent label="sec:HabiroDescent"}

In this section, we'll show that in those situations where a well-behaved derived $q$-Hodge complex can be defined, it descends automatically to the Habiro ring, and furthermore a derived analogue of the comparison with $q$-de Rham--Witt complexes holds true.

Throughout this section, we fix a perfectly covered $\Lambda$-ring $A$.

::: numpar
[]{#conv:QuotientConvention label="conv:QuotientConvention"} In the following we'll consider filtered modules over the filtered ring $(q^m-1)^\star A[q]$ for various $m$. For such a filtered module $\fil^\star M$, we always let $\fil^\star M/(q^m-1)$ denote the base change $$\fil^\star M/(q^m-1)\coloneqq \fil^\star M\lotimes_{(q^m-1)^\star A[q]}A$$ in filtered objects, or in other words, the quotient by $(q^m-1)$ sitting in filtration degree $1$, not filtration degree $0$. In particular, the $n$^th^ filtered piece of the quotient $\fil^\star M/(q^m-1)$ will be $$\cofib\left((q^m-1)\colon \fil^{n-1}M\longrightarrow \fil^nM\right)\,.$$
:::
