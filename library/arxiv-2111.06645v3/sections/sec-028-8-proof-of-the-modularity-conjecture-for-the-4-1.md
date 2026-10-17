---
doc_id: arxiv-2111.06645v3
doc_title: "Part 0: Introduction and overview"
section_id: sec-028-8-proof-of-the-modularity-conjecture-for-the-4-1
section_title: "Proof of the modularity conjecture for the 4_1 knot"
section_number: 8
pages: 58-60
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "Part 0: Introduction and overview — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns indexed by the"
---
[]{#sec.QMC41 label="sec.QMC41"}

In this section, we give our proof of the quantum modularity conjecture for the figure 8 knot, announced several years ago. Another proof was given by [@BD], as well as proofs of the quantum modularity conjecture for a few other knots, but we give our proof for completeness and because the point of view here is somewhat different from the one there.

We denote by $J(x)$ the $J$-function for the $4_1$ knot, as given explicitly by equation [\[Hab41\]](#Hab41){reference-type="eqref" reference="Hab41"} with ${q=\mathbf{e}(x)}$. We have to show that $$\label{tag2}
J\left(\frac{aX+b}{cX+d}\right) \sim
(cX+d)^{3/2} J(X) \widehat\Phi_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)$$ to all orders in $1/X$ as $X$ tends to infinity with bounded denominator with ${\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)}$ fixed and $c>0$, where is the completed version of a formal power series $\Phi_{a/c}(h)$ with algebraic coefficients and where $$V=\text{Vol}\big(S^3\smallsetminus 4_1\big)=2.02988\dots$$ is the volume of the complement of this knot. We give the proofs separately for the special case $\gamma=S$, $\alpha:=a/c=0$ and for the general case, since all the main ideas are already visible for the former and the details are much simpler.

## The case of $\boldsymbol{\alpha=0}$ {#sub.proof41.0}

