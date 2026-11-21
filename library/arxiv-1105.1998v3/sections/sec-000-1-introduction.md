---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
toc_source: outline
text_source: latex
latex_prose_ratio: 0.77
latex_coverage_ratio: 0.896
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
In this paper, we show a connection formula of the Hahn--Exton $q$-Bessel function $J_\nu^{(3)}(x;q)$. At first, we review the Bessel function and $q$-analogues of the Bessel function. The Bessel equation $$\begin{gathered}
\frac{d^2u}{dz^2}+\frac{1}{z}\frac{du}{dz}+\left(1-\frac{\nu^2}{z^2}\right)u=0
\end{gathered}$$ has a solution $u(z)=J_\nu (z)$, $J_{-\nu}(z)$. Here, the Bessel function $J_\nu (z)$ is $$J_\nu (z)=\frac{1}{\Gamma (\nu +1)}\left(\frac{z}{2}\right)^\nu{}_0F_1\left(-,\nu +1, -\frac{z^2}{4}\right).$$ The degenerated confluent hypergeometric function ${}_0F_1(-,\alpha , z)$ is defined by $${}_0F_1(-,\alpha , z)=\sum_{n\ge 0}\frac{1}{(\alpha )_n n!}z^n,\qquad (\alpha )_n=\alpha \{\alpha +1\}\cdots \{\alpha +(n-1)\}.$$ Both $J_\nu(z)$ and $J_{-\nu}(z)$ are linearly independent if $\nu\not\in\mathbb{Z}$.

It is known that there exists three different $q$-analogues of the Bessel function. $$\begin{gathered}
J_\nu^{(1)}(x;q) :=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu {}_2\varphi_1\left(0,0;q^{\nu +1};q,-\frac{x^2}{4}\right),\qquad |x|<2,\\
J_\nu^{(2)}(x;q) :=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu {}_0\varphi_1\left(-;q^{\nu +1};q,-\frac{q^{\nu -1}x^2}{4}\right),\qquad x\in\mathbb{C},\\
J_\nu^{(3)}(x;q) :=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}x^\nu {}_1\varphi_1\left(0;q^{\nu +1};q,qx^2\right),\qquad x\in\mathbb{C}.
\end{gathered}$$ Here, $$\begin{gathered}
(a;q)_n:=
\begin{cases}
1,&\quad n=0,\\
(1-a)(1-aq)\cdots (1-aq^{n-1}),&\quad n\ge 1,
\end{cases}
\\
(a;q)_\infty =\lim_{n\to\infty}(a;q)_n
\end{gathered}$$ and $$(a_1,a_2,\dots ,a_m;q)_\infty =(a_1;q)_\infty (a_2;q)_\infty\cdots (a_m;q)_\infty .$$ Moreover, the basic hypergeometric series ${}_r\varphi_s$ is $${_r\varphi_s}(a_1,\dots ,a_r;b_1,\dots ,b_s;q,x)
:=\sum_{n\ge 0}\frac{(a_1,\dots ,a_r;q)_n}{(b_1,\dots ,b_s;q)_n(q;q)_n}
\left[(-1)^nq^{\frac{n(n-1)}{2}}\right]^{1+s-r}x^n.$$

The first and the second one are called Jackson's first and second $q$-Bessel function and the third one is called the Hahn--Exton $q$-Bessel function. They satisfy the following $q$-difference equations: $$\begin{gathered}
J^{(1)}_\nu :\quad u(xq) -\big(q^{\nu/2} +q^{-\nu/2}\big) u(xq^{1/2}) +\left(1+\frac{x^2}4\right)u(x)=0,\notag 
\\
J^{(2)}_\nu :\quad \left(1+\frac{qx^2}4\right)u(xq) -\big(q^{\nu/2} +q^{-\nu/2}\big) u\big(xq^{1/2}\big) +u(x)=0,\notag \\
J^{(3)}_\nu :\quad u(xq) -\left\{(q^{\nu/2} +q^{-\nu/2}) -q^{-\nu/2+1}x^2\right\} u\big(xq^{1/2}\big) + u(x)=0. \label{j3}
\end{gathered}$$ The limits of these $q$-analogues of the Bessel function are the Bessel function when $q\to 1^-$: $$\lim_{q\to 1^-}J_\nu^{(k)}\left((1-q)x;q\right)=J_{\nu}(x),\qquad k=1,2$$ and $$\lim_{q\to 1^-}J_\nu^{(3)}\left((1-q)x;q\right)=J_\nu (2x).$$ The relation between $J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$ was found by Hahn [@Hahn] as follows: $$\begin{gathered}
\label{J1J2}
J_\nu^{(2)}(x;q)=\left(-\frac{x^2}{4};q\right)_\infty J_\nu^{(1)}(x;q).
\end{gathered}$$

Connection problems of the $q$-difference equation between the origin and the infinity are studied by G.D. Birkhoff [@Birkhoff]. We review connection formulae for several $q$-difference functions.

