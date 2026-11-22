---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble"
section_id: sec-002-21-configuration-spaces-and-lebesgue-poisson-mea
section_title: "Configuration spaces and Lebesgue-Poisson measure."
section_number: 2.1
pages: 3-4
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical canonical ensemble is"
---
Let $\sigma$ be a Lebesgue measure in $\Bbb R^d$. *Configuration space* $\Gamma\;: = \; \Gamma_{\Bbb R^d}$ consists of all locally finite subsets of the space $\Bbb R^d$. This definition is quite natural from the point of view of physics, because an infinite number of particles cannot be in a bounded volume.

Denote the set of all finite configurations of the space $\Gamma$ by $\Gamma_0$, and by $\Gamma^{(n)}$ configuration space with a fixed number of points.

If all such configurations are in some bounded set $\Lambda\subset\Bbb R^d$, then the corresponding space will be $\Gamma^{(n)}_\Lambda$.

State of an ideal gas in equilibrium statistical mechanics is described by the *Poisson* measure $\pi_{z \sigma}$ on configuration space $\Gamma$, where $z> 0$ is the activity (physical parameter that associated with the density of particles in the system).

But we need so-called Lebesgue-Poisson measure, i.e. the Poisson measure on the space of finite configurations, which in some sense is absolutely continuous with respect to the Lebesgue measure in contrast to the $\pi_{\sigma}$ measure for $\Gamma$. Integral for Lebesgue-Poisson measure in space $\Gamma_0$ (or $\Gamma_\Lambda$) is determined by the formula: $$\begin{aligned}
\label{IL-P}
\int_{\Gamma_X}F(\gamma)\lambda_{z\sigma}(d\gamma)\;&:=\;\sum_{n=0}^\infty\frac{z^n}{n!}\int_X\cdots\int_X
F(\{x_1,...,x_n\})\sigma(dx_1)\cdots\sigma(dx_n)=\notag\\
&=\sum_{n=0}^\infty\frac{z^n}{n!}\int_X\cdots\int_X
F_n(x_1,...,x_n)dx_1\cdots dx_n,
\end{aligned}$$ for all measurable functions $F = \{F_n \}_{n \geq 0}$, $F_n \in L^{1}(X^n)$, and $\Gamma_X \in \{\Gamma_0, \Gamma_\Lambda$). Such measure not only simplifies the recording of cumbersome expressions and combinatorial proofs, but also allows to get some new results based on properties infinite divisibility (see, for example, [@Re93; @ReSh97; @Re98; @PR07].

In the language of integrals with the measure $\lambda_{z\sigma}$ we give one well-known and important identity, which will be used very often below (see, for example, [@Ku99]).

::: lemma
[]{#lem2 label="lem2"} For all measurable functions $G:\Gamma_0\mapsto \Bbb R$ and $H: \Gamma_0\times\Gamma_0\mapsto \Bbb R$, for which $G(\xi\cup\gamma)H(\xi,\gamma)\in L^1(\Gamma_0\times\Gamma_0, \lambda_{\sigma}\otimes\lambda_\sigma)$, the following equality is true: $$\label{EgLem2}
\int_{\Gamma_0}G(\gamma)\sum_{\xi\subseteq\gamma}H(\xi,\gamma\setminus\xi)\lambda_\sigma(d\gamma)=\int_{\Gamma_0}\int_{\Gamma_0}G(\xi\cup\gamma)H(\xi,\gamma)\lambda_{\sigma}(d\gamma)\lambda_\sigma(d\xi).$$
:::

*Proof*. Let $\xi\restriction\Gamma_0^{(k)}=\{x_1,...,x_k\}:=\{x\}_1^k$, $\gamma\restriction\Gamma_0^{(m)}=\{x_{k+1},...,x_{k+m}\}:=\{x\}_{k+1}^{k+m}$. Then $$\begin{aligned}
&\int_{\Gamma_0}\int_{\Gamma_0}G(\xi\cup\gamma)H(\xi,\gamma)\lambda_{\sigma}(d\gamma)\lambda_\sigma(d\xi)=\\
&=\sum_{k,m=0}^\infty\frac{1}{k!m!}\int_{\Bbb R^{dk}}\int_{\Bbb R^{dm}}
G(\{x\}_1^{k+m})H(\{x\}_1^k,\{x\}_{k+1}^{k+m})\sigma(dx)^{k+m}=\\
&=\sum_{n=0}^\infty\frac{1}{n!}\sum_{k=0}^n {n \choose k}\int_{\Bbb R^{dn}}
G(\{x\}_1^{n})H(\{x\}_1^k,\{x\}_{k+1}^{n})\sigma(dx)^{n}=\\
&=\int_{\Gamma_0}G(\gamma)\sum_{\xi\subseteq\gamma}H(\xi,\gamma\setminus\eta)\lambda_\sigma(d\gamma).
\end{aligned}$$ $\blacksquare$

Note that the introduction of the measure [\[IL-P\]](#IL-P){reference-type="eqref" reference="IL-P"} and the application of the lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} greatly simplifies the calculations of many combinatorial statements.
