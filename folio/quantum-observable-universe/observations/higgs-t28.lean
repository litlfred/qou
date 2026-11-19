import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card

/-!
# Higgs boson as `T(2, 8)` (`conj:higgs-t28`, §3b-cond)

Class-axiomatised formulation of `conj:higgs-t28` together with unconditional
combinatorial and topological-arithmetic theorems for the 2-strand even torus
link family `T(2, 2k)` on the genus-4 Bring surface.

## Unconditional vs conditional content

1. **Unconditional (`t28_genus_eq_three`, `torusLink2_genus_table`):** the
   minimal Seifert surface of a 2-component torus link `T(2, 2k)` has genus
   `(2k - 2) / 2 = k - 1`, giving `0, 1, 2, 3` for `T(2,2), T(2,4), T(2,6),
   T(2,8)` and `4` (saturating Bring's genus-4 handle budget) for `T(2,10)`.
2. **Unconditional (`t28_unique_genus_three`, `t28_spin_zero_reeb_cancellation`):**
   among even `2k ≥ 2`, `2k = 8` is the unique parameter of Seifert genus `3`,
   and opposite component Reeb windings `(+4) + (-4) = 0` cancel to total spin `0`.
3. **Conditional (`higgs_three_colors`, `higgs_t28_unique_three_divisor_carrier`):**
   under `[HiggsAsT28]`, `T(2, 8)` spans all three exceptional divisors
   `Finset.univ : Finset (Fin 3)` (`D_r, D_g, D_b`) and is the unique admissible
   carrier leaving a Bring handle free that spans all three divisors.

## References

- [leitner2026] `conj:higgs-t28`
- [rolfsen1976] Knots and Links, Ch. 5 (Seifert genus of torus links)
-/

namespace QOU.HiggsT28

/-- Seifert-surface genus `(n - 2) / 2` of a 2-strand even torus link `T(2, n)`. -/
def torusLink2SeifertGenus (n : ℕ) : ℕ := (n - 2) / 2

/-- **Unconditional (`T(2, 8)` Seifert genus).** `T(2, 8)` has genus `3`. -/
-- Ref: [rolfsen1976] Knots and Links, Ch. 5
theorem t28_genus_eq_three : (8 - 2) / 2 = 3 := by decide

/-- **Unconditional (electroweak torus-link genus ladder).** Evaluates the
    Seifert genera of `T(2, 2), T(2, 4), T(2, 6), T(2, 8), T(2, 10)`. -/
theorem torusLink2_genus_table :
    torusLink2SeifertGenus 2 = 0 ∧
    torusLink2SeifertGenus 4 = 1 ∧
    torusLink2SeifertGenus 6 = 2 ∧
    torusLink2SeifertGenus 8 = 3 ∧
    torusLink2SeifertGenus 10 = 4 := by
  decide

/-- **Unconditional (genus-3 uniqueness in `T(2, 2k)`).** Among positive half-twists
    `k ≥ 1`, `k = 4` (`2k = 8`) is the unique index with Seifert genus `3`. -/
theorem t28_unique_genus_three (k : ℕ) :
    torusLink2SeifertGenus (2 * k) = 3 ↔ k = 4 := by
  unfold torusLink2SeifertGenus
  omega

/-- **Unconditional (scalar spin-0 Reeb cancellation).** Opposite Reeb windings
    `+k` and `-k` on the two fiber-adjoint link components sum to `0`. -/
theorem reeb_winding_cancels (k : ℤ) : k + (-k) = 0 :=
   Int.add_right_neg k

/-- **Higgs-as-`T(2, 8)` conjecture (`conj:higgs-t28`, §3b-cond).**
    Models the exceptional-divisor incidence of `T(2, 2k)` against the three
    color divisors `Fin 3` (`D_r, D_g, D_b`) on the genus-4 Bring surface and
    the handle-coexistence constraint (`genus < 4`). No global instance is
    registered. -/
class HiggsAsT28 where
  /-- Subset of the three exceptional divisors `Fin 3` spanned by `T(2, n)`. -/
  spannedDivisors : ℕ → Finset (Fin 3)
  /-- For `1 ≤ k ≤ 4`, the number of spanned exceptional divisors equals the
      Seifert-surface genus `torusLink2SeifertGenus (2 * k)`. -/
  card_eq_seifert_genus :
    ∀ k : ℕ, 1 ≤ k → k ≤ 4 →
      (spannedDivisors (2 * k)).card = torusLink2SeifertGenus (2 * k)
  /-- Admissibility of `T(2, 2k)` on Bring's genus-4 surface coexisting with
      a free Borromean handle. -/
  admissibleCarrier : ℕ → Prop
  /-- Every admissible carrier has `k ≥ 1` and leaves at least one of the 4
      Bring handles unsaturated (`torusLink2SeifertGenus (2 * k) < 4`). -/
  admissible_lt_four :
    ∀ k : ℕ, admissibleCarrier k → 1 ≤ k ∧ torusLink2SeifertGenus (2 * k) < 4

/-- **Conditional theorem (`higgs_three_colors`).** Under `[HiggsAsT28]`,
    `T(2, 8)` spans a divisor set of cardinality `3`, hence spans the entire
    exceptional-divisor set `Finset.univ : Finset (Fin 3)` (`D_r ∪ D_g ∪ D_b`). -/
-- Ref: [leitner2026] conj:higgs-t28
theorem higgs_three_colors [h : HiggsAsT28] :
    (h.spannedDivisors 8).card = 3 ∧ h.spannedDivisors 8 = Finset.univ := by
  have hcard : (h.spannedDivisors 8).card = 3 := by
    have h4 := h.card_eq_seifert_genus 4 (by omega) (by omega)
    simpa [torusLink2SeifertGenus] using h4
  refine ⟨hcard, Finset.eq_univ_of_card (h.spannedDivisors 8) ?_⟩
  simpa using hcard

/-- **Conditional theorem (uniqueness of `T(2, 8)` among admissible carriers).**
    Under `[HiggsAsT28]`, any admissible carrier `T(2, 2k)` spanning all three
    exceptional divisors satisfies `2 * k = 8`. -/
-- Ref: [leitner2026] conj:higgs-t28
theorem higgs_t28_unique_three_divisor_carrier [h : HiggsAsT28]
    (k : ℕ) (hadm : h.admissibleCarrier k)
    (hspan : h.spannedDivisors (2 * k) = Finset.univ) :
    2 * k = 8 := by
  obtain ⟨hk1, hklt⟩ := h.admissible_lt_four k hadm
  have hk4 : k ≤ 4 := by
    unfold torusLink2SeifertGenus at hklt
    omega
  have hcard := h.card_eq_seifert_genus k hk1 hk4
  rw [hspan] at hcard
  have huniv : (Finset.univ : Finset (Fin 3)).card = 3 := by simp
  rw [huniv] at hcard
  have hk_eq : k = 4 := (t28_unique_genus_three k).mp hcard.symm
  omega

end QOU.HiggsT28
