---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-007-32-uξ-modules
section_title: "Uξ-modules."
section_number: 3.2
pages: 6-6
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.969
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
We say a $\mathcal{U}_\xi$ module $V$ has character $\chi \in \slg^*$ if $$z \cdot v = \chi(z) v \text{ for all } v \in V, z \in \mathcal{Z}_0.$$ In particular any simple $\mathcal{U}_\xi$-module has a character. Because the multiplication on characters is compatible with the coproduct the category of $\mathcal{U}_\xi$-modules with characters is graded by $\slg^*$: if $V_1, V_2$ have characters $\chi_1, \chi_2$, then $V_1 \otimes V_2$ has character $\chi_1 \cdot \chi_2$.

A character $\hat \chi : \mathcal{Z}\to \mathbb{C}$ on the full center extending some $\chi \in \slg^*$ is specified by a solution of the equation $$\hat \chi(P_N(\Omega)) = \chi(E^N F^N - (K^N + K^{-N}))
  =
  - \mathop{\mathrm{tr}}\psi(\chi)$$ If the eigenvalues of $\psi(\chi)$ are $m, m^{-1}$, then the Casimir will satisfy $$\hat \chi(\Omega) = \xi^{2\mu + 1} + \xi^{-(2\mu-1)}$$ for some $\mu$ with $\xi^{2\mu} =\omega^{\mu} = m$. For the modules used in this paper ([\[def:standard-rep\]](#def:standard-rep){reference-type="ref" reference="def:standard-rep"}) the choice of $\chi$ and $\mu$ completely determines the isomorphism class of a simple module, so the choice of $\mu$ is analogous to the choice of a highest weight.

However, unlike for ordinary $\mathcal{U}_q$-modules $\mu$ may not be a highest weight, or even a weight at all. Whenever the character of $V$ has $\chi(E^N), \chi(F^N) \ne 0$ the generators $E$ and $F$ act invertibly on $V$. We call such modules , and in this case $\xi^{2\mu}$ will *not* be an eigenvalue of $K$. While one can still consider a weight basis for $V$ by diagonalizing $K$ there is no canonical way to choose a *highest* weight because $E$ does not have a kernel. We will give an explicit description of some cyclic modules in [\[sec:cyclic-reps\]](#sec:cyclic-reps){reference-type="ref" reference="sec:cyclic-reps"}.
