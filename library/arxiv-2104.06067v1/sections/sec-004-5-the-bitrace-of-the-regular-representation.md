---
doc_id: arxiv-2104.06067v1
doc_title: "On irreducible characters of the Iwahori-Hecke algebra in type A"
section_id: sec-004-5-the-bitrace-of-the-regular-representation
section_title: "The bitrace of the regular representation"
section_number: 5
pages: 17-20
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "On irreducible characters of the Iwahori-Hecke algebra in type A — We use vertex operators to compute irreducible characters of the Iwahori-Hecke algebra of type A."
---
The Hecke algebra $H_n(q)$ is a $(H_n(q), H_n(q))$-bimodule under the left and right regular actions, and the two actions mutually commute with each other. As a result $$H_n(q)=\bigoplus_{\lambda\vdash n} V_{\lambda}\otimes V^{\lambda}$$ where $V_{\lambda}$ (resp. $V^{\lambda}$) is the irreducible left (resp. right) $H_n(q)$-module labeled by $\lambda$.

Following [@HLR], we introduce the bitrace of the regular representation of $H_n(q)$ by defining for any compositions $\lambda, \mu\models n$ $$\begin{aligned}
btr(\lambda, \mu)=\sum\limits_{\rho\vdash n}\chi^{\rho}_{\lambda}(q)\chi^{\rho}_{\mu}(q).
\end{aligned}$$ This is a $q$-deformation of the second orthogonality relation between irreducible characters of the symmetric group. It is known that $btr(\lambda, \mu)|_{q=1}=\delta_{\lambda, \mu}z_{\lambda}$.

Halverson, Luduc and Ram [@HLR] proved the following result by using Roichman's formula [@Ro] for the Hecke algebra. We will give an elementary proof using the technique developed in this paper.

