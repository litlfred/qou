---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-045-122-on-determination-of-j-m-by-infinitely-many-w
section_title: "On determination of $J_M$ by infinitely many WRT invariants"
section_number: 12.2
pages: 39-40
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.963
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:determination-jm-wrt label="sec:determination-jm-wrt"}

In this subsection, we prove the following.

::: proposition
[]{#r56 label="r56"} If $\calZ'\subset \calZ$ has no limit point, then the ring homomorphism $\mods _{\calZ'}$ in [\[e61\]](#e61){reference-type="eqref" reference="e61"} is not injective.
:::

Here, recall from Section [\[sec:ring-zqh-cyclotomic\]](#sec:ring-zqh-cyclotomic){reference-type="ref" reference="sec:ring-zqh-cyclotomic"} that a "limit point" of a subset $\calZ'\subset \calZ$ is an element $\xi \in \calZ$ such that there are infinitely many $\zeta \in \calZ'$ adjacent to $\xi$. (Recall that $\xi$ and $\zeta$ are adjacent if $\ord(\zeta \xi ^{-1})$ is a prime power.) Any finite subset $\calZ'\subset \calZ$ has no limit point. There are many infinite subset $\calZ'\subset \calZ$ without limit points, for example $\{6^i\zzzvert i\ge 0\}$.

Proposition [\[r56\]](#r56){reference-type="ref" reference="r56"} shows that Conjecture 6.1 in our previous paper [@H:cyclotomic] is false. It follows that we can not prove, using only properties of $\Zqh$, that the $\tau _\zeta (M)$ for any infinitely many $\zeta \in \calZ$ would determine $J_M$ and hence $\tau (M)$. It should be remarked that it is still open whether the WRT invariants at any infinitely many roots of unity determine $J_M$ or not.

Proposition [\[r56\]](#r56){reference-type="ref" reference="r56"} follows easily from Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"} below. Two elements $m,n\in \modN$ are said to be *adjacent* to each other (written $m\Leftrightarrow n$) if $m/n=p^e$ with $p$ prime and $e\in \modZ$. For a subset $S\subset \modN$, a limit point of $S$ is defined to be an element $m\in \modN$ which is adjacent to infinitely many elements of $S$. Note that if $\zeta ,\xi \in \calZ$ are adjacent, then $\ord(\zeta )$ and $\ord(\xi )$ are adjacent. (One can define a topology on $\modN$ where $S\subset \modN$ is open if for each $m\in S$, $S$ contains all but finitely many elements adjacent to $m$. The map $\ord\zzzcolon \calZ\rightarrow \modN$, $\zeta \mapsto\ord(\zeta )$, turns out to be a continuous map.)

::: proposition
[]{#r55 label="r55"} If $S\subset \modN$ is a subset with no limit point, then the ring homomorphism $$\label{e8}
    \mods _S\zzzcolon \Zqh\rightarrow \prod_{m\in S}\modZ [q]/(\Phi _m(q)),\quad
    f(q)\mapsto (f(q)\mod(\Phi _m(q)))_{m\in S},$$ is not injective.
:::

::: proof
*Proof.* Let $S=\{m_1,m_2,\ldots \}$ with $1\le m_1<m_2<\cdots$. Choose $a\in \modN \setminus S$. We construct $f(q)\in \Zqh$ such that $f(q)\in (\Phi _{m_i}(q))$ for all $i\ge 1$ and $f(q)\not\in (\Phi _a(q))$. For this purpose, it suffices to construct a sequence $f_i(q)\in \modZ [q]$, $i\ge 1$, such that

1.  $f_i(q)\rightarrow 1$ in $\Zqh$ as $i\rightarrow \infty$ (i.e., for each $j$ there is $i$ such that $f_k(q)-1$ is divisible by $(q)_j$ for all $k\ge i$),

2.  $f_i(q)\in (\Phi _{m_i}(q))$ for $i\ge 1$,

3.  $f_i(q)\not\in (\Phi _a(q))$ for $i\ge 1$.

Suppose there is such a sequence $f_i(q)$. Set $f(q)=\prod_{i\ge 1}f_i(q)$, which is well defined by (1). By (2) we have $f(q)\in (\Phi _{m_i}(q))$ for all $i\ge 1$. (1) and (3) implies that $f(q)\not\in (\Phi _a(q))$, hence $f(q)\neq0$.

Now we show that there is a sequence $f_i(q)$ as above. For $i\ge 0$, set $$b_i=\max(\{0\}\cup \{b\in \modN \zzzvert b<m_i;\; b\not\Leftrightarrow m_j\;\text{for all $j\ge i$}\}).$$ The assumption in the statement implies:

-   $0\le b_1\le b_2\le \cdots$ and $\lim_{i}b_i=\infty$,

-   if $1\le n\le b_i$ and $i\le j$, then $m_j$ and $n$ are not adjacent.

It follows from (b) that, for $i\ge 1$, there is $u_i(q)\in \modZ [q]$ such that $(q)_{b_i}u_q(q)\equiv1\mod{(\Phi _{m_i}(q))}$. Set $$f_i(q)=
    \begin{cases}
      \Phi _{m_i}(q)& \text{if $b_i<a$}, \\
      1-(q)_{b_i}u_i(q)& \text{if $b_i\ge a$},\\
    \end{cases}$$ (2) and (3) can be easily verified. (1) follows from (a). ◻
:::

::: proof
*Proof of Proposition [\[r56\]](#r56){reference-type="ref" reference="r56"}.* Set $S=\{\ord(\zeta )\zzzvert \zeta \in \calZ'\}\subset \modN$. By assumption, $S$ has no limit point. Hence, by Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"}, $\mods _S$ is not injective. It follows that $\mods _{\calZ'}$ is not injective, since it factors through $\mods _S$. ◻
:::

::: remark
[]{#r43 label="r43"} By slightly modifying the definition of $f_i(q)$ in the proof of Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"}, we see that if $S\subset \modN$ has no limit point and if $d\zzzcolon S\rightarrow \{0,1,\ldots \}$ is any function, then the ring homomorphism $$g_{S,d}\zzzcolon \Zqh\rightarrow \prod_{m\in S}\modZ [q]/(\Phi _m(q)^{d(m)}),\quad
    f(q)\mapsto (f(q)\mod(\Phi _m(q)^{d(m)}))_{m\in S},$$ is not injective. (It suffices to replace $f_i(q)$ with the $d(m_i)$th power of the original definition of $f_i(q)$.) Using this, one can show that if $\calZ'\subset \calZ$ has no limit point and if $d\zzzcolon \calZ'\rightarrow \{0,1,\ldots \}$ is any function, then the ring homomorphism $$g_{\calZ',d}\zzzcolon \Zqh\rightarrow \prod_{\zeta \in \calZ'}\modZ [q]/((q-\zeta )^{d(m)}),\quad
    f(q)\mapsto (f(q)\mod((q-\zeta )^{d(\zeta )}))_{\xi \in \calZ'},$$ is not injective.
:::

::: remark
[]{#r74 label="r74"} In the situation of Proposition [\[r55\]](#r55){reference-type="ref" reference="r55"}, suppose moreover that the elements of $S$ are pairwise non-adjacent. Then the homomorphism $\mods _S$ is surjective. Since $S=\{6^n\zzzvert n\ge 0\}$ is such an example of $S$ and it is infinite, it follows that $\Zqh$ is *not* Noetherian.
:::
