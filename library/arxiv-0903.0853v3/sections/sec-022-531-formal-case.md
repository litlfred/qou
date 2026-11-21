---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-022-531-formal-case
section_title: "Formal case"
section_number: 5.3.1
pages: 26-27
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.83
latex_coverage_ratio: 0.962
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
Any $q$-difference operator $P$ over ${{\mathbf C}((z))}$ admits, for all $\mu \in S(P)$, a factorisation $P = Q R$ with $S(Q) = \{\mu\}$ and $S(R) = S(P) \setminus \{\mu\}$. As a consequence, writing $M_{(\mu)}$ []{#not22 label="not22"} the biggest pure submodule of slope $\mu$ of $M$, one has $\text{rk~}M_{(\mu)} = r_{M}(\mu)$ and $S(M/M_{(\mu)}) = S(M) \setminus \{\mu\}$. Moreover, all modules are pure: $$M = \bigoplus_{\mu \in S(M)} M_{(\mu)}.$$ The above splitting is canonical, functorial (preserved by morphisms) and compatible with all tensor operations (tensor product, internal Hom, dual).

### Analytic case

Here, from old results due (independantly) to Adams and to Birkhoff and Guenther, one draws that, if $\mu := \min S(P)$ is the smallest slope, then $P$ admits, a factorisation $P = Q R$ with $S(Q) = \{\mu\}$ and $S(R) = S(P) \setminus \{\mu\}$. As a consequence, the biggest pure submodule of slope $\mu$ of $M$, call it $M'$, again satisfies $\text{rk~}M' = r_{M}(\mu)$, so that $S(M/M') = S(M) \setminus \{\mu\}$.

[]{#not23 label="not23"}

::: theo
[]{#theo:slopefiltration label="theo:slopefiltration"} (i) Each $q$-difference module $M$ over ${{\mathbf C}(\{z\})}$ admits a unique filtration with pure isoclinic quotients. It is an ascending filtration $(M_{\leq \mu})$ characterized by the following properties: $$S(M_{\leq \mu}) = S(M) \cap \left]- \infty,\mu\right] \text{~and~}
S(M/M_{\leq \mu}) = S(M) \cap \left]\mu,+\infty\right[.$$ (ii) This filtration is strictly functorial, *i.e.* all morphisms are strict (see explanation after the "proof").\
(iii) Writing $M_{< \mu} := \bigcup_{\mu' < \mu} M_{\leq \mu'}$ and $M_{(\mu)} := M_{\leq \mu}/M_{< \mu}$ (which is pure isoclinic of slope $\mu$ and rank $r_{M}(\mu)$), the functor: $$M \leadsto {\text{gr}}\ M := \bigoplus_{\mu \in S(M)} M_{(\mu)}$$ is exact, ${\mathbf C}$-linear, faithful and $\otimes$-compatible.
:::

::: proof
*Proof.* See [@JSFIL 3.2,3.3]. ◻
:::

Note that assertion (ii) says two things. First, a morphism $f: M \rightarrow N$ of $q$-difference modules automatically respects the canonical filtration, *i.e.* $f(M_{\leq \mu}) \subset N_{\leq \mu}$ for all $\mu$. This implies in particular that $f$ induces morphisms of $q$-difference modules $M_{(\mu)} \rightarrow N_{(\mu)}$, so that $M \leadsto {\text{gr}}M$ is indeed a functor.\
Second, recall from [@ALM p. II.2] that a morphism $f: M \rightarrow N$ is said to be *strict* with respect to the filtrations $(M_{\leq \mu})$, $(N_{\leq \mu})$, if $f(M_{\leq \mu}) = N_{\leq \mu} \cap f(M)$ for all $\mu$; equivalently: the two filtrations on $f(M)$ respectively induced by that of $N$ (by restriction) and by that of $M$ (through $f$) are identical. it is then a classical consequence (and a nice exercice in linear algebra) that the functor $M \leadsto {\text{gr}}M$ is indeed exact.
