import Mathlib.Data.Nat.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases


/-!
# QOU.Torsion.torus_knot_generators_finite

The Euler characteristic χ(A) = -6 (genus 4) forces the torus knot
generator set 𝒢 to be finite: only T_{m,n} with (m-1)(n-1) ≤ 8 embed.

LaTeX label: `prop:torus-knot-generators`
-/

namespace QOU.Torsion

/-- Seifert genus of a torus knot T_{m,n} with gcd(m,n) = 1. -/
def seifertGenus (m n : ℕ) : ℕ := (m - 1) * (n - 1) / 2

/-- The torus knot T_{m,n} embeds in a surface of genus g iff
    its Seifert genus ≤ g. For Bring's surface (g = 4),
    the constraint (m-1)(n-1) ≤ 8 selects a finite set. -/
-- Ref: [leitner2026] Ch. 5, §torus-knot-generators
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem torus_knot_generators_finite
    (g : ℕ) (hg : g = 4)
    : ∃ (S : Finset (ℕ × ℕ)),
        ∀ m n, m ≥ 2 → n > m → Nat.Coprime m n →
          seifertGenus m n ≤ g → (m, n) ∈ S := by
  -- Ref: [leitner2026] Ch. 5, §torus-knot-generators
  -- Any finite set containing the 6 solutions suffices as a witness.
  subst hg
  exact ⟨{(2,3), (2,5), (2,7), (2,9), (3,4), (3,5)}, fun m n hm hmn hcop hg => by
    simp only [Finset.mem_insert, Prod.mk.injEq, Finset.mem_singleton]
    unfold seifertGenus at hg
    -- (m-1)(n-1)/2 ≤ 4 ⟹ (m-1)(n-1) ≤ 9 (Nat division by 2 rounds down).
    have hprod : (m - 1) * (n - 1) ≤ 9 := by omega
    -- With m ≥ 2 (so m-1 ≥ 1) and n > m (so n-1 ≥ 1), each factor is bounded
    -- by the product, giving m ≤ 10, n ≤ 10.
    have hm1 : 0 < m - 1 := by omega
    have hn1 : 0 < n - 1 := by omega
    -- Each factor is ≤ the product (the other factor is positive).
    have hmf : m - 1 ≤ (m - 1) * (n - 1) := Nat.le_mul_of_pos_right _ hn1
    have hnf : n - 1 ≤ (m - 1) * (n - 1) := Nat.le_mul_of_pos_left _ hm1
    have hm_le : m ≤ 10 := by omega
    have hn_le : n ≤ 10 := by omega
    interval_cases m <;> interval_cases n <;> simp_all [Nat.Coprime] <;> omega⟩

end QOU.Torsion
