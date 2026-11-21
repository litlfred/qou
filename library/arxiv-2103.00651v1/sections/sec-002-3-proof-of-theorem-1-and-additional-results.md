---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschitz Functions"
section_id: sec-002-3-proof-of-theorem-1-and-additional-results
section_title: "Proof of Theorem 1 and Additional Results"
section_number: 3
pages: 3-5
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.939
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschitz Functions — We derive two upper bounds for the probability of deviation of a vector-valued Lipschitz function of a collection of random"
---
[]{#sec:ProofMain label="sec:ProofMain"}

**Proof of the first bound in ([\[eq:MainThm_1\]](#eq:MainThm_1){reference-type="ref" reference="eq:MainThm_1"})**: The proof of the first bound relies on covering arguments; see [@v18; @w19; @lc20] and references therein for results based on such arguments. For some $\varepsilon$ in the interval $(0,1]$, let $\mathcal{N}(\varepsilon)$ be an $\varepsilon$-net of the unit Euclidean sphere $\mathbb{S}^{k-1}$ in $\mathbb{R}^k$ with cardinality $\left|\mathcal{N}(\varepsilon)\right|\leq \left(1+\frac{2}{\varepsilon}\right)^k$ [@v18]. Additionally, by Exercise 4.4.2 in [@v18],

$$\label{eq:MainThm_proof_1}
\left\|f(X)-E_{\nu}[f(X)]\right\|_2\leq \frac{1}{1-\varepsilon}\sup_{w \in \mathcal{N}(\varepsilon)}\langle w, f(X)-E_{\nu}[f(X)] \rangle\ \ \ \ \text{a.s.}$$ By ([\[eq:MainThm_proof_1\]](#eq:MainThm_proof_1){reference-type="ref" reference="eq:MainThm_proof_1"}) and by Boole's inequality (union bound) we have that $$\begin{aligned}
\label{eq:MainThm_proof_2}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)&\leq P\left(\sup_{w \in \mathcal{N}(\varepsilon)}\langle w, f(X)-E_{\nu}[f(X)] \rangle \geq \epsilon (1-\varepsilon)\right) \nonumber\\&\leq \sum_{w\in \mathcal{N}(\varepsilon)}P\left(\langle w, f(X)-E_{\nu}[f(X)] \rangle \geq \epsilon (1-\varepsilon)\right)\nonumber\\&\leq |\mathcal{N}(\varepsilon)| \inf_{\lambda>0} e^{-\lambda \epsilon (1-\varepsilon)}E_{\nu}\left[e^{\lambda  \langle w_{*}, f(X)-E_{\nu}[f(X)] \rangle }\right],
\end{aligned}$$ where the last inequality follows from the Chernoff bound [@rs13] and $$w_{*}=\arg\max_{w\in \mathcal{N}(\varepsilon)} P\left(\langle w, f(X)-E_{\nu}[f(X)] \rangle \geq \epsilon (1-\varepsilon)\right).$$ We now note that the function $\langle w_{*}, f(x)-E_{\nu}[f(X)] \rangle$ is $\|f\|_{\rm Lip}$-Lipschitz by the Cauchy---Schwarz inequality and $\langle w_{*}, f(X)-E_{\nu}[f(X)] \rangle$ is mean zero. Assuming that $W_{1}(\mu,\nu)\leq \sqrt{2\sigma^2 D(\mu\|\nu)}, \forall \mu$ holds, an application of the theorem of Bobkov and Götze implies that $$\begin{aligned}
\label{eq:MainThm_proof_3}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)&\leq |\mathcal{N}(\varepsilon)| \inf_{\lambda>0} e^{-\lambda \epsilon (1-\varepsilon)+\frac{\lambda^2\sigma^2 \|f\|_{\rm Lip}^2}{2}}.
\end{aligned}$$ The exponent in the right-hand side of ([\[eq:MainThm_proof_3\]](#eq:MainThm_proof_3){reference-type="ref" reference="eq:MainThm_proof_3"}) is minimized for $\lambda_{*}=\frac{\epsilon (1-\varepsilon)}{\sigma^2\|f\|_{\rm Lip}^2}>0$ leading to $$\begin{aligned}
\label{eq:MainThm_proof_4}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)&\leq |\mathcal{N}(\varepsilon)| e^{-\frac{\epsilon^2 (1-\varepsilon)^2}{2\sigma^2\|f\|_{\rm Lip}^2}}.
\end{aligned}$$ By employing the bound on $|\mathcal{N}(\varepsilon)|$ the desired result follows.

**Proof of the second bound in ([\[eq:MainThm_1\]](#eq:MainThm_1){reference-type="ref" reference="eq:MainThm_1"})**: Using a similar argument as in [@hkz12], let $Z\sim \mathcal{N}(0,I_k)$ be a standard Gaussian random vector, which is independent of $X$. Recall that $E[e^{\langle Z,q \rangle}]=e^{\frac{\|q\|_2^2}{2}}, \forall q\in \mathbb{R}^k$. For any $\lambda \in \mathbb{R}$ we note that $$\begin{aligned}
&E\left[e^{\lambda \langle Z,f(X)-E_{\nu}[f]\rangle}\right]\geq\\&  E\left.\left[e^{\lambda \langle Z, f(X)-E_{\nu}[f] \rangle}\right|\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon\right]P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)=\\& E_{\nu}\left.\left[E_Z\left[e^{\lambda \langle Z, f(X)-E_{\nu}[f] \rangle}\right]\right|\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon\right]P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)=\\& E_{\nu}\left.\left[e^{\frac{\lambda^2 \|f(X)-E_{\nu}[f] \|_2^2}{2}}\right|\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon\right]P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)\geq \\& e^{\frac{\lambda^2 \epsilon^2}{2}} P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)
\end{aligned}$$ or $$\begin{aligned}
\label{eq:MainThm_proof_5}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)\leq e^{-\frac{\lambda^2 \epsilon^2}{2}} E\left[e^{\lambda \langle Z,f(X)-E_{\nu}[f]\rangle}\right].
\end{aligned}$$ We now note that the function $\langle Z, f(x)-E_{\nu}[f(X)] \rangle$ is $\|Z\|_2\|f\|_{\rm Lip}$-Lipschitz when $Z$ is fixed (by the Cauchy---Schwarz inequality) and $\langle Z, f(X)-E_{\nu}[f(X)] \rangle$ is mean zero. Assuming that $W_{1}(\mu,\nu)\leq \sqrt{2\sigma^2 D(\mu\|\nu)}, \forall \mu$ holds, an application of the theorem of Bobkov and Götze implies that $$\begin{aligned}
E\left[e^{\lambda \langle Z,f(X)-E_{\nu}[f]\rangle}\right]&=E_{Z}\left[E_{\nu}\left[e^{\lambda \langle Z,f(X)-E_{\nu}[f]\rangle}\right]\right] \leq E_Z\left[e^{\frac{\lambda^2 \|Z\|_2^2\sigma^2 \|f\|_{\rm Lip}^2}{2}}\right].  
\end{aligned}$$ Moreover, $\|Z\|_2^2$ is a chi-squared random variable with $k$ degrees of freedom and for such a random variable $E\left[e^{t\|Z\|_2^2}\right]=\frac{1}{(1-2t)^{k/2}}, \ \ t<\frac{1}{2}$. Therefore, we conclude that $$\begin{aligned}
\label{eq:MainThm_proof_6}
E\left[e^{\lambda \langle Z,f(X)-E_{\nu}[f]\rangle}\right]\leq E_Z\left[e^{\frac{\lambda^2 \|Z\|_2^2\sigma^2 \|f\|_{\rm Lip}^2}{2}}\right]= \frac{1}{\left(1-\lambda^2 \sigma^2 \|f\|_{\rm Lip}^2\right)^{k/2}},  
\end{aligned}$$ where the last equality holds for any $\lambda\in \mathbb{R}$ such that $\lambda^2 \sigma^2 \|f\|_{\rm Lip}^2<1$. By combining ([\[eq:MainThm_proof_5\]](#eq:MainThm_proof_5){reference-type="ref" reference="eq:MainThm_proof_5"}) and ([\[eq:MainThm_proof_6\]](#eq:MainThm_proof_6){reference-type="ref" reference="eq:MainThm_proof_6"}) we obtain $$\begin{aligned}
\label{eq:MainThm_proof_7}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)\leq \frac{e^{-\frac{\lambda^2 \epsilon^2}{2}}}{\left(1-\lambda^2 \sigma^2 \|f\|_{\rm Lip}^2\right)^{k/2}}, \ \ |\lambda|<\frac{1}{\sigma \|f\|_{\rm Lip}}. 
\end{aligned}$$ Choosing $\lambda=\frac{1}{\sqrt{2}\sigma \|f\|_{\rm Lip}}$, we conclude that $$\begin{aligned}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)\leq 2^{\frac{k}{2}}e^{-\frac{\epsilon^2}{4\sigma^2 \|f\|_{\rm Lip}^2}}.
\end{aligned}$$ $\square$

In the previous proof and more specifically in ([\[eq:MainThm_proof_3\]](#eq:MainThm_proof_3){reference-type="ref" reference="eq:MainThm_proof_3"}) and ([\[eq:MainThm_proof_6\]](#eq:MainThm_proof_6){reference-type="ref" reference="eq:MainThm_proof_6"}), the theorem of Bobkov and Götze for the mean zero, vector-valued function $f(X)-E_{\nu}[f(X)]$ has been applied via a real-valued function of the form $\langle g,f(X)-E_{\nu}[f(X)]\rangle$ with $g=w_{*}$ and $g=Z$, respectively. This suggests the following extension of the theorem of Bobkov and Götze for vector-valued Lipschitz functions:

::: prop
[]{#prop:Bobkov-Gotze_extension label="prop:Bobkov-Gotze_extension"} (**Theorem of Bobkov and Götze for Vector-Valued Functions**) Let $(\mathbb{X},d_{\mathbb{X}})$ and $(\mathbb{Y},d_{\mathbb{Y}})$ be two Polish spaces, where $\mathbb{Y}\subseteq \mathbb{R}^k$ and $d_{\mathbb{Y}}$ is an $\ell_p$-metric for some $p\geq 1$. Let $X$ be a random variable taking values in $\mathbb{X}$ and assume that $X\sim \nu$, where $\nu$ is a probability measure on $(\mathbb{X},d_{\mathbb{X}})$. Then, the following statements are equivalent:

1.  $W_{1}(\mu,\nu)\leq \sqrt{2\sigma^2 D(\mu\|\nu)}, \forall \mu$

2.  $f(X)-E_{\nu}[f(X)]$, for every function $f\in {\rm Lip}(\mathbb{X},\mathbb{Y},d_{\mathbb{X}},d_{\mathbb{Y}})$ such that $\|E_{\nu}[f]\|_\infty<\infty$, is a sub-Gaussian vector with $\sigma^2\|h\|_q^2\|f\|_{\rm Lip}^2$-sub-Gaussian one-dimensional marginals $\langle h,f(X)-E_{\nu}[f(X)]\rangle$, i.e., $$\label{eq:Bobkov_Gotze_extension_1}
    E_{\nu}\left[e^{\lambda \langle h,f(X)-E_{\nu}[f(X)]\rangle}\right]\leq e^{\frac{\lambda^2 \|h\|_q^2 \sigma^2 \|f\|_{\rm Lip}^2}{2}}, \forall h\in \mathbb{R}^{k}, \forall \lambda\in \mathbb{R}.$$ Here, $\|\cdot\|_q$ corresponds to the dual norm of $\|\cdot\|_p$.
:::

The direction "**$1.$ implies $2.$**" can be obtained by the theorem of Bobkov and Götze for the real-valued function $\langle h, f(x)-E_{\nu}[f(X)]\rangle$ by invoking Hölder's inequality to show that the corresponding Lipschitz constant is at most $\|h\|_q \|f\|_{\rm Lip}$. The direction "**$2.$ implies $1.$**" is a direct consequence of the theorem of Bobkov and Götze by choosing $f$ to have only one nonzero coordinate, e.g., $f=\tilde{f}e_1$ and $h=e_1$. Here, $\tilde{f}:\mathbb{X}\rightarrow \mathbb{R}$ is any real-valued $\|f\|_{\rm Lip}$-Lipschitz function and $e_1$ is the first element of the canonical basis in $\mathbb{R}^k$.
