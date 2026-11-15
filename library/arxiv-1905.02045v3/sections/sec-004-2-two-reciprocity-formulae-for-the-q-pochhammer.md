---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-004-2-two-reciprocity-formulae-for-the-q-pochhammer
section_title: "Two reciprocity formulae for the q-Pochhammer symbol"
section_number: 2
pages: 8-9
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.79
latex_coverage_ratio: 0.929
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
[]{#repsec label="repsec"}

## Abel-Plana's summation formula

Our argument is based on the Abel-Plana summation formula.

We denote by $\gamma_\varepsilon$ the following integration contour.

<figure id="fig:contour">

</figure>

::: lemma
[]{#lem:abelplana label="lem:abelplana"} Let $\alpha, \beta,\beta'\in\mathbb{R}$ with $\alpha \leq \beta<\beta'$. Let $f$ be an analytic function on a neighborhood of $U:=\{z\in\mathbb{C}\mid \alpha\leq \operatorname{Re}(z)\leq \beta'\}\setminus\{\alpha,\beta\}$. Assume that the following holds :

1.  $f(z)$ is holomorphic at $\beta$ if $\beta$ is an integer, and otherwise $f(z)=o(|z-\beta|^{-1})$ as $z\to\beta$ with $z\in U$,

2.  $f(x\pm iy) = o(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi y}/y^2)$ as $y\to+\infty$, uniformly in $x\in[\alpha, \beta]$,

3.  $f$ is integrable on $(\alpha, \beta)$.

Then we have $$\begin{aligned}
\label{eq:abelplana}
    \sum_{\alpha < n \leq \beta} f(n) = \int_{\alpha}^{\beta} f(t)\mathrm{d}t - C(f, \alpha) + C(f, \beta), 
  
\end{aligned}$$ where $$C(f, \alpha):=\lim_{\varepsilon\to0^+}\bigg(- i \int_{\gamma_\varepsilon}  \frac{f(\alpha + it)\mathrm{d}{t}}{\ifthenelse{\equal{-\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -\alpha\aftergroup\egroup\originalright)}{( -\alpha)}{( -\alpha)}{( -\alpha)}}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}+ i \int_{\overline{\gamma_\varepsilon}}  \frac{f(\alpha - it)\mathrm{d}{t}}{\ifthenelse{\equal{\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha\aftergroup\egroup\originalright)}{( \alpha)}{( \alpha)}{( \alpha)}}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}\bigg).$$
:::

::: proof
*Proof.* The arguments in [@Olver1997 Chapter 8, eq. (3.01)] are readily adapted. ◻
:::

For $k\in\mathbb{Z}_{\geq 0}$, $k\neq 1$, let $\tilde B_{k}(t)= {B}_{k}(\{t\})$ where $\{t\}$ is the fractional part of $t$ and ${B}_{k}$ is the $k$-th Bernoulli polynomial, and let $\tilde B_{1}(t)={B}_1(\{t\})$ for $t\notin\mathbb{Z}$ and $\tilde B_1(n)=0$ for $n\in\mathbb{Z}$. We require the following computation.

::: lemma
[]{#lem:B-integral label="lem:B-integral"} For $\ell\in\mathbb{Z}_{\geq0}$ and $v\in[0, 1)$, we have $$\int_{0}^\infty \operatorname{Im}\bigg( \frac{(-it)^\ell}{\ifthenelse{\equal{v}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  v\aftergroup\egroup\originalright)}{( v)}{( v)}{( v)}} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}\bigg) \mathrm{d}t=  \frac{(-1)^\ell \tilde B_{\ell+1}(v)}{2(\ell+1)}.$$ Moreover, for all $\omega\in\mathbb{C}\smallsetminus(-\infty, 1]$, we have $$\int_0^\infty \frac{\mathrm{d}t}{\omega  \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1} = \frac{-1}{2\pi}\log(1-\omega^{-1})$$ with $\log$ being the principal determination.
:::

::: proof
*Proof.* The second claim is easy to prove by expanding the fraction as a power series in $\omega$, first for $\omega\in(1,\infty]$, and then by analytic continuation. To show the first claim, first we note that for $\ell=0$, $v=0$, the fraction is a real number, and both sides evaluate to $0$. We may therefore assume that $\ell\geq 1$ or $v\neq 0$. Then $$\begin{aligned}
    \int_{0}^\infty \operatorname{Im}\bigg(\frac{(-it)^\ell}{\ifthenelse{\equal{v}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  v\aftergroup\egroup\originalright)}{( v)}{( v)}{( v)}} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi t}-1}\bigg)\mathrm{d}t = {}& \frac{1}{(2\pi)^{\ell+1}}\operatorname{Im}\bigg( \ifthenelse{\equal{-v}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -v\aftergroup\egroup\originalright)}{( -v)}{( -v)}{( -v)}} (-i)^\ell \int_{0}^\infty \frac{t^\ell \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{-t}\mathrm{d}t}{1-\ifthenelse{\equal{-v}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -v\aftergroup\egroup\originalright)}{( -v)}{( -v)}{( -v)}} \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{-t}}\bigg) \\
    = {}& \frac{\ell!}{(2\pi)^{\ell+1}}\operatorname{Im}{}\bigg( (-i)^\ell \sum_{n\geq 1}\frac{\ifthenelse{\equal{-nv}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -nv\aftergroup\egroup\originalright)}{( -nv)}{( -nv)}{( -nv)}}}{n^{\ell+1}}\bigg)
  
\end{aligned}$$ by [@GZ eq. (3.411.6)]. We write $\operatorname{Im}{}( (-i)^\ell\ifthenelse{\equal{-nv}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  -nv\aftergroup\egroup\originalright)}{( -nv)}{( -nv)}{( -nv)}} )= (-1)^{\ell+1} \cos(2\pi nv - \frac\pi2(\ell+1))$, and conclude by the Fourier expansion of Bernoulli polynomials [@GZ eq. (9.622.1)]. ◻
:::
