---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-008-33-the-braiding-on-characters
section_title: "The braiding on characters"
section_number: 3.3
pages: 6-7
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.987
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:braiding root of unity label="sec:braiding root of unity"} Next we describe how $\mathcal{R}$ gives an action of the braid group on $\mathcal{Z}_{0}$-characters. Set $Y = 1 + K_1^{-N} E_1^N F_2^N K_2^N \in \mathcal{Z}_0 \otimes \mathcal{Z}_0$. In the ring $\mathcal{U}_\xi^{\otimes 2}[Y^{-1}]$ the element $(1 - q^{-1} K_1^{-1} E_1 F_2 K_2)$ is invertible, so $\mathcal{R}$ induces a map $$\mathcal{R}:
  \mathcal{U}_\xi^{\otimes 2}
  \to
  \mathcal{U}_\xi^{\otimes 2}[Y^{-1}]$$ we continue to denote by $\mathcal{R}$. For characters $\chi_1, \chi_2$ the equation $$(\chi_{1'} \otimes \chi_{2'}) (\mathcal{R}(x)) = (\chi_1 \otimes \chi_2), \quad x \in \mathcal{U}_\xi^{2}$$ uniquely defines characters $\chi_{1'}, \chi_{2'}$ whenever $(\chi_1 \otimes \chi_2)(\mathcal{R}^{-1}(Y)) \ne 0$. (Later we will write out this condition explicitly for central $\mathcal{W}$-characters.) As such, we obtain a partially defined, invertible map $$B : \slg^* \times \slg^*  \to \slg^* \times \slg^*
  ,
  B(\chi_1, \chi_2) = (\chi_{2'}, \chi_{1'})$$ that satisfies the braid relation $$(B \times \mathop{\mathrm{id}})
  (\mathop{\mathrm{id}}\times B )
  (B \times \mathop{\mathrm{id}})
  =
  (\mathop{\mathrm{id}}\times B )
  (B \times \mathop{\mathrm{id}})
  (\mathop{\mathrm{id}}\times B )$$ on the subset of $(\slg^*)^{\times 3}$ for which each side is defined. Here by "partially defined" we mean that the domain $B$ is really a subset $(\slg^* \times \slg^*) \setminus \mathfrak{A}$ avoiding the singular pairs $\mathfrak{A}$ of characters discussed above. The braiding $B$ was first studied by @Weinstein1992.

The map $B$ is an example of a generically defined biquandle [@Blanchet2018 Section 6], which means that it makes sense to color tangle diagrams by elements of $\slg^*$ related by $B$ at the crossings. For example, $B$ satisfies a braid relation, so when modifying a diagram by a Reidemeister type 3 move the labellings can be compatibly modified. Geometrically these colorings can be understood as defining a (gauge class of) flat $\sla$ connections on the braid complement [@Kashaev2005; @Blanchet2018; @McPhailSnyder2022].
