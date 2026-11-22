---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S 3"
section_id: sec-002-invariants-of-volume-preserving-flows-helicity
section_title: "Invariants of volume preserving flows. Helicity."
section_number: null
pages: 12-14
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.975
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
[]{#sec:invariants-flows label="sec:invariants-flows"}

Given finitely many volume preserving vector fields $X_1$, $X_2$, $\ldots X_k\in \text{Vect}^\text{vol}(M)$ on $M=S^3$ or a homology 3-sphere one seeks quantities $\mathsf{I}(X_1,X_2,\ldots,X_k)$ invariant under the action of volumorphisms isotopic to the identity $g\in \text{Diff}^\text{vol}_0(M)$, commonly known as *higher-helicities*: $$\begin{gathered}
\label{eq:invariants}
 \mathsf{I}(X_1,X_2,\ldots,X_k)=\mathsf{I}(g_\ast X_1,g_\ast X_2,\ldots,g_\ast X_k),\qquad\quad \text{for all }g\in \text{Diff}^\text{vol}_0(M), 
\end{gathered}$$ where $g_\ast$ is a push-forward by a diffeomorphism $g$. To distinguish the case of a single vector field $X$ (i.e. $X=X_1=\ldots=X_k$) we often refer to $\mathsf{I}(X)=\mathsf{I}(X_1,X_2,\ldots,X_k)$ as *self-helicity*. We elucidated in the introduction a fundamental example of such invariant is the ordinary helicity $\mathsf{H}(X_1,X_2)$ of a pair of vector fields. In the the remaining part of this section we review well known formulations of the helicity, which will later help us to point out analogies to the proposed formulation of the 3rd order helicity. Let $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ represent two invariant subdomains (not necessarily disjoint) under flows of $X_1$ and $X_2$ in $S^3$ and let $$\mathcal{T}=\mathcal{T}_1\times\mathcal{T}_2\subset \text{Conf}(M,2)\subset M\times M.$$ Recall that the formula for $\mathsf{H}(X_1,X_2)$, from [@Khesin05; @Vogel03], specialized to invariant subdomains $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ may be expressed as $$\label{eq:helicity}
 \mathsf{H}_{12}(X_1,X_2)=\int_{\mathcal{T}_1\times\mathcal{T}_2} \omega\wedge\iota_{X_1}\mu\wedge\iota_{X_2}\mu,$$ where $\omega$ is so called linking form on $M\times M$. When $\mathcal{T}=M\times M$ this formula is equivalent to a more commonly known expression: $\mathsf{H}(X_1,X_2)=\int_M \iota_{X_1}\mu\wedge d^{-1}(\iota_{X_2}\mu)$ (because $\omega$ also represents the integral kernel of $d^{-1}$).

Philosophically, $\mathsf{H}(X_1,X_2)$ can be derived (c.f. [@Arnold86]) from the linking number of a pair of closed curves, which is expressed by Arnold's Helicity Theorem. For orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$ of $X_1$ and $X_2$ through $x, y\in M$, we introduce the following notation for the long pieces of closed up orbits

$$\begin{aligned}
\label{eq:orbits}
 \mathscr{O}^i_T(x) & = & \{\Phi^i_t(x)\ |\ 0\leq t\leq T\}\subset \mathscr{O}^i(x),\qquad i=X, Y,\\
 \bar{\mathscr{O}}^i_T(x) & := & \mathscr{O}^i_T(x)\cup \sigma(x,\Phi^i(x,T)).
\end{aligned}$$ where $\sigma(x,y)$ denotes a short path, [@Vogel03], connecting $x$ and $y$ in $M$ (see Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}).

::: theorem
Given $X_1, X_2\in\text{Vect}^\text{vol}(M)$, The following limit exists almost everywhere on $M\times M$: $$\begin{gathered}
\label{eq:linking-function}
  \bar{m}_{X_1 X_2}(x,y)=\lim_{T\to \infty} \frac{1}{T^2}\, \text{lk}(\bar{\mathscr{O}}^1_T(x)\times\bar{\mathscr{O}}^2_T(y))\ .
 
\end{gathered}$$ Moreover, $\bar{m}_{X_1 X_2}$ is in $L^1(M\times M)$, and $$\label{eq:helicity-asymp}
 \mathsf{H}_{12}(X_1,X_2)=\int_{M\times M} \bar{m}_{X_1 X_2}(x,y)\, \mu(x)\wedge\mu(y)\ .$$
:::

The function $\bar{m}_{X_1 X_2}$ represents an asymptotic linking number of orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$, and the identity [\[eq:helicity-asymp\]](#eq:helicity-asymp){reference-type="eqref" reference="eq:helicity-asymp"} tells us that the helicity $\mathsf{H}_{12}(X_1,X_2)$ is equal to the average asymptotic linking number. We will demonstrate, in coming paragraphs, how this philosophy is applied to obtain the asymptotic $\bar{\mu}_{123}$-invariant for 3-component links and the third order helicity.
