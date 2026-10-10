/-
# The GENUINE geometric (Beasley–Witten / WRT(S³/2I)) keystone `W_λ` re-weight of the
# A=3 Borromean H₉ cluster is `d_q²/D²` (a probability measure), NOT the sibling's
# un-normalized `d_q²/[n]_q!` — and it too WALLS the A=3 Δ_λ magnitude (scope-a).

This file is the **distinct geometric angle** on Route 1 of the A=3 Δ_λ magnitude
source (the honest wall recorded in
`docs/audits/2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`).

## What the sibling did, and the normalization it used

`S5So3WLambdaLift.lean` (#4376) + `s5so3_wlambda_borromean_lift_probe.py` re-weighted
the `H₉` cabled-Borromean cluster with the **q-Plancherel proxy**
`W^{raw}_λ = d_q(λ)² / [n]_q!` and measured the re-weight ratio
`r_raw = c₃(W^{raw})/c₃(y_λ) = 52.62` vs the needed `r* = μ₃/v_y ≈ 1.585` — a
**33× overshoot, WALL(scope-a)**.

But at the substrate `q₀ ≈ 1.10998` (real `> 1`, growth regime) the sum of that proxy
is `Σ_λ d_q²/[n]_q! = D²/[n]_q! = 1.1109 ≠ 1` (witnessed). So `d_q²/[n]_q!` is **not a
probability measure** — it is the genuine measure scaled by that sum.

## The genuine geometric object

The corpus's own Lean
[`WLambdaMTCLocalizationObligation.lean`](../../BraidKnot/WLambdaMTCLocalizationObligation.lean)
states the Beasley–Witten / Reshetikhin–Turaev localization weight on the Poincaré
sphere `S³/2I` is

    W^{geom}_λ = d_q(λ)² / D²,   D² = Σ_{λ⊢n} d_q(λ)²   (⇒ Σ_λ W^{geom}_λ = 1, C1),

with `D² = Σ d_q²` the **genuine Plancherel normaliser, NOT `[n]_q!`** (that file's own
words). So the genuine geometric measure is the sibling's raw weight divided by its own
sum `S = D²/[n]_q!`:  `W^{geom}_λ = W^{raw}_λ / S`.

Since the cluster magnitude is **linear** in the block weight (same argument as
`lift_is_coefficient_ratio` / `reweight_is_coefficient_ratio`), dividing the weight by `S`
divides the cluster (and hence the re-weight ratio) by `S`:

    r_geom = r_raw / S = 52.62 / 1.1109 = 47.37.

**Corrected verdict.** The genuine, correctly-normalized geometric `W_λ = d_q²/D²` gives
`r_geom ≈ 47.37`, still a **~30× overshoot** of the needed `r* ≈ 1.585`. The geometric
route is a **WALL(scope-a)** — the correct normalizer (D², not `[n]_q!`) shifts the
number 11 % but does **not** change the verdict. There is no *other* geometric amplitude
to try: the 2026-07-17 synthesis (`self-duality S⁴=1` narrowing) structurally excludes any
free-scale (WRT/Ẑ/F_K) family from carrying the self-dual `d_q` vacuum row, and the
2026-07-12 three-vectors synthesis shows every framed colored-WRT weight either breaks the
proved `W_{λ′}=W_λ` symmetry or collapses in `|·|²` to exactly this Plancherel measure.

## The fit-trap this file inoculates against

`Σ y_λ = 0.0318 ≠ 1` (the production weights are **not** a probability measure). If one
puts *both* weight systems on a common `Σ = 1` normalization — i.e. rescales `y_λ` up by
`1/0.0318 ≈ 31.5` — the ratio becomes `r_geom · Σy_λ = 47.37 · 0.0318 = 1.506`, a
tantalizing but still-missing `5 %` short of `r* ≈ 1.585`. That "both-normalized" comparison
is a **normalization-convention choice** the production trace `ρ_F` does not make (it uses
the raw `y_λ`); selecting it — or any exact-closing rescale `c` — makes `c` an **underived
parameter fixed by inversion from μ₃**, a FIT, declined ("no seventh fit-based ansatz").
`route_closes_with_rescale_iff` makes the trap explicit: closure under a rescale forces `c`
to a specific `μ₃`-determined value, i.e. `c` is inverted from the target.

**Anti-fit discipline (STRICT).** `W^{geom}_λ = d_q²/D²` is fixed by `q₀` + hook-lengths —
0 free parameters, never inverted from `μ₃`. `μ₃` enters only as the target. The RESULT
values below are forward-evaluated by
`computations/deltalambda/s5so3_geometric_wlambda_borromean_lift_probe.py`.

Base ring (§7c): `ℝ` — archimedean magnitude / ratio facts at the substrate anchor.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### The re-weight is a coefficient ratio (recap of the structural invariant) -/

/-- The A=3 cluster magnitude at a block-weight character-sum `κ` (the weight's
`h⁴`-coefficient `κ_w = Σ_λ w_λ |χ_λ|`): `c₃ = E₀ · h⁴ · κ_w`.  Linear in the weight. -/
noncomputable def clusterMag (E0 h κ : ℝ) : ℝ := E0 * (h ^ 4 * κ)

/-- **Linearity in the weight.**  Scaling the block-weight system by `s` scales the
cluster by `s` (`κ_{s·w} = s·κ_w` since `κ` is a linear functional of the weight). -/
theorem clusterMag_smul (E0 h s κ : ℝ) :
    clusterMag E0 h (s * κ) = s * clusterMag E0 h κ := by
  unfold clusterMag; ring

/-- **Re-weight ratio.**  For two weight systems with character-sums `κ_W`, `κ_y`, the
cluster ratio is `κ_W / κ_y` — the shared `E₀·h⁴` cancels. -/
theorem reweight_is_coefficient_ratio {E0 h κ_W κ_y : ℝ}
    (hE : E0 ≠ 0) (hh : h ≠ 0) (hy : κ_y ≠ 0) :
    clusterMag E0 h κ_W / clusterMag E0 h κ_y = κ_W / κ_y := by
  unfold clusterMag
  have h4 : h ^ 4 ≠ 0 := pow_ne_zero 4 hh
  field_simp

/-! ### The genuine geometric normalizer `D²`, and the `S`-correction of the ratio -/

/-- The genuine Beasley–Witten geometric measure is the sibling's raw q-Plancherel weight
`W^{raw}_λ = d_q²/[n]_q!` divided by its own sum `S = Σ_λ W^{raw}_λ = D²/[n]_q!`:
`W^{geom}_λ = W^{raw}_λ / S`.  Its character-sum coefficient is therefore `κ_raw / S`. -/
noncomputable def geomCoeff (κ_raw S : ℝ) : ℝ := κ_raw / S

/-- **Normalization correction of the re-weight ratio.**  Because the genuine geometric
weight is the raw q-Plancherel weight divided by its sum `S`, the genuine re-weight ratio
is the sibling's raw ratio divided by `S`:  `r_geom = r_raw / S`.  (Here `r_raw = κ_raw/κ_y`
and `r_geom = geomCoeff κ_raw S / κ_y`.) -/
theorem geom_ratio_eq_raw_ratio_div_sum {κ_raw κ_y S : ℝ}
    (hS : S ≠ 0) (hy : κ_y ≠ 0) :
    geomCoeff κ_raw S / κ_y = (κ_raw / κ_y) / S := by
  unfold geomCoeff
  field_simp

