import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# A=4 pairwise saturation cap — the isospin-even log-det cumulant is capped at `C(4,2)=6`

Lands the Lean proof deferred (on disk-space) in
`docs/audits/2026-07-18-deltalambda-saturation-det-ceiling.md §3`.

**Context.** Nuclear binding in this framework needs an *additive extensive*
term (the trace binding `B = E₀·Δtr_M` is intensive — proved
`2026-06-02-binding-intensive-vs-extensive-derivation.md`). The candidate
extensive object is the **isospin-even log-det cumulant**
`b_A(m) = −ln det(I + m·(J−I)_A)`, whose determinant on the unsigned complete
graph `K_A` has the exact spectrum `{1+(A−1)m, (1−m)^{×(A−1)}}`, so
`det_A(m) = (1 + (A−1)m)·(1−m)^{A−1}` — in particular

  `det_2(m) = 1 − m²`,   `det_4(m) = (1+3m)(1−m)^3`.

The dimensionless magnitude ratio is `ρ_A(m) := b_A(m)/b_2(m)`.

**The cap (this file, A=4).** `ρ_A(m) ≤ C(A,2) = A(A−1)/2` for all `m ∈ (0,1)`.
For `A=4`, `C(4,2)=6`, and via `exp`-monotonicity the cap `b_4 ≤ 6·b_2` is
equivalent to the **determinant inequality**

  `det_2(m)^6 ≤ det_4(m)`,   i.e.   `(1−m²)^6 ≤ (1+3m)(1−m)^3`   on `[0,1]`,

which is `exchangeDet_pow_two_le_four` below, proved sorry-free.

**Why it matters (the exclusion).** The isospin-corrected *strong* target is
`ρ_strong(4) ≈ 13 > 6` (even the raw AME `ρ_4 = 12.72 > 6`), so the pairwise
isospin-even determinant cumulant **cannot** reach the strong magnitude for any
`m` — a scope-(b) structural exclusion whose cited invariant is the exact `K_A`
spectrum above. Consequence: the missing extensive term must be **super-pairwise**
(irreducibly ≥3-body), not a pairwise-exchange determinant.

**Certificate.** `(1+3m)(1−m)^3 − (1−m²)^6 = m^3(1−m)^3·S(m)` with
`S(m) = m^6+3m^5−8m^3−6m^2+6m+8`, and `S ≥ 0` on `[0,1]` by a Bernstein
certificate (all degree-6 Bernstein coefficients `= 8, 9, 48/5, 47/5, 8, 11/2, 4`
are `≥ 0`).

Base ring `ℝ` (§7c): the ordering `0 ≤ m ≤ 1` is archimedean-essential.

-- Ref: [manuscript] docs/audits/2026-07-18-deltalambda-saturation-det-ceiling.md §3
-/

namespace QOU.MassTheory

/-- **The A=4 pairwise saturation cap (determinant form).** On `[0,1]`,
    `det_2(m)^6 ≤ det_4(m)`, i.e. `(1−m²)^6 ≤ (1+3m)(1−m)^3`.

    Via `exp`-monotonicity this is exactly `b_4(m) ≤ 6·b_2(m)`, i.e.
    `ρ_4(m) ≤ C(4,2) = 6`: the isospin-even log-det cumulant's magnitude ratio
    is capped at the pairwise edge count `C(4,2)`.

    Proof: `det_4 − det_2^6 = m^3(1−m)^3·S(m)` with `S ≥ 0` on `[0,1]` by a
    nonnegative Bernstein expansion (all coeffs `≥ 0`). -/
theorem exchangeDet_pow_two_le_four (m : ℝ) (h0 : 0 ≤ m) (h1 : m ≤ 1) :
    (1 - m ^ 2) ^ 6 ≤ (1 + 3 * m) * (1 - m) ^ 3 := by
  have h1m : (0:ℝ) ≤ 1 - m := by linarith
  -- S(m) = m^6+3m^5−8m^3−6m^2+6m+8 ≥ 0 on [0,1] (Bernstein coeffs all ≥ 0)
  have hS : (0:ℝ) ≤ m ^ 6 + 3 * m ^ 5 - 8 * m ^ 3 - 6 * m ^ 2 + 6 * m + 8 := by
    nlinarith [mul_nonneg (pow_nonneg h0 0) (pow_nonneg h1m 6),
               mul_nonneg (pow_nonneg h0 1) (pow_nonneg h1m 5),
               mul_nonneg (pow_nonneg h0 2) (pow_nonneg h1m 4),
               mul_nonneg (pow_nonneg h0 3) (pow_nonneg h1m 3),
               mul_nonneg (pow_nonneg h0 4) (pow_nonneg h1m 2),
               mul_nonneg (pow_nonneg h0 5) (pow_nonneg h1m 1),
               mul_nonneg (pow_nonneg h0 6) (pow_nonneg h1m 0)]
  -- (1+3m)(1−m)^3 − (1−m^2)^6 = m^3(1−m)^3·S ≥ 0
  nlinarith [mul_nonneg (mul_nonneg (pow_nonneg h0 3) (pow_nonneg h1m 3)) hS]

end QOU.MassTheory
