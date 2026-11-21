---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-035-76-speed-in-convergence
section_title: "Speed in convergence"
section_number: 7.6
pages: 51-53
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.888
latex_coverage_ratio: 0.962
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
We now use [@ReinertRollin2009 Corollary 3.1], which gives an estimate for $$\left| \mathbb{E}_n^{(\alpha)}h(\tilde{W}_d) - \mathbb{E}h(\tilde{\Xi}_d) \right|$$ for non-smooth test functions $h$. In particular, we shall consider functions $h$ in the set $\mathcal{H}$ of indicator functions of convex sets. We have the following result, which is stronger than Theorem [\[theo:SpeedConvergence\]](#theo:SpeedConvergence){reference-type="ref" reference="theo:SpeedConvergence"}.

::: theorem
For any integer $d \ge 2$, we have $$\sup_{h \in \mathcal{H}} |\mathbb{E}_n^{(\alpha)}\, h(\tilde{W}_d) - \mathbb{E}\, h(\tilde{\Xi}_d)| 
        =O\big(n^{-1/4} \big).$$ []{#theo:SpeedConvergenceConvex label="theo:SpeedConvergenceConvex"}
:::

::: proof
*Proof.* Fix an integer $d \ge 2$ and consider the exchangeable pair $(\tilde{W}_d,\tilde{W}^\star_d)$ defined as in the previous sections.

As shown in Section [\[subsec:CheckingHypotheses\]](#subsec:CheckingHypotheses){reference-type="ref" reference="subsec:CheckingHypotheses"}, this exchangeable pair fulfills the condition of [@ReinertRollin2009 Theorem 2.1]. Besides, as mentioned in [@ReinertRollin2009 Section 3], the set $\mathcal{H}$ of functions fulfills conditions $(C1)$, $(C2)$ and $(C3)$ (with $a=2\sqrt{d}$) from this paper. Therefore, one can apply [@ReinertRollin2009 Corollary 3.1] and we find that there exists a constant $\zeta=\zeta(d)$ such that $$\label{eq:ReinertNonSmooth}
        \sup_{h \in \mathcal{H}} |\mathbb{E}_n^{(\alpha)}\, h(\tilde{W}_d) - \mathbb{E}\, h(\tilde{\Xi}_d)|
    \le \zeta^ 2 \left(  \frac{A' \log(1/T')}{2} +\frac{B'}{2\sqrt{T'}} +2\sqrt{dT'} \right),$$ where we define $$\begin{aligned}
        \hat{\lambda}^{(i)} &:= \sum_{m=1}^d |(\varSigma^{-1/2} \Lambda^{-1} \varSigma^{1/2})_{m,i}|,\\
        A'&:= \sum_{i,j} \hat{\lambda}^{(i)} \sqrt{\sum_{k,l} \varSigma^{-1/2}_{i,k}  \varSigma^{-1/2}_{j,\ell}
        \mathop{\mathrm{Var}}(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d} (W'_k -W_k)(W'_\ell-W_\ell)},\\
        B'&:= \sum_{i,j,k} \hat{\lambda}^{(i)} \mathbb{E}_n^{(\alpha)} \left|
        \sum_{r,s,t} \varSigma^{-1/2}_{i,r} \varSigma^{-1/2}_{j,s} \varSigma^{-1/2}_{k,t}
        (W'_r -W_r)(W'_s -W_s)(W'_t -W_t)\right|,\\
        T'&:= \frac{1}{4d}\left( \frac{A'}{2} + \sqrt{B'\sqrt{d} + \frac{(A')^2}{4}} \right)^2.
    
\end{aligned}$$ Comparing this with the statement in [@ReinertRollin2009], note that in our case, there is no remaining matrix $R$, and hence $C'=0$. Besides, for the set $\mathcal{H}$ considered here (indicator functions of convex subsets of $\mathbb{R}^d$), one can choose $a=2\sqrt{d}$.

We shall now describe the asymptotic behaviour of the quantities above. Note that all sums appearing above have fixed number of summands since the summation index set is always the set of integers less or equal to $d$.

Recall that, in our setting, $\Lambda^{-1}$ is the diagonal matrix $(n/(i+1) \cdot  \delta_{i,j})$. Besides $\varSigma^{-1/2}$ (well-defined for $n$ big enough) is a bounded matrix (Proposition [\[prop:SteinCondition2\]](#prop:SteinCondition2){reference-type="ref" reference="prop:SteinCondition2"}). Hence for any $i \le d$, $$\hat{\lambda}^{(i)} = O(n).$$ Consider now $A'$. It was proven in Section [\[subsec:ErrorTerm\]](#subsec:ErrorTerm){reference-type="ref" reference="subsec:ErrorTerm"} (Lemma [\[lem:fourth_moment\]](#lem:fourth_moment){reference-type="ref" reference="lem:fourth_moment"} and equation [\[eq:TechnicalBound\]](#eq:TechnicalBound){reference-type="eqref" reference="eq:TechnicalBound"}) that, for any $k$ and $\ell$, $$|\mathop{\mathrm{Var}}(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d} (W'_k -W_k)(W'_\ell-W_\ell) | = O(n^{-3}).$$ Together with the bound on $\hat{\lambda}^{(i)}$ and the fact that $\varSigma^{-1/2}$ is bounded, this implies $$A'=O(n^{-1/2}).$$ Consider now $B'$. We have proved that the bound [\[eq:BoundTripleProductGoodCase\]](#eq:BoundTripleProductGoodCase){reference-type="eqref" reference="eq:BoundTripleProductGoodCase"} holds in expectation, that is $$\mathbb{E}_n^{(\alpha)} \left|(W'_r -W_r)(W'_s -W_s)(W'_t -W_t)\right| \leq O(n^{-3/2}).$$ As before, the bound above on $\hat{\lambda}^{(i)}$ and the fact that $\varSigma^{-1/2}$ is bounded implies $$B'=O(n^{-1/2}).$$ Combining the bounds for $A'$ and $B'$, we get $T' = O(n^{-1/2})$. Strictly from the definition of $T'$, we also get $T' \ge B'$, which implies that $\frac{B'}{2\sqrt{T'}} \le \sqrt{B'}=O(n^{-1/4})$. Plugging all these estimates in equation [\[eq:ReinertNonSmooth\]](#eq:ReinertNonSmooth){reference-type="eqref" reference="eq:ReinertNonSmooth"}, we get the desired result. ◻
:::
