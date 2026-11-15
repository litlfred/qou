---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-006-31-quotients-of-skew-partitions
section_title: "Quotients of skew-partitions"
section_number: 3.1
pages: 9-10
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.946
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
[]{#subsec:quotients label="subsec:quotients"}

We shall define $n$-quotients and $n$-signs for the following class of skew-partitions.

::: definition
[]{#def:n_dec label="def:n_dec"} Let $m$, $n \in \mathbf{N}$. We say that a skew-partition $\lambda /\mu$ of $mn$ is *$n$-decomposable* if there exists a border-strip tableau of shape $\lambda / \mu$ and type $(n^m)$.
:::

::: definition
[]{#def:n_quo label="def:n_quo"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be an $n$-decomposable skew-partition of $mn$. Let $\Gamma(\lambda)$ be an abacus display for $\lambda$ on an $n$-runner abacus using $tn$ beads for some $t \in \mathbf{N}$. Let $\Gamma(\mu)$ be the abacus display for $\mu$ obtained by performing an appropriate sequence of $m$ upward bead moves on $\Gamma(\lambda)$.

(This is possible since $\lambda / \mu$ is $n$-decomposable.)

Let $(\lambda^{(0)}, \ldots, \lambda^{(n-1)})$ and $(\mu^{(0)}, \ldots, \mu^{(n-1)})$ be the $n$-quotients of $\lambda$ and $\mu$ corresponding to $\Gamma(\lambda)$ and $\Gamma(\mu)$, respectively. The *$n$-quotient* of $\lambda / \mu$ is defined to be $$(\lambda^{(0)} / \mu^{(0)}, \ldots, \lambda^{(n-1)} / \mu^{(n-1)}).$$ We define the $n$-*sign* of $\lambda / \mu$, denoted $\varepsilon_n(\lambda/\mu)$ to be the sign of any border-strip tableau of shape $\lambda / \mu$ and type $(n^m)$.
:::

To avoid cumbersome restatements, we adopt the convention that $\lambda^{(i)} / \mu^{(i)}$ always has the meaning of Definition [\[def:n_quo\]](#def:n_quo){reference-type="ref" reference="def:n_quo"} above. It is clear from the abacus that $\mu^{(i)}$ is a subpartition of $\lambda^{(i)}$ for each $i \in \{0,\ldots,n-1\}$, and so the $n$-quotient is well-defined. It follows from Proposition 3.13 in [@OlssonCombinatorics], or our Proposition [\[prop:nbij\]](#prop:nbij){reference-type="ref" reference="prop:nbij"} below, that the $n$-sign of a skew-partition is well defined. See §[\[subsec:example\]](#subsec:example){reference-type="ref" reference="subsec:example"} below for an example of these definitions and all the results in this section.

We remark that it appears to be impossible to define the $n$-core of an arbitrary skew-partition. The example $\lambda / \mu = (2,2) / (1)$ and $n=2$ illustrates the obstacles that arise. Representing $\lambda$ on a $2$-runner abacus as $$\begin{matrix} \circ& \circ\\ \bullet& \bullet\end{matrix}$$ we see that either bead may be moved up, giving two different skew-partitions from which no border strip of length $2$ can be removed, namely $(2) /(1)$ and $(1,1) / (1)$. The $2$-quotients corresponding to these bead moves, namely $((1),\varnothing)$ and $(\varnothing,(1))$, are also different.

::: theorem
[]{#thm:ind label="thm:ind"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Let $\alpha$ be a partition of $m$. If $\lambda / \mu$ is not $n$-decomposable then $\chi^{\lambda / \mu}(g_{n \alpha}) = 0$. If $\lambda / \mu$ is $n$-decomposable and $(\lambda^{(0)} / \mu^{(0)}, \ldots, \lambda^{(n-1)} / \mu^{(n-1)})$ is its $n$-quotient, then $$\chi^{\lambda / \mu}(g_{n\alpha}) = \varepsilon_n(\lambda / \mu)
\mathop{\mathrm{Ind}}^{S_m}_{S_{\ell_0} \times \cdots \times S_{\ell_{n-1}}}
\bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots \times 
\chi^{\lambda^{(n-1)}/ \mu^{(n-1)}} \bigr)
(g_\alpha)$$ where $|\lambda^{(i)} / \mu^{(i)}| = \ell_i$.
:::

This result, stated in the alternative language of star diagrams, was first proved in [@Farahat1954 Section 4]. The special case where $\mu$ is the $n$-core of $\lambda$ also follows from the correction by Thrall and Robinson [@ThrallRobinson1951] to Section 7 of Robinson [@Robinson1947] or, alternatively, from Littlewood's result in [@Littlewood1951 Section 2]. Farahat's proof depends on an algebraic argument using Schur functions. A character-theoretic proof is given by Kerber, Sänger, and Wagner: see [@KSW Equation 3.6]. In the remainder of this section, we give a shorter character-theoretic proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}, expressing each side of the theorem as a sum, and then constructing a bijection between the summands. An example to illustrate this bijection is given in §[\[subsec:example\]](#subsec:example){reference-type="ref" reference="subsec:example"}. (Our bijection is similar to that defined using *Brettspiele* in [@KSW].)
