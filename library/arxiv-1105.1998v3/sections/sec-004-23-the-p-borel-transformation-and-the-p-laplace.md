---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-004-23-the-p-borel-transformation-and-the-p-laplace
section_title: "The p-Borel transformation and the p-Laplace transformation"
section_number: 2.3
pages: 4-6
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.896
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
[]{#section2.3 label="section2.3"}

We define the $p$-Borel transformation and the $p$-Laplace transformation to solve the equation ([\[b4\]](#b4){reference-type="ref" reference="b4"}), following Zhang [@Z1].

::: definition
For $f(t)=\sum\limits_{n\ge 0}a_nt^n$, the $p$-Borel transformation is defined by $$g(\tau )=\left(\mathcal{B}_pf\right)(\tau ):=\sum_{n\ge 0}a_np^{-\frac{n(n-1)}{2}}\tau^n,$$ and the $p$-Laplace transformation is given by $$\left(\mathcal{L}_pg\right)(t):=\frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta_p\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau }.$$ Here, $r_0>0$ is enough small number.
:::

The $p$-Borel transformation is considered as a formal inverse of the $p$-Laplace transformation.

::: lemma
We assume that the function $f$ can be $p$-Borel transformed to the analytic function $g(\tau )$ around $\tau =0$. Then, $$\mathcal{L}_p\circ\mathcal{B}_pf=f.$$
:::

::: proof
*Proof.* We can prove this lemma calculating residues of the $p$-Laplace transformation around the origin. ◻
:::

The $p$-Borel transformation has the following operational relation.

::: lemma
[]{#oprel label="oprel"}For any $l,m \in \mathbb{Z}_{\ge 0}$, $$\mathcal{B}_p\big(t^m\sigma_p^l\big)=p^{-\frac{m(m-1)}{2}}\tau^m\sigma_p^{l-m}\mathcal{B}_p.$$
:::

Applying the $p$-Borel transformation to the equation ([\[b4\]](#b4){reference-type="ref" reference="b4"}) and using Lemma [\[oprel\]](#oprel){reference-type="ref" reference="oprel"}, $g(\tau )$ satisfies the first order difference equation $$g(p\tau )=\left(1+p^{2\nu +2}\tau \right)\left(1+p^2\tau \right)g(\tau ).$$ Since $g(0)=1$, we get an infinite product of $g(\tau )$: $$g(\tau )=\frac{1}{(-p^{2\nu +2}\tau ;p)_\infty(-p^2\tau ;p)_\infty}.$$ Then $g(\tau )$ has single poles at $$\left\{-p^{-2\nu -2-k},-p^{-2-k};k\in\mathbb{Z}_{\ge 0}\right\}.$$ We set $$0<r<r_0:=\min\left\{\frac{1}{|p^{2\nu +2}|},  \frac{1}{|p^2|}\right\}.$$ and choose the radius $r>0$ such that $0<r<r_0$. By Cauchy's residue theorem, the $p$-Laplace transform of $g(\tau )$ is $$\begin{gathered}
f(t)= \frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta_p\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau }\\
\phantom{f(t)}{}
= -\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta_p\!\left(\frac{t}{\tau}\right)\!\frac{1}{\tau };\tau \!=\!-p^{-2\nu-2-k}\right\}\!
 -\sum_{k\ge 0}\operatorname{Res}\left\{g(\tau )\theta_p\!\left(\frac{t}{\tau}\right)\!\frac{1}{\tau };\tau \!=\! -p^{-2-k}\right\},
\end{gathered}$$ where $0<r<r_0$. To calculate the residue, we use the following lemma.

::: lemma
[]{#lems label="lems"}For any $k\in\mathbb{N}$, $\lambda\in\mathbb{C}^*$, we have

1.  $\operatorname{Res}\left\{\dfrac{1}{\left(\tau /\lambda ;p\right)_\infty}\dfrac{1}{\tau }:\tau =\lambda p^{-k}\right\}
    =\dfrac{(-1)^{k+1}p^{\frac{k(k+1)}{2}}}{(p;p)_k (p;p)_\infty}$,

2.  $\dfrac{1}{(\lambda p^{-k};p)_\infty}=\dfrac{(-\lambda )^{-k}p^{\frac{k(k+1)}{2}}}{(\lambda ;p)_\infty \left(p/\lambda ;p\right)_k},\qquad \lambda \not \in p^{\mathbb{Z}}$.
:::

Summing up all of the residues, we obtain the convergent series $f(t)$ as follows $$\begin{gathered}
f(t) =\frac{\theta
_p\left(-p^{2\nu +2}t\right)}{(p^{-2\nu},p;p)_\infty}
{}_1\varphi_1\left(0,p^{1+2\nu};p,x\right)
 +\frac{\theta _p\left(-p^2t\right)}{(p^{2\nu},p;p)_\infty}
{}_1\varphi_1\left(0,p^{1-2\nu};p,p^{-2\nu}x\right),
\end{gathered}$$ where $xt=1$. Therefore, we acquire the connection formula for $z(t)=\mathcal{E}(t)f(t)$.
