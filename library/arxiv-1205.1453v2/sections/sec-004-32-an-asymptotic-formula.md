---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series"
section_id: sec-004-32-an-asymptotic-formula
section_title: "An asymptotic formula"
section_number: 3.2
pages: 9-10
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.974
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series — We show an asymptotic formula of the divergent bilateral basic hypergeometric series 1ψ0(a; −; q, ·) with using the"
---
In this section, we show an asymptotic formula of [\[b2so\]](#b2so){reference-type="eqref" reference="b2so"} with using the $q$-Borel-Laplace transformations of the first kind. We show the following theorem.

::: thm
[]{#teiri1 label="teiri1"}For any $x\in\mathbb{C}^*\setminus [-\lambda ;q]$, we have $$\hat{{}_1\psi_0}(a;-;\lambda ;q,x)=\frac{(q;q)_\infty}{\left(q/a;q\right)_\infty}\frac{\theta (aq\lambda )}{\theta (q\lambda )}\frac{\theta\left(ax/\lambda \right)}{\theta\left(x/\lambda\right)}\frac{1}{\left(1/ax;q\right)_\infty},$$ where $1<|ax|$.
:::

::: proof
*Proof.* We apply the $q$-Borel transformation $\mathcal{B}_q^+$ to the series ${}_1\psi_0(a;-;q,x)$. Then, $$\psi (\xi ):=\left(\mathcal{B}_q^+{}_1\psi_0\right)(\xi )
={}_1\psi_1(a;0;q,-\xi ).$$ By Ramanujan's sum [\[Rsum\]](#Rsum){reference-type="eqref" reference="Rsum"}, we obtain the infinite product representation of $\psi (\xi )$ as follows; $$\psi (\xi )=\frac{(q;q)_\infty}{(q/a;q)_\infty}\frac{\theta (a\xi )}{\theta (\xi )}(-q/\xi ;q)_\infty .$$ We apply the $q$-Laplace transformation $\mathcal{L}_{q,\lambda}^+$ to $\psi (\xi )$. $$\begin{aligned}
\left(\mathcal{L}_{q,\lambda}^+\psi \right)(x)&
=\sum_{n\in\mathbb{Z}}\frac{\psi (\lambda q^n)}{\theta \left(\frac{\lambda q^n}{x}\right)}
=\frac{(q;q)_\infty}{(q/a;q)_\infty}\sum_{n\in\mathbb{Z}}\frac{1}{\theta (\frac{\lambda q^n}{x})}\frac{\theta (a\lambda q^n)}{\theta (\lambda q^n)}\left(-\frac{q}{\lambda q^n};q\right)_\infty\notag \\
&=\frac{(q;q)_\infty}{(q/a;q)_\infty}\frac{1}{\theta (\lambda /x)}\frac{\theta (a\lambda )}{\theta (\lambda )}\sum_{n\in\mathbb{Z}}q^{\frac{n(n-1)}{2}}\left(\frac{\lambda}{ax}\right)^n \left(-\frac{q}{\lambda q^n};q\right)_\infty\notag \\
&=\frac{(q;q)_\infty}{(q/a;q)_\infty}\frac{1}{\theta (\lambda /x)}\frac{\theta (a\lambda )}{\theta (\lambda )}(-q/\lambda ;q)_\infty {}_1\psi_1(-\lambda ;0;q,1/ax).\label{qblpsi}
\end{aligned}$$ We remark that $${}_1\psi_1(-\lambda ;0;q,1/ax)=\frac{\theta (\lambda /ax)}{(-q/\lambda ;q)_\infty (1/ax;q)_\infty}.$$ Combining [\[qblpsi\]](#qblpsi){reference-type="eqref" reference="qblpsi"} and [\[inv\]](#inv){reference-type="eqref" reference="inv"}, we obtain the conclusion. ◻
:::

Theorem [\[teiri1\]](#teiri1){reference-type="ref" reference="teiri1"} is rewritten by $$\left(\mathcal{L}_{q,\lambda}^+\circ \mathcal{B}_q^+\tilde{u}\right)(x)
=\frac{(q;q)_\infty}{(q/a;q)_\infty}\frac{\theta (aq\lambda )}{\theta (q\lambda )}\frac{\theta (ax/\lambda )}{\theta (x/\lambda )}\frac{\theta (x)}{\theta (ax)}\tilde{u}_\infty (x).$$ We define the function $C(x;q)$ as follows; $$C(x;q):=\frac{(q;q)_\infty}{(q/a;q)_\infty}\frac{\theta (aq\lambda )}{\theta (q\lambda )}\frac{\theta (ax/\lambda )}{\theta (x/\lambda )}\frac{\theta (x)}{\theta (ax)}.$$ Then, $C(x;q)$ is single valued as a function of $x$.

::: cor
The function $C(x;q)$ is the $q$-elliptic function, i.e., $C(x;q)$ satisfies $$C(qx;q)=C(x;q),\qquad C(e^{2\pi i}x;q)=C(x;q).$$
:::
