*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The nuclear binding energy of a derived atom $\mathcal{A}(Z, N)$
([derived atom](#def:derived-atom)) is determined by the brane
tower partition function evaluated on **all three** Wedderburn
channels of $H_3(q)$.

## Statement

**Proposition.**
*Let $\mathcal{A}(Z, N)$ be a derived atom with $A$ nucleons
and $A - 1$ generators in $H_A(q)$, with canonical Hecke element
$T_w = \mathtt{atom\_braid\_word\_3A}(Z, N) \in H_{3A}(q_0)$ in
Gröbner–Shirshov normal form
([def:atomic-braid](#def:atomic-braid),
[`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py)).
The per-generator vertex volumes $\hat{V}_i^\lambda$ below are read
off generator $i$ of $T_w$ in irrep $\lambda \in \{\mathrm{sym},
\mathrm{std}, \mathrm{alt}\}$.  For each generator $i$
and each irrep $\lambda$, let $\hat{V}_i^\lambda$ be the vertex volume
in channel $\lambda$, computed from the Garside staircase with
LP-derived gluon crossings
([integer LP gluon](#prop:mass-endomorphism-tower)):*

- *Symmetric: $\hat{V}_i^{\mathrm{sym}} = \prod_j (c_j q + d_j)$*
- *Standard: $\hat{V}_i^{\mathrm{std}} = z a_i + b_i$
  (transfer chain reduction)*
- *Alternating: $\hat{V}_i^{\mathrm{alt}} = \prod_j (-c_j q^{-1} + d_j)$*

*The brane tower at generator $i$ in channel $\lambda$ is*

$$
  \Phi_q(\hat{V}_i^\lambda)
  =
  \prod_{k=1}^{\infty}
  \bigl|1 - q^{-k} \hat{V}_i^\lambda\bigr|^{-1},
$$

*analytically continued past $|\hat{V}| = q$ via the absolute
value of the $q$-Pochhammer symbol.*

*The nuclear binding energy is*

$$
  B(Z, N)
  =
  \sum_{\lambda}
  w_\lambda \cdot m_e
  \cdot
  \sum_{i=0}^{A-2}
  \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|,
$$

*where $w_\lambda$ are the Wedderburn-Artin weights:
$w_{\mathrm{sym}} = w_{\mathrm{alt}} = 1/([2]_q^2 + 2)$,
$w_{\mathrm{std}} = [2]_q^2/([2]_q^2 + 2)$.*

*The atomic mass is then*

$$
  M(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  - B(Z, N).
$$

## Derivation

The binding energy arises from the gauge sector of the categorical
action ([canonical action](#prop:qou-canonical-action)):

$$
  \mathcal{S}_{\mathrm{gauge}}
  =
  \int_A \mathrm{tr}_A\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr).
$$

Under the Wedderburn-Artin decomposition of $H_3(q)$, the gauge
functional decomposes into three channels.  Although the
weights satisfy $w_{\mathrm{sym}} = w_{\mathrm{alt}}$, the
channels do **not** cancel in the binding: the nonlinearity
of $\ln|\Phi_q|$ breaks the character cancellation because
$\hat{V}^{\mathrm{sym}} \neq \hat{V}^{\mathrm{alt}}$.

Each channel contributes independently:

- **Symmetric** ($\sim 20\%$ of $B$): $\hat{V}^{\mathrm{sym}}
  = \prod (c_j q + d_j)$ grows with $A$, providing the volume
  binding baseline.
- **Standard** ($\sim 65\%$ of $B$): the $2{\times}2$ transfer
  chain $\hat{V}^{\mathrm{std}} = z a_i + b_i$ encodes the
  correlated structure between adjacent nucleons.
- **Alternating** ($\sim 15\%$ of $B$): $\hat{V}^{\mathrm{alt}}
  = \prod (-c_j q^{-1} + d_j)$ captures the Pauli exclusion
  and parity structure.

The $\Phi_q$ tower is analytically continued past
$|\hat{V}| = q$ via the $q$-Pochhammer functional equation,
taking $\ln|\Phi_q| = -\sum_k \ln|1 - q^{-k}\hat{V}|$.
This is well-defined for all $\hat{V} \neq q^n$ ($n$ integer).

The coefficients $w_\lambda \cdot m_e$ are the natural
normalization: $w_\lambda$ weights each channel relative to
the full regular representation, and $m_e$ converts the
dimensionless partition function to physical energy.

## Numerical results

At $q_0 \approx 1.110$, see
[Table: Predicted vs observed binding energies for $Z = 1$ to $20$](#tbl:tower-binding-energy-table-data).

Zero fitted parameters.  Mean mass error: $0.071\%$ across
$Z = 1$ to $Z = 20$.  All coefficients derived from $q_0$
and $m_e$.

**Witness**: `full-tower-mass.witness.json`.