1.  Watson's formula. In 1910 [@W], Watson showed the connection formula of the basic hypergeometric function ${}_2\varphi_1$ as follows: $$\begin{gathered}
    {}_2 \varphi_1\left(a,b;c;q;x \right)=
    \frac{(b,c/a;q)_\infty (a x,q/ a x;q)_\infty }{(c, b/a;q)_\infty (  x,q/   x;q)_\infty }
    {}_2 \varphi_1\left(a,aq/c;aq/b;q;cq/abx \right) \nonumber \\
    \hphantom{{}_2 \varphi_1\left(a,b;c;q;x \right)=}{} +
    \frac{(a,c/b;q)_\infty (b x, q/ b x;q)_\infty }{(c, a/b;q)_\infty (  x,q/   x;q)_\infty }
    {}_2 \varphi_1\left(b, bq/c; bq/a; q; cq/abx \right).
    \end{gathered}$$

2.  Connection formula of $J_\nu^{(1)}(x;q)$. C. Zhang has given some connection formulae for the solutions of the $q$-difference equations of confluent type [@Z0; @Z1] and [@Z2]. In [@Z1], Zhang has shown connection formulae for $J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$. The connection formula of $J_\nu^{(1)}(x;q)$ is given by $$\begin{gathered}
    \frac{\left(\frac{\alpha}{\sqrt{p}x};p\right)_\infty}{\theta_p\left(-\frac{\alpha}{x}\right)}{}_2\varphi_1 \left(p^{\nu +\frac{1}{2}},p^{-\nu +\frac{1}{2}};-p;p,\frac{\alpha}{\sqrt{p}x}\right)\notag\\
    \qquad{} =\frac{1}{\theta_p\left(-\frac{\alpha}{x}\right)}
     \left\{\frac{\theta_p\left(-\frac{\alpha q^{\frac{\nu}{2}}}{x}\right)}{(q,q^{-\nu};q)_\infty}{}_2\varphi_1\left(0,0;q^{\nu +1};q,-\frac{x^2}{4}\right)\right.\notag\\
    \left.\qquad\quad{} + \frac{\theta_p\left(-\frac{\alpha q^{-\frac{\nu}{2}}}{x}\right)}{(q,q^{\nu};q)_\infty}{}_2\varphi_1\left(0,0;q^{-\nu +1};q,-\frac{x^2}{4}\right)
    \right\},\label{Zhb}
    \end{gathered}$$ where $q=p^2$ and $\alpha^2=-4q^{3/2}$.

The connection formula of $J_\nu^{(2)}(x;q)$ is obtained by ([\[Zhb\]](#Zhb){reference-type="ref" reference="Zhb"}) and ([\[J1J2\]](#J1J2){reference-type="ref" reference="J1J2"}). But it is not known the connection formula of the Hahn--Exton $q$-Bessel function.

The Hahn--Exton $q$-Bessel equations ([\[j3\]](#j3){reference-type="ref" reference="j3"}) has two analytic solutions $u(x)=J_\nu^{(3)}(x)$, $J_{-\nu}^{(3)}(xp^{-\nu})$ around $x=0$ and has one analytic solution $z\left(1/x\right)
=\frac{1}{\theta_p\left(-p^{\nu +2}/x\right)}\sum\limits_{n\ge 0}a_nx^{-n}$, $a_0=1$. We show a connection formula of $J_\nu^{(3)}(x;q)$ in Section [\[section2\]](#section2){reference-type="ref" reference="section2"} as follows:

::: theorem
[]{#theorem1 label="theorem1"} For any $x\in\mathbb{C}^*\setminus [p^{\nu +2};p]$, $$\begin{gathered}
z\left(\frac{1}{x}\right) =\frac{1}{(p^{-2\nu},p;p)_\infty}\frac{\theta
_p\left(-\frac{p^{2\nu +2}}{x}\right)}{
\theta_p\left(-\frac{p^{\nu +2}}{x}\right)}\
_1\varphi_1\left(0,p^{1+2\nu};p,x\right)\notag\\
\phantom{z\left(\frac{1}{x}\right) =}{} +\frac{1}{(p^{2\nu},p;p)_\infty}\frac{\theta _p\left(-\frac{p^2}{x}\right)}{
\theta_p\left(-\frac{p^{\nu +2}}{x}\right)}\
_1\varphi_1\left(0,p^{1-2\nu};p,p^{-2\nu}x\right).\label{thm1}
\end{gathered}$$
:::

Here, $\theta_p(\cdot )$ is the theta function of Jacobi and $[\lambda ;q]$ is the $q$-spiral (see Section [\[section2\]](#section2){reference-type="ref" reference="section2"}). We use the $q$-Borel transformation and the $q$-Laplace transformation which is defined by C. Zhang in [@Z1].

In Section [\[section3\]](#section3){reference-type="ref" reference="section3"}, we consider the limit $p\to 1^-$ of the connection formula. If we take a suitable limit $p\to 1^-$ of ([\[thm1\]](#thm1){reference-type="ref" reference="thm1"}), we obtain $$H_\nu^{(2)}\left(\sqrt{z}\right)=\frac{-ie^{\nu\pi i}}{\sin\nu\pi}\left\{J_\nu\left(\sqrt{z}\right)-e^{-\nu\pi i}J_{-\nu}\left(\sqrt{z}\right)\right\}.$$ Here, $H_\nu^{(2)}(z)$ is the Hankel function of the second kind. Thus we obtain a connection formula of the Bessel function as a limit $p\to 1^-$ of ([\[thm1\]](#thm1){reference-type="ref" reference="thm1"}).
