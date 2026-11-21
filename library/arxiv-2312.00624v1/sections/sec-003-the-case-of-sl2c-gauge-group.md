---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-003-the-case-of-sl2c-gauge-group
section_title: "The case of SL(2,C) gauge group"
section_number: null
pages: 6-9
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.961
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: sl2c label="sec: sl2c"} In this work, we take $G_{{\mathbb C}} = \text{SL}(2,{\mathbb C})$. Therefore, we have simply $r=1$, and $$A_{{\cal K}}(P,X)=A_{{\cal K}, 1}(P_1,X_1)$$ is the classical $A$-polynomial of the knot [@Cooper:1994aa]. The operators $\hat{P}, \hat{X}$ act on $u$-states as $$\hat{P} |u\rangle = |u+ {\rm i}{\mathsf{b}}\rangle \, , \quad \hat{X} |u\rangle = X |u\rangle \, .$$ Equivalently, $\hat{P}$ is the operator that shifts $X$ into $q X$, and $\hat{X}$ is the ordinary multiplication. Building on previous results [@hikami01; @hikami07; @dglz], the exact, non-perturbative partition function $\chi_{{\cal K}}(u; \hbar)$ has been constructed from an ideal triangulation of $M$ and identified with a finite-dimensional integral whose integrand is a product of Faddeev's quantum dilogarithm functions [@faddeev], known as the state-integral invariant, or Andersen--Kashaev invariant [@ak; @ak2; @dimofte-rev]. This is a holomorphic function of $\hbar \in {\mathbb C}' = {\mathbb C}\backslash (-\infty, 0 ]$ and $u \in {\mathbb C}$. It can be explicitly verified [@amalusa] that it obeys the $q$-difference equation encoded in the quantized $A$-polynomial of the knot, that is, $$\label{AJ-eq}
\hat{A}_{{\cal K}}(\hat{P}, \hat{X},q) \chi_{{\cal K}}(u;\hbar) = 0 \, .$$

Recall that $S$-duality exchanges ${\mathsf{b}}$ with $1/{\mathsf{b}}$. Therefore, the $S$-dual images of $\hbar$ and $q$ are $$\hbar_D={4 \pi^2 \over \hbar} = \frac{2 \pi}{\tau} \, , \quad q_D= {\rm e}^{{\rm i}\hbar_D} = {\rm e}^{\frac{2 \pi {\rm i}}{\tau}}= \tilde q^{-1},$$ where we have introduced ${\tilde{q}}= {\rm e}^{-{2 \pi {\rm i}\over \tau}}$, while the variable $u$ is invariant under the action of $S$-duality and $X$ transforms into $$X_D = {\rm e}^{\frac{2 \pi u}{{\mathsf{b}}}} = X^{2 \pi \over \hbar} \, .$$ Remarkably, the wave function $\chi_{{\cal K}}(u;\hbar)$ is also invariant under this transformation, that is, $$\chi_{{\cal K}}(u;\hbar)=\chi_{{\cal K}}(u;\hbar_D) \, ,$$ and, in particular, it satisfies the $S$-dual quantum $A$-polynomial equation $$\hat A_{\cal K}(\hat{P}_D, \hat{X}_D, q_D)\chi_{{\cal K}}(u;\hbar)=0 \, ,$$ where $\hat{P}_D$ is the quantum operator acting on $u$-states by shifting $u$ into $u + {\rm i}/{\mathsf{b}}$, or, equivalently, transforming $X_D$ into $q_D X_D$, and $\hat{X}_D$ acts by multiplication.

<figure id="fig: simple_knots">
<p><embed src="figure-eight.pdf" style="width:30.0%" /> <embed src="three-twist.pdf" style="width:30.0%" /></p>
<figcaption>The hyperbolic knots known as the figure-eight knot (<span class="math inline"><strong>4</strong><sub>1</sub></span>), on the left side, and the three-twist knot (<span class="math inline"><strong>5</strong><sub>2</sub></span>), on the right side.</figcaption>
</figure>

Throughout this work, we look at two concrete examples of hyperbolic knots, which allow us to perform explicit and detailed calculations to provide support to and give insight into our claims. These are the figure-eight and the three-twist knots.

