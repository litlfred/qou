---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-005-112-hypothesis-approximate-factorization-of-char
section_title: "Hypothesis: approximate factorization of characters"
section_number: 1.12
pages: 6-9
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
text_source: latex
latex_prose_ratio: 0.834
latex_coverage_ratio: 0.984
---
[]{#sec:partitions label="sec:partitions"}

In the following we will use the following convention. If $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$ is a function on the set of partitions of $n$, we will extend its domain to the set $$\mathcal{P}_{\leq n}:=\bigsqcup_{0\leq k\leq n} \mathcal{P}_{k}$$ of partitions of smaller numbers by setting $$\label{eq:extended-character}
\chi_n(\pi):= \chi_n( \pi,1^{n-|\pi|}) \qquad \text{for } |\pi|\leq n,$$ i.e. we extend the partition $\pi$ by adding an appropriate number of parts, each equal to $1$.

In this way the cumulant $k^{\chi_n}_\ell (l_1,\dots,l_\ell)$ is well defined if $n\geq l_1+\cdots+l_\ell$ is large enough.

::: definition
[]{#def:approx-factorization-charactersA label="def:approx-factorization-charactersA"} Assume that for each integer $n\geq 1$ we are given a function $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$. We say that the sequence $(\chi_n)$ has *approximate factorization property* [@Sniady2006c] if for each integer $\ell\geq 1$ and all integers $l_1,\dots,l_\ell\geq 2$ the limit

$$\label{eq:aprox-fact-property}
    \lim_{n\to\infty} k^{\chi_n}_\ell (l_1,\dots,l_\ell)\ n^{\frac{l_1+\cdots+l_\ell+\ell-2}{2}}$$

exists and is finite.

We say that the sequence $(\chi_n)$ has *enhanced approximate factorization property* if, additionally, in the case $\ell=1$ the rate of convergence in [\[eq:aprox-fact-property\]](#eq:aprox-fact-property){reference-type="eqref" reference="eq:aprox-fact-property"} takes the following explicit form:

for each $l\geq 2$ there exist some constants $a_{l+1},b_{l+1}\in\mathbb{R}$ such that $$\label{eq:refined-asymptotics-characters}
    k^{\chi_n}_1(l) \ n^{\frac{l-1}{2}} =  \chi_n(l) \ n^{\frac{l-1}{2}}  =
    a_{l+1}+ \frac{b_{l+1}+o(1)}{\sqrt{n}} \qquad \text{for }n\to\infty$$ and $$\label{eq:what-is-m}
    \sup_{l\geq 2} \frac{\sqrt[l]{|a_l|}}{l^m} < \infty,
    \qquad
    \text{where }
    m = \begin{cases}2 &\text{for } g \neq 0,\\
    1 & \text{for } g=0,\end{cases}$$ where $g$ is given by [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"}.
:::

::: example
[]{#example:plancherel label="example:plancherel"} It is easy to check that for $\chi_{\mathop{\mathrm{reg}}}$ from [\[eq:regular\]](#eq:regular){reference-type="eqref" reference="eq:regular"} all higher cumulants vanish: $$k^{\chi_{\mathop{\mathrm{reg}}}}_\ell (l_1,\dots,l_\ell) = 0 \qquad \text{for $\ell\geq 2$}$$ and the first cumulant takes a particularly simple form $$k^{\chi_{\mathop{\mathrm{reg}}}}_1 (l) = \chi_{\mathop{\mathrm{reg}}} (l) =
    \begin{cases} 
    1 & \text{if } l=1, \\ 
    0 & \text{otherwise.}
    \end{cases}$$ It follows that that the sequence $(\chi_n)$ for which $\chi_n:=\chi_{\mathop{\mathrm{reg}}}$ fulfills the enhanced approximate factorization property.
:::

## Drawing Young diagrams

### Anisotropic Young diagrams {#sec:anisotropic-young}

<figure id="fig:stretch">
<div class="center">

</div>
<figcaption>A Young diagram <span class="math inline"><em>λ</em> = (4,3,1)</span> shown in the French convention (left) and a generalized Young diagram <span class="math inline">$T_{\frac{1}{2},\frac{3}{2}} \lambda$</span> (right) obtained by an anisotropic scaling. The dashed lines indicate individual boxes.</figcaption>
</figure>

The usual way of drawing Young diagrams is to represent each individual box as a unit square, see [1](#fig:stretch){reference-type="ref" reference="fig:stretch"} (left). However, when dealing with random Young diagrams related to Jack polynomials it is more convenient to represent each box as a rectangle with width $w>0$ and height $h>0$ such that $$\label{eq:aspect-ratio}
\frac{w}{h} = \alpha.$$ A Young diagram viewed like this becomes a polygon contained in the uppper-right quaterplane which will be denoted by $T_{w,h}\lambda$, see [1](#fig:stretch){reference-type="ref" reference="fig:stretch"} (right). We will refer to such polygons as *anisotropic Young diagrams*; they have been first considered by Kerov [@Kerov2000].

### Russian convention. Profile of a Young diagram

We draw (anisotropic) Young diagrams on the plane with the usual Cartesian coordinates $(x,y)$. However, it is also convenient to use the *Russian* coordinate system $(u,v)$ given by $$u = x-y, \qquad v = x+y.$$ This new coordinate system gives rise to the *Russian convention* for drawing (anisotropic) Young diagrams, see [2](#fig:french-fries){reference-type="ref" reference="fig:french-fries"}.

The boundary of a Young diagram $\lambda$ drawn in the Russian convention (the solid zigzag line on the right-hand side of [2](#fig:french-fries){reference-type="ref" reference="fig:french-fries"}) is a graph of a function $\omega_\lambda$ which will be called the *profile* of $\lambda$. If the Young diagram is replaced by an anisotropic Young diagram $T_{w,h}\lambda$ we define in an analogous way its profile $\omega_{T_{w,h}\lambda}$.

<figure id="fig:french-fries">
<div class="center">

</div>
<figcaption> The anisotropic Young diagram from <a href="#fig:stretch" data-reference-type="ref" data-reference="fig:stretch">1</a> shown in the French and Russian conventions. The solid line represents the <em>profile</em> of the Young diagram. The coordinate system <span class="math inline">(<em>u</em>,<em>v</em>)</span> corresponding to the Russian convention and the coordinate system <span class="math inline">(<em>x</em>,<em>y</em>)</span> corresponding to the French convention are shown.</figcaption>
</figure>

## The first main result: Law of Large Numbers

The following theorem is a generalization of the results of Biane [@Biane2001] who considered the special case $\alpha=1$ and the corresponding representations of the symmetric groups.

::: theorem
[]{#theo:lln label="theo:lln"} Assume that $\alpha=\alpha(n)$ is such that [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"} holds true. Assume that $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$ is a reducible Jack character; we denote by $\lambda_n$ the corresponding random Young diagram with $n$ boxes distributed according to $\mathbb{P}^{(\alpha)}_{\chi_n}$. We assume also that the sequence $(\chi_n)$ of characters fulfills the enhanced approximate factorization property.

Then there exists some deterministic function $\omega_{\Lambda_\infty}\colon\mathbb{R}\to\mathbb{R}$ with the property that $$\label{eq:limit}
    \lim_{n\to\infty} \omega_{\Lambda_n} = \omega_{\Lambda_\infty},$$ where $$\label{eq:Lambda}
    \Lambda_n:= T_{\sqrt{\frac{\alpha}{n}},\sqrt{\frac{1}{\alpha n}}} \lambda_n$$

and the convergence in [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"} holds true with respect to the supremum norm, in probability. In other words, for each $\epsilon>0$ $$\lim_{n\to\infty} \mathbb{P}\big( \|\omega_{\Lambda_n}-\omega_{\Lambda_\infty}   \|_\infty>
    \epsilon \big) =0 .$$
:::

::: remark
The concrete formula for the profile $\omega_{\Lambda_\infty}$ may be obtained by computing the corresponding $R$-transform and Cauchy transform, see for example [@Biane2001 Theorem 3].
:::

The proof is postponed to [\[sec:proof-of-LLN\]](#sec:proof-of-LLN){reference-type="ref" reference="sec:proof-of-LLN"}.
