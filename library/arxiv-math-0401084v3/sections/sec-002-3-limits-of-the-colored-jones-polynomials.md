---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-002-3-limits-of-the-colored-jones-polynomials
section_title: "Limits of the colored Jones polynomials"
section_number: 3
pages: 4-14
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.972
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — We calculate limits of the colored Jones polynomials of the ﬁgure- eight knot and conclude that in most cases they determine"
---
K. Habiro [@Habiro:SURIK00] and T. Le showed that the colored Jones polynomial $J_N(E;t)$ of the figure-eight knot $E$ is given as follows (see also [@Masbaum:AGT03]). $$\label{eq:Jones}
  J_N(E;t)=\sum_{n=0}^{N-1}\prod_{k=1}^{n}
           t^N\left(1-t^{-N-k}\right)\left(1-t^{-N+k}\right).$$ We will study the asymptotic behavior of $J_N(E;q_r)$ with $q_r:=\exp(2\pi{r}\sqrt{-1}/N)$ for large $N$.

We approximate $\prod_{k=1}^{n}\left(1-q_r^{-N{\pm}k}\right)$ by an integral. Note that $$\prod_{k=1}^{n}\left(1-q_r^{-N{\pm}k}\right)
  =
  \exp
  \left\{
    \frac{N}{2\pi}
    \sum_{k=1}^{n}
    \frac{2\pi}{N}
    \log\bigl(1-\exp(\pm2\pi{k}{r}\sqrt{-1}/N-2\pi{r}\sqrt{-1})\bigr)
  \right\}.$$

