---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-050-1234-relations-between-two-power-series-expansio
section_title: "Relations between two power series expansions at different roots of unity"
section_number: 12.3.4
pages: 42-43
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.932
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:relat-betw-two label="sec:relat-betw-two"}

Let $\zeta ,\xi \in \calZ$, where $\ord(\zeta /\xi )=p^e$ is a prime power. We consider how the two power series expansions $\iota _\zeta (J_M)\in \modZ [\zeta ][[q-\zeta ]]$ and $\iota _\xi (J_M)\in \modZ [\xi ][[q-\xi ]]$ are related. Note that these two formal power series rings can be regarded as subrings of $$R_{\zeta ,\xi }:=\varprojlim_{i,j}\modZ [\zeta ,\xi ][q]/((q-\zeta )^i,(q-\xi )^j)\cong
  \modZ _p[\zeta ,\xi ][[q-\zeta ]]\cong\modZ _p[\zeta ,\xi ][[q-\xi ]].$$ In $R_{\zeta ,\xi }$ we have $$\begin{split}
    \iota _\zeta (J_M)
    &=\sum_{k\ge 0}\lambda _{\zeta ,k}(q-\zeta )^k\\
    &=\sum_{k\ge 0}\lambda _{\zeta ,k}((q-\xi )+(\xi -\zeta ))^k\\
    &=\sum_{i\ge 0}\Bigl(\sum_{j\ge 0}\binom{i+j}{i}(\xi -\zeta )^j\lambda _{\zeta ,i+j}\Bigr)(q-\xi )^i\\
  \end{split}$$ Hence, we have $$\label{e65}
  \lambda _{\xi ,k}=\sum_{j\ge 0}\binom{k+j}{k}(\xi -\zeta )^j\lambda _{\zeta ,k+j}$$ for $k\ge 0$. This formula describes how the coefficients of the power series expansion at $\zeta$ determines those at $\xi$. Note that each $\lambda _{\xi ,k}$ is determined modulo a given power of $p$ by finitely many coefficients in the power series expansion at $\zeta$.

Setting $k=0$ in [\[e65\]](#e65){reference-type="eqref" reference="e65"}, we have $$\label{e66}
  \tau _\xi (M)=\sum_{j\ge 0}(\xi -\zeta )^j\lambda _{\zeta ,j}$$ Note that if $\zeta =1$ and $\ord(\xi )$ is an odd prime power, then [\[e66\]](#e66){reference-type="eqref" reference="e66"} implies that the Lawrence's $p$-adic convergence conjecture mentioned in the introduction. Thus [\[e66\]](#e66){reference-type="eqref" reference="e66"} generalizes Lawrence's conjecture.

[\[e66\]](#e66){reference-type="eqref" reference="e66"} implies the following.

::: proposition
[]{#r67 label="r67"} Let $\zeta ,\xi \in \calZ$ with $\ord(\zeta /\xi )$ a prime power. Then we have $$\tau _\zeta (M)\equiv \tau _\xi (M)\pmod{(\xi -\zeta )}$$ in $\modZ [\zeta ,\xi ]$.
:::

::: corollary
[]{#r71 label="r71"} Let $\zeta \in \calZ$ with $\ord(\zeta )=dp^e$, where $d\in \{1,2,3,4,6\}$, $e\ge 0$, and $p$ is a prime. Then we have $\tau _\zeta (M)\neq0$.
:::

::: proof
*Proof.* It is well known that we have $\tau _\xi (M)\neq\pm 1$ for $\xi \in \calZ$ with $\ord(\xi )\in \{1,2,3,4,6\}$ (see Section [\[sec:divisibility-results\]](#sec:divisibility-results){reference-type="ref" reference="sec:divisibility-results"}). This fact and Proposition [\[r67\]](#r67){reference-type="ref" reference="r67"} implies the assertion, since $(\xi -\zeta )\neq(1)$ in $\modZ [\zeta ,\xi ]$. ◻
:::

The case $d=1$ and $p$ odd in Corollary [\[r71\]](#r71){reference-type="ref" reference="r71"} follows also from Lawrence's conjecture proved by Rozansky, and presumably has been well known.

::: conjecture
[]{#r73 label="r73"} For any integral homology sphere $M$, we have $\tau _\zeta (M)\neq0$ for every root of unity $\zeta$.
:::

See Conjectures [\[r33\]](#r33){reference-type="ref" reference="r33"} and [\[r31\]](#r31){reference-type="ref" reference="r31"} for stronger statements.
