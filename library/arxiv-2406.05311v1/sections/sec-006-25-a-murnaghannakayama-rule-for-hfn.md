---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-006-25-a-murnaghannakayama-rule-for-hfn
section_title: "A Murnaghan–Nakayama rule for H*Fn"
section_number: 2.5
pages: 7-8
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.779
latex_coverage_ratio: 0.962
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
We recall the following special case of Formula [\[eq:classical-coeffs\]](#eq:classical-coeffs){reference-type="eqref" reference="eq:classical-coeffs"}, which is [@So96 Cor. 9].

::: proposition
[]{#pieri-formulas-version-2 label="pieri-formulas-version-2"} Let $u \in S_n$, $a\leq k$, and $b\leq n{-}k$. Then $$\label{eq:schubert-times-hook-via-peakless-chains}
        {\mathfrak S}_u(x)\cdot s_{(b,1^{a-1})}(x_1,\dotsc,x_k)\ =\ \sum_\gamma {\mathfrak S}_{\mathop{\mathrm{end}}(\gamma)}(x)\,,$$ the sum over all peakless chains starting at $u$ of height $a$ and length $a{+}b{-}1$ in the $k$-Bruhat order.
:::

Using Proposition [\[P:peaklessChains\]](#P:peaklessChains){reference-type="ref" reference="P:peaklessChains"}, we can explicitly describe the coefficients appearing in [\[eq:schubert-times-hook-via-peakless-chains\]](#eq:schubert-times-hook-via-peakless-chains){reference-type="eqref" reference="eq:schubert-times-hook-via-peakless-chains"}.

::: proposition
[]{#P:classical_hook label="P:classical_hook"} Let $u \in S_n$, $a\leq k$ and $b\leq n{-}k$. Then $$\label{Eq:Schubert-times-hook}
        {\mathfrak S}_u(x) \cdot s_{(b, 1^{a-1})}(x_1,\dotsc,x_k)\ =\
        \sum
        \left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)
        {\mathfrak S}_{\zeta u}(x) \,,$$ the sum over all minimal permutations $\zeta \in S_n$ such that $u\leq_k\zeta u$ and ${\mathcal L}(\zeta)=a+b-1$.
:::

We use Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"} to derive a formula for the product of a Schubert polynomial and a power sum symmetric polynomial. Let ${\color{RoyalBlue}p_r(x_1,\dotsc,x_k)}\vcentcolon=x_1^r+\dotsb+x_k^r$ denote the $r$th power sum polynomial. Expanded in terms of Schur polynomials [@Macdonald], we have $$\label{Eq:PowerSumHook}
    p_r(x_1, \ldots, x_k) =
    s_{(r)}(x_1, \ldots, x_k) - s_{(r-1,1)}(x_1, \ldots, x_k) + \cdots + (-1)^{r+1} s_{(1^r)}(x_1, \ldots, x_k).$$

::: corollary
[]{#C:classical-schubert-times-powersum label="C:classical-schubert-times-powersum"} Let $u \in S_n$. Then $${\mathfrak S}_u(x) \cdot p_r(x_1,\dotsc,x_k)\ =\ \sum (-1)^{\mathop{\mathrm{ht}}(\zeta)+1} {\mathfrak S}_{\zeta u}(x)\,,$$

the sum over all minimal cycles $\zeta \in S_n$ such that $u\leq_k\zeta u$ and ${\mathcal L}(\zeta)=r$.
:::

::: proof
*Proof.* Expanding the product ${\mathfrak S}_u(x) \cdot p_r(x_1,\dotsc,x_k)$ using Equations [\[Eq:Schubert-times-hook\]](#Eq:Schubert-times-hook){reference-type="eqref" reference="Eq:Schubert-times-hook"} and [\[Eq:PowerSumHook\]](#Eq:PowerSumHook){reference-type="eqref" reference="Eq:PowerSumHook"} shows that the coefficient of ${\mathfrak S}_{\zeta u}$ for $u\leq_k\zeta u$ is zero unless ${\mathcal L}(\zeta)=r$ and $\zeta$ is minimal. When $\zeta$ is the noncrossing product of $s(\zeta)$ minimal cycles, this coefficient is $$(-1)^{\mathop{\mathrm{ht}}(\zeta)+1} \sum_{a=1}^{r} (-1)^{a-\mathop{\mathrm{ht}}(\zeta)}\binom{s(\zeta)-1}{\mathop{\mathrm{ht}}(\zeta)-a}\ =\
        \begin{cases}
            0,  & \text{ if } s(\zeta)\neq 1,\\
            (-1)^{\mathop{\mathrm{ht}}(\zeta)+1},& \text{ if } s(\zeta)=1.
        \end{cases}
        \qedhere$$ ◻
:::

This proof differs from that given in [@Morrison; @MorrisonSottile].
