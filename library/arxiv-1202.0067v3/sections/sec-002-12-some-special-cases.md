---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-002-12-some-special-cases
section_title: "Some special cases"
section_number: 1.2
pages: 5-6
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.926
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
It is clear than if $m=1$ then $\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi=
\chi$ for any character $\chi$ of $S_n$, and so the special case $m=1$ of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} asserts that $\chi^{\lambda / \mu} (g) = a_{\lambda/ \mu , \gamma}$ for any skew-partition $\lambda / \mu$ of $n$ and any element $g \in S_n$ of cycle type $\gamma$. Equivalently, $$\chi^{\lambda / \mu} (g) = \sum_{T} \mathrm{sgn}(T)$$ where the sum is over all border-strip tableaux of shape $\lambda / \mu$ and type $\gamma$. This is the Murnaghan--Nakayama rule, as stated in [@StanleyII Equation (7.75)]. It should be noted that we require the Murnaghan--Nakayama rule in §[\[subsec:omega_proof\]](#subsec:omega_proof){reference-type="ref" reference="subsec:omega_proof"} below, and so our work does not provide a new proof of this result. In practice the Murnaghan--Nakayama rule is most frequently used as a recursive formula for the values of characters or skew characters. Equation [\[eq:defres_decomp_sgn\]](#eq:defres_decomp_sgn){reference-type="eqref" reference="eq:defres_decomp_sgn"} at the end of §[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"} formulates Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} in this way.

As Stanley observes in [@StanleyII page 348], it is far from obvious that the character values given by the Murnaghan--Nakayama rule applied to a skew-partition $\lambda / \mu$ and a composition $\gamma$ are independent of the order of the parts of $\gamma$. This remark applies even more strongly to Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}. For example, the reader may check that if $\lambda / \mu = (6,5,3,2) / (3,1)$, as in Example [\[example:border_strip\]](#example:border_strip){reference-type="ref" reference="example:border_strip"}, and $\gamma' = (2,1,3)$, then there is a unique $2$-border-strip tableau of shape $(6,5,3,2) / (3,1)$ and type $\gamma'$. Thus $a_{\lambda/\mu,\gamma'} = 1$, but the sums defining $a_{\lambda/ \mu,\gamma}$ and $a_{\lambda / \mu, \gamma'}$ are different.

Another special case of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} worth noting occurs when $g$ is the identity element of $S_n$. If $\xi$ is an irreducible character of $S_m \wr S_n$ then either the base group $B = S_m \times \cdots \times S_m$ is contained in the kernel of $\xi$ and $\left<\mathop{\mathrm{Res}}_B \xi, 1_B\right>
= \xi(1)$, or $\left<\mathop{\mathrm{Res}}_B \xi, 1_B\right> = 0$. Hence, by linearity, we have $$\label{eq:deflation_special} 
(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi)(1) = \left<\mathop{\mathrm{Res}}_B \chi ,1_B\right>$$ for any character $\chi$ of $S_{mn}$. It now follows from Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and Frobenius reciprocity that $$a_{\lambda / \mu, (1^n)} =
\left< \chi^{\lambda / \mu},
 \mathop{\mathrm{Ind}}_{S_m \times \cdots \times S_m}^{S_{mn}}
1_{S_m} \times \cdots \times 1_{S_m} \right>$$ for any skew-partition $\lambda / \mu$ of $mn$. It is clear from Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"} that $a_{\lambda / \mu, (1^n)}$ is the number of semi-standard tableaux of shape $\lambda / \mu$ and type $(m^n)$. Therefore, by setting $\mu = \varnothing$ in the previous equation, we obtain a special case of Young's rule (see [@JK 2.8.5] or [@StanleyII Proposition 7.18.7]).
