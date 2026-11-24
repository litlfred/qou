import Mathlib.Tactic

/-!
# The Bring genus bound picks one full twist

`TorusFamilyTrace` shows that `T(3, 3m+2) = electron^(2m+1) · σ₁` for every `m`, and
that the algebra does not prefer any `m`. This file records what the corpus's genus
rule says about the same family.

The Seifert genus of the torus knot `T(p, q)` is `(p−1)(q−1)/2`. This is the same
formula as `QOU.Torsion.seifertGenus` in `brings-surface/torus-knot-generators.lean`,
restated here so that this file imports only Mathlib.

* Electron family `T(3, 3m+2)`: genus `3m + 1`. The bound `g ≤ 4 = g(Bring)` allows
  `m ∈ {0, 1}`, and `g = 4` holds only at `m = 1`, which is `T(3,5)`.
* Backup-electron family `T(2, 2m+1) = σ₀^(2m+1)`: genus `m`, and `g = 4` holds only at
  `m = 4`, which is `T(2,9)`.

These are statements about a formula. The genus-4 rule itself comes from the corpus
(`rem:bring-embeddable-knots`, and the "saturating carriers" of the electroweak blocks).
This file does not derive it.
-/

namespace QOU.AlphaEM.TorusGenus

-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds" (torus-knot genus)
/-- Seifert genus of the torus knot `T(p, q)`. -/
def seifertGenus (p q : ℕ) : ℕ := (p - 1) * (q - 1) / 2

theorem electronFamily_genus (m : ℕ) : seifertGenus 3 (3 * m + 2) = 3 * m + 1 := by
  unfold seifertGenus; omega

theorem electronFamily_bring_iff (m : ℕ) : seifertGenus 3 (3 * m + 2) ≤ 4 ↔ m ≤ 1 := by
  rw [electronFamily_genus]; omega

theorem electronFamily_saturates_iff (m : ℕ) : seifertGenus 3 (3 * m + 2) = 4 ↔ m = 1 := by
  rw [electronFamily_genus]; omega

theorem backupFamily_genus (m : ℕ) : seifertGenus 2 (2 * m + 1) = m := by
  unfold seifertGenus; omega

theorem backupFamily_saturates_iff (m : ℕ) : seifertGenus 2 (2 * m + 1) = 4 ↔ m = 4 := by
  rw [backupFamily_genus]

end QOU.AlphaEM.TorusGenus
