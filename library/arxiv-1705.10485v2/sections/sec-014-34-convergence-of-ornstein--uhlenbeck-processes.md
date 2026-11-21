---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-014-34-convergence-of-ornstein--uhlenbeck-processes
section_title: "Convergence of Ornstein--Uhlenbeck processes to stable laws"
section_number: 3.4
pages: 24-26
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.954
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#subsec:ornstein label="subsec:ornstein"} Another way to approximate a stable law $\phi_{c,\alpha,\beta}$ is by using the marginales of a random process of Ornstein--Uhlenbeck type. Consider more generally a self-decomposable law $\phi$ on $\mathbb{R}$, that is an infinitely divisible distribution such that for any $b\in (0,1)$, there exists a probability measure $p_b$ on $\mathbb{R}$ such that $$\widehat{\phi}(\xi) = \widehat{\phi}(b\xi)\,\widehat{p}_b(\xi);\label{eq:selfdecomposable}$$ see [@Sato99 Chapter 3, Definition 15.1]. In Equation [\[eq:selfdecomposable\]](#eq:selfdecomposable){reference-type="eqref" reference="eq:selfdecomposable"}, the laws $p_b$ are the marginale laws of certain Markov processes. Fix a Lévy--Khintchine triplet $(l\in \mathbb{R},\,\, \nu^2 \in \mathbb{R}_+,\,\,\rho)$ with $\rho$ probability measure on $\mathbb{R}\setminus \{0\}$ that integrates $\min(1,|x|^2)$, and consider the Lévy process $(Z_t)_{t \in \mathbb{R}_+}$ associated to this triplet: $$\begin{aligned}
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
