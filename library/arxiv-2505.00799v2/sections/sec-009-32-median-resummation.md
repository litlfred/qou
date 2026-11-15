---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-009-32-median-resummation
section_title: "Median Resummation"
section_number: 3.2
pages: 19-24
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.922
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#subsec: median resum label="subsec: median resum"}

In this section, for our functions $g$ of interest, suppose that $g(z) \sim \varphi_{-d/c}(z)$ as $z$ approaches $-d/c \in \mathbb{Q}$. For appropriate $-d/c$, we will prove decompositions of the form $$\label{eqn: decomp integral}
g(z)
=  \mathcal{S}^{\pi/2}_{med}(\varphi_{-d/c})(z) 
+  \int_{\Gamma}e^{-u/(z+d/c)}\widehat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}},$$ where $\widehat{g}_{-d/c}^{odd}(u)$ is a function related to $g$ and the contour $\Gamma$ is displayed in Figure [1](#fig: contours){reference-type="ref" reference="fig: contours"}. In the first cases we will consider, we will show that the second term in the sum vanishes, giving a median resummation result for these functions. In the latter cases, the situation is more interesting, as the second term in the sum will contribute. The general approach for the results in this section was inspired by similar work in [@gukov-marino-putrov; @andersen-mistegard] for false theta functions of weight $1/2$.

::: prop
[]{#prop: med resum label="prop: med resum"} Suppose $g$ is of Type 4 with respect to $\Gamma_0(N)$ or of Type 5, and suppose $\gamma = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \in \Gamma_0(N)$. Then $g= \mathcal{S}_{med}^{\pi/2}(\varphi_{-d/c})$.
:::

::: proof
*Proof.* Let $g(z)= \sum_{n=0}^\infty b_n q^n$ and suppose that $g(z) \sim \varphi_{-d/c}(z)$ as $z$ approaches $-d/c \in \mathbb{Q}$. Now define $\widehat{g}_{-d/c}(u) := \frac{1}{\sqrt{\pi}}\sum_{n =0}^\infty b_n \zeta_c^{-dn}  e^{-\sqrt{8\pi i  nu}}$. We will relate $g$ and $\widehat{g}_{-d/c}$ through Borel resummation.

We will prove our result for $z+d/c$ along the half-line $i\mathbb{R}_+$ and deduce the equalities in Propositions [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"} on $\mathbb{H}$ by holomorphicity. Using Gaussian integration, we have that for $\varepsilon >0$, $$e^{2\pi i n (z+d/c)} = \frac{1}{\sqrt{\pi}\sqrt{8\pi i (z+d/c)}} \int_{i\mathbb{R}+\varepsilon}e^{-\sqrt{n}\eta} e^{-\eta^2/8\pi i (z+d/c)}\;d\eta.$$ Then we may write $$\begin{aligned}
\sum_{n=1}^\infty b^n q^n &= \sum_{n = 1}^\infty b^n \zeta_c^{-dn} e^{2\pi i (z+d/c)} \\&=  \frac{1}{\sqrt{\pi}\sqrt{8\pi i (z+d/c)}}\int_{i\mathbb{R}+\varepsilon}\sum_{n \geq 1} b_n\zeta_c^{-dn} e^{-\sqrt{n}\eta} e^{-\eta^2/8\pi i (z+d/c)}\;d\eta.
\end{aligned}$$ Under the change of variables $\eta^2/8\pi i =u$, this becomes $$\sum_{n = 1}^\infty b_n q^n =  \frac{1}{2\sqrt{z+d/c}}\int_{\Gamma}e^{-u/(z+d/c)} \sum_{n = 1}^\infty b_n\zeta_c^{-dn} e^{-\sqrt{8\pi i nu}} \;\frac{du}{\sqrt{\pi u}},$$ for the contour $\Gamma$ displayed in Figure [1](#fig: contours){reference-type="ref" reference="fig: contours"}.

<figure id="fig: contours">

<figcaption>The contour <span class="math inline"><em>Γ</em></span>.</figcaption>
</figure>

Expanding $\widehat{g}_{-d/c}(u)$ as a Puiseux series supported on half-integer powers, we have $$\label{egn: g hat asymptotic} 
\widehat{g}_{-d/c}(u) = \frac{1}{\sqrt{\pi}}\sum_{n \geq 1} b_n\zeta_c^{-dn} e^{-\sqrt{8\pi i nu}} \sim \frac{1}{\sqrt{\pi }} \sum_{r=0}^\infty \frac{(-1)^r L(g, \zeta_c^{-d};-r/2)}{\Gamma(r+1)}(8\pi iu)^{r/2}.$$ We split this series based on whether $r$ is even or odd. We write $$\widehat{g}_{-d/c}^{even}(u) := \frac{1}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n)}{\Gamma(2n+1)}(8\pi iu)^{n};$$ $$\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u) := -\frac{1}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n}.$$ Since in both cases, we assume a functional equation of degree 2 for some $L$-function related to $L(g, \zeta_c^{-d}; \rho)$ by a shift, both of the above power series converge absolutely in some neighborhood of $u=0$. Moreover, since $\Gamma(n+1)\Gamma(n+1/2) = \frac{\sqrt{\pi}}{4^n} \Gamma(2n+1)$, we see that $$\mathcal{B}_{1/2}(\varphi_{-d/c}(z)) = \frac{1}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n)}{\Gamma(2n+1)}(8\pi iu)^{n} = \widehat{g}_{-d/c}^{even}(u).$$ Then the above allows us to write $$\sum_{n = 1}^\infty b_n q^n =  \frac{1}{2\sqrt{z+d/c}} \left( \int_{\Gamma}e^{-u/(z+d/c)} \mathcal{B}_{1/2}(\varphi_{-d/c}(z)) \frac{du}{\sqrt{\pi u}} \ + \ \int_{\Gamma}e^{-u/(z+d/c)}\widehat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}}\right).$$ By deforming contours, we have $$\int_\Gamma e^{-u/(z+d/c)}\mathcal{B}_{1/2}(\varphi_{-d/c})\;\frac{du}{\sqrt{\pi u}} = \left(\int_0^{e^{i(\frac{\pi}{2}-\varepsilon)}\infty}+ \int_0^{e^{i(\frac{\pi}{2}+\varepsilon)}\infty}\right) e^{-u/(z+d/c)}\mathcal{B}_{1/2}(\varphi_{-d/c})\;\frac{du}{\sqrt{\pi u}},$$ noting that the integrand changes sign when $u$ circles the origin. This shows that this integral is the median resummation with $\varphi_{-d/c}$ of angle $\pi/2$.

