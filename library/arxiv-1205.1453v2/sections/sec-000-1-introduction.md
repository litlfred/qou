---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.901
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series — We show an asymptotic formula of the divergent bilateral basic hypergeometric series 1ψ0(a; −; q, ·) with using the"
---
In this paper, we show an asymptotic formula of the divergent bilateral basic hypergeometric series $${}_1\psi_0 (a;-;q;x ):=\sum_{n\in\mathbb{Z}} (a;q)_n\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{-1}x^n.$$ Here, $(a;q)_n$ is the $q$-shifted factorial; $$(a;q)_n:=
\begin{cases}
1, &n=0, \\
(1-a)(1-aq)\dots (1-aq^{n-1}), &n\ge 1,\\
[(1-aq^{-1})(1-aq^{-2})\dots (1-aq^n)]^{-1}, &n\le -1
\end{cases}$$ moreover, $(a;q)_\infty :=\lim_{n\to \infty}(a;q)_n$ and $$(a_1,a_2,\dots ,a_m;q)_\infty:=(a_1;q)_\infty (a_2;q)_\infty \dots (a_m;q)_\infty.$$

The $q$-shifted factorial $(a;q)_n$ is a $q$-analogue of the shifted factorial $$(\alpha )_n=\alpha \{\alpha +1\}\cdots \{\alpha +(n-1)\}.$$ The series ${}_1\psi_0(a;-;q,\cdot )$ is related to the bilateral basic hypergeometric series ${}_1\psi_1(a;b;q,\cdot )$. At first, we review the series $${}_1\psi_1(a;b;q,z):=\sum_{n\in\mathbb{Z}}\frac{(a;q)_n}{(b;q)_n}z^n.$$ This series has Ramanujan's summation formula [@GR] $${}_1\psi_1(a;b;q,z)=\frac{(q,b/a,az,q/az;q)_\infty}{(b,q/a,z,b/az;q)_\infty}, \qquad 
\left|b/a\right|<|z|<1,\label{rsum}$$ which was first given by Ramanujan [@Hardy]. This formula is considered as a extension of the $q$-binomial theorem [@GR; @Askey]; $$\sum_{n\ge 0}\frac{(a;q)_n}{(q;q)_n}z^n=\frac{(az;q)_\infty}{(z;q)_\infty},\qquad |z|<1.$$ We also regard the summation [\[rsum\]](#rsum){reference-type="eqref" reference="rsum"} as a $q$-analogue of the bilateral binomial theorem [@Horn] discovered by M. E. Horn. If $\alpha$ and $\beta$ are complex numbers $\Re (\beta -\alpha )>1$ and $z$ is a complex number with $|z|=1$, then $$\sum_{n\in\mathbb{Z}}\frac{(\alpha )_n}{(\beta )_n}z^n
=\frac{(1-z)^{\beta -\alpha -1}}{(-z)^{\beta -1}}\frac{\Gamma (1-\alpha )\Gamma (\beta )}{\Gamma (\beta -\alpha )}.\label{bbt1}$$ We remark that the limit $q\to 1-0$ of [\[rsum\]](#rsum){reference-type="eqref" reference="rsum"} with suitable condition gives the bilateral binomial theorem [\[bbt1\]](#bbt1){reference-type="eqref" reference="bbt1"}.

The series ${}_1\psi_1(a;b;q,z)$ satisfies the following $q$-difference equation $$\left(\frac{b}{q}-az\right)u(qz)+(z-1)u(z)=0.$$ In this paper, we study the degeneration of this equation as follows; $$\left(\frac{1}{q}-ax\right)\tilde{u}(qx)+x \tilde{u}(x)=0.$$ This equation has a formal solution $$\tilde{u}(x)={}_1\psi_0(a;-;q,x).

\label{b2s}$$ But $\tilde{u}(x)$ is a divergent around the origin [@GR] and its properties are not clear. In section three, we show an asymptotic formula of the series [\[b2s\]](#b2s){reference-type="eqref" reference="b2s"} with using the $q$-Borel-Laplace transformations. The $q$-Borel-Laplace transformations are introduced in the study of connection problems on linear $q$-difference equations between the origin and the infinity.

Connection problems on $q$-difference equations with regular singular points are studied by G. D. Birkhoff [@Birkhoff]. The first example of the connection formula is given by G. N. Watson [@W] in 1910 as follows; $$\begin{aligned}
{}_2 \varphi_1(a,b;c;q,&x )= 
\frac{(b,c/a;q)_\infty (a x,q/ a x;q)_\infty }{(c, b/a;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(a,aq/c;aq/b;q,cq/abx \right) \notag \\
&+\frac{(a,c/b;q)_\infty (b x, q/ b x;q)_\infty }{(c, a/b;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(b, bq/c; bq/a; q, cq/abx \right). \label{wat}
\end{aligned}$$ The function ${}_2\varphi_1(a,b;c;q,x)$ is the basic hypergeometric series $${}_2\varphi_1(a,b;c;q,x)=\sum_{n\ge 0} \frac{(a,b;q)_n}{(c;q)_n(q;q)_n}x^n,$$ which is introduced by E. Heine [@hein]. This series satisfies the second order linear $q$-difference equation $$(c-abqx)u(q^2x)-\left\{c+q-(a+b)qx\right\}u(qx)+q(1-x)u(x)=0.
\label{heine}$$ around the origin. On the other hand, the equation [\[heine\]](#heine){reference-type="eqref" reference="heine"} has a fundamental system of solutions $$v_1(x)=\frac{\theta (-ax)}{\theta (-x)}{}_2\varphi_1\left(a,\frac{aq}{c};\frac{aq}{b};q,\frac{cq}{abx}\right), 
\quad v_2(x)=\frac{\theta (-bx)}{\theta (-x)}{}_2\varphi_1\left(b,\frac{bq}{c};\frac{bq}{a};q,\frac{cq}{abx}\right)$$ around the infinity [@Z0]. Here, $\theta (\cdot )$ is the theta function of Jacobi (see section two). In the connection formula [\[wat\]](#wat){reference-type="eqref" reference="wat"}, we remark that the connection coefficients are given by $q$-elliptic functions.

Other connection formulae, especially connection formulae of irregular singular type $q$-special functions has not known for a long time. Recently, C. Zhang gives some connection formulae by two different types of $q$-Borel transformations and $q$-Laplace transformations [@Z0; @Z1; @Z2], which are introduced by J. Sauloy[@sauloy]. We assume that $f(x)$ is a formal power series $f(x)=\sum_{n\ge 0}a_nx^n$, $a_0=1$.

::: defi
For any power series $f(x)$, the $q$-Borel transformation of the first kind $\mathcal{B}_q^+$ is $$\left(\mathcal{B}_q^+f\right)(\xi ):=\sum_{n\ge 0}a_nq^{\frac{n(n-1)}{2}}\xi^n=:\varphi (\xi ).$$ For an entire function $\varphi$, the $q$-Laplace transformation of the first kind $\mathcal{L}_{q,\lambda }^+$ is $$\left(\mathcal{L}_{q,\lambda}^+\varphi\right)(x):=
\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta \left(\frac{\lambda q^n}{x}\right)},\quad \lambda\not\in q^{\mathbb{Z}}.$$ Similarly, the $q$-Borel transformation of the second kind $\mathcal{B}_q^-$ is $$\left(\mathcal{B}_q^-f\right)(\xi ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\xi^n=:g(\xi )$$ and the $q$-Laplace transformation of the second kind $\mathcal{L}_q^-$ is $$\left(\mathcal{L}_q^-g\right)(x):=\frac{1}{2\pi i}\int_{|\xi |=r}g(\xi )\theta\left(\frac{x}{\xi}\right)\frac{d\xi}{\xi}.$$
:::

We remark that each $q$-Borel transformation is a formal inverse of each $q$-Laplace transformation; $$\mathcal{L}_{q,\lambda}^+\circ\mathcal{B}_q^+f=f,\qquad 
\mathcal{L}_q^-\circ\mathcal{B}_q^-f=f.$$

We can find applications of the $q$-Borel-Laplace method of the first kind in [@Z0; @Z1; @M4]. This summation method is powerful to deal with divergent type basic hypergeometric series and to study the $q$-Stokes phenomenon. Applications of the method of the second kind can be found in [@Z2; @M0; @M1; @M4]. But other examples, for example, applications to bilateral basic hypergeometric series, has not known.

In this paper, we study an asymptotic formula of the divergent bilateral basic hypergeometric series ${}_1\psi_0(a;-;q,\cdot )$ from viewpoint of connection problems on linear $q$-difference equations. We show the following theorem.

**Theorem.** *For any* $x\in\mathbb{C}^*\setminus [-\lambda ;q]$ *, we have* $$\hat{{}_1\psi_0}(a;-;\lambda ;q,x)=\frac{(q;q)_\infty}{\left(q/a;q\right)_\infty}\frac{\theta (aq\lambda )}{\theta (q\lambda )}\frac{\theta\left(ax/\lambda \right)}{\theta\left(x/\lambda\right)}\frac{1}{\left(1/ax;q\right)_\infty},$$ *where $1<|ax|$.*

Here, the function $\hat{{}_1\psi_0}(a;-;\lambda ;q,x)$ is the $q$-Borel-Laplace transform of the series ${}_1\psi_0(a;-;q,x)$ and the set $[-\lambda ;q]$ is the $q$-spiral which is given by $[\lambda ;q]:=\{\lambda q^k: k\in\mathbb{Z}\}$. We also show the limit $q\to 1-0$ of our asymptotic formula in section four. If we take a suitable limit $q\to 1-0$ of the theorem above, we formally obtain the asymptotic formula of the bilateral hypergeometric series ${}_1H_0$.
