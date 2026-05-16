**Hoefsmit $\rho_{(2,1)}(\sigma_0)$ eigenvalue identification (closed Lean proof).**

The Hoefsmit seminormal action of $\sigma_0$ on $V_{(2,1)}$ of $H_3(q)$ is
the explicit diagonal matrix

$$
  \rho_{(2,1)}(\sigma_0) \;=\;
   \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix} .
$$

Its eigenvalues are immediately $\{q,\, -q^{-1}\}$, with eigenvectors
$[1,0]^T$ and $[0,1]^T$ respectively. The matrix satisfies the
Hecke-quadratic identity

$$
  M^2 \;=\; (q - q^{-1}) M + I \;=\; h \cdot M + I .
$$

This is a purely arithmetic statement at the matrix level — no Hecke or
crystal-graph theory is needed for $\sigma_0$ alone.

## Lean proofs

The companion file [`hoefsmit-sigma0-eigenvalues.lean`](hoefsmit-sigma0-eigenvalues.lean)
proves all five claims with **no `sorry`s**:

1. `hoefsmit_sigma0_eigenvector_q`: $M \cdot [1,0]^T = q \cdot [1,0]^T$
2. `hoefsmit_sigma0_eigenvector_neg_qinv`: $M \cdot [0,1]^T = -q^{-1} \cdot [0,1]^T$
3. `hoefsmit_sigma0_trace`: $\mathrm{tr}(M) = q - q^{-1} = h$
4. `hoefsmit_sigma0_det`: $\det(M) = -1$ for $q \neq 0$
5. `hoefsmit_sigma0_hecke_quadratic_explicit`: $M^2 = h M + I$

All five close by `fin_cases + simp + field_simp + ring` after unfolding
the matrix definition.

The bundled export `hoefsmit_sigma0_eigenvalues` combines them.

## Partial discharge of `V21Eigenphase`

This DISCHARGES the **σ_0 component** of the `V21Eigenphase` class used
in [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization).
For the full `V21Eigenphase` discharge we still need:

- **σ_1 off-diagonal analysis**: the same eigenvalues $\{q, -q^{-1}\}$
  but with $b$-coupled eigenvectors (computed via the characteristic
  polynomial of $\rho_{(2,1)}(\sigma_1)$ — a quadratic with known
  discriminant by Hecke).
- **Single-wrap eigenphase identification**: the transfer matrix's
  eigenphase $\alpha = (z-1)h/2$ emerges from analysing $\sigma_0 \cdot \sigma_1$
  perturbed around $q = 1$.

The first is straightforward but requires care with the off-diagonal
$b$ entries. The second is research-level Hecke-seminormal work.

## Status

Lean stub: **closed**, no `sorry`s. Discharges the σ_0 component of
`V21Eigenphase` directly. The σ_1 component remains an open
discharge target, but the σ_0 portion is now fully formal.
