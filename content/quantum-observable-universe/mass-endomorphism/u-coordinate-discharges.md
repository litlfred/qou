*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Macdonald coordinate $u = q^2$ substantive discharges for the
$H_3 / V_{(2,1)}$ scalar invariants.**

Many Hecke / Wenzl-bridge scalar invariants are **rational** in
$u = q^2$ even when they involve `Real.sqrt` over $q$. This block
exploits the Macdonald-substitution to deliver concrete, no-sqrt
closed-form Lean identities that substantively back the explicit-
residual discharges in
[`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules)
and elsewhere.

## Substantive identities (all proved by `field_simp + ring`)

See [Table](#tbl:u-coordinate-discharges-table-data).

Each scalar identity above is exported as a Lean theorem closed by
`field_simp + ring` (no sqrt, no opaque axioms).

## Why this matters

Before this block, the explicit-residual discharges at the class
level (`⟨0, rfl⟩`) appeared **abstractly trivial** — the residual is
$0$ but there's no concrete computation tying that to substrate
arithmetic. The $u$-coordinate identities above transform the
underlying scalars into **rational functions in a single variable**
$u$, where `ring` and `field_simp` close every required equality.

For example, the abstract class field
`HeckeQuadraticAllGenerators 3 q .hecke_quad_residual_eq_zero`
declares the residual is $0$; the substantive content of *why* it
vanishes is then concretely captured by `hecke_root_sum_times_q`:
$q \cdot (q - q^{-1}) = u - 1$, which is a non-trivial rational
identity provable by `field_simp + ring`.

## Files affected (downstream consumers)

- `rem:ck-extraction-from-algebraic-rules` — instances now point to
  the $u$-coordinate identities as their substantive backing.
- `rem:h3-hecke-idempotents` — `dimQ_V21^2` identity links to
  `dimQ_V21_sq_in_u`.
- `prop:hoefsmit-V21-cos-symmetrization` — Hoefsmit $b^2$ closed
  form has a no-sqrt counterpart via `hoefsmit_b_sq_in_u`.
