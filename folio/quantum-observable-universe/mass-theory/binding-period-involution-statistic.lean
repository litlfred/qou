import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Units
import Mathlib.Data.Multiset.Basic
import Mathlib.Tactic.Ring
import QOU.Mathlib.SchenstedInsertion

/-!
# QOU.Mass — the balanced dimension sum as an involution statistic

For `n ≥ 1` the balanced dimension sum `S^bal(n; q) = Σ_{λ⊢n} dim_q^bal(λ)`
(the q-analogue of the involution count `I(n)`, the numerator of the binding
period `a_D^(n) = I(n)/n` at `q = 1`) satisfies

  S^bal(n; q) · q^{n(n−1)/2} = Σ_{w ∈ Inv(Sₙ)} q^{2·maj(w) + content(λ(w))},

where `λ(w)` is the RSK shape of the involution `w`, `maj` the major index and
`content(λ) = Σ_{(i,j)∈λ} (j − i)`. LaTeX label:
`prop:binding-period-involution-statistic`.

## Lean structure — machine-checked instances, cited general proof

The statistic side is **fully computable** here: words, involution filter,
major index, RSK shape via the Schensted brick (`QOU.Mathlib.Schensted
.insertWord`), and content of a shape. The exponent multisets are decided by
the kernel (`statExponents_three/_four`), and the proposition's identity is
then proved **sorry-free** for `n = 3` and `n = 4` against the explicitly
expanded balanced side (`binding_period_involution_statistic_three/_four`).

The general-`n` statement composes three classical results — Stanley's
q-hook-maj formula, RSK/Schützenberger descent preservation on involutions,
and the balanced-convention twist `dim_q^bal(λ) = q^{content(λ)−n(n−1)/2}
·f̃^λ(q²)` — and its narrative proof lives in the proof block; it is NOT
restated here as a Lean declaration because the balanced side requires
partition/hook machinery not yet formalized (no `sorry` masquerading as a
general theorem; the decided instances are exactly what is machine-checked).
Exact symbolic verification to `n = 8` (764 involutions):
`computations/lever1_kernel_maj_involution_identification.py`; the transfer
operator built on this statistic:
`computations/lever1_descent_transfer_operator.py`.

## References

- [stanley1999] Enumerative Combinatorics 2 (q-hook-maj / fake degrees)
- [sagan2001] The Symmetric Group (RSK, Schützenberger `Des(w) = Des(P(w))`)
- [leitner2026] §mass-theory/binding-period-involution-statistic

## Ground ring (§7c) — a `CommRing` with `q` carried as a unit

The decided combinatorics is ring-free. The polynomial instances are *Laurent
identities*: the balanced side carries `q⁻¹`, but nothing here ever divides by
a quantity that might vanish, so a field is not needed. Carrying `q : Rˣ` and
reading both sides into `R` through the unit coercion puts the instances on
`ℤ[q, q⁻¹] = LaurentPolynomial ℤ`, where these q-dimensions actually live, and
the single algebraic input is the *unit* cancellation `q⁻¹ · q = 1`
(`Units.inv_mul`) rather than `field_simp`.

This is strictly stronger than the earlier `[Field K]` + `q ≠ 0` form:
instantiate `R := K`, `q := Units.mk0 q hq` to recover it.
-/

namespace QOU.Mass
namespace BindingInvolutionStatistic

open QOU.Mathlib.Schensted

/-- Insert `x` into every position of a word (structural recursion, so the
kernel can evaluate it inside `decide` — `List.permutations` is well-founded-
recursive and does not kernel-reduce). -/
def insertAll (x : ℕ) : List ℕ → List (List ℕ)
  | [] => [[x]]
  | y :: ys => (x :: y :: ys) :: (insertAll x ys).map (y :: ·)

/-- All permutations of a word, by successive insertion (structural). -/
def perms : List ℕ → List (List ℕ)
  | [] => [[]]
  | x :: xs => (perms xs).flatMap (insertAll x)

/-- The word `[1, …, n]` (structural). -/
def upTo : ℕ → List ℕ
  | 0 => []
  | n + 1 => upTo n ++ [n + 1]

/-- All one-line words of `Sₙ` on the letters `1..n`. -/
def words (n : ℕ) : List (List ℕ) := perms (upTo n)

