---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension"
section_id: sec-004-6-the-q-borel-laplace-transformations
section_title: "The q-Borel-Laplace transformations"
section_number: 6
pages: 13-19
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
doc_brief: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension — We show connection formulae of local solutions of the Ramanu - jan equation between the origin and the"
text_source: latex
latex_prose_ratio: 0.604
latex_coverage_ratio: 0.987
---
In this section, we show a connection formula of the divergent series ${}_2\varphi_0$. This series appears in the second solution of the Ramanujan equation [\[ram\]](#ram){reference-type="eqref" reference="ram"}. At first, we define two types of the $q$-Borel-Laplace transformations.

**Definition.** *We assume that $f(x)$ is a formal power series $f(x)=\sum_{n\ge 0}a_nx^n$, $a_0=1$.*

1.  The $q$-Borel transformation of the first kind is $$\left(\mathcal{B}_q^+f\right)(\xi ):=\sum_{n\ge 0}a_nq^{\frac{n(n-1)}{2}}\xi^n\left(=:\varphi (\xi )\right).$$

2.  The $q$-Laplace transformation of the first kind is $$\left(\mathcal{L}_{q, \lambda}^+\varphi\right)(x):=
    \frac{1}{1-q}\int_0^{\lambda\infty}\frac{\varphi (\xi )}{\theta_q\left(\frac{\xi}{x}\right)}\frac{d_q\xi}{\xi}=\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta_q\left(\frac{\lambda q^n}{x}\right)},$$ here, this transformation is given by Jackson's $q$-integral [@GR].

We also define the $q$-Borel-Laplace transformations of the second kind as follows:

