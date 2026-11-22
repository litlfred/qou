---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-008-36-the-connection-formula-of-the-q-airy-function
section_title: "The connection formula of the q-Airy function"
section_number: 3.6
pages: 12-13
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.979
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanujan equation between the origin and the inﬁnity."
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
