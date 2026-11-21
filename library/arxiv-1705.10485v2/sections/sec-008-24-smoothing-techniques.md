---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-008-24-smoothing-techniques
section_title: "Smoothing techniques"
section_number: 2.4
pages: 14-17
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.949
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#subsec:smoothing label="subsec:smoothing"} We now explain how to relate the estimates on test functions or distributions to estimates on the Kolmogorov distance. The main tool with respect to this problem is the following:

::: lemma
[]{#lem:kernelD1 label="lem:kernelD1"} There exists a function $\rho$ (called kernel) on $\mathbb{R}$ with the following properties.

1.  The kernel $\rho$ is non-negative, with $\int_{\mathbb{R}} \rho(x)\,d\hspace*{-0.3mm}{x}=1$.

2.  The support of $\widehat{\rho}$ is $[-1,1]$ (hence, $\rho$ is a test function in $\mathscr{T}_0(\mathbb{R})$).

3.  The functions $\rho$ and $\widehat{\rho}$ are even, and $$\rho(K) \leq \min\left(\frac{3}{8\pi},\frac{96}{\pi\,K^4}\right).$$
:::

<figure id="fig:smooth">
<div class="center">

</div>
<figcaption>The smoothing kernel <span class="math inline">$\rho_{\frac{1}{4}}$</span>, and its Fourier transform which is supported on <span class="math inline">[−4,4]</span>.<span id="fig:smooth" label="fig:smooth"></span></figcaption>
</figure>

::: proof
*Proof.* Set $$\rho(x) = \frac{3}{8\pi}\,\left(\mathrm{sinc}\left(\frac{x}{4}\right)\right)^4 .$$ It has its Fourier transform supported on $[-\frac{1}{4},\frac{1}{4}] + [-\frac{1}{4},\frac{1}{4}] + [-\frac{1}{4},\frac{1}{4}] + [-\frac{1}{4},\frac{1}{4}] = [-1,1]$. On the other hand, an easy computation gives $\int_{\mathbb{R}} \rho(x)\,d\hspace*{-0.3mm}{x}=1$: use for example the Plancherel formula $$\int_{\mathbb{R}} |f(x)|^2\,d\hspace*{-0.3mm}{x} = \frac{1}{2\pi}\,\int_{\mathbb{R}} |\widehat{f}(\xi)|^2\,d\hspace*{-0.3mm}{\xi}$$ with $f(x)=\mathrm{sinc}(x)^2$ and thus $\widehat{f}(\xi) = \frac{1}{2\pi} \,\widehat{\mathrm{sinc}}*\widehat{\mathrm{sinc}}(\xi) = \frac{\pi}{2} (2-|\xi|)_+$. Finally, $\mathrm{sinc}(x) \leq \min(1,\frac{1}{|x|})$, which leads to the inequality stated for $\rho(K)$.0◻ ◻
:::

<figure id="fig:smoothheaviside">
<div class="center">

</div>
<figcaption>The approximation <span class="math inline">$f_{1,\frac{1}{4}}$</span> of the Heaviside function <span class="math inline">1<sub>( − ∞, 1]</sub></span>.<span id="fig:smoothheaviside" label="fig:smoothheaviside"></span></figcaption>
</figure>

In the following, for $\varepsilon>0$, we set $\rho_{\varepsilon}(x)=\frac{1}{\varepsilon}\,\rho(\frac{x}{\varepsilon})$, which has its Fourier transform compactly supported on $[-\frac{1}{\varepsilon},\frac{1}{\varepsilon}]$; see Figure [1](#fig:smooth){reference-type="ref" reference="fig:smooth"}. We also denote $f_{a,\varepsilon}(x)=f_\varepsilon(x-a)$, where $f_\varepsilon$ is the function $1_{(-\infty,0]} * \rho_\varepsilon$; *cf.* Figure [2](#fig:smoothheaviside){reference-type="ref" reference="fig:smoothheaviside"}. For all $a,\varepsilon$, $f_{a,\varepsilon}$ is an approximation of the Heaviside function $1_{(-\infty,a]}$, and one has the following properties:

::: proposition
The function $f_{a,\varepsilon}$ is a smooth test distribution in $\mathscr{T}_1(\mathbb{R})$ whose derivative $\partial f_{a,\varepsilon}$ has its Fourier transform compactly supported on $[-\frac{1}{\varepsilon},\frac{1}{\varepsilon}]$, and satisfies $\|\partial f_{a,\varepsilon}\|_{\mathrm{L}^1} = 1$. Moreover:

1.  The function $f_{a,\varepsilon}$ has a non-positive derivative, and decreases from $1$ to $0$.

2.  One has $f_1(x)=1-f_1(-x)$, and for all $K\geq 0$, $$\begin{aligned}
    f_1(K)&=\int_{0}^\infty \rho(K+y)\,d\hspace*{-0.3mm}{y} \leq \frac{32}{\pi\,K^3};\\
    \int_0^\infty f_1(u-K)\,d\hspace*{-0.3mm}{u} & \leq K + \int_{w=0}^\infty \min\left(1,\frac{32}{\pi\,w^3}\right)\,d\hspace*{-0.3mm}{w} = K  + 3\sqrt[3]{\frac{3}{\pi}}.
    \end{aligned}$$
:::

::: proof
*Proof.* The derivative of $f_{a,\varepsilon}$ is $$\begin{aligned}
\partial(f_{a,\varepsilon})(x) &= \partial(1_{(-\infty,a]}*\rho_\varepsilon)(x) = \left(\partial(1_{(-\infty,a]}) * \rho_\varepsilon\right)(x)  \\
&= \left(-\delta_a * \rho_\varepsilon\right)(x) = -\rho_{\varepsilon}(x-a),
\end{aligned}$$ so it is indeed in $\mathscr{T}_0(\mathbb{R})$, and non-positive. Its Fourier transform is supported by $[-\frac{1}{\varepsilon},\frac{1}{\varepsilon}]$, and $\|\partial f_{a,\varepsilon}\|_{\mathrm{L}^1}=\int_{\mathbb{R}}\rho_{\varepsilon}(x)\,d\hspace*{-0.3mm}{x} = 1$. Then, $$\lim_{x \to +\infty} f_{a,\varepsilon}(x) = \lim_{x \to +\infty} f_{1}\!\left(\frac{x-a}{\varepsilon}\right) = \lim_{y \to +\infty} f_1(y),$$ so $\lim_{x \to +\infty} f_{a,\varepsilon}(x) = 0$. Since by definition $f_1(y)=\int_y^\infty \rho(u) \,d\hspace*{-0.3mm}{u}$, the symmetry relation $f_1(x)=1-f_1(-x)$ follows from $\rho$ even; it implies the other limit statement $\lim_{x \to -\infty} f_{a,\varepsilon}(x) = 1$. The inequalities in part ii) are immediate consequences of those of Lemma [\[lem:kernelD1\]](#lem:kernelD1){reference-type="ref" reference="lem:kernelD1"}.0◻ ◻
:::

Let us now state a result which converts estimates on smooth test distributions into estimates of Kolmogorov distances. It already appeared in [@MN15 Lemma 16], and is inspired by [@Tao12 p. 87] and [@Fel71 Chapter XVI, §3, Lemma 1]:

::: theorem
[]{#theorem:tao label="theorem:tao"} Let $X$ and $Y$ be two random variables with cumulative distribution functions $F_X(a)=\mathbb{P}[X \leq a]$ and $F_Y(a)=\mathbb{P}[Y\leq a]$. Assume that for some $\varepsilon>0$ and $B>0$, $$\sup_{a \in \mathbb{R}} \, |\mathbb{E}[f_{a,\varepsilon}(X)]-\mathbb{E}[f_{a,\varepsilon}(Y)] | \leq B\varepsilon.$$ We also suppose that $Y$ has a density w.r.t. Lebesgue measure that is bounded by $m$. Then, for every $\lambda>0$, $$\begin{aligned}
d_\mathrm{Kol}(X,Y)&=\sup_{a \in \mathbb{R}} |F_X(a)-F_Y(a)|\\
& \leq (1+\lambda)\left(B+\frac{m}{\sqrt[3]{\pi}}\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\varepsilon.
\end{aligned}$$
:::

The choice of the parameter $\lambda$ allows one to optimize constants according to the reference law of $Y$ and to the value of $B$. A general bound is obtained by choosing $\lambda=\frac{1}{2}$; this gives after some simplifications $$d_\mathrm{Kol}(X,Y) \leq \frac{3}{2}(B+7m)\,\varepsilon,$$ which is easy to remember and manipulate.

::: proof
*Proof.* For the convenience of the reader, we reproduce here the proof given in [@MN15]. Fix a positive constant $K$, and denote $\Delta=\sup_{a \in \mathbb{R}}|F_X(a)-F_Y(a)|$ the Kolmogorov distance between $X$ and $Y$. One has $$\begin{aligned}
F_X(a) = \mathbb{E}[1_{X \leq a}] &\leq \mathbb{E}[f_{a+K\varepsilon,\varepsilon}(X)] + \mathbb{E}[(1-f_{a+K\varepsilon,\varepsilon}(X))\,1_{X \leq a}] \nonumber\\
&\leq \mathbb{E}[f_{a+K\varepsilon,\varepsilon}(Y)] + \mathbb{E}[(1-f_{a+K\varepsilon,\varepsilon}(X))\,1_{X \leq a}] + B\varepsilon.
\label{eq:UB_FX}
\end{aligned}$$ The second expectation writes as $$\begin{aligned}
\mathbb{E}[(1-&f_{a+K\varepsilon,\varepsilon}(X))\,1_{X \leq a}]=\int_{\mathbb{R}} (1-f_{a+K\varepsilon,\varepsilon}(x))\,1_{(-\infty,a]}(x)\, \mathbb{P}_X(\!\,d\hspace*{-0.3mm}{x})\\
&=-\int_{\mathbb{R}} ((1-f_{a+K\varepsilon,\varepsilon}(x))\,1_{(-\infty,a]}(x))'\, F_X(x)\,d\hspace*{-0.3mm}{x} = A_1+A_2,
\end{aligned}$$ where $A_1=(1-f_{a+K\varepsilon,\varepsilon}(a))\,F_X(a)$, $A_2=\int_{\mathbb{R}} f_{a+K\varepsilon,\varepsilon}'(x)\,1_{(-\infty,a]}(x)\, F_X(x)\,d\hspace*{-0.3mm}{x}$. Indeed, in the space of tempered distributions, $((1-f_{a+K\varepsilon,\varepsilon}(x))\,1_{(-\infty,a]}(x))' = -(1-f_{a+K\varepsilon,\varepsilon}(x))\,\delta_a(x)-f'_{a+K\varepsilon,\varepsilon}(x)\,1_{(-\infty,a]}(x).$

We evaluate the two terms $A_1$ and $A_2$ as follows:

-   Since $F_X(a) \leq F_Y(a)+\Delta$, $$\begin{aligned}
    A_1 &\leq  (1-f_{a+K\varepsilon,\varepsilon}(a))\, F_Y(a) + (1-f_{a+K\varepsilon,\varepsilon}(a))\,\Delta \\
    &\leq \int_{\mathbb{R}} (1-f_{a+K\varepsilon,\varepsilon}(x))\,\delta_a(x)\, F_Y(x)\,d\hspace*{-0.3mm}{x} + (1-f_{1}(-K))\,\Delta .
    \end{aligned}$$

-   For $A_2$, since $F_X(x)\geq F_Y(x)-\Delta$ and the derivative of $f_{a+K\varepsilon,\varepsilon}$ is negative, an upper bound is obtained as follows: $$\begin{aligned}
    A_2 &\le \int_{\mathbb{R}} f_{a+K\varepsilon,\varepsilon}'(x)\,1_{(-\infty,a]}(x)\, F_Y(x)\,d\hspace*{-0.3mm}{x} - \Delta\int_{\mathbb{R}}f_{a+K\varepsilon,\varepsilon}'(x)\,1_{(-\infty,a]}(x)\,d\hspace*{-0.3mm}{x} \\
    &= \int_{\mathbb{R}} f_{a+K\varepsilon,\varepsilon}'(x)\,1_{(-\infty,a]}(x)\, F_Y(x)\,d\hspace*{-0.3mm}{x} +  (1-f_{a+K\varepsilon,\varepsilon}(a))\,\Delta\\
    &=\int_{\mathbb{R}} f_{a+K\varepsilon,\varepsilon}'(x)\,1_{(-\infty,a]}(x)\, F_Y(x)\,d\hspace*{-0.3mm}{x} + (1-f_{1}(-K))\,\Delta.
    \end{aligned}$$

Therefore, by gathering the bounds on $A_1$ and $A_2$, we get $$\mathbb{E}[(1-f_{a+K\varepsilon,\varepsilon}(X))\,1_{X \leq a}]\leq \mathbb{E}[(1-f_{a+K\varepsilon,\varepsilon}(Y))\,1_{Y \leq a}]+2 (1-f_1(-K))\,\Delta.
  \label{eq:Tech1}$$ On the other hand, if $m$ is a bound on the density $f_Y$ of $Y$, then $$\begin{aligned}
\mathbb{E}[f_{a+K\varepsilon,\varepsilon}(Y)\,1_{Y \geq a}] &= \int_a^{\infty} f_{a+K\varepsilon,\varepsilon}(y)\,f_Y(y)\,d\hspace*{-0.3mm}{y}\\
&\leq m\int_{a}^\infty f_{\varepsilon}(y-a-K\varepsilon)\,d\hspace*{-0.3mm}{y} = m\int_0^\infty f_\varepsilon(y-K\varepsilon)\,d\hspace*{-0.3mm}{y}\\\
&\leq m\varepsilon\int_0^\infty f_1(u-K)\,d\hspace*{-0.3mm}{u} \leq m \varepsilon\left(K+3\sqrt[3]{\frac{3}{\pi}}\right);
\end{aligned}$$ and $$\begin{aligned}
\mathbb{E}[f_{a+K\varepsilon,\varepsilon}(Y)] &\leq \mathbb{E}[f_{a+K\varepsilon,\varepsilon}(Y)\,1_{Y \leq a}] + m\left(K+3\sqrt[3]{\frac{3}{\pi}}\right)\varepsilon.
\label{eq:Tech2}
\end{aligned}$$ Putting together Eqs. [\[eq:UB_FX\]](#eq:UB_FX){reference-type="eqref" reference="eq:UB_FX"}, [\[eq:Tech1\]](#eq:Tech1){reference-type="eqref" reference="eq:Tech1"} and [\[eq:Tech2\]](#eq:Tech2){reference-type="eqref" reference="eq:Tech2"}, we get $$F_X(a) \leq F_Y(a) + \left(B+m\left(K+3\sqrt[3]{\frac{3}{\pi}}\right)\right) \varepsilon+ \frac{64}{\pi\,K^3}\,\Delta.$$ Similarly, $F_X(a)\geq F_Y(a) - \left(B+m(K+3\sqrt[3]{\frac{3}{\pi}})\right) \varepsilon- \frac{64}{\pi\,K^3}\,\Delta$, so in the end $$\Delta = \sup_{a \in \mathbb{R}}|F_X(a)-F_Y(a)| \leq \left(B+m\left(K+3\sqrt[3]{\frac{3}{\pi}}\right)\right)\varepsilon+ \frac{64}{\pi\,K^3}\,\Delta.$$ As this is true for every $K$, setting $K=4\sqrt[3]{\frac{1+\lambda}{\pi\lambda}}$ with $\lambda>0$, one obtains $$\Delta \leq (1+\lambda)\left(B+\frac{m}{\sqrt[3]{\pi}}\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\varepsilon.\qquad\qed$$ ◻
:::

In the next Section [\[sec:berry\]](#sec:berry){reference-type="ref" reference="sec:berry"}, we shall combine Theorem [\[theorem:tao\]](#theorem:tao){reference-type="ref" reference="theorem:tao"} and the estimates on smooth test distributions given by Proposition [\[prop:zonedistribution\]](#prop:zonedistribution){reference-type="ref" reference="prop:zonedistribution"} to get a Berry--Esseen type bound on the Kolmogorov distances in the setting of mod-$\phi$ convergence.
