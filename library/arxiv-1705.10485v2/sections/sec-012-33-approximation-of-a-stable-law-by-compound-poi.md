---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-012-33-approximation-of-a-stable-law-by-compound-poi
section_title: "Approximation of a stable law by compound Poisson laws"
section_number: 3.3
pages: 21-26
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.97
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

## Convergence of Ornstein--Uhlenbeck processes to stable laws {#subsec:ornstein}

Another way to approximate a stable law $\phi_{c,\alpha,\beta}$ is by using the marginales of a random process of Ornstein--Uhlenbeck type. Consider more generally a self-decomposable law $\phi$ on $\mathbb{R}$, that is an infinitely divisible distribution such that for any $b\in (0,1)$, there exists a probability measure $p_b$ on $\mathbb{R}$ such that $$\widehat{\phi}(\xi) = \widehat{\phi}(b\xi)\,\widehat{p}_b(\xi);\label{eq:selfdecomposable}$$ see [@Sato99 Chapter 3, Definition 15.1]. In Equation [\[eq:selfdecomposable\]](#eq:selfdecomposable){reference-type="eqref" reference="eq:selfdecomposable"}, the laws $p_b$ are the marginale laws of certain Markov processes. Fix a Lévy--Khintchine triplet $(l\in \mathbb{R},\,\, \nu^2 \in \mathbb{R}_+,\,\,\rho)$ with $\rho$ probability measure on $\mathbb{R}\setminus \{0\}$ that integrates $\min(1,|x|^2)$, and consider the Lévy process $(Z_t)_{t \in \mathbb{R}_+}$ associated to this triplet: $$\begin{aligned}
\mathbb{E}[\E^{\I \xi Z_t}] &= \exp(t\psi(\I \xi)) \\
&=  \exp\left(t\left(\I l \xi - \frac{\nu^2\xi^2}{2}+\int_{\mathbb{R}} (\E^{\I \xi x} - 1 - 1_{|x|<1}\I \xi x)\,\rho(\!\,d\hspace*{-0.3mm}{x})\right)\right).
\end{aligned}$$ The Ornstein--Uhlenbeck process with triplet $(l,\nu^2,\rho)$, speed $v$ and starting point $x$ is the solution $(U_t)_{t \geq 0}$ of the stochastic differential equation $$U_t = \E^{-vt}x + \int_0^t \E^{-v(t-s)}\,dZ_s.$$ The Ornstein--Uhlenbeck process $(U_t)_{t \geq 0}$ can be shown to be a Markov process whose transition kernel $(P_t(x,\!\,d\hspace*{-0.3mm}{y}))_{t\geq 0}$ satisfies: $$\widehat{P_t(x,\cdot)}(\xi) =\int_{\mathbb{R}} \E^{\I \xi y}\,P_t(x,\!\,d\hspace*{-0.3mm}{y}) = \exp\left(\I \xi \E^{-vt} x + \int_{0}^t \psi(\I \xi\E^{-vs})\,d\hspace*{-0.3mm}{s} \right)$$ see [@Sato99 Lemma 17.1]. The connection with self-decomposable laws is provided by:

::: theorem
[]{#thm:selfdecomposable label="thm:selfdecomposable"} For any self-decomposable law $\phi$ and any fixed speed $v$, there exists a unique Lévy--Khintchine triplet $(l,\nu^2,\rho)$ with $\int_{|x|\geq 1}\log |x|\,\rho(\!\,d\hspace*{-0.3mm}{x})<+\infty$, such that the associated Ornstein--Uhlenbeck process $(U_t)_{t \geq 0}$ with speed $v$ satisfies: $$\forall x \in \mathbb{R},\,\,P_t(x,\cdot) \rightharpoonup \phi.$$ If $\psi(\I \xi)$ is the exponent associated to $(l,\nu^2,\rho)$, then $$\widehat{\phi}(\xi) = \exp\left(\int_{s=0}^\infty \psi(\I \xi\E^{-vs}) \,d\hspace*{-0.3mm}{s}\right).$$
:::

We refer to [@SY83] and [@Sato99 Theorem 17.5]. In the setting of Theorem [\[thm:selfdecomposable\]](#thm:selfdecomposable){reference-type="ref" reference="thm:selfdecomposable"}, one has the relation $$\widehat{\phi}(\xi) = \widehat{\phi}(\E^{-vt}\xi)\,\left(\widehat{P_t(x,\cdot)}(\xi)\,\widehat{\delta_{-\E^{-vt}x}}(\xi)\right),$$ so if $b \in (0,1)$, setting $b=\E^{-vt}$, one recovers $p_b$ as the law of $U_t-\E^{-vt}x$, where $(U_t)_{t \in \mathbb{R}_+}$ is the Ornstein--Uhlenbeck process that converges in distribution to $\phi$ and that has speed $v$ and starting point $x$.

Suppose that $\phi=\phi_{c,\alpha,\beta}$ is a stable law. Then, the previous computations can be reinterpreted in the framework of mod-$\phi$ convergence. We set $$\theta(\xi) =  \frac{\widehat{\delta_{x}}(\xi)}{\widehat{\phi}(\xi)} = \exp(\I \xi x - \eta(\I \xi)),$$ and $$X_t = \begin{cases}
     \E^{vt} U_t &\text{ if }\alpha \neq 1,\\
     \E^{vt} \left(U_t - \frac{2c\beta vt}{\pi}\right) &\text{ if }\alpha = 1.
\end{cases}$$ Then, $$\begin{aligned}
\mathbb{E}[\E^{\I \xi X_t}] &= \begin{cases}
    \widehat{\mu}(\E^{vt} \xi) \,\theta(\xi)&\text{ if }\alpha \neq 1,\\
    \widehat{\mu}(\E^{vt} \xi)\,\E^{-\I \xi \E^{vt} \frac{2c\beta vt}{\pi}} \,\theta(\xi)&\text{ if }\alpha = 1,
\end{cases}\\
&= \E^{\E^{\alpha vt}\eta(\I \xi)} \,\theta(\xi),
\end{aligned}$$ so $(X_t)_{t \geq 0}$ converges mod-$\phi$ with parameters $\E^{\alpha vt}$, and with limit equal to the residue $\theta(\xi)$. Note that $\theta_t = \theta$ for any $t \geq 0$, so we are in a special situation where the residues are constant (time-independent). Assuming that $x \neq 0$, one has for any $\xi \in \mathbb{R}$ $$|\theta(\xi)-1| \leq \begin{cases}
K_1\, |\xi|\,\exp(K_2\,|\xi|^\alpha) &\text{if }\alpha \in (1,2],\\
K_1\, |\xi|^{\alpha}\,\exp(K_2\,|\xi|^\alpha) & \text{if }\alpha \in (0,1) \text{ or }\alpha=1,\beta=0,\\
K_1\, |\xi|\log |\xi| \,\exp(K_2\,|\xi|) &\text{if }\alpha=1,\beta \neq 0.
\end{cases}$$ For the two first cases, the condition $\gamma \leq \min(\frac{1}{w-\alpha},\frac{v-1}{\alpha})$ in Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"} imposes the following choices of $\gamma$ when computing Berry--Esseen estimates: $\gamma = \frac{\alpha-1}{\alpha}$ when $\alpha\leq 1$, and $\gamma = 0$ when $\alpha \geq 1$. In these cases, one obtains: $$d_\mathrm{Kol}(U_t, \phi_{c,\alpha,\beta}) = \begin{cases}
    O(\E^{-vt}) &\text{ if } \alpha \in (1,2],\\
    O(\E^{-\alpha vt}) &\text{ if }\alpha \in (0,1) \text{ or }\alpha=1,\beta=0.
\end{cases}$$ Because of the term $\log |\xi|$, the last case does not exactly fit the framework of zones of control, but it is easy to adapt the proofs and one gets an estimate $O(vt\,\E^{-vt})$. On the other hand, when $x=0$, the only difference with the previous discussion is the case $\alpha \in (1,2]$, where we obtain $$|\theta(\xi)-1| \leq K_1\, |\xi|^\alpha\,\exp(K_2\,|\xi|^\alpha)$$ and by Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}, $d_\mathrm{Kol}(U_t,\phi_{c,\alpha,\beta}) = O(\E^{-\alpha vt})$, choosing $\gamma = \frac{\alpha-1}{\alpha}$. So, to summarise:

::: proposition
[]{#prop:ornstein label="prop:ornstein"} Let $Y$ be a random variable with stable law $\phi_{c,\alpha,\beta}$, and $(U_t)_{t \geq 0}$ be the corresponding Ornstein--Uhlenbeck process with starting point $x$ and speed $v$. We have: $$d_\mathrm{Kol}(U_t,Y) = \begin{cases}
     O(\E^{-vt})\!&\text{if }\alpha \in (1,2],x \neq 0,\\
    O(\E^{-\alpha vt})\!&\text{if }\alpha \in (0,1) \text{ or }\alpha =1,\beta =0 \text{ or }\alpha \in (1,2],x=0,\\
    O(vt\,\E^{-vt})\! &\text{if }\alpha=1,\beta \neq 0,
\end{cases}$$ with constants in the $O(\cdot)$ depending only on $x$ and $\alpha$.
:::