::: lem
[]{#lem:max_min label="lem:max_min"} If $r\not\in\mathbb{R}$ then $$\begin{gathered}
  \log\left|1-e^{2\pi{b}/N}\right|
  \le
  \log\left|1-\exp\left(sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  \le
  \log\left(1+e^{2\pi{b}}\right),
  \\
  \intertext{and}
  \log\left|1-e^{2\pi{b}}\right|
  \le
  \log\left|1-\exp\left(-sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  <
  \log\left(1+e^{4\pi|b|}\right)
\end{gathered}$$ where $r=a+b\sqrt{-1}$ with $a\in\mathbb{R}$, $0\ne{b}\in\mathbb{R}$ and $0\le{s}\le2\pi-2\pi/N$.

::: proof
*Proof.* If we put $r:=a+b\sqrt{-1}$ with $b\ne0$, we have $$\exp\left(sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)
  =
  e^{-bs+2\pi{b}}\exp\bigl((as-2\pi{a})\sqrt{-1}\bigr).$$ Therefore $\left|1-\exp\left(sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|$ is smaller (greater, respectively) than or equal to the longest (shortest, respectively) distance between $1\in\mathbb{C}$ and the circle centered at $0$ with radius $e^{-bs+2\pi{b}}$. So if $b>0$, $$1+e^{2\pi{b}}
  \ge
  \left|1-\exp\left(sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  \ge
  e^{-b(2\pi-2\pi/N)+2\pi{b}}-1
  =
  e^{2\pi{b}/N}-1$$ and if $b<0$, $$1+e^{2\pi{b}}
  \ge
  \left|1-\exp\left(sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  \ge
  1-e^{2\pi{b}/N}.$$

Similarly if $b>0$, $$e^{2\pi{b}}-1
  \le
  \left|1-\exp\left(-sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  \le
  e^{b(2\pi-2\pi/N)+2\pi{b}}+1
  <
  e^{4\pi{b}}+1$$ and if $b<0$, $$1-e^{2\pi{b}}
  \le
  \left|1-\exp\left(-sr\sqrt{-1}-2\pi{r}\sqrt{-1}\right)\right|
  \le
  e^{4\pi{b}-2\pi{b}/N}+1
  \le
  e^{2\pi{b}}+1.$$ ◻
:::
:::

We put $$\begin{gathered}
  \varphi_{N,\pm}(n)
  :=
  \sum_{k=1}^{n}
  \frac{2\pi}{N}
  \log
  \bigl(
    1-\exp(\pm2\pi{k}r\sqrt{-1}/N-2\pi{r}\sqrt{-1})
  \bigr)
  \\
  -
  \int_{0}^{2{\pi}n/N}
  \log
  \bigl(
    1-\exp({\pm}sr\sqrt{-1}-2{\pi}r\sqrt{-1})
  \bigr)\,ds.
\end{gathered}$$

::: lem
[]{#lem:logN label="lem:logN"} If $r\not\in\mathbb{R}$, then there exist constants $d\ge1$ and $\delta>0$ such that $$\begin{gathered}
  \left|\operatorname{Re}\varphi_{N,+}(n)\right|
  <
  \frac{2\pi{d}}{N}
  \left\{
    \log\left(1+e^{2\pi{b}}\right)
    -
    \log\left(\frac{2\pi|b|\delta}{N}\right)
  \right\}
  \\
  \intertext{and}
  \left|\operatorname{Re}\varphi_{N,-}(n)\right|
  <
  \frac{2\pi{d}}{N}
  \left\{
    \log\left(1+e^{4\pi|b|}\right)
    -
    \log\left|1-e^{2\pi{b}}\right|
  \right\}
\end{gathered}$$ for sufficiently large $N$.
:::

::: proof
*Proof.* First we note that if a real continuous function $g(s)$ ($0\le{s}\le{A}$) has $c$ extremes, then $$\left|
    \int_{0}^{nA/N}g(s)\,ds
    -
    \sum_{k=1}^{n}\frac{A}{N}g(kA/N)
  \right|
  \le
  (2c+1)\frac{A}{N}
  \left(\max_{0\le{s}\le{A}}{g(s)}-\min_{0\le{s}\le{A}}{g(s)}\right).$$ This is because if $g$ is monotonic in $[jA/N,(j+l)A/N]$ $$\begin{gathered}
  \left|
    \int_{jA/N}^{(j+l)A/N}g(s)\,ds
    -
    \sum_{k=j+1}^{j+l}\frac{A}{N}g(kA/N)
  \right|
  \\
  \le
  \frac{A}{N}
  \left|
    g(jA/N)-g((j+l)A/N)
  \right|
  \le
  \frac{A}{N}
  \left(
    \max_{0\le{s}\le{A}}{g(s)}-\min_{0\le{s}\le{A}}{g(s)}
  \right)
\end{gathered}$$ and there are $c+1$ such intervals. For other $c$ intervals $[jA/N,(j+1)A/N]$ clearly $$\left|
    \int_{jA/N}^{(j+1)A/N}g(s)\,ds
    -
    \frac{A}{N}g((j+1)A/N)
  \right|
  \le
  \frac{A}{N}
  \left(
    \max_{0\le{s}\le{A}}{g(s)}-\min_{0\le{s}\le{A}}{g(s)}
  \right)$$ holds.

Therefore from Lemma [\[lem:max_min\]](#lem:max_min){reference-type="ref" reference="lem:max_min"} there exists a constant $d$ such that $$\begin{gathered}
  \left|
    \operatorname{Re}\varphi_{N,+}(n)
  \right|
  \le
  \frac{2\pi{d}}{N}
  \left\{
    \log\left(1+e^{2\pi{b}}\right)
    -
    \log\left|1-e^{2\pi{b}/N}\right|
  \right\}
  \\
  \intertext{and}
  \left|\operatorname{Re}\varphi_{N,-}(n)\right|
  <
  \frac{2\pi{d}}{N}
  \left\{
    \log\left(1+e^{4\pi|b|}\right)
    -
    \log\left|1-e^{2\pi{b}}\right|
  \right\}
\end{gathered}$$ Since if $b>0$, $$e^{2\pi{b}/N}-1
  =
  \frac{2\pi{b}}{N}+\frac{(2\pi{b})^2}{2N^2}+\cdots
  >
  \frac{2\pi{b}}{N}$$ for any $N$ and if $b<0$, $$1-e^{2\pi{b}/N}
  =
  -\frac{2\pi{b}}{N}-\frac{(2\pi{b})^2}{2N^2}-\cdots
  >
  -\frac{2\pi{b}\delta}{N}$$ for any $0<\delta<1$ if $N$ is sufficiently large. This completes the proof. ◻
:::

Therefore we have $$D^{-1}N^{-d}
  <
  \left|
    \exp\left(\frac{N}{2\pi}\varphi_{N,\pm}(n)\right)
  \right|
  <
  DN^d$$ for some constants $D>0$ and $d\ge1$ for sufficient large $N$.

We also have

::: lem
If $r\not\in\mathbb{R}$, then for any positive number $\varepsilon$ $$\left|\operatorname{Im}\varphi_{N,\pm}(n)\right|
  <
  \varepsilon$$ for sufficiently large $N$.
:::

::: proof
*Proof.* Clearly $$\begin{gathered}
  \max_{2\pi/N\le{s}\le2\pi-2\pi/N}
  \arg\bigl(1-\exp(\pm{sr}\sqrt{-1}-2\pi{r}\sqrt{-1})\bigr)
  \\
  -
  \min_{2\pi/N\le{s}\le2\pi-2\pi/N}
  \arg\bigl(1-\exp(\pm{sr}\sqrt{-1}-2\pi{r}\sqrt{-1})\bigr)
\end{gathered}$$ is bounded by a positive constant depending only $r$. So we can show as in the previous lemma that $$\begin{gathered}
  \left|\operatorname{Im}\varphi_{N,\pm}(n)\right|
  =
  \Biggl|
    \sum_{k=1}^{n}\frac{2\pi}{N}
    \arg\bigl(1-\exp(\pm{sr}\sqrt{-1}-2\pi{r}\sqrt{-1})\bigr)
  \\
    -
    \int_{0}^{2\pi{n}/N}
    \arg\bigl(1-\exp(\pm{sr}\sqrt{-1}-2\pi{r}\sqrt{-1})\bigr)
  \Biggr|
\end{gathered}$$ is bounded by a positive constant times $1/N$ and the result follows. ◻
:::

Putting $$\chi_{N,\pm}(n):=\exp\left(\frac{N}{2\pi}\varphi_{N,\pm}(n)\right),$$ we have $$\begin{gathered}
  \prod_{k=1}^{n}
  \left(1-q_r^{-N\pm{k}}\right)
  \\
  =
  \chi_{N,\pm}(n)
  \exp
  \left\{
    \frac{N}{2\pi}
    \int_{0}^{2\pi{n}/N}
    \log\bigl(1-\exp(\pm{sr}\sqrt{-1}-2\pi{r}\sqrt{-1})\bigr)\,ds
  \right\}
\end{gathered}$$ with $D^{-1}N^{-d}<\left|\chi_{N,\pm}(n)\right|<DN^d$ and $|\arg\chi_{N,\pm(n)}|<\varepsilon$ if $r\not\in\mathbb{R}$. Therefore $$\begin{split}
  &\prod_{k=1}^{n}
  \left(1-q_r^{-N\pm{k}}\right)
  \\
  &\quad=
  \chi_{N,\pm}(n)
  \exp
  \left\{
    \frac{\pm{N}}{2\pi{r}\sqrt{-1}}
    \int_{\exp(-2\pi{r}\sqrt{-1})}
        ^{\exp(\pm2\pi{nr}\sqrt{-1}/N-2\pi{r}\sqrt{-1})}
    \frac{\log(1-u)}{u}\,du
  \right\}
  \\
  &\quad=
  \chi_{N,\pm}(n)
  \exp
  \left\{
    \frac{\pm{N}}{2\pi{r}\sqrt{-1}}
    \Bigl(
      \operatorname{Li}_2\left(m^{-2}\right)-\operatorname{Li}_2\left(q_r^{\pm{n}}m^{-2}\right)
    \Bigr)
  \right\}.
\end{split}$$ Here we put $$m:=\exp(\pi{r}\sqrt{-1})$$ and $$\operatorname{Li}_2(z):=-\int_{0}^{z}\frac{\log(1-u)}{u}\,du$$ is the dilogarithm function.

Thus we have $$\begin{split}
  &J_{N}(E;q_r)
  \\
  &\quad=
  \sum_{n=0}^{N-1}
  q_r^{Nn}
  \prod_{k=1}^{n}
  \left(1-q_r^{-N+k}\right)
  \left(1-q_r^{-N-k}\right)
  \\
  &\quad=
  \sum_{n=0}^{N-1}
  q_r^{Nn}
  \chi_{N,+}(n)
  \exp
  \left\{
    \frac{N}{2\pi{r}\sqrt{-1}}
    \Bigl(
      \operatorname{Li}_2\left(m^{-2}\right)-\operatorname{Li}_2\left(q_r^{n}m^{-2}\right)
    \Bigr)
  \right\}
  \\
  &\qquad\qquad\qquad\times
  \chi_{N,-}(n)
  \exp
  \left\{
    \frac{-N}{2\pi{r}\sqrt{-1}}
    \Bigl(
      \operatorname{Li}_2\left(m^{-2}\right)-\operatorname{Li}_2\left(q_r^{-n}m^{-2}\right)
    \Bigr)
  \right\}
  \\
  &\quad=
  \sum_{n=0}^{N-1}
  \chi_N(n)
  \exp
  \left\{
    \frac{N}{2\pi{r}\sqrt{-1}}
    \Bigl(
      \operatorname{Li}_2\left(q_r^{-n}m^{-2}\right)-\operatorname{Li}_2\left(q_r^{n}m^{-2}\right)
  \right.
  \\
  &\qquad\qquad\qquad\qquad
  \left.\vphantom{\frac{N}{2\pi{r}\sqrt{-1}}}
      +\bigl(\log\left(-q_r^n\right)+\pi\sqrt{-1}\bigr)(\log{m^2}
    \Bigr)
  \right\}
  \\
  &\quad=
  \sum_{n=0}^{N-1}
  \chi_N(n)
  \exp
  \left\{
    \frac{N}{2\pi{r}\sqrt{-1}}H\left(q_r^n,m^2\right)
  \right\},
\end{split}$$ where we put $$H(\xi,\eta)
  :=
  \operatorname{Li}_2\left(\xi^{-1}\eta^{-1}\right)-\operatorname{Li}_2\left(\xi\eta^{-1}\right)
  +\left(\log(-\xi)+\pi\sqrt{-1}\right)\log{\eta}$$ and $\chi_N(n):=\chi_{N,+}(n)\chi_{N,-}(n)$. Note that $D^{-2}N^{-2d}<|\chi(n)|<D^2N^{2d}$. Note also that we use $\log(-\xi)+\pi\sqrt{-1}$ instead of $\log\xi$ since we choose the branch of $\log$ as $(0,+\infty)$ and that of $\operatorname{Li}_2$ as $(1,+\infty)$.

Let $\Psi_N(z)$ be an analytic function such that $\Psi_N\bigl(\exp(2\pi{n}\sqrt{-1}/N)\bigr)=\chi_N(n)$, that $P(N^{-1})<|\Psi_N(z)|<Q(N)$ with some polynomials $P$ and $Q$, and that $|\arg\Psi_N(z)|<\varepsilon$ near $C$ defined below. Since the residue around $z=\exp(2\pi{n}\sqrt{-1}/N)$ of $1/\bigl(z(1-z^{-N})\bigr)$ is $1/N$, we have from the residue theorem $$J_N(E;q_r)   =   1+   \frac{N}{2\pi\sqrt{-1}}   \int_{C}   \frac{\Psi_N(z)}{z(1-z^{-N})}   \exp   \left(\frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)\right)   dz,$$ where $C=C_{+}{\cup}C_{-}$ is defined by $$\begin{cases}
  C_{+}&:=
  \left\{
    z\in\mathbb{C}\mid|z|=1+\kappa,\pi/N\le\arg{z}\le2\pi-\pi/N
  \right\}
  \\
  &\phantom{:=}\quad
  \cup
  \left\{
    t\exp( \sqrt{-1}/N)\in\mathbb{C}\mid1-\kappa\le{t}\le1+\kappa
  \right\}
  \\
  &\phantom{:=}\quad
  \cup
  \left\{
    t\exp(-\sqrt{-1}/N)\in\mathbb{C}\mid1-\kappa\le{t}\le1+\kappa
  \right\}
  \\
  C_{-}&:=
  \left\{
    z\in\mathbb{C}\mid|z|=1-\kappa,\pi/N\le\arg{z}\le2\pi-\pi/N
  \right\}
\end{cases}$$ for small $\kappa>0$. Now we have $$\begin{split}
  &J_N(E;q_r)
  \\   &\quad=
  1+
  \frac{N}{2\pi\sqrt{-1}}
  \int_{C_{+}}
  \frac{\Psi_N(z)}{z}
  \exp
  \left(\frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)\right)
  dz
  \\
  &\quad\quad
  +
  \frac{N}{2\pi\sqrt{-1}}
  \int_{C_{+}}
  \frac{\Psi_N(z)}{z(1-z^{-N})}
  \exp
  \left(
    \frac{N}{2\pi{r}\sqrt{-1}}
    \left\{
      H(z^r,m^2)
      -
      2\pi\sqrt{-1}\log{z^r}
    \right\}
  \right)
  dz
  \\
  &\quad\quad
  +
  \frac{N}{2\pi\sqrt{-1}}
  \int_{C_{-}}
  \frac{\Psi_N(z)}{z(z^{N}-1)}
  \exp
  \left(
    \frac{N}{2\pi{r}\sqrt{-1}}
    \left\{
      H(z^r,m^2)
      +
      2\pi\sqrt{-1}\log{z^r}
    \right\}
  \right)
  dz.
\end{split}$$

Here we want to apply the steepest descent method (or the saddle point method, see for example [@Marsden/Hoffman:Complex_Analysis Theorem 7.2.9])

::: thm
[]{#thm:steepest_descent_method label="thm:steepest_descent_method"} Let $\Gamma\colon[a,b]\to\mathbb{C}$ be a $C^1$ curve. Let $h(z)$ be a continuous function on $\Gamma$ that is analytic at $z_0=\Gamma(t_0)$, and $g_N(z)$ be a continuous function on $z\in{\Gamma}$ for each $N=1,2,3,\dots$ with $g_N(z_0)\ne0$ such that $|g_N(z)|<N^p$ for some $p>0$. We also assume the following conditions: For sufficient large integer $N$,

1.  $\int_{\Gamma}g_N(z)\exp\bigl(Nh(z)\bigr)dz$ converges absolutely.

2.  $d\,h(z_0)/dz=0$ and $d^2\,h(z_0)/dz^2\ne0$.

3.  $\operatorname{Im}\bigl(Nh(z)\bigr)$ is constant for $z$ on $c$ in some neighborhood of $z_0$.

4.  $\operatorname{Re}\bigl(Nh(z)\bigr)$ takes its strict maximum along $\Gamma$ at $z_0$.

Then $$\int_{\Gamma}g_N(z)\exp\bigl(Nh(z)\bigr)dz
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{2\pi}g_N(z_0)\exp\bigl(Nh(z_0)\bigr)}
       {\sqrt{N}\sqrt{-d^2\,h(z_0)/dz^2}}$$ for appropriate chosen square roots. Here $\underset{N\to\infty}{\sim}$ means the ratio of both hand sides goes to $1$ when $N\to\infty$.
:::

Putting $h(z):=\frac{1}{2\pi{r}\sqrt{-1}}H(z^r,m^2)$, $g(z):=\Psi_N(z)/z$, we can prove the following proposition.

::: prop
We have $$\begin{gathered}
  \int_{C_{+}}
  \frac{\Psi_N(z)}{z}
  \exp
  \left(\frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)\right)
  dz
  \\
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
  \exp\left(\frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)\right)
\end{gathered}$$ with $$y:=\frac{m^4-m^2+1-\sqrt{(m^2+m+1)(m^2+m-1)(m^2-m+1)(m^2-m-1)}}{2m^2},$$ where the branch of the square root in the definition of $y$ is taken so that if $m=-1$, then $y=\exp(-\pi\sqrt{-1}/3)$. Note that $y$ satisfies the following equality: $$\label{eq:y}
  y+y^{-1}=m^2-1+m^{-2}.$$
:::

::: proof
*Proof.* First of all we calculate derivatives of $H(z^r,m^2)$. We have $$\begin{split}
  \frac{\partial\,H(z^r,m^2)}{\partial{z}}
  &=
  \frac{\partial\,H(\xi,\eta)}{\partial\xi}
  \frac{d\,z^r}{dz}
  \\
  &=
  \frac{rz^{r-1}}{z^r}
  \left\{
    \log(1-z^{-r}m^{-2})
    +
    \log(1-z^{r}m^{-2})
    +
    \log{m^2}
  \right\}
  \\
  &=
  \frac{r}{z}
  \log\left(m^2-(z^{r}+z^{-r})+m^{-2}\right)
\end{split}$$ and $$\begin{gathered}
  \frac{\partial^2\,H(z^r,m^2)}{\partial{z^2}}
  \\
  =
  -
  \frac{r}{z^2}\log\left(m^2-(z^{r}+z^{-r})+m^{-2}\right)
  +
  \frac{r}{z}
  \times
  \frac{-rz^{r-1}+rz^{-r-1}}{m^2-(z^{r}+z^{-r}+m^{-2})}.
\end{gathered}$$ Therefore $y^{1/r}$ gives a solution to $\partial\,H(z^r,m^2)/\partial{z}=0$, and $$\frac{\partial^2\,H(z^r,m^2)}{\partial{z^2}}\Biggr|_{z=y^{1/r}}
  =
  r^2y^{-2/r}(-y+y^{-1}).$$

Now we will consider the case when $r=1$ precisely. In this case $y=\exp(-\pi\sqrt{-1}/3)$.

We change $C_{+}$ to ${C'}_{+}$ where $$\begin{split}
  {C'}_{+}&:=
  \left\{
    z\in\mathbb{C}\mid|z|=1,\pi/N\le\arg{z}\le2\pi-\pi/N
  \right\}
  \\
  &\phantom{:=}\quad
  \cup
  \left\{
    t\exp( \sqrt{-1}/N)\in\mathbb{C}\mid1-\kappa\le{t}\le1
  \right\}
  \\
  &\phantom{:=}\quad
  \cup
  \left\{
    t\exp(-\sqrt{-1}/N)\in\mathbb{C}\mid1-\kappa\le{t}\le1
  \right\}.
\end{split}$$ Then on the unit circle $$\label{eq:H_on_circle}
\begin{split}
  H(\exp(\theta\sqrt{-1}),1)
  &=
  \operatorname{Li}_2(\exp(-\theta\sqrt{-1}))-\operatorname{Li}_2(\exp(\theta\sqrt{-1}))
  \\
  &=
  \left\{
    \frac{\pi^2}{6}
    -
    \frac{2\pi-\theta}{2}
    \left(\pi-\frac{2\pi-\theta}{2}\right)
    +
    2\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{2\pi-\theta}{2}\right)
  \right\}
  \\
  &\quad
  -
  \left\{
    \frac{\pi^2}{6}
    -
    \frac{\theta}{2}\left(\pi-\frac{\theta}{2}\right)
    +
    2\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{\theta}{2}\right)
  \right\}
  \\
  &=
  -4\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{\theta}{2}\right).
\end{split}$$ Here we use the following formula: $$\label{eq:dilog}
  \operatorname{Li}_2\bigl(\exp(\beta\sqrt{-1})\bigr)
  =
  \frac{\pi^2}{6}
  -
  \frac{\beta}{2}\left(\pi-\frac{\beta}{2}\right)
  +
  2\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{\beta}{2}\right)$$ for $0\le\beta\le2\pi$ and the fact that $\operatorname{\text{\tencyr\cyracc L}}$ is an odd function with period $\pi$. (See for example [@Milnor:BULAM382 p. 18].) So on ${C'}_{+}$ $\operatorname{Im}{H(z,1)}$ takes its maximum at $y$ and near $y$ $\operatorname{Re}{H(z,1)}=0$. Moreover in this case $$\frac{\partial^2\,H(z,1)}{\partial{z^2}}\Biggr|_{z=y}
  =
  \frac{-3-\sqrt{3}\sqrt{-1}}{2}
  \ne0.$$ Therefore we can apply the saddle point method and the proposition follows when $r=1$.

If $r$ is near $1$ we can also apply the saddle point method similarly from the continuity of $H(z^r,m^2)$ with respect to $r$, completing the proof. ◻
:::

From Lemma [\[lem:C\_-\]](#lem:C_-){reference-type="ref" reference="lem:C_-"} below we see $$\begin{split}
  &
  \left|
  \int_{C_{+}}
  \frac{\Psi_N(z)}{z(1-z^{-N})}
  \exp
  \left(
    \frac{N}{2\pi{r}\sqrt{-1}}
    \left\{
      H(z^r,m^2)
      -
      2\pi\sqrt{-1}\log{z^r}
    \right\}
  \right)
  dz
  \right|
  \\
  &\quad
  \le
  \int_{C_{+}}
  \frac{\left|\Psi_N(z)\right|}{\left|z(1-z^{-N})\right|}
  \exp
  \left(
    \frac{N}{2\pi}
    \operatorname{Im}
    \left(
      \frac{H(z^r,m^2)-2\pi\sqrt{-1}\log{z^r}}{r}
    \right)
  \right)
  |dz|
  \\
  &\quad
  <
  \exp
  \left(
    \frac{N}{2\pi}
    \operatorname{Im}\left(\frac{H(y,m^2)}{r}\right)
  \right)
  \int_{C_{+}}
  \frac{\left|\Psi_N(z)\right|}{\left|z(1-z^{-N})\right|}
  |dz|
  \\
  &\quad
  \le
  \exp
  \left(
    \frac{N}{2\pi}
    \operatorname{Im}\left(\frac{H(y,m^2)}{r}\right)
  \right)
  \frac{|C_{+}|Q(N)}{(1+\kappa)\left(1-(1+\kappa)^{-N}\right)}
\end{split}$$ and $$\begin{gathered}
  \left|
    \int_{C_{-}}
    \frac{\Psi_N(z)}{z(z^{N}-1)}
    \exp
    \left(
      \frac{N}{2\pi{r}\sqrt{-1}}
      \left\{
        H(z^r,m^2)
        +
        2\pi\sqrt{-1}\log{z^r}
      \right\}
    \right)
    dz
  \right|
  \\
  <
  \exp
  \left(
    \frac{N}{2\pi}
    \operatorname{Im}\left(\frac{H(y,m^2)}{r}\right)
  \right)
  \frac{|C_{-}|Q(N)}{(1-\kappa)\left(1-(1-\kappa)^{N}\right)},
\end{gathered}$$ where $|C_{\pm}|$ is the length of $C_{\pm}$. Now we have $$\label{eq:log/N}
\begin{split}
  &
  \log\bigl(J_N(E;q_r)\bigr)\big/N
  -
  \frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}
  -
  \log\left(
        \frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
      \right)\Big/N
  \\
  &\quad
  =
  \log
  \Biggl(
    \frac{r\sqrt{N}\sqrt{y-y^{-1}}}{\sqrt{2\pi}\Psi_N(y^{1/r})}
    \exp\left(\frac{-N}{2\pi{r}\sqrt{-1}}H(y,m^2)\right)
  \\
  &\quad\quad
  +
  \frac{N}{2\pi\sqrt{-1}}
  \frac{\int_{C_+}\frac{\Psi_N(z)}{z}
        \exp\left(\frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)\right)\dz}
       {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
         \exp\left(
               \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
             \right)}
  \\
  &\quad\quad
  +
  \frac{N}{2\pi\sqrt{-1}}
  \frac{\int_{C_+}\frac{\Psi_N(z)}{z(1-z^{-N})}
        \exp
        \left(
          \frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)-2\pi\sqrt{-1}\log{z^r}
        \right)\dz}
       {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
         \exp\left(
               \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
             \right)}
  \\
  &\quad\quad
  +
    \frac{N}{2\pi\sqrt{-1}}
    \frac{\int_{C_-}\frac{\Psi_N(z)}{z(z^{N}-1)}
          \exp
          \left(
            \frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)+2\pi\sqrt{-1}\log{z^r}
          \right)\dz}
         {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
           \exp\left(
                 \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
               \right)}
  \Biggr)
  \Bigg/N.
\end{split}$$ We will estimate each term in $\log$. First we observe that $$\begin{gathered}
  \left|
    \frac{r\sqrt{N}\sqrt{y-y^{-1}}}{\sqrt{2\pi}\Psi_N(y^{1/r})}
    \exp\left(\frac{-N}{2\pi{r}\sqrt{-1}}H(y,m^2)\right)
  \right|
  \\
  =
  \frac{|r|\sqrt{N}|\sqrt{y-y^{-1}}|}{\sqrt{2\pi}\left|\Psi_N(y^{1/r})\right|}
  \exp\left(-N\operatorname{Re}\left(\frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}\right)\right)
\end{gathered}$$ goes to $0$. This is because $P(N^{-1})<|\Psi_N(y^{1/r})|<Q(N)$ for polynomials $P$ and $Q$, and $\operatorname{Re}\bigl(H(y,m^2)/2\pi{r}\sqrt{-1}\bigr)>0$ if $r$ is near $1$ since when $r=1$ $$\frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}
  =
  \frac{H(\exp(-\pi\sqrt{-1}/3),1)}{2\pi\sqrt{-1}}
  =
  \frac{2\operatorname{\text{\tencyr\cyracc L}}(\pi/6)}{\pi}
  >
  0$$ from [\[eq:H_on_circle\]](#eq:H_on_circle){reference-type="eqref" reference="eq:H_on_circle"}. Next we have $$\lim_{N\to\infty}
  \frac{\int_{C_+}\frac{\Psi_N(z)}{z}
        \exp\left(\frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)\right)\dz}
         {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
           \exp\left(
                 \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
               \right)}
  =1,$$ $$\begin{split}
  &
  \left|
    \frac{N}{2\pi\sqrt{-1}}
    \frac{\int_{C_+}\frac{\Psi_N(z)}{z(1-z^{-N})}
          \exp
          \left(
            \frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)-2\pi\sqrt{-1}\log{z^r}
          \right)\dz}
         {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
           \exp\left(
                 \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
               \right)}
  \right|
  \\
  &\quad
  <
  \frac{|rN^{3/2}\sqrt{y-y^{-1}}||C_{+}|Q(N)}
        {(2\pi)^{3/2}|\Psi_N(y^{1/r}|)
         (1+\kappa)\left(1-(1+\kappa)^{-N}\right)}
  \\
  &\quad
  <
  \frac{|rN^{3/2}\sqrt{y-y^{-1}}||C_{+}|Q(N)(1+N\kappa)}
        {(2\pi)^{3/2}P(N^{-1}))(1+\kappa)N\kappa}
