---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-004-5-the-ramanujan-function-and-the-q-airy-function
section_title: "The Ramanujan function and the q-Airy function"
section_number: 5
pages: 11-13
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
There are two different $q$-analogue of the Airy function. One is called the Ramanujan function which appears in [@Ramanujan]. Ismail [@Is] pointed out that the Ramanujan function can be considered as a $q$-analogue of the Airy function. The other one is called the $q$-Airy function which is obtained by K. Kajiwara, T. Masuda, M. Noumi, Y. Ohta and Y. Yamada [@KMNOY]. In this section, we see the properties of these functions. We explain the reason why they are called $q$-analogues of the Airy function and we show $q$-difference equations which they satisfy.The Ramanujan function appears in Ramanujan's "Lost notebook" [@Ramanujan]. Ismail has pointed out that the Ramanujan function can be considered as a $q$-analogue of the Airy function. The Ramanujan function is defined by following convergent series; $$\operatorname{A}_q(x):=\sum_{n\ge 0}\frac{q^{n^2}}{(q;q)_n}(-x)^n
={_0\varphi_1}(-;0;q,-qx).$$

In the theory of ordinary differencial equations, the term Plancherel-Rotach asymptotics refers to asymptotics around the largest and smallest zeros. With $x=\sqrt{2n+1}-2^{\frac{1}{2}}3^{\frac{1}{3}}n^{\frac{1}{6}}t$ and for $t\in\mathbb{C}$, the Plancherel-Rotach asymptotic formula for Hermite polynomials $H_n(x)$ is $$\lim_{n\to +\infty}\frac{e^{-\frac{x^2}{2}}}{3^{\frac{1}{3}}\pi^{-\frac{3}{4}}2^{\frac{n}{2}+\frac{1}{4}}\sqrt{n!}}H_n(x)=\operatorname{Ai}(t). \label{pr}$$ In [@Is], Ismail shows the $q$-analogue of [\[pr\]](#pr){reference-type="eqref" reference="pr"};

::: prp
We have $$\lim_{n\to\infty}\frac{q^{n^2}}{t^n}h_n(\sinh\xi_n|q)=\operatorname{A}_q\left(\frac{1}{t^2}\right)$$ where $e^{\xi_n}=tq^{-\frac{n}{2}}$.
:::

Here, $h_n(\cdot |q)$ is the $q$-Hermite polynomial. In this sense, we can deal with the Ramanujan function $\operatorname{A}_q(x)$ as a $q$-analogue of the Airy function. The Ramanujan function satisfies the following $q$-diference equation; $$\left(qx\sigma_q^2-\sigma_q+1\right)u(x)=0.
\label{ram}$$

::: rem
We remark that another solution of the equation [\[ram\]](#ram){reference-type="eqref" reference="ram"} is given by $$u(x)=\theta (x){}_2\varphi_0(0,0;-;q,-x/q).$$ Here, $${}_2\varphi_0\left(0,0;-;q,-\frac{x}{q}\right)=\sum_{n\ge 0}\frac{1}{(q;q)_n}\left\{(-1)^nq^{\frac{n(n-1)}{2}}\right\}^{-1}\left(-\frac{x}{q}\right)^n$$ is a divergent series.
:::

The $q$-Airy function is found by K. Kajiwara, T. Masuda, M. Noumi, Y. Ohta and Y. Yamada [@KMNOY], in their study of the $q$-Painlevé equations. This function is the special solution of the second $q$-Painlevé equations and given by the following series $$\operatorname{Ai}_q(x):=\sum_{n\ge 0}\frac{1}{(-q,q;q)_n}\left\{(-1)^nq^\frac{n(n-1)}{2}\right\}(-x)^n={}_1\varphi_1(0;-q;q,-x).$$

T. Hamamoto, K. Kajiwara, N. S. Witte [@hama] proved following asymptotic expansions;

::: prp
With $q=e^{-\frac{\delta^3}{2}}$, $x=-2ie^{-\frac{s}{2}\delta^2}$ as $\delta\to 0$, $${_1\varphi_1}(0;-q;q,-qx)=2\pi^{\frac{1}{2}}\delta^{-\frac{1}{2}}
e^{-\left(\frac{\pi i}{\delta^3}\right)\ln 2+\left(\frac{\pi i}{2\delta }\right)s+\frac{\pi i}{12}}\left[\operatorname{Ai}\left(se^{\frac{\pi i}{3}}\right)+O(\delta^2)\right],$$ $${_1\varphi_1}(0;-q;q,qx)=2\pi^{\frac{1}{2}}\delta^{-\frac{1}{2}}
e^{-\left(\frac{\pi i}{\delta^3}\right)\ln 2-\left(\frac{\pi i}{2\delta }\right)s-\frac{\pi i}{12}}\left[\operatorname{Ai}\left(se^{-\frac{\pi i}{3}}\right)+O(\delta^2)\right]$$ for $s$ in any compact domain of $\mathbb{C}$.
:::

Here, $\operatorname{Ai}(x)$ is the Airy function. From this proposition, we can regard the $q$-Airy function as a $q$-analogue of the Airy function.

We can easily check out that the $q$-Airy function satisfies the second order linear $q$-difference equation $$\left(\sigma_q^2+x\sigma_q-1\right)u(x)=0.
\label{qai}$$ Another solution of the equation [\[qai\]](#qai){reference-type="eqref" reference="qai"} is given by $$u(x)=
e^{\pi i\left(\frac{\log x}{\log q}\right)}{_1\varphi_1}(0;-q;q,x)
=e^{\pi i\left(\frac{\log x}{\log q}\right)}\operatorname{Ai}_q(-x).$$
