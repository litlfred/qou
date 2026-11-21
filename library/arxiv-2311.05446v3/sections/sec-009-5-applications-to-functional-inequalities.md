---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-009-5-applications-to-functional-inequalities
section_title: "Applications to functional inequalities"
section_number: 5
pages: 25-29
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.891
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
[]{#sec: gaussianapp label="sec: gaussianapp"}

In this section, we present some applications of the second part of Proposition [\[prop: oneendgaussian\]](#prop: oneendgaussian){reference-type="ref" reference="prop: oneendgaussian"}, that is, the $(2,n)$-convexity of $D(\mu_{t} \Vert \gamma)$ when one endpoint of the geodesic segment $\{ \mu_{t} \}_{t \in [0,1]}$ is an even strongly log-concave probability measure, and the other is the $\gamma$ itself. More specifically, we will prove improved $(2,n)$ versions to the (a priori $(1, \infty)-$) Gaussian *HWI*, Logarithmic Sobolev, and Talagrand inequalities, for even strongly log-concave probability measures.

::: definition
The (relative) *Fisher information* of a measure $\mu$ is defined by, $$I(\mu \Vert \gamma) = \int \frac{\vert \nabla f \vert^{2}}{f} \textnormal{ d}\gamma,$$ where $f = \frac{\textnormal{ d}\mu}{\textnormal{ d}\gamma}$.
:::

As discussed in the Introduction, HWI inequalities relate the three quantities that its initials correspond to. The main idea is to do calculus on the relative entropy $D(\mu_{t} \Vert \gamma)$ along the displacement interpolation between $\mu$ and $\gamma$, using the convexity properties of relative entropy. This accounts for the "H" and the "W". The Fisher information $I(\mu \Vert \gamma)$ appears because it plays the role of the squared norm of the gradient of $D(\cdot \Vert \gamma)$ under the previously mentioned Riemannian-like structure on $\mathscr{W}_{2}(\mathbb{R}^n)$. This makes the Fisher information a natural candidate to bound the derivative of relative entropy along any given (unit) tangent. To the interested reader who is unfamiliar with the idea outlined in this paragraph, we recommend the clear heuristic treatment of the $(K,\infty)$-case in [@OttoVillani00 Section 3]. Logarithmic Sobolev and Talagrand inequalities (which relate $H,I$, and $W,I$, respectively) follow from a suitable HWI inequality.

We follow the footsteps of [@ErbarKuwadaSturm15 Section 3.4] where the authors derive $(\kappa, n)$-versions of these inequalities from $(\kappa,n)$-convexity of relative entropy in a very general setup. While a global $(\kappa,n)$-convexity condition is assumed in [@ErbarKuwadaSturm15], it is easily seen from the proofs that the requirement is only on the interpolations connecting a measure $\mu$ (for which the inequalities are to be proven) to the reference measure ($\gamma$ in our case). Therefore, for completeness, we will only sketch the main steps in [@ErbarKuwadaSturm15] adapted to our setup. The reader is referred to [@ErbarKuwadaSturm15] for more details.

To begin with, we decipher what the local condition of $(2,n)$-convexity means globally. Towards this, we need some definitions.

::: definition
[@ErbarKuwadaSturm15 Definition 2.1] For $\theta \geq 0$, we define the following functions. $$\begin{split}
& \mathfrak{s} (\theta) = \mathfrak{s}_{2/n} (\theta) = \sqrt{\frac{n}{2}} \sin \left( \sqrt{\frac{2}{n}}  \theta \right), \\
& \mathfrak{c}(\theta) = \mathfrak{c}_{2/n} (\theta) = \cos \left(  \sqrt{\frac{2}{n}}  \theta  \right).\\
\end{split}$$ For $t \in [0,1]$, we set $$\sigma^{(t)}(\theta) = \sigma_{2/n}^{(t)}(\theta) = 
\begin{cases}
    \frac{\mathfrak{s}(t \theta)}{\mathfrak{s}(\theta)}, & \textnormal{if } \theta < \sqrt{\frac{n}{2}} \pi, \\
    \infty, &\textnormal{ otherwise.}\\
\end{cases}$$
:::

In terms of the coefficients $\sigma^{(t)}$ we may write a global condition for $(2, n)$-convexity.

::: lem
[@ErbarKuwadaSturm15 Lemma 2.2] []{#lem: 2ncon label="lem: 2ncon"} The $(2,n)$-convexity of $D(\mu_{t} \Vert \gamma)$ implies that, $$\label{eq: 2ncon}
e^{-\frac{D(\mu_{t} \Vert \gamma)}{n}} \geq \sigma^{(1-t)} (\mathscr{W}_{2}(\mu_{0}, \mu_{1})) e^{-\frac{D(\mu_{0} \Vert \gamma)}{n}} + \sigma^{(t)} (\mathscr{W}_{2}(\mu_{0}, \mu_{1})) e^{-\frac{D(\mu_{1} \Vert \gamma)}{n}}.$$
:::

::: proof
*Proof outline.* Let $u(t) = e^{-\frac{D(\mu_{t} \Vert \gamma)}{n}}$ let $v(t)$ denote the RHS in the above inequality. The $(2,n)$-convexity of $D(\mu_{t} \Vert \gamma)$ is equivalent to the condition $u''(t) \leq - \frac{2}{n} \mathscr{W}_{2}^{2}(\mu_{0}, \mu_{1}) u(t)$. On the other hand, $v(t)$ satisfies $v''(t) =  - \frac{2}{n} \mathscr{W}_{2}^{2}(\mu_{0}, \mu_{1}) v(t)$. The proof concludes by a maximum principle. ◻
:::

::: rem
Lemma [\[lem: 2ncon\]](#lem: 2ncon){reference-type="ref" reference="lem: 2ncon"} forces $\mathscr{W}_{2}^{2} (\mu, \gamma) \leq \frac{n}{2} \pi^{2}$ for all even strongly log-concave probability measures because the coefficients $\sigma^{(t)}(\cdot)$ blow up at $\sqrt{\frac{n}{2}} \pi$. However, this is not alarming since the stronger bound $\mathscr{W}_{2}^{2} (\mu, \gamma) \leq n$ can be obtained by a straightforward calculation using Caffarelli's contraction theorem and the Gaussian Poincaré inequality.
:::

Using Lemma [\[lem: 2ncon\]](#lem: 2ncon){reference-type="ref" reference="lem: 2ncon"}, we obtain Theorem [\[thm: HWIintro\]](#thm: HWIintro){reference-type="ref" reference="thm: HWIintro"}, which is restated below.

::: thm
Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$, then, $$\label{eq: hwi*}
e^{\frac{D(\mu_{0} \Vert \gamma)}{n}- \frac{D(\mu_{1} \Vert \gamma)}{n}}
\leq \mathfrak{c}( \mathscr{W}_{2}(\mu_{0}, \mu_{1})) + \frac{1}{n} \mathfrak{s}( \mathscr{W}_{2}(\mu_{0}, \mu_{1})) \sqrt{I(\mu_{0} \Vert \gamma)},$$ where $\{ \mu_{0} , \mu_{1} \} = \{ \mu , \gamma \}$.

In particular, $$\label{eq: hwi}
e^{\frac{D(\mu \Vert \gamma)}{n}} \leq \mathfrak{c}(\mathscr{W}_{2}(\mu, \gamma)) + \frac{1}{n} \mathfrak{s}(\mathscr{W}_{2}(\mu, \gamma)) \sqrt{I(\mu \Vert \gamma)}.$$
:::

::: proof
*Proof outline.* When $\{ \mu_{0}, \mu_{1} \} = \{ \mu , \gamma \}$, the relative entropy $D(\mu_{t} \Vert \gamma)$ is $(2,n)$-convex by Proposition [\[prop: oneendgaussian\]](#prop: oneendgaussian){reference-type="ref" reference="prop: oneendgaussian"} and Theorem [\[thm: 2nconunderconditions\]](#thm: 2nconunderconditions){reference-type="ref" reference="thm: 2nconunderconditions"}. Therefore, Equation [\[eq: 2ncon\]](#eq: 2ncon){reference-type="eqref" reference="eq: 2ncon"} holds. Now subtracting $e^{-\frac{D(\mu_{0} \Vert \gamma)}{n}}$ from both sides of Equation [\[eq: 2ncon\]](#eq: 2ncon){reference-type="eqref" reference="eq: 2ncon"}, dividing both sides by $t$, and letting $t \to 0$, we obtain $$e^{- \frac{D(\mu_{1} \Vert \gamma)}{n}} \leq \mathfrak{c}(\mathscr{W}_{2}(\mu_{0}, \mu_{1})) \cdot e^{- \frac{D(\mu_{0} \Vert \gamma)}{n}} + \frac{\mathfrak{s}(\mathscr{W}_{2}(\mu_{0}, \mu_{1}))}{\mathscr{W}_{2}(\mu_{0}, \mu_{1})}  \left. \frac{\textnormal{ d}}{\textnormal{ d}t} e^{- \frac{D(\mu_{t} \Vert \gamma)}{n}} \right|_{t=0}.$$ Observing that $$\begin{split}
\left. \frac{\textnormal{ d}}{\textnormal{ d}t} e^{- \frac{D(\mu_{t} \Vert \gamma)}{n}} \right|_{t=0} &= \frac{1}{n} e^{- \frac{D(\mu_{0} \Vert \gamma)}{n}} \frac{\textnormal{ d}}{\textnormal{ d}t} \left. \left( - D(\mu_{t} \Vert \gamma) \right) \right|_{t=0} \\
&\leq \frac{1}{n} e^{- \frac{D(\mu_{0} \Vert \gamma)}{n}} \sqrt{I(\mu_{0} \Vert \gamma)} \mathscr{W}_{2}(\mu_{0}, \mu_{1}) \\
\end{split}$$ completes the proof of the first inequality. Here we have used a piece from the computation [\[eq: firstderivativeentropycomp\]](#eq: firstderivativeentropycomp){reference-type="eqref" reference="eq: firstderivativeentropycomp"}, $$\begin{split}
\frac{\textnormal{ d}}{\textnormal{ d}t} \left. \left( - D(\mu_{t} \Vert \gamma) \right) \right|_{t=0} &= \int L \theta_{0} \textnormal{ d}\mu_{0} = - \int \langle \nabla\log f, \nabla\theta_{0} \rangle \textnormal{ d}\mu_{0} \\
&\leq \left( \int \vert \nabla\log f \vert^{2} \textnormal{ d}\mu_{0}  \right)^{1/2} \left( \int \vert \nabla\theta_{0} \vert^{2} \textnormal{ d}\mu_{0} \right)^{1/2} \\
&= \sqrt{I(\mu_{0} \Vert \gamma)} \mathscr{W}_{2}(\mu_{0}, \mu_{1}),
\end{split}$$ where $f = \frac{\textnormal{ d}\mu_{0}}{\textnormal{ d}\gamma}$ and $\nabla\theta_{t}$ denotes the velocity field driving the displacement interpolation from $\mu_{0}$ to $\mu_{1}$.

The second inequality is obtained simply by setting $\mu_{0} = \mu, \mu_{1} = \gamma$. ◻
:::

As immediate corollaries, dimensional improvements of the Gaussian Logarithmic Sobolev and Gaussian Talagrand inequalities are obtained for even strongly log-concave measures.

::: cor
[]{#cor: logsobolev label="cor: logsobolev"} Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$. Then, $$\label{eq: logsobolev}
4 D(\mu \Vert \gamma) \leq 2n \left( e^{\frac{2}{n}D(\mu \Vert \gamma)} - 1 \right) \leq I( \mu \Vert \gamma).$$
:::

::: proof
*Proof.* We square both sides of Equation [\[eq: hwi\]](#eq: hwi){reference-type="eqref" reference="eq: hwi"} to obtain $$e^{\frac{2}{n}D(\mu \Vert \gamma)} \leq \mathfrak{c}(\mathscr{W}_{2}(\mu, \gamma))^{2} + \frac{2}{n} \mathfrak{s}(\mathscr{W}_{2}(\mu, \gamma)) \mathfrak{c}(\mathscr{W}_{2}(\mu, \gamma)) \sqrt{I(\mu \Vert \gamma)} + \frac{1}{n^2} \mathfrak{s}(\mathscr{W}_{2}(\mu, \gamma))^{2} I(\mu \vert \gamma).$$ The inequality $2 ab \leq 2 a^{2} + \frac{1}{2}b^{2}$ applied to $a = \mathfrak{s} / \sqrt{n}, b = \mathfrak{c} \sqrt{I(\mu \Vert \gamma)/n}$, gives $$e^{\frac{2}{n}D(\mu \Vert \gamma)} \leq \left( \mathfrak{c}(\mathscr{W}_{2}(\mu, \gamma))^{2} + \frac{2}{n} \mathfrak{s}(\mathscr{W}_{2}(\mu, \gamma))^{2} \right) \left(1 + \frac{1}{2n} I(\mu \Vert \gamma) \right).$$ Now the identity $\mathfrak{c}^{2} + \frac{2}{n} \mathfrak{s}^{2} = 1$ allows us to conclude the second inequality in the assertion. The first inequality, which compares our result with a Logarithmic Sobolev inequality in a more standard form, follows from the inequality $e^x -1 \ge x$. ◻
:::

::: rem
The Gaussian measure satisfies a Logarithmic Sobolev inequality with constant $1$, that is, $D(\mu \Vert \gamma) \leq \frac{C}{2} I(\mu \Vert \gamma)$, $C=1$, without symmetry or concavity assumptions on $\mu$. Moreover, Bobkov, Gozlan, Roberto and Samson's result from [@BobkovGozlanRobertoSamson14] implies that if $\mu$ is strongly log-concave and centered, we already have $n \left( e^{\frac{2}{n}D(\mu \Vert \gamma)} - 1 \right) \leq I( \mu \Vert \gamma)$ -- See Corollary 2.2 there and note that indeed $b\le 1$ in this setting by Poincaré. Corollary [\[cor: logsobolev\]](#cor: logsobolev){reference-type="ref" reference="cor: logsobolev"} says that, for even strongly log-concave measures, both of these results improve by a factor of $2$. It is well known that the Poincaré constant of the Gaussian measure improves to $1/2$ for even functions. Given the relationship between Logarithmic Sobolev inequalities (stronger) and Poincaré inequalities (weaker), one may wonder if Corollary [\[cor: logsobolev\]](#cor: logsobolev){reference-type="ref" reference="cor: logsobolev"} can be strengthened to hold for all even measures. However, this is not the case; the improvement by a factor of $2$ in the Gaussian Poincaré inequality for even functions cannot be lifted to the same improvement in the Logarithmic Sobolev inequality for even measures without further assumptions, as the following example shows.
:::

::: exmpl
[]{#exmpl: betterlsineedsslc label="exmpl: betterlsineedsslc"} Let $\mu$ denote the distribution of $tZ$, where $Z$ has the distribution of standard Gaussian in $\mathbb{R}$. Then, all quantities involved can be explicitly computed, $$D(\mu \Vert \gamma) = - \log t + \frac{t^2}{2} - \frac{1}{2}, \textnormal{ and }
    I(\mu \Vert \gamma) = \frac{(t^2 - 1)^2}{t^2}.$$ As $t \mapsto \infty$, we have $\frac{4 D(\mu \Vert \gamma)}{t^{2}} \to 2$ but $\frac{I(\mu \Vert \gamma)}{t^{2}} \to 1$. On the other hand, taking the limit $t \to 1$ shows that our inequality is sharp.
:::

The improvement in the Logarithmic Sobolev inequality for even strongly log-concave measures also reflects in the convergence rate to equilibrium.

::: cor
Let $P^{\ast}_{t} \mu$ denote the Ornstein-Uhlenbeck evolution of an even strongly log-concave measure $\mu = \mu_{0}$, that is, $\textnormal{ d}P^{\ast}_{t} \mu = P_{t} \left( \frac{\textnormal{ d}\mu}{\textnormal{ d}\gamma} \right) \textnormal{ d}\gamma$. Here $P_{t}$ denotes the Ornstein-Uhlenbeck semigroup. Then, $$D(P^{\ast}_{t} \mu \Vert \gamma ) \leq e^{-4t} D(\mu_{0} \Vert \gamma).$$
:::

::: proof
*Proof sketch.* The proof is a standard argument using the facts that $\frac{\textnormal{ d}}{\textnormal{ d}t}   D(P^{\ast}_{t} \mu \Vert \gamma ) = -   I(P^{\ast}_{t} \mu \Vert \gamma )$, and that the Ornstein-Uhlenbeck semigroup $P_{t}$ (which acts on functions) preserves the class of even functions as well as the class of log-concave functions. ◻
:::

::: rem
The previous proof uses only the dimension-free part $4D(\mu \Vert \gamma) \leq I(\mu \Vert \gamma)$ in Corollary [\[cor: logsobolev\]](#cor: logsobolev){reference-type="ref" reference="cor: logsobolev"}. One can use the dimensional dependence available. However, this really improves the inequality only for short times $t$. Long-term behavior seems to be dominated by the "curvature" aspect. The interested reader may also consult [@BakryBolleyGentil12].
:::

We conclude this section with another typical application of the HWI inequality.

::: cor
[]{#cor: talagrand label="cor: talagrand"} Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$. Then, $$\label{eq: talagrand}
\mathscr{W}_{2}^{2} (\mu , \gamma) \leq - n \log \cos \left( \sqrt{\frac{2}{n}} \mathscr{W}_{2}(\mu, \gamma) \right) \leq D(\mu \Vert \gamma).$$
:::

::: proof
*Proof.* This follows from plugging in $\gamma = \mu_{0}$ and $\mu = \mu_{1}$ in the HWI Inequality [\[eq: hwi\*\]](#eq: hwi*){reference-type="eqref" reference="eq: hwi*"}, which makes $I(\mu_{0})=0$. ◻
:::

::: rem
The Gaussian measure satisfies $\mathscr{W}_{2}^{2} (\mu, \gamma) \leq 2 D(\mu \Vert \gamma)$ for all probability measures $\mu$. Since the Gaussian Talagrand inequality is also stronger than the Poincaré inequality ([@OttoVillani00 Section 7]), one may again consider the possibility that Corollary [\[cor: talagrand\]](#cor: talagrand){reference-type="ref" reference="cor: talagrand"} holds for all even measures. However, again, this is not the case. The example presented in the case of the Logarithmic Sobolev inequality serves us here as well.
:::

::: exmpl
[]{#exmpl: bettertalagrandneedsslc label="exmpl: bettertalagrandneedsslc"} Let $\mu$ denote the distribution of $tZ$, where $Z$ has the distribution of standard Gaussian in $\mathbb{R}$. Then, $$\mathscr{W}_{2}^{2} (\mu , \gamma) = (t-1)^2, \textnormal{ and }D(\mu \Vert \gamma) = - \log t + \frac{t^2}{2} - \frac{1}{2}.$$ As $t \to \infty$, we have $\frac{\mathscr{W}_{2}^{2}(\mu, \gamma)}{t^2} \to 1$ but $\frac{D(\mu \Vert \gamma)}{t^{2}} \to \frac{1}{2}$. On the other hand, as before, taking $t \to 1$ shows that our inequality is sharp.
:::
