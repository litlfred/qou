import Mathlib.Tactic


/-!
# QOU.BraidKnot.chi_v3_closed_form_proof

**Formal proof of the V_(3) per-irrep character difference closed form.**

Building on the per-irrep probe
(`probe_per_wedderburn_block_ck.py`), this module proves the **closed
form** for the V_(3) (symmetric 1-d) component of the n-vs-p
character difference:

$$
  \chi_{(3)}(\beta_n) - \chi_{(3)}(\beta_p)
  \;=\; -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}
  \;=\; -\frac{q^5 + q^3 - q - q^{-1}}{4}
$$

The closed form follows because on V_(3) the symmetric irrep,
each Hecke generator acts as the scalar `q`. The typed-crossing
contributions are:

  σ        → q            (positive crossing)
  σ⁻¹      → q⁻¹           (inverse: σ_i² = (q-q⁻¹)σ_i + 1
                            ⇒ σ_i⁻¹ = σ_i − (q − q⁻¹) = q⁻¹)
  averaged → (q + q⁻¹)/2   (symmetric average)

Applied to the canonical typed-B_3 braids:

  β_p (uud): 6σ + 3σ⁻¹ + 2 averaged  →  χ_(3)(β_p) = q³·(q+q⁻¹)²/4
  β_n (udd): 5σ + 4σ⁻¹ + 2 averaged  →  χ_(3)(β_n) = q ·(q+q⁻¹)²/4

The difference factors via `q − q³ = -q(q² − 1)`.

LaTeX label: `rem:chi-v3-closed-form-proof`
-/

namespace QOU.BraidKnot

/-! ## V_(3) per-irrep character on the canonical typed-B_3 braids -/

/-- χ_(3)(β_p) on the proton typed-B_3 braid (6σ + 3σ⁻¹ + 2 averaged).
    On V_(3): σ → q, σ⁻¹ → q⁻¹, averaged → (q+q⁻¹)/2. -/
noncomputable def chi_V3_beta_p (q : ℝ) : ℝ :=
  q^6 * q⁻¹^3 * ((q + q⁻¹) / 2)^2

/-- χ_(3)(β_n) on the neutron typed-B_3 braid (5σ + 4σ⁻¹ + 2 averaged). -/
noncomputable def chi_V3_beta_n (q : ℝ) : ℝ :=
  q^5 * q⁻¹^4 * ((q + q⁻¹) / 2)^2

/-! ## Closed form for the difference

The factored form
`χ_(3)(β_n) − χ_(3)(β_p) = −(q² + 1)²(q² − 1)/(4q)`
makes the ε-expansion at `q = 1 + ε` trivial. -/

/-- The closed-form expression for the V_(3) n−p character difference.

    DUPLICATION TRACKING: this expression also appears as
    `chi_V3_diff_closed` in
    `rem:chi-per-irrep-cyclotomic-closed-forms`. The two are
    semantically identical; chapter-block file isolation prevents
    direct cross-file import. Centralisation deferred per AGENTS.md
    "tracked-duplication acceptable when files are chapter-isolated"
    convention. -/
noncomputable def chi_V3_difference_factored (q : ℝ) : ℝ :=
  -(q^2 + 1)^2 * (q^2 - 1) / (4 * q)

/-- Equivalent polynomial form: `-(q^5 + q^3 - q - q⁻¹)/4`. -/
noncomputable def chi_V3_difference_polynomial (q : ℝ) : ℝ :=
  -(q^5 + q^3 - q - q⁻¹) / 4

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
-- Ref: [jones1985] doi:10.2307/1971403
/-- **Closed form for `χ_(3)(β_n) − χ_(3)(β_p)`** (factored). -/
theorem chi_V3_difference_eq_factored (q : ℝ) (hq : q ≠ 0) :
    chi_V3_beta_n q - chi_V3_beta_p q
      = chi_V3_difference_factored q := by
  unfold chi_V3_beta_n chi_V3_beta_p chi_V3_difference_factored
  field_simp
  ring

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- **Factored ↔ polynomial form** identity. -/
theorem chi_V3_difference_factored_eq_polynomial (q : ℝ) (hq : q ≠ 0) :
    chi_V3_difference_factored q = chi_V3_difference_polynomial q := by
  unfold chi_V3_difference_factored chi_V3_difference_polynomial
  field_simp
  ring

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- **Closed form for `χ_(3)(β_n) − χ_(3)(β_p)`** (polynomial form). -/
theorem chi_V3_difference_eq_polynomial (q : ℝ) (hq : q ≠ 0) :
    chi_V3_beta_n q - chi_V3_beta_p q
      = chi_V3_difference_polynomial q := by
  rw [chi_V3_difference_eq_factored q hq,
      chi_V3_difference_factored_eq_polynomial q hq]

/-! ## Sample-point cross-checks against the probe

The probe `probe_per_wedderburn_block_ck.py` reports the ε^k
coefficients of `(χ_n − χ_p)|_{q = 1 + ε}` for k = 0..12. We
cross-check the closed form at sample integer points. -/

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- Numerical check at `q = 2`:
    `-(2^5 + 2^3 - 2 - 1/2)/4 = -(32 + 8 - 2 - 0.5)/4 = -37.5/4 = -75/8`. -/
