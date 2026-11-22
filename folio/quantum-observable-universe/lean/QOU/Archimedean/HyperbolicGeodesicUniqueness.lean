/-
# HyperbolicGeodesicUniqueness.lean (T2, WALL-5) — the full geodesic-uniqueness
# assembly: `HypMinimizerUnique` is DERIVED from WALL-2 + WALL-4.

The capstone of the T2 geodesic-uniqueness program.  It composes the two closed
walls into the general uniqueness statement, discharging the sole open input of
the whole development:

* **WALL-2** (`exists_normalization_isom`, `HyperbolicNormalization`): every pair
  `x, y ∈ H³` is carried onto the z-axis by a `dH`-isometry `Φ` that has a
  `dH`-isometry LEFT INVERSE `Ψ`.  So `Φ` is injective and preserves `dH` exactly.
* **WALL-4** (`zaxis_minimizer_eq_vseg`, `HyperbolicGeodesicZAxisUniqueness`): a
  constant-speed minimiser between two z-axis points IS the vertical segment
  `vseg`, pointwise.

## The reduction (DERIVED, not assumed)

Given two constant-speed minimisers `γ, δ` between arbitrary `x, y ∈ H³`:

1. Normalise: `Φ x = zpt a`, `Φ y = zpt b` with `a = (Φ x)₂ > 0`, `b = (Φ y)₂ > 0`.
2. `Φ ∘ γ` and `Φ ∘ δ` are constant-speed minimisers between `zpt a` and `zpt b`
   (`minimizer_comp`): `Φ` preserves admissibility (`admissiblePath_comp`), length
   (`pathLenH_comp`), constant speed (`speed_comp`), and — because `Φ` has a
   `dH`-isometry left inverse — minimality (`dH (Φ x)(Φ y) = dH x y`,
   `dH_eq_of_leftInverse`).
3. By WALL-4 both equal `vseg a b` pointwise, so `Φ (γ t) = Φ (δ t)`.
4. `Φ` is injective (left inverse `Ψ`), hence `γ t = δ t`.

This is exactly the field of the open `HypMinimizerUnique` class, so
`hypMinimizerUnique_derived : HypMinimizerUnique` is a GENUINE derivation — not a
fabricated / `sorry` / trivial instance.

## Disposition (STRICT — read before promoting)

`HypMinimizerUnique` was authored as the deliberately-open, "one genuinely open,
Mathlib-scale input of the whole T2 development" (`HyperbolicGeodesic`), with NO
instance.  This file DERIVES it, but deliberately provides it as a `def`
(`hypMinimizerUnique_derived`), **NOT** a global `instance` — so it does not
silently flip every `[HypMinimizerUnique]`-conditional theorem in the corpus to
unconditional.  Promoting to a global `instance` (a one-line change) is left to
the owner, who should first review the two supporting walls.  `HyperbolicGeodesic`
is left untouched: no `HypMinimizerUnique` instance is fabricated there.

The derivation rests on WALL-4 (`zaxis_minimizer_eq_vseg`, bean `qou-xidi`).  That
file was originally authored WITHOUT machine verification; it is here confirmed to
build `lean`-direct exit 0 with `#print axioms` = `[propext, Classical.choice,
Quot.sound]` (no `sorryAx`) — the verification `qou-xidi` was waiting on.

Archimedean (ℝ): `dH`, `‖·‖`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.4 (isometry group acts transitively; reduction
  --   of geodesic uniqueness to the vertical geodesic)
  -- Ref: [ratcliffe] §4.6 (geodesics of `H³`; uniqueness of the minimiser)
  -- Ref: [leitner2026] beans qou-r111 (the full geodesic-uniqueness wall),
  --   qou-0a0z (WALL-2), qou-xidi (WALL-4), qou-473l (T2), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicNormalization
import QOU.Archimedean.HyperbolicGeodesic
import QOU.Archimedean.HyperbolicGeodesicZAxisUniqueness

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric
open scoped ENNReal

/-- **A z-axis point equals `zpt` of its height.**  A point of `zAxis` has both
horizontal coordinates `0`, so it is `(0,0,·)` — the value `zpt ((·) 2)`.  Lets a
`zAxis` membership be fed to the z-axis uniqueness lemma, which is stated in terms
of `zpt`. -/
theorem zAxisPt_eq {v : E} (h : v ∈ zAxis) : v = zpt (v 2) := by
  funext i
  fin_cases i
  · show v 0 = zpt (v 2) 0; rw [h.1, zpt_coord0]
  · show v 1 = zpt (v 2) 1; rw [h.2.1, zpt_coord1]
  · show v 2 = zpt (v 2) 2; rw [zpt_height]

