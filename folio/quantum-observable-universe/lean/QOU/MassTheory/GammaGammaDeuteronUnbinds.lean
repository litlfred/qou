import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# The γγ bond alone unbinds the deuteron, for every q > 1

Bean `qou-sv7h`. Scope: the deuteron word of
`computations/probes/light_nuclei_a2_a3/hecke_flint.py` (`atom_word("pn", [(0, 1)], "over")`):
a proton block and a neutron block on three strands each, joined by one γγ bond
`V³ = (σ₀σ₁⁻¹)³` (owner rulings 2026-11-20 photon form, 2026-11-22 γγ bond), traced with the
convention-D Ocneanu trace `z = q³/(q²+1)`.

**What is proved here and what is not.** The three closed forms `trP`, `trN`, `trAtom` below are
the exact traces as rational functions of `q`, computed symbolically by
`computations/probes/light_nuclei_a2_a3/deuteron_closed_form_probe.py` (exact arithmetic in
`ℚ[q, q⁻¹, (q²+1)⁻¹]`, cross-checked against the independent permutation-basis engine
`hecke_flint` at several rational `q`). Lean does **not** derive them from the Hecke algebra; it
takes them as definitions and proves:

* `ratio_eq`: `trAtom / (trP · trN) = mA(q²) / (q²(q²+1) nN(q²))`;
* `ratio_sub_one`: that ratio minus one equals `(q²−1)⁵ (q⁸+q⁴+1) / (q²(q²+1) nN(q²))`;
* `one_lt_ratio`: the ratio exceeds `1` for every `q > 1`.

Under the log law `B = E₀ · log(tr_free / tr_atom)` (owner ruling 2026-11-25) a ratio above one
is a negative binding. So within this word and this trace the γγ bond **cannot** bind the
deuteron at any `q > 1`; this is a scope-(b) exclusion for the bond alone, with the invariant
being the sign of `(q²−1)⁵` times polynomials whose shifted coefficients are all positive. It says
nothing about a closure with further terms. The factor `(q²−1)⁵` is also why the magnitude at
`q₀ ≈ 1.11` is small (ratio `1.00061`).

Base ring: any ordered field (§7c), since the statement needs the order.
-/

namespace QOU.MassTheory.GammaGammaDeuteron

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Numerator polynomial of the proton-block trace, in `x = q²`. -/
def mP (x : R) : R :=
  x ^ 9 - 3 * x ^ 8 + 7 * x ^ 7 - 8 * x ^ 6 + 10 * x ^ 5 - 9 * x ^ 4 + 10 * x ^ 3
    - 6 * x ^ 2 + 3 * x - 1

/-- Numerator polynomial of the neutron-block trace, in `x = q²`. -/
def nN (x : R) : R :=
  x ^ 7 - 3 * x ^ 6 + 4 * x ^ 5 - 4 * x ^ 4 + 5 * x ^ 3 - 4 * x ^ 2 + 3 * x - 1

/-- The extra numerator factor of the bonded deuteron trace, in `x = q²`. -/
def mA (x : R) : R :=
  2 * x ^ 9 - 7 * x ^ 8 + 12 * x ^ 7 - 15 * x ^ 6 + 17 * x ^ 5 - 15 * x ^ 4 + 14 * x ^ 3
    - 9 * x ^ 2 + 4 * x - 1

/-- Convention-D trace of the proton block (closed form from the probe). -/
def trP (q : R) : R := (q ^ 4 + 1) * mP (q ^ 2) / (4 * q ^ 9 * (q ^ 2 + 1) ^ 2)

/-- Convention-D trace of the neutron block (closed form from the probe). -/
def trN (q : R) : R := (q ^ 4 + 1) * nN (q ^ 2) / (4 * q ^ 9)

/-- Convention-D trace of the γγ-bonded deuteron word (closed form from the probe). -/
def trAtom (q : R) : R :=
  (q ^ 4 + 1) ^ 2 * mP (q ^ 2) * mA (q ^ 2) / (16 * q ^ 20 * (q ^ 2 + 1) ^ 3)

lemma mP_pos {x : R} (hx : 1 ≤ x) : 0 < mP x := by
  obtain ⟨t, ht, rfl⟩ : ∃ t : R, 0 ≤ t ∧ x = 1 + t := ⟨x - 1, by linarith, by ring⟩
  have h : mP (1 + t) = t ^ 9 + 6 * t ^ 8 + 19 * t ^ 7 + 41 * t ^ 6 + 67 * t ^ 5 + 82 * t ^ 4
      + 75 * t ^ 3 + 49 * t ^ 2 + 21 * t + 4 := by unfold mP; ring
  rw [h]; linarith [pow_nonneg ht 2, pow_nonneg ht 3, pow_nonneg ht 4, pow_nonneg ht 5, pow_nonneg ht 6, pow_nonneg ht 7, pow_nonneg ht 8, pow_nonneg ht 9]

