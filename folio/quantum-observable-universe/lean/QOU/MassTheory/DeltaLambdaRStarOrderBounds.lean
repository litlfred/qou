/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Convention-D `r*` Target vs. Uncabled Pairwise-Door Extrapolation & `r_both` Divergence

Bean `qou-cds5` (epic `qou-v2om`). Companion to `QOU.MassTheory.S5So3GeometricWLambda`.

## Mathematical Problem

Bean `qou-cds5` guards the `Δ_λ` `A = 3` magnitude evaluation against scoring the six pruned
closure ansätze against an unverified Convention-D `r*` band (`[2.04, 2.16]` relayed from PR
`#4766`):

1. **Opposite-direction scaling between the uncabled pairwise door and the cabled Borromean
   cluster (`rStarD_lt_doorScaled_band`):**
   PR `#4766` (`docs/audits/2026-08-08-binding-channel-convention-exposure.md` §3a) measured the
   **uncabled pairwise supermodularity door** `d = |c₃^door|` (`d_D < d_C`, since zeroing the `25`
   `>2`-row blocks of `H₉` reduces `Δ²g`) and observed that scaling the C-frame ratio
   `r*_C = μ₃ / c_{3,C}` by `d_C / d_D > 1` moves upward into `[2.04, 2.16]`.
   On the actual `#4364` width-`3` **cabled-Borromean** cluster (`grouped` word), however, upward
   re-weighting of the surviving `≤ 2`-row Wenzl weights makes `c_{3,D} > c_{3,C} > 0`, so
   `r*_D = μ₃ / c_{3,D} < r*_C < r*_C · (d_C / d_D)`: the true target moves **downward**, strictly
   below any `[2.04, 2.16]` door-extrapolated band.
2. **Word-ordering separation (`doorScaled_lt_rStarD_of_cluster_drop`):**
   Conversely, on the canonical `borromean` intra-nucleon word (`qou-hu1f`), `c_{3,D}^bor` drops by
   more than `d_D / d_C`, pushing `r*_D(borromean)` **strictly above** the door-extrapolated band.
   Neither word's Convention-D `r*` lies inside `[2.04, 2.16]`.
3. **Divergence of the `Σ = 1` normalization trap (`rBoth_increases_while_rStar_decreases`):**
   For the Beasley–Witten geometric weight `W^geom_λ` (`Σ W^geom_λ = 1`, `c_{3,geom}` independent
   of `z`) and raw Wenzl sum `S_y = Σ_λ y_λ`, the `Σ = 1`-rescaled ratio is
   `r_both = (c_{3,geom} / c_{3,y}) · S_y`. Whenever `S_y^D / S_y^C > c_{3,y}^D / c_{3,y}^C > 1`,
   `r_both` strictly **increases** under C → D while `r* = μ₃ / c_{3,y}` strictly **decreases**,
   establishing algebraically that the C-frame `1.504 vs 1.585` proximity was a frame-dependent
   normalization artifact and rescues none of the six pruned `Δ_λ` ansätze.

Base ring (§7c): generic `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` throughout `§1–§2`,
with explicit `ℝ` archimedean specialisation in `§3`. Zero empirical literals.

-- Ref: [hoefsmit1974] Ch. 2 (H_9 seminormal character evaluation)
-- Ref: [ram1991] Thm. 4.14 (Wenzl-Ocneanu principal specialisation weights)
-- Ref: [leitner2026] bean qou-cds5; docs/audits/2026-08-08-binding-channel-convention-exposure.md
-/

namespace QOU.MassTheory

/-! ## §1. Cabled-Cluster `r*` Target vs. Uncabled Pairwise-Door Extrapolation -/

section DoorVsCabledOrder

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Needed closure ratio `r* = μ / c₃` for residual target `μ` and derived cluster `c₃`. -/
def rStarTarget (μ c3 : K) : K := μ / c3

/-- Door-extrapolated ratio `(μ / c₃_C) * (d_C / d_D)` obtained by scaling `r*_C` by the C-to-D
ratio of uncabled pairwise supermodularity door magnitudes `d_C / d_D`. -/
def doorScaledTarget (μ c3C dC dD : K) : K := (μ / c3C) * (dC / dD)

/-- When `0 < μ` and `0 < c₃_C < c₃_D`, the needed ratio `r*` strictly decreases (`r*_D < r*_C`). -/
theorem rStarTarget_lt_of_cluster_gt {μ c3C c3D : K}
    (hμ : 0 < μ) (hcC : 0 < c3C) (hc : c3C < c3D) :
    rStarTarget μ c3D < rStarTarget μ c3C := by
  unfold rStarTarget
  exact div_lt_div_of_pos_left hμ hcC hc

/-- When `0 < μ`, `0 < c₃_C`, and `0 < d_D < d_C` (uncabled door shrinks under D), scaling `r*_C`
by `d_C / d_D > 1` strictly increases the ratio above `r*_C`. -/
theorem rStarTarget_lt_doorScaledTarget {μ c3C dC dD : K}
    (hμ : 0 < μ) (hcC : 0 < c3C) (hdD : 0 < dD) (hd : dD < dC) :
    rStarTarget μ c3C < doorScaledTarget μ c3C dC dD := by
  unfold rStarTarget doorScaledTarget
  have hrC : 0 < μ / c3C := div_pos hμ hcC
  have hgt1 : 1 < dC / dD := (one_lt_div hdD).2 hd
  calc
    μ / c3C = (μ / c3C) * 1 := (mul_one _).symm
    _ < (μ / c3C) * (dC / dD) := mul_lt_mul_of_pos_left hgt1 hrC

