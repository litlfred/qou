---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.935
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
In this papar, we deal with the Ramanujan equation $$qxu(q^2x)-u(qx)+u(x)=0,\qquad \forall x\in\mathbb{C}^*.
\label{ramanujaneq}$$ We assume that $0<|q|<1$. The Ramanujan equation [\[ramanujaneq\]](#ramanujaneq){reference-type="eqref" reference="ramanujaneq"} has solutions $$\begin{aligned}
u_1(x)&={}_0\varphi_1(-;0;q,-qx), \\
u_2(x)&=\theta_q(x){}_2\varphi_0\left(0,0;-;q,-\frac{x}{q}\right)\label{secondram}
\end{aligned}$$ around the origin. The equation [\[ramanujaneq\]](#ramanujaneq){reference-type="eqref" reference="ramanujaneq"} also has a fundamental system of solutions around the infinity [@IZ]: $$\begin{aligned}
v_1(x)&=\frac{\theta_q(x)}{\theta_{q^2}(x)}{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)\\
v_2(x)&=\frac{q}{q-1}\frac{\theta_q(x/q)}{\theta_{q^2}(x/q)}\frac{1}{x}{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$ Here, the function ${}_r\varphi_s(a_1,\dots ,a_r;b_1,\dots ,b_s;q,x)$ is the basic hypergeometric series with the base $q$ [@GR]: $$\begin{aligned}
{}_r\varphi_s(a_1,\dots ,a_r&;b_1,\dots ,b_s;q,x)\\
&:=\sum_{n\ge 0}\frac{(a_1,\dots ,a_r;q)_n}{(b_1,\dots ,b_s;q)_n(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{1+s-r}x^n.
\end{aligned}$$ The notation $(a;q)_n$ is the $q$-shifted factorial; $$(a;q)_n:=
\begin{cases}
1, &n=0, \\
(1-a)(1-aq)\dots (1-aq^{n-1}), &n\ge 1,
\end{cases}$$ moreover, $(a;q)_\infty :=\lim_{n\to \infty}(a;q)_n$ and $$(a_1,a_2,\dots ,a_m;q)_\infty:=(a_1;q)_\infty (a_2;q)_\infty \dots (a_m;q)_\infty.$$ The basic hypergeometric series has radius of convergence $\infty , 1$ or $0$ according to whether $r-s<1, r-s=1$ or $r-s>1$. We remark that the solution $u_2(x)$ contains a divergent series and other solutions $u_1(x)$, $v_1(x)$ and $v_2(x)$ are convergent series. We study the relation between these solutions from the viewpoint of connection problems on linear $q$-difference equations. The function $\theta_q(x)$ is the theta function of Jacobi with the base $q$ (see section two for more details).

The solution $u_1(x)$ is called the Ramanujan function, which has found by Ramanujan [@Ramanujan].

M. E. H. Ismail [@IZ] has introduced the notation $$\operatorname{A}_q(x):=\sum_{n\ge 0}\frac{q^{n^2}}{(q;q)_n}(-x)^n= {}_0\varphi_1(-;0;q,-qx).$$ He shows that $\operatorname{A}_q(x)$ is one of $q$-analogues of the Airy function [@Is]. The Ramanujan function $\operatorname{A}_q(x)$ appears in the third identity on p.$57$ of Ramanujan's "Lost notebook" [@Ramanujan] as follows (with $x$ replaced by $q$): $$\operatorname{A}_q(-a)=\sum_{n\ge 0}\frac{a^nq^{n^2}}{(q;q)_n}=
\prod_{n\ge 1}\left(1+\frac{aq^{2n-1}}{1-q^ny_1-q^{2n}y_2-q^{3n}y_3-\cdots }\right)$$ where $$\begin{aligned}
y_1&=\frac{1}{(1-q)\psi^2(q)},\\
y_2&=0,\\
y_3&=\frac{q+q^3}{(1-q)(1-q^2)(1-q^3)\psi^2(q)}
-\frac{\sum_{n\ge 0}\frac{(2n+1)q^{2n+1}}{1-q^{2n+1}}}{(1-q)^3\psi^6(q)},\\
y_4&=y_1y_3,\\
\psi (q)&=\sum_{n\ge 0}q^{\frac{n(n+1)}{2}}=\frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}.\\
\end{aligned}$$

Strictly speaking, Ramanujan has not shown that the Ramanujan function $\operatorname{A}_q(x)$ satisfies the equation [\[ramanujaneq\]](#ramanujaneq){reference-type="eqref" reference="ramanujaneq"}. But we propose that the equation [\[ramanujaneq\]](#ramanujaneq){reference-type="eqref" reference="ramanujaneq"} is named "the Ramanujan equation" after his study.

We review some $q$-special functions and connection formulae of these functions. Recently, Y. Ohyama [@Ohyama] shows that there exists "the digeneration diagram" for Heine's series ${}_2\varphi_1(a,b;c;q,x)$: $$\begin{picture}(370,70)(0,0)
        \put(20,30){{  $ _2 \varphi_1(a,b;c;z)$ } }
        \put(110,30){{ $q$-confluent   }}
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
     \end{picture}
\label{qdegenerate}$$

We remark that there exist three different types of $q$-Bessel functions $J_\nu^{(j)},j=1,2,3$ [@GR] and two $q$-analogues of the Airy function. These $q$-analogue are solutions of different types of linear $q$-difference equations. In this point, this diagram is essentially different from the differential case: $$\begin{picture}(370,70)(0,0)
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

The Ramanujan function is the most degenerated case in the diagram [\[qdegenerate\]](#qdegenerate){reference-type="eqref" reference="qdegenerate"}. We study connection problems on linear $q$-difference equations between around the origin and around the infinity with irregular singular points. The irregularity of $q$-difference equations and $q$-difference modules for some cases of slopes of the Newton polygons are studied by J.-P. Ramis, J. Sauloy and C. Zhang [@RSZ]. Graphically, these (formal) invariants are the height of the right part of the Newton polygon, from the bottom to the upper right end. In this paper, we show connection formulae for the Ramanujan equation. Connection problems on linear $q$-difference equations between the origin and the infinity are studied by G. D. Birkhoff [@Birkhoff].

Connection formulae of second order linear $q$-difference equations are linear relations in a matrix form: $$\begin{pmatrix}
u_1(x)\\
u_2(x)
\end{pmatrix}
=
\begin{pmatrix}
C_{11}(x)&C_{12}(x)\\
C_{21}(x)&C_{22}(x)
\end{pmatrix}
\begin{pmatrix}
v_1(x)\\
v_2(x)
\end{pmatrix}.$$ Here, $u_1(x)$ and $u_2(x)$ are solutions around the origin, $v_1(x)$ and $v_2(x)$ are solutions around infinity and $C_{ij}$ $(1\le i,j\le 2)$ are doubly periodic functions such that $$\sigma_qC_{ij}(x)=C_{ij}(x),\quad C_{ij}(e^{2\pi i}x)=C_{ij}(x),$$ namely, $q$-elliptic functions. The first example of the connection formula with regular singular points was found by G. N. Watson [@W] in 1912: $$\begin{aligned}
\label{wato}
{}_2 \varphi_1\left(a,b;c;q;x \right)= 
\frac{(b,c/a;q)_\infty (a x,q/ a x;q)_\infty }{(c, b/a;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(a,aq/c;aq/b;q;cq/abx \right) \nonumber \\+ 
\frac{(a,c/b;q)_\infty (b x, q/ b x;q)_\infty }{(c, a/b;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(b, bq/c; bq/a; q; cq/abx \right).\notag
\end{aligned}$$ But connection formulae for irregular singular case had not found for a long time. Recently, C. Zhang gives connection formulae for some confluent type basic hypergeometric series [@Z0; @Z1; @Z2]. In [@Z1], Zhang gives a connection matrix of Jackson's first and second $q$-Bessel function $J_\nu^{(j)}(x;q), (j=1,2)$ [@GR] with using the $q$-Borel-Laplace transformations of the second kind. Zhang also gives the connection formula for the divergent seties ${}_2\varphi_0(a,b;-;q,x)$ in [@Z0; @Z2] with using the $q$-Borel-Laplace transformations of the first kind. These resummation method are powerful tools for connection problems with irregular singular points. We define these transformations later.

The connection formula for the solution [\[secondram\]](#secondram){reference-type="eqref" reference="secondram"}, i.e., $u_2(x)$ has not known. We remark that the basic hypergeometric part ${}_2\varphi_0(0,0;-;q,-x/q)$ in this solution is a divergent series around the origin and the $q$-Stokes phenomenon occurs [@sauloy]. Therefore, we need a suitale resummation method, which is the $q$-Borel-Laplace transformations of the first kind. By this resummation method, we obtain the following connection formula in the matrix form exactly and solve the connection problem on the Ramanujan equation.

**Theorem.** *For any $x\in\mathbb{C}^*\setminus [-\lambda ;q]$, we have* $$\begin{pmatrix}
u_1(x)\\
\tilde{u}_2(x,\lambda )
\end{pmatrix}
=
\begin{pmatrix}
C_{11}(x)&C_{12}(x)\\
\tilde{C}_{21}(x)&\tilde{C}_{22}(x)
\end{pmatrix}
\begin{pmatrix}
v_1(x)\\
v_2(x)
\end{pmatrix},$$ *provided that* $$C_{11}(x)=\frac{\theta_{q^2}(qx)\theta_{q^2}(x)}{(q,q^2;q^2)_\infty\theta_q(x)}, \quad 
C_{12}(x)=\frac{\theta_{q^2}(x)\theta_{q^2}(x/q)}{(q,q^2;q^2)_\infty\theta_q(x/q)},$$ $$\tilde{C}_{21}(x)=\frac{(q;q)_\infty\theta_{q^2}(-qx/\lambda^2)\theta_{q^2}(x)}{\theta_q(-q/\lambda )\theta_q(x/\lambda )\theta_q(x)}$$ *and* $$\tilde{C}_{22}(x)=\frac{(q;q)_\infty\theta_{q^2}(-x/\lambda^2)\theta_{q^2}(x/q)}{\theta_q(-1/\lambda )\theta_q(x/\lambda )\theta_q(x/q)}.$$ *Here, the function $\tilde{u}_2(x,\lambda )$ is* $$\tilde{u}_2(x,\lambda )=\theta_q(x){}_2f_0(0,0;-;q,\lambda ,-x/q)$$ *which is meromorphic function on $\mathbb{C}^*\setminus [-\lambda ;q]$ and the set $[\lambda ;q]$ is the $q$-spiral(see section two). We denote ${}_2f_0(0,0;-;q,\lambda ,-x/q)$ as the resummation of ${}_2\varphi_0(0,0;-;q,-x/q)$.*

We show this formula with the using of the $q$-Borel-Laplace method of the first kind. The connection formula between the Ramanujan function and the $q$-Airy function has given with the using of the $q$-Borel-Laplace method of the second kind.

**Theorem** (Morita[@M0]) *For any* $x\in\mathbb{C}^*$, we have $$\operatorname{A}_{q^2}\left(-\frac{q^3}{x^2}\right)
=
\frac{1}{(q,-1;q)_\infty}\left\{\theta_q\left(\frac{x}{q}\right)\operatorname{Ai}_q(-x)
+\theta_q \left(-\frac{x}{q}\right)\operatorname{Ai}_q (x)\right\}.\label{ram-qairy}$$

Here, the function $\operatorname{Ai}_q(x )$ is the $q$-Airy function, which is another $q$-analogue of the Airy function. The $q$-Airy function $\operatorname{Ai}_q(x )$ is found as a special solution of the second $q$-Painlevé equation by K. Kajiwara, T. Masuda, M. Noumi, Y. Ohta and Y. Yamada [@hama; @KMNOY] . The function $\operatorname{Ai}_q(x)$ is defined by

$$\operatorname{Ai}_q(x):=\sum_{n\ge 0}\frac{1}{(-q;q)_n(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}(-x)^n.$$

These functions $\operatorname{A}_q(x)$ and $\operatorname{Ai}_q(x)$ are most degenerated case in the diagram for Heine's ${}_2\varphi_1(a,b;c;q,x)$ series [\[qdegenerate\]](#qdegenerate){reference-type="eqref" reference="qdegenerate"} and satisfy different two types of second order $q$-difference equations. The Ramanujan function $\operatorname{A}_q(x)$ satisfies $$qxu(q^2x)-u(qx)+u(x)=0$$ and the $q$-Airy function $\operatorname{Ai}_q(x)$ satisfies $$u(q^2x)+xu(qx)-u(x)=0.$$

Ismail also has pointed out the Ramanujan function and the $q$-Airy function are different. But the relation between them has not known. Our connection formula [\[ram-qairy\]](#ram-qairy){reference-type="eqref" reference="ram-qairy"} shows that the Ramanujan function can be represented by the $q$-Airy functions.

We remark that the connection formula for $u_1(x)$ is essentially given by Ismail and C. Zhang as follows [@IZ]:

$$\begin{aligned}
\operatorname{A}_q(x)&=\frac{(qx,q/x;q^2)_\infty}{(q;q^2)_\infty}{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)\notag\\
&-\frac{q(q^2x,1/x;q^2)_\infty}{(1-q)(q;q^2)_\infty}{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\label{Is-Zh}
\end{aligned}$$ They give [\[Is-Zh\]](#Is-Zh){reference-type="eqref" reference="Is-Zh"} as an asymptotic formula for the Ramanujan function. But from the viewpoint of connection problems on $q$-difference equations, we can regard the formula [\[Is-Zh\]](#Is-Zh){reference-type="eqref" reference="Is-Zh"} as one of connection formulae of the Ramanujan function. In fact, we can rewrite this formula as follows: $$\begin{aligned}
u(x)=\frac{\theta_{q^2}(qx)\theta_{q^2}(x)}{(q,q^2;q^2)_\infty \theta_q(x)}v_1(x)+\frac{\theta_{q^2}(x)\theta_{q^2}(x/q)}{(q,q^2;q^2)_\infty \theta_q(x/q)}v_2(x).
\end{aligned}$$ Here, connection coefficients are $q^2$-elliptic functions. In [@M0], we derive Ismail-Zhang's formula [\[Is-Zh\]](#Is-Zh){reference-type="eqref" reference="Is-Zh"} from [\[ram-qairy\]](#ram-qairy){reference-type="eqref" reference="ram-qairy"} by suitable algebraic transformation.

In the last section, we introduce the $q$-Borel-Laplace transformations of level $r-1$. These transformations are higher order extension of the $q$-Borel-Laplace transformations. We also apply these new method to a divergent series ${}_r\varphi_0(0,0,\dots ,0;-;q,x)$ and give the asymptotic formula as follows:

**Theorem.** For any $\mathbb{C}^*\setminus [-\lambda ;q^{r-1}]$, we have $$\begin{aligned}
&\left(\mathcal{L}_{q^{r-1,\lambda}}^+\circ \mathcal{B}_{q^{r-1}}^+{}_r\varphi_0(0,0,\dots ,0;-;q,x)\right)\notag\\
&=\frac{1}{\theta_{q^{r-1}}\left(\frac{\lambda}{x}\right)}\frac{(q;q)_\infty}{\theta_q(-\lambda )}\theta_{q^{r(r-1)}\left((-1)^{r-1}q^{\frac{(r-1)(r-2)}{2}}\left(\frac{\lambda}{x}\right)^r\right)}\notag\\
&\times{}_{r-1}\varphi_{r-1}\left(0,0,\dots ,0;q,q^2,\dots ,q^{r-1};q^r,q^{\frac{(r-1)(r-2)}{2}}/x\right)\notag\\
&+\dots \notag\\
&+\frac{1}{\theta_{q^{r-1}}\left(\frac{\lambda}{x}\right)}\frac{(q;q)_\infty}{\theta_q(-\lambda )}\theta_{q^{r(r-1)}\left((-1)^{r-1}q^{\frac{3r(r-1)}{2}}\left(\frac{\lambda}{x}\right)^r\right)}\notag\\
&\times \frac{(-1)^{r-1}q^{\frac{(r-1)(r-2)}{2}}}{(1-q)(1-q^2)\dots (1-q^{r-1})}\left(\frac{q}{\lambda}\right)^{r-1}\notag\\
&\times{}_{r-1}\varphi_{r-1}\left(0,0,\dots ,0;q^r,q^{r+1},\dots ,q^{2r-1};q^r,q^{\frac{3r(r-1)}{2}}/x\right)\notag
\end{aligned}$$
