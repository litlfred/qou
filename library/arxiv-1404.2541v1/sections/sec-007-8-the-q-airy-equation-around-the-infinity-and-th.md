---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-007-8-the-q-airy-equation-around-the-infinity-and-th
section_title: "The q-Airy equation around the infinity and the connection formula"
section_number: 8
pages: 17-19
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.985
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
We consider the behavior of the equation [\[qai\]](#qai){reference-type="eqref" reference="qai"} around the infinity. We set $x=1/t$ and $z(t)=u(1/t)$. Then $z(t)$ satisfies $$\left(-\sigma_q^2+\frac{1}{q^2t}\sigma_q+1\right)z(t)=0.$$ We set $\mathcal{E}(t)=1/\theta (-q^2t)$ and $f(t)=\sum_{n\ge 0}a_nt^n,\quad a_0=1$. We assume that $z(t)$ can be described as $$z(t)=\mathcal{E}(t)f(t)=\frac{1}{\theta (-q^2t)}\left(\sum_{n\ge 0}a_nt^n\right).$$

The function $\mathcal{E}(t)$ has the following property;

::: lmm
For any $t\in\mathbb{C}^*$, $$\sigma_q\mathcal{E}(t)=-q^2t\mathcal{E}(t),
\qquad \sigma_q^2\mathcal{E}(t)=q^5t^2\mathcal{E}(t).$$
:::

From this lemma, $f(t)$ satisfies the following equation $$\label{qaeq}
\left(-q^5t^2\sigma_q^2-\sigma_q+1\right)f(t)=0.$$ Since [\[qaeq\]](#qaeq){reference-type="eqref" reference="qaeq"} is the same as [\[kram\]](#kram){reference-type="eqref" reference="kram"} for $K=-q^5$, we obtain $$f(t)={}_0\varphi_1(-;0;q^2,q^5t^2)=\operatorname{A}_{q^2}(-q^3t^2).$$

We show a connection formula for $f(t)$. In order to obtain a connection formula, we need the $q$-Borel transformation and the $q$-Laplace transformation following Zhang [@Z1].

Applying the $q$-Borel transformation to the equation [\[kram\]](#kram){reference-type="eqref" reference="kram"} and using lemma [\[orqb\]](#orqb){reference-type="ref" reference="orqb"}, we obtain the first order $q$-difference equation $$g(q\tau )=(1+q^2\tau )(1-q^2\tau )g(\tau ).$$ Since $g(0)=1$, $g(\tau )$ is given by an infinite product $$g(\tau )=\frac{1}{(-q^2\tau ;q)_\infty(q^2\tau ;q)_\infty}$$ which has single poles at $$\left\{\tau ;\tau =\pm q^{-2-k},\quad \forall k\in\mathbb{Z}_{\ge 0}\right\}.$$ By Cauchy's residue theorem, the $q$-Laplace transform of $g(\tau )$ is $$\begin{aligned}
f(t)=&\frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau }\\
=&-\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{1}{\tau };\tau =-q^{-2-k}\right\}\\
&-\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{1}{\tau };\tau =q^{-2-k}\right\}
\end{aligned}$$ where $0<r<r_0:=1/|q^2|$. We can culculate the residue from lemma [\[lems\]](#lems){reference-type="ref" reference="lems"}.

::: lmm
[]{#lems label="lems"}For any $k\in\mathbb{N}$, $\lambda\in\mathbb{C}^*$, we have:

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