/-- `w` is an involution: `w(w(i)) = i` at every position (1-based letters). -/
def isInvolution (w : List ℕ) : Bool :=
  (List.range w.length).all fun i => w.getD (w.getD i 0 - 1) 0 == i + 1

/-- Major index of a word: the sum of the (1-based) descent positions. -/
def majW (w : List ℕ) : ℕ :=
  (List.range (w.length - 1)).foldl
    (fun acc i => if w.getD (i + 1) 0 < w.getD i 0 then acc + (i + 1) else acc) 0

/-- RSK shape of a word: row lengths of its Schensted insertion tableau. -/
def shape (w : List ℕ) : List ℕ := (insertWord w).map List.length

/-- Content of a shape `λ` (row lengths, top row first):
`Σ_{(i,j)∈λ} (j − i) = Σ_i (λᵢ(λᵢ−1)/2 − i·λᵢ)`, 0-based `i, j`. -/
def shapeContent (s : List ℕ) : ℤ :=
  (List.range s.length).foldl
    (fun acc i =>
      acc + (s.getD i 0 * (s.getD i 0 - 1) / 2 : ℕ) - (i : ℤ) * (s.getD i 0 : ℕ))
    0

/-- The involution-statistic exponent multiset at level `n`:
`{2·maj(w) + content(λ(w)) : w ∈ Inv(Sₙ)}`. -/
def statExponents (n : ℕ) : Multiset ℤ :=
  ((words n).filter (isInvolution ·)).map
    (fun w => 2 * (majW w : ℤ) + shapeContent (shape w))

/-- The four involutions of `S₃` carry exponents `{2, 3, 3, 4}` (kernel-decided:
words → involution filter → maj → RSK shape → content). -/
theorem statExponents_three : statExponents 3 = {2, 3, 3, 4} := by decide

/-- The ten involutions of `S₄` carry exponents `{4,4,4, 6,6,6,6, 8,8,8}`
(kernel-decided). -/
theorem statExponents_four :
    statExponents 4 = {4, 4, 4, 6, 6, 6, 6, 8, 8, 8} := by decide

section LaurentInstances

variable {R : Type*} [CommRing R]

/-- The single algebraic input the three instances need: `q⁻¹ · q = 1` read into
`R`. This is a **unit** cancellation (`Units.inv_mul`), not a division — which is
why no field appears below. -/
theorem inv_mul_val (q : Rˣ) : ((q⁻¹ : Rˣ) : R) * (q : R) = 1 := q.inv_mul

/-- **`n = 3` instance of `prop:binding-period-involution-statistic`**:
`S^bal(3) = 2 + q + q⁻¹` (partitions `(3), (1³) ↦ 1`, `(2,1) ↦ [2] = q + q⁻¹`),
and `S^bal(3)·q³` equals the statistic sum over the four involutions of `S₃`. -/
theorem binding_period_involution_statistic_three (q : Rˣ) :
    (2 + (q : R) + ((q⁻¹ : Rˣ) : R)) * (q : R) ^ 3
      = ((statExponents 3).map (fun e => ((q ^ e : Rˣ) : R))).sum := by
  have hu : ((q⁻¹ : Rˣ) : R) * (q : R) = 1 := inv_mul_val q
  rw [statExponents_three]
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.sum_cons, Multiset.sum_singleton, zpow_ofNat,
    Units.val_pow_eq_pow_val]
  rw [show (2 + (q : R) + ((q⁻¹ : Rˣ) : R)) * (q : R) ^ 3
        = 2 * (q : R) ^ 3 + (q : R) ^ 4
          + (((q⁻¹ : Rˣ) : R) * (q : R)) * (q : R) ^ 2 by ring]
  rw [hu, one_mul]
  ring

