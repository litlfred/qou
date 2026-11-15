---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-003-13-asymptotics-in-the-bulk-of-the-spectrum
section_title: "Asymptotics in the bulk of the spectrum"
section_number: 1.3
pages: 6-8
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s13 label="s13"}

Given a sequence of subsets

$$X(n)=\left\{x_1(n)<\dots<x_s(n)\right\}\subset\mathbb{Z}\,,$$

where $s=|X(n)|$ is some fixed integer, we call this sequence *regular* if the following limits

$$\begin{aligned}
a_i &= \lim_{n\to\infty} \frac{x_i(n)}{\sqrt{n}}\,, \label{e14}\\
d_{ij}&=\lim_{n\to\infty}\left(x_i(n)-x_j(n)\right)\,, \label{e15}
\end{aligned}$$

exist, finite or infinite. Here $i,j=1,\dots,s$. Observe that if $d_{ij}$ is finite then $d_{ij}=x_i(n)-x_j(n)$ for $n\gg 0$.

In the case when $X(n)$ can be represented as $X(n)=X'(n)\cup X''(n)$ and the distance between $X'(n)$ and $X''(n)$ goes to $\infty$ as $n\to\infty$ we shall say that the sequence *splits*; otherwise, we call it *nonsplit*. Obviously, $X(n)$ is nonsplit if and only if all $x_i(n)$ stay at a finite distance from each other.

Define the correlation functions $\boldsymbol{\varrho}(n,\,\cdot\,)$ of the measures $M_n$ by the same rule as in [\[e0006\]](#e0006){reference-type="eqref" reference="e0006"}

$$\boldsymbol{\varrho}(n,X)= M_n\left(\left\{\lambda\,|\, X\subset \mathcal{D}(\lambda)\right\} 
\right)\,.$$

We are interested in the limit of $\boldsymbol{\varrho}(n,X(n))$ as $n\to\infty$. This limit will be computed in Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} below. As we shall see, if $X(n)$ splits, then the limit correlations factor accordingly.

Introduce the following *discrete sine kernel* which is a translation invariant kernel on the lattice $\mathbb{Z}$ $$\mathsf{S}(k,l;a)=\mathsf{S}(k-l,a)\,, \quad k,l\in\mathbb{Z}\,,$$ depending on a real parameter $a$:

$$\begin{aligned}
\mathsf{S}(k,a)&=\frac{\sin(\arccos(a/2)\,k)}{\pi k}\\
&=
\frac{\sqrt{4-a^2}}{2\pi} \frac{U_{k-1}(a/2)}{k}\,,
\quad k\in \mathbb{Z}\,.
\end{aligned}$$

Here $U_k$ is the Tchebyshev polynomials of the second kind. We agree that

$$\mathsf{S}(0,a)=\frac{\arccos(a/2)}\pi\,, 
\quad \mathsf{S}(\infty,a)=0$$

and also that $$\mathsf{S}(k,a)=
\cases 0\,,& \textup{$a\ge 2$ or $a\le 2$ and $k\ne 0$}\,,\\
1 \,,  &\textup{$a\le 2$ and $k= 0$}\,.
\endcases$$

The following result describes the local structure of a Plancherel typical partition.

::: theorem
[]{#t2 label="t2"} Let $X(n)\subset\mathbb{Z}$ be a regular sequence and let the numbers $a_i$, $d_{ij}$ be defined by [\[e14\]](#e14){reference-type="eqref" reference="e14"}, [\[e15\]](#e15){reference-type="eqref" reference="e15"}. If $X(n)$ splits, that is, if $X(n)=X'(n)\cup X''(n)$ and the distance between $X'(n)$ and $X''(n)$ goes to $\infty$ as $n\to\infty$ then

$$\label{e1t2}
\lim_{n\to\infty} \boldsymbol{\varrho}(n,X(n)) =
\lim_{n\to\infty} \boldsymbol{\varrho}(n,X'(n))  \cdot
\lim_{n\to\infty} \boldsymbol{\varrho}(n,X''(n))\,.$$

If $X(n)$ is nonsplit then

$$\label{e2t2}
\lim_{n\to\infty} \boldsymbol{\varrho}\left(n,X(n)\right)
=
\det \Big[\,\mathsf{S}(d_{ij},a)
\Big]_{1\le i,j \le s}\,,$$

where $\mathsf{S}$ is the discrete sine kernel and $a=a_1=a_2=\dots$.
:::

We prove this theorem in Section [\[s3\]](#s3){reference-type="ref" reference="s3"}.

::: remark
Notice that, in particular, Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} implies that, as $n\to\infty$, the shape of a typical partition $\lambda$ near any point of the limit curve $\Omega$ is described by a stationary random process. For distinct points on the curve $\Omega$ these random processes are independent.
:::

::: remark
By complementation, see Section [\[sA3\]](#sA3){reference-type="ref" reference="sA3"} and [\[s32\]](#s32){reference-type="ref" reference="s32"}, one obtains from Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} an equivalent statement about the asymptotics of the following correlation functions

$$\rho(n,X)= M_n\left(\left\{\lambda\,|\, X\subset \operatorname{Fr}(\lambda)\right\} 
\right)\,.$$
:::

::: remark
The discrete sine kernel was studied before, see [@Wi1; @Wi2], mainly as a model case for the continuous sine kernel. In particular, the asymptotics of Toeplitz determinants built from the discrete sign kernel was obtained by H. Widom in [@Wi2] answering a question of F. Dyson. As pointed out by S. Kerov, this asymptotics has interesting consequences for the Plancherel measures.
:::

::: remark
Note that, in particular, Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} implies that the limit density (the 1-point correlation function) is given by

$$\label{e16}
\boldsymbol{\varrho}(\infty,a)=\cases
\frac1\pi\, {\arccos(a/2)}\,, & |a|\le 2\,,\\
0\,, & a>2 \,,\\
1\,, & a<-2 \,.
\endcases$$

This is in agreement with the Logan-Shepp-Vershik-Kerov result about the limit shape $\Omega$. More concretely, the function $\Omega$ is related to the density [\[e16\]](#e16){reference-type="eqref" reference="e16"} by

$$\boldsymbol{\varrho}(\infty,u)=\frac{1-\Omega'(u)}2 \,,$$

which can be interpreted as follows. Approximately, we have

$$\#\left\{i\,\left|\, \frac{\lambda_i}{\sqrt{n}} \in [u,u+\Delta u]\right.\right\}
\approx \sqrt{n} \, \boldsymbol{\varrho}(\infty,u) \, \Delta u \,.$$

Set $w=\dfrac{i}{\sqrt{n}}$. Then the above relation reads $\Delta w \approx \boldsymbol{\varrho}(\infty,u) \, \Delta u$ and it should be satisfied on the boundary $v=\Omega(u)$ of the limit shape. Since $v=u+2w$, we conclude that

$$\boldsymbol{\varrho}(\infty,u)\approx \frac{d w}{du}=\frac{1-\Omega'}2 \,,$$

as was to be shown.
:::

::: remark
The discrete sine-kernel $\mathsf{S}$ becomes especially nice near the diagonal, that is, where $a=0$. Indeed,

$$\mathsf{S}(x,0)= \cases 
1/2\,, & x=0 \,,\\
{(-1)^{(x-1)/2}}\Big/(\pi x) \,,
& x=\pm1,\pm3,\dots \,, \\
0\,, &x=\pm2,\pm4,\dots \,.
\endcases$$
:::
