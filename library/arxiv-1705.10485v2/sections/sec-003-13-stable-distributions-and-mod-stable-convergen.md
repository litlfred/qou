---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-003-13-stable-distributions-and-mod-stable-convergen
section_title: "Stable distributions and mod-stable convergence"
section_number: 1.3
pages: 5-6
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.771
latex_coverage_ratio: 0.936
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#Sect:Background_Stable label="Sect:Background_Stable"} Let us recall briefly the classification of stable distributions (see [@Sato99 Chapter 3]). Fix $c>0$ (the *scale* parameter), $\alpha \in (0,2]$ (the *stability* parameter), and $\beta \in [-1,1]$ (the *skewness* parameter).

::: definition
The stable distribution of parameters $(c,\alpha,\beta)$ is the infinitely divisible law $\phi=\phi_{c,\alpha,\beta}$ whose Fourier transform $$\widehat{\phi}(\xi)=\int_{\mathbb{R}}\E^{\I x\xi} \,\phi(\!\,d\hspace*{-0.3mm}{x}) = \E^{\eta(\I\xi)}$$ has for Lévy exponent $\eta(\I\xi)=\eta_{c,\alpha,\beta}(\I\xi)= -|c\xi|^\alpha \left(1-\I \beta \,h(\alpha,\xi)\,\mathrm{sgn}(\xi)\right),$ where $$h(\alpha,\xi) =\begin{cases}
\tan\left( \frac{\pi \alpha}{2}\right)& \text{if }\alpha \neq 1,\\
-\frac{2}{\pi} \log |\xi|& \text{if }\alpha = 1
\end{cases}$$ and $\mathrm{sgn}(\xi) = \pm 1$ is the sign of $\xi$.
:::

The most usual stable distributions are:

-   the standard Gaussian distribution $\frac{1}{\sqrt{2\pi}}\,\E^{-x^2/2}\,d\hspace*{-0.3mm}{x}$ for $c=\frac{1}{\sqrt{2}}$, $\alpha=2$ and $\beta=0$;

-   the standard Cauchy distribution $\frac{1}{\pi(1+x^2)}\,d\hspace*{-0.3mm}{x}$ for $c=1$, $\alpha=1$ and $\beta=0$;

-   the standard Lévy distribution $\frac{1}{\sqrt{2\pi}}\,\frac{\E^{-1/2x}}{x^{3/2}}\,\mathbbm{1}_{x \geq 0}\,d\hspace*{-0.3mm}{x}$ for $c=1$, $\alpha=\frac{1}{2}$ and $\beta=1$.

<figure>
<div class="center">

</div>
<figcaption>Densities of the standard Gaussian, Cauchy and Lévy distribution.</figcaption>
</figure>

We recall that mod-$\phi$ convergence on an open subset $D$ of $\mathbb{C}$ containing $0$ can only occur when the characteristic function of $\phi$ is analytic around $0$. Among stable distributions, only Gaussian laws (which correspond to $\alpha=2$) satisfy this property. Mod-$\phi$ convergence on $D=\I \mathbb{R}$ can however be considered for any stable distribution $\phi$.

Since $|\E^{\eta(\I\xi)}|=\E^{-|c\xi|^\alpha}$ is integrable, any stable law $\phi_{c,\alpha,\beta}$ has a density $m_{c,\alpha,\beta}(x)\,d\hspace*{-0.3mm}{x}$ with respect to the Lebesgue measure. Moreover, the corresponding Lévy exponents have the following scaling property: for any $t>0$, $$t \,\eta_{c,\alpha,\beta}\left(\frac{\I\xi}{t^{1/\alpha}}\right)=
\begin{cases}
\eta_{c,\alpha,\beta}(\I\xi)&\text{if }\alpha \neq 1,\\
\eta_{c,\alpha,\beta}(\I\xi) - \left(\frac{2c\beta}{\pi}\,\log t\right)\I\xi &\text{if }\alpha=1.
\end{cases}$$ This will be used in the following proposition:

::: proposition
[]{#prop:clt label="prop:clt"} If $(X_n)_{n \in \mathbb{N}}$ converges in the mod-$\phi_{c,\alpha,\beta}$ sense, then $$Y_n=\begin{cases}
\frac{X_n}{(t_n)^{1/\alpha}}&\text{if }\alpha \neq 1,\\
\frac{X_n}{t_n}-\frac{2c\beta}{\pi} \,\log t_n&\text{if }\alpha=1
\end{cases}$$ converges in law towards $\phi_{c,\alpha,\beta}$.
:::

::: proof
*Proof.* In both situations, $$\mathbb{E}[\E^{\I \xi Y_n}] = \E^{\eta(\I\xi)}\,\,\theta_n\!\left(\frac{\xi}{(t_n)^{1/\alpha}}\right)=\E^{\eta(\I\xi)}\,\theta(0)\,(1+o(1)) = \E^{\eta(\I\xi)}\,(1+o(1))$$ thanks to the uniform convergence of $\theta_n$ towards $\theta$, and to the scaling property of the Lévy exponent $\eta$.0◻ ◻
:::
