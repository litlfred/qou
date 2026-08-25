/-
# The `ρ = tr_M` radial binding-handle ansatz is refuted by the T/³He mirror test (scope-a)

After PR #4556 refuted a single-universal `C_knot` and PR #4592 refuted the angular (eigenphase) route,
the surviving compass is that the missing binding scale must be RADIAL: the mass formula runs on
`m = m_e·Vol(K)·ρ(K)/ℏ_q²` while the binding formula `B = m_e·|S(K)|` lacks that geometric dressing, so
the deficit `C_knot = B_AME/(m_e·|S(K)|)` might BE the missing `Vol·ρ/ℏ_q²` factor.

**Decisive mirror test.** Tritium (³H) and ³He are mirror nuclei (p↔n). IF they are also mirror knots
(`Vol(T) = Vol(³He)`), the radial ansatz forces `C_knot(T)/C_knot(³He) = ρ(T)/ρ(³He)` (Vol and ℏ_q²
cancel), with the paper-canonical per-block density `ρ(K) = tr_M(K) = Σ_λ y_λ χ^λ(β_K)`. The committed
χ witnesses give (0-fit): `C_knot(T)/C_knot(³He) ≈ 1.35` (T more bound, > 1) but
`ρ(T)/ρ(³He) = 0.104071/0.206578 ≈ 0.50` (< 1). The two ratios straddle unity, so they cannot be equal:
the ansatz is refuted **in direction**, not merely magnitude.

This file machine-checks the ratio identity and the resulting contradiction (sorry-free). **scope-(a)**:
this refutes the specific ansatz `ρ = tr_M` under `Vol(T)=Vol(³He)`. It does NOT exclude the radial
handle in general — the survivors are a density `ρ ≠ tr_M`, or genuinely distinct volumes
`Vol(T) ≠ Vol(³He)` (the two braids differ, `tr_M(T) ≠ tr_M(³He)`, so mirror-knot equality is an
assumption, not established). Nothing wired; no fit; the numeric literals consume the probe
`computations/deltalambda/radial_volrho_mirror_test_probe.py`.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.RadialVolRhoMirrorTest

variable {R : Type*} [Field R]

/-- **The radial ansatz forces the mirror ratio identity.** If `C_knot(K) = Vol·ρ(K)/h` with a COMMON
volume `Vol` and `h = ℏ_q²` (the shared geometric dressing), then `C_knot(T)/C_knot(³He) = ρ(T)/ρ(³He)`
— Vol and h cancel. (Generic field algebra; `V, h, rHe ≠ 0`.) -/
theorem mirror_ratio_of_radial {V h rT rHe cT cHe : R}
    (hV : V ≠ 0) (hh : h ≠ 0) (hRHe : rHe ≠ 0)
    (hcT : cT = V * rT / h) (hcHe : cHe = V * rHe / h) :
    cT / cHe = rT / rHe := by
  subst hcT hcHe
  field_simp

/-- **The witnessed ratios straddle unity.** `C_knot(T)/C_knot(³He) > 1` (T more bound) while the
per-block density ratio `ρ(T)/ρ(³He) = tr_M(T)/tr_M(³He) < 1` (T smaller trace). -/
theorem cknot_ratio_gt_one : (4.444 : ℝ) / 3.292 > 1 := by norm_num

theorem trM_ratio_lt_one : (0.104071 : ℝ) / 0.206578 < 1 := by norm_num

/-- **Mirror test refutes `ρ = tr_M` under equal Vol.** Assume the radial ansatz with a common volume:
`C_knot(T) = Vol·tr_M(T)/ℏ_q²` and `C_knot(³He) = Vol·tr_M(³He)/ℏ_q²` at the witnessed values. Then the
ratio identity forces `C_knot(T)/C_knot(³He) = tr_M(T)/tr_M(³He)`, but the former is `> 1` and the
latter `< 1` — contradiction. Hence no common `Vol, ℏ_q²` reproduce `C_knot` from `ρ = tr_M`. -/
theorem mirror_test_excludes_rho_trM {V h : ℝ} (hV : V ≠ 0) (hh : h ≠ 0)
    (hcT : (4.444 : ℝ) = V * 0.104071 / h)
    (hcHe : (3.292 : ℝ) = V * 0.206578 / h) : False := by
  have hRHe : (0.206578 : ℝ) ≠ 0 := by norm_num
  have key : (4.444 : ℝ) / 3.292 = 0.104071 / 0.206578 :=
    mirror_ratio_of_radial hV hh hRHe hcT hcHe
  have h1 : (4.444 : ℝ) / 3.292 > 1 := cknot_ratio_gt_one
  have h2 : (0.104071 : ℝ) / 0.206578 < 1 := trM_ratio_lt_one
  rw [key] at h1
  linarith

/-- **Capstone.** The `ρ = tr_M` radial ansatz (with `Vol(T)=Vol(³He)`) is refuted: the C_knot and
tr_M mirror ratios lie on opposite sides of 1 (`mirror_test_excludes_rho_trM`). scope-(a): the radial
handle survives only with `ρ ≠ tr_M` or `Vol(T) ≠ Vol(³He)`; nothing wired, no fit. -/
theorem rho_trM_radial_ansatz_refuted :
    (4.444 : ℝ) / 3.292 > 1 ∧ (0.104071 : ℝ) / 0.206578 < 1 :=
  ⟨cknot_ratio_gt_one, trM_ratio_lt_one⟩

end QOU.MassTheory.RadialVolRhoMirrorTest
