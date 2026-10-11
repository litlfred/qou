---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-006-36-the-connection-formula-of-the-q-airy-function
section_title: "The connection formula of the q-Airy function"
section_number: 3.6
pages: 12-14
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanu jan equation between the origin and the inﬁnity."
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
---
Applying the $q$-Borel transformation in [\[qbql\]](#qbql){reference-type="ref" reference="qbql"} to the equation ([\[kram\]](#kram){reference-type="ref" reference="kram"}) and using lemma [\[orqb\]](#orqb){reference-type="ref" reference="orqb"}, we obtain the first order $q$-difference equation $$g(q\tau )=(1+q^2\tau )(1-q^2\tau )g(\tau ).$$ Since $g(0)=1$, $g(\tau )$ is given by an infinite product $$g(\tau )=\frac{1}{(-q^2\tau ;q)_\infty(q^2\tau ;q)_\infty}$$ which has single poles at $$\left\{\tau ;\tau =\pm q^{-2-k},\quad \forall k\in\mathbb{Z}_{\ge 0}\right\}.$$ By Cauchy's residue theorem, the $q$-Laplace transform of $g(\tau )$ is $$\begin{aligned}
f(t)=&\frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau }\\
=&-\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{1}{\tau };\tau =-q^{-2-k}\right\}\\
&-\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{1}{\tau };\tau =q^{-2-k}\right\}
\end{aligned}$$ where $0<r<r_0:=1/|q^2|$. We can culculate the residue from lemma [\[lems\]](#lems){reference-type="ref" reference="lems"}.

::: lem
[]{#lems label="lems"}For any $k\in\mathbb{N}$, $\lambda\in\mathbb{C}^*$, one can get;

1.  $\operatorname{Res}\left\{\dfrac{1}{\left(\tau /\lambda ;q\right)_\infty}\dfrac{1}{\tau}:\tau =\lambda q^{-k}\right\}
    =\dfrac{(-1)^{k+1}q^{\frac{k(k+1)}{2}}}{(q;q)_k (q;q)_\infty}$,

2.  $\dfrac{1}{(\lambda q^{-k};q)_\infty}=\dfrac{(-\lambda )^{-k}q^{\frac{k(k+1)}{2}}}{(\lambda ;q)_\infty \left(q/\lambda ;q\right)_k},\quad \lambda \not \in q^{\mathbb{Z}}$.
:::

Summing up all of residues, we obtain $$\begin{aligned}
f(t)&=\frac{\theta (q^2t)}{(q,-1;q)_\infty} {_1\varphi_1}\left(0,-q;q,\frac{1}{t}\right)
+\frac{\theta (-q^2 t)}{(q,-1;q)_\infty} {_1\varphi_1}\left(0,-q;q,-\frac{1}{t}\right).
\end{aligned}$$

We obtain a connection formula for $z(t)=\mathcal{E}(t)f(t)$. Finally, we acquire the following connection formula between the Ramanujan function and the $q$-Airy function.

::: thm
For any $x\in\mathbb{C}^*$, $$\operatorname{A}_{q^2}\left(-\frac{q^3}{x^2}\right)
=\frac{1}{(q,-1;q)_\infty}
\left\{\theta \left(\frac{x}{q}\right)\operatorname{Ai}_q(-x)+\theta\left(-\frac{x}{q}\right)\operatorname{Ai}_q(x)\right\}.$$
:::

Here, both $\operatorname{A}_q(x)$ and $\operatorname{Ai}_q(x)$ are defined by convergent series on whole of the complex plain. The connection formula above is valid for any $x\in\mathbb{C}^*$.

# Connection formula of the divergent series ${}_2\varphi_0(0,0;-;q,\cdot )$

In this section, we show a connection formula of the divergent series ${}_2\varphi_0$. This series appears in the second solution of the Ramanujan equation [\[ram\]](#ram){reference-type="eqref" reference="ram"}. At first, we review two $q$-exponential functions to consider our connection formula.

## Two different $q$-exponential functions

In this section, we review two different $q$-exponential functions from the viewpoint of the connection problems. One of the $q$-exponential function $e_q(x)$ is given by $$e_q(x):={}_1\varphi_0 (0;-;q,x)=\sum_{n\ge 0}\frac{x^n}{(q;q)_n}.$$ The other $q$-exponential function $E_q(x)$ is $$E_q(x):={}_0\varphi_0(-;-;q,-x)=\sum_{n\ge 0}\frac{q^{\frac{n(n-1)}{2}}}{(q;q)_n}x^n.$$ The function $e_q(x)$ satisfies the following first order $q$-difference equation $$\left\{\sigma_q-(1-x)\right\}u(x)=0$$ and $E_q(x)$ satisfies $$\left\{(1+x)\sigma_q-1\right\}u(x)=0.$$ The limit $q\to 1-0$ converges the exponential function $$\lim_{q\to 1-0}e_q\left(x(1-q)\right)=\lim_{q\to 1-0}E_q\left(x(1-q)\right)=e^x.$$ In this sense, these functions considered as $q$-analogues of the exponential function. It is known that there exists the relation between these functions: $$e_q(x)E_q(-x)=1,\quad e_{q^{-1}}(x)=E_q(-qx).$$ But another relation has not known. We show the connection formula between them and give alternate representation of $e_q(\cdot )$.
