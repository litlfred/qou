import Mathlib.Data.Nat.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Set.Finite.Basic

/-!
# QOU.Torsion.torus_knot_generators_finite

For any surface of genus `g`, a nontrivial coprime torus knot `T_{m,n}`
(`2 ≤ m < n`, `gcd(m, n) = 1`) has Seifert genus `g(T_{m,n}) = (m - 1)(n - 1) / 2`
satisfying `2 · g(T_{m,n}) = (m - 1)(n - 1)` (since coprime `m, n` cannot both
be even).  The embeddability bound `g(T_{m,n}) ≤ g` is therefore equivalent to
`(m - 1)(n - 1) ≤ 2g`, forcing `m ≤ 2g + 1` and `n ≤ 2g + 1`, so the set of
coprime torus-knot generators is finite for **every** `g : ℕ`.

Specialising to Bring's surface (`g = 4`, `χ_eu = 2 - 2g = -6`), the bound
`(m - 1)(n - 1) ≤ 8` selects the exact six-element coprime torus-knot set
`{(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)}`, and together with the
unknot `T_{1,0} = (1, 0)` the full generator set `𝒢` has cardinality `7`.

LaTeX label: `prop:torus-knot-generators`
-/

namespace QOU.Torsion

/-- Seifert genus `g(T_{m,n}) = (m - 1)(n - 1) / 2` of a torus knot `T_{m,n}`. -/
def seifertGenus (m n : ℕ) : ℕ := (m - 1) * (n - 1) / 2

/-- Coprime natural numbers cannot both be even, so at least one is odd. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem coprime_odd_left_or_right {m n : ℕ} (hcop : Nat.Coprime m n) :
    m % 2 = 1 ∨ n % 2 = 1 := by
  by_contra h
  push_neg at h
  have hm2 : 2 ∣ m := Nat.dvd_of_mod_eq_zero (by omega)
  have hn2 : 2 ∣ n := Nat.dvd_of_mod_eq_zero (by omega)
  have h21 : 2 ∣ 1 := hcop.gcd_eq_one ▸ Nat.dvd_gcd hm2 hn2
  omega

/-- Because at least one of two coprime parameters `m, n` is odd, `(m - 1)(n - 1)`
    is always even, so `2 * seifertGenus m n = (m - 1) * (n - 1)` holds with no
    integer-division rounding loss. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem two_mul_seifertGenus_of_coprime {m n : ℕ} (hcop : Nat.Coprime m n) :
    2 * seifertGenus m n = (m - 1) * (n - 1) := by
  unfold seifertGenus
  rcases Nat.eq_zero_or_pos m with rfl | hmpos
  · simp
  rcases Nat.eq_zero_or_pos n with rfl | hnpos
  · simp
  have hdvd : 2 ∣ (m - 1) * (n - 1) := by
    rcases coprime_odd_left_or_right hcop with hm_odd | hn_odd
    · exact dvd_mul_of_dvd_left ⟨(m - 1) / 2, by omega⟩ (n - 1)
    · exact dvd_mul_of_dvd_right ⟨(n - 1) / 2, by omega⟩ (m - 1)
  exact Nat.mul_div_cancel' hdvd

/-- Explicit parameter bounds for any coprime torus knot `T_{m,n}` (`2 ≤ m < n`)
    with Seifert genus `g(T_{m,n}) ≤ g`:
    `(m - 1)(n - 1) ≤ 2g`, `m ≤ 2g + 1`, and `n ≤ 2g + 1`. -/
-- Ref: [leitner2026] Ch. 5, §torus-knot-generators
theorem torus_knot_bounds_of_seifertGenus_le {g m n : ℕ}
    (hm : 2 ≤ m) (hmn : m < n) (hcop : Nat.Coprime m n)
    (hg : seifertGenus m n ≤ g) :
    (m - 1) * (n - 1) ≤ 2 * g ∧ m ≤ 2 * g + 1 ∧ n ≤ 2 * g + 1 := by
  have h2 : 2 * seifertGenus m n = (m - 1) * (n - 1) :=
    two_mul_seifertGenus_of_coprime hcop
  have hprod : (m - 1) * (n - 1) ≤ 2 * g := by omega
  have hn1_le : n - 1 ≤ (m - 1) * (n - 1) := by
    simpa using Nat.mul_le_mul_right (n - 1) (by omega : 1 ≤ m - 1)
  refine ⟨hprod, by omega, by omega⟩

/-- The set of nontrivial coprime torus-knot parameter pairs `(m, n)` (`2 ≤ m < n`,
    `gcd(m, n) = 1`) whose Seifert genus is at most `g`. -/
