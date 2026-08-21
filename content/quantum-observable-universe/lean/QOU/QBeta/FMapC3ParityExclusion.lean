import Mathlib.Tactic

/-!
# Bar-parity exclusion of a bar-odd derivation of `c₃ = J_Hopf(1) = −2`

Bean `qou-cds1` (f-map attack). Three feasibility probes tried to DERIVE the
c₃ identification `c₃ = J_Hopf(1) = −2` from the convention-D two-row Markov
trace: route A (the bar-odd crossing term), route B (the Z3 carrier `G·D`,
bar-even functional × bar-odd carrier), and the bar-even redirect. Routes A and
B both fail for the SAME reason, and it is a proved parity invariant, not a
numeric near-miss.

`c₃ = J_Hopf(1) = −2` is the value of the Hopf-link Jones polynomial
`−(q²+q⁻²)` at `q = 1` — a **bar-EVEN** quantity (`q ↦ q⁻¹` fixes `q²+q⁻²`),
value `−2 ≠ 0`. But every **bar-odd** construction vanishes at the bar fixed
point `q = 1`. So no bar-odd object — crossing term or Z3 carrier — can produce
the bar-even value `−2` there. This file formalises that invariant.

Symbolic cross-check (all 19 assertions, exact ℚ(q)):
`computations/qbeta/fmap_c3_parity_genericity_exclusion.py`. The bar-EVEN
channel fails separately, by genericity (scope-(a)) — `−2` at `q=1` is hit by
many bar-even combinations and none equals the full (non-bar-even) Hopf
polynomial — recorded in the probe and the audit, not here (it is not a proved
invariant). Sorry-free.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: docs/audits/2026-08-21-fmap-c3-parity-genericity-exclusion.md
-/

namespace QOU.QBeta

/-- The bar-odd part of a function of `q` under the bar involution `q ↦ q⁻¹`:
    `barOdd f q = (f q − f q⁻¹)/2`. -/
noncomputable def barOdd (f : ℝ → ℝ) (q : ℝ) : ℝ := (f q - f q⁻¹) / 2

/-- **Any bar-odd part vanishes at the bar fixed point `q = 1`.** Since
    `(1 : ℝ)⁻¹ = 1`, `barOdd f 1 = (f 1 − f 1)/2 = 0`. -/
@[simp] theorem barOdd_at_one (f : ℝ → ℝ) : barOdd f 1 = 0 := by
  unfold barOdd; rw [inv_one]; ring

/-- **Parity exclusion of the bar-odd routes to `c₃`.** The bar-odd content of
    any construction is `0` at `q = 1`, but the c₃ target — the Hopf-link Jones
    value at `q = 1` — is `−2 ≠ 0`. So `c₃ = J_Hopf(1) = −2` cannot be the
    bar-odd content of any object: it is a **bar-EVEN q=1 shadow**. This is the
    single invariant behind the refutation of both route A (crossing term) and
    route B (Z3 carrier); both are bar-odd, hence vanish here. -/
theorem barOdd_ne_hopf_value_at_one (f : ℝ → ℝ) : barOdd f 1 ≠ -2 := by
  rw [barOdd_at_one]; norm_num

/-- **The Hopf-link Jones value `−(q²+q⁻²)` is bar-EVEN**, so it is *not* an
    obstruction to the parity argument: it sits in the complementary channel to
    every bar-odd construction. (`bar` sends `q ↦ q⁻¹`; `q²+q⁻²` is fixed.) -/
theorem hopfValue_bar_even (q : ℝ) (hq : q ≠ 0) :
    (-(q ^ 2 + (q⁻¹) ^ 2)) = (-((q⁻¹) ^ 2 + ((q⁻¹)⁻¹) ^ 2)) := by
  rw [inv_inv]; ring

/-- The Hopf value at the classical point is `−2` (bar-even, nonzero). -/
theorem hopfValue_at_one : (-((1 : ℝ) ^ 2 + (1⁻¹) ^ 2)) = -2 := by
  norm_num

end QOU.QBeta
