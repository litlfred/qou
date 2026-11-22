---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschitz Functions"
section_id: sec-001-2-preliminaries-and-main-result
section_title: "Preliminaries and Main Result"
section_number: 2
pages: 2-3
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.962
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschitz Functions — We derive two upper bounds for the probability of deviation of a vector-valued Lipschitz function of a collection of random"
---
Let $(\mathbb{X},d_{\mathbb{X}})$ be a Polish space and $\rho$ be a (Borel) probability measure on $(\mathbb{X},d_{\mathbb{X}})$. The triplet $(\mathbb{X},d_{\mathbb{X}},\rho)$ defines a metric probability space in the sense of Gromov [@rs13], [@g07]. Given two metric spaces $(\mathbb{X}, d_{\mathbb{X}})$ and $(\mathbb{Y}, d_{\mathbb{Y}})$, let $f:\mathbb{X}\rightarrow \mathbb{Y}$ be a Lipschitz mapping with Lipschitz constant $\|f\|_{\rm Lip}$, i.e., $d_{\mathbb{Y}}(f(x),f(\tilde{x}))\leq \|f\|_{\rm Lip} d_{\mathbb{X}}(x,\tilde{x}),$ $\forall x,\tilde{x}\in \mathbb{X}$. In the following, the set of all such mappings will be denoted by ${\rm Lip}(\mathbb{X},\mathbb{Y},d_{\mathbb{X}},d_{\mathbb{Y}})$. Moreover, let $\mathbb{P}_{1}(\mathbb{X})$ denote the set of all probability measures $\rho$ on $\mathbb{X}$ such that $E_{\rho}[d_{\mathbb{X}}(X,x_0)]<\infty$ holds for an arbitrary (and therefore for all) $x_0\in \mathbb{X}$. The $L^1$ Wasserstein distance between $\rho,\tilde{\rho}\in \mathbb{P}_1(\mathbb{X})$ is defined as $$\label{eq:defin1}
W_{1}(\rho,\tilde{\rho})=\inf_{X\sim \rho,\tilde{X}\sim \tilde{\rho}}E[d_{\mathbb{X}}(X,\tilde{X})]=\inf_{\gamma\in \Pi(\rho,\tilde{\rho})}\int_{\mathbb{X}\times \mathbb{X}}d_{\mathbb{X}}(x,\tilde{x})\gamma(dx,d\tilde{x}).$$ The infimum in the first part is taken over all jointly distributed pairs $(X,\tilde{X})$ on the product space $\mathbb{X}^2=\mathbb{X}\times \mathbb{X}$ with marginals $\rho,\tilde{\rho}$, respectively. In the last part, $\Pi(\rho,\tilde{\rho})$ denotes the set of all possible couplings of $\rho,\tilde{\rho}$. An optimal coupling $\gamma^{*}\in \Pi(\rho,\tilde{\rho})$ achieving the infimum exists [@rs13], [@v08]. Additionally, a different measure gauging the dissimilarity between two probability measures $\rho,\tilde{\rho}$ is the relative entropy or Kullback-Leibler divergence $D(\tilde{\rho}\| \rho)=E_{\tilde{\rho}}\left[\log \frac{d\tilde{\rho}}{d\rho}\right]=E_{\rho}\left[\frac{d\tilde{\rho}}{d\rho}\log \frac{d\tilde{\rho}}{d\rho}\right]$ for $\tilde{\rho}\ll \rho$ and $D(\tilde{\rho}\| \rho)=\infty$ otherwise, where $d\tilde{\rho}/d\rho$ is the Radon-Nikodym derivative of $\tilde{\rho}$ with respect to $\rho$ and $\tilde{\rho}\ll \rho$ denotes that $\tilde{\rho}$ is absolutely continuous with respect to $\rho$.

The following theorem provides a concentration inequality for $f(X)$ when the deviation from $E_{\nu}[f(X)]$ is measured in terms of the $\ell_2$-metric.

::: theorem
[]{#thm:MainThm label="thm:MainThm"} Let $(\mathbb{X},d_{\mathbb{X}})$ and $(\mathbb{Y},d_{\mathbb{Y}})$ be two Polish spaces, where $\mathbb{Y}\subseteq \mathbb{R}^k$ and $d_{\mathbb{Y}}(y,\tilde{y})=\|y-\tilde{y}\|_2$ with $\|\cdot\|_2$ being the Euclidean norm. Let $X$ be a random variable taking values in $\mathbb{X}$ and assume that $X\sim \nu$, where $\nu$ is a probability measure on $(\mathbb{X},d_{\mathbb{X}})$. Then, the inequality $W_{1}(\mu,\nu)\leq \sqrt{2\sigma^2 D(\mu\|\nu)}, \forall \mu$ implies that $\forall \epsilon>0$, $\forall \varepsilon\in (0,1]$ and for any $f\in {\rm Lip}(\mathbb{X},\mathbb{Y},d_{\mathbb{X}},\|\cdot\|_2)$ such that $\|E_{\nu}[f]\|_\infty<\infty$, $$\begin{aligned}
\label{eq:MainThm_1}
P(\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon)\leq \min\left\{\left(1+\frac{2}{\varepsilon}\right)^k e^{-\frac{\epsilon^2 (1-\varepsilon)^2}{2 \sigma^2\|f\|_{\rm Lip}^2}}, 2^{\frac{k}{2}}e^{-\frac{\epsilon^2}{4\sigma^2 \|f\|_{\rm Lip}^2}}\right\}.
\end{aligned}$$
:::

The proof of this theorem is provided in Section [\[sec:ProofMain\]](#sec:ProofMain){reference-type="ref" reference="sec:ProofMain"}. This result can be straightforwardly extended to any $\ell_p$-metric for $p\geq 1, p\neq 2$. Define $$\begin{aligned}
\label{eq:MainThm_3}
\tau_p&=\sup_{y\in f(\mathbb{X})}\frac{\|y-E_{\nu}[f(X)]\|_p}{\|y-E_{\nu}[f(X)]\|_2}.
\end{aligned}$$ Here, $y$ is assumed different from $E_{\nu}[f(X)]$ if $E_{\nu}[f(X)]\in f(\mathbb{X})$, since for $y=E_{\nu}[f(X)]$ (if $E_{\nu}[f(X)]\in f(\mathbb{X})$) the inequality $\|y-E_{\nu}[f(X)]\|_p\leq \tau_p \|y-E_{\nu}[f(X)]\|_2$ trivially holds for any $\tau_p>0$. Then, ([\[eq:MainThm_1\]](#eq:MainThm_1){reference-type="ref" reference="eq:MainThm_1"}) can be replaced by $$\begin{aligned}
\label{eq:MainThm_4}
P(\|f(X)-E_{\nu}[f(X)]\|_p\geq \epsilon)\leq \min\left\{\left(1+\frac{2}{\varepsilon}\right)^k e^{-\frac{\epsilon^2 (1-\varepsilon)^2}{2\tau_p^2 \sigma^2\|f\|_{\rm Lip}^2}}, 2^{\frac{k}{2}}e^{-\frac{\epsilon^2}{4\sigma^2\tau_p^2 \|f\|_{\rm Lip}^2}}\right\}
\end{aligned}$$ due to $\{\|f(X)-E_{\nu}[f(X)]\|_p\geq \epsilon\}\subseteq \{\|f(X)-E_{\nu}[f(X)]\|_2\geq \epsilon/\tau_p\}$ by ([\[eq:MainThm_3\]](#eq:MainThm_3){reference-type="ref" reference="eq:MainThm_3"}).
