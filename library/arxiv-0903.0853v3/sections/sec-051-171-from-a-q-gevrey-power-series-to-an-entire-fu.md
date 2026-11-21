---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-051-171-from-a-q-gevrey-power-series-to-an-entire-fu
section_title: "From a $q$-Gevrey power series to an entire function"
section_number: 17.1
pages: 89-92
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.879
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:qGevreytoentire label="subsection:qGevreytoentire"}

As before, let $\Lambda = \sum\limits_{1\le i\le m}\nu_i[\lambda_i]$ be a divisor and let $\theta_\Lambda$ be the associated theta function given by the relation [\[eqn:thetalambda\]](#eqn:thetalambda){reference-type="eqref" reference="eqn:thetalambda"}.

::: lemm
[]{#lemm:thetatronque label="lemm:thetatronque"} Consider the Laurent series expansion $\sum\limits_{n\in{\mathbf Z}} \beta_n~z^n$ of $\theta_\Lambda$.

1.  For all $(k, r) \in {\mathbf Z}^2$, one has: $$\label{eqn:beta}
    \beta_{k\nu+r} = \left(\frac L{q^r}\right)^k~q^{-k(k+1)\nu/2}~\beta_r~.$$ (The constant $L$ is defined at the beginning of the proof.)

2.  For all $n \in {\mathbf Z}$, write $T_n$ the function defined by: $$T_n: = \theta_{\Lambda,n}(z) = \sum_{\ell\le n} \beta_\ell~z^\ell~.$$ If $j\in\{1,\ldots,m\}$, one has: $$\label{eqn:thetatronque}
     K_{n,j} := \sup_{z\in[\lambda_j]} \left |z^{-n}~T_n(z) \right |< +\infty~.$$
:::

::: proof
*Proof.* From the fundamental relation $\theta(qz) = qz\theta(z)$, one draws: $$\theta_\Lambda(qz) = L~z^\nu~\theta_\Lambda(z),\quad
L := \prod_{j=1}^m\left(-\dfrac{q}{\lambda_j}\right)^{\nu_j}~,$$ whence, for all $k \in {\mathbf Z}$: $$\theta_\Lambda(q^kz) = L^k~z^{k\nu}~q^{k(k-1)\nu/2}~\theta_\Lambda(z)~.$$ The relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"} follows immediately.

Since $z^{-n}~T_n(z)$ represents an analytic function over ${\mathbf C}^* \cup \{\infty\}$, one obtains [\[eqn:thetatronque\]](#eqn:thetatronque){reference-type="eqref" reference="eqn:thetatronque"} by noticing that, if $z \in [\lambda_j]$, then: $$T_n(z) = -\sum_{\ell>n}\beta_\ell~z^\ell~,$$ which implies that $z^{-n}~T_n(z)$ tends to zero as $z$ tends $0$ along the half-spiral $\lambda_i q^{-{\mathbf N}}$. ◻
:::

Consider a $q$-Gevrey series $\hat f = \sum\limits_{n\ge 0} a_n z^n \in {{\mathbf C}[[z]]}_{q;1/\nu}$ with order $1/\nu$ and, for all $\ell \in {\mathbf Z}$, put $c_\ell := \sum\limits_{n\ge 0}a_n\beta_{\ell-n}$. Set $\ell := k \nu + r$ with $k \in {\mathbf Z}$ and $r \in {\mathbf Z}$, and write: $$c_\ell = \sum_{j=0}^{\nu - 1} \sum_{m \ge 0} a_{m \nu + j}\,\beta_{(k-m)\nu+(r-j)}.$$ As we shall see now, the above infinie series converges when the integer $-\ell$ is large enough. Indeed, using relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"}, one gets: $$\beta_{(k-m)\nu+(r-j)} = (Lq^{-r})^{k} \, q^{-k(k+1)\nu/2}\,q^{kj} \,
\left(\frac{q^{r-j+k\nu}}L\right)^m \, q^{-m(m-1)\nu/2}.$$ Since $\hat f$ has $q$-Gevrey order $1/\nu$, there exists $C_1 > 0$, $A_1 > 0$ such that $|a_n| \le C_1\,A_1^n\,|q|^{n(n-1)/(2\nu)}$ for all $n\in{\mathbf N}$. One has: $$\begin{aligned}
\left |a_{m\nu+j}\,\beta_{(k-m)\nu+(r-j)} \right |&\leq \\
C_1 (|L||q|^{-r})^{k} \, & |q|^{-k(k+1)\nu/2} \, (|q|^k A_1)^{j} \,
|q|^{j(j-1)/(2\nu)} \left(\frac{|q|^{r+k\nu+(\nu-1)/2}}{|L|A_1^{-\nu}}\right)^m\,.
\end{aligned}$$ Therefore, if we set: $$C_2 := \sum_{j=0}^{\nu-1} A_1^{j} |q|^{j(j-1)/(2\nu)},$$ then we find ($\ell = k \nu + r$): $$|c_\ell| \leq C_1\,C_2\,(|Lq^{-r}|)^k\,|q|^{-k(k-1)\nu/2}
\sum_{m\geq 0} \left(\frac{|q|^{\ell+(\nu-1)/2}}{|L|A_1^{-\nu}}\right)^m\,.$$ It is easy to see that the last series converges if $|q|^{\ell+(\nu-1)/2} < |L| A_1^{-\nu}$; moreover, when $\ell\to-\infty$, the sequence $(c_\ell)$ is $q$-Gevrey of level $(-\nu)$.

::: prop
[]{#prop:ftheta label="prop:ftheta"} Let $\hat f := \sum\limits_{n\ge 0} a_nz^n \in {{\mathbf C}[[z]]}_{q;1/\nu}$ and let $N_0$ be a negative integer such that any series defining $c_\ell$ converges for $\ell \leq N_0$. Let $F(z) := \sum\limits_{\ell\le N_0}c_\ell z^\ell$. Then, $F\in E_0^\Lambda$.
:::

::: proof
*Proof.* Since $(c_\ell)$ is a $q$-Gevrey sequence of order $(-1/\nu)$ for $\ell \to -\infty$, the sum $F$ represents an analytic function in ${\mathbf C}^* \cup \{\infty\}$, with $q$-exponential growth of order $\nu$ at zero.

We are left to estimate $F(z)$ and its derivatives along the spirals $[\lambda_j]$ belonging to the divisor $\Lambda$. Taking in account relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"}, one has: $$T_{-n-k\nu}(z) = (Lz^\nu)^{-k}~q^{-k(k-1)\nu/2}~T_{-n}(q^kz).$$ Therefore, when $z\in [\lambda_j]$, relation [\[eqn:thetatronque\]](#eqn:thetatronque){reference-type="eqref" reference="eqn:thetatronque"} allows writing $F(z)$ in the following form: $$F(z) = \sum_{k\ge
  0}\sum_{n=0}^{\nu-1}a_{k\nu+n}~z^{k\nu+n}~T_{N_0-k\nu-n}(z),$$ and also: $$\label{eqn:FT}
F(z) = \sum_{n=0}^{\nu-1}z^n\sum_{k\ge 0}L^{-k}a_{k\nu+n}~q^{-k(k-1)\nu/2}~T_{N_0-n}(q^kz).$$ One deduces that $F$ has moderate growth when $z \to 0$ along spirals $[\lambda_j]$ belonging to the divisor $\Lambda$.

As for the derivatives $F^{(\ell)}$, along each spiral $[\lambda_j]$, with $\ell<\nu_j$, one may proceed all the same: the function $T_{n}^{(\ell)}$ is indeed bounded over $[\lambda_j]$ for all $\ell < \nu_j$ and one checks that relation [\[eqn:FT\]](#eqn:FT){reference-type="eqref" reference="eqn:FT"} remains true up to order $\ell$, that is, if $z\in[\lambda_j]$: $$F^{(\ell)}(z) =
\sum_{n=0}^{\nu-1} \sum_{k\ge 0}
L^{-k}a_{k\nu+n}~q^{-k(k-1)\nu/2}~\bigl[z^n~T_{N_0-n}(q^kz)\bigr]^{(\ell)}.$$ ◻
:::
