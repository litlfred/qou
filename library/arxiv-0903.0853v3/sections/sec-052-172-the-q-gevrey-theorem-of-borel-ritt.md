---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-052-172-the-q-gevrey-theorem-of-borel-ritt
section_title: "The $q$-Gevrey theorem of Borel-Ritt"
section_number: 17.2
pages: 92-94
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.95
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:qGevreyBorelRitt label="subsection:qGevreyBorelRitt"}

The main result of this paragraph is the following[^1].

::: theo
[]{#theo:BorelRitt label="theo:BorelRitt"} The mapping $J$ sending an element $f$ to its asymptotic expansion is a surjective linear map from the ${\mathbf C}$-vector space ${\mathbb A}_{q}^{\Lambda}$ to the ${\mathbf C}$-vector space ${{\mathbf C}[[z]]}_{q;1/\nu}$.
:::

::: proof
*Proof.* Let $\hat f = \sum\limits_{n\ge 0}a_nz^n$ be a $q$-Gevrey series of order $1/\nu$ and let $F$ be the function defined in proposition [\[prop:ftheta\]](#prop:ftheta){reference-type="ref" reference="prop:ftheta"}. Maybe at the cost of taking a smaller $N_0$, we may assume that formula [\[eqn:FT\]](#eqn:FT){reference-type="eqref" reference="eqn:FT"} remains true for all $z \in {\mathbf C}^*$; this being granted, one has: $$\label{eqn:FTa}
F(z) = \sum_{\ell\ge 0}a_\ell~z^\ell~T_{N_0-\ell}(z)~.$$ Put $f := \dfrac{F}{\theta_\Lambda}$, so that $f \in {\mathbb A}_{q}^{\Lambda}$, after theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}. We are going to prove that $f$ admits $\hat f$ as an asymptotic expansion. To that aim, it is enough to show that, if $\lambda \notin \Lambda$, one has: $$\label{eqn:fell}
\lim_{n\to+\infty}f^{(\ell)}(\lambda q^{-n}) = \ell!~a_\ell$$ for any integer $\ell \geq 0$.

Since $\left |T_{N_0-n}(z) \right |\leq e_\Lambda(z)$ and $\left |\theta_\Lambda(z) \right |\sim e_\Lambda(z)$ (see lemma [\[lemm:thetamin\]](#lemm:thetamin){reference-type="ref" reference="lemm:thetamin"}), relation [\[eqn:FTa\]](#eqn:FTa){reference-type="eqref" reference="eqn:FTa"} immediately leads us to the limit [\[eqn:fell\]](#eqn:fell){reference-type="eqref" reference="eqn:fell"} for $\ell =0$. If $\ell \geq
1$, one has: $$f^{(\ell)}(z) = \sum_{n\ge 0} \sum_{j=0}^\ell 
a_n~\binom nj~\frac{j!}{(\ell-j)!}~z^{n-j}~
\left[\dfrac{T_{N_0-n}(z)}{\theta_\Lambda(z)}\right]^{(\ell-j)}~.$$ Through direct estimates, one gets the limit [\[eqn:fell\]](#eqn:fell){reference-type="eqref" reference="eqn:fell"} (omitted details are left to the reader). ◻
:::

The theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"} can also be interpreted with help of interpolation of a $q$-Gevrey sequence by entire functions at points in a geometric progression. Indeed, if $f \in {\mathbb A}_q^\Lambda$ is asymptotic to the $q$-Gevrey series $\sum\limits_{k\ge  0}a_kz^k$ of level $\nu$, then, from the decomposition [\[eqn:fLambda\]](#eqn:fLambda){reference-type="eqref" reference="eqn:fLambda"}, one draws: $$a_k = \sum_{n\ge N_0}\sum_{1\le i\le m}\sum_{0\le j<\nu_i}(-1)^{j+1}~
\binom{k+j}j~\dfrac{\alpha_{i,j,n}}{(\lambda_iq^{-n})^{k+j+1}}+h_k~,$$ where $h_k$ denotes the coefficient of $z^k$ in the Taylor series of $h$. Put: $$f_{i,j}(z) := \sum_{n\ge N_0}\alpha_{i,j,n}~z^n~;$$ then: $$\label{eqn:afij}
a_k = \sum_{1\le i\le m}\sum_{0\le j<\nu_i}
\binom{k+j}j~\dfrac{(-1)^{j+1}}{\lambda_i^{k+j+1}}~f_{i,j}(q^{k+j+1})+h_k~.$$

::: coro
[]{#coro:interpol label="coro:interpol"} Let $(a_n)$ be a $q$-Gevrey sequence of order $\nu$ and let $\Lambda = \sum\limits_{1\le i\le m}\nu_i[\lambda_i]$ be a divisor of degree $\nu := \nu_1 + \cdots + \nu_m$. Then, there exists $\nu$ entire functions $A_{i,j}$, $1 \leq i \leq m$, $0 \leq j < \nu_i$ satisfying the following properties:

1.  Each function $A_{i,j}$ has $q$-exponential growth of order (at most) $\nu$ at infinity.

2.  There exists $C>0$, $A>0$ such that, for all $n\in{\mathbf N}$: $$\label{eqn:interpol2}
    \left |a_n - 
    \sum_{1\le i\le m} \sum_{0\le j<\nu_i}
    \binom{n+j}j~\dfrac{(-1)^{j+1}}{\lambda_i^{n+j+1}}~A_{i,j}(q^{n+j+1})\right |< CA^n~.$$
:::

::: proof
*Proof.* The functions $A_{i,j}$ are defined by replacing $N_0$ by $\max(0,N_0)$ in definition [\[eqn:afij\]](#eqn:afij){reference-type="eqref" reference="eqn:afij"}; one then uses relation [\[eqn:afij\]](#eqn:afij){reference-type="eqref" reference="eqn:afij"} to get the bounds [\[eqn:interpol2\]](#eqn:interpol2){reference-type="eqref" reference="eqn:interpol2"}. ◻
:::

Note that if $\Lambda$ is solely made of simple spirals ($\nu_i = 1$), then corollary [\[coro:interpol\]](#coro:interpol){reference-type="ref" reference="coro:interpol"} spells as follows: $$\left |a_n + \sum_{1\le i\le \nu}{\lambda_i^{-n-1}}~A_{i}(q^{n+1}) \right |< C A^n~,$$ where $C>0$, $A>0$ and where the $A_i$ are $\nu$ entire functions with $q$-exponential growth of order at most $\nu$ at infinity. In other words, one can interpolate a $q$-Gevrey sequence of order $\nu$, up to a sequence with at most geometric growth, by $\nu$ entire functions on a half-spiral $\lambda q^{\mathbf N}$.

[^1]: Theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"} is proved with the help of theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}, where we gave conditions for a function to have a certain type Taylor expansion; here, we deal with the *surjectivity* of the "Taylor expansion mapping".
