---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-016-8-algebraically-split-links
section_title: "Algebraically-split links"
section_number: 8
pages: 28-29
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.912
---
[]{#sec8 label="sec8"}

In this section, we prove an integrality result for the colored Jones polynomials of algebraically-split, $0$-framed links. We also give some conjectures for boundary links in the last subsection.

## The algebra $\modP$ and its completion $\hat\modP$ {#sec:algebra--its-1}

For $n\ge 0$, set $$\begin{gathered}
  P'_n = \frac{P_n}{\{n\}!}\in \modR _{\modQ (v)},\\
  \tP'_n = v^{-\hf n(n-1)}P'_n\in \modR _{\modQ (v)}.
\end{gathered}$$ We have $P'_0=1$. Define a $\Zqq$-submodule $\modP$ of $\modR _{\modQ (v)}$ by $$\modP  = \Span_{\Zqq}\{\tP'_n\zzzvert n\ge 0\}.$$

::: lemma
[]{#r26 label="r26"} $\modP$ is a $\Zqq$-subalgebra of $\modR _{\modQ (v)}$.
:::

::: proof
*Proof.* By induction, we obtain $$P_mP_n = \sum_{i=0}^{\min(m,n)}
    \frac{\BB mi\BB ni\BB{m+n}i}{\{i\}!}P_{m+n-i}.$$ Hence, $$\label{eq:69}
    P'_mP'_n = \sum_{i=0}^{\min(m,n)}
    \frac{\{m+n\}!}{\{i\}!\{m-i\}!\{n-i\}!}P'_{m+n-i}.$$ The coefficient in the right-hand side is contained in $v^d\Zqq$, where $    d\equiv\binom{m+n+1}2-\binom{i+1}2-\binom{m-i+1}2-\binom{n-i+1}2
    \equiv \binom{i+1}2\pmod2.
  $ Since $    \binom m2+\binom n2 -\binom{m+n-i}2
      \equiv \binom{i+1}2\pmod2,
  $ we have $v^{\binom m2}P'_mv^{\binom n2}P'_n\in \modP$. Therefore, we have $\modP \modP \subset \modP$. Since we have $1=P'_0\in \modP$, we have the assertion. ◻
:::

For $k\ge 0$, set $$\modP _k = \Span_{\Zqq}\{\tP'_n\zzzvert n\ge k\}\subset \modP .$$ We have $$\modP =\modP _0\supset \modP _1\supset \modP _2\supset \cdots.$$ It follows from [\[eq:69\]](#eq:69){reference-type="eqref" reference="eq:69"} that each $\modP _k$ is an ideal in $\modP$. Set $$\hP = \varprojlim_{k\ge 0} \modP /\modP _k,$$ which inherits a $\Zqq$-algebra structure from $\modP$. Each element $x\in \hP$ can be uniquely expressed as an infinite sum $x=\sum_{k=0}^\infty 
x_k\tP'_k$, where $x_k\in \Zqq$ for $k\ge 0$. Since $\bigcap_{k\ge 0}\modP _k=\{0\}$, we may regard $\modP$ as a subalgebra of $\hP$.

## Integrality for algebraically-split, $0$-framed links {#sec:maps-jlhphphaq}

The following theorem is proved in Section [\[sec:proof-theorem-refr29\]](#sec:proof-theorem-refr29){reference-type="ref" reference="sec:proof-theorem-refr29"}.

::: theorem
[]{#r29 label="r29"} Let $L$ be an $m$-component, algebraically-split, $0$-framed link. For $i=1,\ldots,m$, let $x_i\in \modP _{k_i}$, $k_i\ge 0$. Then we have $$J_L(x_1,\ldots,x_m) \in \frac{\BBq{2k+1}{k+1}}{\{1\}_q}\Zqq,$$ where $k=\max(k_1,\ldots,k_m)$.
:::

Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"} immediately implies the following.

::: corollary
[]{#r87 label="r87"} Let $L$ be an $m$-component, algebraically-split, $0$-framed link. Then the $\modQ (v)$-multilinear map $J_L\zzzcolon \modR _{\modQ (v)}\times \cdots\times \modR _{\modQ (v)}\rightarrow \modQ (v)$ restricts to a $\Zqq$-multilinear map $$J_L\zzzcolon \modP \times \cdots\times \modP \rightarrow \Zqq,$$ which induces a $\Zqq$-multilinear map $$J_L\zzzcolon \hP\times \cdots\times \hP\rightarrow \Zqh.$$
:::

::: remark
[]{#r30 label="r30"} It follows from [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"} that for an $m$-component, algebraically-split, $0$-framed link $L$, the colored Jones polynomial $J_L(\V_{n_1},\ldots,\V_{n_m})$, $n_1,\ldots,n_m\ge 0$, can be expressed as a linear combination of the $J_L(P'_{k_1},\ldots,P'_{k_m})$, $k_1,\ldots,k_m\ge 0$ as follows: $$\label{e37}
    \begin{split}
      &J_L(\V_{n_1},\ldots,\V_{n_m})
      =\sum_{k_1=0}^{n_1}\cdots\sum_{k_m=0}^{n_m}
      \prod_{i=1}^m\Bigl(\bb{n_i+k_i+1}{2k_i+1}\{k_i\}!\Bigr)
      J_L(P'_{k_1},\ldots,P'_{k_m}).
    \end{split}$$ Here the sums may be replaced with infinite sums $\sum_{k_i=0}^\infty$.
:::
