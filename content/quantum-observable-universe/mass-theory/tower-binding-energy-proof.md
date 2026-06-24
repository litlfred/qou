The binding energy arises from the gauge sector of the categorical action
([canonical action](#prop:qou-canonical-action)):

$$
  \mathcal{S}_{\mathrm{gauge}}
  =
  \int_A \mathrm{tr}_A\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr).
$$

Under the Wedderburn–Artin decomposition of $H_3(q)$, the gauge functional
decomposes into three channels. Although the weights satisfy
$w_{\mathrm{sym}} = w_{\mathrm{alt}}$, the channels do **not** cancel in
the binding: the nonlinearity of $\ln|\Phi_q|$ breaks the character
cancellation because $\hat{V}^{\mathrm{sym}} \neq \hat{V}^{\mathrm{alt}}$.
Each channel contributes independently:

- **Symmetric** ($\sim 20\%$ of $B$): $\hat{V}^{\mathrm{sym}} = \prod (c_j q + d_j)$
  grows with $A$, providing the volume binding baseline.
- **Standard** ($\sim 65\%$ of $B$): the $2{\times}2$ transfer chain
  $\hat{V}^{\mathrm{std}} = z a_i + b_i$ encodes the correlated structure
  between adjacent nucleons.
- **Alternating** ($\sim 15\%$ of $B$): $\hat{V}^{\mathrm{alt}} = \prod (-c_j q^{-1} + d_j)$
  captures the Pauli exclusion and parity structure.

The $\Phi_q$ tower is analytically continued past $|\hat{V}| = q$ via the
$q$-Pochhammer functional equation, taking
$\ln|\Phi_q| = -\sum_k \ln|1 - q^{-k}\hat{V}|$, well-defined for all
$\hat{V} \neq q^n$ ($n$ integer).

The coefficients $w_\lambda \cdot m_e$ are the natural normalization:
$w_\lambda$ weights each channel relative to the full regular
representation (the weights sum to $1$ — Lean `wedderburnWeightsSum`, with
$w_{\mathrm{sym}} = w_{\mathrm{alt}}$ recorded by `wedderburnSymEqAlt`),
and $m_e$ converts the dimensionless partition function to physical energy.
The atomic mass $M(Z,N)$ then follows by adding the free-nucleon and
electron rest masses and subtracting $B$ (Lean `atomMass`). $\qquad\blacksquare$
