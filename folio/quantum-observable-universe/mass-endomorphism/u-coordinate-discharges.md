**Macdonald coordinate $u = q^2$ substantive discharges for $H_3 / V_{(2,1)}$ scalar invariants.**

Many scalar invariants in the Hecke and Wenzl-bridge algebras are rational in the Macdonald coordinate $u = q^2$, even when their defining formulas require `Real.sqrt` over $q$. We use this Macdonald substitution to eliminate square roots. This provides concrete, closed-form Lean identities that algebraically verify the explicit-residual discharges required in [$c_k$ extraction from four algebraic reduction rules (Yang-Baxter](#rem:ck-extraction-from-algebraic-rules) and related proofs.

## Substantive identities

See [Table](#tbl:u-coordinate-discharges-table-data).

We export each scalar identity as a Lean theorem. Because the substitution removes square roots, the `field_simp + ring` tactic closes every proof without opaque axioms.

## Significance

Previously, explicit-residual discharges at the class level (such as `⟨0, rfl⟩`) appeared abstractly trivial: the residual evaluates to $0$, but no concrete computation connects this to the underlying substrate arithmetic. The $u$-coordinate identities express the underlying scalars as rational functions in a single variable $u$. This enables `ring` and `field_simp` to verify the equalities mechanically.

For example, the abstract class field `HeckeQuadraticAllGenerators 3 q .hecke_quad_residual_eq_zero` mandates that the residual vanishes. The substantive reason for this vanishing lies in the identity `hecke_root_sum_times_q`: the relation $q \cdot (q - q^{-1}) = u - 1$ constitutes a non-trivial rational identity closed by `field_simp + ring`.

## Downstream dependencies

These $u$-coordinate identities act as the computational backing for several downstream files:

- `rem:ck-extraction-from-algebraic-rules` references these identities to justify its instances.
- `rem:h3-hecke-idempotents` links its `dimQ_V21^2` computation to `dimQ_V21_sq_in_u`.
- `prop:hoefsmit-V21-cos-symmetrization` establishes a no-sqrt closed form for the Hoefsmit coupling $b^2$ via `hoefsmit_b_sq_in_u`.
