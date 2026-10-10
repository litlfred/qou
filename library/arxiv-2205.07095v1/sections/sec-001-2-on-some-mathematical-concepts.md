---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko"
section_id: sec-001-2-on-some-mathematical-concepts
section_title: "On some mathematical concepts"
section_number: 2
pages: 3-4
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
text_source: latex
latex_prose_ratio: 0.787
latex_coverage_ratio: 1.0
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical"
---
## Configuration spaces and Lebesgue-Poisson measure.

Let $\sigma$ be a Lebesgue measure in $\Bbb R^d$. *Configuration space* $\Gamma\;: = \; \Gamma_{\Bbb R^d}$ consists of all locally finite subsets of the space $\Bbb R^d$. This definition is quite natural from the point of view of physics, because an infinite number of particles cannot be in a bounded volume.

Denote the set of all finite configurations of the space $\Gamma$ by $\Gamma_0$, and by $\Gamma^{(n)}$ configuration space with a fixed number of points.

If all such configurations are in some bounded set $\Lambda\subset\Bbb R^d$, then the corresponding space will be $\Gamma^{(n)}_\Lambda$.

State of an ideal gas in equilibrium statistical mechanics is described by the *Poisson* measure $\pi_{z \sigma}$ on configuration space $\Gamma$, where $z> 0$ is the activity (physical parameter that associated with the density of particles in the system).

But we need so-called Lebesgue-Poisson measure, i.e. the Poisson measure on the space of finite configurations, which in some sense is absolutely continuous with respect to the Lebesgue measure in contrast to the $\pi_{\sigma}$ measure for $\Gamma$. Integral for Lebesgue-Poisson measure in space $\Gamma_0$ (or $\Gamma_\Lambda$) is determined by the formula: $$\begin{align}
\label{IL-P}
\int_{\Gamma_X}F(\gamma)\lambda_{z\sigma}(d\gamma)\;&:=\;\sum_{n=0}^\infty\frac{z^n}{n!}\int_X\cdots\int_X
F(\{x_1,...,x_n\})\sigma(dx_1)\cdots\sigma(dx_n)=\notag\\
&=\sum_{n=0}^\infty\frac{z^n}{n!}\int_X\cdots\int_X
F_n(x_1,...,x_n)dx_1\cdots dx_n,
\end{align}$$ for all measurable functions $F = \{F_n \}_{n \geq 0}$, $F_n \in L^{1}(X^n)$, and $\Gamma_X \in \{\Gamma_0, \Gamma_\Lambda$). Such measure not only simplifies the recording of cumbersome expressions and combinatorial proofs, but also allows to get some new results based on properties infinite divisibility (see, for example, [@Re93; @ReSh97; @Re98; @PR07].

In the language of integrals with the measure $\lambda_{z\sigma}$ we give one well-known and important identity, which will be used very often below (see, for example, [@Ku99]).

::: lemma
[]{#lem2 label="lem2"} For all measurable functions $G:\Gamma_0\mapsto \Bbb R$ and $H: \Gamma_0\times\Gamma_0\mapsto \Bbb R$, for which $G(\xi\cup\gamma)H(\xi,\gamma)\in L^1(\Gamma_0\times\Gamma_0, \lambda_{\sigma}\otimes\lambda_\sigma)$, the following equality is true: $$\begin{equation}
\label{EgLem2}
\int_{\Gamma_0}G(\gamma)\sum_{\xi\subseteq\gamma}H(\xi,\gamma\setminus\xi)\lambda_\sigma(d\gamma)=\int_{\Gamma_0}\int_{\Gamma_0}G(\xi\cup\gamma)H(\xi,\gamma)\lambda_{\sigma}(d\gamma)\lambda_\sigma(d\xi).
\end{equation}$$
:::

*Proof*. Let $\xi\restriction\Gamma_0^{(k)}=\{x_1,...,x_k\}:=\{x\}_1^k$, $\gamma\restriction\Gamma_0^{(m)}=\{x_{k+1},...,x_{k+m}\}:=\{x\}_{k+1}^{k+m}$. Then $$\begin{align*}
&\int_{\Gamma_0}\int_{\Gamma_0}G(\xi\cup\gamma)H(\xi,\gamma)\lambda_{\sigma}(d\gamma)\lambda_\sigma(d\xi)=\\
&=\sum_{k,m=0}^\infty\frac{1}{k!m!}\int_{\Bbb R^{dk}}\int_{\Bbb R^{dm}}
G(\{x\}_1^{k+m})H(\{x\}_1^k,\{x\}_{k+1}^{k+m})\sigma(dx)^{k+m}=\\
&=\sum_{n=0}^\infty\frac{1}{n!}\sum_{k=0}^n {n \choose k}\int_{\Bbb R^{dn}}
G(\{x\}_1^{n})H(\{x\}_1^k,\{x\}_{k+1}^{n})\sigma(dx)^{n}=\\
&=\int_{\Gamma_0}G(\gamma)\sum_{\xi\subseteq\gamma}H(\xi,\gamma\setminus\eta)\lambda_\sigma(d\gamma).
\end{align*}$$ $\blacksquare$

Note that the introduction of the measure [\[IL-P\]](#IL-P){reference-type="eqref" reference="IL-P"} and the application of the lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} greatly simplifies the calculations of many combinatorial statements.

## Algebra of generating functionals.

For any function $\psi\in C_0(\Gamma_0)$ define *generating functional* : $$\begin{align}
\label{GFf}
\widetilde{F}_\psi(j)&\;=\;\sum_{N=0}^{\infty}\frac{1}{N!}\int_{\Bbb R^{dN}}(dx)^{N}j(x_1)\cdots j(x_N)\psi(x_1,\ldots, x_N)=\notag \\
&\;=\;\int_{\Gamma_0}e(j;\gamma)\psi(\gamma)\lambda_\sigma(d\gamma),
\end{align}$$ where functional $e(j;\gamma)$ is defined by the formula $$\begin{align}
\label{I-lam4}
e(j;\gamma):=\;&\begin{cases}
 1,\;&\gamma=\emptyset,\\
  \prod_{x\in\gamma}j(x),
\;&\gamma\in\Gamma_0\setminus\{\emptyset\},
  \end{cases}
\end{align}$$

and $j\in C_0(\Bbb R^d)$ is bounded (take for simplicity $j\leq 1$), continuum, nonnegative function.

It is easy to calculate using the lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} that $$\begin{equation}
\label{odprod}
  \widetilde{F}_{\psi_1}(j)\widetilde{F}_{\psi_2}(j)\;=\;\widetilde{F}_{\psi_1*\psi_2}(j)=\int_{\Gamma_0}e(j;\gamma)(\psi_1*\psi_2)(\gamma)\lambda_\sigma(d\gamma),
\end{equation}$$ where $\psi_1*\psi_2$ is product $\psi_1$ and $\psi_2$ in commutative algebra $\mathcal{A}$, which was introduced by Ruelle (see [@Ru69], Ch. 4). Formula [\[odprod\]](#odprod){reference-type="eqref" reference="odprod"} establishes an unambiguous correspondence between the algebra of generating functionals with operation of ordinary multiplication and the algebra $\mathcal {A}$. Recall that for $\gamma=\{x_1, x_2, ... x_n\}$ $$\begin{equation}
\label{odprodRu}
(\psi_1*\psi_2)(\gamma)= \sum_{\xi\subseteq\gamma}\psi_{1}(\xi)\psi_{2}(\gamma\setminus\xi).
\end{equation}$$
