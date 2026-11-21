---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-014-33-with-a-strong-magnetic-field
section_title: "With a strong magnetic field"
section_number: 3.3
pages: 16-16
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.99
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#SectBoundMF label="SectBoundMF"} The last regime we consider is the Ising model with a strong magnetic field, *i.e.* $h$ is bigger than some value $h_1>0$ ($h_1$ is to be determined later). The case of negative $h$ (smaller than $-h_1<0$) is obviously symmetric.

In this regime, there is also a well-known cluster expansion for the partition function [@Velenik Section 5.7]. Let us present it briefly.

Fix $\Lambda \subset \mathbb{Z}^d$ and consider the Ising model on $\Lambda$ with $+$ boundary conditions. We first write its partition function in a suitable form. For a subset $\Lambda^-$ of $\Lambda$, we denote $$\delta_e \Lambda^- = \{ \{i,j\} \in \mathcal{E}_\Lambda^b,\ i \in \Lambda^-,\, j \notin \Lambda^-\}.$$ Define also $\mathop{\mathrm{wt}}(\Lambda^-) = \exp(-2 \beta\, |\delta_e \Lambda^-| -2h|\Lambda^-|)$. Then we have:

::: lemma
With the above notation, $$Z^+_{\Lambda,\beta,h} = \exp \big( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| \big) 
  \left( \sum_{\Lambda^- \subseteq \Lambda} \mathop{\mathrm{wt}}(\Lambda^-) \right).$$ []{#lem:Z_MF label="lem:Z_MF"}
:::

::: proof
*Proof.* The proof is not difficult and can be found, *e.g.*, in [@Velenik Section 5.7]. It is important to note that the sum over $\Lambda^- \subseteq \Lambda$ corresponds to the sum over spin configurations in the definition of the partition function: the correspondence simply associates with a spin configuration the set $\Lambda^-$ of positions of its minus spins. ◻
:::

Let $A$ be a subset of $\Lambda$. It is straightforward to modify the argument to find a similar expression for the numerators of $\langle \sigma_A \rangle$ (as in [\[Sect:CE_LT\]](#Sect:CE_LT){reference-type="ref" reference="Sect:CE_LT"}) or of $\left\langle \exp\left(\sum_{i \in A} t_i \sigma_i \right) \right\rangle$ (as in [\[Sect:CE_HT\]](#Sect:CE_HT){reference-type="ref" reference="Sect:CE_HT"}). $$\begin{aligned}
  \sum_{\omega \in \Omega_\Lambda} \sigma_A(\omega) e^{-H^+_{\Lambda;\beta,h}(\omega)} &= \exp \big( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| \big)              
  \left( \sum_{\Lambda^- \subseteq \Lambda} (-1)^{|A \cap \Lambda^-|} \mathop{\mathrm{wt}}(\Lambda^-) \right).\label{eq:SA_MF}\\
    \sum_{\omega \in \Omega_\Lambda} \exp\left(\sum_{i \in A} t_i \sigma_i \right) &= 
e   \exp \left( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| + \sum_{i \in A} t_i \right)
    \, \left( \sum_{\Lambda^- \subseteq \Lambda} \left[\prod_{i \in A \cap \Lambda^-} \exp(-2t_i)\right] \mathop{\mathrm{wt}}(\Lambda^-) \right).
    \label{eq:MGF_MF}
\end{aligned}$$ A set $\Lambda^- \subseteq \Lambda$ can be seen as a subgraph of the lattice $\mathbb{Z}^d$. As such, it admits a unique decomposition as disjoint union of its connected components $\Lambda^-=S_1 \sqcup S_2 \sqcup \dots \sqcup S_r$. The weight $\mathop{\mathrm{wt}}$ behaves multiplicatively with respect to this decomposition $\mathop{\mathrm{wt}}(\Lambda^-)=\prod_{i=1}^r \mathop{\mathrm{wt}}(S_i)$; the same is true for the modified weights $(-1)^{|A \cap \Lambda^-|} \mathop{\mathrm{wt}}(\Lambda^-)$ and $\left[\prod_{i \in A \cap \Lambda^-} \exp(-2t_i)\right] \mathop{\mathrm{wt}}(\Lambda^-)$ which appear in [\[eq:SA_MF,eq:MGF_MF\]](#eq:SA_MF,eq:MGF_MF){reference-type="ref" reference="eq:SA_MF,eq:MGF_MF"} above. This enables us to use the technique of cluster expansion.

The convergence of this cluster expansion is proved for the partition function in [@Velenik Section 5.7]. The argument can be directly adapted to get a cluster expansion of the expression in [\[eq:SA_MF,eq:MGF_MF\]](#eq:SA_MF,eq:MGF_MF){reference-type="ref" reference="eq:SA_MF,eq:MGF_MF"} above. The same reasoning as in [\[Sect:CE_HT\]](#Sect:CE_HT){reference-type="ref" reference="Sect:CE_HT"} or in [\[Sect:CE_LT\]](#Sect:CE_LT){reference-type="ref" reference="Sect:CE_LT"} leads to similar bounds on joint cumulants, which proves [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"} in the strong magnetic field regime.
