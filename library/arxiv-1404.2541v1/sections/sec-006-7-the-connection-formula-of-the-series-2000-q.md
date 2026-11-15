---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-006-7-the-connection-formula-of-the-series-2000-q
section_title: "The connection formula of the series 20(0,0;-;q,)"
section_number: 7
pages: 15-17
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.957
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
The aim of this section is to give a proof for the following theorem;

::: thm
[]{#divergentramanujan label="divergentramanujan"}For any $x\in\mathbb{C}^*\setminus [-\lambda ;q],$ $$\begin{aligned}
\theta_q(x){}_2f_0&\left(0,0;-;q,-\frac{x}{q}\right)=(q;q)_\infty\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{qx}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}
{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)\\
&+\frac{(q;q)_\infty}{1-q}\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{x}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\frac{\lambda}{x}
{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$
:::

We give the proof of theorem [\[divergentramanujan\]](#divergentramanujan){reference-type="ref" reference="divergentramanujan"}.

::: proof
*Proof.* We apply the $q$-Borel transformation $\mathcal{B}_q^+$ to the divergent series $v(x)={}_2\varphi_0(0,0;-;q,-x/q)$. We obtain $$\left(\mathcal{B}_q^+v\right)(\xi )={}_1\varphi_0\left(0;-;q,\frac{\xi}{q}\right)=:\varphi (\xi ).$$ From lemma [\[alt\]](#alt){reference-type="ref" reference="alt"}, $$\varphi (\xi )=\frac{(q;q)_\infty}{\theta_q\left(-\frac{\xi}{q}\right)}
{}_0\varphi_1\left(-;q;q^2,\frac{q^5}{\xi^2}\right)-\frac{(q;q)_\infty}{\theta_q\left(-\frac{\xi}{q}\right)}
\frac{q^2}{(1-q)\xi}{}_0\varphi_1\left(-;q^3;q^2,\frac{q^7}{\xi^2}\right)$$ where $|\xi /q|<1$.

We apply the $q$-Laplace transformation $\mathcal{L}_{q, \lambda}^+$ to $\varphi (\xi )$: $$\begin{aligned}
&\left(\mathcal{L}_{q,  \lambda}^+\varphi\right)(x)=\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta_q\left(\frac{\lambda q^n}{x}\right)}
=\sum_{n\in\mathbb{Z}}\frac{{}_1\varphi_0\left(0;-;q,\frac{\lambda q^n}{q}\right)}{\theta_q\left(\frac{\lambda q^n}{x}\right)}\\









&=\frac{(q;q)_\infty}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\sum_{n-m\in\mathbb{Z}}(q^2)^{\frac{(n-m)(n-m-1)}{2}}\left(-\frac{\lambda^2}{qx}\right)^{n-m}\\
&\qquad\qquad\qquad\qquad \times \sum_{m\ge 0}\frac{(-1)^m(q^2)^{\frac{m(m-1)}{2}}}{(q;q^2;q^2)_m}\left(\frac{q^2}{x}\right)^m\\
&-\frac{(q;q)_\infty}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\frac{q^2}{(1-q)\lambda}\sum_{n-m\in\mathbb{Z}}(q^2)^{\frac{(n-m)(n-m-1)}{2}}\left(-\frac{\lambda^2}{q^2x}\right)^{n-m}\\
&\qquad\qquad\qquad\qquad \times
\sum_{m\ge 0}\frac{(-1)^m(q^2)^{\frac{m(m-1)}{2}}}{(q^3,q^2;q^2)_m}\left(\frac{q^3}{x}\right)^m.
\end{aligned}$$ Therefore, $$\begin{aligned}
&{}_2f_0\left(0,0;-;q,-\frac{x}{q}\right)
=\mathcal{L}_{q, \lambda}^+\circ\mathcal{B}_q^+{}_2\varphi_0\left(0,0;-;q,-\frac{x}{q}\right)\\
&=(q;q)_\infty\frac{\theta_{q^2}\left(-\frac{\lambda^2}{qx}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)
+\frac{(q;q)_\infty}{1-q}\frac{\theta_{q^2}\left(-\frac{\lambda^2}{x}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}
{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$ We obtain the conclusion. ◻
:::

::: rem
By theorem [\[divergentramanujan\]](#divergentramanujan){reference-type="ref" reference="divergentramanujan"}, we have $$\tilde{u}_2(x,\lambda )=\tilde{C}_{21}v_1(x)+\tilde{C}_{22}v_2(x),$$ where $$\tilde{C}_{21}(x)=\frac{(q;q)_\infty\theta_{q^2}(-qx/\lambda^2)\theta_{q^2}(x)}{\theta_q(-q/\lambda )\theta_q(x/\lambda )\theta_q(x)}$$ and $$\tilde{C}_{22}(x)=\frac{(q;q)_\infty\theta_{q^2}(-x/\lambda^2)\theta_{q^2}(x/q)}{\theta_q(-1/\lambda )\theta_q(x/\lambda )\theta_q(x/q)}.$$ This is a half of our connection formula.
:::
