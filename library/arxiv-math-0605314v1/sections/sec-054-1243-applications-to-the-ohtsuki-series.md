---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-054-1243-applications-to-the-ohtsuki-series
section_title: "Applications to the Ohtsuki series"
section_number: 12.4.3
pages: 45-47
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.94
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:appl-ohts-seri label="sec:appl-ohts-seri"}

Here we apply Propositions [\[thm:44\]](#thm:44){reference-type="ref" reference="thm:44"} and [\[r10\]](#r10){reference-type="ref" reference="r10"} to the Ohtsuki series $\tau ^O(M)$, and obtain some congruence relations on the coefficients of $\tau ^O(M)$, which generalize well-known results by Murakami [@Murakami1] and Ohtsuki [@Ohtsuki1], and by Lin and Wang [@Lin-Wang; @Lin-Wang2] for the first and the second coefficients.

We write $$\tau ^O(M)=\iota _1(J_M)=1+\lambda _1(M)\modh +\lambda _2(M)\modh ^2+\cdots\in \modZ [[\modh ]],$$ where we set $\modh =q-1$. We often write $\lambda _i=\lambda _i(M)$ in the following.

The following gives an infinite set of congruence relations for the coefficients $\lambda _i(M)$ of the Ohtsuki series of $M$.

::: proposition
[]{#r68 label="r68"} For $k\ge 0$, we have $$\label{e39}
    \sum_{i=0}^k a_i\lambda _{k-i+1}(M)\equiv0\pmod{\modZ }.$$ Here $a_0=1/6$, $a_1=-1/4$, $a_2=17/72$, $a_3=-25/144$, $\dots\in \modZ [\frac16]$ are determined by $$\sum_{i\ge 0}a_i\modh ^i=\frac1{(q+1)(q^2+q+1)}=\frac{1}{6+9\modh +5\modh ^2+\modh ^3}.$$ In particular, each $\lambda _{k+1}(M)\mod6$, $k\ge 0$, is determined by $\lambda _i(M)$, $i=1,\ldots,k$.
:::

::: proof
*Proof.* Set $$\begin{gathered}
    f(\modh )=\modh ^{-1}(\tau ^O(M)-1)=\sum_{k\ge 0}\lambda _{k+1}\modh ^k\in \modZ [[\modh ]],\\
    a(\modh )=(q+1)(q^2+q+1)=6+9\modh +5\modh ^2+\modh ^3.
  
\end{gathered}$$ Using Proposition [\[thm:44\]](#thm:44){reference-type="ref" reference="thm:44"}, we see that there is $g(\modh )=\sum_{k\ge 0}g_k\modh ^k\in \modZ [[\modh ]]$ such that $f(\modh )=a(\modh )g(\modh )$, hence $g(\modh )=f(\modh )a(\modh )^{-1}$. (Here we used the divisibility of $J_M-1$ by $(q-1)(q+1)(q^2+q+1)$, not by $q^6-1$.) We have $$g_k= \sum_{i=0}^k a_i\lambda _{k-i+1}.$$ Since $g_k\in \modZ$ for all $k\ge 0$, we have [\[e39\]](#e39){reference-type="eqref" reference="e39"}. Since $a_0=1/6$, the latter assertion follows. ◻
:::

By [\[e39\]](#e39){reference-type="eqref" reference="e39"} and $a_0=\frac16$, we have $$\label{e71}
  \lambda _{k+1}\equiv - \sum_{i=1}^k 6a_i\lambda _{k-i+1}\pmod6.$$ For small values of $k$, [\[e71\]](#e71){reference-type="eqref" reference="e71"} implies the following.

1.  []{#item:5 label="item:5"} $\lambda _1\equiv0\pmod6$. This is known by Murakami [@Murakami1] and Ohtsuki [@Ohtsuki1].

2.  []{#item:6 label="item:6"} $\lambda _2\equiv\frac{3}{2}\lambda _1\equiv\frac{1}{2}\lambda _1\pmod6$. This is known by Lin and Wang [@Lin-Wang]. See also Corollary [\[r60\]](#r60){reference-type="ref" reference="r60"} below.

3.  []{#item:7 label="item:7"} $\lambda _3\equiv\frac{3}{2}\lambda _2-\frac{17}{12}\lambda _1\pmod6$.

4.  []{#item:8 label="item:8"} $\lambda _4\equiv\frac{3}{2}\lambda _3-\frac{17}{12}\lambda _2+\frac{25}{24}\lambda _1\pmod6$.

::: remark
[]{#r69 label="r69"} One can use divisibility of $J_M-1$ by $q^6-1$ instead of $(q-1)(q+1)(q^2+q+1)=(q^6-1)/\Phi _6(q)$. In this case, we obtain a result equivalent to Proposition [\[r68\]](#r68){reference-type="ref" reference="r68"} as a consequence of the fact that $\Phi _6(q)=q^2-q+1$ is invertible in $\modZ [[q-1]]$.
:::

The above-described idea can be applied also to Proposition [\[r10\]](#r10){reference-type="ref" reference="r10"} to obtain better results. We write $$\begin{gathered}
  \iota _1(J_M-q^{\lambda _1(M)})=\tau ^O(M)-q^{\lambda _1(M)}=\sum_{k\ge 2}\lambda '_k(M)\modh ^k.
\end{gathered}$$ We have $$\label{e69}
  \lambda '_k(M) = \lambda _k(M)-\binom{\lambda _1(M)}{k}\in \modZ$$ for $k\ge 2$.

::: proposition
[]{#r70 label="r70"} For $k\ge 0$, we have $$\label{e68}
    \sum_{i=0}^k b_i\lambda '_{k-i+2}(M)\equiv0\pmod{\modZ }.$$ Here $b_0=1/12$, $b_1=-5/24$, $b_2=41/144$, $b_3=-77/288$, $\dots\in \modZ [\frac16]$ are determined by $$\sum_{i\ge 0}b_i\modh ^i=\frac1{(q+1)(q^2+q+1)(q^2+1)}
    =\frac{1}{12+30\modh +34\modh ^2+21\modh ^3+7\modh ^4+\modh ^5}.$$ In particular, for $k\ge 0$, $\lambda '_{k+2}(M)\mod{12}$ is determined by $\lambda '_i(M)$, $i=2,\ldots,k+1$.
:::

::: proof
*Proof.* The proof is similar to that for Proposition [\[r68\]](#r68){reference-type="ref" reference="r68"}, where we use Proposition [\[r10\]](#r10){reference-type="ref" reference="r10"} instead of Proposition [\[thm:44\]](#thm:44){reference-type="ref" reference="thm:44"}. The details are left to the reader. ◻
:::

::: corollary
[]{#r59 label="r59"} For $k\ge 0$, $\lambda _{k+2}(M)\mod{12}$ is determined by $\lambda _i(M)$, $i=1,\ldots,k+1$.
:::

::: proof
*Proof.* This immediately follows from Proposition [\[r70\]](#r70){reference-type="ref" reference="r70"} and [\[e69\]](#e69){reference-type="eqref" reference="e69"}. ◻
:::

The case $k=0$ of [\[e68\]](#e68){reference-type="eqref" reference="e68"} is equivalent to the following.

::: corollary
[]{#r60 label="r60"} We have $$\lambda _2(M)\equiv3\lambda (M)=\hf\lambda _1(M)\pmod{12}.$$
:::

::: proof
*Proof.* We have $\lambda _2(M)\equiv\binom{\lambda _1(M)}{2} =\binom{6\lambda (M)}{2}
  =18\lambda (M)^2-3\lambda (M) \equiv6\lambda (M)-3\lambda (M) \equiv3\lambda (M)\pmod{12}$. ◻
:::

::: remark
[]{#r61 label="r61"} Propositions [\[thm:44\]](#thm:44){reference-type="ref" reference="thm:44"} and [\[r10\]](#r10){reference-type="ref" reference="r10"} can be applied to the power series $\iota _{-1}(J_M)\in \modZ [[q+1]]$ and one can obtain results similar to Propositions [\[r68\]](#r68){reference-type="ref" reference="r68"} and [\[r70\]](#r70){reference-type="ref" reference="r70"}. In particular, we have the following.

1.  $\lambda _{-1,1}(M)\in 6\modZ$.

2.  $\lambda _{-1,2}(M)\equiv\hf\lambda _{-1,1}(M)\pmod{12}$.

3.  For $k\ge 2$, $\lambda _{-1,k}(M)\mod12$ is determined by $\lambda _{-1,i}(M)$, $i=1,2,\ldots,k-1$.

Here $\lambda _{-1,k}(M)\in \modZ$ is defined as in [\[e75\]](#e75){reference-type="eqref" reference="e75"}.
:::

::: remark
[]{#r63 label="r63"} As for the relation between $\lambda _1(M)$ and $\lambda _{-1,1}(M)$, we have $$\label{e70}
    \lambda _1(M)\equiv\lambda _{-1,1}(M)\pmod{12}.$$ Hence, like the Casson invariant, the mod $2$ reduction of the integer-valued invariant $\frac16\lambda _{-1,1}$ equals the Rochlin invariant of $M$. [\[e70\]](#e70){reference-type="eqref" reference="e70"} follows from $\lambda _1(M)\equiv\lambda _{-1,1}(M)\equiv0\pmod3$ and $\lambda _1(M)\equiv\lambda _{-1,1}(M)\pmod{4}$. (Here, the latter congruence follows from [\[e65\]](#e65){reference-type="eqref" reference="e65"} for $\zeta =1$, $\xi =-1$, $k=1$.)
:::

### The eighth WRT invariant $\tau _8(M)$ {#sec:wrt-invariant-at}

For each $r\in \modN$, it would be interesting to know the range of $\tau _r(M)$. Using the modified version $$\tilde\tau _r(M)=\mods _{\zeta _r}(\tJ_M)=\zeta _r^{-6\lambda (M)}\tau _r(M)\in \modZ [\zeta _r],$$ one can expect to obtain sharper results than using $\tau _r(M)$. Theorem [\[r10\]](#r10){reference-type="ref" reference="r10"} implies $$\label{e63}
  \tilde\tau _r(M)-1
  \in 
  (\zeta _r-1)(\zeta _r^6-1)(\zeta _r^2+1)\modZ [\zeta _r].$$ If $r$ is of the form $ip^e$, where $i\in \{1,2,3,4,6\}$ and $p^e$ is a prime power, [\[e63\]](#e63){reference-type="eqref" reference="e63"} gives some restriction on the value of $\tilde\tau _r(M)$.

For example, we here consider $\tau _8(M)$. We have $\zeta _8=\exp
\frac{2\pi \sqrt{-1}}{8}=\frac{1+\sqrt{-1}}{\sqrt{2}}$, and $$\tilde\tau _8(M)=\sqrt{-1}^{\lambda (M)}\tau _8(M)\in \modZ [\zeta _8].$$

::: proposition
[]{#r11 label="r11"} For any integral homology sphere $M$, we have $$\tilde\tau _8(M)-1
    \in 2(\zeta _8-1)\modZ [\zeta _8]
    =\Span_\modZ \{4,2\sqrt2,2+2\sqrt{-1},2+\sqrt2+\sqrt{-2}\}.$$
:::

::: proof
*Proof.* By [\[e63\]](#e63){reference-type="eqref" reference="e63"}, it follows that $\tilde\tau _8(M)-1$ is divisible in $\modZ [\zeta _8]$ by $(\zeta _8-1)(\zeta _8^4-1)=-2(\zeta _8-1)$. Hence, we have the assertion. ◻
:::

Note that $\modZ [\zeta _8]/2(\zeta _8-1)\modZ [\zeta _8]\cong(\modZ /4\modZ )\oplus(\modZ /2\modZ )^3$. Computations suggest the following, a much stronger restriction on $\tilde\tau _8$.

::: conjecture
[]{#r7 label="r7"} For any integral homology sphere $M$, we have $$\tilde\tau _8(M)-1
    \in \Span_\modZ \{4,2\sqrt2\}.$$ (Consequently, $\tilde\tau _8(M)$ is real. Hence, $\tau _8(M)$ is either real or purely imaginary.)
:::

::: remark
[]{#r13 label="r13"} Conjecture [\[r7\]](#r7){reference-type="ref" reference="r7"} implies that the $\modQ$-vector subspace $G_8$ of $\modQ (\zeta _8)$ generated by $\tilde\tau _8(M)-1$ for all integral homology spheres $M$ is strictly smaller than $\modQ (\zeta _8)$. More generally, let $G_r\subset \modQ (\zeta _r)$ be the $\modQ$-vector subspace generated by the $\tilde\tau _r(M)-1$. Then $G_r\subsetneq\modQ (\zeta _r)$ if $r=1,2,3,4,6$. Conjecturally, $G_r=\modQ (\zeta _r)$ if $r\neq 1,2,3,4,6,8$.
:::
