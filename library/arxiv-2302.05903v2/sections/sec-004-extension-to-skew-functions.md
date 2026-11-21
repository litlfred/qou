---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-004-extension-to-skew-functions
section_title: "Extension to skew functions"
section_number: null
pages: 5-6
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.985
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Now, one can easily obtain similar formulas for sums of the skew Schur functions $S_{R/P}$. To this end, one needs a slight generalization of the Cauchy identity ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}): $$\begin{aligned}
\label{C2}
\sum_R S_{R/P}\{p\}S_{R}\{\bar p\}=\exp\left(\sum_{k=1}^\infty{p_k\bar p_k\over k}\right)S_{P}\{\bar p\}
\end{aligned}$$ Taking the average of this identity over $\bar p_k$ with measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}), one obtains $$\begin{aligned}
\label{av}
\sum_R S_{R/P}\{p\}\Big<S_{R}\{\bar p\}\Big>^{\bf\!A}_{\bar p}=\sum_R S_{R/P}\{p\}=
\left<\exp\left(\sum_{k=1}^\infty{p_k\bar p_k\over k}\right)S_{P}\{\bar p\}\right>^{\bf\!A}_{\bar p}
\end{aligned}$$ Let us prove that the r.h.s. of this formula is given by $$\begin{aligned}
\label{pr}
\left<\exp\left(\sum_{k=1}^\infty{p_k\bar p_k\over k}\right)S_{P}\{\bar p\}\right>^{\bf \!A}_{\!\!\bar p}=
\exp\left\{\sum_{k=1}^\infty \left(\frac{p_k^2}{2k}+ \frac{p_{2k-1}}{2k-1}\right)\right\}\sum_QS_{P/Q}\{p\}
\end{aligned}$$ with literally the same $p$-dependent factor as in ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}). To this end, we convert this formula with the Schur functions $S_P\{p'\}$. This gives $$\begin{aligned}
\left<\exp\left(\sum_{k=1}^\infty{(p_k+p'_k)\bar p_k\over k}\right)\right>^{\bf\!A}_{\!\!\bar p}=
\exp\left\{\sum_{k=1}^\infty \left(\frac{p_k^2}{2k}+ \frac{p_{2k-1}}{2k-1}+{p_kp'_k\over k}\right)\right\}\sum_QS_Q\{p'\}
\end{aligned}$$ where we once again used the Cauchy identities ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}) and ([\[C2\]](#C2){reference-type="ref" reference="C2"}) at the l.h.s. and at the r.h.s. Now it remains to calculate the Gaussian integral at the l.h.s. as it was done in ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}), and also to use ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}) to evaluate the sum at the r.h.s. Hence, formula ([\[pr\]](#pr){reference-type="ref" reference="pr"}) is correct, and we finally obtain from ([\[av\]](#av){reference-type="ref" reference="av"}) $$\begin{aligned}
\label{sS}
\sum_R S_{R/P}\{p\}=\exp\left\{\sum_{k=1}^\infty \left(\frac{p_k^2}{2k}+ \frac{p_{2k-1}}{2k-1}\right)\right\}\sum_QS_{P/Q}\{p\}
\end{aligned}$$ We can now make one more check that ([\[sS\]](#sS){reference-type="ref" reference="sS"}) is correct. Convert this formula with $S_P\{p'\}$ and use the Cauchy identity ([\[C2\]](#C2){reference-type="ref" reference="C2"}) and the definition of the skew Schur polynomial $$\begin{aligned}
S_R\{p+p'\}=\sum_PS_{R/P}\{p\}S_P\{p'\}
\end{aligned}$$ Then $$\begin{aligned}
\sum_RS_R\{p+p'\}=\exp\left\{\sum_{k=1}^\infty \left(\frac{p_k^2}{2k}+ \frac{p_{2k-1}}{2k-1}+{p_kp'_k\over k}\right)\right\}
\sum_QS_Q\{p\}
\end{aligned}$$ Both sums can be calculated using ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}) in order to validate this formula. We emphasize once again that, according to this argument, the $p$-dependent factor at the r.h.s. is literally the same as in ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}), and the same will be true for the skew Schur counterparts of all other identities in this section.
