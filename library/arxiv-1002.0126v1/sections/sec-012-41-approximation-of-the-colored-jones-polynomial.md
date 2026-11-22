---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-012-41-approximation-of-the-colored-jones-polynomial
section_title: "Approximation of the colored Jones polynomial"
section_number: 4.1
pages: 22-26
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.977
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
Put $\xi_N:=\exp(2\pi\sqrt{-1}/N)$ and I will give an interpretation of the $R$-matrix used to define the colored Jones polynomial. From [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} and [\[eq:R_inverse\]](#eq:R_inverse){reference-type="eqref" reference="eq:R_inverse"} we have $$\label{eq:R_N}
\begin{split}
  R^{ij}_{kl}\bigr|_{q:=\xi_N}
  &=
  \sum_{m}
  \text{(a power of $\xi_N$)}\times
  \delta_{l,i+m}\delta_{k,j-m}\,
  \frac{\{l\}!\{N-1-k\}!}{\{i\}!\{m\}!\{N-1-j\}!},
  \\
  (R^{-1})^{ij}_{kl}\bigr|_{q:=\xi_q}
  &=
  \sum_{m}
  \text{(a power of $\xi_N$)}\times
  \delta_{l,i-m}\delta_{k,j+m}\,
  \frac{\pm\{k\}!\{N-1-l\}!}{\{j\}!\{m\}!\{N-1-i\}!}.
\end{split}$$ Since $$\{k\}!\bigr|_{q:=\xi_N}
  =
  \left(2\sqrt{-1}\right)^{k}
  \sin(\pi/N)
  \sin(2\pi/N)
  \cdots
  \sin(k\pi/N),$$ we have $$\begin{split}
  &
  \{k\}!\{N-k-1\}!\bigr|_{q:=\xi_N}
  \\
  =&
  \left(2\sqrt{-1}\right)^{N-1}
  \sin(\pi/N)\sin(2\pi/N)\cdots\sin(k\pi/N)
  \\
  &\times
  \sin\bigl((N-(k+1))\pi/N\bigr)
  \sin\bigl((N-(k+2))\pi/N\bigr)
  \sin\bigl((N-(N-1))\pi/N\bigr)
  \\
  =&
  (-1)^{N-k-1}\left(\sqrt{-1}\right)^{N-1}
  2^{N-1}
  \sin(\pi/N)\sin(2\pi/N)\cdots\sin((N-1)\pi/N)
  \\
  =&
  \varepsilon N
\end{split}$$ for $\varepsilon\in\{1,-1,\sqrt{-1},-\sqrt{-1}\}$. For the last equality, see for example [@Murakami/Murakami:ACTAM12001]. So if we put $$\begin{aligned}
  (\xi_N)_{k^+}&:=(1-\xi_N)\cdots(1-\xi^k_N),
  \\
  (\xi_N)_{k^{-}}&:=(1-\xi_N)\cdots(1-\xi^{N-1-k}_N),
\end{aligned}$$ we have $$\begin{aligned}
  \{k\}!\bigr|_{q:=\xi_N}
  &=
  \text{(a power of $\xi_N$)}\times(\xi_N)_{k^+},
  \\
  \{N-1-k\}!\bigr|_{q:=\xi_N}
  &=
  \text{(a power of $\xi_N$)}\times(\xi_N)_{k^-}
  \\
  \intertext{and}
  (\xi_N)_{k^+}(\xi_N)_{k^-}
  &=
  \text{(a power of $\xi_N$)}\times N.
\end{aligned}$$

Therefore from [\[eq:R_N\]](#eq:R_N){reference-type="eqref" reference="eq:R_N"} the $R$-matrix and its inverse can be written as $$\begin{aligned}
  R^{ij}_{kl}\bigr|_{q:=\xi_N}
  &=
  \sum_{m}
  \delta_{l,i+m}\delta_{k,j-m}\,
  \frac{\text{(a power of $\xi_N$)}\times N^2}
       {(\xi_N)_{m^+}(\xi_N)_{i^+}(\xi_N)_{k^+}
                       (\xi_N)_{j^-}(\xi_N)_{l^-}},
  \\
  (R^{-1})^{ij}_{kl}\bigr|_{q:=\xi_N}
  &=
  \sum_{m}
  \delta_{l,i-m}\delta_{k,j+m}\,
  \frac{\text{(a power of $\xi_N$)}\times N^{2}}
       {(\xi_N)_{m^+}(\xi_N)_{i^-}(\xi_N)_{k^-}
                       (\xi_N)_{j^+}(\xi_N)_{l^+}}.
\end{aligned}$$

If we are given a knot $K$, we express it as a closed braid and calculate the colored Jones polynomial as described in §[\[subsec:calculation\]](#subsec:calculation){reference-type="ref" reference="subsec:calculation"}. Then we have $$\label{eq:Jones_R}
\begin{split}
  J_N(K;\xi_N)
  &=
  \sum_{\text{labelings}}
  \left(
    \prod_{\text{crossings}}
    (R^{\pm1})^{ij}_{kl}
  \right)
  \\
  &=
  \sum_{\text{labelings}}
  \left(
    \prod_{\text{crossings}}
    \frac{\text{(a power of $\xi_N$)}\times N^{2}}
         {(\xi_N)_{m^+}(\xi_N)_{i^{\pm}}(\xi_N)_{k^{\pm}}
                         (\xi_N)_{j^{\mp}}(\xi_N)_{l^{\mp}}}
  \right),
\end{split}$$ where the summation is over all the labelings with $\{0,1,\dots,N-1\}$ corresponding to the basis $\{e_0,e_1,\dots,e_{N-1}\}$ and for a fixed labeling the product is over all the crossings, each of which corresponds to an entry $R^{ij}_{kl}$ (or $(R^{-1})^{i,j}_{kl}$, respectively), determined by the four labeled arcs around the vertex, of the $R$-matrix (or its inverse, respectively).

We will approximate $(\xi_N)_{k^{+}}$ for large $N$. By taking the logarithm, we have $$\begin{split}
  \log(\xi_N)_{k^{+}}
  &=
  \sum_{j=1}^{k}
  \log(1-\xi^j_N)
  \\
  &=
  \sum_{j=1}^{k}
  \log\bigl(1-\exp(2\pi\sqrt{-1}j/N)\bigr).
\end{split}$$ Putting $x:=j/N$, we may replace the summation with the following integral for large $N$ (this is *not rigorous!*). $$\begin{split}
  \log(\xi_N)_{k^{+}}
  &\underset{N\to\infty}{\approx}
  N\int_{0}^{k/N}\log\bigl(1-\exp(2\pi\sqrt{-1}x)\bigr)\,dx
  \\
  &=
  \frac{N}{2\pi\sqrt{-1}}
  \int_{1}^{\exp(2\pi\sqrt{-1}k/N)}\frac{\log(1-y)}{y}\,dy,
\end{split}$$ where we put $y:=\exp(2\pi\sqrt{-1}x)$ in the last equality and $\underset{N\to\infty}{\approx}$ means a very rough approximation (which may be not true at all) for large $N$.

This integral is known as the dilogarithm function. We put $$\operatorname{Li}_2(z)
  :=
  -\int_{0}^{z}\frac{\log(1-y)}{y}\,dy$$ for $z\in\mathbb{C}\setminus{[1,\infty)}$. This is called dilogarithm since it has the Taylor expansion for $|z|<1$ as $$\sum_{n=1}^{\infty}\frac{z^n}{n^2}.$$ For more details about this function, see for example [@Zagier:2007].

So by using the dilogarithm function, we have the following approximation: $$\log(\xi_N)_{k^{+}}
  \underset{N\to\infty}{\approx}
  \frac{N}{2\pi\sqrt{-1}}
  \left[
    \operatorname{Li}_2(1)-\operatorname{Li}_2(\xi^k_N)
  \right].$$ Since $\operatorname{Li}_2(1)$, which equals $\zeta(2)=\pi^2/6$ ($\zeta(z)$ is the Riemann zeta function), can be ignored for large $N$, we have $$(\xi_N)_{k^{+}}
  \underset{N\to\infty}{\approx}
  \exp
  \left[
    -\frac{N}{2\pi\sqrt{-1}}\operatorname{Li}_2(\xi^{k}_N)
  \right].$$ Similarly we have $$(\xi_N)_{k^{-}}
  \underset{N\to\infty}{\approx}
  \exp
  \left[
    -\frac{N}{2\pi\sqrt{-1}}\operatorname{Li}_2(\xi^{-k}_N)
  \right].$$

Therefore from [\[eq:Jones_R\]](#eq:Jones_R){reference-type="eqref" reference="eq:Jones_R"} the colored Jones polynomial can be (roughly) approximated as follows. $$\begin{gathered}
\label{eq:Jones_approx}
  J_N(K;\xi_N)
  \underset{N\to\infty}{\approx}
  \sum_{\text{labelings}}
  \exp
  \left[\vphantom{\sum_{\text{crossings}}}
    \frac{N}{2\pi\sqrt{-1}}
  \right.
  \\
  \left.
  \times
  \left(
    \sum_{\text{crossings}}
    \left\{
      \operatorname{Li}_2(\xi^m_N)
      +
      \operatorname{Li}_2(\xi^{\pm i}_N)
      +
      \operatorname{Li}_2(\xi^{\mp j}_N)
      +
      \operatorname{Li}_2(\xi^{\pm k}_N)
      +
      \operatorname{Li}_2(\xi^{\mp l}_N)
      +
      \text{$\log$ terms}
    \right\}
  \right)
  \right],
\end{gathered}$$ where the $\log$ terms come from powers of $\xi_N$ and $N$.

Since the term $$\label{eq:dilog}
  \sum_{\text{crossings}}
  \left\{
    \operatorname{Li}_2(\xi^m_N)
    +
    \operatorname{Li}_2(\xi^{\pm i}_N)
    +
    \operatorname{Li}_2(\xi^{\mp j}_N)
    +
    \operatorname{Li}_2(\xi^{\pm k}_N)
    +
    \operatorname{Li}_2(\xi^{\mp l}_N)
    +
    \text{$\log$ terms}
  \right\}$$ can be regarded as a function of $\xi_N^{i_1},\xi_N^{i_2},\dots,\xi_N^{i_c}$ with $i_1,i_2,\dots,i_c$ labelings of arcs, we can write it as $V(\xi_N^{i_1},\xi_N^{i_1}\dots,\xi_N^{i_c})$. Note that $m$ can be expressed as a difference of two such labelings. So we have $$\label{eq:Jones_sum}
  J_N(K;\xi_N)
  \underset{N\to\infty}{\approx}
  \sum_{i_1,i_2,\dots,i_c}
  \exp
  \left[
    \frac{N}{2\pi\sqrt{-1}}
    V(\xi_N^{i_1},\xi_N^{i_2},\dots,\xi_N^{i_c})
  \right].$$

We want to apply a method used in the proof for the figure-eight knot in §[\[subsec:proof_fig8\]](#subsec:proof_fig8){reference-type="ref" reference="subsec:proof_fig8"}. Recall that the point of the proof is to find the maximum term of the summand because the maximum dominates the asymptotic behavior. We will seek for the "maximum" term of the summation in [\[eq:Jones_sum\]](#eq:Jones_sum){reference-type="eqref" reference="eq:Jones_sum"}.

To do that we first approximate this with the following integral: $$\label{eq:Jones_integral2}
  J_N(K;\xi_N)
  \underset{N\to\infty}{\approx}
  \int_{J_1}\int_{J_2}\cdots\int_{J_c}
  \exp
  \left[
    \frac{N}{2\pi\sqrt{-1}}
    V(z_1,z_2\dots,z_c)
  \right]\,dz_1dz_2\cdots dz_c,$$ where $z_d$ corresponds to $\xi_N^{i_d}$ and $J_1,J_2,\dots,J_c$ are certain contours. (The argument here is not rigorous. In particular I do not know how to choose the contours.)

Then we will find the maximum of the absolute value of the integrand. To be more precise we apply the steepest descent method. For a precise statement, see for example [@Marsden/Hoffman:Complex_Analysis Theorem 7.2.9]).

::: theorem
[]{#thm:steepest_descent_method label="thm:steepest_descent_method"} Under certain conditions for the functions $f$, $g$, and a contour $C$, we have $$\begin{split}
  \int_{C}g(z)\exp(N\,h(z))\,dz
  &\underset{N\to\infty}{\sim}
  \frac{\exp(N\,h(z_0))\sqrt{2\pi}g(z_0)}{\sqrt{N}\sqrt{-h''(z_0)}}
  \\
  &\underset{N\to\infty}{\approx}
  \exp(N\,h(z_0)),
\end{split}$$ where $h'(z_0)=0$ and $\operatorname{Re}(h(z))$ takes its positive maximum at $z_0$.

Note that the symbol $\underset{N\to\infty}{\sim}$ means that the ratio of both sides converges to $1$ when $N\to\infty$ and that we ignore the constant term and $\sqrt{N}$ in the rough approximation $\underset{N\to\infty}{\approx}$ because $\exp(N\,h(z_0))$ grows exponentially when $N\to\infty$. $($Recall that we want to know the limit of $\log|J_N(K,\xi_N)|/N$ and so polynomial terms will not matter.$)$
:::

::: remark
In general, to apply the steepest descent method, we need to change the contour $C$ so that it passes through $z_0$.
:::

Now we apply (a multidimensional version of) this method to [\[eq:Jones_integral2\]](#eq:Jones_integral2){reference-type="eqref" reference="eq:Jones_integral2"} and we will find the the maximum of $\{\operatorname{Im}V(z_1,\dots,z_c)\mid{(z_1,z_2,\dots,z_c)\in J_1\times J_2\dots\times J_c}\}$. Let $(x_1,x_2,\dots,x_c)$ be such a point. Then we have $$\label{eq:steepest_descent}
  J_N(K;\xi_N)
  \underset{N\to\infty}{\approx}
  \exp
  \left[
    \frac{N}{2\pi\sqrt{-1}}
    V(x_1,x_2,\dots,x_c)
  \right]$$ and so we finally have $$\label{eq:limit}
  2\pi\sqrt{-1}
  \lim_{N\to\infty}
  \frac{\log{J_N(K;\xi_N)}}{N}
  =
  V(x_1,x_2,\dots,x_c).$$ Note that the point $(x_1,x_2,\dots,x_c)$ is a solution to the following equation: $$\label{eq:differential}
  \frac{\partial\,V}{\partial\,z_d}(z_1,z_2,\dots,z_c)=0$$ for $d=1,2,\dots,c$.

Remember that our argument here is far from rigor! Especially I am cheating on the following points:

-   Replacing a summation with an integral in [\[eq:Jones_integral2\]](#eq:Jones_integral2){reference-type="eqref" reference="eq:Jones_integral2"}. Here we do not know how to choose the multidimensional contour.

-   Applying the steepest descent method in [\[eq:steepest_descent\]](#eq:steepest_descent){reference-type="eqref" reference="eq:steepest_descent"}. In general, we have many solutions to the system of equations [\[eq:differential\]](#eq:differential){reference-type="eqref" reference="eq:differential"} but we do not know which solution gives the maximum. Moreover we may need to change the contour so that it passes through the solution that gives the maximum but we do not know whether this is possible or not.
