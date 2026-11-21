---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-026-7-mirrors-to-divisor-complements
section_title: "Mirrors to divisor complements"
section_number: 7
pages: 63-64
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.823
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:complements label="sec:complements"}

In this section we examine the relationship between the wrapped Floer cohomology of our Lagrangians $L(d)$ and the cohomology of coherent sheaves on complements of components of the anticanonical divisor in $\CP^2$. Let $D = C \cup L$ denote the anticanonical divisor which is the union of a conic $C$ and a line $L$. We can consider the divisor complements $U_D =\CP^2 \setminus D$, $U_C = \CP^2 \setminus
C$, and $U_L = \CP^2 \setminus L$. The torus fibration $\CP^2
\setminus D$ can be restricted to such a complement, and T-duality gives the same space $X^\vee$ as before, but with a different superpotential, reflecting the counts of holomorphic disks intersecting the remaining components of the anticanonical divisor.

::: {#tab:divisor-complements}
  Variety                     Anticanonical divisor     Mirror space                         Superpotential
  --------------------------- ------------------------- ------------------------------------ -----------------------------------------
  $\CP^2$                     $D = C \cup L$            $X^\vee = \{(u,v) \mid uv\neq 1\}$   $W
                                                                                                 = u + \frac{e^{-\Lambda}v^2}{uv-1}$
  $U_L = \CP^2 \setminus L$   $C \setminus (C\cap L)$   $X^\vee$                             $W_L =
                                                                                                 u$
  $U_C = \CP^2 \setminus C$   $L \setminus (L\cap C)$   $X^\vee$                             $W_C =
                                                                                                 \frac{e^{-\Lambda}v^2}{uv-1}$
  $U_D = \CP^2 \setminus D$   $\emptyset$               $X^\vee$                             $W_D = 0$

  : Mirrors to divisor complements.
:::

Once again, the cohomology of coherent sheaves $\cO(d)$ corresponds to Floer cohomology of the Lagrangian submanifolds $L(d)$.

Removing a divisor $D$ from a compact variety $X$ changes the cohomology of a coherent sheaf $\cF$, since, for example, sections of $\cF$ with poles along $D$ are regular on the complement $U=X\setminus D$, so that $H^0(U,\cF)$ is not finitely generated in general.

On the symplectic side, changing the superpotential by dropping a term modifies the boundary condition for our Lagrangian submanifolds $L(d)$. Some parts of $L(d)$ that were required to lie on the fiber of $W$ are no longer so constrained, and it is appropriate to *wrap* these parts of $L(d)$. The algebraic structure associated to $L(d)$ is then *wrapped Floer cohomology* $HW^*(L(d_1),L(d_2))$, which is the limit $\lim_{w\to \infty} HF^*(\phi_{wH}(L(d_1)),L(d_2))$, where $H$ is an appropriate Hamiltonian function (a more precise definition is given below). The limit $HW^*(L(d_1),L(d_2))$ will not be finitely generated in general, since it potentially contains trajectories of $H$ joining $L(d_1)$ to $L(d_2)$ of *any* length. The general theory of wrapped Floer cohomology is developed in [@as-open-string].
