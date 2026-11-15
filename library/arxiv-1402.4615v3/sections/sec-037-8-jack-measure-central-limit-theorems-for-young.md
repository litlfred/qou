---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-037-8-jack-measure-central-limit-theorems-for-young
section_title: "Jack measure: central limit theorems for Young diagrams and transition measures"
section_number: 8
pages: 53-54
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#sect:CLT2 label="sect:CLT2"}

In this section, we state formally and prove our fluctuation results for Young diagrams under Jack measure. We will also present a fluctuation result for the transition measures of these diagrams.

Before we state our results, we need some preparations. We follow here notations from [@IvanovOlshanski2002 Sections 7 and 8]. First, we define $$\begin{aligned}
u_k(x) &= U_k(x/2) = \sum_{0 \leq j \leq \lfloor k/2 \rfloor}(-1)^j\binom{k-j}{j}x^{k-2j},\\
 t_k(x) &= 2T_k(x/2) = \sum_{0 \leq j \leq \lfloor k/2 \rfloor}(-1)^j\frac{k}{k-j}\binom{k-j}{j}x^{k-2j},
\end{aligned}$$ where $T_k$ and $U_k$ are respectively Chebyshev polynomials of the first and second kind. They can be alternatively defined by the following equations: $$\begin{aligned}
 u_k(2 \cos(\theta)) &= \frac{\sin((k+1)\theta)}{\sin(\theta)};\\
 t_k(2 \cos(\theta)) &= 2 \cos(k\theta).
\end{aligned}$$ It is known that $\left(u_k(x)\right)_k$ and $\left(t_k(x)\right)_k$ form a family of orthonormal polynomials with respect to the measures $\frac{\sqrt{4-x^2}}{2\pi}dx$ and $\frac{1}{2\pi \sqrt{4-x^2}}dx$, respectively, *i. e.*: $$\begin{aligned}
 \int^2_{-2} u_k(x)u_l(x)\frac{\sqrt{4-x^2}}{2\pi }dx &= \delta_{k,l};\\
 \int^2_{-2} t_k(x)t_l(x)\frac{1}{2\pi \sqrt{4-x^2}}dx &= \delta_{k,l}.
\end{aligned}$$ The measure $\frac{\sqrt{4-x^2}}{2\pi}dx$ supported on the interval $[-2,2]$ is called the *semi-circular distribution* and is denoted by the $\mu_{S-C}$ (see Subsection [\[subsect:JackPlancherel\]](#subsect:JackPlancherel){reference-type="ref" reference="subsect:JackPlancherel"}).

Recall from Theorem [\[theo:RYD-limit\]](#theo:RYD-limit){reference-type="ref" reference="theo:RYD-limit"} that the limit shape of scaled Young diagrams $$\omega\bigg(D_{1/\sqrt{n}}\big(A_\alpha(\lambda_{(n)})\big)\bigg)$$ is given by $\Omega$, where $\lambda_{(n)}$ is a random Young diagram with $n$ boxes distributed according to Jack measure. Hence, in order to study fluctuations of the random Young diagrams around the limit shape, we introduce the following application from the set of Young diagrams to the space of functions from $\mathbb{R}$ to $\mathbb{R}$: $$\Delta^{(\alpha)}(\lambda)(x) := \sqrt{n}\frac{\omega\bigg(D_{1/\sqrt{n}}\big(A_\alpha(\lambda)\big)\bigg)(x)
 - \Omega(x)}{2},$$ where $n$ is the number of boxes of $\lambda$.

Besides, tt was shown by Kerov [@Kerov1993] that the transition measure (see Subsection [\[subsect:TransMeasure\]](#subsect:TransMeasure){reference-type="ref" reference="subsect:TransMeasure"}) of the continuous Young diagram $\Omega$ is the semi-circular distribution (see Subsection [\[subsect:JackPlancherel\]](#subsect:JackPlancherel){reference-type="ref" reference="subsect:JackPlancherel"}). Thus we define the following function on the set of Young diagrams with $n$ boxes with values in the space of real signed measures: $$\widehat{\Delta}^{(\alpha)}(\lambda) := \sqrt{n}\left( \mu_{\bigg(D_{1/\sqrt{n}}\big(A_\alpha(\lambda)\big)\bigg)} - \mu_{S-C} \right) .$$ As above, $n$ is the number of boxes of $\lambda$. This function describes the (scaled) difference between the transition measure of the scaled Young diagram and the limiting semi-circular measure.

Now, we are ready to formulate the central limit theorem for the Jack measure. Here, we use the usual notation $[\text{condition}]$ for the indicator function of the corresponding condition.

::: theorem
[]{#theo:Fluctuations label="theo:Fluctuations"} Choose a sequence $\left(\Xi_k \right)_{k=2,3,\dots}$ of independent standard Gaussian random variables and let $\lambda_{(n)}$ be a random Young diagram of size $n$ distributed according to Jack measure. As $n \to \infty$, we have

1.  []{#item:fluctuationsOfDiagrams label="item:fluctuationsOfDiagrams"} a central limit theorem for Young diagrams: $$\left( u^{(\alpha)}_{k}(\lambda_{(n)}) \right)_{k=1,2,\dots} \xrightarrow{d} 
    \left(  \frac{\Xi_{k+1}}{\sqrt{k+1}} - \frac{\gamma}{k+1} \, [k\text{ is odd}]\right)_{k=1,2,\dots},$$ where $u^{(\alpha)}_{k} (\lambda) = \int_\mathbb{R}u_k(x) \Delta^{(\alpha)}(\lambda)(x)\ dx$;

2.  []{#item:fluctuationsOfTransition label="item:fluctuationsOfTransition"} and a central limit theorem for transition measures: $$\left( t^{(\alpha)}_{k}(\lambda_{(n)}) \right)_{k=3,4,\dots} \xrightarrow{d} \left(  \sqrt{k-1}\, \Xi_{k-1} - \gamma \, [k\text{ is odd}]  \right)_{k=3,4,\dots},$$ where $t^{(\alpha)}_{k} (\lambda) = \int_\mathbb{R}t_k(x) \widehat{\Delta}^{(\alpha)}(\lambda)(dx)$.
:::

::: remark
Notice that, for $\gamma=0$ (*i.e.* $\alpha=1$), this theorem specializes to Kerov's central limit theorems for Plancherel measure [@Kerov1993; @IvanovOlshanski2002].
:::
