---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-013-7-symmetric-functions
section_title: "Symmetric functions"
section_number: 7
pages: 30-31
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.947
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
[]{#sec:concl label="sec:concl"}

Finally, we discuss the translation of our results

into the language of symmetric functions. The following well-known facts can be found in [@Macdonald1995 Chapter I]. Let $\Lambda$ be the ring of symmetric functions with integer coefficients in variables $x_1, x_2,\ldots$, and let $R=\bigoplus_{n\ge 0} \, \mathcal{C}(S_n)$. There is a well-known canonical ring isomorphism $\operatorname{ch}\colon R\to \Lambda$, where the ring structure on $R$ is given, for $f \in \mathcal{C}(S_m)$ and $g\in \mathcal{C}(S_n)$, by $fg = \mathop{\mathrm{Ind}}_{S_m \times S_n}^{S_{mn}}(f \times g)$.

Moreover, the map $\operatorname{ch}$ is an isometry with respect to the standard inner products $\langle\cdot, \hskip1pt \cdot \rangle$ on $R$ and $\Lambda$. If $\lambda/\mu$ is any skew-partition, then $\operatorname{ch}(\chi^{\lambda/\mu}) = s_{\lambda/\mu}$, the skew Schur function corresponding to $\lambda/\mu$. Furthermore, suppose that $\beta$ and $\nu$ are partitions, with $|\beta|=m$ and $|\nu|=n$. Denote by $s_{\nu}\circ s_{\beta}$ the plethysm of $s_{\nu}$ and $s_{\beta}$ (see [@Macdonald1995 §I.8]). Then $$\label{eq:ch}
 \operatorname{ch}\left( \mathop{\mathrm{Ind}}_{S_m\wr S_n}^{S_{mn}} (\widetilde{(\chi^{\beta})^{\times n}} \mathop{\mathrm{Inf}}_{S_n}^{S_m\wr S_n} \chi^{\nu}) \right) = s_{\nu} \circ s_{\beta}$$ (see [@Macdonald1995 §I.8 and §I.A.6]). By first using Frobenius reciprocity, then the inflation-deflation reciprocity relation of Equation ([\[eq:reciprocity\]](#eq:reciprocity){reference-type="ref" reference="eq:reciprocity"}), we have $$\left<
\mathop{\mathrm{Ind}}_{S_m\wr S_n}^{S_{mn}} (\widetilde{(\chi^{\beta})^{\times n}} \mathop{\mathrm{Inf}}_{S_n}^{S_m\wr S_n} \chi^{\nu}),
\chi^{\lambda/\mu}
\right> = \left< \chi^\nu, \mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{\beta}}_{S_n} \chi^{\lambda/\mu} \right>$$ for any skew-partition $\lambda / \mu$ with $|\lambda / \mu| = mn$. Comparing with Equation [\[eq:ch\]](#eq:ch){reference-type="eqref" reference="eq:ch"} shows that if $\lambda/\mu$ is such a skew-partition then $$\label{eq:defpl}
 \mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{\beta}}_{S_n} \chi^{\lambda/\mu} = \sum_{\nu} \langle s_{\lambda/\mu}, s_{\nu}\circ s_{\beta} \rangle\chi^{\nu}$$ where the sum is over all partitions $\nu$ of $n$.

Let $p_l = \sum_{i} x_i^l$ be the power-sum symmetric function, and write $p_{\gamma} = p_{\gamma_1} \cdots p_{\gamma_d}$ for any composition $\gamma=(\gamma_1,\ldots, \gamma_d)$. If $\gamma$ is a composition of $n$, then $\chi^{\nu} (g_{\gamma}) = \langle p_{\gamma}, s_{\nu} \rangle$ (see [@Macdonald1995 Equation (I.7.8)]). Using Equation [\[eq:defpl\]](#eq:defpl){reference-type="eqref" reference="eq:defpl"}, we obtain $$\label{eq:trans}
 \begin{split}
  (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}^{\chi^{\beta}} \chi^{\lambda/\mu})(g_{\gamma}) &= \sum_{\nu} \langle s_{\lambda/\mu}, s_{\nu} \circ s_{\beta} \rangle\chi^{\nu} (g_{\gamma}) \\
 &= \sum_{\nu}\langle s_{\lambda/\mu}, s_{\nu} \circ s_{\beta} \rangle\langle s_{\nu}, p_{\gamma} \rangle= \langle s_{\lambda/\mu}, p_{\gamma} \circ s_{\beta} \rangle
 \end{split}$$ where the sums are over all partitions of $n$.

In the case when $\beta = (m)$, we have $s_{\beta} = h_m$, where $h_m$ is the complete symmetric function of degree $m$ (see [@Macdonald1995 Section I.2]). Thus Equation [\[eq:trans\]](#eq:trans){reference-type="eqref" reference="eq:trans"} shows that Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} is equivalent to the identity $$\label{eq:cd2}
 \langle s_{\lambda/\mu}, p_{\gamma} \circ h_m \rangle= a_{\lambda/\mu, \gamma}.$$

In [@DLT Section 9], Désarménien, Leclerc, and Thibon obtain a formula which implies that $$\label{eq:DLT}
 s_{\mu} (p_n \circ h_m) = \sum_{\lambda} \varepsilon_n (\lambda/\mu) a_{\lambda/\mu, (n)},$$ where the sum is over the partitions $\lambda$ of $|\mu|+mn$ such that $\lambda\supseteq \mu$. (Our definition of an $m$-border-strip tableau of type $(n)$ is equivalent to the definition of a horizontal $n$-ribbon tableau of weight $m$ in [@DLT].) In fact, the formula in [@DLT] is more general, giving a combinatorial description of $s_{\mu} (p_n \circ s_{\kappa})$ for any partition $\kappa$ of $n$. Clearly, Equation [\[eq:DLT\]](#eq:DLT){reference-type="eqref" reference="eq:DLT"} is equivalent to Equation [\[eq:cd2\]](#eq:cd2){reference-type="eqref" reference="eq:cd2"} in the case $\gamma=(n)$; this leads, after some work, to an alternative proof of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}.

Furthermore, in the special case when $\mu=\varnothing$, a combinatorial description of the left-hand side of Equation [\[eq:cd2\]](#eq:cd2){reference-type="eqref" reference="eq:cd2"} is given by Macdonald in [@Macdonald1995 §I.8, Example 8]. Using Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}, one can see that this description is equivalent to the definition of $a_{\lambda, \gamma}$.