/-- **C1 — the genuine geometric measure sums to `1`.**  With `D² = Σ_λ d_q²` and the raw
sum `S = D²/[n]_q!`, the genuine measure `W^{geom}_λ = (d_q²/[n]_q!)/S` has total mass
`(D²/[n]_q!)/S = 1`.  (Stated as: dividing the raw total `S` by `S` gives `1`.) -/
theorem geom_measure_normalized {S : ℝ} (hS : S ≠ 0) : geomCoeff S S = 1 := by
  unfold geomCoeff; exact div_self hS

/-! ### Closure predicate on the genuine geometric ratio — RESULT filled from the probe -/

/-- **Geometric-route closure predicate.**  The A=3 magnitude closes under the genuine
geometric `W^{geom}_λ` re-weight iff the derived ratio `r_geom` equals the needed
`r* = μ₃/v_y`.  `r_geom` is FIXED by `q₀` + hook-lengths (0 fit); a value chosen to satisfy
this would be a FIT and is declined. -/
def GeomRouteCloses (r_geom v_y μ₃ : ℝ) : Prop := r_geom * v_y = μ₃

theorem geomRoute_closes_iff {r_geom v_y μ₃ : ℝ} (hv : v_y ≠ 0) :
    GeomRouteCloses r_geom v_y μ₃ ↔ r_geom = μ₃ / v_y := by
  unfold GeomRouteCloses
  rw [eq_div_iff hv]

