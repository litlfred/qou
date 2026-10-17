---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q -Airy function"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.877
doc_brief: "A connection formula between the Ramanujan function and the q -Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
In the study of the $q$-analysis, it is known that there exist several different $q$-special functions corresponding to a special function defined by a differential equation. For example, three types of $q$-Bessel functions are known. We denote them $J_\nu^{(1)}(x;q)$, $J_\nu^{(2)}(x;q)$ and $J_\nu^{(3)}(x;q)$ due to Ismail [@Is]. The first and the second one are called Jackson's first and second $q$-Bessel function and the third one is called the Hahn-Exton $q$-Bessel function. Similarly, two types of $q$-Airy functions are known. We denote them $\operatorname{A}_q(x)$ and $\operatorname{Ai}_q(x)$. The first one is called the Ramanujan function and the second one is called the $q$-Airy function.

Three $q$-Bessel functions are given by $$\begin{aligned}
J_\nu^{(1)}(x;q)&:=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu\sum_{n\ge 0}\frac{1}{(q^{\nu +1};q)_n}\left(-\frac{x^2}{4}\right)^n,\\
J_\nu^{(2)}(x;q)&:=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}\left(\frac{x}{2}\right)^\nu\sum_{n\ge 0}\frac{q^{n^2}}{(q^{\nu +1};q)_n}\left(-\frac{q^\nu x^2}{4}\right)^n,\\
J_\nu^{(3)}(x;q)&:=\frac{(q^{\nu +1};q)_\infty}{(q;q)_\infty}x^\nu\sum_{n\ge 0}\frac{q^{\frac{n(n+1)}{2}}}{(q^{\nu +1};q)_n}\left(-x^2\right)^n.\\
\end{aligned}$$

The Ramanujan function and the $q$-Airy function are defined by $$\begin{aligned}
\operatorname{A}_q(x)&:=\sum_{n\ge 0}\frac{q^{n^2}}{(q;q)_n}(-x)^n,\\
\operatorname{Ai}_q(x)&:=\sum_{n\ge 0}\frac{1}{(-q,q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}(-x)^n.
\end{aligned}$$

Here, $(a;q)_n$ and $(a;q)_\infty$ are the $q$-Pochhammer symbol defined in section two. According to [@Andre] , the Ramanujan function $\operatorname{A}_q(x)$ appears in the third identity on p.$57$ of Ramanujan's \"Lost notebook\" [@Ramanujan] as follows (with $x$ replaced by $q$): $$\operatorname{A}_q(-a)=\sum_{n\ge 0}\frac{a^nq^{n^2}}{(q;q)_n}=
\prod_{n\ge 1}\left(1+\frac{aq^{2n-1}}{1-q^ny_1-q^{2n}y_2-q^{3n}y_3-\cdots }\right)$$ where $$\begin{aligned}
y_1&=\frac{1}{(1-q)\psi^2(q)},\\
y_2&=0,\\
y_3&=\frac{q+q^3}{(1-q)(1-q^2)(1-q^3)\psi^2(q)}
-\frac{\sum_{n\ge 0}\frac{(2n+1)q^{2n+1}}{1-q^{2n+1}}}{(1-q)^3\psi^6(q)},\\
y_4&=y_1y_3,\\
\psi (q)&=\sum_{n\ge 0}q^{\frac{n(n+1)}{2}}=\frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}.\\
\end{aligned}$$

Ismail has pointed out that the Ramanujan function is a $q$-analogue of the Airy function [@Is]. We show more detail about these functions in section three.

It is known that there exist a relation for the $q$-Bessel functions and the $q$-Airy function. One is a relation between Jackson's first and second $q$-Bessel function [@Hahn] : $$J_\nu^{(2)}(x;q)=\left(-\frac{x^2}{4};q\right)_\infty J_\nu^{(1)}(x;q).\label{ha}$$ Another is a relation between the Hahn-Exton $q$-Bessel function and the $q$-Airy function [@Oyama] : $$J_\nu^{(3)}(x;q)=\frac{(-q;q)_\infty}{(q;q)_\infty}x^\nu\operatorname{Ai}_q(-qx^2),\label{oh}$$ where $q^{\nu}=-1$.

Other relations are not known. The main result in this paper is a relation between two $q$-Airy functions. It is not known any relation between the Ramanujan function and the $q$-Airy function, but these two functions are related by a connection formula and not by algebraic relation like ([\[ha\]](#ha){reference-type="ref" reference="ha"}) or ([\[oh\]](#oh){reference-type="ref" reference="oh"}).

Connection problems of linear $q$-difference equations between the origin and the infinity are studied by G. D. Birkhoff [@Birkhoff]. Watson gave a connection formula for the basic hypergeometric equation ${}_2\varphi_1$ in $1910$ [@W]:

$$\begin{aligned}
{}_2 \varphi_1\left(a,b;c;q,x \right)=&
\frac{(b,c/a;q)_\infty (a x,q/a x;q)_\infty }{(c, b/a ;q)_\infty (  x,q/x ;q)_\infty } 
{}_2 \varphi_1\left(a,aq/c;aq/b;q,cq/abx \right) \nonumber \\
&+ 
\frac{(a,c/b;q)_\infty (b x, q/ b x;q)_\infty }{(c, a/b;q)_\infty (  x,q/   x;q)_\infty } 
{}_2 \varphi_1\left(b, bq/c; bq/a; q, cq/abx \right). 
\end{aligned}$$

Recently, C. Zhang has given some connection formulae of $q$-difference equations of the confluent type [@Z0], [@Z1] and [@Z2]. Zhang gives a connection formula of Jackson's $q$-Bessel function $J_\nu^{(1)}(x;q)$ [@Z2]. In [@Z2], Zhang introduced the $q$-Borel transformation and the $q$-Laplace transformation which are useful to study connection problems. In section four, we apply Zhang's method to the $q$-Airy functions.

The connection formula of the $q$-Airy function gives a relation between the Ramanujan function and the $q$-Airy function as follows:

::: thm
For any $x\in\mathbb{C}^*$, $$\operatorname{A}_{q^2}\left(-\frac{q^3}{x^2}\right)
=\frac{1}{(q,-1;q)_\infty}
\left\{\theta \left(\frac{x}{q}\right)\operatorname{Ai}_q(-x)+\theta\left(-\frac{x}{q}\right)\operatorname{Ai}_q(x)\right\}.$$
:::

Since our new relation shows an asymptotic behavior of the Ramanujan function near the infinity, it may be useful to study the Ramanujan function or similar type $q$-series.
