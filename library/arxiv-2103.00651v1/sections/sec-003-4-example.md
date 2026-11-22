---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschitz Functions"
section_id: sec-003-4-example
section_title: "Example"
section_number: 4
pages: 5-9
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.614
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschitz Functions — We derive two upper bounds for the probability of deviation of a vector-valued Lipschitz function of a collection of random"
---
Consider a sample $X_{0:n-1}=\{X_0,X_1,\ldots, X_{n-1}\}$ of size $n$ drawn from an ergodic, discrete-time, finite-state Markov chain $(X_k)_{k\geq 0}$ with state space $\mathbb{E}=[K]=\{1,2,\ldots, K\}$, transition matrix $\mathrm{P}=[\mathrm{P}_{ij}]$ and $X_0\sim \varrho$, where $\varrho$ denotes the initial measure of the chain. We denote such a Markov chain by $(\mathrm{P},\varrho)$ and the corresponding stationary chain by $(\mathrm{P},\pi)$, where $\pi$ is the underlying invariant measure. Let the chain be $r$-contractive with Dobrushin coefficient $r<1$. Consider the natural plug-in estimators for the stationary probabilities: $$\hat{\pi}_i(X_{0:n-1})=\frac{1}{n}\sum_{k=0}^{n-1}\mathbbm{1}(X_k=i).$$ By the Ergodic Theorem for Markov chains [@b13], $\hat{\pi}_i\rightarrow \pi_i, \forall i\in \mathbb{E}$ with probability $1$ as $n\rightarrow \infty$ for any initial measure $\varrho$.

The distance of $(\mathrm{P},\varrho)$ from stationarity can be quantified by the (nonstationarity) index [@p15] $$\label{eq:index}
\left\|\frac{\varrho}{\pi}\right\|^2_{2,\pi}=E_{\pi}\left[\left(\frac{d\varrho}{d\pi}\right)^2\right]=\sum_{i\in \mathbb{E}} \left[\frac{\varrho(i)}{\sqrt{\pi(i)}}\right]^2,$$ where the first equality corresponds to the general definition of the index for $\varrho\ll \pi$ and the second equality is the specialization of this definition to our setting. Furthermore, $1\leq \left\|\varrho/\pi\right\|_{2,\pi}\leq \infty$ and $\|\cdot\|_{2,\pi}$ is the norm induced by the inner product $\langle f,g \rangle_{\pi}=\sum_{i\in \mathbb{E}} f(i)g(i)\pi(i)$ in $\ell^2(\pi)$ [@lpw09]. Due to ergodicity, $\min_{i\in \mathbb{E}}\pi(i)>0$ and also $\left\|\varrho/\pi\right\|_{2,\pi}\leq 1/\sqrt{\min_{i\in \mathbb{E}}\pi(i)}$. Additionally, $\left\|\varrho/\pi\right\|_{2,\pi}=1$ for $\varrho=\pi$ and $\left\|\varrho/\pi\right\|_{2,\pi}=\infty$ if $\varrho$ is not absolutely continuous with respect to $\pi$.

