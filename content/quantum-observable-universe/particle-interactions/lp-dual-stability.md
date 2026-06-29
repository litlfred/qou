An element $x \in H_3(q)$ with NF decomposition
$x = \sum_{i=1}^{6} x_i b_i$ is classified by the
[LP-stable](#def:lp-stable) and [LP-confined](#def:lp-confined)
criteria.

**Proposition (LP dual stability of confined hadrons).**
*Let $x^*$ be a confined hadron (proton or neutron, built via
$B_3 \cdot \Phi_{\mathrm{quarks}}$). Then:*

1. *$x^*$ is LP-stable: $Gx^* \geq 0$ in all six channels.*

2. *The dual shadow prices $y_i^*$ are bounded:
   $|y_i^*| \leq \kappa(G) \cdot \|t\|$ where
   $\kappa(G) \approx 7.0$ is the condition number.*

3. *The $B_3$ sub-braid $\sigma_0\sigma_1^{-1}$ is LP-unstable:
   $G\vec{x}$ has a negative $\sigma_0$ component $\approx -0.106$.
   Hence partial confinement (1 of 3 $B_3$ units) is not
   sufficient --- all three units are required.*

4. *Strong duality holds: $\mathrm{tr}_M(x^*) = y_0^* \cdot
   n_{\mathrm{target}}$.*

**Verified values at $q_0 \approx 1.110$:**

See [Table](#tbl:lp-dual-stability-table-data).

**Key finding: individual quarks are LP-stable, but the $B_3$
sub-unit is not.**  This is the precise algebraic statement of
confinement: the gluon field ($B_3 = (\sigma_0\sigma_1^{-1})^3$)
contains an LP-unstable intermediate ($\sigma_0\sigma_1^{-1}$),
but the full 3-fold Borromean product restores stability.
The confinement mechanism is not that quarks are
unstable, but that the **binding operator** requires a
topologically complete (Borromean) structure to be stable.

**Gram eigenvalues:**
$\lambda = (-0.956, +0.414, +0.428, +0.956, +1.282, +2.893)$.

The negative eigenvalue $\lambda_{\min} \approx -0.956$ is the
reason the LP has a global minimum at $\mathrm{tr}_M = 0$
(massless).  The braid group realizability constraint
prevents this --- braid words of length $L$ have NF
coefficients bounded by $O((1+|h|)^L)$, and the $\mathrm{tr}_M = 0$
solution requires unbounded coefficients.

**Witness:** `confinement-lp.witness.json`,
`confinement-operator-selection.witness.json`.
