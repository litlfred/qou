---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-008-22-link-with-representation-of-the-hecke-algebra
section_title: "Link with representation of the Hecke algebras"
section_number: 2.2
pages: 7-7
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.976
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:qPlancherel_trace label="subsect:qPlancherel_trace"} The $q$-Plancherel measure appears naturally in the abstract harmonic analysis of the Iwahori-Hecke algebras $\mathscr{H}_{n,q}$. Recall that if $n \in \mathbb{N}$ and $q$ is a complex parameter, then $\mathscr{H}_{n,q}$ is the complex associative algebra with generators $T_1,T_2,\ldots,T_{n-1}$ and relations: $$\begin{aligned}
 \text{braid relations:}&\quad  \forall i,\,\,\,T_iT_{i+1}T_i=T_{i+1}T_iT_{i+1} ;\\
\text{commutation relations:}&\quad \forall\, |j-i|\geq 2,\,\,\,T_iT_j=T_jT_i ;\\
\text{quadratic relations:}&\quad  \forall i,\,\,\,(T_i-q)(T_i+1)=0.
\end{aligned}$$ We recover the symmetric group algebra $\mathbb{C}\mathfrak{S}_n$ for $q=1$. For any value of $q$, one can define an element corresponding to a permutation $\sigma \in \mathfrak{S}_n$: $$T_\sigma=T_{i_1}T_{i_2}\cdots T_{i_k},$$ where $\sigma=s_{i_1}s_{i_2}\cdots s_{i_k}$ is a minimal decomposition of $\sigma$ in elementary transpositions (thanks to Matsumoto's theorem, the result does not depend on which minimal decomposition we choose). It can be shown that $(T_\sigma)_{\sigma \in \mathfrak{S}_n}$ forms a linear basis of $\mathscr{H}_{n,q}$ (see for example [@Mat99] or [@GP00]). Moreover, if $q \neq 0$ is not a root of unity (in the following, we assume that we are in this case, as $q$ is a positive real number), then $\mathscr{H}_{n,q}$ is a semi-simple algebra abstractly isomorphic to $\mathbb{C}\mathfrak{S}_n$, and consequently has the same theory of representations: the irreducible $\mathscr{H}_{n,q}$-modules are parameterized by the partitions of size $n$, and each $q$-Specht module $S^\lambda(q)$ has dimension $\dim S^\lambda(q)=\dim \lambda$. We will denote by $\varsigma^\lambda(q)$ the trace of the simple module $S^\lambda(q)$, and by $\chi^{\lambda}(q)$ the *normalized* character, so that $\varsigma^\lambda(q)=(\dim \lambda)\,\chi^\lambda(q)$. Both objects are central linear forms on $\mathscr{H}_{n,q}$.

Let us consider the regular trace of the Iwahori-Hecke algebra: $$\tau_q(T_\sigma)=\begin{cases}
                  1&\text{if }\sigma=\mathrm{id},\\
                 0&\text{otherwise}.
                 \end{cases}$$ The decomposition of $\tau_q$ in the basis of normalized $q$-characters $\chi^\lambda(q)$ writes as (this corresponds to [@Stra08 equation (16)]): $$\begin{aligned}
\tau_q &= \sum_{\lambda \in \mathscr{Y}_n} M_{n,q}(\lambda)\,\chi^\lambda(q)=\sum_{\lambda\in \mathscr{Y}_n} \frac{D_\lambda(q)}{\{n!\}_q}\,\varsigma^\lambda(q). \label{eq:tau_qPlancherel}
\end{aligned}$$ Of course, this characterizes the $q$-Plancherel measure. Therefore, if we consider the $q$-characters on a fixed element $T_\sigma$ as a function of the indexing partition $\lambda$, its expectation under the $q$-Plancherel measure is $\tau_q(T_\sigma)$, that is either $0$ or $1$. Using this, we will be able to compute expectations of observables of diagrams.

::: remark
We will prove in this article that we have in fact a concentration of the $q$-characters around the regular trace and compute explicitly their fluctuations, see Corollary [\[corol:concentration_q-characters\]](#corol:concentration_q-characters){reference-type="ref" reference="corol:concentration_q-characters"} and Remark [\[RemFluctuationsQCharacters\]](#RemFluctuationsQCharacters){reference-type="ref" reference="RemFluctuationsQCharacters"}.
:::
