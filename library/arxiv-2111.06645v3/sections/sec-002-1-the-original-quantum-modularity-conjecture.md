---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-002-1-the-original-quantum-modularity-conjecture
section_title: "The original quantum modularity conjecture"
section_number: 1
pages: 9-11
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.997
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sec.QMCK label="sec.QMCK"}

The starting point for this paper is the quantum modularity conjecture of [@Za:QMF], which itself is a refinement of the famous volume conjecture of Kashaev [@K95]. Let us recall them briefly here. Kashaev defined an invariant $\langle K \rangle_N \in \mathbb Z[{\rm e}^{2 \pi {\rm i}/N}]$ for every knot $K$ and positive integer $N$ and conjectured that if $K$ is hyperbolic knot the absolute values of these numbers grow exponentially like ${\rm e}^{c_KN}$, where $2\pi c_K$ is the hyperbolic volume of $S^3\smallsetminus K$. A more precise version of the conjecture [@Gu] says that there is a full asymptotic expansion $$\label{K1}
\langle K \rangle_N  \sim
N^{3/2} {\rm e}^{v(K)N} \Phi^{(K)} \left(\frac{2\pi {\rm i}}N\right)$$ valid to all orders in $1/N$ where $v(K)$ is the suitably normalized complexified volume of $K$ and where $\Phi^{(K)}(h)$ is a (divergent) power series. (Here and from now on we use the abbreviation ${\zeta_n=\mathbf{e}(1/n)}$ for $n\in\mathbb N$, where $\mathbf{e}(x):={\rm e}^{2\pi{\rm i}x}$.) It was further conjectured in [@DGLZ] and in [@Ga:CS] that $\Phi^{(K)}(h)$ has algebraic coefficients, and more precisely that it belongs to $\zeta_8 \delta^{-1/2}F_K[[h]]$, where $F_K$ is the trace field of $K$ and $\delta$ some nonzero element of $F_K$.

For instance, for the simplest hyperbolic knot $4_1$ (figure eight knot), the Kashaev invariant is given explicitly by $$\label{J0for41}
\langle 4_1\rangle_N = \sum_{n=0}^{N-1} \bigl|(\zeta_N;\zeta_N)_n\bigr|^2$$ (see [@K97 equation (2.2)]) with $(q;q)_n:=\prod_{j=1}^n\big(1-q^j\big)$, with values for $N=1,\dots,6$ and $100$ given numerically by

::: center
            $N$             $1$   2   3    4               5               6    $\cdots$           100
  ------------------------ ----- --- ---- ---- -------------------------- ---- ---------- ---------------------
   $\langle 4_1\rangle_N$   $1$   5   13   27   $46+2\sqrt5\approx50.47$   89   $\cdots$   $8.2\times 10^{16}$
:::

