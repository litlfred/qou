**Proposition (universal residue at curvature-rank $k \geq 4$).**
*Define the **curvature-rank-$k$ residue functional***

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|,
  \qquad \tilde w_\lambda \;=\; \frac{\dim_q^2 V_\lambda}{[n]_q!},
$$

*where $A = H_n(R, q)$, $A_\lambda = e_\lambda A e_\lambda$ is the
Wedderburn block, $\beta_\mathcal{K}$ is a braid representative of the
knot $\mathcal{K}$, $\mathcal{T} \in A$ is a test element, and
$\mathrm{depth}(\lambda) = \mathrm{height}(\lambda) - 1$ is the
curvature-rank ([curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
The symbol $\tilde w_\lambda$ denotes the **q-deformed
Wedderburn-block weight** — distinct from the classical Plancherel
measure $w_\lambda = (\dim V_\lambda)^2/n!$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
which it specialises to at $q = 1$. The **universal residue** is the
high-tower contribution:*

$$
  \boxed{\;
    \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
    \qquad \alpha \;=\; m_e \cdot 8G.
  \;}
$$

*This is the algebraic content of what older drafts called "Term 7":
deep-tower strata where no specific hyperbolic-knot ideal appears, only
the universal Frobenius co-Casimir tail.*

**Universality at $k \geq 4$.** *At low strata $k \leq 3$ the
restricted Frobenius integral $\int_{A_\lambda} \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
factors through specific hyperbolic-knot ideals (specifically $4_1$
at $k = 3$ — the chirality channel via Fricke-trace derivation, empirically
resolved by ; see
[chirality residue](#prop:chirality-from-frobenius-self-pairing) for
the derivation).
At $k \geq 4$ no specific knot ideal remains in the centre — what
survives is the dualizing-complex residue, which depends only on
$(\mathcal{K}, \mathcal{T})$ and the Wedderburn-stratification
data, not on a distinguished knot.*
