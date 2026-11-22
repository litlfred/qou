---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-002-invariants-of-volume-preserving-flows-helicities
section_title: "Invariants of volume preserving flows. Helicities."
section_number: null
pages: 10-11
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.992
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
[]{#sec:invariants-flows label="sec:invariants-flows"}

Given finitely many volume preserving vector fields $B_1$, $B_2$, $\ldots B_k\in \text{\rm SVect}(M)$ on $M=S^3$ or a homology 3-sphere one seeks quantities $\mathsf{I}(B_1,B_2,\ldots,B_k)$ invariant under the action of volumorphisms isotopic to the identity $g\in \text{\rm SDiff}_0(M)$, commonly known as *helicities* or *higher helicities*: $$\begin{gathered}
\label{eq:invariants}
 \mathsf{I}(B_1,B_2,\ldots,B_k)=\mathsf{I}(g_\ast B_1,g_\ast B_2,\ldots,g_\ast B_k),\qquad\quad \text{for all }g\in \text{\rm SDiff}_0(M), 
\end{gathered}$$ where $g_\ast$ is a push-forward by a diffeomorphism $g$. To distinguish the case of a single vector field $B$ (i.e. $B=B_1=\ldots=B_k$) we often refer to $\mathsf{I}(B)=\mathsf{I}(B,B,\ldots,B)$ as *self helicity*. We elucidated in the introduction a fundamental example of such invariant is the ordinary helicity $\mathsf{H}(B_1,B_2)$ of a pair of vector fields. In the remaining part of this section we review well known formulations of the helicity, which will later help us to point out analogies to the proposed formulation of the 3rd order helicity. Let $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ represent two invariant subdomains (not necessarily disjoint) under flows of $B_1$ and $B_2$ in $S^3$ and let $$\mathcal{T}=\mathcal{T}_1\times\mathcal{T}_2\subset \text{\rm Conf}_2(M)\subset M\times M.$$ Recall that the formula for $\mathsf{H}(B_1,B_2)$, from [@Khesin05; @Vogel03], specialized to invariant subdomains $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ may be expressed as $$\label{eq:helicity}
 \mathsf{H}_{12}(B_1,B_2)=\int_{\mathcal{T}_1\times\mathcal{T}_2} \omega\wedge\iota_{B_1}\mu\wedge\iota_{B_2}\mu,$$ where $\omega$ is known as the linking form on $M\times M$. When $\mathcal{T}=M\times M$ this formula is equivalent to a more commonly known expression: $\mathsf{H}(B_1,B_2)=\int_M \iota_{B_1}\mu\wedge d^{-1}(\iota_{B_2}\mu)$ (because $\omega$ also represents the integral kernel of $d^{-1}$). Philosophically, $\mathsf{H}(B_1,B_2)$ can be derived (c.f. [@Arnold86]) from the linking number of a pair of closed curves, which is expressed by Arnold's Helicity Theorem. For orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$ of $B_1$ and $B_2$ through $x, y\in M$, we introduce the following notation for the long pieces of closed up orbits $$\label{eq:orbits}
\begin{split}
 \mathscr{O}^{B_i}_T(x) & =  \{\Phi^i_t(x)\ |\ 0\leq t\leq T\}\subset \mathscr{O}^i(x),\qquad i=1,2\\
 \bar{\mathscr{O}}^i_T(x) & :=  \mathscr{O}^i_T(x)\cup \sigma(x,\Phi^i(x,T)).
\end{split}$$ where $\sigma(x,y)$ denotes a short path, [@Vogel03], connecting $x$ and $y$ in $M$ (see Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}). Paraphrasing [@Arnold86] we state (for the proof also see [@Vogel03]),

::: theorem
Given $B_1, B_2\in\text{\rm SVect}(M)$, The following limit exists almost everywhere on $M\times M$: $$\begin{gathered}
\label{eq:linking-function}
  \bar{m}_{B_1 B_2}(x,y)=\lim_{T\to \infty} \frac{1}{T^2}\, \text{lk}(\bar{\mathscr{O}}^1_T(x)\times\bar{\mathscr{O}}^2_T(y))\ .
 
\end{gathered}$$ Moreover, $\bar{m}_{B_1 B_2}$ is in $L^1(M\times M)$, and $$\label{eq:helicity-asymp}
 \mathsf{H}_{12}(B_1,B_2)=\int_{M\times M} \bar{m}_{B_1 B_2}(x,y)\, \mu(x)\wedge\mu(y)\ .$$
:::

The function $\bar{m}_{B_1 B_2}$ represents an asymptotic linking number of orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$, and the identity [\[eq:helicity-asymp\]](#eq:helicity-asymp){reference-type="eqref" reference="eq:helicity-asymp"} tells us that the helicity $\mathsf{H}_{12}(B_1,B_2)$ is equal to the average asymptotic linking number. In coming paragraphs, we will demonstrate, how this philosophy is applied to obtain the asymptotic $\bar{\mu}_{123}$-invariant for 3-component links and the third order helicity.