\end{split}$$ and $$\begin{split}
  &
  \left|
    \frac{N}{2\pi\sqrt{-1}}
    \frac{\int_{C_-}\frac{\Psi_N(z)}{z(z^{N}-1)}
          \exp
          \left(
            \frac{N}{2\pi{r}\sqrt{-1}}H(z^r,m^2)+2\pi\sqrt{-1}\log{z^r}
          \right)\dz}
         {\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}
           \exp\left(
                 \frac{N}{2\pi{r}\sqrt{-1}}H(y,m^2)
               \right)}
  \right|
  \\
  &\quad
  <
  \frac{|rN^{3/2}\sqrt{y-y^{-1}}||C_{-}|Q(N)}
       {(2\pi)^{3/2}|\Psi_N(y^{1/r}|)
         (1-\kappa)\left(1-(1-\kappa)^{N}\right)}
  \\
  &\quad
  <
  \frac{|rN^{3/2}\sqrt{y-y^{-1}}||C_{-}|Q(N)}
       {(2\pi)^{3/2}P(N^{-2})(1-\kappa)(\kappa+(N-1)\kappa^2/2)}.
\end{split}$$ So we see that the absolute values of the first, third, and fourth terms in $\log$ in [\[eq:log/N\]](#eq:log/N){reference-type="eqref" reference="eq:log/N"} are smaller than a polynomial in $N$. Therefore [\[eq:log/N\]](#eq:log/N){reference-type="eqref" reference="eq:log/N"} goes to $0$ when $N\to\infty$ and so we have $$\begin{split}
  &\lim_{N\to\infty}\frac{\log\bigl(J_N(E;q_r)\bigr)}{N}
  \\
  &\quad=
  \frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}
  +
  \lim_{N\to\infty}
  \log
  \left(\frac{\sqrt{2\pi}\Psi_N(y^{1/r})}{r\sqrt{N}\sqrt{y-y^{-1}}}\right)
  \big/N
  \\
  &\quad=
  \frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}
  +
  \lim_{N\to\infty}\frac{\log\left|\Psi_N(y^{1/r})\right|}{N}
  +
  \sqrt{-1}\lim_{N\to\infty}\frac{\arg\Psi_N(y^{1/r})}{N}
  \\
  &\quad=
  \frac{H(y,m^2)}{2\pi{r}\sqrt{-1}}
