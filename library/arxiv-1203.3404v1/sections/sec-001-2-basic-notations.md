---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-001-2-basic-notations
section_title: "Basic notations"
section_number: 2
pages: 7-8
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanujan equation between the origin and the inﬁnity."
---
In this section, we review our notations. We assume that $q\in\mathbb{C}^*$ satisfies $0<|q|<1$. The $q$-shifted operator $\sigma_q$ is given by $\sigma_qf(x)=f(qx)$. For any fixed $\lambda\in\mathbb{C}^*\setminus q^{\mathbb{Z}}$, the set $[\lambda ;q]$-spiral is $[\lambda ;q]:=\lambda q^{\mathbb{Z}}=\{\lambda q^k;k\in\mathbb{Z}\}$. The (generalized) basic hypergeometric series ${}_r\varphi_s(a_1,\dots ,a_r;b_1,\dots ,b_s;q,x)$ is $$\begin{aligned}
{}_r\varphi_s(a_1,\dots ,a_r&;b_1,\dots ,b_s;q,x)\\
&:=\sum_{n\ge 0}\frac{(a_1,\dots ,a_r;q)_n}{(b_1,\dots ,b_s;q)_n(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{1+s-r}x^n.
\end{aligned}$$ This series has radius of convergence $\infty , 1$ or $0$ according to whether $r-s<1, r-s=1$ or $r-s>1$ (see [@GR] for further details). In connection problems, the theta function of Jacobi is important. This function is defined by $$\theta_q(x):=\sum_{n\in\mathbb{Z}}q^{\frac{n(n-1)}{2}}x^n,\qquad x\in\mathbb{C}^*.$$ We denote $\theta_q(\cdot )$ or more shortly $\theta (\cdot )$. The theta function has the following properties;

1.  Jacobi's triple product identity is $$\theta_q(x)=\left(q,-x,-\frac{q}{x};q\right)_\infty .$$

2.  The $q$-difference equation which the theta function satisfies; $$\theta_q(q^kx)=q^{-\frac{n(n-1)}{2}}x^{-k}\theta_q(x),\quad \forall k\in\mathbb{Z}.$$

3.  The inversion formula; $$\theta_q\left(\frac{1}{x}\right)=\frac{1}{x}\theta_q(x).$$

We remark that the function $\theta (-\lambda x)/\theta (\lambda x)$, $\lambda\in\mathbb{C}^*$ satisfies a $q$-difference equation $$u(qx)=-u(x)$$ which is also satisfied by the function $u(x)=e^{\pi i\left(\frac{\log x}{\log q}\right)}$.
