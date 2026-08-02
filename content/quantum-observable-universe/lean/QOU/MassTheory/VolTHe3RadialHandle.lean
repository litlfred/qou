/-
# `ρ = tr_M` radial binding handle: refuted under EVERY volume reading (scope-a)

Front-1 decision point (beans `qou-g5fm` / `qou-0g4z`), the sequel to
`RadialVolRhoMirrorTest.lean` (#4603). That file refuted the radial ansatz
`C_knot = Vol(K)·ρ(K)/ℏ_q²` with `ρ = tr_M` under the ASSUMPTION `Vol(T)=Vol(³He)`. This file
discharges the open question it left — the actual hyperbolic volumes — for the two available readings,
sorry-free. The numeric literals consume `computations/deltalambda/vol_t_he3_snappy_probe.py` (SnapPy,
0-fit; nothing wired).

**Reading 1 — mass-braid H₉ closures are non-hyperbolic.** SnapPy finds no positively-oriented
triangulation of the closure of `β_T`, `β_³He` under any averaged-crossing convention, so
`Vol(T) = Vol(³He) = 0` (degenerate). A zero volume annihilates the handle: `Vol·ρ/ℏ_q² = 0`, which
cannot equal the nonzero `C_knot`. `degenerate_vol_kills_handle` machine-checks this implication.

**Reading 2 — the corpus binding links are hyperbolic but UNEQUAL.** `T → 8₁₁` (Vol 8.2863168),
`³He → L6a4 = Borromean` (Vol 7.3277248). With DISTINCT volumes the ratio identity keeps the volume
factor: `C_knot(T)/C_knot(³He) = (Vol(T)·ρ(T))/(Vol(³He)·ρ(³He))`. At the witnessed values the RHS is
`< 1` (the volume asymmetry 1.13 is too weak to flip `tr_M`'s 0.50) while `C_knot` ratio is `> 1` —
opposite sides of unity, contradiction. `mirror_test_excludes_rho_trM_true_vol` proves it.

**scope-(a).** `ρ = tr_M` is refuted under both readings; the radial handle survives only with a
DERIVED `ρ ≠ tr_M` whose T/³He ratio exceeds `~2.1` (never a `ρ` fitted to `C_knot`). No fit.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.VolTHe3RadialHandle

variable {R : Type*} [Field R]

/-- **General two-volume ratio identity.** If `C_knot(K) = Vol(K)·ρ(K)/h` with a shared `h = ℏ_q²` but
possibly DISTINCT volumes, then `C_knot(T)/C_knot(³He) = (Vol(T)·ρ(T))/(Vol(³He)·ρ(³He))` — only `h`
cancels, the volume factor survives (generic field; `V_He, r_He, h ≠ 0`). Reduces to the equal-Vol
identity of `RadialVolRhoMirrorTest.mirror_ratio_of_radial` when `V_T = V_He`. -/
theorem radial_ratio_general {vT vHe rT rHe h cT cHe : R}
    (hh : h ≠ 0) (hVHe : vHe ≠ 0) (hRHe : rHe ≠ 0)
    (hcT : cT = vT * rT / h) (hcHe : cHe = vHe * rHe / h) :
    cT / cHe = (vT * rT) / (vHe * rHe) := by
  subst hcT hcHe
  field_simp

/-- **A degenerate (zero) volume annihilates the handle.** If `Vol(K) = 0` then the radial dressing
`Vol(K)·ρ(K)/h = 0`, so it cannot equal a nonzero `C_knot`. This is Reading 1: the mass-braid H₉
closures are non-hyperbolic (SnapPy), `Vol ≡ 0`, hence the handle is identically 0 and no nonzero
binding deficit is reproduced. -/
theorem degenerate_vol_kills_handle {vK rK h cK : R}
    (hVol : vK = 0) (hCk : cK ≠ 0) : cK ≠ vK * rK / h := by
  rw [hVol]
  simpa using hCk

/-- **C_knot mirror ratio exceeds 1** (T more bound). Master-formula μ_ext values (PR #4556). -/
theorem cknot_ratio_gt_one : (4.444147 : ℝ) / 3.291800 > 1 := by norm_num

/-- **The Vol·tr_M product ratio is below 1** at the TRUE binding-link volumes.
`(Vol(8₁₁)·tr_M(T)) / (Vol(Borromean)·tr_M(³He)) = (8.2863168·0.104071)/(7.3277248·0.206578) ≈ 0.570`.
The volume asymmetry (8.2863168/7.3277248 ≈ 1.131, > 1) is far too weak to flip `tr_M`'s 0.504. -/
theorem binding_link_pred_ratio_lt_one :
    (8.2863168 * 0.104071 : ℝ) / (7.3277248 * 0.206578) < 1 := by norm_num

/-- **The binding-link volumes are genuinely unequal** (`Vol(T)/Vol(³He) > 1`). So "mirror nuclei ⇒
equal Vol" is FALSE even for the hyperbolic binding-link reading. -/
theorem binding_link_vol_ratio_gt_one : (8.2863168 : ℝ) / 7.3277248 > 1 := by norm_num

/-- **Reading 2 — mirror test refuted with the TRUE (unequal) binding-link volumes.** Assume the radial
ansatz with the witnessed volumes and densities: `C_knot(T) = Vol(8₁₁)·tr_M(T)/h`,
`C_knot(³He) = Vol(Borromean)·tr_M(³He)/h`. The general ratio identity forces
`C_knot(T)/C_knot(³He) = (Vol(T)·tr_M(T))/(Vol(³He)·tr_M(³He))`, but the LHS is `> 1` and the RHS `< 1`
— contradiction. Even the true volume asymmetry does not rescue `ρ = tr_M`. -/
theorem mirror_test_excludes_rho_trM_true_vol {h : ℝ} (hh : h ≠ 0)
    (hcT : (4.444147 : ℝ) = 8.2863168 * 0.104071 / h)
    (hcHe : (3.291800 : ℝ) = 7.3277248 * 0.206578 / h) : False := by
  have hVHe : (7.3277248 : ℝ) ≠ 0 := by norm_num
  have hRHe : (0.206578 : ℝ) ≠ 0 := by norm_num
  have key : (4.444147 : ℝ) / 3.291800
      = (8.2863168 * 0.104071) / (7.3277248 * 0.206578) :=
    radial_ratio_general hh hVHe hRHe hcT hcHe
  have h1 : (4.444147 : ℝ) / 3.291800 > 1 := cknot_ratio_gt_one
  have h2 : (8.2863168 * 0.104071 : ℝ) / (7.3277248 * 0.206578) < 1 :=
    binding_link_pred_ratio_lt_one
  rw [key] at h1
  linarith

/-- **Capstone.** `ρ = tr_M` radial handle is refuted under both available volume readings:
(1) mass-braid closures degenerate (`Vol ≡ 0`, `degenerate_vol_kills_handle`); (2) binding-link volumes
hyperbolic but unequal, and the true asymmetry keeps the prediction ratio on the opposite side of 1 from
`C_knot` (`binding_link_vol_ratio_gt_one` ∧ `binding_link_pred_ratio_lt_one` ∧ `cknot_ratio_gt_one`).
scope-(a); survivor is a derived `ρ ≠ tr_M`. Nothing wired; no fit. -/
theorem rho_trM_radial_handle_refuted_every_reading :
    (8.2863168 : ℝ) / 7.3277248 > 1
      ∧ (8.2863168 * 0.104071 : ℝ) / (7.3277248 * 0.206578) < 1
      ∧ (4.444147 : ℝ) / 3.291800 > 1 :=
  ⟨binding_link_vol_ratio_gt_one, binding_link_pred_ratio_lt_one, cknot_ratio_gt_one⟩

end QOU.MassTheory.VolTHe3RadialHandle
