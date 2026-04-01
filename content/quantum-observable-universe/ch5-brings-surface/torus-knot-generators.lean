/-!
# QOU.Torsion.torus_knot_generators_finite

The Euler characteristic χ(A) = -6 (genus 4) forces the torus knot
generator set 𝒢 to be finite: only T_{m,n} with (m-1)(n-1) ≤ 8 embed.

LaTeX label: `prop:torus-knot-generators`
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Finset.Basic

namespace QOU.Torsion

/-- Seifert genus of a torus knot T_{m,n} with gcd(m,n) = 1. -/
def seifertGenus (m n : ℕ) : ℕ := (m - 1) * (n - 1) / 2

/-- The torus knot T_{m,n} embeds in a surface of genus g iff
    its Seifert genus ≤ g. For Bring's surface (g = 4),
    the constraint (m-1)(n-1) ≤ 8 selects a finite set. -/
-- Ref: [manuscript] Ch. 5, §torus-knot-generators
-- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
theorem torus_knot_generators_finite
    (g : ℕ) (hg : g = 4)
    : ∃ (S : Finset (ℕ × ℕ)),
        ∀ m n, m ≥ 2 → n > m → Nat.Coprime m n →
          seifertGenus m n ≤ g → (m, n) ∈ S := by
  -- Ref: [manuscript] Ch. 5, §torus-knot-generators
  sorry

end QOU.Torsion
