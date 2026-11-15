---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-012-vertex-operators
section_title: "Vertex Operators"
section_number: null
pages: 16-17
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
In string theory, correlation functions on a genus $g$ world-sheet at instanton degree $d$ scale as $g_s^{2g-2+k}$, where $k$ is the number of insertions on the world-sheet. The genus expansion is canonically written as a sum over all world-sheet topologies weighted by a factor $g_s^{2g-2}$. The remaining factor $g_s^k$ is relegated to the normalization of vertex operators: each one comes with a single factor of the string coupling $g_s$. In Hurwitz theory, the insertion of a conjugacy class $C_{\alpha}$ in the target space corresponds to the insertion of $\ell(\alpha)$ marked points on the worldsheet. Therefore, each such insertion must be weighted by an additional factor $g_s^{\ell(\alpha)}$, and this is indeed what we find. The physical interpretation of this finding is straightforward. By lore, single cycles correspond to single string states, and come with a single factor $g_s$.[^1] Accordingly, multi-cycles correspond to multi-string states and the length of a conjugacy class counts the number of strings in the state defined by this conjugacy class.

This state of affairs is complicated by the presence of the coefficients $p_{\alpha}(U)$, which also scale with $N$. Consider an element $U$ of the unitary group $U(N)$ that acts non-trivially on a $p$-dimensional space, with $p\ll N$. Then, $$p_{\alpha}(U)=N^{\ell(\alpha_i)} \prod_i \left(1-\frac{\Tr_p (U\rvert_p)^{\alpha_i}}{N}\right)\, ,$$ where $U\rvert_p$ denotes the restriction of the element $U$ to its non-trivial subspace, and $\Tr_p$ the trace on this subspace.

In other words, $p_{\alpha}(U)$ scales as $g_s^{-\ell(\alpha)}$, up to corrections in $g_s$. Thus, the dominant part of the correlator on a surface of genus $g$ scales as $g_s^{2g-2}$, as expected from a Yang-Mills partition function. The identification of the correlation functions of both theories necessitates that we insert rescaled vertex operators on the string theory side. The dictionary of observables at order $d$ reads $$U \to g_s^{-d} \left( C_e + \mathcal{O}(g_s) \right)\, .$$

Before we move on the implementation of the deformations, we remark that in going from a field theory to a string theory correlation function in equation [\[FieldToString\]](#FieldToString){reference-type="eqref" reference="FieldToString"}, we have dismantled the operator algebra structure of the observables. Indeed, in the field theory, $$\langle C_{\alpha}, C_{\beta}\rangle_d = c_{\alpha \beta}^{\ \ \gamma} \langle C_{\gamma}\rangle_d\, ,$$ where the $c_{\alpha\beta}^{\ \ \gamma}$ are the structure constants of the conjugacy class algebra $\mathcal{C}_d$. In the string theory, this equation no longer holds, because the Riemann-Hurwitz formula is not preserved by the product of the algebra, which implies that the value of the genus for which $\langle C_{\gamma} \rangle_{g,d}$ is non-zero depends on $\gamma$.

The break-down of the algebra is crucial for dealing with the deformations, as we explain momentarily.[^2]

Finally, we stress that in order to simplify notations, we systematically write $$\langle C_{\alpha} C_{\beta}\rangle_{g,d}\, ,$$ in order to refer to the correlation function $$\langle C_{\alpha}, C_{\beta}\rangle_{g,d}\, .$$ In this paper, expressions involving products of correlators should always be understood as the insertion of two separate observables.

[^1]: It was noted in [@Lerche:2023wkj; @Benizri:2024mpx], based on [@OP1], that there are interesting corrections to this lore. We discuss this aspect further in section [\[DeformedGW\]](#DeformedGW){reference-type="ref" reference="DeformedGW"}.

[^2]: An interesting observation is that the product of the filtered Hurwitz theory -- see e.g. [@Li:2020zwo] -- does preserve the Riemann-Hurwitz formula.
