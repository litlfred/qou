---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-014-71-the-p-adics
section_title: "The p-adics"
section_number: 7.1
pages: 15-16
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.916
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
We now explain the $p$-adic variant. If the field $K$ in Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"} has a prime lying over $p$ that is split, for example, if $p$ splits completely in $K$, then $K$ embeds into $\mathbb Q_p$ and thus the set $A \subseteq \mathcal O_K$ constructed in Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"} embeds into $\mathbb Z_p$. Thus, to prove the analogue of Theorem [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"} in $\mathbb Z_p$, it suffices to prove the following variant of Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}.

::: lemma
[]{#field-existence-split-p label="field-existence-split-p"} There exists an absolute constant $C>0$ such that, for every $d$ a power of $2$, there exists a totally real number field $K$ with degree $d$ in which the prime $p$ splits completely such that $\Delta_K\leq C^d$.
:::

::: proof
*Proof.* Let $T = \{p,\infty\}$ and $S=\{3,5,7,11,13,17,19,23\}\backslash \{p\}$. Let $G_S^T(2)$ be the Galois group of the maximal pro-$2$ extension of $\mathbb Q$ unramified outside $S$ and split completely at all primes in $T$. If $G_S^T(2)$ is infinite, then for every $d$ a power of $2$ there is a number fields $K$ with degree $d$ which is totally real (since $\infty$ splits), in which $p$ splits completely, and is ramified only at primes in $S$, with Galois group of order a power of $2$. This is because an infinite pro-$2$-group has open subgroups of index every power of $2$ (because a finite $2$-group has subgroups of index every power of $2$ up to its order).

An extension of fields is called tamely ramified at a prime $p$ if the order of the inertia subgroup at $p$ of the Galois group is coprime to $p$. Since these fields $K$ have Galois group of order a power of $2$, the inertia subgroup has order a power of $2$, so because they are ramified only at odd primes, they are tamely ramified at each ramified prime. It follows by [@Ne99 III, Theorem 2.6] that $\Delta_K \leq (\prod_{q\in S} q )^d \leq C^d$ where $C= 3\cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 \cdot 23$. So it only remains to check that $G_S^T(2)$ is infinite.

Let $d(G_S^T(2))$ be the minimum number of generators and $r(G_S^T(2))$ the minimum number of relations in a presentation of $G_S^T(2)$. We can check $$d(G_S^T(2)) \geq |S|-2$$ as follows. The quadratic field $\mathbb Q( \{ \sqrt{q} \mid q \in S\})$ is split at infinity, ramified only at primes in $S$ and possibly at $2$, and has Galois group $(\mathbb Z/2)^{|S|}$. For $m$ an odd integer, the extension $\mathbb Q_2(\sqrt{m})$ depends only on $m$ mod $8$. It follows that $$\mathbb Q_2( \{ \sqrt{q} \mid q \in S\})= \mathbb Q_2( 1,\sqrt{-1}, \sqrt{5},\sqrt{-5})=\mathbb Q_2( \sqrt{-1},\sqrt{5})$$ where we have chosen one representative from each congruence class mod $8$. Since $\mathbb Q_2(\sqrt{5})$ is unramified, $\mathbb Q_2( \sqrt{-1},\sqrt{5})$ has inertia group of order $2$. Thus the inertia group at $2$ is a subgroup of order $2$ of the Galois group. Taking the quotient by this we get a field with Galois group $(\mathbb Z/2)^{|S|-1}$ that is ramified only at primes in $S$. The Frobenius element at $p$ is an element of this Galois group, and thus has order $1$ or $2$. Taking the quotient by this element, we get a field with Galois group $(\mathbb Z/2)^{|S|-2}$ or $(\mathbb Z/2)^{|S|-1}$ which in addition splits completely at $p$. Thus $(\mathbb Z/2)^{|S|-2}$ is a quotient of $G_S^T(2)$ and hence $$\label{Zp-case-1} d(G_S^T(2)) \geq |S|-2\geq 5.$$

We have $$\label{Zp-case-2} r(G_S^T(2)) \leq  d(G^T_S(2))+1$$ by [@Neukirch2008 Theorem 10.7.12], since, in the notation of [@Neukirch2008], $\chi(G_S^T(2))=1+r(G_S^T(2))-d(G_S^T(2))$ and we have $\theta=0$, $S$ does not intersect $S_p =\{p\}$, $r=1$, and $T \setminus S_\infty= \{p\}$ has cardinality $1$, so that $\chi(G_S^T(2))\leq 0+0+1+1=2$ and hence $r(G_S^T(2))-d(G_S^T(2))\leq 1$.

It follows from [\[Zp-case-1\]](#Zp-case-1){reference-type="eqref" reference="Zp-case-1"} and [\[Zp-case-2\]](#Zp-case-2){reference-type="eqref" reference="Zp-case-2"} that $$r(G_S^T(2)) <  \frac{d(G^T_S(2))^2}{4}$$ and hence by the Golod-Shafarevich theorem [@GolodShafarevich] in its refined form due to Gaschütz and Vinberg [@Vinberg1965; @Koch1969], $G_S^T(2)$ is infinite, as desired. ◻
:::