\end{split}$$ since $P(N^{-1})<|\Psi_N(y^{1/r})|<Q(N)$ and $|\arg\Psi_N(y^{1/r})|<\varepsilon$.

::: lem
[]{#lem:C_- label="lem:C_-"} There exists a neighborhood $U'$ of $1\in\mathbb{C}$ such that if $r{\in}U'$, $$\label{eq:ineq}
  \operatorname{Im}
  \left(
    \frac{H\left(z^r,m^2\right)\mp2\pi\sqrt{-1}\log{z^r}}{r}
  \right)
  <
  \operatorname{Im}
  \left(
    \frac{H(y,m^2)}{r}
  \right)$$ for $z\in{C_{\pm}}$.
:::

::: proof
*Proof.* We will show that the inequality holds when $r=1$. Then from the compactness of $C_{\pm}$ and the continuity we see that there exists such a neighborhood $U'$ of $1$.

Put $$\begin{split}
  h_{\mp}(z)
  &:=
  H(z,1)\mp2\pi\sqrt{-1}\log{z}-H\bigl(\exp(-\pi\sqrt{-1}/3),1\bigr)
  \\
  &=
  \operatorname{Li}_2(1/z)-\operatorname{Li}_2(z)\mp2\pi\sqrt{-1}\log{z}
  -\operatorname{Li}_2\left(e^{\pi\sqrt{-1}/3}\right)
  +\operatorname{Li}_2\left(e^{-\pi\sqrt{-1}/3}\right).
\end{split}$$ and we regard it as a function of $\rho$ and $\theta$ with $z=\rho\exp(\theta\sqrt{-1})$; that is $$\begin{gathered}
  h_{\mp}(\rho,\theta)
  =
  \operatorname{Li}_2\left(\rho^{-1}{e}^{-\theta\sqrt{-1}}\right)
  -
  \operatorname{Li}_2\left(\rho{e}^{\theta\sqrt{-1}}\right)
  \pm
  2\pi\theta
  \mp
  2\pi\sqrt{-1}\log{\rho}
  \\
  -\operatorname{Li}_2\left(e^{\pi\sqrt{-1}/3}\right)
  +\operatorname{Li}_2\left(e^{-\pi\sqrt{-1}/3}\right).
\end{gathered}$$ We also put $$\begin{cases}
  D_{+}:=\{z\in\mathbb{C}\mid|z|\ge1\},
  \\
  D_{-}:=\{z\in\mathbb{C}\mid|z|\le1\}.
\end{cases}$$ We will show that $\operatorname{Im}{h_{\mp}(\rho,\theta)}$ on $D_{\pm}$ takes its unique maximum $0$ at $\exp(-\pi\sqrt{-1}/3)$.

Since $$\frac{\partial\,h_{\mp}(\rho,\theta)}{\partial\theta}
  =
  \sqrt{-1}\log\left(1-\rho^{-1}{e}^{-\theta\sqrt{-1}}\right)
  +
  \sqrt{-1}\log\left(1-\rho{e}^{\theta\sqrt{-1}}\right)
  \pm
  2\pi,$$ we have $$\frac{\partial\,\operatorname{Im}{h_{\mp}(\rho,\theta)}}{\partial\,\theta}
  =
  \log
  \biggl|
    \left(1-\rho^{-1}{e}^{-\theta\sqrt{-1}}\right)
    \left(1-\rho     {e}^{ \theta\sqrt{-1}}\right)
  \biggr|.$$ Since $$\begin{split}
  \left|
    \left(1-\rho^{-1}{e}^{-\theta\sqrt{-1}}\right)
    \left(1-\rho     {e}^{ \theta\sqrt{-1}}\right)
  \right|^2
  &=
  \left(1+\rho^{-2}-2\rho^{-1}\cos\theta\right)
  \left(1+\rho^{ 2}-2\rho     \cos\theta\right)
  \\
  &=
  \left(\rho+\rho^{-1}-2\cos\theta\right)^2,
\end{split}$$ $\operatorname{Im}{h_{\mp}(\rho,\theta)}$ takes its maximum at $\theta=2\pi-\arccos\left(\dfrac{\rho+\rho^{-1}-1}{2}\right)$ for a fixed $\rho$ if $\left(3-\sqrt{5}\right)/2<\rho<\left(3+\sqrt{5}\right)/2$.

Now we put $\theta(\rho):=2\pi-\arccos\left(\dfrac{\rho+\rho^{-1}-1}{2}\right)$ and denote $h_{\mp}(\rho,\theta(\rho))$ by $h_{\mp}(\rho)$. Since $$\frac{\partial\,h_{\mp}(\rho,\theta)}{d\rho}
  =
  \frac{1}{\rho}
  \left\{
    \log\left(1-\rho^{-1}{e}^{-\theta\sqrt{-1}}\right)
    +
    \log\left(1-\rho{e}^{\theta\sqrt{-1}}\right)
    \mp
    2\pi\sqrt{-1}
  \right\}$$ and $$\frac{d\,\theta(\rho)}{d\rho}
  =
  \frac{1-\rho^{-2}}{2\sin{\theta(\rho)}}$$ we have $$\begin{gathered}
  \frac{d\,h_{\mp}(\rho)}{d\rho}
  =
  \left\{
    \frac{1}{\rho}+\frac{\sqrt{-1}(1-\rho^{-2})}{2\sin\theta(\rho)}
  \right\}
  \\
  \times
  \left\{
    \log
    \biggl(
      \left(1-\rho^{-1}{e}^{-\theta(\rho)\sqrt{-1}}\right)
      \left(1-\rho     {e}^{ \theta(\rho)\sqrt{-1}}\right)
    \biggr)
    \mp2\pi\sqrt{-1}
  \right\}.
\end{gathered}$$ Therefore $$\begin{split}
  \frac{d\,\operatorname{Im}{h_{\mp}(\rho)}}{d\rho}
  &=
  \frac{1}{\rho}
  \left\{
    \arg
    \biggl(
      \left(1-\rho^{-1}{e}^{-\theta(\rho)\sqrt{-1}}\right)
      \left(1-\rho     {e}^{ \theta(\rho)\sqrt{-1}}\right)
    \biggr)
    \mp2\pi
  \right\}
  \\
  &\quad
  +
  \frac{1-\rho^{-2}}{2\sin\theta(\rho)}
  \left\{
    \log
    \biggl|
      \left(1-\rho^{-1}{e}^{-\theta(\rho)\sqrt{-1}}\right)
      \left(1-\rho     {e}^{ \theta(\rho)\sqrt{-1}}\right)
    \biggr|
  \right\}
  \\
  &=
  \frac{1}{\rho}
  \left\{
    \arg
    \biggl(
      \left(1-\rho^{-1}{e}^{-\theta(\rho)\sqrt{-1}}\right)
      \left(1-\rho     {e}^{ \theta(\rho)\sqrt{-1}}\right)
    \biggr)
    \mp2\pi
  \right\}
\end{split}$$ since $$\biggl|
    \left(1-\rho^{-1}{e}^{-\theta(\rho)\sqrt{-1}}\right)
    \left(1-\rho     {e}^{ \theta(\rho)\sqrt{-1}}\right)
  \biggr|
  =1.$$

Thus we have $$\begin{cases}
  \dfrac{d\,\operatorname{Im}{h_{+}(\rho)}}{d\rho}>0,
  \\[3mm]
  \dfrac{d\,\operatorname{Im}{h_{-}(\rho)}}{d\rho}<0
\end{cases}$$ and so $\operatorname{Im}{h_{\pm}(\rho)}$ on $D_{\mp}$ takes maximum at $\rho=1$.

Since $\theta(1)=-\pi/3$, $\operatorname{Im}{h_{\mp}(1)}=0$. Therefore [\[eq:ineq\]](#eq:ineq){reference-type="eqref" reference="eq:ineq"} holds when $r=1$. ◻
:::

Now we consider the case when $r\in\mathbb{R}$. In this case $m^2+m^{-2}=2\cos(2\pi{r})$ and so $$y=\exp\bigl(-\alpha(r)\sqrt{-1}\bigr)$$ with $\alpha(r):=\arccos(\cos(2\pi{r})-1/2)$ ($0\le\arccos{x}\le{\pi}$). From [\[eq:dilog\]](#eq:dilog){reference-type="eqref" reference="eq:dilog"} $$\begin{split}
  &
  H(y,m^2)
  \\
  &\quad=
  \operatorname{Li}_2(y^{-1}m^{-2})-\operatorname{Li}_2(ym^{-2})+\left(\log(-y)+\pi\sqrt{-1}\right)\log{m^2}
  \\
  &\quad=
  \operatorname{Li}_2
  \Bigl(\exp\bigl(\alpha(r)-2\pi{r})\sqrt{-1}\bigr)\Bigr)
  -
  \operatorname{Li}_2
  \Bigl(\exp\bigl(-\alpha(r)-2\pi{r})\sqrt{-1}\bigr)\Bigr)
  \\
  &\quad\quad
  +2\pi(r-1)(\alpha(r)-2\pi)
  \\
  &\quad
  =
  \frac{\pi^2}{6}
  -\frac{2\pi+\alpha(r)-2\pi{r}}{2}
   \left(\pi-\frac{2\pi+\alpha(r)-2\pi{r}}{2}\right)
  +2\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{\alpha(r)-2\pi{r}}{2}\right)
  \\
  &\quad\quad
  -\frac{\pi^2}{6}
  +\frac{4\pi-\alpha(r)-2\pi{r}}{2}
   \left(\pi-\frac{4\pi-\alpha(r)-2\pi{r}}{2}\right)
  -2\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}\left(\frac{-\alpha(r)-2\pi{r}}{2}\right)
  \\
  &\quad\quad
  +2\pi(r-1)(\alpha(r)-2\pi)
  \\
  &\quad=
  -2\pi^2(r-1)
  +
  2\sqrt{-1}
  \left\{
    \operatorname{\text{\tencyr\cyracc L}}\bigl(\pi{r}+\alpha(r)/2\bigr)-\operatorname{\text{\tencyr\cyracc L}}\bigl(\pi{r}-\alpha(r)/2\bigr)
  \right\}.