1.  The $q$-Borel transformation of the second kind is $$(\mathcal{B}_q^-f)(\xi ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\xi^n\left(=:g(\xi )\right).$$

2.  The $q$-Laplace transformation of the second kind is $$\left(\mathcal{L}_q^-g\right)(x):=\frac{1}{2\pi i}\int_{|\xi |=r}g(\xi )\theta_q\left(\frac{x}{\xi }\right)\frac{d\xi}{\xi},$$ where $r>0$ is enough small number.

We remark that the $q$-Borel transformation $\mathcal{B}_q^+$ is formal inverse of the $q$-Laplace transformation $\mathcal{L}_{q,\lambda }^+$ as follows;

::: lmm
For any entire function $f(x)$, we have $$\mathcal{L}_{q, \lambda}^+\circ\mathcal{B}_q^+f=f.$$
:::

The $q$-Borel transformation $\mathcal{B}_q^-$ also can be considered as a formal inverse of the $q$-Laplace transformation.

::: lmm
We assume that the function $f$ can be $q$-Borel transformed to the analytic function $g(\xi )$ around $\xi =0$. Then, we have $$\mathcal{L}^-_q\circ\mathcal{B}^-_qf=f.$$
:::

::: proof
*Proof.* We can prove this lemma calculating residues of the $q$-Laplace transformation around the origin. ◻
:::

The $q$-Borel transformation $\mathcal{B}_q^-$ has following operational relation.

::: lmm
[]{#orqb label="orqb"} For any $l,m\in\mathbb{Z}_{\ge 0}$, $$\mathcal{B}_q^-(t^m\sigma_q^l)=q^{-\frac{m(m-1)}{2}}\tau^m\sigma_q^{l-m}\mathcal{B}_q^-.$$
:::

In the following subsection, we apply these resummation methods to deal with the connection problem.

# The connection formula of the series ${}_2\varphi_0(0,0;-;q,\cdot )$

The aim of this section is to give a proof for the following theorem;

::: thm
[]{#divergentramanujan label="divergentramanujan"}For any $x\in\mathbb{C}^*\setminus [-\lambda ;q],$ $$\begin{aligned}
\theta_q(x){}_2f_0&\left(0,0;-;q,-\frac{x}{q}\right)=(q;q)_\infty\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{qx}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}
{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)\\
&+\frac{(q;q)_\infty}{1-q}\frac{\theta_q(x) \theta_{q^2}\left(-\frac{\lambda^2}{x}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\frac{\lambda}{x}
{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$
:::

We give the proof of theorem [\[divergentramanujan\]](#divergentramanujan){reference-type="ref" reference="divergentramanujan"}.

::: proof
*Proof.* We apply the $q$-Borel transformation $\mathcal{B}_q^+$ to the divergent series $v(x)={}_2\varphi_0(0,0;-;q,-x/q)$. We obtain $$\left(\mathcal{B}_q^+v\right)(\xi )={}_1\varphi_0\left(0;-;q,\frac{\xi}{q}\right)=:\varphi (\xi ).$$ From lemma [\[alt\]](#alt){reference-type="ref" reference="alt"}, $$\varphi (\xi )=\frac{(q;q)_\infty}{\theta_q\left(-\frac{\xi}{q}\right)}
{}_0\varphi_1\left(-;q;q^2,\frac{q^5}{\xi^2}\right)-\frac{(q;q)_\infty}{\theta_q\left(-\frac{\xi}{q}\right)}
\frac{q^2}{(1-q)\xi}{}_0\varphi_1\left(-;q^3;q^2,\frac{q^7}{\xi^2}\right)$$ where $|\xi /q|<1$.

We apply the $q$-Laplace transformation $\mathcal{L}_{q, \lambda}^+$ to $\varphi (\xi )$: $$\begin{aligned}
&\left(\mathcal{L}_{q,  \lambda}^+\varphi\right)(x)=\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta_q\left(\frac{\lambda q^n}{x}\right)}
=\sum_{n\in\mathbb{Z}}\frac{{}_1\varphi_0\left(0;-;q,\frac{\lambda q^n}{q}\right)}{\theta_q\left(\frac{\lambda q^n}{x}\right)}\\









&=\frac{(q;q)_\infty}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\sum_{n-m\in\mathbb{Z}}(q^2)^{\frac{(n-m)(n-m-1)}{2}}\left(-\frac{\lambda^2}{qx}\right)^{n-m}\\
&\qquad\qquad\qquad\qquad \times \sum_{m\ge 0}\frac{(-1)^m(q^2)^{\frac{m(m-1)}{2}}}{(q;q^2;q^2)_m}\left(\frac{q^2}{x}\right)^m\\
&-\frac{(q;q)_\infty}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}\frac{q^2}{(1-q)\lambda}\sum_{n-m\in\mathbb{Z}}(q^2)^{\frac{(n-m)(n-m-1)}{2}}\left(-\frac{\lambda^2}{q^2x}\right)^{n-m}\\
&\qquad\qquad\qquad\qquad \times
\sum_{m\ge 0}\frac{(-1)^m(q^2)^{\frac{m(m-1)}{2}}}{(q^3,q^2;q^2)_m}\left(\frac{q^3}{x}\right)^m.
\end{aligned}$$ Therefore, $$\begin{aligned}
&{}_2f_0\left(0,0;-;q,-\frac{x}{q}\right)
=\mathcal{L}_{q, \lambda}^+\circ\mathcal{B}_q^+{}_2\varphi_0\left(0,0;-;q,-\frac{x}{q}\right)\\
&=(q;q)_\infty\frac{\theta_{q^2}\left(-\frac{\lambda^2}{qx}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}{}_1\varphi_1\left(0;q;q^2,\frac{q^2}{x}\right)
+\frac{(q;q)_\infty}{1-q}\frac{\theta_{q^2}\left(-\frac{\lambda^2}{x}\right)}{\theta_q\left(-\frac{\lambda}{q}\right)\theta_q\left(\frac{\lambda}{x}\right)}
{}_1\varphi_1\left(0;q^3;q^2,\frac{q^3}{x}\right).
\end{aligned}$$ We obtain the conclusion. ◻
:::

::: rem
By theorem [\[divergentramanujan\]](#divergentramanujan){reference-type="ref" reference="divergentramanujan"}, we have $$\tilde{u}_2(x,\lambda )=\tilde{C}_{21}v_1(x)+\tilde{C}_{22}v_2(x),$$ where $$\tilde{C}_{21}(x)=\frac{(q;q)_\infty\theta_{q^2}(-qx/\lambda^2)\theta_{q^2}(x)}{\theta_q(-q/\lambda )\theta_q(x/\lambda )\theta_q(x)}$$ and $$\tilde{C}_{22}(x)=\frac{(q;q)_\infty\theta_{q^2}(-x/\lambda^2)\theta_{q^2}(x/q)}{\theta_q(-1/\lambda )\theta_q(x/\lambda )\theta_q(x/q)}.$$ This is a half of our connection formula.
:::

# The $q$-Airy equation around the infinity and the connection formula

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