lemma nN_pos {x : R} (hx : 1 ≤ x) : 0 < nN x := by
  obtain ⟨t, ht, rfl⟩ : ∃ t : R, 0 ≤ t ∧ x = 1 + t := ⟨x - 1, by linarith, by ring⟩
  have h : nN (1 + t) = t ^ 7 + 4 * t ^ 6 + 7 * t ^ 5 + 6 * t ^ 4 + 4 * t ^ 3 + 3 * t ^ 2
      + 3 * t + 1 := by unfold nN; ring
  rw [h]; linarith [pow_nonneg ht 2, pow_nonneg ht 3, pow_nonneg ht 4, pow_nonneg ht 5, pow_nonneg ht 6, pow_nonneg ht 7, pow_nonneg ht 8, pow_nonneg ht 9]

lemma mA_pos {x : R} (hx : 1 ≤ x) : 0 < mA x := by
  obtain ⟨t, ht, rfl⟩ : ∃ t : R, 0 ≤ t ∧ x = 1 + t := ⟨x - 1, by linarith, by ring⟩
  have h : mA (1 + t) = 2 * t ^ 9 + 11 * t ^ 8 + 28 * t ^ 7 + 41 * t ^ 6 + 39 * t ^ 5
      + 27 * t ^ 4 + 20 * t ^ 3 + 16 * t ^ 2 + 9 * t + 2 := by unfold mA; ring
  rw [h]; linarith [pow_nonneg ht 2, pow_nonneg ht 3, pow_nonneg ht 4, pow_nonneg ht 5, pow_nonneg ht 6, pow_nonneg ht 7, pow_nonneg ht 8, pow_nonneg ht 9]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The polynomial identity behind the sign: `mA(x) − x(x+1) nN(x) = (x−1)⁵ (x⁴+x²+1)`. -/
lemma mA_sub (x : R) : mA x - x * (x + 1) * nN x = (x - 1) ^ 5 * (x ^ 4 + x ^ 2 + 1) := by
  unfold mA nN; ring

lemma one_le_sq {q : R} (hq : 1 < q) : 1 ≤ q ^ 2 := by nlinarith

lemma ratio_eq {q : R} (hq : 1 < q) :
    trAtom q / (trP q * trN q) = mA (q ^ 2) / (q ^ 2 * (q ^ 2 + 1) * nN (q ^ 2)) := by
  have h0 : (0 : R) < q := by linarith
  have hP := (mP_pos (one_le_sq hq)).ne'
  have hN := (nN_pos (one_le_sq hq)).ne'
  have h4 : q ^ 4 + 1 ≠ 0 := by positivity
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq0 : q ≠ 0 := h0.ne'
  unfold trAtom trP trN
  field_simp
  ring

theorem ratio_sub_one {q : R} (hq : 1 < q) :
    trAtom q / (trP q * trN q) - 1
      = (q ^ 2 - 1) ^ 5 * (q ^ 8 + q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1) * nN (q ^ 2)) := by
  rw [ratio_eq hq]
  have hN := (nN_pos (one_le_sq hq)).ne'
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq0 : q ≠ 0 := by intro h; rw [h] at hq; linarith
  have key := mA_sub (q ^ 2)
  rw [div_sub_one (mul_ne_zero (mul_ne_zero (pow_ne_zero 2 hq0) h2) hN)]
  congr 1
  linear_combination key

/-- **The γγ bond alone raises the deuteron trace for every `q > 1`**, so under the log law it
unbinds. -/
theorem one_lt_ratio {q : R} (hq : 1 < q) : 1 < trAtom q / (trP q * trN q) := by
  have h := ratio_sub_one hq
  have hN := nN_pos (one_le_sq hq)
  have hs : (0 : R) < q ^ 2 - 1 := by nlinarith
  have hq2 : (0 : R) < q ^ 2 := pow_pos (by linarith) 2
  have hpos : 0 < (q ^ 2 - 1) ^ 5 * (q ^ 8 + q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1) * nN (q ^ 2)) :=
    div_pos (mul_pos (pow_pos hs 5) (by positivity)) (mul_pos (mul_pos hq2 (by positivity)) hN)
  linarith

end QOU.MassTheory.GammaGammaDeuteron
