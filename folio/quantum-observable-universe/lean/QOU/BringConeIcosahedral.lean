import QOU.BringCone

/-!
# Does a quaternionic symmetry single out the chirality unit `u`?

Bean `qou-wqto`. Preregistration:
`docs/audits/2026-11-15-bring-s5-distinguished-unit-preregistration.md`.

`QOU/BringCone.lean` showed that the chirality grading `Γ_u = L_u ∘ M_i` on the model
cone `BringCone R = Quaternion R` needs a pure unit `u`, and that every linear map
commuting with the Reeb triad is a left multiplication
(`commutes_reeb_triad_iff_leftMul`). This file records what follows for **any group of
unit quaternions acting by left multiplication** — the only shape a triad-respecting
linear symmetry can have. The intended case is the binary icosahedral group `2I`, the
lift of the icosahedral `A₅`; but **the corpus does not establish that Bring's `S₅` (or
its `A₅`) acts on this cone at all.** Every statement below is about the action of the
named unit quaternions; none asserts that they are Bring's automorphisms.

Proved here (generic `CommRing R`, §7c):

* `leftMul_conj_chiralGammaU`: `L_g ∘ Γ_u ∘ L_{ḡ} = Γ_{g u ḡ}`. So a left-multiplication
  symmetry acts on the admissible units by conjugation `u ↦ g u ḡ`.
* `re_conjBy`, `normSq_conjBy`: conjugation by a unit `g` preserves "pure" and the norm,
  so it maps admissible units to admissible units.
* `conjBy_unitI_unitJ_fixed_eq_zero`: no nonzero pure quaternion is fixed by conjugation
  by both `i` and `j` (when `2` is cancellable). Both lie in `2I` in its standard
  embedding, so **no admissible `u` is fixed by the whole group** (rule R0 is empty).
* `conjBy_neg_of_anticomm`, `leftMul_flips_chiralGammaU`: if a pure unit `w` anticommutes
  with `u` (a 2-fold rotation axis perpendicular to `u`), conjugation by `w` sends `u` to
  `−u` and the symmetry `L_w` carries `Γ_u` to `−Γ_u` — it swaps L and R.
* `leftMul_unitJ_flips_chiralGamma_i`: the instance `w = j`, `u = i`.

The orbit structure of `2I` itself (12 / 20 / 30 exceptional points, each orbit closed
under `u ↦ −u` by a perpendicular 2-fold rotation) is verified in exact arithmetic over
`ℚ(√5)` in `computations/probes/bring_cone_icosahedral_unit_orbits_probe.py`, not here.

No `sorry`, no axiom, no `native_decide`.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- Conjugation of an admissible unit by `g`: `u ↦ g u ḡ`. -/
def conjBy (g u : BringCone R) : BringCone R := g * u * star g

/-- **A left-multiplication symmetry acts on the chirality unit by conjugation.**
`L_g ∘ Γ_u ∘ L_{ḡ} = Γ_{g u ḡ}`, for every `g` (no norm condition: `L_{ḡ}` is written
explicitly, and is the inverse of `L_g` when `normSq g = 1`). -/
theorem leftMul_conj_chiralGammaU (g u p : BringCone R) :
    leftMul g (chiralGammaU u (leftMul (star g) p)) = chiralGammaU (conjBy g u) p := by
  simp only [chiralGammaU, leftMul, reebM_i, conjBy, mul_assoc]

/-- Conjugation scales the real part by `normSq g`; in particular it preserves "pure". -/
theorem re_conjBy (g u : BringCone R) :
    (conjBy g u).re = Quaternion.normSq g * u.re := by
  rw [Quaternion.normSq_def']
  simp [conjBy]
  ring

/-- Conjugation scales the norm by `normSq g ^ 2`; a unit `g` preserves it. -/
theorem normSq_conjBy (g u : BringCone R) :
    Quaternion.normSq (conjBy g u) = Quaternion.normSq g ^ 2 * Quaternion.normSq u := by
  simp only [conjBy, map_mul, Quaternion.normSq_star]
  ring

/-- **No common fixed admissible unit.** If `2` is cancellable in `R`, a pure quaternion
fixed by conjugation by both `i` and `j` is zero. (Conjugation by `i` is the half-turn
about the `i`-axis, by `j` the half-turn about the `j`-axis; their fixed lines meet only
at `0`.) -/
theorem conjBy_unitI_unitJ_fixed_eq_zero (h2 : ∀ x : R, 2 * x = 0 → x = 0)
    {u : BringCone R} (hre : u.re = 0)
    (hi : conjBy unitI u = u) (hj : conjBy unitJ u = u) : u = 0 := by
  have hiJ := congrArg (fun x : BringCone R => x.imJ) hi
  have hiK := congrArg (fun x : BringCone R => x.imK) hi
  have hjI := congrArg (fun x : BringCone R => x.imI) hj
  simp [conjBy, unitI, unitJ] at hiJ hiK hjI
  have hb : u.imJ = 0 := h2 _ (by linear_combination -hiJ)
  have hc : u.imK = 0 := h2 _ (by linear_combination -hiK)
  have ha : u.imI = 0 := h2 _ (by linear_combination -hjI)
  ext <;> simp [hre, ha, hb, hc]

/-- **A perpendicular half-turn sends `u` to `−u`.** If `w` anticommutes with `u` and
`normSq w = 1`, then `w u w̄ = −u`. -/
theorem conjBy_neg_of_anticomm {w u : BringCone R} (hw : Quaternion.normSq w = 1)
    (hanti : w * u = -(u * w)) : conjBy w u = -u := by
  have hws : w * star w = 1 := by
    rw [Quaternion.self_mul_star, hw]; rfl
  calc conjBy w u = (w * u) * star w := rfl
    _ = -(u * (w * star w)) := by rw [hanti, neg_mul, mul_assoc]
    _ = -u := by rw [hws, mul_one]

/-- **…and so the symmetry `L_w` swaps the two chiralities**: it carries `Γ_u` to
`−Γ_u = Γ_{−u}`. A group containing such a `w` identifies L with R at `u`; it cannot
fix a handedness there. -/
theorem leftMul_flips_chiralGammaU {w u : BringCone R} (hw : Quaternion.normSq w = 1)
    (hanti : w * u = -(u * w)) (p : BringCone R) :
    leftMul w (chiralGammaU u (leftMul (star w) p)) = -chiralGammaU u p := by
  rw [leftMul_conj_chiralGammaU, conjBy_neg_of_anticomm hw hanti, chiralGammaU_neg]

/-- The instance `w = j`, `u = i`: the half-turn about `j` flips `Γ_i`. -/
theorem leftMul_unitJ_flips_chiralGamma_i (p : BringCone R) :
    leftMul unitJ (chiralGammaU unitI (leftMul (star unitJ) p)) = -chiralGammaU unitI p := by
  refine leftMul_flips_chiralGammaU ?_ ?_ p
  · rw [Quaternion.normSq_def']; simp [unitJ]
  · ext <;> simp [unitI, unitJ]

end QOU.Tetraplectic
