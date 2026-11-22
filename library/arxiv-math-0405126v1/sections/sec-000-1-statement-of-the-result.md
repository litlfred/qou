---
doc_id: arxiv-math-0405126v1
doc_title: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT"
section_id: sec-000-1-statement-of-the-result
section_title: "Statement of the result"
section_number: 1
pages: 2-2
source_pdf: 0405126v1.pdf
source_sha256: 713498dbe80f7319
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.945
doc_brief: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT — We study the asymptotic behaviors of the colored Jones polyno- mials of torus knots. Contrary to the works by R. Kashaev, O."
---
Let $T(a,b)$ be the $(a,b)$-torus knot for coprime integers $a$ and $b$ ($a>1$, $b>1$). Then its colored Jones polynomial $J_N\bigl(T(a,b);t\bigr)$ is given as follows [@Morton:MATPC95]. $$J_N\bigl(T(a,b);t\bigr)
  =
  \frac{t^{-ab(N^2-1)/4}}{t^{N/2}-t^{-N/2}}
  \sum_{\varepsilon=\pm1}
  \sum_{k=-(N-1)/2}^{(N-1)/2}
  \varepsilon
  t^{abk^2+k(a+\varepsilon{b})+\varepsilon/2}.$$

We will show the following theorem.

::: thm
[]{#thm label="thm"} There exists a neighborhood $U$ of $1\in\mathbb{C}$ such that if $r\in{U}$ and $r\notin\mathbb{R}$, then $$\begin{gathered}
  \lim_{N\to\infty}J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)
  =
  \frac{1}{\Delta\left(T(a,b);e^{2\pi{r}\sqrt{-1}}\right)}
  \quad\text{if $\operatorname{Im}{r}<0$},
  \label{eq:negative}
  \\
  \intertext{and}
  \lim_{N\to\infty}
  \frac{\log{J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)}}{N}
  =
  \left(1-\dfrac{1}{2abr}-\dfrac{abr}{2}\right)\pi\sqrt{-1}
  \quad\text{if $\operatorname{Im}{r}>0$}.
  \label{eq:positive}
\end{gathered}$$
:::

::: rem
To be precise, the limit in [\[eq:positive\]](#eq:positive){reference-type="eqref" reference="eq:positive"} means $$J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)
  \\
  \underset{N\to\infty}{\sim}
  P(N)e^{N(1-1/(2abr)-abr/2)\pi\sqrt{-1}}$$ for some function of $P(N)$ such that $N^{-c}<|P(N)|<N^c$ for some positive integer $c$. Here $f(N)\underset{N\to\infty}{\sim}g(N)$ means that $\lim_{N\to\infty}f(N)/g(N)=1$. Note that $\lim_{N\to\infty}\log{P(N)}/N=0$ for such $P(N)$. Note also that since the real part of the right hand side of [\[eq:positive\]](#eq:positive){reference-type="eqref" reference="eq:positive"} is positive, the formula shows that $\left|J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)\right|$ grows exponentially if $\operatorname{Im}{r}>0$.
:::

::: rem
For $r=1$, Kashaev and Tirkkonen [@Kashaev/Tirkkonen:ZAPNS200] proved that $$\left|J_N\left(T(a,b);e^{2\pi{r}\sqrt{-1}/N}\right)\right|
  \underset{N\to\infty}{\sim}
  Ck^{3/2}$$ for some constant $C$. K. Hikami and A. Kirillov study the phase factor [@Hikami/Kirillov:PHYLB] and show a relation to the $SU(2)$ Chern--Simons invariant.
:::
