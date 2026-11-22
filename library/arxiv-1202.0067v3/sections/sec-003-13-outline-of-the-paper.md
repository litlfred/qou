---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-003-13-outline-of-the-paper
section_title: "Outline of the paper"
section_number: 1.3
pages: 6-7
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.992
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
The remainder of the paper proceeds as follows. Throughout, we shall adopt the convention that if $\alpha$ is a partition of $r \in \mathbf{N}$, then $g_\alpha \in S_r$ is an element of cycle type $\alpha$, and $z_\alpha$ is the size of the centralizer of $g_\alpha$ in $S_r$. (The choice of $g_\alpha$ within the conjugacy class is irrelevant.) If $\alpha = (\alpha_1,\ldots,\alpha_k)$, we write $n\alpha = (n\alpha_1,\ldots,n\alpha_k)$.

In §[\[sec:averaging\]](#sec:averaging){reference-type="ref" reference="sec:averaging"} we prove Proposition [\[prop:deflation\]](#prop:deflation){reference-type="ref" reference="prop:deflation"}, which implies that if $\chi$ is a character of $S_{mn}$ and $g\in S_n$, then $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi)(g)$ is the average value of $\chi$ on the coset of the base group $S_m \times \cdots \times S_m$ in $S_m \wr S_n$ corresponding to $g$. Equation [\[eq:deflation_special\]](#eq:deflation_special){reference-type="eqref" reference="eq:deflation_special"} above is a special case of this result. In the case when $g \in S_n$ is an $n$-cycle, we obtain Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}(ii), which implies that if $\lambda / \mu$ is a skew-partition of $mn$, then $$\label{eq:cycle_deflation}
 \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu}(g) = 
\sum_{\alpha}\frac{\chi^{\lambda / \mu}(g_{n\alpha})}{z_\alpha}$$ where the sum is over all partitions $\alpha$ of $m$, and $n\alpha$ denotes the partition obtained from $\alpha$ by multiplying each of its parts by $n$.

In §[\[sec:skew\]](#sec:skew){reference-type="ref" reference="sec:skew"} we state a theorem of Farahat (see [@Farahat1954 Section 4]), which gives a formula for the character values $\chi^{\lambda/\mu}(g_{n\alpha})$ appearing on the right-hand side of [\[eq:cycle_deflation\]](#eq:cycle_deflation){reference-type="eqref" reference="eq:cycle_deflation"}. We then give a character-theoretic proof of this theorem.

In §[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"} we combine the results of §3 and §4 to show that Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} holds when $g \in S_n$ is an $n$-cycle (Proposition [\[prop:basecase\]](#prop:basecase){reference-type="ref" reference="prop:basecase"}) and then to deduce it in general.

In §[\[sec:Foulkes\]](#sec:Foulkes){reference-type="ref" reference="sec:Foulkes"} we apply our results on deflations to Foulkes' Conjecture on permutation characters the symmetric group. In particular, we prove a new recursive formula for the character multiplicities that appear in this conjecture. Using this formula we check Foulkes' Conjecture in some new cases, extending the results in [@MN].

In §[\[sec:gendef\]](#sec:gendef){reference-type="ref" reference="sec:gendef"}, we consider the more general deflation maps $\mathop{\mathrm{Def}}^\vartheta_{S_n}$. When $\vartheta=\chi^{(a,1^b)}$ is labelled by a hook partition, Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} gives a combinatorial description of the value of $\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_n} \chi^{\lambda/ \mu}$ on an $n$-cycle. This result generalizes the case $\gamma=(n)$ of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and may be viewed as a simultaneous generalization of the Murnaghan--Nakayama rule and a special case of the Littlewood--Richardson rule. We also give an illustrative example showing how our methods can be used to compute values of deflated characters in the non-hook case.

Finally, in §[\[sec:concl\]](#sec:concl){reference-type="ref" reference="sec:concl"}, we discuss the aforementioned connections between Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and results in [@DLT; @Macdonald1995] stated in terms of symmetric functions.
