/-!
# QOU.Descartes.QMomentum — q-Momentum from braid writhe

The q-momentum of a particle is the Hecke-weighted writhe of its
braid representative.  At q=1 this reduces to the classical writhe.

LaTeX label: `def:q-momentum`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] §6/q-momentum
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

namespace QOU.Descartes

/-- The q-momentum of a braid, computed from its crossing signs.
    Each positive crossing contributes +1, each negative contributes -1,
    weighted by q-deformation. -/
-- Ref: [manuscript] §6/q-momentum
noncomputable def qMomentum (q : ℝ) (crossingSigns : List ℤ) : ℝ :=
  crossingSigns.foldl (fun acc ε =>
    acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0

/-- At q = 1, q-momentum equals the writhe (sum of signs). -/
-- Ref: [manuscript] §6/q-momentum
-- The limit q → 1 of (q^{2ε} - 1)/(q² - 1) = ε by L'Hôpital.
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem qMomentum_classical_limit (signs : List ℤ) :
    -- In the q → 1 limit, each term (q^{2ε} - 1)/(q² - 1) → ε
    -- So q-momentum → writhe = Σε
    ∀ ε > 0, ∃ δ > 0, ∀ q : ℝ, 0 < |q - 1| → |q - 1| < δ →
      |qMomentum q signs - (signs.foldl (fun acc s => acc + ↑s) (0 : ℝ))| < ε := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Each term (q^{2ε} - 1)/(q² - 1) → ε by L'Hôpital as q → 1
  -- Ref: [manuscript] Ch. 6, §q-momentum
  sorry

/-- The writhe of a braid word (sum of crossing signs). -/
-- Ref: [manuscript] §6/q-momentum
def writhe (crossingSigns : List ℤ) : ℤ :=
  crossingSigns.foldl (· + ·) 0

/-- Trefoil writhe = +3. -/
-- Ref: [manuscript] §6/q-momentum
example : writhe [1, 1, 1] = 3 := by decide

/-- Figure-eight writhe = 0 (amphichiral). -/
-- Ref: [manuscript] §6/q-momentum
example : writhe [1, -1, 1, -1] = 0 := by decide

/-- Mirror reversal negates the writhe. -/
-- Ref: [manuscript] §6/q-momentum
theorem writhe_mirror (signs : List ℤ) :
    writhe (signs.map (· * (-1))) = -writhe signs := by
  unfold writhe
  induction signs with
  | nil => simp [List.foldl]
  | cons s ss ih =>
    simp only [List.map_cons, List.foldl]
    -- Need a helper: foldl (· + ·) a (map (· * -1) l) = -foldl (· + ·) (-a) l... not quite
    -- Actually let's try a different approach with a general accumulator
    suffices h : ∀ (acc : ℤ) (l : List ℤ),
      List.foldl (· + ·) acc (l.map (· * (-1))) = -(List.foldl (· + ·) (-acc) l) by
      simpa using h 0 (s :: ss)
    intro acc l
    induction l generalizing acc with
    | nil => simp [List.foldl]
    | cons x xs ih =>
      simp only [List.map_cons, List.foldl]
      rw [ih]
      ring_nf

end QOU.Descartes
