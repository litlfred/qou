---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-016-51-abel-jacobi-and-the-riemann-constant-vector
section_title: "Abel-Jacobi and the Riemann Constant Vector"
section_number: 5.1
pages: 31-31
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 1.0
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: AJ and RCV label="subsec: AJ and RCV"} We will now take a detour to lay out some notation and definitions in preparation for later.

::: definition
[]{#def: AJ map and RCV label="def: AJ map and RCV"} The **Abel-Jacobi map** on a Riemann surface $\mathcal{C}$ with basis of differentials $\left\{ \omega_j \right\}$, based at $Q \in \mathcal{C}$, is given by $$(\mathcal{A}_Q(P))_j = \int_Q^P \omega_j  .$$ This is well defined up to periods on the curve. Letting $\tau$ be the Riemann matrix of $\mathcal{C}$, the **Riemann Constant Vector (RCV)** based at $Q$ is given by $$(K_Q)_j = -\frac{1+\tau_{jj}}{2} + \sum_{k \neq j}^g \oint_{a_k} \omega_k(P) (\mathcal{A}_Q(P))_j  .$$
:::

The RCV is related to the canonical divisor by $2K_Q\equiv\mathcal{A}_Q(\mathcal{K}_\mathcal{C})$. Indeed, [@Deconinck2015] shows how to find $K_Q$ from this relation given the theta function. We then have the following theorem about the divisor of the Szëgo kernel $\Delta_S$, defined in [@Fay1973].

::: theorem
$K_Q = \mathcal{A}_Q(\Delta_S)$, and as such $\Delta_S$ is a theta characteristic.
:::

The definition of the RCV also requires that the differentials are normalised with respect to the homology basis taken $\left\{ a_j , b_j \right\}$ such that $\oint_{a_j} \omega_i = \delta_{ij}$. As such hidden in the above result is the fact that the Szëgo kernel divisor is homology dependent, because the RCV is.
