---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-004-31-the-proof-of-theorem-31
section_title: "The proof of Theorem 3.1"
section_number: 3.1
pages: 7-8
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
Apply [\[usemn3\]](#usemn3){reference-type="eqref" reference="usemn3"} and Corollary [\[centralizer2\]](#centralizer2){reference-type="ref" reference="centralizer2"}: With $\rho$ and $\nu$ denoting partitions of $k$ and $\mu$ partitions of $n$ we have $$\left[\chi^\rho_\nu\right]\left[ \psi_{\rho,n}(\mu)\right]
=\left[\sum_{\lambda\vdash n}\chi^\lambda _{(n-k,\nu)}\cdot\chi^\lambda_\mu \right]
=\left[\begin{cases}|Z_{S_k}(\nu)|\cdot(n-k) & if ~\bar\mu=\nu
\\
0 & if~ \bar\mu\ne \nu.\\
\end{cases}
\right]=$$ $$\begin{aligned}
\label{usemn31}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=\left[\begin{cases}|Z_{S_k}(\nu)| & if ~\bar\mu=\nu
\\
0 & if~ \bar\mu\ne \nu.\\
\end{cases}
\right]\cdot(n-k)
\end{aligned}$$ Restrict now to partitions $\mu=(n-k,\bar\mu)$ (so $\mu$ is given by $\bar\mu$), then [\[usemn31\]](#usemn31){reference-type="eqref" reference="usemn31"} becomes

$$\left[\chi^\rho_\nu\right]\left[ \psi_{\rho,n}(n-k,\bar\mu)\right]
=\left[\sum_{\lambda\vdash n}\chi^\lambda _{(n-k,\nu)}\cdot\chi^\lambda_{(n-k,\bar\mu)} \right]
=\left[\begin{cases}|Z_{S_k}(\nu)|\cdot(n-k) & if ~\bar\mu=\nu
\\
0 & if~ \bar\mu\ne \nu.\\
\end{cases}
\right]=$$

$$\begin{aligned}
\label{usemn311}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=\left[\begin{cases}|Z_{S_k}(\nu)| & if ~\bar\mu=\nu
\\
0 & if~ \bar\mu\ne \nu\\
\end{cases}
\right]\cdot(n-k).
\end{aligned}$$

Note that each side of [\[usemn311\]](#usemn311){reference-type="eqref" reference="usemn311"} is a column of height $d=|\{Par(k)\}|$, parametrized by the partitions $\bar\mu\in Par(k)$. Thus, if $\nu=\bar\mu^{(j)}$ is the $j$th element in $Par(k)$ then the transpose of the corresponding column of [\[usemn311\]](#usemn311){reference-type="eqref" reference="usemn311"} is $$(0,\ldots,0,|Z_{S_k}(\bar\mu^{(j)})|,0,\ldots,0)\cdot (n-k).$$ The columns $\left[ \psi_{\rho,n}(n-k,\bar\mu)\right]$ of height $d$ is parametrized by $\rho\in Par(k)$, with $\bar\mu$ fixed. From these columns we form the $d\times d$ matrix $$M=\left[ \psi_{\rho,n}(n-k,\bar\mu^{(1)}),\psi_{\rho,n}(n-k,\bar\mu^{(2)}),\ldots,
 \psi_{\rho,n}(n-k,\bar\mu^{(d)})\right].$$ Also denote $K=\left[\chi^\rho_\nu\right]$ and $D=diag( |Z_{S_k}(\bar\mu^{(1)})|,\ldots,|Z_{S_k}(\bar\mu^{(d)})| )$. By [\[usemn311\]](#usemn311){reference-type="eqref" reference="usemn311"} we get $$\left[\chi^\rho_\nu\right] M=KM=D\cdot(n-k)
=diag( |Z_{S_k}(\bar\mu^{(1)})|,\ldots,|Z_{S_k}(\bar\mu^{(d)})| )\cdot(n-k),$$ and by [\[columns2\]](#columns2){reference-type="eqref" reference="columns2"} $$KK^T=D=diag( |Z_{S_k}(\bar\mu^{(1)})|,\ldots,|Z_{S_k}(\bar\mu^{(d)})| ).$$

Thus we have $KM=KK^T\cdot(n-k).$

Note that $K$ is the character table of $S_k$, hence is invertible. Left cancelation of $K$ implies that $M=K^T\cdot (n-k)$, so $M$ = (the character table of $S_k)\cdot(n-k)$. This completes the proof of Theorem [\[v4\]](#v4){reference-type="ref" reference="v4"}.