/-- **A `dH`-isometry maps a constant-speed minimiser to a constant-speed
minimiser** (given that it preserves the distance between the endpoints).  All
three fields transport: admissibility by `admissiblePath_comp`, minimality by
`pathLenH_comp` together with the endpoint-distance hypothesis `hdH`, and constant
speed by `speed_comp` (the line element is preserved pointwise). -/
theorem minimizer_comp {φ : E → E} (hφ : IsDHIsometry φ) {γ : ℝ → E} {x y : E}
    (hγ : IsHypMinimizer γ x y) (hdH : dH (φ x) (φ y) = dH x y) :
    IsHypMinimizer (φ ∘ γ) (φ x) (φ y) where
  admissible := hφ.admissiblePath_comp hγ.admissible
  minimal := by
    rw [hφ.pathLenH_comp hγ.admissible.diff hγ.admissible.mem, hγ.minimal, hdH]
  constSpeed := by
    intro s hs t ht
    have hs' := hφ.speed_comp hγ.admissible.diff hγ.admissible.mem hs
    have ht' := hφ.speed_comp hγ.admissible.diff hγ.admissible.mem ht
    have hc := hγ.constSpeed s hs t ht
    simp only [hypSpeed] at hc ⊢
    rw [hs', ht']; exact hc

/-- **WALL-5 — geodesic uniqueness in `H³` (DERIVED, sorry-free).**  Between any two
points of `H³`, two constant-speed length-minimisers agree pointwise on `[0,1]`.
The reduction: normalise both endpoints onto the z-axis by an invertible
`dH`-isometry `Φ` (WALL-2), where the two images `Φ∘γ`, `Φ∘δ` are minimisers
between z-axis points, hence both equal the vertical segment (WALL-4); injectivity
of `Φ` then transfers the equality back.

This is exactly the content of the open `HypMinimizerUnique.unique` field. -/
theorem hyp_minimizer_unique_pointwise {x y : E} (hx : x ∈ upperH) (hy : y ∈ upperH)
    {γ δ : ℝ → E} (hγ : IsHypMinimizer γ x y) (hδ : IsHypMinimizer δ x y)
    {t : ℝ} (ht : t ∈ Set.Icc (0 : ℝ) 1) : γ t = δ t := by
  obtain ⟨Φ, Ψ, hΦ, hΨ, hLI, hΦx, hΦy⟩ := exists_normalization_isom hx hy
  have ha0 : 0 < (Φ x) 2 := hΦx.2.2
  have hb0 : 0 < (Φ y) 2 := hΦy.2.2
  have hΦxeq : Φ x = zpt ((Φ x) 2) := zAxisPt_eq hΦx
  have hΦyeq : Φ y = zpt ((Φ y) 2) := zAxisPt_eq hΦy
  -- `Φ` preserves `dH` exactly (it has a `dH`-isometry left inverse)
  have hdH : dH (Φ x) (Φ y) = dH x y := dH_eq_of_leftInverse hΦ hΨ hLI x y
  -- the two images are minimisers between the z-axis points `zpt a`, `zpt b`
  have hmγ : IsHypMinimizer (Φ ∘ γ) (zpt ((Φ x) 2)) (zpt ((Φ y) 2)) := by
    have hm := minimizer_comp hΦ hγ hdH; rwa [hΦxeq, hΦyeq] at hm
  have hmδ : IsHypMinimizer (Φ ∘ δ) (zpt ((Φ x) 2)) (zpt ((Φ y) 2)) := by
    have hm := minimizer_comp hΦ hδ hdH; rwa [hΦxeq, hΦyeq] at hm
  -- WALL-4: both equal the vertical segment, hence each other, at `t`
  have e1 := zaxis_minimizer_eq_vseg ha0 hb0 hmγ t ht
  have e2 := zaxis_minimizer_eq_vseg ha0 hb0 hmδ t ht
  have hΦeq : Φ (γ t) = Φ (δ t) := by
    have h : (Φ ∘ γ) t = (Φ ∘ δ) t := by rw [e1, e2]
    simpa only [Function.comp_apply] using h
  exact hLI.injective hΦeq

/-- **`HypMinimizerUnique` is DERIVABLE** — the derived witness of the T2
geodesic-uniqueness conjecture, assembled from WALL-2 (`exists_normalization_isom`)
and WALL-4 (`zaxis_minimizer_eq_vseg`) via `hyp_minimizer_unique_pointwise`.

Deliberately a `def`, NOT a global `instance`: it does not auto-activate the
`[HypMinimizerUnique]`-conditional theorems across the corpus.  Promotion to a
global `instance` is the owner's call after reviewing the two supporting walls.
`HyperbolicGeodesic` is left untouched (no fabricated instance there). -/
def hypMinimizerUnique_derived : HypMinimizerUnique where
  unique := fun _x hx _y hy _γ _δ hγ hδ _t ht =>
    hyp_minimizer_unique_pointwise hx hy hγ hδ ht

end QOU.Archimedean
