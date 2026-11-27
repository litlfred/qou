import QOU.BraidsAndKnots.S5SO3FiberAction
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse

/-!
# The geometric build: the forced `BringFiberAction` instance

The s5-so3 keystone's conditional class `BringFiberAction` (`S5SO3FiberAction.lean`) carries the
geometric fibre map `irrepToRotation : A5Irrep → IcosahedralRotation` and its substantive injectivity
field `five_distinct_classes` (the five A₅ irreps realize five DISTINCT icosahedral rotation angles).
Every downstream keystone result (`s5_so3_fiber_action_scaffold`, `reeb_eq_restriction_scaffold`) was
**conditional** on `[BringFiberAction]`. This file **discharges** it with the forced icosahedral data.

**The map is determined.** A₅ ≅ the icosahedral rotation group I ⊂ SO(3) (Klein 1884). The per-irrep
icosahedral Reeb phase is `θ_λ = arccos(χ_λ(C₅)/dim_λ)`, where `χ_λ(C₅)` is the A₅ character on the
5-fold conjugacy class. The five cosines are exact (A₅ character table; PR #2591 validated the angle
assignment to `5×10⁻⁴¹`, with the golden-ratio fingerprint `χ_{ℓ=1}(72°)=1+2cos72°=φ`):

| irrep | dim | χ(C₅)/dim |
|---|---|---|
| A  | 1 | `1` |
| T₁ | 3 | `(1+√5)/6 = φ/3` |
| T₂ | 3 | `(1−√5)/6 = −φ⁻¹/3` |
| G  | 4 | `−1/4` |
| H  | 5 | `0` |

These five reals are distinct, so the five Reeb phases are distinct (arccos is injective on `[−1,1]`),
and `five_distinct_classes` holds. The instance is therefore **content-bearing**, not the falsified
vacuous `: True` map (AGENTS.md §3b): `irrepToRotation` is the genuine icosahedral Reeb map and its
injectivity is proved from the character data.

**Scope (honest).** This discharges `conj:s5-so3-fiber-action` — the *fibre-map* existence + the
distinct-angles half — with the validated icosahedral angles, making
`s5_so3_fiber_action_scaffold` (and the conjugation-identification it derives) **unconditional**. It
does **not** close residual (i) (the separate `W_λ = d_q²/D²` Plancherel/MTC-matching obligation,
formalized as `BeasleyWittenLocalization`), and it imports the #2591-validated character/angle data as
the map's definition rather than re-deriving Bring's quintic automorphism from scratch.
-/

namespace QOU.BraidsAndKnots

open Real

/-- The forced 5-fold-class cosines `χ_λ(C₅)/dim_λ` of the A₅ character table (PR #2591). -/
noncomputable def reebCos : A5Irrep → ℝ
  | .A  => 1
  | .T₁ => (1 + Real.sqrt 5) / 6
  | .T₂ => (1 - Real.sqrt 5) / 6
  | .G  => -1 / 4
  | .H  => 0

/-- The per-irrep icosahedral Reeb phase `θ_λ = arccos(χ_λ(C₅)/dim_λ)`. -/
noncomputable def reebAngle (l : A5Irrep) : ℝ := Real.arccos (reebCos l)

private lemma s5sq : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
private lemma s5nn : (0 : ℝ) ≤ Real.sqrt 5 := Real.sqrt_nonneg 5
private lemma s5lt : Real.sqrt 5 < 5 / 2 := by nlinarith [s5sq, s5nn]
private lemma s5gt : (2 : ℝ) < Real.sqrt 5 := by nlinarith [s5sq, s5nn]

/-- Each cosine lies in `[−1, 1]` (so `arccos` is defined and injective there). -/
private lemma reebCos_mem (l : A5Irrep) : reebCos l ∈ Set.Icc (-1 : ℝ) 1 := by
  cases l <;> rw [Set.mem_Icc] <;> refine ⟨?_, ?_⟩ <;>
    simp only [reebCos] <;> nlinarith [s5lt, s5gt, s5nn]

/-- **The five cosines are distinct.** -/
lemma reebCos_inj : Function.Injective reebCos := by
  intro a b h
  cases a <;> cases b <;> simp only [reebCos] at h <;>
    first
      | rfl
      | (exfalso; nlinarith [s5lt, s5gt, s5nn, h])

/-- **The five Reeb phases are distinct** — arccos is injective on `[−1, 1]` and the cosines differ. -/
lemma reebAngle_inj : Function.Injective reebAngle := by
  intro a b h
  apply reebCos_inj
  have ha := reebCos_mem a; have hb := reebCos_mem b
  rw [Set.mem_Icc] at ha hb
  have hcos := congrArg Real.cos h
  rwa [reebAngle, reebAngle, Real.cos_arccos ha.1 ha.2, Real.cos_arccos hb.1 hb.2] at hcos

/-- **The geometric build: the forced `BringFiberAction` instance.** Each A₅ irrep maps to a rotation
by its icosahedral Reeb phase `θ_λ = arccos(χ_λ(C₅)/dim_λ)` about the Seifert `S¹` (Reeb) axis. The
five phases are distinct (`reebAngle_inj`), discharging `five_distinct_classes` — the content-bearing
instance of `conj:s5-so3-fiber-action`, making `s5_so3_fiber_action_scaffold` unconditional. -/
noncomputable instance bringFiberAction_icosahedral : BringFiberAction where
  irrepToRotation l := ⟨{ axis_x := 0, axis_y := 0, axis_z := 1, angle := reebAngle l }⟩
  five_distinct_classes := reebAngle_inj

/-- **`s5_so3_fiber_action_scaffold` is now unconditional** (the `BringFiberAction` hypothesis is
discharged by the icosahedral Reeb map): the partition `dim²` sum is `120`, conjugation is involutive,
and conjugate partitions share a fibre rotation. -/
theorem s5_so3_fiber_action_unconditional :
    (PartitionOf5.allList.map (fun p => p.dim ^ 2)).sum = 120 ∧
    (∀ p : PartitionOf5, p.conjugate.conjugate = p) ∧
    (∀ p : PartitionOf5,
      bringFiberAction_icosahedral.irrepToRotation p.conjugate.toA5Irrep
        = bringFiberAction_icosahedral.irrepToRotation p.toA5Irrep) :=
  s5_so3_fiber_action_scaffold

/-- **Weighted character orthogonality on the 5-fold class (`uer8`).**
Weighting `reebCos l = χ_l(C₅)/dim_l` by `dim_l²` across the five irreps of `A₅`
(`1, 3, 3, 4, 5`) recovers the column orthogonality relation `∑_l dim_l · χ_l(C₅) = 0`. -/
theorem reebCos_dim_sq_weighted_sum_zero :
    (1 : ℝ) ^ 2 * reebCos .A + (3 : ℝ) ^ 2 * reebCos .T₁ +
      (3 : ℝ) ^ 2 * reebCos .T₂ + (4 : ℝ) ^ 2 * reebCos .G +
      (5 : ℝ) ^ 2 * reebCos .H = 0 := by
  have hA : reebCos .A = 1 := rfl
  have hH : reebCos .H = 0 := rfl
  dsimp [reebCos]
  ring

end QOU.BraidsAndKnots
