---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-052-1241-divisibility-in-the-ring-zqh
section_title: "Divisibility in the ring $\Zqh$"
section_number: 12.4.1
pages: 43-44
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.625
latex_coverage_ratio: 0.957
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:divis-ring-zqh label="sec:divis-ring-zqh"}

Here, we make some basic observations about divisibility for elements of $\Zqh$ by products of powers of cyclotomic polynomials, which we will freely use in the rest of this section.

::: lemma
[]{#r66 label="r66"} Let $f(q)\in \Zqh$, $\zeta \in \calZ$, $n=\ord\zeta$, and $k\ge 0$. Then the following conditions are equivalent.

1.  []{#item:9 label="item:9"} $f(q)$ is divisible by $\Phi _n(q)^k$ in $\Zqh$.

2.  []{#item:10 label="item:10"} $f(q)$ is divisible by $(q-\zeta )^k$ in $\Zqh\otimes _\modZ \modZ [\zeta ]$.

3.  []{#item:11 label="item:11"} $\frac{d^if}{dq^i}(\zeta )=0$ for $i=0,1,\ldots,k-1$.
:::

::: proof
*Proof.* It is easy to check that ([\[item:10\]](#item:10){reference-type="ref" reference="item:10"}) and ([\[item:11\]](#item:11){reference-type="ref" reference="item:11"}) are equivalent, and that ([\[item:9\]](#item:9){reference-type="ref" reference="item:9"}) implies ([\[item:10\]](#item:10){reference-type="ref" reference="item:10"}). To prove ([\[item:10\]](#item:10){reference-type="ref" reference="item:10"}) implies ([\[item:9\]](#item:9){reference-type="ref" reference="item:9"}), use the fact that $f(q)$ is divisible by $(q-\zeta ')^k$ for each $\zeta '\in \calZ$ with $\ord(\zeta ')=n$ (by Galois equivariance). The details are left to the reader. ◻
:::

Given $f(q)\in \Zqh$ with $f(q)\neq0$, let $\ord_n(f(q))\ge 0$ denote the largest integer $l$ such that $f(q)$ is divisible by $\Phi _n(q)^l$. (Existence of such integer follows from injectivity of the natural homomorphism $$\Zqh\rightarrow \varprojlim_{k}\modZ [q]/(\Phi _n(q)^k),$$ see [@H:cyclotomic Corollary 4.1].) If $f(q)=0$, then set $\ord_n(f(q))=\infty$ for all $n\in \modN$. It is not difficult to show that if $d\zzzcolon \modN \rightarrow \{0,1,\ldots \}$ is a function such that $d(n)\le \ord_n(f(q))$ for all $n\in \modN$, and such that $d(n)=0$ for all but finitely many $n\in \modN$, then $f(q)$ is divisible by $\prod_{n\in \modN }\Phi _n(q)^{d(n)}$ in $\Zqh$.

A consequence of this fact is the following.

::: proposition
[]{#r57 label="r57"} The ring $\Zqh$ is *not* a unique factorization domain.
:::

::: proof
*Proof.* One can easily check that each cyclotomic polynomial $\Phi _n(q)$, $n\in \modN$, is a prime element in $\Zqh$. (In fact, the principal ideal $(\Phi _n(q))$ in $\Zqh$ is a prime ideal.)

Let $f(q)\in \Zqh$ be as defined in the proof of Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"}. Thus, there is a sequence $1\le m_1<m_2<\cdots$ such that $f(q)\in (\Phi _{m_i}(q))\subset \Zqh$ for all $i\ge 1$, where $\{m_1,m_2,\ldots \}$ has no limit points (see the proof of Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"}). The observation above implies that $f(q)$ is divisible by $\Phi _{m_1}(q)\cdots\Phi _{m_i}(q)$ for all $i\ge 1$. Since $\Phi _{m_i}(q)$ are prime elements, it follows that $\Zqh$ is not a unique factorization domain. ◻
:::
