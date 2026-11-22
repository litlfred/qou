---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-035-82-the-general-case
section_title: "The general case"
section_number: 8.2
pages: 60-63
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.proof41 label="sub.proof41"}

We now apply the same analysis to the expansion of $J(x)$ around an arbitrary rational number $\alpha$. The second part of the argument, replacing sums by integrals and computing them by using the functional $I_\lambda$, is unchanged, but the analogue of Proposition [\[prop.a1\]](#prop.a1){reference-type="ref" reference="prop.a1"} is now slightly more complicated, since the asymptotic formula for $P_n(x)$ near the $m$-th peak depends on both $m$ and the residue class of $n$ modulo the denominator of $\alpha$. We use the notations given above, i.e., with $X$ tending to infinity in the class $\beta\!\pmod1$ and $M=m+\frac56$ with $0\le m<\mathrm{den}(\beta)$, but now we also fix a residue class $r\!\pmod c$ and consider $n$ satisfying $$n \equiv r+m d\pmod c , \qquad n = \frac M\hbar+c \nu$$ with $|\nu|\ll X$. (Notice that $\nu$ has the opposite sign to the one used for $c=1$.)

::: Proposition
[]{#prop.a2 label="prop.a2"} For fixed $m<\mathrm{den}(\beta)$ and $r\in\mathbb Z/c\mathbb Z$ and for $n$ and $X$ tending to infinity as in $(5)$, we have the asymptotic formula $$\begin{gathered}
\label{tag6}
\log P_n\bigl(x\bigr) \;\sim\;\log\left(\frac1\hbar\right) + \log P_m(\beta)
+ \sum_{k=-1}^\infty C_k^{(r)}(\nu) h^k ,
\end{gathered}$$ valid to all orders in $h$, where $C_k^{(r)}$ is the polynomial of degree $k-1$ defined by $$\begin{gathered}
\label{tag7}
C_k^{(r)}(\nu) = - 2 \operatorname{Re}\biggl[\frac{{\rm i}^{-k}}{(k+1)!}
 \sum_{j=1}^c \text{{\rm Li}}_{1-k}\big(\zeta_\alpha^{r+j}Z\big) B_{k+1}\left(\nu+\frac jc\right)\biggr],
\qquad\! r\in\mathbb Z/c\mathbb Z, \quad\! k\ge-1\!\!\!
\end{gathered}$$ with $\zeta_\alpha=\mathbf{e}(\alpha)$ and $Z=\mathbf{e}(-5/(6c))$.
:::

The proof of this proposition, which we omit, is similar to that of Proposition [\[prop.a1\]](#prop.a1){reference-type="ref" reference="prop.a1"}, the main point again being that the difference of the right-hand sides of [\[tag6\]](#tag6){reference-type="eqref" reference="tag6"} for $n$ and $n-1$ is given by $$\begin{aligned}
\sum_{k=-1}^\infty \big[C_k^{(r)}(\nu) - C_k^{(r-1)}(\nu-1)\big] h^k
& = - 2 \operatorname{Re}\Biggl[\sum_{k=0}^\infty \text{{\rm Li}}_{1-k}(\zeta_\alpha^rZ)
\frac{(-{\rm i}h\nu)^k}{k!}\Biggr] \\
 &
= \log\bigl|1 - \zeta_\alpha^rZ{\rm e}^{-{\rm i}\nu h}\bigr|^2 = \log|1-q^n|^2 \\ &
= \log P_n(x)  - \log P_{n-1}(x) ,
\end{aligned}$$ because $$q^n = \mathbf{e}\left(n\left(\alpha - \frac1{c(cX+d)}\right)\right) =
\mathbf{e}\left((r+md)\alpha - \frac{m+5/6}c - \nu\hbar\right) = \zeta_\alpha^rZ{\rm e}^{-{\rm i}\nu h}$$ and $$\begin{aligned}
C_k^{(r)}(\nu)  - C_k^{(r-1)}(\nu-1) &
= - 2 \operatorname{Re}\Biggl[\frac{{\rm i}^{-k}}{(k+1)!}
 \Biggl(\sum_{j=1}^c - \sum_{j=0}^{c-1} \Biggr)
\text{{\rm Li}}_{1-k}\big(\zeta_\alpha^{r+j}Z\big) B_{k+1}\left(\nu+\frac jc\right)\Biggr] \\
 & = - 2 \operatorname{Re}\biggl[{\rm i}^{-k}\text{{\rm Li}}_{1-k}(\zeta_\alpha^rZ) \frac{B_{k+1}
(\nu+1) - B_{k+1}(\nu)}{(k+1)!}\biggr] \\ &
 = - 2 \operatorname{Re}\biggl[  \text{{\rm Li}}_{1-k}(\zeta_\alpha^rZ) \frac{(\nu/{\rm i})^k}{k!} \biggr] .
\end{aligned}$$ Note that in the above calculation we used that is independent of both $\nu$ and $r$. In fact, it is given by $$C_{-1}^{(r)}(\nu) = 2 \operatorname{Im}\Biggl[\sum_{j=1}^c \text{{\rm Li}}_2\big(\zeta_\alpha^{r+j}Z\big)\Biggr]
 = \frac2c \operatorname{Im}[\text{{\rm Li}}_2(Z^c)] = \frac V c ,$$ where we have used the well-known "distribution" property of the dilogarithm. The corresponding distribution property of the 1-logarithm $\text{{\rm Li}}_1(z)=-\log(1-z)$ shows that is also independent of $\nu$ and is given by $$C_0^{(r)}(\nu) = \sum_{j=1}^c \left(\nu+\frac jc-\frac12\right)
\log\bigl|1 - \zeta_\alpha^{r+j}Z\bigr|^2 = \log E_r(\alpha) ,$$ where $E_r(\alpha)$ is the real algebraic number defined by $$\label{tag8}
E_r(\alpha) = \prod_{j=1}^c \bigl|1 - \zeta_\alpha^{r+j}Z\bigr|^{2j/c},
\qquad r\in\mathbb Z/c\mathbb Z.$$ Hence, the exponentiated version of (6) can be written $$P_n(x) \;\sim\;P_m(\beta) \frac{{\rm e}^{V/c\hbar}}\hbar E_r(\alpha)
\exp\left(\sum_{k=1}^\infty C_k^{(r)}(\nu) h^k\right) ,$$ where again the exponential factor at the end has the form ${\rm e}^{-c\sqrt 3\nu^2h/2}\phi_{c,r}\big(\nu\sqrt h,\sqrt h\big)$ with $$\phi_{c,r}\big(\varepsilon\sqrt h,\sqrt h\big)=
\exp\biggl(
\widetilde C_1^{(r)}(\nu) +
\sum_{k \geq 2} C_k^{(r)}(\nu) h^k
\biggr),$$ where is given by the same formula as the right-hand side of [\[tag7\]](#tag7){reference-type="eqref" reference="tag7"} (with $k=1$) and with $B_2(x)=x^2-x+1/6$ replaced by $B_2(x)-x^2$. Note that $\phi_{c,r}(t,\varepsilon)$ is a power series in $\varepsilon$ with coefficients in $\mathbb Q(\zeta_\alpha,Z)[t]$ and leading coefficient 1. The same reasoning as for $c=1$ now shows that the sum of the values of $P_n(x)$ for $n$ running over the $m$-th peak and in the residue class $r+md\!\pmod c$ is equal to for some power series with leading coefficient $E_r(\alpha)$, and summing this over all $r$ gives equation [\[QMCa\]](#QMCa){reference-type="eqref" reference="QMCa"} for the $4_1$ knot with $$\Phi^{(4_1,\sigma_1)}_\alpha(h)=3^{-1/4}c^{-1/2} \sum_{r\!\!\!\!\pmod c}\Phi_\alpha^{(r)}(h) .$$ Note that the formal Gaussian integration formula for the power series $\Phi_\alpha(h)$ requires to expand the integrand up to order $O\big(h^{3k+1}\big)$ in order to obtain the coefficient of $h^k$ in the series $\Phi_\alpha(h)$.

It remains to look at the units $E_r(\alpha)$. Write $F$ for $\mathbb Q(\mathbf{e}(1/6))$, the trace field of the figure 8 knot, and $F_c$ for its cyclotomic extension $F(\zeta_\alpha)=\mathbb Q(Z)$. We claim that both $E_r(\alpha)/E_0(\alpha)$ and $\prod_{r\!\!\pmod c}E_r(\alpha)$ belong to $F_c$. The second claim follows from the first, since it is clear that $E_0(\alpha)^c$ belongs to $F_c$, and the first claim follows from the calculation $$\frac{E_r(\alpha)}{E_{r-1}(\alpha)}
 = \frac{\prod_{j=0}^c \bigl|1-\zeta_\alpha^{r+j}Z\bigr|^{2j/c}}{\prod_{j=0}^{c-1}
\bigl|1-\zeta_\alpha^{r+j}Z\bigr|^{2(j+1)/c}}
 = \frac{\bigl|1-\zeta_\alpha^rZ\bigr|^2}{\prod_{n\!\!\!\!\pmod c} \bigl|1-\zeta_\alpha^nZ
\bigr|^{2/c}} = |1 - \zeta_\alpha^rZ\bigr|^2 ,$$ from which we get by induction the formula $$E_r(\alpha) = E_0(\alpha) \bigl|(\zeta_\alpha Z,\zeta_\alpha)_r\bigr|^2$$ for all $r$. In particular, we can write our asymptotic formula to leading order as $$J\left(\frac{aX+b}{cX+d}\right)\Bigr/ J(X) \;\sim\;
\frac{c E_0(\alpha) S(\alpha)}{3^{1/4}}
 X^{3/2} \exp\left(\frac V{2\pi} \left(X+\frac dc\right)\right)$$ as $X\to\infty$ with bounded denominator, where $$\label{tag10}
S(\alpha) = \sum_{r\!\!\!\!\pmod c}\frac{E_r(\alpha)}{E_0(\alpha)} =
\sum_{n=0}^{c-1} \bigl|(\zeta_\alpha Z,\zeta_\alpha)_n\bigr|^2 \in F_c .$$

It is the factor $S(\alpha)$ which for $c=5$ contains the funny prime $\pi_{29}$ occurring in [@Za:QMF p. 14], while $E_0(a)$ is the unit analyzed in [@CGZ]. Note that the special properties [\[cunit\]](#cunit){reference-type="eqref" reference="cunit"} of this unit are clear from the definition [\[tag8\]](#tag8){reference-type="eqref" reference="tag8"} since if $c$ is prime to $6$ and we denote by $\sigma_k$ the Galois automorphism of $F_c$ over $F$ sending a primitive $c$-th root of unity to its $k$-th power, then it is easy to see from (8) that $\sigma_k(E_r(a/c)^c)=E_r(ka/c)^c$ and that the quotient $E_r(ka/c)^k/E_r(a/c)$ belongs to $F_c$.

For other knots $K$, there is a similar story, but we can no longer rigorously prove anything, since the terms in the sum defining $J^K(x)$ are no longer positive (or even real) and there is cancellation. However, this sum still has the form of an $N$-dimensional sum of products or quotients of Pochhammer symbols, where $N$ is the dimension of some terminating $q$-hypergeometric series (related to the number of simplices in a triangulation of $S^3\smallsetminus K$), and we can formally look at the parts of this sum where the summands are locally constant ("stationary phase"), even if those "parts" now lie outside of the original domain of summation. This leads to a conjectural, but completely explicit, formula of the same general form as (2), and in particular to an asymptotic formula like (9), but with $E_r(\alpha)=E^K_r(\alpha)$ now depending on an element $r$ of $(\mathbb Z/c\mathbb Z)^N$ rather than just $\mathbb Z/c\mathbb Z$ and with the sum in (10) replaced by one over $(\mathbb Z/c\mathbb Z)^N$. For the $5_2$ knot and its sister, the $(-2,3,7)$ pretzel knot, we worked out the corresponding expressions and for small values of $c$ obtained both the units and the pre-factors $S^K(\alpha)\in F_c$ ($F$ = trace field of $K$) that we had previously found numerically. These are, however, much more complicated than in the $4_1$ case; for instance, the factor , a prime of norm 29 that occurred for the $4_1$ knot and $c=5$ (see equation [\[as41at5\]](#as41at5){reference-type="eqref" reference="as41at5"} and the discussion in the next section) is replaced for the $5_2$ knot by $\mathfrak p_7^2 \mathfrak p_{43}$ if $c=3$ and by $\mathfrak p_{9491}\mathfrak p_{1227271}$ if $c=5$, where each $\mathfrak p_p$ denotes a prime of norm $p$ in $\mathbb Q(\xi)$.
