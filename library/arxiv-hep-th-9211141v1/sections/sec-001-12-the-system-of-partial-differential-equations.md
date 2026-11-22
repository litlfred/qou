---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-001-12-the-system-of-partial-differential-equations
section_title: "The System of Partial Differential Equations"
section_number: 1.2
pages: 4-5
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.881
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsec:sum_pde label="subsec:sum_pde"} We set $$J=\bigcup_{j=1}^m\left(a_{2j-1},a_{2j}\right)$$ and write $D(J;\lambda)$ for the Fredholm determinant of $K$ acting on $J$. We think of this as a function of $a=(a_1,\ldots,a_{2m})$. Then $$d_a \log D(J;\lambda) = - \sum_{j=1}^{2m} (-1)^j R(a_j,a_j)\, da_j
\label{dlog_tau}$$ where $R(x,y)$ is the kernel of the operator $K(I-K)^{-1}$ and $d_a$ denotes exterior differentiation with respect to the $a_j$'s. We introduce quantities $$q_j=(I-K)^{-1} A(a_j)\, , \ \ p_j=(I-K)^{-1} A^\prime(a_j)\, ,
\label{qp_defn}$$ (which are the analogue of the quantities $r_{\pm j}$ of [@jmms]; see also [@dyson92; @its90; @mehta92b; @mehta_mahoux]) as well as two further quantities $$u=\left(A,(I-K)^{-1}A\right)\, , \ \ v=\left(A,(I-K)^{-1}A^\prime\right)
\label{uv_defn}$$ where the inner products refer to the domain $J$. Then the equations read $$\begin{aligned}
{\partial q_j\over\partial a_k}&=& (-1)^k\,  {q_j p_k - p_j q_k\over
a_j-a_k}\, q_k\,\ \ \ (j\neq k), \label{airy_1}  \\
{\partial p_j\over\partial a_k}&=& (-1)^k\,  {q_j p_k - p_j q_k\over
a_j-a_k}\, p_k \ \ \  (j\neq k), \label{airy_2} \\
{\partial q_j\over\partial a_j}&=&
-\sum_{k\neq j} (-1)^k\,  {q_j p_k - p_j q_k \over a_j - a_k}\, q_k
+p_j - q_j u\, ,\label{airy_3} \\
{\partial p_j\over\partial a_j}&=&
-\sum_{k\neq j} (-1)^k\,  {q_j p_k - p_j q_k \over a_j - a_k}\, p_k
+a_j q_j + p_j u-2 q_j v\, , \label{airy_4} \\
{\partial u\over\partial  a_j}&=&(-1)^j q_j^2\, , \label{airy_5}  \\
{\partial v\over\partial  a_j}&=& (-1)^j p_j q_j \, . \label{airy_6}
\end{aligned}$$ Moreover the quantities $R(a_j,a_j)$ appearing in ([\[dlog_tau\]](#dlog_tau){reference-type="ref" reference="dlog_tau"}) are given by $$R(a_j,a_j)=\sum_{k\neq j}(-1)^k\,  {(q_j p_k - p_j q_k)^2\over a_j - a_k} \,
+ p_j^2 - a_j q_j^2 - 2 p_j q_j u + 2 q_j^2 v \, .\label{airy_7}$$ These equations are derived very much in the spirit of [@tw1]; see also [@dyson92; @its90; @mehta92b].
