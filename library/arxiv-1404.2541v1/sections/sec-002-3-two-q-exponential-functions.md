---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-002-3-two-q-exponential-functions
section_title: "Two q-exponential functions"
section_number: 3
pages: 8-11
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
We review two different $q$-exponential functions $e_q(x)$ and $E_q(x)$ to consider the connection problem on the Ramanujan equation. In this section, we show the relation between them. We review two different $q$-exponential functions from the viewpoint of the connection problems. One of the $q$-exponential function $e_q(x)$ is given by $$e_q(x):={}_1\varphi_0 (0;-;q,x)=\sum_{n\ge 0}\frac{x^n}{(q;q)_n}.$$ The other $q$-exponential function $E_q(x)$ is $$E_q(x):={}_0\varphi_0(-;-;q,-x)=\sum_{n\ge 0}\frac{q^{\frac{n(n-1)}{2}}}{(q;q)_n}x^n.$$ The function $e_q(x)$ satisfies the following first order $q$-difference equation $$\left\{\sigma_q-(1-x)\right\}u(x)=0$$ and $E_q(x)$ satisfies $$\left\{(1+x)\sigma_q-1\right\}u(x)=0.$$ The limit $q\to 1-0$ converges the exponential function $$\lim_{q\to 1-0}e_q\left(x(1-q)\right)=\lim_{q\to 1-0}E_q\left(x(1-q)\right)=e^x.$$ In this sense, these functions considered as $q$-analogues of the exponential function. It is known that there exists the relation between these functions [@GR]: $$e_q(x)E_q(-x)=1,\quad e_{q^{-1}}(x)=E_q(-qx).$$ But another relation has not known. We show the connection formula between them and give alternate representation of $e_q(x)$.

At first, we show the following connection formula between $e_q(x)$ and $E_q(x)$.

::: thm
[]{#eqEq label="eqEq"} For any $x\in\mathbb{C}^*\setminus [1;q]$, $$e_q(x)=\frac{(q;q)_\infty}{\theta_q(-x)}E_q\left(-\frac{q}{x}\right)$$ where $|x|<1$.
:::

::: proof
*Proof.* The function $e_q(x)$ and $E_q(x)$ have infinite product as follows: $$e_q(x)=\frac{1}{(x;q)_\infty},\qquad |x|<1$$ and $$E_q(x)=(-x;q)_\infty .$$ We remark that $e_q(x)$ can be described as $$e_q(x)=\frac{1}{\theta_q(-x)}\left(q,\frac{q}{x};q\right)_\infty =\frac{(q;q)_\infty}{\theta_q(-x)}E_q\left(-\frac{q}{x}\right)$$ where $|x|<1$. We obtain the conclusion. ◻
:::

Therefore, these $q$-exponential functions are related by the connection formula between the origin and the infinity. If we replace $x$ by $x/q$, we obtain the following lemma. This is useful to consider the connection problem in the last section.

::: lmm
[]{#alt label="alt"}For any $x\in\mathbb{C}^*\setminus [1;q]$, the function $e_q(x/q)$ has the following alternate representation. $$\begin{aligned}
e_q\left(\frac{x}{q}\right)=

\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}{}_0\varphi_1\left(-;q;q^2,\frac{q^5}{x^2}\right)
-\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}\frac{q^2}{(1-q)x}{}_0\varphi_1\left(-;q^3;q^2,\frac{q^7}{x^2}\right).
\end{aligned}$$
:::

::: proof
*Proof.* From theorem [\[eqEq\]](#eqEq){reference-type="ref" reference="eqEq"}, $${}_1\varphi_0\left(0;-;q,\frac{x}{q}\right)=\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}E_q\left(-\frac{q^2}{x}\right)=\frac{(q;q)_\infty}{\theta_q\left(-\frac{x}{q}\right)}{}_0\varphi_0\left(-;-;q,\frac{q^2}{x}\right).$$ Here, $${}_0\varphi_0\left(-;-;q,\frac{q^2}{x}\right)
=\sum_{k\ge 0}\frac{1}{(q;q)_k}(-1)^kq^{\frac{k(k-1)}{2}}\left(\frac{q^2}{x}\right)^k$$ and we remark that $(a;q)_{2k}=(a,aq;q^2)_k$ [@GR]. By separating the terms with even and odd $k\ge 0$, we obtain the conclusion. ◻
:::

By separating the terms with $r$-th order terms, we have the following corollary.

::: crl
[]{#cor33 label="cor33"}For any $x\in\mathbb{C}^*\setminus [1;q]$, we have $$\begin{aligned}
e_q(x)&=\frac{(q;q)_\infty}{\theta_q(-x)}
\left[{}_0\varphi_{r-1}\left(-;q,q^2,\dots ,q^{r-1};q^r,(q^r)^{\frac{r-1}{2}}\left(\frac{q}{x}\right)^r\right)\right.\notag\\
&+\frac{(-1)}{1-q}\frac{q}{x}{}_0\varphi_{r-1}\left(-;q^2,\dots ,q^{r-1},q^{r+1};q^r,(q^r)^{\frac{r+1}{2}}\left(\frac{q}{x}\right)^r\right)\notag\\
&+\dots +\frac{(-1)^{r-1}q^{\frac{(r-1)(r-2)}{2}}}{(1-q)(1-q^2)\dots (1-q^{r-1})}\left(\frac{q}{x}\right)^{r-1}\notag\\
&\left.{}_0\varphi_{r-1}\left(-;q^{r+1},\dots ,q^{2(r-1)};q^r,(q^r)^{\frac{3(r-1)}{2}}\left(\frac{q}{x}\right)^r\right)
\right].\notag
\end{aligned}$$
:::
