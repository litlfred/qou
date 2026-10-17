---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.902
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanujan equation between the origin and the inﬁnity."
---
In this papar, we show two essentially different connection formulae of some basic hypergeometric series between the origin and the infinity. In 1846, E. Heine [@hein] introduced the basic hypergeometric series ${}_2\varphi_1(a,b;c;q,x)$ as follows; $${}_2\varphi_1(a,b;c;q,x):=\sum_{n\ge 0}\frac{(a,b;q)_n}{(c;q)_n(q;q)_n}x^n,\quad c\not \in q^{-\mathbb{N}}.
\label{heine}$$ Here, $(a;q)_n$ is the $q$-shifted factorial; $$(a;q)_n:=
\begin{cases}
1, &n=0, \\
(1-a)(1-aq)\dots (1-aq^{n-1}), &n\ge 1,
\end{cases}$$ moreover, $(a;q)_\infty :=\lim_{n\to \infty}(a;q)_n$ and $$(a_1,a_2,\dots ,a_m;q)_\infty:=(a_1;q)_\infty (a_2;q)_\infty \dots (a_m;q)_\infty.$$ The $q$-shifted factorial $(a;q)_n$ is a $q$-analogue of the shifted factorial $(\alpha )_n$; $$(\alpha )_n:=
\begin{cases}1, &n=0,\\
\alpha (\alpha +1)\dots \{\alpha +(n-1)\}, &n\ge 1.
\end{cases}$$ The basic hypergeometric series [\[heine\]](#heine){reference-type="eqref" reference="heine"} is a $q$-analogue of the hypergeometric series ${}_2F_1(\alpha ,\beta ;\gamma ,z)$[@Gauss13]; $${}_2F_1(\alpha ,\beta ;\gamma ,z):=\sum_{n\ge 0}\frac{(\alpha )_n(\beta )_n}{(\gamma )_nn!}z^n.\label{gauss}$$ This series [\[gauss\]](#gauss){reference-type="eqref" reference="gauss"} has the following famous degeneration diagram $$\begin{picture}(370,70)(0,0)
        \put(35,30){{  Gauss } }
        
        \put(120,30){{  Kummer }}
        
        \put(205,0){{  Bessel}}
        
        \put(205,65){{  Weber}}
        
        \put(270,30){{  Airy}}
        
        \put(80,32){\vector(1,0){38}}
        \put(180,36){\vector(2,1){38}}
        \put(180,30){\vector(2,-1){38}}
        \put(225,10){\vector(2,1){38}}
        \put(225,56){\vector(2,-1){38}}
     \end{picture}\label{digconti}$$

Recently, Y. Ohyama [@Ohyama] shows that there exists "the digeneration diagram" of Heine's series [\[heine\]](#heine){reference-type="eqref" reference="heine"} as follows: $$\begin{picture}(370,70)(0,0)
        \put(20,30){{  $ _2 \varphi_1(a,b;c;z)$ } }
        \put(110,30){{ $ _1 \varphi_1(a;c;z)$   }}
        \put(200,5){{ $ _1 \varphi_1(a;0;z)$   }}
        \put(205,55){{ $J_\nu^{(3)}$  }}
        
        \put(205,30){{$J_\nu^{(1)},J_{\nu}^{(2)} $}}
        \put(270,55){{  $q$-Airy}}
        \put(270,18){{ Ramanujan}}
        \put(90,32){\vector(1,0){20}}
        \put(170,36){\vector(3,2){27}}
        \put(170,32){\vector(1,0){27}}
        \put(230,55){\vector(1,0){27}}
        \put(170,28){\vector(3,-2){27}}
        \put(260,8){\vector(2,1){12}}
        \put(244,32){\vector(3,-1){27}}
     \end{picture}$$ We remark that there exist three different $q$-Bessel functions $J_\nu^{(j)},j=1,2,3$[@GR] and two $q$-analogues of the Airy function. In this point, this diagram is essentially different from the diagram [\[digconti\]](#digconti){reference-type="eqref" reference="digconti"}.

Ismail has pointed out that the Ramanujan function is one of $q$-analogues of the Airy function [@Is]. The Ramanujan function appears in the third identity on p.$57$ of Ramanujan's "Lost notebook" [@Ramanujan] as follows (with $x$ replaced by $q$): $$\operatorname{A}_q(-a)=\sum_{n\ge 0}\frac{a^nq^{n^2}}{(q;q)_n}=
\prod_{n\ge 1}\left(1+\frac{aq^{2n-1}}{1-q^ny_1-q^{2n}y_2-q^{3n}y_3-\cdots }\right)$$ where $$\begin{aligned}
y_1&=\frac{1}{(1-q)\psi^2(q)},\\
y_2&=0,\\
y_3&=\frac{q+q^3}{(1-q)(1-q^2)(1-q^3)\psi^2(q)}
-\frac{\sum_{n\ge 0}\frac{(2n+1)q^{2n+1}}{1-q^{2n+1}}}{(1-q)^3\psi^6(q)},\\
y_4&=y_1y_3,\\
\psi (q)&=\sum_{n\ge 0}q^{\frac{n(n+1)}{2}}=\frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}.\\
\end{aligned}$$ To be precise, the Ramanujan function is given by $$A_q(x):=\sum_{n\ge 0}\frac{q^{n^2}}{(q;q)_n}(-x)^n.$$ This function satisfies the following second order linear $q$-difference equation; $$qxu(q^2x)-u(qx)+u(x)=0.
\label{ramanujaneq}$$ The equation [\[ramanujaneq\]](#ramanujaneq){reference-type="eqref" reference="ramanujaneq"} has another solution which is given by a divergent series $$\theta_q(x){}_2\varphi_0\left(0,0;-;q,-\frac{x}{q}\right)
=\theta_q(x)\sum_{n\ge 0}\frac{1}{(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{-1}\left(-\frac{x}{q}\right)^n.$$ Here, $\theta_q(\cdot )$ is the theta function of Jacobi (see the section 2).

An asymptotic formula for the Ramanujan function is obtained by M. E. H. Ismail and C. Zhang as follows[@IZ]; $$\operatorname{A}_q(x)=\frac{(qx,q/x;q^2)_\infty}{(q;q^2)_\infty}{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)-\frac{q(q^2x,1/x;q^2)_\infty}{(1-q)(q;q^2)_\infty}{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\label{Is-Zh}$$ From the viewpoint of connection problems on $q$-difference equations, we can regard the formula [\[Is-Zh\]](#Is-Zh){reference-type="eqref" reference="Is-Zh"} as one of connection formulae of the Ramanujan function.

The other $q$-analogue of the Airy function is known as the $q$-Airy function $\operatorname{Ai}_q(\cdot )$. The $q$-Airy function has found in the study of the second $q$-Painlevé equation[@hama]. The function $\operatorname{Ai}_q(\cdot )$ is defined by $$\operatorname{Ai}_q(x):=\sum_{n\ge 0}\frac{1}{(-q;q)_n(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}(-x)^n$$ and satisfies the following $q$-difference equation $$u(q^2x)+xu(qx)-u(x)=0.\label{qairy}$$ The other solution of the equation [\[qairy\]](#qairy){reference-type="eqref" reference="qairy"} around the origin is given by $$u(x)=\frac{\theta_q(q^2x)}{\theta_q(-q^2x)}\operatorname{Ai}_q(-x).$$ Ismail also has pointed out the Ramanujan function and the $q$-Airy function are different. But the relation between them has not known. In the section 3, we give the connection formula between these functions with using the $q$-Borel-Laplace transformations of the second kind.

**Theorem** *For any* $x\in\mathbb{C}^*$, we have $$\operatorname{A}_{q^2}\left(-\frac{q^3}{x^2}\right)
=
\frac{1}{(q,-1;q)_\infty}\left\{\theta\left(\frac{x}{q}\right)\operatorname{Ai}_q(-x)
+\theta \left(-\frac{x}{q}\right)\operatorname{Ai}_q (x)\right\}.$$

Connection problems on linear $q$-difference equations between the origin and the infinity are studied by G. D. Birkhoff [@Birkhoff]. The first example of the connection formula was found by G. N. Watson [@W] in 1912. This formula is known as "Watson's formula for ${}_2\varphi_1(a,b;c;q,x)$" as follows [@GR]; $$\begin{aligned}
\label{wato}
{}_2 \varphi_1\left(a,b;c;q;x \right)= 
\frac{(b,c/a;q)_\infty (a x,q/ a x;q)_\infty }{(c, b/a;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(a,aq/c;aq/b;q;cq/abx \right) \nonumber \\+ 
\frac{(a,c/b;q)_\infty (b x, q/ b x;q)_\infty }{(c, a/b;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(b, bq/c; bq/a; q; cq/abx \right).
\end{aligned}$$ But other connection formulae had not found for a long time. Recently, C. Zhang gives connection formulae for some confluent type basic hypergeometric series [@Z0; @Z1; @Z2]. In [@Z1], Zhang gives a connection formula of Jackson's first and second $q$-Bessel function $J_\nu^{(j)}(x;q), (j=1,2)$; $$J_\nu^{(1)}(x;q):=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu\sum_{n\ge 0}\frac{1}{(q^{\nu +1};q)_n}\left(-\frac{x^2}{4}\right)^n$$and $$J_\nu^{(2)}(x;q):=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu\sum_{n\ge 0}\frac{q^{n^2}}{(q^{\nu +1};q)_n}\left(-\frac{q^\nu x^2}{4}\right)^n$$ with using the $q$-Borel-Laplace transformations of the second kind $\mathcal{B}_q^-$ and $\mathcal{L}_q^-$. These transformations are defined for a formal power series $f(x)=\sum_{n\ge 0}a_nx^n$, $a_0=1$ as follow;

1.  The $q$-Borel transformation of the second kind is $$(\mathcal{B}_q^-f)(\xi ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\xi^n\left(=:g(\xi )\right).$$

2.  The $q$-Laplace transformation of the second kind is $$\left(\mathcal{L}_q^-g\right)(x):=\frac{1}{2\pi i}\int_{|\xi |=r}g(\xi )\theta_q\left(\frac{x}{\xi }\right)\frac{d\xi}{\xi},$$ where $r>0$ is enough small number.

In [@M0] and [@M1], we obtained connection formulae of the Hahn-Exton $q$-Bessel function $$J_\nu^{(3)}(x;q):=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}x^\nu\sum_{n\ge 0}\frac{q^{\frac{n(n+1)}{2}}}{(q^{\nu +1};q)_n}\left(-x^2\right)^n$$ and the $q$-confluent type basic hypergeometric function $${}_1\varphi_1(a;b;q,x):=\sum_{n\ge 0}\frac{(a;q)_n}{(b;q)_n(q;q)_n}(-1)^nq^{\frac{n(n-1)}{2}}x^n$$ by these transformations. In section 3, we use these transformations to obtain connection formula between the Ramanujan function and the $q$-Airy function.

On the other hand, the $q$-Borel-Laplace transformations of the first kind are defined for a formal power series as follow;

1.  The $q$-Borel transformation of the first kind is $$\left(\mathcal{B}_q^+f\right)(\xi ):=\sum_{n\ge 0}a_nq^{\frac{n(n-1)}{2}}\xi^n\left(=:\varphi (\xi )\right).$$

2.  The $q$-Laplace transformation of the first kind is $$\left(\mathcal{L}_q^+\varphi\right)(x):=
    \frac{1}{1-q}\int_0^{\lambda\infty}\frac{\varphi (\xi )}{\theta_q\left(\frac{\xi}{x}\right)}\frac{d_q\xi}{\xi}=\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta_q\left(\frac{\lambda q^n}{x}\right)},$$ here, this transformation is given by Jackson's $q$-integral [@GR].

These two different types of $q$-Borel-Laplace transformations are introduced by J. Sauloy [@sauloy] and stusied by C. Zhang. We remark that each $q$-Borel transformation is formal inverse of each $q$-Laplace transformation, i.e., $$\mathcal{L}_q^{\pm}\circ\mathcal{B}_q^{\pm}f=f.$$ The application of the $q$-Borel-Laplace transformations of the first kind is found in [@Z0; @Z2]. Zhang gives the connection formula of the divergent basic hypergeometric series ${}_2\varphi_0(a,b;-;q,x)$ as follows;

**Theorem** (Zhang, [@Z0]) *For any $x\in\mathbb{C}^*$, we have* $$\begin{aligned}
{}_2f_0&(a,b;\lambda ,q,x)\\
=&\frac{(b;q)_\infty}{(b/a;q)_\infty}\frac{\theta_q(a\lambda )}{\theta_q(\lambda )}\frac{\theta_q(qax/\lambda )}{\theta_q(\lambda /x)}{}_2\varphi_1\left(a,0;\frac{aq}{b};q,\frac{q}{abx}\right)\\
+&\frac{(a;q)_\infty}{(a/b;q)_\infty}\frac{\theta_q(b\lambda )}{\theta_q(\lambda )}\frac{\theta_q(qbx/\lambda )}{\theta_q(\lambda /x)}{}_2\varphi_1\left(b,0;\frac{bq}{a};q,\frac{q}{abx}\right)
\end{aligned}$$ *where $\lambda\in\mathbb{C}^*\setminus \{-q^n;n\in\mathbb{Z}\}$.*

Here, ${}_2f_0(a,b;\lambda ,q,x)$ in the left-hand side is the $q$-Borel-Laplace transform of the function ${}_2\varphi_0(a,b;-;q,x)$. But other application of this method (of the first kind ) has not known. In the section 4, we show the connection formula of the divergent series $${}_2\varphi_0(a,b;-;q,x)=\sum_{n\ge 0}\frac{1}{(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{-1}x^n.$$ This formula is given by the following theorem;

**Theorem** *For any $x\in\mathbb{C}^*\setminus [-\lambda ;q]$,* $$\begin{aligned}
\theta_q(x){}_2f_0\left(0,0;-;q,-\frac{x}{q}\right)&=(q;q)_\infty\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{qx}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}
{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)\\
&+\frac{(q;q)_\infty}{1-q}\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{x}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\frac{\lambda}{x}
{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$