Here the trace field $F_K$ is $\mathbb Q\big(\sqrt{-3}\big)$ and the series $\Phi^{(K)}(h)$ begins $$\label{as41}
\Phi^{(4_1)}(h)= \frac1{\sqrt[4]{3}}
\left(1 + \frac{11}{72\sqrt{-3}} h + \frac{697}{2 \big(72\sqrt{-3}\big)^2} h^2
 + \frac{724351}{30 \big(72\sqrt{-3}\big)^3} h^3 +\cdots\right) .$$ Similarly, for the knot $5_2$, where the Kashaev invariant is given by formula [\[K52\]](#K52){reference-type="eqref" reference="K52"} below, the trace field is $\mathbb Q(\xi)$, where $\xi$ is the root of $\xi^3-\xi^2+1=0$ with negative imaginary part, and $\Phi^{(K)}(\hbar)$ has an expansion starting $$\begin{aligned}
\Phi^{(5_2)}(h) ={}& \frac{\zeta_8}{\sqrt{3\xi-2}}
\left(1 + \frac{117\xi^2-222\xi+203}{24(3\xi-2)^3}h\right.\nonumber\\
&\left. {}  + \frac{117279\xi^2 - 209229\xi + 157228}{2\big(24(3\xi-2)^3\big)^2}h^2
 + \cdots\right).\label{as52}
\end{aligned}$$

The passage from the volume conjecture to the quantum modularity conjecture (QMC for short) begins with the observation that the Kashaev invariant $\langle K\rangle_N$ is the value at $x=-1/N$ of a 1-periodic function $J(x)=J^{(K)}(x)$ on the rational numbers (i.e., it satisfies $J(x+1)=J(x)$ for all $x$), defined uniquely by the further requirement that it is a Galois-invariant function of $\mathbf{e}(x)$. (The uniqueness holds because every primitive $N$-th root of unity is a Galois conjugate of $\zeta_N$.) As shown by Murakami and Murakami [@MM], this function can also be identified with an evaluation of the colored Jones polynomial $J_{K,N}(q)$ [@Jones; @Tu1] by $J(x) = J_{K,N}(\mathbf{e}(-x))$ for any ${N \in
\mathbb Z}$ with $N x \in \mathbb Z$. In [@Za:QMF], it was found that [\[K1\]](#K1){reference-type="eqref" reference="K1"} is just the special case $\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)=\bigl(\smallmatrix 0&-1\\1&0\endsmallmatrix\bigr)$ of the more general (and of course still conjectural) statement that $$\label{QMCa}
J^{(K)}\left(\frac{aN+b}{cN+d}\right) \sim (cN+d)^{3/2} {\rm e}^{v(K)(N+d/c)}
\Phi^{(K)}_{a/c}\left(\frac{2 \pi {\rm i}}{c(cN+d)}\right)$$ to all orders in $N$ as $N \to \infty$ for any matrix $\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr) \in \mathrm{SL}_2(\mathbb Z)$ with $c>0$, where $\Phi^{(K)}_\alpha(\hbar)$ is a power series with algebraic coefficients depending on $\alpha\in \mathbb Q/\mathbb Z$, with . This does not yet look like a modularity statement, but in [@Za:QMF] it was further observed that [\[QMCa\]](#QMCa){reference-type="eqref" reference="QMCa"} holds also for non-integral values of $N$ (which we then denote by $X$ for clarity) but with one crucial modification, namely that we have $$\label{QMCb}
J^{(K)}\left(\frac{aX+b}{cX+d}\right) \sim (cX+d)^{3/2}
{\rm e}^{v(K)(X+d/c)} \Phi^{(K)}_{a/c}\left(\frac{2 \pi {\rm i}}{c(cX+d)}\right) J^{(K)}(X)$$ to all orders in $1/X$ as $X\to\infty$ in $\mathbb Q$ with bounded denominator, with the same series $\Phi^{(K)}_\alpha(\hbar)$ as before but now with the additional factor $J^{(K)}(X)$ depending only on $X$ modulo 1. (Here the condition of $X$ having bounded denominator was included in the original conjecture, and will be retained for its refinements in this paper, because all of our experiments were done for $X$ with simple fractional part. However, it will be a consequence of the smoothness statements cited above and discussed in Section [\[sub.lift\]](#sub.lift){reference-type="ref" reference="sub.lift"} that in fact [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"} remains true for any sequence of rational numbers $X$ tending to infinity, and we have checked this experimentally for many cases.)

Formula [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"} expresses the QMC in a quantitative form, in terms of specific power series with algebraic coefficients, while the plots of $J^{(K)}(X)$ and $J^{(K)}(X)/J^{(K)}(\gamma X)$ for $K=4_1$ and ${\gamma=S}$ that were shown (on a logarithmic scale because the functions grow exponentially) in the introduction presents the same conjecture in a more qualitative visual form. Both ways of looking at the conjecture will be refined greatly during the course of this paper.

The QMC [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"}, or even its special case [\[QMCa\]](#QMCa){reference-type="eqref" reference="QMCa"}, give us not just one, but a whole collection of power series associated to any knot. These series have a striking arithmetical structure. For example, in [@Za:QMF] we found that for $K=4_1$ and $\alpha$ with denominator 5 that $$\label{as41at5}

\Phi^{(4_1)}_{\alpha}(\hbar)= \pm  \sqrt[4]{3} \varepsilon_\alpha^{1/5}
\bigl(A^{(\alpha)}_0 + A^{(\alpha)}_1 h +\cdots\bigr)
\qquad\text{if\quad$\alpha\in \frac15 \mathbb Z\smallsetminus\mathbb Z,$}$$ where $\varepsilon_\alpha$ is a unit (whose fifth root must be chosen appropriately) of the cyclotomic field $\mathbb Q(\zeta_{15})=F_{4_1}(\zeta_5)$ ($\zeta_m:=\mathbf{e}(1/m)$) (explicitly , with $Z_\alpha:=\mathbf{e}\big(\alpha-\frac13\big)$) and the coefficients  belong to the same field, e.g., , a prime of norm 29. More generally, in the appendix to this paper extensive evidence is given for the conjecture that the power series for any knot $K$ and rational number $\alpha$ always belongs to $\mu \delta^{-1/2}\sqrt[c]{\varepsilon}F_{K,c}[[h]]$ with the same $\delta$ as before and some $8c$-th root of unity $\mu$, where $c$ is the denominator of $\alpha$, $F_{K,c}$ the field obtained by adjoining the $c$-th root of unity $\mathbf{e}(\alpha)$ to $F_K$, and $\varepsilon$ is an $S$-unit of $F_{K,c}$ for some finite set of primes $S$ of $F_K$ independent of $c$. This experimentally discovered property of quantum invariants of knots in turn suggested the purely number-theoretical conjecture, which was then proved in [@CGZ], that to an *arbitrary* number field $F$ and element of the Bloch group of $F$ one can canonically associate a sequence of $S$-units, well defined up to $c$-th powers, in the $c$ cyclotomic extension $F(\zeta_c)$ for all $c\ge1$, with $S$ independent of $c$.

We will give more details about this and other arithmetic properties of the series (such as estimates of the denominators of their coefficients) in Section [\[sec.arithmetic\]](#sec.arithmetic){reference-type="ref" reference="sec.arithmetic"}, and will give a complete proof in the case of the $4_1$ knot in Section [\[sec.QMC41\]](#sec.QMC41){reference-type="ref" reference="sec.QMC41"}. (This case and a few others were proven independently by Bettin and Drappeau [@BD].) We will also give detailed numerical evidence for several other knots, for several values of $\alpha\in\mathbb Q/\mathbb Z$, and to a relatively high degree in the power series , in the appendix to this paper. The calculations required to obtain these values are not at all trivial, since one has to be able to calculate the Kashaev invariants for (many) arguments with large denominators and then use very precise extrapolation methods to be able to find the coefficients to high enough accuracy to recognize them numerically as algebraic numbers.

Presenting the numerical evidence for the QMC was the initial motivation for this paper, and this already led to interesting numerical observations, such as the appearance of the near unit $\varepsilon$ or the denominator estimates mentioned above. But in the course of doing these calculations we discovered that the QMC is only part of a much larger story involving a whole collection of power series indexed by a certain finite set $\mathcal P_K$ (defined below) as well as by an index in $\mathbb Q/\mathbb Z$ as before. In the rest of Part I, we explain what these power series are, how they are related to each other, and how they lead to new invariants and to a whole series of successive refinements of the original quantum modularity conjecture.