To prove Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"}, it then suffices to show that in the given cases, $$\label{eqn: 0 integral}
\frac{1}{2\sqrt{z+d/c}}\int_{\Gamma}e^{-u/(z+d/c)}\widehat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}} = 0.$$ We will treat both cases separately.

First, suppose that $g$ is the Eichler integral of a cusp form $f$ of weight $k \in \frac{1}{2}+\mathbb{Z}$ on $\Gamma_0(N)$ where $4 \mid N$. Then $b_n = a_n n^{1-k}$ for $f(z) = \sum_{n=1}^\infty a_nq^n$. Considering equation ([\[egn: g hat asymptotic\]](#egn: g hat asymptotic){reference-type="ref" reference="egn: g hat asymptotic"}), note that for $r/2 \geq k-1$ and $r$ odd, $L(f, \zeta_c^{-d};k-1-r/2)$ vanishes due to the poles of $\Gamma(\rho)$ and the fact that $\Lambda(f, \zeta_c^{-d};\rho)$ is entire. This means that $$\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u) = -\frac{1}{\sqrt{\pi }} \sum_{n=0}^{k-5/2} \frac{ L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n},$$ which is just a polynomial in $u$. Then, we claim that $$\int_{\Gamma} e^{-u/(z+d/c)}\left( \sum_{n=0}^{k-5/2} \frac{L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n}\right)\;du = 0.$$ To see this, one considers an arc of radius $R>0$ which connects two points of $\Gamma$ to form an oriented closed curve. The integral along this entire curve must be 0 by the residue theorem, and as $R$ tends to infinity, the integral along the arc approach zero since the expression in brackets is a polynomial and $e^{-u/(z+d/c)}$ decays exponentially as $\Im(u) \to \infty$ (recalling that $z+d/c \in i\mathbb{R}_+)$.

Now suppose that $g$ is of *Type 5*. We consider only $z \to 0$. Showing Equation [\[eqn: 0 integral\]](#eqn: 0 integral){reference-type="ref" reference="eqn: 0 integral"} will require more work in this case. In order to show that the integral vanishes, we realize $\frac{1}{2\sqrt{u}}\widehat{g}^{odd}_{-d/c}$ as a Borel transform of another asymptotic series. Taking the Borel transform with a different shift results in a much simpler function which is easily shown to be holomorphic on $\mathbb{H}$. This, coupled with Lemma [\[lem: borel laplace shifts\]](#lem: borel laplace shifts){reference-type="ref" reference="lem: borel laplace shifts"}, is enough to prove our claim.

Recalling the definitions of $L_0$ and $L_1$ from Section [\[subsec: maass\]](#subsec: maass){reference-type="ref" reference="subsec: maass"}, we have $$L_0(-n-1/2) =\frac{1}{\pi^{2n+3} \cdot 2^{2n+2}} \Gamma(n+3/2)^2L_0(n+3/2);$$ $$L_1 (-n-1/2) = - \frac{1}{\pi^{2n+3} \cdot 2^{2n+2}} \Gamma(n+3/2)^2L_1(n+3/2).$$

Returning to $\widehat{g}_0^{odd}$ in this new case, we have $$\frac{1}{2\sqrt{u}}\widehat{g}_0^{odd}(u) = -\frac{1}{2\sqrt{\pi}}\sum_{n=0}^\infty \frac{(8\pi i)^{n+1/2}}{\pi^{2n+3} \cdot 2^{2n+2}} \frac{\Gamma(n+3/2)^2}{\Gamma(2n+2)} \left(L_0(n+3/2)-L_1(n+3/2)\right) u^n.$$ Noting that $\Gamma(2n+2) = \frac{2^{2n+1}}{\sqrt{\pi}} \Gamma(n+1)\Gamma(n+3/2)$, we can write this as $$-\sum_{n=0}^\infty \frac{1}{\pi^{2n+3} \cdot 2^{2n+3}} \frac{\Gamma(n+3/2)}{\Gamma(n+1)} \left(L_0(n+3/2)-L_1(n+3/2)\right)(2\pi i)^{n+1/2} u^n .$$

Now we define the function $$\Phi(z) := -\sum_{n=0}^\infty \frac{1}{\pi^{2n+3} \cdot 2^{2n+3}} \Gamma(n+3/2) \left(L_0(n+3/2)-L_1(n+3/2)\right)(2\pi i)^{n+1/2} z^n.$$ Then $\mathcal{B}_1(\Phi(z)) = \frac{1}{2\sqrt{u}}\widehat{g}_0^{odd}(u)$. Let us instead consider $\mathcal{B}_{3/2}(\Phi(z))$. This is equal to $$-\sum_{n=0}^\infty \frac{1}{\pi^{2n+3} \cdot 2^{2n+3}} \left(L_0(n+3/2)-L_1(n+3/2)\right)(2\pi i)^{n+1/2} u^n.$$

From here, we compute $$\begin{aligned}
        \mathcal{B}_{3/2}(\Phi(z)) = &-\sum_{n=0}^\infty \frac{(2\pi i)^{n+1/2}}{\pi^{2n+3}2^{2n+3}} \left[ \sum_{m=1}^\infty \frac{A_{-m}}{m^{n+3/2}}\right]u^{n}\\
    = &-\frac{1}{2\pi i}\sum_{n=0}^\infty \left[ \sum_{m=1}^\infty \frac{A_{-m}}{(-2\pi im)^{n+3/2}}\right]u^{n}\\
    = &-\frac{1}{2\pi i}\sum_{m=1}^\infty \frac{A_{-m}}{(-2\pi i m)^{3/2}} \left[ \sum_{n=0}^\infty \frac{u^n}{(-2\pi im)^{n}}\right]\\
    = &\frac{1}{2\pi i}\sum_{m=1}^\infty \frac{A_{-m}}{(-2\pi i m)^{1/2}} \left( \frac{1}{u-(-2\pi i m)}\right)\\
\end{aligned}$$ This function has only simple poles at points $-2\pi i m$ for $m \in \mathbb{N}$. Importantly, the poles are *not* in the upper half-plane. In particular, we have that $$\mathcal{L}_{3/2}^{\pi/2-\varepsilon}(\mathcal{B}_{3/2}(\Phi(z)) = \mathcal{L}_{3/2}^{\pi/2+\varepsilon}(\mathcal{B}_{3/2}(\Phi(z))$$ for $0< \varepsilon < \pi/2$. Then by Lemma [\[lem: borel laplace shifts\]](#lem: borel laplace shifts){reference-type="ref" reference="lem: borel laplace shifts"}, we have that $$\mathcal{L}_{1}^{\pi/2-\varepsilon}(\mathcal{B}_{1}(\Phi(z)) = \mathcal{L}_{3/2}^{\pi/2-\varepsilon}(\mathcal{B}_{3/2}(\Phi(z)) = \mathcal{L}_{3/2}^{\pi/2+\varepsilon}(\mathcal{B}_{3/2}(\Phi(z)) = \mathcal{L}_{1}^{\pi/2+\varepsilon}(\mathcal{B}_{1}(\Phi(z)).$$

This is exactly what we want. To see this, consider again $$\frac{1}{2}\int_{\Gamma}e^{-u/z}\widehat{g}_{0}^{odd}(u)\frac{du}{\sqrt{u}}.$$ For $\varepsilon$ sufficiently small, the contour $\Gamma$ in Figure [1](#fig: contours){reference-type="ref" reference="fig: contours"} is equivalent to a median resummation contour for $\theta=\pi/2$ since our function is analytic in a disc around the origin. From here, we have that

$$\begin{aligned}
\frac{1}{2}\int_\Gamma e^{-u/z} \widehat{g}_{0}^{odd}(u) \;\frac{du}{\sqrt{u}} &= \int_\Gamma e^{-u/z} \mathcal{B}_1(\Phi(z))\;du
\\
&= \left(\int_0^{e^{i(\frac{\pi}{2}-\varepsilon)}\infty}- \int_0^{e^{i(\frac{\pi}{2}+\varepsilon)}\infty}\right) e^{-u/z} \mathcal{B}_1(\Phi(z)) \;du \\

&=  z\left(\mathcal{L}_{3/2}^{\pi/2-\varepsilon}\mathcal{B}_{3/2}(\Phi(z)) - \mathcal{L}_{3/2}^{\pi/2+\varepsilon}\mathcal{B}_{3/2}(\Phi(z))\right) = 0. 
\end{aligned}$$ Now we have shown that the second integral in Equation [\[eqn: decomp integral\]](#eqn: decomp integral){reference-type="ref" reference="eqn: decomp integral"} vanishes, proving that $g(z)
=  \mathcal{S}^{\pi/2}_{med}(\varphi_{-d/c})(z)$ as desired. ◻
:::

In the case where $g$ is of *Type 6*, we modify the argument slightly and end up with a similar result.

::: prop
[]{#prop: eisenstein med label="prop: eisenstein med"} If $g$ is of Type 6, then $$g= \mathcal{S}_{med}^{\pi/2}(\varphi_{0}) +\frac{1}{2\sqrt{z}}\int_\Gamma e^{-u/z} \left( \frac{-4+2\log(8\pi i u)}{2\pi i u} \right)\frac{du}{\sqrt{\pi u}}.$$
:::

::: proof
*Proof.* We write $$1-4\sum_{n = 1}^\infty d(n) q^n =  \frac{1}{2\sqrt{z}}\int_{\Gamma}e^{-u/z} \left( 1-4\sum_{n = 1}^\infty d(n) e^{-\sqrt{8\pi i nu}}\right) \;\frac{du}{\sqrt{\pi u}},$$ and using the Mellin transform again we rewrite the inner sum as $$- \frac{4-2\log(8\pi i u)}{2\pi i u} - \frac{4}{\sqrt{\pi }} \sum_{r=1}^\infty \frac{(-1)^r \zeta^2(-r/2)}{\Gamma(r+1)}(8\pi iu)^{r/2},$$ Noting that the calculation for the pole at $s=2$ differs slightly. Leaving the leading term, we again split the sum into the cases where $r$ is even or odd to get $$\widehat{g}_{0}^{even}(u) := \frac{-4}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ \zeta^2(-n)}{\Gamma(2n+1)}(8\pi iu)^{n};$$ $$\frac{1}{\sqrt{u}}\widehat{g}_{0}^{odd}(u) := \frac{4}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ \zeta^2(-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n}.$$ As before, we have that $\widehat{g}_{0}^{even}(u) = \mathcal{B}_{1/2}(\varphi_0)$, where $\varphi_0$ was defined for $g$ in the proof of Proposition [\[prop: eisenstein asymptotic\]](#prop: eisenstein asymptotic){reference-type="ref" reference="prop: eisenstein asymptotic"}. The proof that the integral of $\widehat{g}_{0}^{odd}(u)$ vanishes is the same as in Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"} when $g$ is of *Type 5*. After appropriately rescaling to get from $\sum_{n=1}^\infty d(n)q^n$ to $g$, we get the desired result. ◻
:::

Note that in the cases where $g$ is of *Type 1 , 2,* or *3*, one can argue the same way as in Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"} to get the same decomposition as in Equation [\[eqn: decomp integral\]](#eqn: decomp integral){reference-type="ref" reference="eqn: decomp integral"}. However, in these cases, the second integral no longer vanishes. Moreover, we know that when $g$ is of *Type 1* or *2*, $\mathcal{B}_{1/2}(\varphi_{-d/c}(z))$ is zero, while for $g$ of *Type 3*, it is a polynomial. So we have that the first integral satisfies $$\begin{aligned}
&\frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)} \mathcal{B}_{1/2}(\varphi_{-d/c}(z)) \frac{du}{\sqrt{\pi u}}\\&= \frac{1}{\sqrt{z+d/c}} \int_{0}^{\infty}e^{-u/(z+d/c)} \mathcal{B}_{1/2}(\varphi_{-d/c}(z)) \frac{du}{\sqrt{\pi u}},
\end{aligned}$$ which up to prefactors is the Borel-Laplace sum of $\varphi_{-d/c}$ in direction 0.
