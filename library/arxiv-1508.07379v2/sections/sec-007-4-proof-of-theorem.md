---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity"
section_id: sec-007-4-proof-of-theorem
section_title: "Proof of Theorem ??"
section_number: 4
pages: 12-13
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity — We establish new lower bounds for the convergence radius of the Mayer series and the Virial series of a continuous"
---
To deduce Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} from Proposition [\[pro1\]](#pro1){reference-type="ref" reference="pro1"} we just need to show the following easy lemma.

::: lem
[]{#le3 label="le3"} For any $\t\in T_n$ it holds $$\int_{\L}dx_1\dots \int_{\L}dx_{n} \prod_{\{i,j\}\in E_{\t}}
\left(1-e^{-\b |V(x_i-x_j)|}\right)\le
|\L|\left[\hat C(\b)\right]^{n-1}$$
:::

\
**Proof**. Without loss of generality we can always assume (eventually through a renomination of the indices in the integral of the l.h.s. of equation above) that $E_{\t}~=~\{2,j_2\},\{3,j_3\},\dots \{n,j_{n}\}$ with $j_k<k$ for all $k=2,\dots, n$, so that $$\int_{\L}dx_1\dots \int_{\L}dx_{n} \prod_{\{i,j\}\in E_{\t}}
\left( 1- e^{ -\b |V(x_i -x_j)|}\right)~
=~
\int_{\L}dx_1\dots \int_{\L}dx_{n} \prod_{k=2}^{n}
\left(1-e^{ -\b |V(x_{k} -x_{j_k})|}\right )$$

\
Define the following change of variables $(x_1,\dots,x_n) \to (y_1,\dots, y_n)$ in the integral []{#change label="change"} y_1 =x_1,     y\_k= x\_k-x\_j_k,       k =2,...,n The Jacobian matrix of such transformation ([\[change\]](#change){reference-type="ref" reference="change"}), being lower triangular with entries of the diagonal all equal to one, has determinant equal to one. Therefore we have $$\int_{\L}dx_1\dots\int_{\L}dx_{n} \prod_{k~=~1}^{n-1} \left(1-e^{ -\b |V(x_{i_k} -x_{j_k})|}\right ) ~\le$$ $$\le~
\int_{\L}dy_1\int_{\mathbb{R}^3}dy_2\dots
\int_{\mathbb{R}^3}dy_{n}
 \prod_{j=2}^{n}
\left( 1- e^{ -\b |V(y_j)|}\right )~=$$ $$=~
|\L|\left[\int_{\mathbb{R}^3}(1-   e^{ -\b |V(x)|})dx\right]^{n-1}~= |\L|\left[\hat C(\b)\right]^{n-1}$$ $\Box$

\
Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"} follows now straightforwardly. Indeed, from Proposition [\[pro1\]](#pro1){reference-type="ref" reference="pro1"} and Lemma [\[le3\]](#le3){reference-type="ref" reference="le3"} we get the following bound for the absolute value of the Mayer coefficient $C_n(\b,\L)$. $$|C_n(\b,\L)|~\le ~{1\over |\L|}{1\over n!}\int_{\L}\,dx_1
\dots \int_{\L} dx_n\: \left|\sum\limits_{g\in {\mathcal G}_{n}}
\prod\limits_{\{i,j\}\in E_g}\left[  e^{ -\b V(x_i-x_j)|} -1\right]\right|\le$$ $$~~~~~~~~~~~~~~\le ~{e^{\b Bn}\over |\L|}{1\over n!}\int_{\L}\,dx_1
\dots \int_{\L} dx_n\: \sum_{\tau \in {\mathcal T}_n} \prod_{\{i,j\} \in E_\tau} (1-e^{-\b| V(x_i-x_j)|}) =$$ $$~~~~~~~~~~~~~~= ~{e^{\b Bn}\over |\L|}{1\over n!}\sum_{\tau \in {\mathcal T}_n}\int_{\L}\,dx_1
\dots \int_{\L} dx_n\:  \prod_{\{i,j\} \in E_\tau} (1-e^{-\b| V(x_i-x_j)|}) \le$$ $$~~~~~~\le ~{e^{\b Bn}}{1\over n!}\left[\hat C(\b)\right]^{n-1} \sum_{\tau \in {\mathcal T}_n} 1~ =~{e^{\b Bn}}{n^{n-2}\over n!}\left[\hat C(\b)\right]^{n-1}
~$$ where in the last line we have also used the Cayley formula $\sum_{\tau \in {\mathcal T}_n} 1=|\mathcal T_n|=n^{n-2}$ (see [@Ca]).

This concludes the proof of Theorem [\[teo1\]](#teo1){reference-type="ref" reference="teo1"}.
