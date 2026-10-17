---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble"
section_id: sec-003-22-algebra-of-generating-functionals
section_title: "Algebra of generating functionals."
section_number: 2.2
pages: 4-5
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical canonical ensemble is"
---
For any function $\psi\in C_0(\Gamma_0)$ define *generating functional* : $$\begin{aligned}
\label{GFf}
\widetilde{F}_\psi(j)&\;=\;\sum_{N=0}^{\infty}\frac{1}{N!}\int_{\Bbb R^{dN}}(dx)^{N}j(x_1)\cdots j(x_N)\psi(x_1,\ldots, x_N)=\notag \\
&\;=\;\int_{\Gamma_0}e(j;\gamma)\psi(\gamma)\lambda_\sigma(d\gamma),
\end{aligned}$$ where functional $e(j;\gamma)$ is defined by the formula $$\begin{aligned}
\label{I-lam4}
e(j;\gamma):=\;&\begin{cases}
 1,\;&\gamma=\emptyset,\\
  \prod_{x\in\gamma}j(x),
\;&\gamma\in\Gamma_0\setminus\{\emptyset\},
  \end{cases}
\end{aligned}$$

and $j\in C_0(\Bbb R^d)$ is bounded (take for simplicity $j\leq 1$), continuum, nonnegative function.

It is easy to calculate using the lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} that $$\label{odprod}
  \widetilde{F}_{\psi_1}(j)\widetilde{F}_{\psi_2}(j)\;=\;\widetilde{F}_{\psi_1*\psi_2}(j)=\int_{\Gamma_0}e(j;\gamma)(\psi_1*\psi_2)(\gamma)\lambda_\sigma(d\gamma),$$ where $\psi_1*\psi_2$ is product $\psi_1$ and $\psi_2$ in commutative algebra $\mathcal{A}$, which was introduced by Ruelle (see [@Ru69], Ch. 4). Formula [\[odprod\]](#odprod){reference-type="eqref" reference="odprod"} establishes an unambiguous correspondence between the algebra of generating functionals with operation of ordinary multiplication and the algebra $\mathcal {A}$. Recall that for $\gamma=\{x_1, x_2, ... x_n\}$ $$\label{odprodRu}
(\psi_1*\psi_2)(\gamma)= \sum_{\xi\subseteq\gamma}\psi_{1}(\xi)\psi_{2}(\gamma\setminus\xi).$$