We begin with the case $\alpha=0$, which makes it clear where the factor $J(X)$ in equation [\[tag2\]](#tag2){reference-type="eqref" reference="tag2"} comes from. We use the notation $$P_n(x)=|(q;q)_n|^2 ,$$ for $q=\mathbf{e}(x)$ with $x$ rational, so that $P_n(x)$ is the $n$-th summand in the definition of $J(x)$, and denote by $c_r$ ($r\ge0$) the numbers defined by the Taylor expansion $$\cot\left(\frac\pi6 - \frac x2\right) = \sum_{r=0}^\infty c_r \frac{x^r}{r!} ,$$ the first values being given by the table

::: center
    $r$       0       1       2        3         4          5          6          7
  ------- ---------- --- ----------- ------ ------------ ------- ------------- --------
   $c_r$   $\sqrt3$   2   $2\sqrt3$   $10$   $22\sqrt3$   $182$   $602\sqrt3$   $6970$
:::

Note that these numbers can also be written $c_r=2 \operatorname{Im}({\rm i}^{-r}\text{{\rm Li}}_{-r}(\mathbf{e}(1/6)))$ and hence have a natural extrapolation backwards by $c_{-1}=0$, $c_{-2}=-V$. We want to study $J(-1/X)=J(1/X)$ as $X$ tends to infinity in the fixed residue class $\beta\pmod1$, with $\beta$ rational. The summands in [\[J0for41\]](#J0for41){reference-type="eqref" reference="J0for41"} are all positive (that is what makes this case much easier to treat than the general one), and it is easy to find their local peaks, which occur near $n=\big(m+\frac56\big)X$ for $0\le m<\mathrm{den}(\beta)$, where $\mathrm{den}(b)$ is the denominator of $b$. (Notice that the terms for larger values of $m$ are 0 anyway, since $P_n(x)$ vanishes for $n\ge\mathrm{den}(x)$.) The following proposition, which is valid at a fixed peak even for $X$ real, gives the asymptotic value of the summand $P_n(x)$ for $n$ in each of these peaks. As usual, $B_r(x)$ denotes the $r$-th Bernoulli polynomial.

::: Proposition
[]{#prop.a1 label="prop.a1"} Fix an integer $m\ge0$, and set $M=m+\frac56$. Then for $X$ tending to infinity and $n$ an integer of the form $MX-\nu$ with $|\nu|\ll X$ we have the asymptotic expansion $$\label{tag3}
\log P_n\left(\frac1X\right) \;\sim\;\frac V{2\pi} X + \log X + \log P_m(X)
+ \sum_{k=1}^\infty c_{k-1} \frac{B_{k+1}(\nu)}{(k+1)!} \left(-\frac{2\pi}X\right)^k .$$
:::

By the above remark we can omit the first term and sum over $k\ge-1$ instead.

::: proof
*Proof.* We first note that for $q=\mathbf{e}(1/X)$ we have $$\log\left(\frac{P_n(1/X)}{P_{n-1}(1/X)}\right)
= \log\bigl|1 - q^n\bigr|^2 = \log\left|1 - \mathbf{e}\left(\frac16 +\frac\nu X \right)\right|^2
= -\sum_{k=1}^\infty \frac{c_{k-1}}{k!} \left(\frac{2\pi\nu}X\right)^k$$ (here we have used that $\frac {\rm d}{{\rm d}x}\log|1-\mathbf{e}(x)|^2=2\pi\cot(\pi x)$), in agreement with equation [\[tag3\]](#tag3){reference-type="eqref" reference="tag3"} to all orders in $1/X$ since $B_{r+1}(\nu+1)-B_{r+1}(\nu)= (r+1)\nu^r$. This proves [\[tag3\]](#tag3){reference-type="eqref" reference="tag3"} up to a power series independent of $n$ (but depending a priori on $\alpha$ and $m$). The full assertion uses the shifted Euler--Maclaurin summation formula; we omit the details. ◻
:::

Note that equation [\[tag3\]](#tag3){reference-type="eqref" reference="tag3"} does not make sense if $X$ is rational and $m\ge\mathrm{den}(X)$, since then $P_n(1/X)$ and $P_m(X)$ vanish, but we will use it only in the exponentiated form $$\label{tag4}
P_n\left(\frac1X\right) \;\sim\;P_m(X) X {\rm e}^{V/h}
\exp\Biggl( \sum_{r\ge1} (-1)^rc_{r} \frac{B_{r+1}(\nu)}{(r+1)!} h^r\Biggr),
\qquad h=\frac{2\pi}X ,$$ which holds also in this case. The key point here is that the only dependence on $m$ of the expression on the right-hand side is the factor $P_m(X)$, which equals $P_m(\beta)$ if $X$ goes to infinity in the fixed class $\mathbb Z+\beta$ modulo 1. Moreover, since $B_2(\nu) = \nu^2+O(\nu)$ and $B_{r+1}(\nu)=O\big(\nu^{r+1}\big)$ for $r>2$, the exponential factor in equation [\[tag4\]](#tag4){reference-type="eqref" reference="tag4"} has the form , where $$\phi\big(\varepsilon\sqrt h,\sqrt h\big)=
\exp\bigg(\frac{\sqrt{3}}{2} h \left(\varepsilon-\frac{1}{6} \right)+
\sum_{r\ge 2} (-1)^rc_{r} \frac{B_{r+1}(\varepsilon)}{(r+1)!} h^r\bigg)
 .$$ The contribution to $J(1/X)$ from the $m$-th peak is equal to $P_m(\beta)X{\rm e}^{V/h}$ times the sum of this exponential factor over all $\nu$ with $|\nu|\ll X$ in a fixed residue class $\nu_0\pmod1$, where $\nu_0\equiv-MX\pmod1$. But by the Poisson summation formula and the fact that the Fourier transform of a Gaussian decays exponentially, we have that $$\begin{aligned}
\sum_{\substack{\nu\equiv\nu_0 \text{(mod~1)}\\|\nu|\ll X}}
{\rm e}^{-\sqrt 3\nu^2h/2}\phi\big(\nu\sqrt h,\sqrt h\big)
={}& \int_{-\infty}^\infty {\rm e}^{-\sqrt 3 \nu^2h/2}\phi\big(\nu\sqrt h,\sqrt h\big) {\rm d}\nu\nonumber\\
= {}&\sqrt X I_{\sqrt3}\bigl[\phi\big(t,\sqrt h\big)\bigr] ,\label{VZ}
\end{aligned}$$ to all orders in $h$, where $I_\lambda$ for $\lambda>0$ denotes the linear map from $\mathbb C[[t]]$ to $\mathbb C$ defined by $$I_\lambda\bigl[\phi(t)\bigr] = \frac1{\sqrt{2\pi}} \int_{-\infty}^\infty
{\rm e}^{-\lambda t^2/2}\phi(t) {\rm d}t ,
\qquad I_\lambda\bigl[t^n\bigr] =
\begin{cases}
(n-1)!! \lambda^{-(n+1)/2} &\text{if $n$ is even,}\\ 0
&\text{if $n$ is odd.}
\end{cases}$$ Here $(n-1)!!$ as usual denotes the "double factorial" $(n-1)\times(n-3)\times\cdots\times3\times1$. A discussion of the estimates that prove equation [\[VZ\]](#VZ){reference-type="eqref" reference="VZ"} is given in [@VZ; @Zagier] and [@GZ:asymptotics]. It follows that the contribution to $J(1/X)$ from the $m$-th peak is equal to $P_m(\beta)X^{3/2}{\rm e}^{V/h}\Phi_0(h)$ to all orders, where $\Phi_0(h)$ is the power series given by equation [\[Phi410\]](#Phi410){reference-type="eqref" reference="Phi410"}. Hence, $J(1/X)$ itself equals $J(\beta)X^{3/2}{\rm e}^{V/h}\Phi_0(h)$ to all orders, as claimed. Note that $\Phi_0(h)$ equals $3^{-1/4}$ times a power series in $h$ with coefficients in $\mathbb Q\big(\sqrt3\big)$ and leading coefficient 1, since $I_\lambda[\phi(t)]$ has coefficients in for any power series $\phi(t)$ with rational coefficients. (That it is a power series in $h$ rather than merely  follows from the fact that $I_\lambda$ annihilates odd functions.)

This concludes the proof of equation [\[tag2\]](#tag2){reference-type="eqref" reference="tag2"} when $\alpha=0$, with $\Phi_0(h)$ given by $$\label{Phi410}
\Phi_0(h) = I_{\sqrt{3}}\big(\phi\big(t\sqrt{h},\sqrt{h}\big)\big) .$$
