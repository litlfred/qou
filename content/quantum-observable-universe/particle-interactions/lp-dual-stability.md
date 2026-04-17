An element $x \in H_3(q)$ with NF decomposition
$x = \sum_{i=1}^{6} x_i b_i$ is classified by two LP criteria.

**Definition (LP-stable).**
$x$ is *LP-stable* if $Gx \geq 0$ (component-wise), where $G$ is
the Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$.

**Definition (LP-confined).**
$x$ is *LP-confined* if $x$ is LP-stable and no proper sub-braid
(obtained by removing one or more generators from the braid word)
is LP-stable.

**Proposition (LP dual stability of confined hadrons).**
*Let $x^*$ be a confined hadron (proton or neutron, built via
$B_3 \cdot \Phi_{\mathrm{quarks}}$). Then:*

1. *$x^*$ is LP-stable: $Gx^* \geq 0$ in all six channels.*

2. *The dual shadow prices $y_i^*$ are bounded:
   $|y_i^*| \leq \kappa(G) \cdot \|t\|$ where
   $\kappa(G) \approx 7.0$ is the condition number.*

3. *The $B_3$ sub-braid $\sigma_0\sigma_1^{-1}$ is LP-unstable:
   $G\vec{x}$ has a negative $\sigma_0$ component $\approx -0.106$.
   This means partial confinement (1 of 3 $B_3$ units) is not
   sufficient --- all three units are required.*

4. *Strong duality holds: $\mathrm{tr}_M(x^*) = y_0^* \cdot
   n_{\mathrm{target}}$.*

**Verified values at $q_0 \approx 1.110$:**

| Element | $Gx$ components | LP-stable? | Min$(Gx)$ |
|---------|----------------|:----------:|----------:|
| Proton $(B_3 \cdot uud)$ | $(+0.44, +0.24, +1.10, +0.62, +0.13, +0.28)$ | **Yes** | $+0.13$ |
| Neutron $(B_3 \cdot udd)$ | $(+0.32, +0.20, +1.01, +0.48, +0.08, +0.21)$ | **Yes** | $+0.08$ |
| Up quark $\sigma_0$ | $(+0.50, +1.10, +0.25, +0.12, +0.55, +0.28)$ | **Yes** | $+0.12$ |
| Down quark $\sigma_0^{-1}$ | $(+0.29, +1.00, +0.14, +0.07, +0.50, +0.25)$ | **Yes** | $+0.07$ |
| $B_3$ sub-unit $\sigma_0\sigma_1^{-1}$ | $(+0.14, \mathbf{-0.11}, +0.50, +1.10, +0.16, +0.55)$ | **No** | $-0.11$ |
| $\sigma_0^2$ (Hopf) | $(+1.10, +0.73, +0.55, +0.28, +0.36, +0.18)$ | **Yes** | $+0.18$ |

**Key finding: individual quarks are LP-stable, but the $B_3$
sub-unit is not.**  This is the precise algebraic statement of
confinement: the gluon field ($B_3 = (\sigma_0\sigma_1^{-1})^3$)
contains an LP-unstable intermediate ($\sigma_0\sigma_1^{-1}$),
but the full 3-fold Borromean product restores stability.
Physically: the confinement mechanism is not that quarks are
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
