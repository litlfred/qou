---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗"
section_id: sec-001-2-basic-notations
section_title: "Basic notations"
section_number: 2
pages: 5-8
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗ — We show an asymptotic formula of the divergent bilateral bas ic hypergeometric series 1ψ 0(a; −;q, ·)"
text_source: latex
latex_prose_ratio: 0.711
latex_coverage_ratio: 0.976
---
In this section, we fix our notations. We assume that $0<|q|<1$ and $\sigma_q$ is the $q$-difference operator such that $\sigma_qf(x)=f(qx)$. The basic hypergeometric series is $$\begin{aligned}
{}_r\varphi_s(a_1,\dots ,a_r;&b_1,\dots ,b_r;q,x)\notag\\
&:=\sum_{n\ge 0}\frac{(a_1,\dots ,a_r;q)_n}{(b_1,\dots ,b_s;q)_n(q;q)_n}
\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{1+s-r}x^n.
\label{bh}
\end{aligned}$$ The radius of convergence $\rho$ of the basic hypergeometric series is given by [@Koo] $$\rho =
\begin{cases}
\infty ,& \textrm{if }\quad r<s+1, \\
1, & \textrm{if }\quad r=s+1, \\
0, & \textrm{if }\quad r>s+1.
\end{cases}$$ The bilateral basic hypergeometric series is $$\begin{aligned}
{}_r\psi_s(a_1,\dots ,a_r;&b_1,\dots ,b_s;q,x)\notag\\
&:=\sum_{n\in\mathbb{Z}}\frac{(a_1,\dots ,a_r;q)_n}{(b_1,\dots ,b_s;q)_n}
\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{s-r}x^n.
\label{bbh}
\end{aligned}$$ If $s<r$, the series [\[bbh\]](#bbh){reference-type="eqref" reference="bbh"} diverges for $x\not=0$ and if $r=s$, the series [\[bbh\]](#bbh){reference-type="eqref" reference="bbh"} converges $|b_1\dots b_s/a_1\dots a_r|<|x|<1$ (see [@GR] for more detail). The series [\[bh\]](#bh){reference-type="eqref" reference="bh"} is a $q$-analogue of the generalized hypergeometric function $$\begin{aligned}
{}_rF_s (\alpha_1,\dots ,\alpha_r&;\beta_1,\dots ,\beta_s;x)
:=\sum_{n\ge 0}\frac{(\alpha_1,\dots ,\alpha_r)_n}{(\beta_1,\dots ,\beta_s)_nn!}x^n
\end{aligned}$$ and the series [\[bbh\]](#bbh){reference-type="eqref" reference="bbh"} is a $q$-analogue of the bilateral hypergeometric function $${}_rH_s(\alpha_1,\dots ,\alpha_r;\beta_1,\dots ,\beta_s;x)
:=\sum_{n\in\mathbb{Z}}\frac{(\alpha_1,\dots ,\alpha_r)_n}{(\beta_1;\dots ,\beta_s)_n}x^n.$$ By D'Alembert's ratio test, it can be checked that ${}_rH_r$ converges only for $|x|=1$ [@Slater], provided that $\Re (\beta_1+\dots +\beta_r-\alpha_1-\dots -\alpha_r)>1$.

The $q$-exponential function $e_q(x)$ is $$e_q(x):={}_1\varphi_0(0;-;q,x)
=\sum_{n\ge 0}\frac{x^n}{(q;q)_n}$$ The function $e_q(x)$ has the infinite product representation as follows; $$e_q(x)=\frac{1}{(x;q)_\infty},\qquad |x|<1.$$ The limit $q\to 1-0$ of $e_q(x)$ is the exponential function [@GR]; $$\lim_{q\to 1-0}e_q(x(1-q))=e^x.
\label{limexp}$$

The $q$-gamma function $\Gamma_q(x)$ is $$\Gamma_q(x):=\frac{(q;q)_\infty}{(q^x;q)_\infty}(1-q)^{1-x},\qquad 0<q<1.$$ The limit $q\to 1-0$ of $\Gamma_q(x)$ gives the gamma gunction [@GR]; $$\lim_{q\to 1-0}\Gamma_q(x)=\Gamma (x).\label{limgamma}$$ The theta function of Jacobi is given by $$\theta (x):=\sum_{n\in\mathbb{Z}}q^{\frac{n(n-1)}{2}}x^n,\qquad \forall x\in\mathbb{C}^*.$$ Jacobi's triple product identity is $$\theta (x)=(q,-x,-q/x;q)_\infty$$ and the theta function satisfies the following $q$-difference equation $$\theta (q^kx)=x^{-k}q^{-\frac{k(k-1)}{2}}\theta (x),\qquad \forall k\in\mathbb{Z}.$$ The inversion formula is $$\theta (x)=x\theta (1/x).
\label{inv}$$ We remark that $\theta (\lambda q^k/x)=0$ if and only if $x\in[-\lambda ;q]$. In our study, the following proposition [@Z1] is useful to consider the limit $q\to 1-0$ of our formula.

::: prop
For any $x\in\mathbb{C}^* (-\pi <\arg x<\pi )$, we have $$\lim_{q\to 1-0}\frac{\theta (q^\alpha x)}{\theta (q^\beta x)}=x^{\beta -\alpha}\label{limt1}$$ and $$\lim_{q\to 1-0}\frac{\theta \left(\dfrac{q^\alpha x}{(1-q)}\right)}{\theta \left(\dfrac{q^\beta x}{(1-q)}\right)}(1-q)^{\beta -\alpha}=
\left(\frac{1}{x}\right)^{\alpha -\beta}.\label{limt2}$$
:::

We also use the limit [@GR] as follows; $$\lim_{q\to 1-0}\frac{(xq^\alpha ;q)_\infty}{(x;q)_\infty}=(1-x)^{-\alpha},\qquad |x|<1.
\label{limbin}$$

# An asymptotic formula of the divergent series ${}_1\psi_0(a;-;q,x)$

In this section, we show an asymptotic formula of the divergent series ${}_1\psi_0(a;-;q,x)$. At first, we review Ramanujan's sum for ${}_1\psi_1(a;b;q,z)$ and its property. Ramanujan gives the following sum [@Hardy] $${}_1\psi_1(a;b;q,z)=\frac{(q,b/a,az,q/az;q)_\infty}{(b,q/a,z,b/az;q)_\infty},\qquad \left|b/a\right|<|z|<1.
\label{Rsum}$$ We can regard this sum as a $q$-analogue of the bilateral binomial theorem [@Horn] as follows;

**Theorem.** *(Horn [@Horn])* *If $z$ is a complex number such that $|z|=1$, we have*$${}_1H_1(\alpha ;\beta ;z)=\frac{\Gamma (\beta )\Gamma (1-\alpha )}{\Gamma (\beta -\alpha )}\frac{(1-z)^{\beta -\alpha -1}}{(-z)^{\beta -1}},
\label{bbt}$$ *provided that $\Re (\beta -\alpha )>1$.*

Let $z$ is a complex number such that $-\pi <\arg z <\pi$. The summation [\[Rsum\]](#Rsum){reference-type="eqref" reference="Rsum"} is rewritten by $$\frac{(q,b/a,az,q/az;q)_\infty}{(b,q/a,z,b/az;q)_\infty}
=\frac{(q,b/a;q)_\infty}{(b,q/a;q)_\infty}\frac{\theta (-az)}{\theta (-aqz/b)}\frac{(aqz/b;q)_\infty}{(z;q)_\infty}.
\label{bin3}$$ In [\[bin3\]](#bin3){reference-type="eqref" reference="bin3"}, we put $a=q^\alpha$ and $b=q^\beta$ (with $\Re (\beta -\alpha )>1$), we obtain $${}_1\psi_1 (q^\alpha ;q^\beta ;q,z)
=\frac{\Gamma_q(\beta )\Gamma_q (1-\alpha )}{\Gamma_q(\beta -\alpha )}
\frac{\theta (q^\alpha (-z))}{\theta (q^{\alpha +1-\beta }(-z))}
\frac{(q^{\alpha +1-\beta}z;q)_\infty}{(z;q)_\infty},
\label{qbb}$$ where $|q^{\beta -\alpha}|<|z|<1$. Combining [\[limgamma\]](#limgamma){reference-type="eqref" reference="limgamma"}, [\[limt1\]](#limt1){reference-type="eqref" reference="limt1"} and [\[limbin\]](#limbin){reference-type="eqref" reference="limbin"}, we can check out that the limit $q\to 1-0$ of [\[qbb\]](#qbb){reference-type="eqref" reference="qbb"} gives the bilateral binomial theorem [\[bbt\]](#bbt){reference-type="eqref" reference="bbt"}, provided that $-\pi <\arg z <\pi$.

The bilateral basic hypergeometric series ${}_1\psi_1(a;b;q,z)$ satisfies the $q$-difference equation $$\left(\frac{b}{q}-az\right)u(qz)+(z-1)u(z)=0.
\label{bqua}$$ We consider the degeneration of the equation [\[bqua\]](#bqua){reference-type="eqref" reference="bqua"} in the next section.