/-- **Direction-reversal separation (`qou-cds5`, grouped word):**
Whenever the cabled cluster increases (`0 < c₃_C < c₃_D`) while the uncabled door decreases
(`0 < d_D < d_C`), the true Convention-D target `r*_D` is strictly smaller than `r*_C` and hence
strictly below any door-extrapolated band `[doorScaledTarget μ c₃_C dC_lo dD_lo, ...]`. -/
theorem rStarD_lt_doorScaled_band {μ c3C c3D dC dD : K}
    (hμ : 0 < μ) (hcC : 0 < c3C) (hc : c3C < c3D) (hdD : 0 < dD) (hd : dD < dC) :
    rStarTarget μ c3D < doorScaledTarget μ c3C dC dD :=
  lt_trans (rStarTarget_lt_of_cluster_gt hμ hcC hc)
    (rStarTarget_lt_doorScaledTarget hμ hcC hdD hd)

/-- **Upper-side separation (`qou-cds5`, Borromean word):**
Conversely, if a word reordering drops the cabled cluster `c₃_D_bor > 0` strictly below
`c₃_C * (d_D / d_C)` (`c₃_D_bor * d_C < c₃_C * d_D`), then `r*_D(borromean)` lies strictly above
the upper endpoint of the door-extrapolated band. -/
theorem doorScaled_lt_rStarD_of_cluster_drop {μ c3C c3DBor dC dD : K}
    (hμ : 0 < μ) (hcC : 0 < c3C) (hcBor : 0 < c3DBor) (hdD : 0 < dD)
    (hdrop : c3DBor * dC < c3C * dD) :
    doorScaledTarget μ c3C dC dD < rStarTarget μ c3DBor := by
  unfold doorScaledTarget rStarTarget
  have hmul : (dC / dD) / c3C < 1 / c3DBor := by
    rw [div_div, div_lt_div_iff₀ (mul_pos hdD hcC) hcBor]
    linarith
  have hscale := mul_lt_mul_of_pos_left hmul hμ
  calc
    (μ / c3C) * (dC / dD) = μ * ((dC / dD) / c3C) := by ring
    _ < μ * (1 / c3DBor) := hscale
    _ = μ / c3DBor := by ring

end DoorVsCabledOrder

/-! ## §2. Opposite-Sign Shift of `r_both` vs. `r*` Under Convention Change -/

section RBothDivergence

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Common-`Σ = 1` rescaled geometric ratio `r_both = (c₃_geom / c₃_y) * S_y`, where `c₃_geom` is
the `z`-independent Beasley–Witten `d_q² / D²` cluster and `S_y = Σ_λ y_λ` is the unnormalised sum
of Wenzl block weights. -/
def rBothNormalized (c3Geom c3y Sy : K) : K := (c3Geom / c3y) * Sy

/-- **Opposite-direction divergence of `r_both` and `r*` (`qou-cds5`):**
When `0 < μ`, `0 < c₃_geom`, `0 < c₃_C < c₃_D`, and the weight-sum growth exceeds the
cabled-cluster growth (`c₃_D * S_C < c₃_C * S_D`), moving from Convention C to Convention D makes
`r_both` strictly **increase** while `r*` strictly **decreases**. In particular, if `r_both^C`
already exceeded `r*_D` (or if `r*_C < r_both^D`), `r_both^D > r*_D` strictly overshoots. -/
theorem rBoth_increases_while_rStar_decreases {μ c3Geom c3C c3D SC SD : K}
    (hμ : 0 < μ) (hgeom : 0 < c3Geom) (hcC : 0 < c3C) (hc : c3C < c3D)
    (hgrow : c3D * SC < c3C * SD) :
    rStarTarget μ c3D < rStarTarget μ c3C ∧
      rBothNormalized c3Geom c3C SC < rBothNormalized c3Geom c3D SD := by
  refine ⟨rStarTarget_lt_of_cluster_gt hμ hcC hc, ?_⟩
  unfold rBothNormalized
  have hcD : 0 < c3D := lt_trans hcC hc
  have hfrac : SC / c3C < SD / c3D := by
    rw [div_lt_div_iff₀ hcC hcD]
    linarith
  have hmul := mul_lt_mul_of_pos_left hfrac hgeom
  calc
    (c3Geom / c3C) * SC = c3Geom * (SC / c3C) := by ring
    _ < c3Geom * (SD / c3D) := hmul
    _ = (c3Geom / c3D) * SD := by ring

end RBothDivergence

/-! ## §3. Archimedean `ℝ` Specialisation (`§7c`) -/

section ArchimedeanReal

/-- Archimedean `ℝ` specialisation of `rStarD_lt_doorScaled_band` and
`rBoth_increases_while_rStar_decreases`. -/
theorem rStarD_and_rBoth_separation_real {μ c3Geom c3C c3D dC dD SC SD : ℝ}
    (hμ : 0 < μ) (hgeom : 0 < c3Geom) (hcC : 0 < c3C) (hc : c3C < c3D)
    (hdD : 0 < dD) (hd : dD < dC) (hgrow : c3D * SC < c3C * SD) :
    rStarTarget μ c3D < doorScaledTarget μ c3C dC dD ∧
      rBothNormalized c3Geom c3C SC < rBothNormalized c3Geom c3D SD :=
  ⟨rStarD_lt_doorScaled_band hμ hcC hc hdD hd,
   (rBoth_increases_while_rStar_decreases hμ hgeom hcC hc hgrow).2⟩

end ArchimedeanReal

end QOU.MassTheory
