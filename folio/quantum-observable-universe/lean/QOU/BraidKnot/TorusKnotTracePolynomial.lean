import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.TorusKnotTracePolynomial — the `T(2,2m)` trace polynomial, proved

`docs/canonical-derivation-cheat-sheet.md` §5 records, for the `T(2, 2m)` torus-knot
Markov trace (PR #1125, `torus-knot-h-expansion-pattern.md`):

    `P_m(h) = Σ_{j=0}^{m} C(m+j, 2j)/2 · h^{2j} = (q^{2m+1} + q^{−(2m+1)}) / (2·[2]_q)`,
    `h = q − q⁻¹`,

and marks it **"sympy-exact across `m = 1..6`"** — that is, verified on six cases. It
is the identity the categorical Weinberg-angle statement is built on, via
`P_m(h₀) = cosh((2m+1)η₀) / (2 cosh η₀)` at a real substrate `q₀ = e^{η₀}`.

This file proves it, for all `m`, over any field.

## How, and why the recursion comes first

Both sides satisfy the same Chebyshev-type recurrence, because `q² + q⁻² = h² + 2`:

    `S_{m+1} = (h² + 2)·S_m − S_{m−1}`,   `S_0 = 1`,  `S_1 = h² + 1`.

So the work splits cleanly:

* `chebS_q_form` — the recursion equals the `q`-form. Pure field algebra; this is the
  half the cosh statement needs, and it is proved first because it is the load-bearing
  one.
* `chebS_eq_sum` — the recursion equals the binomial sum. This is where the
  combinatorial content sits, and it reduces to one Pascal identity
  (`choose_shift_identity`), applied twice.

Composing them gives `traceIdentity`, the cheat-sheet statement.

Doing it in this order matters: the recursion is the object that makes both sides
computable, and neither side is naturally defined in terms of the other. A direct
sum-to-`q`-form induction would have to carry the binomial manipulation and the field
algebra simultaneously.

## What this does and does not settle

It settles that the closed form is an identity rather than a coincidence checked on
six cases. It says nothing about the `+1.07 %` residual in the Weinberg-angle
comparison — that is a question about which of `cosh` and `cos` the physics selects,
and `QOU.MathlibExt.CoshCosSeparation` shows the two are not near each other.

-- Ref: [leitner2026] torus-knot-h-expansion-pattern
-/

namespace QOU.BraidKnot

open Finset

/-! ## The recursion -/

/-- The Chebyshev-type recursion underlying the `T(2,2m)` trace polynomial:
`S₀ = 1`, `S₁ = h² + 1`, `S_{m+2} = (h² + 2)·S_{m+1} − S_m`. -/
def chebS {K : Type*} [Ring K] (h : K) : ℕ → K
  | 0 => 1
  | 1 => h ^ 2 + 1
  | (m + 2) => (h ^ 2 + 2) * chebS h (m + 1) - chebS h m

@[simp] theorem chebS_zero {K : Type*} [Ring K] (h : K) : chebS h 0 = 1 := rfl

@[simp] theorem chebS_one {K : Type*} [Ring K] (h : K) : chebS h 1 = h ^ 2 + 1 := rfl

theorem chebS_succ_succ {K : Type*} [Ring K] (h : K) (m : ℕ) :
    chebS h (m + 2) = (h ^ 2 + 2) * chebS h (m + 1) - chebS h m := rfl

/-! ## Half one — the `q`-form

`h² + 2 = q² + q⁻²`, which is exactly the multiplier in the recurrence satisfied by
`q^{2m+1} + q^{−(2m+1)}`. -/

variable {K : Type*} [Field K]

/-- **The `q`-form.** `S_m(q − q⁻¹)·(q + q⁻¹) = q^{2m+1} + q^{−(2m+1)}`.

At a real substrate `q = e^η` this reads `S_m·2cosh η = 2cosh((2m+1)η)`, i.e. the
cheat sheet's `P_m(h₀) = cosh((2m+1)η₀)/(2 cosh η₀)`. -/
theorem chebS_q_form (q : K) (hq : q ≠ 0) (m : ℕ) :
    chebS (q - q⁻¹) m * (q + q⁻¹) = q ^ (2 * m + 1) + (q ^ (2 * m + 1))⁻¹ := by
  -- two-step induction, carried as a conjunction so ordinary `induction` suffices
  suffices H : ∀ n : ℕ,
      (chebS (q - q⁻¹) n * (q + q⁻¹) = q ^ (2 * n + 1) + (q ^ (2 * n + 1))⁻¹) ∧
      (chebS (q - q⁻¹) (n + 1) * (q + q⁻¹)
        = q ^ (2 * (n + 1) + 1) + (q ^ (2 * (n + 1) + 1))⁻¹) from (H m).1
  intro n
  induction n with
  | zero =>
      refine ⟨?_, ?_⟩
      · rw [show chebS (q - q⁻¹) 0 = 1 from rfl, one_mul]
        norm_num
      · rw [show chebS (q - q⁻¹) (0 + 1) = (q - q⁻¹) ^ 2 + 1 from rfl,
          show 2 * (0 + 1) + 1 = 3 by norm_num]
        field_simp
        ring
  | succ k ih =>
      refine ⟨ih.2, ?_⟩
      -- unfold the recursion and feed in both halves of the hypothesis
      have hdist : chebS (q - q⁻¹) (k + 2) * (q + q⁻¹)
          = ((q - q⁻¹) ^ 2 + 2) * (chebS (q - q⁻¹) (k + 1) * (q + q⁻¹))
            - chebS (q - q⁻¹) k * (q + q⁻¹) := by
        rw [chebS_succ_succ]; ring
      have hstep : (k + 1) + 1 = k + 2 := rfl
      rw [hstep, hdist, ih.1, ih.2]
      -- now a field identity in `q` and `X = q^(2k+1)`
      have e1 : 2 * (k + 1) + 1 = (2 * k + 1) + 2 := by ring
      have e2 : 2 * (k + 1 + 1) + 1 = (2 * k + 1) + 4 := by ring
      rw [e1, e2, pow_add, pow_add]
      have hX : q ^ (2 * k + 1) ≠ 0 := pow_ne_zero _ hq
      field_simp
      ring

/-! ## Half two — the binomial sum

The combinatorial content is one Pascal identity, used twice. -/

/-- **The Pascal identity behind the recurrence.**

`C(m+i+2, 2i+2) + C(m+i, 2i+2) = C(m+i, 2i) + 2·C(m+i+1, 2i+2)`.

Indexed by `i` rather than by `j = i+1` so that every argument is a genuine natural
number and no truncated subtraction appears. Three applications of Pascal's rule and
`omega` on the resulting linear combination. -/
theorem choose_shift_identity (m i : ℕ) :
    (m + i + 2).choose (2 * i + 2) + (m + i).choose (2 * i + 2)
      = (m + i).choose (2 * i) + 2 * (m + i + 1).choose (2 * i + 2) := by
  have p1 : (m + i + 2).choose (2 * i + 2)
      = (m + i + 1).choose (2 * i + 1) + (m + i + 1).choose (2 * i + 2) :=
    Nat.choose_succ_succ' (m + i + 1) (2 * i + 1)
  have p2 : (m + i + 1).choose (2 * i + 2)
      = (m + i).choose (2 * i + 1) + (m + i).choose (2 * i + 2) :=
    Nat.choose_succ_succ' (m + i) (2 * i + 1)
  have p3 : (m + i + 1).choose (2 * i + 1)
      = (m + i).choose (2 * i) + (m + i).choose (2 * i + 1) :=
    Nat.choose_succ_succ' (m + i) (2 * i)
  omega

/-- The explicit binomial sum of `torus-knot-h-expansion-pattern` (PR #1125),
`Σ_{j≤m} C(m+j, 2j)·h^{2j}` — the cheat sheet's `P_m` before its factor of `1/2`. -/
def chebSum {K : Type*} [CommRing K] (h : K) (m : ℕ) : K :=
  ∑ j ∈ range (m + 1), ((m + j).choose (2 * j) : K) * h ^ (2 * j)

/-- Terms past `j = m` vanish, because `2j > m + j` there. This is what lets every
sum in the recurrence be written over one common range. -/
theorem choose_add_vanish {m j : ℕ} (hj : m < j) : (m + j).choose (2 * j) = 0 :=
  Nat.choose_eq_zero_of_lt (by omega)

/-- `chebSum` may be summed over any range at least as long as its own. -/
theorem chebSum_eq_range {K : Type*} [CommRing K] (h : K) (m M : ℕ) (hM : m + 1 ≤ M) :
    chebSum h m = ∑ j ∈ range M, ((m + j).choose (2 * j) : K) * h ^ (2 * j) := by
  refine Finset.sum_subset (by simpa using hM) ?_
  intro j _ hj
  rw [mem_range, not_lt] at hj
  rw [choose_add_vanish (by omega), Nat.cast_zero, zero_mul]

/-- **`chebSum` satisfies the recursion**, in additive form.

Stated as `S_{m+2} + S_m = (h²+2)·S_{m+1}` rather than with a subtraction on purpose:
the termwise fact underneath is `choose_shift_identity`, which is an identity between
sums of binomial coefficients in `ℕ`, and keeping it additive means no truncated
subtraction ever has to be reasoned about.

All three sums are first put over the common range `range (m+3)` — legitimate by
`chebSum_eq_range`, since the extra terms vanish — after which peeling index `0`
aligns the `h²` shift with the rest. -/
theorem chebSum_succ_succ_add {K : Type*} [CommRing K] (h : K) (m : ℕ) :
    chebSum h (m + 2) + chebSum h m = (h ^ 2 + 2) * chebSum h (m + 1) := by
  have hA : chebSum h (m + 2)
      = ∑ j ∈ range (m + 3), ((m + 2 + j).choose (2 * j) : K) * h ^ (2 * j) :=
    chebSum_eq_range h (m + 2) (m + 3) (by omega)
  have hC : chebSum h m
      = ∑ j ∈ range (m + 3), ((m + j).choose (2 * j) : K) * h ^ (2 * j) :=
    chebSum_eq_range h m (m + 3) (by omega)
  have hBpad : chebSum h (m + 1)
      = ∑ j ∈ range (m + 3), ((m + 1 + j).choose (2 * j) : K) * h ^ (2 * j) :=
    chebSum_eq_range h (m + 1) (m + 3) (by omega)
  have hBnat : chebSum h (m + 1)
      = ∑ j ∈ range (m + 2), ((m + 1 + j).choose (2 * j) : K) * h ^ (2 * j) := rfl
  -- The `h²` piece keeps `chebSum`'s own range and becomes a shift; the `2·` piece is
  -- padded to `range (m+3)` so it can be peeled at `0` against the left-hand side.
  -- Splitting the two BEFORE peeling is the whole trick: the `h²` contribution of
  -- index `0` belongs at index `1`, so peeling the product as one term misaligns them.
  have expand : (h ^ 2 + 2) * chebSum h (m + 1)
      = (∑ j ∈ range (m + 2), ((m + 1 + j).choose (2 * j) : K) * h ^ (2 * (j + 1)))
        + ∑ j ∈ range (m + 3), 2 * (((m + 1 + j).choose (2 * j) : K) * h ^ (2 * j)) := by
    have e1 : h ^ 2 * chebSum h (m + 1)
        = ∑ j ∈ range (m + 2), ((m + 1 + j).choose (2 * j) : K) * h ^ (2 * (j + 1)) := by
      rw [hBnat, Finset.mul_sum]
      refine Finset.sum_congr rfl fun j _ => ?_
      rw [show 2 * (j + 1) = 2 * j + 2 by omega, pow_add]
      ring
    have e2 : 2 * chebSum h (m + 1)
        = ∑ j ∈ range (m + 3), 2 * (((m + 1 + j).choose (2 * j) : K) * h ^ (2 * j)) := by
      rw [hBpad, Finset.mul_sum]
    calc (h ^ 2 + 2) * chebSum h (m + 1)
        = h ^ 2 * chebSum h (m + 1) + 2 * chebSum h (m + 1) := by ring
      _ = _ := by rw [e1, e2]
  -- the peeled tails agree termwise; this is the only place the combinatorics enters
  have hsum : ∑ k ∈ range (m + 2),
        ((((m + 2 + (k + 1)).choose (2 * (k + 1)) : K)) * h ^ (2 * (k + 1))
          + (((m + (k + 1)).choose (2 * (k + 1)) : K)) * h ^ (2 * (k + 1)))
      = (∑ j ∈ range (m + 2), ((m + 1 + j).choose (2 * j) : K) * h ^ (2 * (j + 1)))
        + ∑ k ∈ range (m + 2),
            2 * (((m + 1 + (k + 1)).choose (2 * (k + 1)) : K) * h ^ (2 * (k + 1))) := by
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    have hcast : ((m + 1 + i + 2).choose (2 * i + 2) : K)
        + ((m + 1 + i).choose (2 * i + 2) : K)
        = ((m + 1 + i).choose (2 * i) : K)
          + 2 * ((m + 1 + i + 1).choose (2 * i + 2) : K) := by
      exact_mod_cast congrArg (Nat.cast : ℕ → K) (choose_shift_identity (m + 1) i)
    rw [show m + 2 + (i + 1) = m + 1 + i + 2 by omega,
      show m + (i + 1) = m + 1 + i by omega,
      show m + 1 + (i + 1) = m + 1 + i + 1 by omega,
      show 2 * (i + 1) = 2 * i + 2 by omega]
    linear_combination h ^ (2 * i + 2) * hcast
  rw [expand, hA, hC, ← Finset.sum_add_distrib,
    Finset.sum_range_succ' (fun j => ((m + 2 + j).choose (2 * j) : K) * h ^ (2 * j)
      + ((m + j).choose (2 * j) : K) * h ^ (2 * j)) (m + 2),
    Finset.sum_range_succ' (fun j => 2 * (((m + 1 + j).choose (2 * j) : K) * h ^ (2 * j)))
      (m + 2), hsum]
  -- what is left is the index-`0` bookkeeping: `C(m+2,0) + C(m,0) = 2 = 2·C(m+1,0)`
  simp only [Nat.choose_zero_right, Nat.cast_one, Nat.mul_zero, pow_zero, mul_one]
  ring

/-- **The binomial sum *is* the recursion.** Two-step induction; the step is
`chebSum_succ_succ_add` rearranged, so the additive form is used exactly once and the
subtraction only ever appears on the `chebS` side, where it is over a ring. -/
theorem chebSum_eq_chebS {K : Type*} [CommRing K] (h : K) (m : ℕ) :
    chebSum h m = chebS h m := by
  suffices H : ∀ n : ℕ, chebSum h n = chebS h n ∧ chebSum h (n + 1) = chebS h (n + 1) from
    (H m).1
  intro n
  induction n with
  | zero =>
      refine ⟨?_, ?_⟩
      · simp [chebSum]
      · simp [chebSum, Finset.sum_range_succ]
        ring
  | succ k ih =>
      refine ⟨ih.2, ?_⟩
      rw [show k + 1 + 1 = k + 2 from rfl, chebS_succ_succ, ← ih.1, ← ih.2]
      linear_combination chebSum_succ_succ_add h k

/-! ## The cheat-sheet statement -/

/-- **`P_m(h) = (q^{2m+1} + q^{−(2m+1)}) / (2·[2]_q)`**, for every `m`.

This is `docs/canonical-derivation-cheat-sheet.md` §5's identity, recorded there as
"sympy-exact across `m = 1..6`". It is now a theorem over any field of characteristic
zero, with no bound on `m`.

At a real substrate `q = e^η` the right-hand side is `cosh((2m+1)η) / (2 cosh η)`, which
is the form the categorical Weinberg-angle statement uses. -/
theorem traceIdentity {K : Type*} [Field K] [CharZero K] (q : K) (hq : q ≠ 0)
    (hq2 : q + q⁻¹ ≠ 0) (m : ℕ) :
    (∑ j ∈ range (m + 1), ((m + j).choose (2 * j) : K) / 2 * (q - q⁻¹) ^ (2 * j))
      = (q ^ (2 * m + 1) + (q ^ (2 * m + 1))⁻¹) / (2 * (q + q⁻¹)) := by
  have h1 : (∑ j ∈ range (m + 1), ((m + j).choose (2 * j) : K) / 2 * (q - q⁻¹) ^ (2 * j))
      = chebSum (q - q⁻¹) m / 2 := by
    rw [chebSum, Finset.sum_div]
    exact Finset.sum_congr rfl fun j _ => by ring
  -- `field_simp` clears `q⁻¹` into `q² + 1`, so it needs that form of the hypothesis
  have hq21 : q ^ 2 + 1 ≠ 0 := by
    intro hc
    apply hq2
    field_simp
    linear_combination hc
  rw [h1, chebSum_eq_chebS, ← chebS_q_form q hq m]
  field_simp

end QOU.BraidKnot
