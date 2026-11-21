---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-011-42-the-connection-formula-and-alternate-represen
section_title: "The connection formula and alternate representation"
section_number: 4.2
pages: 14-15
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanujan equation between the origin and the inﬁnity."
---
At first, we show the following connection formula between $e_q(\cdot )$ and $E_q(\cdot )$.

::: thm
[]{#eqEq label="eqEq"} For any $x\in\mathbb{C}^*\setminus [1;q]$, $$e_q(x)=\frac{(q;q)_\infty}{\theta_q(-x)}E_q\left(-\frac{q}{x}\right)$$ where $|x|<1$.
:::

::: proof
*Proof.* The function $e_q(x)$ and $E_q(x)$ have infinite product as follows: $$e_q(x)=\frac{1}{(x;q)_\infty},\qquad |x|<1$$ and $$E_q(x)=(-x;q)_\infty .$$ We remark that $e_q(x)$ can be described as $$e_q(x)=\frac{1}{\theta_q(-x)}\left(q,\frac{q}{x};q\right)_\infty =\frac{(q;q)_\infty}{\theta_q(-x)}E_q\left(-\frac{q}{x}\right)$$ where $|x|<1$. We obtain the conclusion. ◻
:::

Therefore, these $q$-exponential functions are related by the connection formula between the origin and the infinity. If we replace $x$ by $x/q$, we obtain the following lemma. This is useful to consider the connection problem in the last section.

::: lem
[]{#alt label="alt"}For any $x\in\mathbb{C}^*\setminus [1;q]$, the function $e_q(x/q)$ has the following alternate representation. $$\begin{aligned}
e_q\left(\frac{x}{q}\right)=

\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}{}_0\varphi_1\left(-;q;q^2,\frac{q^5}{x^2}\right)
-\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}\frac{q^2}{(1-q)x}{}_0\varphi_1\left(-;q^3;q^2,\frac{q^7}{x^2}\right).
\end{aligned}$$
:::

::: proof
*Proof.* From theorem [\[eqEq\]](#eqEq){reference-type="ref" reference="eqEq"}, $${}_1\varphi_0\left(0;-;q,\frac{x}{q}\right)=\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}E_q\left(-\frac{q^2}{x}\right)=\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}{}_0\varphi_0\left(-;-;q,\frac{q^2}{x}\right).$$ Here, $${}_0\varphi_0\left(-;-;q,\frac{q^2}{x}\right)
=\sum_{k\ge 0}\frac{1}{(q;q)_k}(-1)^kq^{\frac{k(k-1)}{2}}\left(\frac{q^2}{x}\right)^k$$ and we remark that $(a;q)_{2k}=(a,aq;q^2)_k$[@GR]. By separating the terms with even and odd $k\ge 0$, we obtain the conclusion. ◻
:::