\end{split}$$

On the other hand from [@Murakami:KYUMJ2004 Theorem 1.2] $$\begin{gathered}
  2\pi{r}\operatorname{Re}\lim_{N\to\infty}
  \frac{\log{J_N\bigl(E;\exp(2\pi{r}\sqrt{-1}/N)\bigr)}}{N}
  \\
  =
  2
  \left\{
    \operatorname{\text{\tencyr\cyracc L}}\bigl(\pi{r}+\alpha(r)/2\bigr)-\operatorname{\text{\tencyr\cyracc L}}\bigl(\pi{r}-\alpha(r)/2\bigr)
  \right\}
\end{gathered}$$ if $r\not\in\mathbb{Q}$ and $5/6<r<7/6$, or $r=1$. Moreover from its proof we see that the sign of $J_N\bigl(E;\exp(2\pi{r}\sqrt{-1})/N\bigr)$ for large $N$ is $(-1)^{\lfloor{N(1-r)/r}\rfloor}$, where $\lfloor{x}\rfloor$ is the greatest integer that does not exceed $x$. So $$\begin{split}
  2\pi{r}\operatorname{Im}\lim_{N\to\infty}
  \frac{\log{J_N\bigl(E;\exp(2\pi{r}\sqrt{-1}/N)\bigr)}}{N}
  &=
  2\pi{r}\operatorname{Im}\lim_{N\to\infty}
  \frac{\log\left((-1)^{\lfloor{N(1-r)/r}\rfloor}\right)}{N}
  \\
  &=
  2\pi^2(1-r).
\end{split}$$ Therefore we have $$2\pi{r}\sqrt{-1}\lim_{N\to\infty}
  \frac{\log{J_N\bigl(E;\exp(2\pi{r}\sqrt{-1}/N)\bigr)}}{N}
  =
  H(y,m^2)$$ if $5/6<r<7/6$ and $r\not\in\mathbb{Q}\setminus\{0\}$.

Putting $$u:=2\pi{r}\sqrt{-1}-2\pi\sqrt{-1}$$ and $$H(u):=H(y,m^2),$$ we have proved the following theorem.

::: thm
Let $E$ be the figure-eight knot. There exists a neighborhood $U$ of $0$ in $\mathbb{C}$ such that for any $u\in(U\setminus\pi\sqrt{-1}\mathbb{Q})\cup\{0\}$, $$(u+2\pi\sqrt{-1})
  \lim_{N\to\infty}
  \frac{\log\left(
              J_N\left(
                   E;\exp\left(\frac{u+2\pi\sqrt{-1}}{N}\right)
                 \right)
            \right)}
  {N}
  =H(u).$$
:::
