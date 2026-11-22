---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-013-34-conventional-multimatrix-models
section_title: "Conventional Multimatrix models"
section_number: 3.4
pages: 52-53
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.955
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
The multimatrix integrals of the form
\be
Z_N\{t^{(\alpha)}\} \equiv \nn \\
\equiv c_N^{p-1}\int_{N\times N} dH^{(1)}...dH^{(p-1)}
\prod_{\alpha = 1}^{p-1} e^{\sum_{k=0}^{\infty}t_k^{(\alpha)}{\rm Tr}
H_{(\alpha)}^k} \prod_{\alpha = 1}^{p-2} e^{{\rm
Tr}H^{(\alpha)}H^{(\alpha+1)}}
\label{mumamo'}
\ee
can be rewritten in the eigenvalue form using the same Itzykson-Zuber formula
(\ref{IZ}). Indeed, substituting
$H^{(\alpha)} = \left.U^{(\alpha)}\right.^{\dagger}D^{(\alpha)} U^{\alpha)}$
and then defyining $U^{(\alpha)}\left.U^{(\alpha+1)}\right.^{\dagger}
\equiv \tilde U^{(\alpha)}$, we
obtain:
\be
\new
\begin{array}{c}
Z_N\{t^{(\alpha)}\} =\\
= \frac{1}{N!} \prod_{\alpha = 1}^{p-1}
\prod_{i=1}^N \int dh_i^{(\alpha)} e^{-V(h_i^{(\alpha)})}
\Delta^2(h^{(\alpha)})
\prod_{\alpha = 1}^{p-2} I_N\{H^{(\alpha)}, H^{(\alpha+1)}\} =  \\
= \frac{1}{N!} \prod_{\alpha = 1}^{p-1}
\prod_{i=1}^N \int dh_i^{(\alpha)} e^{-V(h_i^{(\alpha)})}
\prod_{\alpha = 1}^{p-2} e^{h_i^{(\alpha)}h_i^{(\alpha+1)}}
\Delta(h^{(1)})\Delta(h^{(2)}),
\end{array}
\label{mumamoev}
\ee
where the same trick is done with the substitution of
$\frac{1}{N!} {\rm det}_{ij} e^{h_i^{(\alpha)}h_j^{(\alpha+1)}}$ for
$e^{\sum_{i=1}^N h_i^{(\alpha)}h_i^{(\alpha+1)}}$ under the sign of the
$h_i^{(\alpha)}$-integration  (step by step: first - for $\alpha = 1$,
then for $\alpha = 2$ and so on). Note that all the Van-der-Monde determinants
disappeared from the final formula at the r.h.s. of eq.(\ref{mumamoev}), except
for those at the ends of the matrix chain (at $\alpha = 1$ and $\alpha =
p-1$).

If the chain was closed rather than open, i.e. there was an additional factor
of $e^{{\rm Tr}H^{(p-1)}H^{(1)}}$ under the integral in (\ref{mumamo'}),
then the trick with separation of all angular-variable (unitary-matrix)
integrations would not work so simply: in addition to the Itzykson-Zuber
integral the much more involved quantities would be required, like
\be
\new
\begin{array}{c}
I_n\{X_1,X_2; L\} \equiv  \\
\equiv c_n \int_{n\times n}
\frac{[dU_1]}{[dU_{1,Cartan}]}  \frac{[dU_2]}{[dU_{2,Cartan}]}
\\ \cdot
\exp\left({{\rm tr} X_1U_1 L U_1^{\dagger} + {\rm tr} X_2U_2 L U_2^{\dagger}
+ {\rm tr}X_1(U_1U_2^{\dagger})X_2(U_2U_1^{\dagger})}\right)
\end{array}
\ee
This (so far unresolved) closed chain model (lattice Potts model) is an
example of non-eigenvalue models, in the $p=\infty$ case it turns into
"compactified" $c=1$ model. This theory is $more$ complicated then the
so far simplest class of non-eigenvalue models of "induces Yang-Mills theory",
known as Kazakov-Migdal models.
