---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q -Airy function"
section_id: sec-001-2-standard-notations
section_title: "Standard notations"
section_number: 2
pages: 4-5
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "A connection formula between the Ramanujan function and the q -Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
In this section, we fix our notations. We assume that $q\in\mathbb{C}^*$ satisfies $0<~|q|<1$. We define the $q$-Pochhammer symbol $(a;q)_n$.

::: defi
For any $n\in\mathbb{Z}_{\ge 0}$, $$(a;q)_n=
\begin{cases}
1,&\qquad n=0,\\
(1-a)(1-aq)\cdots (1-aq^{n-1}),&\qquad n\ge 1,
\end{cases}$$ and $$(a;q)_\infty =\lim_{n\to\infty}(a;q)_n.$$ Moreover, $$(a_1,a_2,\cdots ,a_m;q)_\infty =(a_1;q)_\infty (a_2;q)_\infty\cdots (a_m;q)_\infty .$$
:::

The $q$-difference operator $\sigma_q$ is given by $\sigma_qf(x)=f(qx)$. The basic hypergeometric series ${}_r\varphi_s$ is defined as follows.

::: defi
The basic hypergeometric series is given by $${_r\varphi_s}(a_1,\cdots ,a_r;b_1,\cdots ,b_s;q,x)
:=\sum_{n\ge 0}\frac{(a_1,\cdots ,a_r;q)_n}{(b_1,\cdots ,b_s;q)_n(q;q)_n}
\left[(-1)^nq^{\frac{n(n-1)}{2}}\right]^{1+s-r}x^n.$$
:::

We define the theta function of Jacobi. We denote by $\theta_q(x)$ or more shortly $\theta (x)$. The theta function of Jacobi is given by following series;

::: defi
For any $x\in\mathbb{C}^*$, $$\theta_q(x)=\theta (x)=\sum_{n\in\mathbb{Z}}q^{\frac{n(n-1)}{2}}x^n.$$
:::

The theta function has some important properties. The following lemma is called Jacobi's triple product identity.

::: lem
For any $x\in\mathbb{C}^*$, we have $$\theta (x)=\left(q,-x,-\frac{q}{x};q\right)_\infty .$$
:::

The theta function satisfies the following $q$-difference relation.

::: lem
[]{#qt label="qt"} For any $k\in\mathbb{Z}, \theta (x)$ satisfies $$\theta (q^kx)=q^{-\frac{k(k-1)}{2}}x^{-k}\theta (x),\qquad \forall x\in\mathbb{C}^*.$$
:::

From lemma[\[qt\]](#qt){reference-type="ref" reference="qt"} , we remark that the function $\theta (-\lambda x)/\theta (\lambda x)$, $\forall\lambda\in\mathbb{C}^*$ satisfies a $q$-difference equation $$u(qx)=-u(x)$$ which is also satisfied by the function $u(x)=e^{\pi i\left(\frac{\log x}{\log q}\right)}$. From the definition, the theta function has the following inversion formula.

::: lem
[]{#inv label="inv"} For any $x\in\mathbb{C}^*$ , one gets $$x\theta\left(\frac{1}{x}\right)=\theta (x).$$
:::
