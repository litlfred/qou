---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-002-12-the-ring-zqh-of-analytic-functions-on-the-set
section_title: "The ring $\Zqh$ of analytic functions on the set of roots of unity"
section_number: 1.2
pages: 2-3
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.965
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:ring-zqh-cyclotomic label="sec:ring-zqh-cyclotomic"}

The invariant $J_M$ of an integral homology sphere $M$ which we construct in the paper takes values in a completion $\Zqh$ of the polynomial ring $\modZ [q]$, which was introduced in [@H:rims2001] and studied in [@H:cyclotomic]. One of the simplest definitions of $\Zqh$ is $$\Zqh = \varprojlim_{n}\modZ [q]/((q)_n),$$ where we set $$(q)_n = (1-q)(1-q^2)\cdots(1-q^n).$$

The ring $\Zqh$ may be regarded as the ring of "analytic functions defined on the set $\calZ$ of roots of unity". This statement is justified by the following facts. (The following overlaps those in [@H:rims2001; @H:cyclotomic].)

First of all, *each element of $\Zqh$ can be evaluated at each root of unity*. That is, for each $\zeta \in \calZ$, the evaluation map $\mods _\zeta \zzzcolon \modZ [q]\rightarrow \modZ [\zeta ]$, $f(q)\mapsto f(\zeta )$, induces a (surjective) ring homomorphism $$\mods _\zeta \zzzcolon \Zqh\rightarrow \modZ [\zeta ],$$ since $\mods _\zeta ((q)_n)=0$ if $n\ge \ord(\zeta )$. It is often useful to write $f(\zeta )=\mods _\zeta (f(q))$ for $f(q)\in \Zqh$.

Second, *each element of $\Zqh$ can be regarded as a (set-theoretic) function on the set of roots of unity.* This means that each $f\in \Zqh$ is determined uniquely by the values $\mods _\zeta (f)\in \modZ [\zeta ]$ for all $\zeta \in \calZ$, or, equivalently, the function $$\label{e4}
  \mods _{\calZ}\zzzcolon \Zqh\rightarrow \prod_{\zeta \in \calZ}\modZ [\zeta ],\quad
  f(q)\mapsto (f(\zeta ))_{\zeta \in \calZ}.$$ is injective [@H:cyclotomic Theorem 6.3]. Here, in a natural way, $\prod_{\zeta \in \calZ}\modZ [\zeta ]$ can be regarded as a subring of the ring of $\C$-valued functions on $\calZ$.

Third, *each element of $\Zqh$ has a power series expansion in $q-\zeta$ for each root of unity, and any such power series determines $\Zqh$.* In fact, for each $\zeta \in \calZ$, the inclusion $\modZ [q]\subset \modZ [\zeta ][q]$ induces a ring homomorphism $$\label{e6}
  \iota _\zeta \zzzcolon \Zqh\rightarrow \modZ [\zeta ][[q-\zeta ]],$$ since, for each $i\ge 0$, $(q)_n$ is divisible by $(q-\zeta )^i$ in $\modZ [\zeta ][q]$ if $n\ge i\ord(\zeta )$. Since $\iota _\zeta$ is injective [@H:cyclotomic Theorem 5.2], each $f\in \Zqh$ is determined by the power series $\iota _\zeta (f)$. $\iota _\zeta (f)$ may be regarded as the Taylor expansion of $f$, see Section [\[sec:power-seri-expans-1\]](#sec:power-seri-expans-1){reference-type="ref" reference="sec:power-seri-expans-1"}.

Fourth, *each element of $\Zqh$ is completely determined by its values on a subset $\calZ'\subset \calZ$ if $\calZ'$ has a limit point. Otherwise, not completely.* To explain what this means, we introduce a topology on the set $\calZ$, which is different from the usual one induced by the topology of $\C$. Two elements $\zeta ,\xi \in \calZ$ are said to be *adjacent* if $\zeta \xi ^{-1}$ is of prime power order, or, equivalently, if $\zeta -\xi$ is not a unit in $\modZ [\zeta ,\xi ]$. A subset $\calZ'\subset \calZ$ is defined to be *open* if, for each $\zeta \in \calZ'$, all but finitely many elements adjacent to $\zeta$ is contained in $\calZ'$. In this topology, an element $\xi \in \calZ$ is a limit point of a subset $\calZ'\subset \calZ$ (i.e., $(U\setminus \{\xi \})\cap \calZ'\neq\emptyset$ for all neighborhood $U$ of $\xi$) if and only if there are infinitely many $\zeta \in \calZ'$ adjacent to $\xi$. We have the following.

::: proposition
[]{#r85 label="r85"} If $\calZ'\subset \calZ$ has a limit point, then the ring homomorphism $$\label{e61}
    \mods _{\calZ'}\zzzcolon \Zqh\rightarrow \prod_{\zeta \in \calZ'}\modZ [\zeta ],\quad
    f(q)\mapsto (f(\zeta ))_{\zeta \in \calZ},$$ is injective.
:::

If $\calZ'\subset \calZ$ has no limit point, then $\mods _{\calZ'}$ is not injective, i.e., there is a non-zero "analytic function" $f\in \Zqh$ vanishing on $\calZ'$, see Proposition [\[r56\]](#r56){reference-type="ref" reference="r56"}.

The above-explained properties of $\Zqh$ are closely related to the integrality of $\Zqh$. In fact, the completion $\Qqh =
\varprojlim_{n}\modQ [q]/((q)_n)$ does not behave like $\Zqh$, see [@H:cyclotomic Section 7.5].