/-- **`n = 4` instance of `prop:binding-period-involution-statistic`**:
`S^bal(4) = 4 + 3q² + 3q⁻²` (partitions `(4), (1⁴) ↦ 1`, `(3,1), (2,1,1) ↦
[3] = q² + 1 + q⁻²`, `(2,2) ↦ [4]/[2] = q² + q⁻²`), and `S^bal(4)·q⁶` equals
the statistic sum over the ten involutions of `S₄`. -/
theorem binding_period_involution_statistic_four (q : Rˣ) :
    (4 + 3 * (q : R) ^ 2 + 3 * ((q⁻¹ : Rˣ) : R) ^ 2) * (q : R) ^ 6
      = ((statExponents 4).map (fun e => ((q ^ e : Rˣ) : R))).sum := by
  have hu : ((q⁻¹ : Rˣ) : R) * (q : R) = 1 := inv_mul_val q
  rw [statExponents_four]
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.sum_cons, Multiset.sum_singleton, zpow_ofNat,
    Units.val_pow_eq_pow_val]
  rw [show (4 + 3 * (q : R) ^ 2 + 3 * ((q⁻¹ : Rˣ) : R) ^ 2) * (q : R) ^ 6
        = 4 * (q : R) ^ 6 + 3 * (q : R) ^ 8
          + 3 * ((((q⁻¹ : Rˣ) : R) * (q : R)) ^ 2 * (q : R) ^ 4) by ring]
  simp only [hu, one_pow, one_mul]
  ring

/-- The 26 involutions of `S₅` carry exponents `{6³,7²,8³,9²,10⁶,11²,12³,13²,14³}`
(kernel-decided). -/
theorem statExponents_five :
    statExponents 5 =
      {6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14} := by
  decide

/-- **`n = 5` instance of `prop:binding-period-involution-statistic`**:
`S^bal(5) = 6 + 2([1]-ish q±) + 3q^{±2} + 2q^{±3} + 3q^{±4}` (the seven partitions
of 5), and `S^bal(5)·q^{10}` equals the statistic sum over the 26 involutions of `S₅`. -/
theorem binding_period_involution_statistic_five (q : Rˣ) :
    (6 + 2 * (q : R) + 2 * ((q⁻¹ : Rˣ) : R) + 3 * (q : R) ^ 2
        + 3 * ((q⁻¹ : Rˣ) : R) ^ 2 + 2 * (q : R) ^ 3 + 2 * ((q⁻¹ : Rˣ) : R) ^ 3
        + 3 * (q : R) ^ 4 + 3 * ((q⁻¹ : Rˣ) : R) ^ 4) * (q : R) ^ 10
      = ((statExponents 5).map (fun e => ((q ^ e : Rˣ) : R))).sum := by
  have hu : ((q⁻¹ : Rˣ) : R) * (q : R) = 1 := inv_mul_val q
  rw [statExponents_five]
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.sum_cons, Multiset.sum_singleton, zpow_ofNat,
    Units.val_pow_eq_pow_val]
  rw [show (6 + 2 * (q : R) + 2 * ((q⁻¹ : Rˣ) : R) + 3 * (q : R) ^ 2
        + 3 * ((q⁻¹ : Rˣ) : R) ^ 2 + 2 * (q : R) ^ 3 + 2 * ((q⁻¹ : Rˣ) : R) ^ 3
        + 3 * (q : R) ^ 4 + 3 * ((q⁻¹ : Rˣ) : R) ^ 4) * (q : R) ^ 10
        = 6 * (q : R) ^ 10 + 2 * (q : R) ^ 11 + 3 * (q : R) ^ 12
          + 2 * (q : R) ^ 13 + 3 * (q : R) ^ 14
          + 2 * ((((q⁻¹ : Rˣ) : R) * (q : R)) ^ 1 * (q : R) ^ 9)
          + 3 * ((((q⁻¹ : Rˣ) : R) * (q : R)) ^ 2 * (q : R) ^ 8)
          + 2 * ((((q⁻¹ : Rˣ) : R) * (q : R)) ^ 3 * (q : R) ^ 7)
          + 3 * ((((q⁻¹ : Rˣ) : R) * (q : R)) ^ 4 * (q : R) ^ 6) by ring]
  simp only [hu, one_pow, one_mul]
  ring

/-- At `q = 1` the statistic sum counts involutions: sanity anchor tying the
decided multisets to the telephone numbers `I(3) = 4`, `I(4) = 10`. -/
theorem statExponents_card :
    Multiset.card (statExponents 3) = 4 ∧ Multiset.card (statExponents 4) = 10 := by
  rw [statExponents_three, statExponents_four]
  constructor <;> rfl

end LaurentInstances

end BindingInvolutionStatistic
end QOU.Mass
