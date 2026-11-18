import Mathlib.Tactic

/-!
# Route C step 2 — the pivotal Markov parameter against the count-shaped one

Bean `qou-8uxw` (route C of the binding-gap survey,
`docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md` §7d).
Route C step 1 showed the order-zero cross term is a Burnside fixed-point count.
Step 2 asks whether the framework's *q*-deformation of that count is itself an
unweighted count (a groupoid cardinality in the Baez–Hoffnung–Walker sense).

On the spin-½ tensor space `V^{⊗n}` with the §7a R-matrix (eigenvalues `q` on
`Sym²`, `−q⁻¹` on `Λ²`) there are two natural normalised traces of a single
crossing:

* the **pivotal** one, `K = diag(q, q⁻¹)` inserted on every strand — the
  framework's convention D, `zD q = q³ / (q² + 1)`;
* the **ordinary** one, no weight — the count-shaped reading,
  `zJ q = (3q − q⁻¹) / 4`.

This file carries the three algebraic facts the probe
`computations/probes/route_c_step2_pivotal_vs_count_probe.py` measures, stated
over a generic field so nothing archimedean enters:

1. `zJ_sub_zD` — the exact difference `zJ − zD = −(q² − 1)² / (4q(q² + 1))`, so
   the two agree at `q = 1` **and to first order** (double root) and split at
   second order;
2. `zJ_eq_zD_iff` — they coincide iff `q² = 1`;
3. `ordinary_partial_trace_scalar_iff` — the mechanism: the unweighted partial
   trace of the R-matrix over the closed strand is `diag(2q − q⁻¹, q)`, and
   that is scalar iff `q² = 1`.  A trace on `V^{⊗n}` is a Markov trace iff
   that partial trace is scalar, so the ordinary trace is not a Markov trace
   away from `q = ±1` — the framework's q-count is the K-weighted count.

The partial-trace matrix itself is computed in the probe (it is a 2×2
calculation); what is proved here is the scalar-iff-`q² = 1` step, which is the
step a numerical evaluation at one `q` cannot establish.

Base ring: a generic `Field K` with `(4 : K) ≠ 0`; the two hypotheses
`q ≠ 0` and `q² + 1 ≠ 0` are exactly the denominators.  No `ℝ`.
-/

namespace QOU.Mass.RouteCPivotalVsCount

variable {K : Type*} [Field K]

/-- Convention-D (pivotal) Markov parameter on spin-½: `q³ / (q² + 1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Ordinary-trace (count-shaped) Markov parameter on spin-½: `(3q − q⁻¹) / 4`. -/
def zJ (q : K) : K := (3 * q - q⁻¹) / 4

/-- The exact difference: a double root at `q = 1` (and at `q = −1`), so the two
parameters share value and slope there and part at second order. -/
theorem zJ_sub_zD (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h4 : (4 : K) ≠ 0) :
    zJ q - zD q = -((q ^ 2 - 1) ^ 2) / (4 * q * (q ^ 2 + 1)) := by
  unfold zJ zD
  field_simp
  ring

/-- Both parameters are `1/2` at `q = 1`. -/
theorem zD_one : zD (1 : K) = 1 / 2 := by
  unfold zD; norm_num

theorem zJ_one (h2 : (2 : K) ≠ 0) (h4 : (4 : K) ≠ 0) : zJ (1 : K) = 1 / 2 := by
  unfold zJ
  rw [inv_one, div_eq_div_iff h4 h2]
  norm_num

/-- The two parameters coincide iff `q² = 1`. -/
theorem zJ_eq_zD_iff (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h4 : (4 : K) ≠ 0) :
    zJ q = zD q ↔ q ^ 2 = 1 := by
  rw [← sub_eq_zero, zJ_sub_zD q hq hq2 h4]
  have hden : (4 * q * (q ^ 2 + 1)) ≠ 0 := by
    apply mul_ne_zero (mul_ne_zero h4 hq) hq2
  constructor
  · intro h
    have : -((q ^ 2 - 1) ^ 2) = 0 := by
      rcases div_eq_zero_iff.mp h with h' | h'
      · exact h'
      · exact absurd h' hden
    have h0 : (q ^ 2 - 1) ^ 2 = 0 := by linear_combination -this
    exact sub_eq_zero.mp (pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h0)
  · intro h
    rw [h]; simp

/-- The unweighted partial trace of the R-matrix over the closed strand is
`diag(2q − q⁻¹, q)` (computed in the probe); it is scalar iff its two diagonal
entries agree, i.e. iff `q² = 1`.  This is the step that makes the ordinary
trace fail the Markov property away from `q = ±1`. -/
theorem ordinary_partial_trace_scalar_iff (q : K) (hq : q ≠ 0) :
    2 * q - q⁻¹ = q ↔ q ^ 2 = 1 := by
  constructor
  · intro h
    have h' : q = q⁻¹ := by linear_combination h
    have : q * q = 1 := by
      calc q * q = q * q⁻¹ := by rw [← h']
        _ = 1 := mul_inv_cancel₀ hq
    simpa [sq] using this
  · intro h
    have hinv : q⁻¹ = q := by
      have : q * q = 1 := by simpa [sq] using h
      calc q⁻¹ = q⁻¹ * (q * q) := by rw [this, mul_one]
        _ = q := by field_simp
    rw [hinv]; ring

/-- At `q = 1`, the difference between the two parameters vanishes. -/
theorem zJ_sub_zD_at_one (h2 : (2 : K) ≠ 0) (h4 : (4 : K) ≠ 0) :
    zJ (1 : K) - zD (1 : K) = 0 := by
  rw [zJ_one h2 h4, zD_one, sub_self]

end QOU.Mass.RouteCPivotalVsCount
