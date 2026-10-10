---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-002-3-approximating-the-integral-formula
section_title: "Approximating the integral formula"
section_number: 3
pages: 6-10
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
text_source: latex
latex_prose_ratio: 0.824
latex_coverage_ratio: 0.926
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
---
[]{#sec:approximation label="sec:approximation"} In this section we approximate the integral formula for the colored Jones polynomial obtained in the previous section.

Since $\tan(N\pi w)$ is close to $\sqrt{-1}$ ($-\sqrt{-1}$, respectively) when $\operatorname{Im}(w)$ is positive and large (negative and $|\operatorname{Im}(w)|$ is large, respectively), we can approximate $G_{\pm}(N,\varepsilon)$ by the integral of $g_N(w)$ on $C_{\pm}(\varepsilon)$. In fact if we write $$\begin{equation*}
  G_{\pm}(N,\varepsilon)
  =
  \pm\sqrt{-1}\int_{C_{\pm}(\varepsilon)}g_N(w)\,dw
  +
  \int_{C_{\pm}(\varepsilon)}(\tan(N\pi w)\mp\sqrt{-1})g_N(w)\,dw,
\end{equation*}$$ then we have the following lemma.

::: prop
[]{#prop:4.7 label="prop:4.7"} There exists a positive constant $K_{1,\pm}$ independent of $N$ and $\varepsilon$ such that the following inequality holds: $$\begin{equation*}
  \left|
    \int_{C_{\pm}(\varepsilon)}(\tan(N\pi w)\mp\sqrt{-1})g_N(w)\,dw
  \right|
  <
  \frac{K_{1,\pm}}{N}.
\end{equation*}$$
:::

A proof is given in Section [\[sec:prop:4.7\]](#sec:prop:4.7){reference-type="ref" reference="sec:prop:4.7"}.

Now we approximate the integral of $g_N(w)$ along $C_{\pm}(\varepsilon)$. Define $$\begin{equation*}
  \Phi(w)
  :=
  \frac{1}{\xi}
  \bigl(
    \operatorname{Li}_2\left(e^{u-\xi w}\right)-\operatorname{Li}_2\left(e^{u+\xi w}\right)
  \bigr)
  -uw.
\end{equation*}$$ Since $\operatorname{Li}_2$ is analytic in the region $\mathbb{C}\setminus(1,\infty)$, the function $\Phi$ is analytic in the region $\{w\in\mathbb{C}\mid-\frac{2\pi}{u}\operatorname{Re}(w)<\operatorname{Im}(w)<-\frac{2\pi}{u}(\operatorname{Re}(w)-1)\}$ (Figure [\[fig:contour\]](#fig:contour){reference-type="ref" reference="fig:contour"}).

::: prop
[]{#prop:4.9 label="prop:4.9"} Let $p(\varepsilon)$ be any contour in the parallelogram bounded by $C(\varepsilon)$ connecting $\varepsilon$ and $1-\varepsilon$, then there exists a positive constant $K_2$ independent of $N$ and $\varepsilon$ such that the following inequality holds. $$\begin{equation*}
  \left|
    \int_{p(\varepsilon)}
    g_N(w)\,dw
    -
    \int_{p(\varepsilon)}
    \exp(N\Phi(w))\,dw
  \right|
  \le
  \frac{K_2\log(N)}{N}
  \max_{w\in p(\varepsilon)}\left\{\exp\bigl(N\operatorname{Re}\Phi(w)\bigr)\right\}.
\end{equation*}$$
:::

A proof is given in Section [\[sec:prop:4.9\]](#sec:prop:4.9){reference-type="ref" reference="sec:prop:4.9"}.

We will study the asymptotic behavior of $\int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw$ for large $N$.

Since $\Phi(w)$ is analytic in the region $\{w\in\mathbb{C}\mid-\frac{2\pi}{u}\operatorname{Re}(w)<\operatorname{Im}(w)<-\frac{2\pi}{u}(\operatorname{Re}(w)-1)\}$, we have $$\begin{equation*}
  \int_{C_{+}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
  =
  \int_{C_{-}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
\end{equation*}$$ by Cauchy's integral theorem.

We will apply the saddle point method (see for example [@Marsden/Hoffman:Complex_Analysis § 7.2]) to approximate the integral $\int_{C_{-}(\varepsilon)}\exp(N\Phi(w))\,dw$.

First we find a solution to the equation $d\,\Phi(w)/d\,w=0$. Since we have $$\begin{equation*}
  \frac{d\,\Phi(w)}{d\,w}
  =
  \log(1-e^{u-\xi w})+\log(1-e^{u+\xi w})-u,
\end{equation*}$$ a solution to the equation $$\begin{equation*}
  e^{\xi w}+e^{-\xi w}
  =
  e^u+e^{-u}-1
\end{equation*}$$ can be a saddle point that we need. Put $$\begin{align}
\label{eq:varphi}
  \varphi(u)
  &:=
  \operatorname{arccosh}(\cosh(u)-1/2)\notag
  \\
  &=
  \log
  \left(
    \frac{1}{2}
    \left(
      e^u+e^{-u}-1-\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}
    \right)
  \right),
  \\
  \tilde{\varphi}(u)
  &:=
  \varphi(u)+2\pi\sqrt{-1},\notag
  \\
  \intertext{and}
  w_0
  &:=
  \frac{\tilde{\varphi}(u)}{\xi},\notag
\end{align}$$ where we choose the square root of $(e^u+e^{-u}+1)(e^u+e^{-u}-3)$ as a positive multiple of $\sqrt{-1}$ and the branch of $\log$ so that $-\pi/3<\operatorname{Im}\varphi(u)<0$.

::: rem
[]{#rem:varphi label="rem:varphi"} Note that $\varphi(u)$ and $\tilde{\varphi}(u)$ are purely imaginary since $\left|e^u+e^{-u}-1-\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}\right|=4$.
:::

It is easy to see that $d\,\Phi(w_0)/d\,w=0$. Since we have $$\begin{equation*}
  \operatorname{Im}(w_0)+\frac{2\pi}{u}\operatorname{Re}(w_0)
  =
  \frac{\operatorname{Im}\tilde{\varphi}(u)}{u},
\end{equation*}$$ $w_0$ is in the domain of $\Phi$.

<figure id="fig:contour09" data-latex-placement="h">
<embed src="saddle.eps" />
<figcaption>A contour plot of <span class="math inline">Re <em>Φ</em>(<em>w</em>)</span> on the complex plane for <span class="math inline"><em>u</em> = 0.9</span>. A brighter part is higher than a darker part. The path <span class="math inline"><em>P</em></span> is indicated by a thick curve and the saddle point <span class="math inline"><em>w</em><sub>0</sub></span> is marked by a circle.</figcaption>
</figure>

We choose a path $P$ from $\varepsilon$ to $1-\varepsilon$ that passes through $w_0$ so that near $w_0$ it keeps $\operatorname{Im}\Phi(w)$ constant and that $\operatorname{Re}\Phi(w)$ takes its maximum (over all $w$ on $P$) at $w_0$ as indicated in the thick curve in Figures [1](#fig:contour09){reference-type="ref" reference="fig:contour09"}. Then the integral $\int_{C_-(\varepsilon)}\exp(N\Phi(w))\,dw$ is approximated by the integral near $w_0$ along the path we choose. More precisely we have $$\begin{equation}
\label{eq:Phi_saddle}
  \int_{C_-(\varepsilon)}\exp(N\Phi(w))\,dw
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{2\pi}\exp(N\Phi(w_0))}{\sqrt{N}\sqrt{-d^2\,\Phi(w_0)/d\,w^2}}
\end{equation}$$ from [@Marsden/Hoffman:Complex_Analysis Theorem 7.2.8], where the sign of the square root of $-d^2\,\Phi(w_0)/d\,w^2$ is chosen so that $$\begin{equation}
\label{eq:argument}
  \sqrt{-d^2\,\Phi(w_0)/d\,w^2}\times\text{(tangent of $P$ at $w_0$)}>0.
\end{equation}$$ Note that $$\begin{equation}
\label{eq:Phi_0}
  \Phi(w_0)
  =
  \frac{1}{\xi}
  \left(
    \operatorname{Li}_2\left(e^{u-\varphi(u)}\right)
    -
    \operatorname{Li}_2\left(e^{u+\varphi(u)}\right)
    -u\tilde{\varphi}(u)
  \right).
\end{equation}$$

From Propositions [\[prop:4.7\]](#prop:4.7){reference-type="ref" reference="prop:4.7"} and [\[prop:4.9\]](#prop:4.9){reference-type="ref" reference="prop:4.9"}, choosing $P$ as a contour in Proposition [\[prop:4.9\]](#prop:4.9){reference-type="ref" reference="prop:4.9"} we have $$\begin{equation*}
\begin{split}
  &\left|
    G_{\pm}(N,\varepsilon)
    \mp
    \sqrt{-1}
    \int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
  \right|
  \\
  \le&
  \left|
    \int_{C_{\pm}(\varepsilon)}(\tan(N\pi w)\mp\sqrt{-1})g_N(w)\,dw
    \pm\sqrt{-1}
    \int_{C_{\pm}(\varepsilon)}\left(g_N(w)-\exp\bigl(N\Phi(w)\bigr)\right)\,dw
  \right|
  \\
  \le&
  \frac{K_{1,\pm}}{N}
  +
  \frac{K_2\log(N)}{N}
  \exp\bigl(N\operatorname{Re}\Phi(w_0)\bigr).
\end{split}
\end{equation*}$$ From [\[eq:Phi_saddle\]](#eq:Phi_saddle){reference-type="eqref" reference="eq:Phi_saddle"} we have $$\begin{equation*}
\begin{split}
  &\lim_{N\to\infty}
  \left|
    \frac{G_{\pm}(N,\varepsilon)}
         {\pm\sqrt{-1}
          \int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw}
  -1
  \right|
  \\
  \le&
  \frac{K_{1,\pm}}
       {N
        \left|
          \int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
        \right|}
  +
  \frac{K_2\log(N)}{N}\times
  \frac{\exp\bigl(N\operatorname{Re}\Phi(w_0)\bigr)}
       {\left|
          \int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw
        \right|}
  \\
  \underset{N\to\infty}{\longrightarrow}&0.
\end{split}
\end{equation*}$$ Here we use the following lemma which will be proved in Section [\[lem:Phi_0\]](#lem:Phi_0){reference-type="ref" reference="lem:Phi_0"}.

::: lem
[]{#lem:Phi_0 label="lem:Phi_0"} The real part of $\Phi(w_0)$ is positive for $0<u<\log\bigl((3+\sqrt{5})/2\bigr)$. Therefore from [\[eq:Phi_saddle\]](#eq:Phi_saddle){reference-type="eqref" reference="eq:Phi_saddle"} we see that $\int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw$ grows exponentially.
:::

So we have $$\begin{equation*}
  G_{\pm}(N,\varepsilon)
  \underset{N\to\infty}{\sim}
  \pm\sqrt{-1}
  \int_{C_{\pm}(\varepsilon)}\exp\bigl(N\Phi(w)\bigr)\,dw.
\end{equation*}$$

Therefore from [\[eq:G\]](#eq:G){reference-type="eqref" reference="eq:G"} we have $$\begin{equation*}
\begin{split}
  &J_N\bigl(K;\exp(\xi/N)\bigr)
  \\
  \underset{N\to\infty}{\sim}&
  \frac{e^{2\pi\sqrt{-1}u N/\xi}}{e^u-1}

  \frac{N e^{u/2}}{2}
  \left(
    \int_{C_{-}(\varepsilon)}\exp(N\Phi(w))\,dw
    -
    \int_{C_{+}(\varepsilon)}\exp(N\Phi(w))\,dw
  \right)
  \\
  =&
  \frac{N e^{2\pi\sqrt{-1}u N/\xi}}{2\sinh(u/2)}
  \left(
    \int_{C_{-}(\varepsilon)}\exp(N\Phi(w))\,dw
  \right)
\end{split}
\end{equation*}$$ from the lemma below.

::: lem
[]{#lem:S_gamma label="lem:S_gamma"} For $\gamma=(2\pi-\sqrt{-1}u)/(2N)$ with positive $u$, we have $$\begin{equation*}
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  =
  \frac{e^{\pi u/\gamma}-1}{e^u-1}.
\end{equation*}$$ Therefore we have the following asymptotic equivalence: $$\begin{equation*}
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  \underset{N\to\infty}{\sim}
  \frac{e^{2\pi\sqrt{-1}u N/\xi}}{e^u-1}.
\end{equation*}$$
:::

A proof of the lemma is given in Section [\[sec:S_gamma\]](#sec:S_gamma){reference-type="ref" reference="sec:S_gamma"}.

::: rem
[]{#rem:S label="rem:S"} When $u=0$, we have $$\begin{equation*}
  \frac{S_{\gamma}(-\pi+\gamma)}{S_{\gamma}(\pi-\gamma)}
  =
  N
\end{equation*}$$ from [@Andersen/Hansen:JKNOT2006 P. 492].
:::

Since $$\begin{equation*}
  \frac{d^2\,\Phi(w_0)}{d\,w^2}







  =
  \xi\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)},
\end{equation*}$$ we have the following asymptotic equivalence from [\[eq:Phi_saddle\]](#eq:Phi_saddle){reference-type="eqref" reference="eq:Phi_saddle"}: $$\begin{equation*}
\begin{split}
  \int_{C_{-}(\varepsilon)}\exp(N\Phi(w))\,dw
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{2\pi}\exp(N\Phi(w_0))}
  {\sqrt{N}\sqrt{-\xi\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}}},
\end{split}
\end{equation*}$$ where we choose the square root of $\sqrt{-\xi\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}}$ so that it is in the fourth quadrant from [\[eq:argument\]](#eq:argument){reference-type="eqref" reference="eq:argument"}.

Therefore we finally have $$\begin{equation*}
\begin{split}
  &J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  \underset{N\to\infty}{\sim}&
  \frac{N e^{2\pi\sqrt{-1}u N/\xi}}{2\sinh(u/2)}
  \frac{\sqrt{2\pi}}{\sqrt{N}\sqrt{-\xi\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}}}
  \\
  &
  \times
  \exp
  \left(
    \frac{N}{\xi}
    \left(
      \operatorname{Li}_2\left(e^{u-\varphi(u)}\right)
      -
      \operatorname{Li}_2\left(e^{u+\varphi(u)}\right)
      -
      u\tilde{\varphi}(u)
    \right)
  \right)
  \\
  =&
  \frac{\sqrt{\pi}}{2\sinh(u/2)}
  \sqrt{
    \frac{-2}{\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}}
       }
  \sqrt{\frac{N}{\xi}}
  \exp\left(\frac{N}{\xi}S(u)\right).
\end{split}
\end{equation*}$$ Here we put $$\begin{equation*}
  S(u)
  :=
  \operatorname{Li}_2\left(e^{u-\varphi(u)}\right)
  -
  \operatorname{Li}_2\left(e^{u+\varphi(u)}\right)
  -
  u\varphi(u).
\end{equation*}$$

::: rem
When $u=0$, we have $$\begin{equation*}
\begin{split}
  \int_{C_{-}(\varepsilon)}\exp(N\Phi(w))\,dw
  \underset{N\to\infty}{\sim}
  \frac{\exp(N\Phi(w_0))}
  {\sqrt{N}3^{1/4}}.
\end{split}
\end{equation*}$$ Since $w_0=5/6$ in this case we have $$\begin{equation*}
\begin{split}
  \Phi(w_0)
  &=
  \frac{1}{2\pi\sqrt{-1}}
  \left(
    \operatorname{Li}_2(e^{-5\pi\sqrt{-1}/3})-\operatorname{Li}_2(e^{5\pi\sqrt{-1}/3})
  \right)
  \\
  &=
  \frac{6\sqrt{-1}\Lambda(\pi/3)}{2\pi\sqrt{-1}}
  =
  \frac{\operatorname{Vol}(E)}{2\pi}.
\end{split}
\end{equation*}$$ Therefore from Remark [\[rem:S\]](#rem:S){reference-type="ref" reference="rem:S"}, we have Theorem [\[thm:Andersen/Hansen\]](#thm:Andersen/Hansen){reference-type="ref" reference="thm:Andersen/Hansen"}.
:::
