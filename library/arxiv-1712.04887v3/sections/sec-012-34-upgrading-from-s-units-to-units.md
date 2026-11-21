---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-012-34-upgrading-from-s-units-to-units
section_title: "Upgrading from S-units to units"
section_number: 3.4
pages: 20-20
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.975
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.updrading2 label="sub.updrading2"}

We give the following slight improvement on Lemma [\[lemma:avoidS\]](#lemma:avoidS){reference-type="ref" reference="lemma:avoidS"}.

::: lemma
[]{#lemma:avoidS2 label="lemma:avoidS2"} Suppose that any prime divisor $p$ of $n$ is odd and divides neither the discriminant of $F$ nor the order of $K_2(\mathcal{O}_F)$. Then the image of $c_\zeta$ on $K_3(F)/nK_3(F)$ may be realized by an element of $\mathcal{O}^{\times}_n$.
:::

::: proof
*Proof.* By Lemma [\[lem.mab\]](#lem.mab){reference-type="ref" reference="lem.mab"}, it suffices to consider the case when $n$ is a power of $p$. Let $\zeta= \zeta_n$. The fact that $p$ is prime to the discriminant of $F$ implies that $F(\zeta)/F$ is totally ramified at $p$. The image of $c_{\zeta}$ factors through $H^1_{\text{\'{e}t}}(\mathcal{O}[1/p],\mathbf Z/n\mathbf Z(2))$, and, via inflation--restriction, through $H^1_{\text{\'{e}t}}(\mathcal{O}_{F(\zeta)}[1/p],\mathbf Z/n\mathbf Z(1))$. The Kummer sequence for étale cohomology gives a short exact sequence: $$\mathcal{O}_{F(\zeta)}[1/p]^{\times}/\mathcal{O}_{F(\zeta)}[1/p]^{\times n}
\rightarrow   H^1_{\text{\'{e}t}}(\mathcal{O}_{F(\zeta)}[1/p],\mathbf Z/n(1))
\rightarrow \mathrm{Pic}(\mathcal{O}_F(\zeta)[1/p])[n]\,.$$ The image of $c_{\zeta}$ lands in the $\chi^{-1}$-invariant part of the second group. The $\chi^{-1}$-invariant part $M^{\chi^{-1}}$ of a $G$-module $M$ is non-zero if and only if the largest $\chi^{-1}$-invariant quotient $M_{\chi^{-1}}$ is non-zero. However, by results of Keune [@Keune], there is an injection $$\left(\mathrm{Pic}(\mathcal{O}_F(\zeta)[1/p])/p^{m} \right)_{\chi^{-1}} 
\rightarrow K_2(\mathcal{O}_F)/p^{m} \,.$$ In particular, the pushforward of the image of $c_{\zeta}$ to the Picard group is trivial whenever $K_2(\mathcal{O}_F) \otimes \mathbf Z_p$ is trivial. Since we are assuming that $p$ does not divide the order of $K_2(\mathcal{O}_F)$, we deduce that the image of $c_{\zeta}$ is realized by $p$-units. We now upgrade this to actual units. There is an exact sequence: $$(\mathcal{O}_{F(\zeta)})^{\times}/ (\mathcal{O}_{F(\zeta)})^{\times n} \rightarrow 
(\mathcal{O}_{F(\zeta)}[1/p])^{\times}/(\mathcal{O}_{F(\zeta)}[1/p])^{\times n} 
\rightarrow \bigoplus_{v|p} \mathbf Z/n\mathbf Z\,,$$ where the last map is the valuation map. Since $p$ is totally ramified in $F(\zeta)/F$, the action of $G$ on the final term is trivial. By assumption, the quotient $\mathrm{Gal}(F(\zeta_p)/F)$ is non-trivial, and hence the $\chi^{-1}$-invariants of the final term are zero. Hence, after taking $\chi^{-1}$-invariants, we see that the image of $c_\zeta$ comes from a unit. ◻
:::