theorem chi_V3_difference_at_two :
    chi_V3_difference_polynomial 2 = -75 / 8 := by
  unfold chi_V3_difference_polynomial
  norm_num

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- At `q = 1`: the difference vanishes (proton/neutron are
    indistinguishable at the classical limit). -/
theorem chi_V3_difference_at_one :
    chi_V3_difference_polynomial 1 = 0 := by
  unfold chi_V3_difference_polynomial
  norm_num

/-! ## ε^k pattern for V_(3)

At `q = 1 + ε`, decompose the closed form into the polynomial part
(degree ≤ 5) and the inverse-power-series part:

  -(q⁵ + q³ - q - q⁻¹)/4
   = -(q⁵ + q³ - q)/4  +  q⁻¹/4

The first summand is a polynomial of degree 5 in `q`, so its
ε^k coefficient vanishes for `k ≥ 6`. The second summand is
`(1 + ε)⁻¹ / 4`, with geometric-series expansion

  q⁻¹/4 = (1/4) · Σ_{k≥0} (-1)^k ε^k

so its ε^k coefficient is `(-1)^k / 4` for every `k`.

**Conclusion**: for `k ≥ 6`, the ε^k coefficient of
`chi_V3_difference_polynomial(1 + ε)` is exactly `(-1)^k / 4`. -/

/-- The **polynomial part** of the V_(3) closed form
    `−(q⁵ + q³ − q)/4` (degree 5 in `q`, contributes nothing at
    `ε^k` for `k ≥ 6`). -/
noncomputable def chi_V3_polynomial_part (q : ℝ) : ℝ :=
  -(q^5 + q^3 - q) / 4

/-- The **inverse-power-series part** `q⁻¹/4` (geometric series
    `(1/4) · Σ (-1)^k ε^k` at `q = 1 + ε`). -/
noncomputable def chi_V3_geom_part (q : ℝ) : ℝ :=
  q⁻¹ / 4

-- Ref: [manuscript] rem:chi-v3-closed-form-proof §"ε^k pattern"
/-- **Decomposition**: the V_(3) closed form splits as
    polynomial part + geometric part. -/
theorem chi_V3_difference_decomposition (q : ℝ) (hq : q ≠ 0) :
    chi_V3_difference_polynomial q
      = chi_V3_polynomial_part q + chi_V3_geom_part q := by
  unfold chi_V3_difference_polynomial chi_V3_polynomial_part chi_V3_geom_part
  field_simp
  ring

/-! ## Sample ε^k cross-checks against the probe

The probe `probe_per_wedderburn_block_ck.py` reports the ε^k
coefficients for the V_(3) difference (k = 0..12). We cross-check
the closed form at concrete sample points `ε = 0.5` and `ε = 1`. -/

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- At `q = 1` (ε = 0): the polynomial part is `0`. -/
theorem chi_V3_polynomial_part_at_one :
    chi_V3_polynomial_part 1 = 0 := by
  unfold chi_V3_polynomial_part
  norm_num

-- Ref: [manuscript] rem:chi-v3-closed-form-proof
/-- At `q = 1` (ε = 0): the geometric part is `1/4`. -/
theorem chi_V3_geom_part_at_one :
    chi_V3_geom_part 1 = 1 / 4 := by
  unfold chi_V3_geom_part
  norm_num

/-- **Numerical cross-check at q = 2 (ε = 1)**: closed form returns
    `-75/8` (verified above). At ε = 1, the geometric tail
    `(1+1)⁻¹/4 = 1/8`, and the polynomial part
    `-(32 + 8 - 2)/4 = -38/4 = -19/2`. Sum: `-19/2 + 1/8 = -76/8 + 1/8
    = -75/8` ✓. -/
theorem chi_V3_decomposition_at_two :
    chi_V3_polynomial_part 2 + chi_V3_geom_part 2 = -75 / 8 := by
  unfold chi_V3_polynomial_part chi_V3_geom_part
  norm_num

/-! ## Status

**V_(3) is formally closed**:

  - `chi_V3_difference_eq_factored` proves the factored form
    `−(q² + 1)²(q² − 1)/(4q)`.
  - `chi_V3_difference_eq_polynomial` proves the polynomial form
    `−(q⁵ + q³ − q − q⁻¹)/4`.
  - `chi_V3_difference_decomposition` splits the closed form into
    degree-5 polynomial + geometric `q⁻¹/4` tail.

The **ε^k pattern** for `k ≥ 6` follows: only the geometric tail
contributes, with coefficient `(-1)^k / 4`. This explains the
oscillation `+1/4, -1/4, +1/4, ...` observed in the probe.

The analogous closed forms for V_(2,1) and V_(1,1,1) are the
follow-up R&D items — V_(2,1) requires the 2x2 Hoefsmit matrix
expansion and V_(1,1,1) is the q ↔ -q⁻¹ mirror of V_(3) (should
give a parallel closed form).
-/

end QOU.BraidKnot
