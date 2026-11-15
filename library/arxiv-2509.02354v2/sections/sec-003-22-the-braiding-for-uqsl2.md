---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-003-22-the-braiding-for-uqsl2
section_title: "The braiding for Uq(sl2)"
section_number: 2.2
pages: 3-4
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.731
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:outer-R-matrix label="sec:outer-R-matrix"} The algebra $\mathcal{U}_q(\sla)$ is not quasitriangular. Instead it is *braided* [@Reshetikhin1995] which means there is an outer automorphism $$\mathcal{R}:  \mathop{\mathrm{Div}}(\mathcal{U}_q(\sla)^{\otimes 2}) \to \mathop{\mathrm{Div}}(\mathcal{U}_q(\sla)^{\otimes 2})$$ of the division ring of $\mathcal{U}_q(\sla)^{\otimes 2}$ which intertwines the coproduct and opposite coproduct $$\mathcal{R}(\Delta(x)) =  \Delta^{op}(x)$$ and satisfies hexagon identities $$\begin{aligned}
  
  (\Delta \otimes 1) \mathcal{R}(x \otimes y) &= \mathcal{R}_{13} \mathcal{R}_{23} (\Delta(x) \otimes y) \\
  
  (1 \otimes \Delta) \mathcal{R}(x \otimes y) &= \mathcal{R}_{13} \mathcal{R}_{12} (x \otimes \Delta(y))
\end{aligned}$$ that imply the Yang-Baxter equation. Here $\mathcal{R}_{ij}$ means that $\mathcal{R}$ acts on tensor factors $i$ and $j$. That is, for each $x, y \in \mathcal{U}_q$ one can write $$\mathcal{R}(x \otimes y) = \sum_k f_k \otimes g_k$$ for some $f_k, g_k \in \mathcal{U}_q$ and we define $$\mathcal{R}_{13}(x \otimes z \otimes y) = \sum_k f_k \otimes z \otimes g_k$$ and so on. The automorphism $\mathcal{R}$ is derived from the conjugation action of the universal $R$-matrix in the $h$-adic quantum group, $q = e^h$ [@Kashaev2004].

$\mathcal{R}$ acts on generators as $$\begin{aligned}
  \mathcal{R}(\Delta(x)) &= \Delta^{\operatorname{op}}(x), \ x \in \mathcal{U}_\xi \\
  \mathcal{R}(K_1) &= K_1 (1  - q^{-1} K_1^{-1} E_1 F_2 K_2 ) \\
  \mathcal{R}(E_1) &= E_1 K_2 \\
  \mathcal{R}(F_2) &= K_1^{-1} F_2
\end{aligned}$$ where we abbreviate $K_1 = K \otimes 1, E_2 = 1 \otimes E$, etc.

::: proposition
$\mathcal{R}$ acts on the remaining generators of $\mathcal{U}_q^{\otimes 2}$ by: $$\begin{aligned}
    \mathcal{R}(K_2) &= (1 - q^{-1} K_1^{-1} E_1 F_2 K_2)^{-1} K_2 \\
    \mathcal{R}(E_2) &= E_1 + K_1 E_2 - E_1 K_2^2 (1 - q K_1^{-1} E_1 F_2 K_2)^{-1} \\
    \mathcal{R}(F_1) &= F_1 K_2^{-1} + F_2 - K_1^{-2} F_2(1 - q K_1^{-1} E_1 F_2 K_2)^{-1}
  
\end{aligned}$$ and preserves Casimirs: $\mathcal{R}(\Omega_1) = \Omega_1, \mathcal{R}(\Omega_2) = \Omega_2.$
:::

These follow from computations like $$\mathcal{R}(1 \otimes K) = \mathcal{R}(K \otimes 1)^{-1} \mathcal{R}(K \otimes K) = \mathcal{R}(K \otimes 1)^{-1} K \otimes K$$ and $$\mathcal{R}(1 \otimes E) = \mathcal{R}(E \otimes K + 1 \otimes E - E \otimes K) = E \otimes 1 + K \otimes E - \mathcal{R}(E \otimes K).$$