def torusKnotPairs (g : ℕ) : Set (ℕ × ℕ) :=
  { pq | 2 ≤ pq.1 ∧ pq.1 < pq.2 ∧ Nat.Coprime pq.1 pq.2 ∧ seifertGenus pq.1 pq.2 ≤ g }

/-- Computable finite enumeration of all coprime torus-knot generators up to
    Seifert genus `g`, cut out inside `[2, 2g + 1] × [2, 2g + 1]`. -/
def torusKnotFinset (g : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.Icc 2 (2 * g + 1) ×ˢ Finset.Icc 2 (2 * g + 1)).filter
    (fun pq => pq.1 < pq.2 ∧ Nat.Coprime pq.1 pq.2 ∧ seifertGenus pq.1 pq.2 ≤ g)

/-- Exact equivalence between membership in the computable `torusKnotFinset g`
    and the mathematical set `torusKnotPairs g`, valid for all `g : ℕ`. -/
-- Ref: [leitner2026] Ch. 5, §torus-knot-generators
theorem mem_torusKnotFinset_iff (g : ℕ) (pq : ℕ × ℕ) :
    pq ∈ torusKnotFinset g ↔ pq ∈ torusKnotPairs g := by
  unfold torusKnotFinset torusKnotPairs
  simp only [Finset.mem_filter, Finset.mem_product, Finset.mem_Icc, Set.mem_setOf_eq]
  constructor
  · rintro ⟨⟨⟨hm, _⟩, _⟩, hmn, hcop, hg⟩
    exact ⟨hm, hmn, hcop, hg⟩
  · rintro ⟨hm, hmn, hcop, hg⟩
    obtain ⟨_, hm_ub, hn_ub⟩ := torus_knot_bounds_of_seifertGenus_le hm hmn hcop hg
    exact ⟨⟨⟨hm, hm_ub⟩, ⟨by omega, hn_ub⟩⟩, hmn, hcop, hg⟩

/-- **Finiteness of the `T_{m,n}` generator set** (`prop:torus-knot-generators`):
    for **every** surface genus `g : ℕ`, the set `torusKnotPairs g` of coprime
    torus knots `T_{m,n}` (`2 ≤ m < n`, `gcd(m, n) = 1`, `g(T_{m,n}) ≤ g`) is
    finite (`Set.Finite`), witnessed explicitly by `torusKnotFinset g`. -/
-- Ref: [leitner2026] Ch. 5, §torus-knot-generators
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem torus_knot_generators_finite (g : ℕ) :
    (torusKnotPairs g).Finite ∧
    ∃ (S : Finset (ℕ × ℕ)),
      ∀ m n, 2 ≤ m → m < n → Nat.Coprime m n →
        seifertGenus m n ≤ g → (m, n) ∈ S := by
  have hfin : (torusKnotPairs g).Finite := by
    refine (torusKnotFinset g).finite_toSet.subset ?_
    intro pq hpq
    exact Finset.mem_coe.mpr ((mem_torusKnotFinset_iff g pq).mpr hpq)
  refine ⟨hfin, torusKnotFinset g, ?_⟩
  intro m n hm hmn hcop hg
  exact (mem_torusKnotFinset_iff g (m, n)).mpr ⟨hm, hmn, hcop, hg⟩

/-- The six nontrivial coprime torus knots `(m, n)` satisfying
    `(m - 1)(n - 1) ≤ 8` on Bring's surface (`g = 4`, `χ_eu = -6`). -/
def bringsTorusKnotFinset : Finset (ℕ × ℕ) :=
  {(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)}

/-- Full torus-knot seed set `𝒢` at genus `g`, adjoining the unknot `T_{1,0} = (1, 0)`
    to `torusKnotFinset g`. -/
def fullTorusGeneratorFinset (g : ℕ) : Finset (ℕ × ℕ) :=
  insert (1, 0) (torusKnotFinset g)

/-- **Exact enumeration at Bring's genus `g = 4`**:
    `torusKnotFinset 4` consists of the exact six coprime pairs
    `{(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)}`, and adjoining the
    unknot `T_{1,0} = (1, 0)` gives `|𝒢| = 7`. -/
-- Ref: [leitner2026] Ch. 5, §torus-knot-generators
theorem brings_torus_knot_generators_eq :
    torusKnotFinset 4 = bringsTorusKnotFinset ∧
    (torusKnotFinset 4).card = 6 ∧
    (1, 0) ∉ torusKnotFinset 4 ∧
    (fullTorusGeneratorFinset 4).card = 7 := by
  decide

end QOU.Torsion
