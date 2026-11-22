---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-013-33-approximation-of-a-stable-law-by-compound-poi
section_title: "Approximation of a stable law by compound Poisson laws"
section_number: 3.3
pages: 21-24
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.943
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#subsec:compoundpoisson label="subsec:compoundpoisson"} Let $\phi_{c,\alpha,\beta}$ be a stable law; the Lévy--Khintchine formula for its exponent allows one to write $$\E^{\eta_{c,\alpha,\beta}(\I\xi)} = \begin{cases}
    \E^{-|c\xi|^2} &\text{if }\alpha=2,\\
    \exp\left(\I m\xi+\int_{\mathbb{R}}(\E^{\I \xi x}-1-1_{|x|<1}\I\xi x)\,\pi_{c,\alpha,\beta}(\!\,d\hspace*{-0.3mm}{x})\right)& \text{if }\alpha\in(0,2),
\end{cases}$$ where $\pi_{c,\alpha,\beta}(\!\,d\hspace*{-0.3mm}{x})$ is the Lévy measure defined for $\alpha \in (0,2)$ by $$\pi_{c,\alpha,\beta}(\!\,d\hspace*{-0.3mm}{x}) = \frac{c_+\,1_{x>0}}{x^{1+\alpha}} +\frac{c_-\,1_{x<0}}{|x|^{1+\alpha}} ,$$ with $m \in \mathbb{R}$ and $c_+,c_-\in \mathbb{R}_+$ related to $(c,\alpha,\beta)$ by $\beta = \frac{c_+-c_-}{c_++c_-}$ and $$\begin{aligned}
m&=\begin{cases}
    \frac{c_+-c_-}{1-\alpha} &\text{if }\alpha \neq 1,\\
    \left(\int_0^1 \frac{\sin t - t}{t^2}\,dt+\int_1^\infty \frac{\sin t}{t^2}\,dt\right)(c_+-c_-)&\text{if } \alpha = 1;
\end{cases} \\
c_++c_- &= \begin{cases}
    \frac{\alpha\,c^\alpha}{\Gamma(1-\alpha)\,\sin\left(\frac{\pi(1-\alpha)}{2}\right)}  &\text{if }\alpha \neq 1,\\
    \frac{2c}{\pi}&\text{if }\alpha=1.
\end{cases}
\end{aligned}$$ The proof of the Lévy--Khintchine formula in the general case of an infinitely divisible law involves the following elementary fact (*cf.* [@Sato99 Chapter 2]): if $\mu$ is infinitely divisible and $\mu = (\rho_n)^{*n}$ for $n \geq 1$, then the compound Poisson law $\mu_n$ of intensity $n\,\rho_n$, which has Fourier transform $$\widehat{\mu_n}(\xi) = \exp\left(\int_{\mathbb{R}} (\E^{\I x\xi}-1)\,n\rho_n(\!\,d\hspace*{-0.3mm}{x})\right),$$ converges in law towards $\mu$; thus, any infinitely divisible law is a limit of compound Poisson laws. In the case of stable laws, this approximation result can be precised in terms of Kolmogorov distances:

::: proposition
[]{#prop:compoundpoisson label="prop:compoundpoisson"} Let $Y$ be a random variable with stable law $\phi_{c,\alpha,\beta}$, and $Y_n$ be a random variable with the following compound Poisson distribution: if $\mu_n$ is the law of $Y_n$, then its Fourier transform is $$\widehat{\mu_n}(\xi) = \exp\left(\int_{\mathbb{R}} (\E^{\I x\xi}-1)\,n\,\phi_{\frac{c}{n^{1/\alpha}},\alpha,\beta}(\!\,d\hspace*{-0.3mm}{x})\right).$$ The Kolmogorov distance between $Y_n$ and $Y$ is $$d_\mathrm{Kol}(Y_n,Y) \leq \begin{cases}
    C(\alpha)\,n^{-1/\alpha} &\text{if }\alpha \in (1,2],\\
    C(\alpha)\,n^{-1}&\text{if }\alpha \in (0,1) \text{ or }\alpha=1,\beta=0,\\
    C'\,(\log n)^2\,n^{-1}&\text{if } \alpha=1,\beta\neq 0,
\end{cases}$$ with constants $C(\alpha)$ or $C'$ that depend only on the exponent $\alpha$.
:::

We thus get a phase transition between the cases $\alpha>1$ and $\alpha<1$, with the case $\alpha=1$ that exhibit distinct transition behaviors according to the value of $\beta$.

::: proof
*Proof.* Let us distinguish the following cases:

-   Suppose first $\alpha \notin \{1,2\}$. The definition of $Y_n$ implies that $$\mathbb{E}[\E^{\I \xi Y_n}]=\widehat{\mu_n}(\xi) = \exp\left(n\!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n}}-1\right)\right).$$ Set $X_n = n^{1/(2\alpha)}Y_n$, $t_n = \sqrt{n}$ and $\theta_n(\xi) = \mathbb{E}[\E^{\I \xi X_n}]\,\E^{-t_n\,\eta_{c,\alpha,\xi}(\I \xi)}$. We have $$\begin{aligned}
    \theta_n(\xi) &= \exp\left(n\!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}}-1-\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}\right)\right).
    \end{aligned}$$ On the zone $[-K(t_n)^{1/\alpha},K(t_n)^{1/\alpha}]$ with $K = \frac{|\cos(\frac{\pi \alpha}{2})|^{\frac{2}{\alpha}}}{c}$, we can use a Taylor formula with an integral form remainder: $$\begin{aligned}
    n\!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}}\!-1-\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}\right) &= (\eta_{c,\alpha,\beta}(\I \xi))^2\left(\int_{0}^1\!(1-u)\,\E^{\frac{u\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}}\,d\hspace*{-0.3mm}{u}\right) \\
    \left|n\!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}}\!-1-\frac{\eta_{c,\alpha,\beta}(\I \xi)}{n^{1/2}}\right) \right| &\leq  \frac{1}{2}\,|\eta_{c,\alpha,\beta}(\I \xi)|^2 \leq \frac{1}{2}\left(\frac{c^\alpha}{\cos\left(\frac{\pi\alpha}{2}\right)}\right)^{\!2}\,|\xi|^{2\alpha}.
    \end{aligned}$$ We thus obtain a zone of control for $(X_n)_{n\in \mathbb{N}}$ with $v=w=2\alpha$, $\gamma = \frac{1}{\alpha}$, $$K_1=K_2 = \frac{1}{2}\left(\frac{c^\alpha}{\cos\left(\frac{\pi\alpha}{2}\right)}\right)^{\!2},$$ and one checks that $$\left(\frac{c^\alpha}{2K_2}\right)^{\frac{1}{w-\alpha}} = \frac{|\cos(\frac{\pi \alpha}{2})|^{\frac{2}{\alpha}}}{c} = K.$$ Since we need $\gamma \leq \min\left(\frac{1}{w-\alpha},\frac{v-1}{\alpha}\right)$ to obtain a bound on the Kolmogorov distance (see the hypotheses of Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}), this leads to a reduction of $\gamma$ when $\alpha<1$: $$\gamma+\frac{1}{\alpha} = \begin{cases}
        \frac{2}{\alpha} &\text{if }\alpha>1,\\
        2 &\text{if }\alpha<1.
    \end{cases}$$ With Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}, we obtain the following upper bound for $d_\mathrm{Kol}(Y_n,Y)$: $$\frac{1+\lambda}{\alpha\pi}\left(\frac{2}{\left(\cos(\frac{\pi\alpha}{2})\right)^2}+\frac{\Gamma(\frac{1}{\alpha})}{\sqrt[3]{\pi}\,\left|\cos(\frac{\pi\alpha}{2})\right|^{2/\alpha}}\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\frac{1}{n^{\frac{\gamma}{2}+\frac{1}{2\alpha}}},$$ Then, any choice of $\lambda>0$ gives a constant $C(\alpha)$ that depends only on $\alpha$.

-   When $\alpha=2$, the result follows from the usual Berry--Esseen estimates, since $\sqrt{n}\,Y_n$ has the law of a sum of $n$ independent random variables with same law and finite variance and third moment.

-   If $\alpha=1$ and $\beta=0$, then the same computations as above can be performed with a constant $K= \frac{1}{c}$, $v=w=2$, $\gamma=1$, $$K_1=K_2=\frac{c^2}{2},$$ and this leads to $$d_\mathrm{Kol}(Y_n,Y) \leq \frac{1+\lambda}{\pi}\left(2+\frac{1}{\sqrt[3]{\pi}}\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\frac{1}{n},$$ and a constant $C=3.04$ when $\lambda=0.2$.

-   Let us finally treat the case $\alpha=1$, $\beta \neq 0$. Recall that we then have $\eta_{c,\alpha,\beta}(\I \xi) = -|c\xi|\,(1+\frac{2\I \beta}{\pi}\,\mathrm{sgn}(\xi)\,\log|\xi|)$. We choose $t_n$ such that $t_n \log t_n = \sqrt{n}$, and set $$X_n = t_n\,Y_n + \frac{2c\beta}{\pi}\,\sqrt{n}.$$ We then have $$\begin{aligned}
    \theta_n(\xi) &= \mathbb{E}[\E^{\I\xi X_n}]\,\E^{-t_n\,\eta_{c,\alpha,\beta}(\I \xi)} \\
    &= \exp\left(\frac{2c\beta \I \xi}{\pi} \,t_n \log t_n + n \!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}}-1\right) -t_n\,\eta_{c,\alpha,\beta}(\I \xi)\right) \\
    &= \exp\left(n \!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}} -1 - \frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}\right) \right),
    \end{aligned}$$ and the Taylor formula with integral remainder yields: $$\begin{aligned}
    \left|n \!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}} -1 - \frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}\right)\right| &\leq \frac{1}{2n}\,|\eta_{c,\alpha,\beta}(\I t_n  \xi)|^2 \\
    &\leq \frac{c^2|\xi|^2}{2}\left(\frac{1+ \frac{4}{\pi^2}\,(\log |t_n\xi|)^2}{(\log t_n)^2}\right).
    \end{aligned}$$ On the zone $[-\frac{t_n}{2c} , \frac{t_n}{2c}]$, we thus have $$\begin{aligned}
      &\left|n \!\left(\E^{\frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}} -1 - \frac{\eta_{c,\alpha,\beta}(\I t_n  \xi)}{n}\right)\right| \\
      &\leq \frac{c^2|\xi|^2}{2}\left(\frac{1+ \frac{4}{\pi^2}\,(2 \log t_n -\log 2c)^2}{(\log t_n)^2}\right) \\
      &\leq c^2|\xi|^2\quad \text{for $t_n$ large enough.}
     
    \end{aligned}$$ So, there is a zone of control with constants $K_1=K_2 = c^2$, $v=w=2$ and $\gamma=1$, and $K= \frac{1}{2c}$. We thus get as before an estimate of $d_\mathrm{Kol}(Y_n,Y)$ of order $\mathcal{O}((t_n)^{-2})$, and since $(t_n \log t_n)^2 = n$, $(t_n)^2$ is asymptotically equivalent to $\frac{4n}{\log^2 n}$.0◻

 ◻
:::
