---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.904
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
[]{#sect:intro label="sect:intro"}

It follows from its very definition that the category $\operatorname{Rep}H$ of finite-dimensional representations of a Hopf algebra $H$ is a tensor category. There is a less obvious way to go from Hopf algebras with some extra structure (called spherical Hopf algebras) to tensor categories. Spherical Hopf algebras and the procedure to obtain a tensor category from them were introduced by Barrett and Westbury [@BaW-adv; @BaW-tams], inspired by previous work by Reshetikhin and Turaev [@RT-cmp; @RT-inv], in turn motivated to give a mathematical foundation to the work of Witten [@Wi]. A spherical Hopf algebra has by definition a group-like element that implements the square of the antipode (called a pivot) and satisfies the left-right trace symmetry condition [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"}. The classification (or even the characterization) of spherical Hopf algebras is far from being understood, but there are two classes to start with. Let us first observe that semisimple spherical Hopf algebras are excluded from our considerations, since the tensor categories arising from the procedure are identical to the categories of representations. Another remark: any Hopf algebra is embedded in a pivotal one, so that the trace condition [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} is really the crucial point. Now the two classes we mean are

-   Hopf algebras with involutory pivot, or what is more or less the same, with ${\mathcal S}^4 = \operatorname{id}$. Here the trace condition follows for free, and the quantum dimensions will be (positive and negative) integers.

-   Ribbon Hopf algebras [@RT-cmp; @RT-inv].

It is easy to characterize pointed or copointed Hopf algebras with ${\mathcal S}^4 = \operatorname{id}$; so we have many examples of (pointed or copointed) spherical Hopf algebras with involutory pivot, most of them not even quasi-triangular, see Section [\[sec:inv-pivot\]](#sec:inv-pivot){reference-type="ref" reference="sec:inv-pivot"}. On the other hand, any quasitriangular Hopf algebra is embedded in a ribbon one [@RT-cmp]; combined with the construction of the Drinfeld double, we see that any finite-dimensional Hopf algebra gives rise to a ribbon one. So, we have plenty of examples of spherical Hopf algebras.

The procedure to get a tensor category from a spherical Hopf algebra $H$ consists in taking a suitable quotient $\operatorname{\underline{Rep}}H$ of the category $\operatorname{Rep}H$. This appears in [@BaW-adv] but similar ideas can be found elsewhere, see e. g. [@GK-inv; @Kn]. The resulting spherical categories are semisimple but seldom have a finite number of irreducibles, that is, they are seldom fusion categories in the sense of [@ENO]. We are interested in describing fusion tensor subcategories of $\operatorname{\underline{Rep}}H$ for suitable $H$. This turns out to be a tricky problem. First, if the pivot is involutive, then the fusion subcategories of $\operatorname{\underline{Rep}}H$ are integral, see Proposition [\[prop:spherical-involutory\]](#prop:spherical-involutory){reference-type="ref" reference="prop:spherical-involutory"}. The only way we know is through tilting modules; but it seems to us that there is no general method, just a clever recipe that works. This procedure has a significant outcome in the case of quantum groups at roots of one, where the celebrated Verlinde categories are obtained [@AP]; see also [@Sa] for a self-contained exposition and [@Mat] for similar results in the setting of algebraic groups over fields of positive characteristic. One should also mention that the Verlinde categories can be also constructed from vertex operator algebras related to affine Kac-moody algebras, see [@BK; @Hu; @HuL; @KaLu] and references therein; the comparison of these two approaches is highly non-trivial. Another approach, at least for $SL(n)$, was proposed in [@hayashi] via face algebras (a notion predecessor of weak Hopf algebras).

The paper is organized as follows. Section [\[sec:preliminaries\]](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"} contains some information about the structure of Hopf algebras and notation used later in the paper. Section [\[sec:sph-hopf\]](#sec:sph-hopf){reference-type="ref" reference="sec:sph-hopf"} is devoted to spherical Hopf algebras. In Section [\[sec:titling2\]](#sec:titling2){reference-type="ref" reference="sec:titling2"} we discuss tilting modules and how this recipe would work for some finite-dimensional pointed Hopf algebras associated to Nichols algebras of diagonal type, that might be thought of as generalizations of the small quantum groups of Lusztig.