::: thm
[]{#t:brt label="t:brt"} Let $\lambda=(\lambda_1,\lambda_2,\ldots,\lambda_r)$ and $\mu=(\mu_1,\mu_2,\ldots,\mu_s)$ be two compositions of $n$. Then $$\begin{aligned}
\label{e:brt}
btr(\lambda, \mu)=(q-1)^{-r-s}\sum\limits_M wt(M),
\end{aligned}$$ where $M=(m_{ij})$ run through all $r\times s$ nonnegative integral matrices such that $\sum_{a}m_{ia}=\lambda_i$ $(1\leq i\leq r)$ and $\sum_bm_{bj}=\mu_j$ $(1\leq j\leq s)$ and

$$\begin{aligned}
wt(M)=\prod\limits_{m_{ij}\neq 0}(q-1)^2[m_{ij}]_{q^2}.
\end{aligned}$$
:::

By the Frobenius formula of the Hecke algebra $H_n(q)$ it is readily seen that

$$\begin{aligned}
btr(\lambda, \mu)=\langle \tilde{q}_{\lambda}(q), \tilde{q}_{\mu}(q) \rangle.
\end{aligned}$$

Let $H^{\lambda}_{\mu}(t)=\langle q_{\lambda}(t), q_{\mu}(t) \rangle$, then $brt(\lambda, \mu)(q)=\frac{q^{2n}}{(q-1)^{l(\lambda)+l(\mu)}}H^{\lambda}_{\mu}(q^{-1})$.

Using vertex operators and [\[e:qop\]](#e:qop){reference-type="eqref" reference="e:qop"}-[\[e:qop\*\]](#e:qop*){reference-type="eqref" reference="e:qop*"}, we have the following relation: $$\begin{aligned}
Q^*(z)Q(w)\frac{z-t^2w}{z-tw}=Q(w)Q^*(z)\frac{z-tw}{z-w},
\end{aligned}$$ where the rational functions are power series in negative powers of $z$. Comparing coefficients of $z^{-n}w^{m}$ we immediately obtain the following commutation relation.

::: prop
For any $m,n\in\mathbb{Z}_+$, as operators on $\Lambda_{\mathbb C[t, t^{-1}]}$ $$\begin{aligned}
\label{e:com3}
q^{*}_{n}q_{m}=q_{m}q^{*}_{n}+(1-t)\sum\limits_{k=1}^{min(m, n)}q_{m-k}q^*_{n-k}+(t-1)\sum\limits_{k=1}^{min(m, n)}q^*_{n-k}q_{m-k}t^k.
\end{aligned}$$
:::

For simplicity we denote for integer $k>0$ $$(k)_{t}=(t-1)\frac{t^{2k}-1}{t+1}=(t-1)^2[k]_{t^2}$$ and make the convention that $(k)_t=0$ for $k<0$ and $(0)_t=1$. The following result is easily shown by induction, and also can be used as an inductive definition of $(k)_t$.

::: lem
[]{#t:idetity label="t:idetity"} Let $k$ be a positive integer, then we have $$\begin{aligned}
\label{e:identity}
1-t+(t-1)\sum\limits_{i=1}^{k}(k-i)_tt^i=(k)_t.
\end{aligned}$$
:::

::: thm
[]{#t:q*q label="t:q*q"} Let $k\in \mathbb Z_+$ and $\mu\vDash n$ a composition, then $$\begin{aligned}
q^*_{k}q_{\mu}=\sum\limits_{\tau\models k}\prod\limits_{\tau_a>0}(\tau_a)_t q_{\mu-\tau}.
\end{aligned}$$
:::

::: proof
*Proof.* Use induction on $k+n$. The initial step is clear. Assume the identity holds for $q^*_{k'}q_{\mu}$ such that $k'+|\mu|<k+n$, then $$\begin{aligned}
&q^*_{k}q_{\mu_1}q_{\mu_2}\cdots q_{\mu_l}\\
=&q_{\mu_1}q^*_{k}q_{\mu_2}\cdots q_{\mu_l}+(1-t)\sum\limits_{i\geq1}q_{\mu_{1}-i}q^*_{k-i}q_{\mu_2}\cdots q_{\mu_l}+(t-1)\sum\limits_{i\geq1}q^*_{k-i}q_{\mu_{1}-i}q_{\mu_2}\cdots q_{\mu_l}t^i\\
=&q_{\mu_1}\sum\limits_{\tau\models k}\prod\limits_{\tau_a\geq1}(\tau_a)_t q_{\mu^{[1]}-\tau}+(1-t)\sum\limits_{i\geq1}\sum\limits_{
\tau\models k-i}\prod\limits_{\tau_a\geq 1}(\tau_a)_t q_{\mu_{1}-i}q_{\mu^{[1]}-\tau}\\
&\hskip 3cm +(t-1)\sum\limits_{i\geq1}\sum\limits_{\tau\models k-i}\prod\limits_{\tau_a\geq1}(\tau_i)_tq_{\mu_{1}-i-\tau_1}q_{\mu^{[1]}-\tau^{[1]}}t^i.
\end{aligned}$$ The first summand is $\sum\limits_{\tau\models k}\prod\limits_{\tau_a\geq1}(\tau_a)_t q_{\mu-\tau}$ with $\tau_1=0$. Replacing $i+\tau_1$ by $j$ in the third summand and pulling $(\tau_1)_t=(j-i)_t$ forward, we simplify the second and the third summands as follows: $$\begin{aligned}
&(1-t)\sum\limits_{i\geq1}\sum\limits_{
\tau\models k-i}\prod\limits_{\tau_a\geq1}(\tau_a)_t q_{\mu_{1}-i}q_{\mu^{[1]}-\tau}+(t-1)\sum\limits_{i\geq1}\sum\limits_{j\geq i}(j-i)_tt^i\sum\limits_{\tau\models k-j}\prod\limits_{\tau_a\geq1}(\tau_a)_tq_{\mu_{1}-j}q_{\mu^{[1]}-\tau}\\
=&(1-t)\sum\limits_{i\geq1}\sum\limits_{
\tau\models k-i}\prod\limits_{\tau_a\geq1}(\tau_a)_t q_{\mu_{1}-i}q_{\mu^{[1]}-\tau}+\sum\limits_{j\geq1}(t-1)\sum\limits_{i=1}^{j}(j-i)_tt^i\sum\limits_{\tau\models k-j}\prod\limits_{\tau_a\geq1}(\tau_a)_tq_{\mu_{1}-j}q_{\mu^{[1]}-\tau}\\
=&\sum\limits_{j\geq1}(j)_t\sum\limits_{\tau\models k-j}\prod\limits_{\tau_a\geq1}(\tau_a)_tq_{\mu_{1}-j}q_{\mu^{[1]}-\tau}  ~~~\text{(by Lemma \ref{t:idetity})}.
\end{aligned}$$ Combining this with the first summand, we see the total sum is $\sum\limits_{\tau\models k}\prod\limits_{\tau_a\geq1}(\tau_a)_t q_{\mu-\tau}$. ◻
:::

The following is an immediate consequence of Theorem [\[t:q\*q\]](#t:q*q){reference-type="ref" reference="t:q*q"}.

::: cor
Let $\lambda, \mu\models n$ with $l(\lambda)=r$ and $l(\mu)=s$. Then $$\begin{aligned}
\label{e:H}
H_{\mu}^{\lambda}(t)=\sum\limits_{M}\prod\limits_{i=1}^{r}\prod\limits_{a\geq1}(\tau^{(i)}_a)_t.
\end{aligned}$$ where the sum is over all $r\times s$ nonnegative integer matrices $M=(\tau^{(i)}_a)_{1\leq i\leq r, 1\leq a \leq s}$ such that the row sums are $\lambda_1,\ldots,\lambda_r$ and the column sums are $\mu_1,\ldots,\mu_s$
:::

This provides a simple proof of Theorem [\[t:brt\]](#t:brt){reference-type="ref" reference="t:brt"} due the fact that $t^{2k}(k)_{t^{-1}}=(k)_t,$ and $q_i=0$ for $i<0$.

**Acknowledgments**

The work is partially supported by Simons Foundation grant No. 523868 and NSFC grant No. 11531004.