::: example
[]{#41example label="41example"} The figure-eight knot, also denoted by $\bm{4}_1$, is shown on the left side of Fig. [1](#fig: simple_knots){reference-type="ref" reference="fig: simple_knots"}. Its classical $A$-polynomial can be written in symmetrized form as

$$A_{\bm{4}_1}(P, X) = P^{-1} + P -( X^2+ X^{-2} -X -X^{-1} -2) \, .$$

The corresponding polynomial equation $A_{\bm{4}_1}(P, X)=0$ has only two distinct non-abelian branches. Explicitly, the geometric and conjugate branches are labeled as $$\alpha = \rm{geom}, \rm{conj} \, ,$$ and they are described by $$\label{classicP}
P^{(\rm{geom}, \rm{conj})} = \frac{T(X) \pm (1-X^2) \sqrt{\Delta(X)} }{2 X^2} \, ,$$ where we have introduced $$\begin{align}
T(X) &= 1 - X - 2 X^2 - X^3 + X^4 \, , \label{classicT} \\
\Delta(X) &= 1 - 2 X -  X^2 - 2 X^3 + X^4 \, . \label{classicD}
\end{align}$$

Building on the results and conventions of [@ggm2], the descendant $\hat A$-operator is given by

$$\label{rec41x}
    \hat A_{\bf{4}_1} (\hat{P},\hat{X},q^m,q) = \sum_{j=0}^2 C_j(\hat{X},q^m,q) \hat{P}^j \, ,$$

where $m$ takes values in ${\mathbb Z}$ and the coefficient functions $C_j(\hat{X},q^m,q)$ are

$$\begin{align}
      \label{rec41x0}
      C_0(\hat{X},q^m,q) =&q^{2 + 3 m} \hat{X}^2 (-1 + q^{3 + m} \hat{X}^2) \, , \\
      \label{rec41x1}
      C_1(\hat{X},q^m,q) =& -q^m (-1 + q^{2 + m} \hat{X}^2) (1 - q \hat{X} - q^{1 + m} \hat{X}^2 \\
      &- q^{3 + m} \hat{X}^2 - q^{3 + m} \hat{X}^3 + q^{4 + 2 m} \hat{X}^4) \, ,\nonumber \\ 
      \label{rec41x2}
      C_2(\hat{X},q^m,q) =& q^2 \hat{X}^2 (-1 + q^{1 + m} \hat{X}^2) \, .
\end{align}$$ If we set $m=0$, symmetrize by multiplying by $\hat{P}^{-1}$, simplify a common factor $q^2 \hat{X}^2$, and perform the change of variable $\hat{X} \rightarrow q^{-1} \hat{X}$, we obtain the conventional $\hat A$-operator of the figure-eight knot, that is,

$$\label{41Ahat}
    \hat A_{\bf{4}_1} (\hat{P},\hat{X},q) = C_0(\hat{X},q) \hat{P}^{-1} + C_1(\hat{X},q) + C_2(\hat{X},q) \hat{P} \, ,$$

where the coefficient functions $C_j(\hat{X},q)$ are

$$\begin{align}
      \label{41xC0}
      C_0(\hat{X},q) =&q \hat{X}^2-1 \, ,\\
      \label{41xC1}
      C_1(\hat{X},q) =& - (\hat{X}^2-1)( \hat{X}^2 + \hat{X}^{-2} - \hat{X} - \hat{X}^{-1} - q - q^{-1} ) \, ,\\ 
      \label{41xC2}
      C_2(\hat{X},q) =& q^{-1} \hat{X}^2-1 \, .
\end{align}$$
:::

::: example
[]{#52example label="52example"} The three-twist knot, also denoted by $\bm{5}_2$, is shown on the right side of Fig. [1](#fig: simple_knots){reference-type="ref" reference="fig: simple_knots"}. Its classical $A$-polynomial can be written in symmetrized form as

$$\begin{aligned}
A_{\bm{5}_2}(P, X) = &P^{-1} -(X^{-2} -X^{-1} +2 X + 2 X^2 - X^3) \\
&- (X^{-1} - 2 - 2 X + X^3 - X^4) P - X^2 P^2 \, .
\end{aligned}$$

The corresponding polynomial equation $A_{\bm{5}_2}(P, X)=0$ has three distinct non-abelian branches: the geometric branch, its conjugate, and a third, self-conjugate branch. We label them by $$\alpha = \rm{geom}, \rm{conj}, \rm{\text{self}} \, .$$ Again, following [@ggm2], the descendant $\hat A$-operator is given by

$$\label{rec52x}
    \hat A_{\bf{5}_2} (\hat{P},\hat{X},q^m,q) = \sum_{j=0}^3 C_j(\hat{X},q^m,q) \hat{P}^j \, ,$$

where $m$ takes values in ${\mathbb Z}$ and the coefficient functions $C_j(\hat{X},q^m,q)$ are

$$\begin{align}
      \label{rec52x0}
      C_0(\hat{X},q^m,q) =
      &-q^{2 + m} \hat{X}^2 (1-q^2 \hat{X})(1+q^2 \hat{X})(1-q^5 \hat{X}^2) \, , \\
      \label{rec52x1}
      C_1(\hat{X},q^m,q) =
      & (1-q \hat{X})(1+q \hat{X})(1-q^5 \hat{X}^2)(1-q\hat{X}-q\hat{X}^2-q^4\hat{X}^2 \\
      &+q^{2+m}\hat{X}^2+q^{3+m}\hat{X}^2+q^2\hat{X}^3+q^5\hat{X}^3+q^5\hat{X}^4+q^{5+m}\hat{X}^4-q^6\hat{X}^5) \, , \nonumber\\ 
      \label{rec52x2}
      C_2(\hat{X},q^m,q) =
      & q\hat{X}(1-q^2\hat{X})(1+q^2\hat{X})(1-q\hat{X}^2)(1-q^2\hat{X}-q^{2+m}\hat{X}-q^2\hat{X}^2-q^5\hat{X}^2 \\
      &+q^4\hat{X}^3+q^7\hat{X}^3-q^{5+m}\hat{X}^3-q^{6+m}\hat{X}^3+q^7\hat{X}^4-q^9\hat{X}^5) \, , \nonumber \\
      \label{rec52x3}
      C_3(\hat{X},q^m,q) =
      & q^{8+m}\hat{X}^4(1-q\hat{X})(1+q\hat{X})(1-q\hat{X}^2) \,.
\end{align}$$

If we set $m=0$, symmetrize by multiplying by $\hat{P}^{-2}$, and perform the change of variable $\hat{X} \rightarrow q^{-1} \hat{X}$, we obtain the conventional $\hat A$-operator of the three-twist knot, that is,

$$\label{52Ahat}
\begin{aligned}
\hat A_{\bf{5}_2}(\hat{P},\hat{X},q) = C_0(\hat{X},q) \hat{P}^{-2} + C_1(\hat{X},q) \hat{P}^{-1} + C_2(\hat{X},q) + C_3(\hat{X},q) \hat{P} \, ,
\end{aligned}$$

where we have defined $$\label{52xC}
\begin{align}
      \label{52xC0}
      C_0(\hat{X},q) =&-\hat{X}^2 (1-q^2 \hat{X}^2) (1-q^3 \hat{X}^2) \, , \\
      \label{52xC1}
      C_1(\hat{X},q) =& (1-\hat{X}^2) (1-q^3 \hat{X}^2)(q^2 \hat{X}^3-q^2 \hat{X}^2-q \hat{X}^5 \\
      &+2 q \hat{X}^4+q^{-1}\hat{X}^3+q \hat{X}^2-q^{-1}\hat{X}^2+\hat{X}^2-\hat{X}+1) \, , \nonumber \\ 
      \label{52xC2}
      C_2(\hat{X},q) =& \hat{X} (1-q^2 \hat{X}^2) (1-q^{-1}\hat{X}^2) (-q^4 \hat{X}^5+q^4 \hat{X}^3 \\
      &+q^3 \hat{X}^4-q^3 \hat{X}^3-q^3 \hat{X}^2-q^2 \hat{X}^3+q \hat{X}^3-2 q \hat{X}-\hat{X}^2+1)  \, , \nonumber \\
      \label{52xC3}
      C_3(\hat{X},q) =& q^4 \hat{X}^4 (1-\hat{X}^2)(1-q^{-1}\hat{X}^2) \, .
\end{align}$$
:::