The index in ([\[eq:index\]](#eq:index){reference-type="ref" reference="eq:index"}) is useful in our context due to the following theorem [@p15]:

::: theorem
[]{#thm:Paulin label="thm:Paulin"} Let $X_{0:n-1}$ be a sample drawn from a time-homogeneous Markov chain $(\mathrm{P},\varrho)$ with state space $\mathbb{E}$ and stationary measure $\pi$. Then for any measurable function $g:\mathbb{E}^{n}\rightarrow \mathbb{R}$ and $\forall \epsilon>0$, $$P_{\varrho}\left(g(X_{0:n-1}\right)\geq \epsilon)\leq \left\|\frac{\varrho}{\pi}\right\|_{2,\pi}\sqrt{P_{\pi}(g(X_{0:n-1})\geq \epsilon)},$$ where $P_{\varrho}$ is the law of $(\mathrm{P},\varrho)$ and $P_{\pi}$ is the law of $(\mathrm{P},\pi)$.
:::

Our goal is to bound $P_{\varrho}(\|\hat{\pi}-\pi\|_{p}\geq \epsilon)=P_{\varrho}(\|\hat{\pi}-E_{\pi}[\hat{\pi}]\|_p\geq \epsilon)$ for $p\geq 1$. To tackle the problem within the transportation method framework, we will use the following theorem due to Marton [@m96] adapted to our setting:

::: theorem
[]{#thm:Marton label="thm:Marton"} Consider a Markov chain $(X_k)_{k\geq 0}$ with a finite state space $\mathcal{X}$, transition matrix $P=[P_{ij}]$ and Dobrushin coefficient $r<1$. For $x_{0:n-1},\tilde{x}_{0:n-1}\in \mathcal{X}^{n}$ let $\tilde{d}_{1,\mathcal{X}^{n}}(x_{0:n-1},\tilde{x}_{0:n-1})=\sum_{k=0}^{n-1}\mathbbm{1}(x_k\neq \tilde{x}_k)$. Then, $$W_{1}\left(\mu,\nu\right)\leq \left[\frac{n}{2(1-r)^2}D(\mu\| \nu)\right]^{1/2},$$ where $\nu=P_{\varrho}$ is the measure on $(\mathbb{X}=\mathcal{X}^{n},d_{\mathbb{X}}=\tilde{d}_{1,\mathcal{X}^{n}})$ due to the Markov chain starting at some arbitrary initial measure $\varrho$ and $\mu$ is any measure on $(\mathbb{X},d_{\mathbb{X}})$.
:::

We now compare different approaches for bounding $P_{\varrho}(\|\hat{\pi}-\pi\|_{p}\geq \epsilon)$ and show that the bound obtained in Theorem 1 gives better results than other, more direct applications of the theorem of Bobkov and Götze.

**Approach 1: Direct application of the theorem of Bobkov and Götze**. Let $f(x)=f(x_{0:n-1})=\|\hat{\pi}(x_{0:n-1})-\pi\|_{p}$. Assume that $x=x_{0:n-1}$ and $\tilde{x}=\tilde{x}_{0:n-1}$ are two realizations of the random sequence $X_{0:n-1}$, which differ at a single element. By employing the reverse triangle inequality for the $\ell_p$-norm we obtain $$\begin{aligned}
\label{eq:Lipschitz_example_1}
\left|f(x)-f(\tilde{x})\right|&\leq \|\hat{\pi}(x_{0:n-1})-\hat{\pi}(\tilde{x}_{0:n-1})\|_{p}\nonumber\\&\leq \frac{\sqrt[p]{2}}{n}= \frac{\sqrt[p]{2}}{n} \tilde{d}_{1,\mathbb{E}^n}(x_{0:n-1},\tilde{x}_{0:n-1})=\frac{\sqrt[p]{2}}{n} \sum_{k=0}^{n-1}\mathbbm{1}(x_k\neq \tilde{x}_k).
\end{aligned}$$ Clearly, ([\[eq:Lipschitz_example_1\]](#eq:Lipschitz_example_1){reference-type="ref" reference="eq:Lipschitz_example_1"}) implies that $\|f\|_{\rm Lip}=\sqrt[p]{2}/n$ for any $x_{0:n-1},\tilde{x}_{0:n-1}$ (not necessarily different at a single element). This can be easily seen by expressing $\hat{\pi}(x_{0:n-1})=(1/n)\sum_{k=0}^{n-1}\sum_{i=1}^{K}\mathbbm{1}(x_{k}=i)e_i$, where $\{e_1,\ldots, e_K\}$ is the canonical basis in $\mathbb{R}^K$.

Consider the stationary chain $(\mathrm{P},\pi)$. An application of the theorem of Bobkov and Götze (one-sided version) combined with Theorem [\[thm:Marton\]](#thm:Marton){reference-type="ref" reference="thm:Marton"} gives $$P_{\pi}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]+\epsilon)\leq e^{-2^{1-2/p}n \epsilon^2 (1-r)^2}, \ \ \forall \epsilon>0$$ or equivalently, $\forall \epsilon>E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]$, $$P_{\pi}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq e^{-2^{1-2/p}n\left(\epsilon-E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]\right)^2 (1-r)^2}.$$ Theorem [\[thm:Paulin\]](#thm:Paulin){reference-type="ref" reference="thm:Paulin"} now implies that $\forall \epsilon>E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]$, $$P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \left\|\frac{\varrho}{\pi}\right\|_{2,\pi} e^{-2^{-2/p}n\left(\epsilon-E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]\right)^2 (1-r)^2}.$$ Finally, for any $\delta\in (0,1)$ and any $\epsilon>E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]$, $P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \delta$ for any $n$ such that $$\label{eq:sample_complexity_Markov_1}
n\geq \frac{2^{\frac{2}{p}} \log\left(\frac{\left\|\frac{\varrho}{\pi}\right\|_{2,\pi}}{\delta}\right)}{\left(\epsilon-E_{\pi}[\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}]\right)^2(1-r)^2}.$$ $\newline$

**Approach 2: A union bound approach**

We may try to eliminate the problem of $\epsilon$ being *bounded away from zero* by using the observation that any $\ell_p$-norm is separable in the corresponding coordinates. We have $$\begin{aligned}
P_{\pi}(\|\hat{\pi}-\pi\|_{p}\geq \epsilon)&=P_{\pi}\left(\sum_{i=1}^K|\hat{\pi}_i-\pi_i|^p\geq \epsilon^p\right)\leq \sum_{i=1}^K P_{\pi}\left(|\hat{\pi}_i-E_{\pi}[\hat{\pi}_i]|\geq \frac{\epsilon}{\sqrt[p]{K}}\right),
\end{aligned}$$ where the union bound and the fact that $\hat{\pi}_i$ are unbiased estimators $\forall i$ have been used. In this case $f(x)=f(x_{0:n-1})=\hat{\pi}_i(x_{0:n-1})$, therefore $$|f(x)-f(\tilde{x})| \leq \frac{1}{n} \tilde{d}_{1,\mathbb{E}^n}(x_{0:n-1},\tilde{x}_{0:n-1}), \ \ \forall x_{0:n-1},\tilde{x}_{0:n-1}\in \mathbb{E}^n.$$ By combining the theorem of Bobkov and Götze with Theorems [\[thm:Paulin\]](#thm:Paulin){reference-type="ref" reference="thm:Paulin"} and [\[thm:Marton\]](#thm:Marton){reference-type="ref" reference="thm:Marton"} we obtain: $$\label{eq:scalarized_bound_Markov_1}
P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \sqrt{2K}\left\|\frac{\varrho}{\pi}\right\|_{2,\pi} e^{-K^{-2/p}n\epsilon^2 (1-r)^2}.$$

Finally, for any $\delta\in (0,1)$ and any $\epsilon>0$, $P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \delta$ for any $n$ such that $$\label{eq:sample_complexity_Markov_2}
n\geq \frac{K^{\frac{2}{p}} \log\left(\frac{\sqrt{2K}\left\|\frac{\varrho}{\pi}\right\|_{2,\pi}}{\delta}\right)}{\epsilon^2(1-r)^2}.$$

**Approach 3: Application of Theorem [\[thm:MainThm\]](#thm:MainThm){reference-type="ref" reference="thm:MainThm"}**

For simplicity, we will work with the first bound in ([\[eq:MainThm_1\]](#eq:MainThm_1){reference-type="ref" reference="eq:MainThm_1"}). Note that by working with both bounds in ([\[eq:MainThm_1\]](#eq:MainThm_1){reference-type="ref" reference="eq:MainThm_1"}) we can only obtain an improvement of the derived sample complexity.

We observe that by the usual norm equivalence constants, the definition of $\tau_p$ in ([\[eq:MainThm_3\]](#eq:MainThm_3){reference-type="ref" reference="eq:MainThm_3"}) and the hierarchy of $\ell_p$-norms in $\mathbb{R}^k$ we have that $\tau_1\leq \sqrt{k}$, $\tau_2=1$, $\tau_p\leq 1$ for any $p>2$ and $\tau_{p_1}\leq \tau_{p_2}$ for $p_1\geq p_2$. By Theorems [\[thm:MainThm\]](#thm:MainThm){reference-type="ref" reference="thm:MainThm"}, [\[thm:Paulin\]](#thm:Paulin){reference-type="ref" reference="thm:Paulin"} and [\[thm:Marton\]](#thm:Marton){reference-type="ref" reference="thm:Marton"} we obtain that $\forall \epsilon>0$ and $\forall \varepsilon \in (0,1]$, $$\label{eq:Bobkov_Gotze_Extension_Markov_probability_bound}
P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \left\|\frac{\varrho}{\pi}\right\|_{2,\pi} \left(1+\frac{2}{\varepsilon}\right)^{\frac{K}{2}}e^{-\frac{n\epsilon^2(1-\varepsilon)^2(1-r)^2}{2 \tau_p^2}}.$$ Therefore, for any $\delta\in (0,1)$, any $\epsilon>0$ and any $\varepsilon\in (0,1]$, $P_{\varrho}(\|\hat{\pi}(X_{0:n-1})-\pi\|_{p}\geq \epsilon)\leq \delta$ for any $n$ such that $$\label{eq:sample_complexity_Markov_3}
n\geq \frac{2\tau_p^2}{\epsilon^2(1-\varepsilon)^2(1-r)^2}\left[\frac{K}{2}\log\left(1+\frac{2}{\varepsilon}\right)+\log\left(\left\|\frac{\varrho}{\pi}\right\|_{2,\pi}\right)+\log\left(\frac{1}{\delta}\right)\right].$$

**Sample Complexity Comparisons**

We first note that $\left\|\varrho/\pi\right\|_{2,\pi}\leq 1/\sqrt{\min_{i\in \mathbb{E}}\pi(i)}$ and often $\min_{i\in \mathbb{E}}\pi(i)\asymp 1/K^{m}$ for some $m\geq 1$. For a rough complexity comparison between ([\[eq:sample_complexity_Markov_1\]](#eq:sample_complexity_Markov_1){reference-type="ref" reference="eq:sample_complexity_Markov_1"}) and ([\[eq:sample_complexity_Markov_3\]](#eq:sample_complexity_Markov_3){reference-type="ref" reference="eq:sample_complexity_Markov_3"}) consider for simplicity the special case of i.i.d. random variables and $p=1$. In this setting, we correspondingly work with $P_{\pi}(\cdot)$ only (only $P_{\pi}(\cdot)$ is meaningful). It turns out that $E_{\pi}[\|\hat{\pi}-\pi\|_1]\lesssim K/\sqrt{n}$. Then, ([\[eq:sample_complexity_Markov_1\]](#eq:sample_complexity_Markov_1){reference-type="ref" reference="eq:sample_complexity_Markov_1"}) and ([\[eq:sample_complexity_Markov_3\]](#eq:sample_complexity_Markov_3){reference-type="ref" reference="eq:sample_complexity_Markov_3"}) are orderwise the same, but without the problem of $\epsilon$ being bounded away from zero in ([\[eq:sample_complexity_Markov_3\]](#eq:sample_complexity_Markov_3){reference-type="ref" reference="eq:sample_complexity_Markov_3"}). Further, ([\[eq:sample_complexity_Markov_3\]](#eq:sample_complexity_Markov_3){reference-type="ref" reference="eq:sample_complexity_Markov_3"}) is better by a **logarithmic in $K$ factor** over ([\[eq:sample_complexity_Markov_2\]](#eq:sample_complexity_Markov_2){reference-type="ref" reference="eq:sample_complexity_Markov_2"}) for $p\in\{1,2\}$. For chains such that $\min_{i\in \mathbb{E}}\pi(i)\asymp 1/e^K$, ([\[eq:sample_complexity_Markov_3\]](#eq:sample_complexity_Markov_3){reference-type="ref" reference="eq:sample_complexity_Markov_3"}) is better by a **$K$ factor** over ([\[eq:sample_complexity_Markov_2\]](#eq:sample_complexity_Markov_2){reference-type="ref" reference="eq:sample_complexity_Markov_2"}) for $p\in\{1,2\}$. We also note that depending on the geometry of $f(\mathbb{X})$, $f$ and $\nu$, $\tau_p$ may or may not have a favorable value for a particular $p$. More specifically, it is possible that the last approach is orderwise better than the union bound approach for some choices of $p$, primarily for $p\in \{1,2\}$, while it is worse for other values of $p$, depending on the particular problem at hand.

# Acknowledgment

This work was supported by the ONR Grant Navy N00014-19-1-2566.