/-- **RESULT (probe, 0-fit): the genuine geometric ratio is `47.37`, the needed is `1.585`
— the geometric route does NOT close.**  `r_geom = r_raw/S = 52.6226/1.1109 = 47.369`
(forward-evaluated; `μ₃`, AME, CODATA never inverted).  Stated with the derived value and
the needed ratio as explicit hypotheses so `μ₃` sets nothing. -/
theorem geom_route_walls
    {r_geom v_y μ₃ : ℝ}
    (hv : v_y = (0.296958 : ℝ))
    (hμ : μ₃ = (0.4708 : ℝ))
    (hr : r_geom = (47.369 : ℝ)) :
    ¬ GeomRouteCloses r_geom v_y μ₃ := by
  rw [geomRoute_closes_iff (by rw [hv]; norm_num)]
  rw [hr, hv, hμ]
  norm_num

/-- **The genuine geometric cluster overshoots `μ₃` by ~30× (the honest wall).**  With the
derived geometric cluster value `c₃(geom) = 14.069 MeV` and target `μ₃ = 0.4708`, the
cluster is positive (right sign, #4360) and far larger than `μ₃` — a scope-(a) overshoot,
not the missing `1.585×`.  (`14.069 = 15.6267/1.1109`, the `S`-corrected sibling value.) -/
theorem geom_cluster_overshoots
    {c3 μ₃ : ℝ} (hc : c3 = (14.069 : ℝ)) (hμ : μ₃ = (0.4708 : ℝ)) :
    0 < c3 ∧ μ₃ < c3 := by
  refine ⟨?_, ?_⟩
  · rw [hc]; norm_num
  · rw [hc, hμ]; norm_num

/-! ### The declined fit-trap: closing by rescaling `y_λ` needs a `μ₃`-inverted parameter -/

/-- **Fit-trap (declined).**  `Σ y_λ = 0.0318 ≠ 1`, so one *could* rescale the production
weights `y_λ ↦ c·y_λ`, changing the cluster to `c·v_y` and requiring the geometric ratio
`r_geom` to satisfy `r_geom·(c·v_y) = μ₃`.  Closure under such a rescale forces `c` to the
specific value `c = μ₃/(r_geom · v_y)` — i.e. `c` is **inverted from the target `μ₃`**, a
free parameter, hence a FIT.  (Even the *derivation-flavoured* choice "put both weights on
`Σ=1`", `c = 1/Σy_λ ≈ 31.5`, only reaches `r_geom·Σy_λ = 1.506`, a `5 %` miss — and is
itself an undetermined normalization convention, not a derivation.)  This lemma states
exactly that dependence (closure ⟺ `c` takes the `μ₃`-determined value). -/
theorem route_closes_with_rescale_iff
    {r_geom v_y μ₃ c : ℝ} (hr : r_geom ≠ 0) (hv : v_y ≠ 0) :
    r_geom * (c * v_y) = μ₃ ↔ c = μ₃ / (r_geom * v_y) := by
  have hrv : r_geom * v_y ≠ 0 := mul_ne_zero hr hv
  rw [eq_div_iff hrv]
  constructor <;> intro h <;> linear_combination h

end QOU.MassTheory
