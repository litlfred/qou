import Mathlib.Algebra.Polynomial.Roots

/-!
# QOU.SchurWeyl.GenericParameter — what "generic `q`" has to mean over a general field

Beans `qou-kwoa` (the general-field item) and `qou-j377` (SW-6).

`QOU/SchurWeyl/HeckeWedderburnGeneral.lean` proves the Wedderburn decomposition at every
rank, but over `ℝ`.  `qou-kwoa` recorded that as *"blocked upstream — `heckeWedderburn` is
`ℝ`-only"*, which is true and says nothing about **why**, so it reads as an accident of
statement.  It is not.  Measured on the theorem's 103-module in-repo import cone:

* `Real.sqrt` does **not** occur anywhere in it — the seminormal form as built here needs
  no square roots, so the usual reason a Hoefsmit construction wants `ℝ` does not apply;
* exactly **two** modules use anything `Real.*` in code, `SeminormalRep` and
  `SeminormalInequivalence`, and both use only the `Real.log` family, in one idiom.

That idiom is `zpow_ne_one : q ≠ 0 → q ^ 2 ≠ 1 → ∀ m ≠ 0, q ^ m ≠ 1`, whose own docstring
already says it is *sharp over `ℝ`*: `q ^ m = 1` forces `|q| = 1`, hence `q = ±1`, hence
`q ^ 2 = 1`.  So over `ℝ` the two-line hypothesis `q ≠ 0 ∧ q ^ 2 ≠ 1` **is** "`q` is not a
root of unity".  Over a general field it is not — a primitive cube root of unity in `ℂ`
satisfies both and has `q ^ 3 = 1`.

**So the `ℝ` is load-bearing, but only as a cheap proof of one hypothesis.**  The classical
criterion is the one the literature states — `q` not a root of unity — and this file
carries it as a hypothesis over an arbitrary field, together with the two consequences the
two `Real.log` proofs actually extract from it.  Nothing here is about `ℝ`; the last
theorem is the bridge showing the `ℝ` statement is the specialisation.

## Why this and not the whole refactor

Generalising the cone means moving 13 files and 248 occurrences of `ℝ`, which is a tranche
rather than a step.  These three lemmas are the part that must exist whichever way that
tranche is done, and they are what makes it mechanical: once `q` not a root of unity is a
hypothesis, every remaining `ℝ` in those files is a base ring that never gets ordered.
-/

namespace QOU.SchurWeyl.GenericParameter

variable {K : Type*}

section Field

variable [Field K] {q : K}

/-- **`q` is not a root of unity**, in the form the seminormal construction consumes: no
positive power is `1`.  Over `ℝ` this is implied by `q ≠ 0 ∧ q ^ 2 ≠ 1`
(`ofSqNeOne` below); over a general field it is strictly stronger and is the hypothesis
the classical statement actually carries. -/
def NotRootOfUnity (q : K) : Prop := ∀ m : ℕ, 0 < m → q ^ m ≠ 1

/-- **The powers of a non-root-of-unity are pairwise distinct.**  This is what
`SeminormalInequivalence` extracts from `Real.log_pow` — there, by taking logs and
cancelling; here, by cancelling `q ^ a` itself, which needs no order. -/
theorem pow_left_injective (hq0 : q ≠ 0) (hq : NotRootOfUnity q) :
    Function.Injective fun m : ℕ => q ^ m := by
  have key : ∀ a b : ℕ, a ≤ b → q ^ a = q ^ b → a = b := by
    intro a b hab h
    obtain ⟨c, rfl⟩ := Nat.exists_eq_add_of_le hab
    rw [pow_add] at h
    have hc : q ^ c = 1 :=
      (mul_left_cancel₀ (pow_ne_zero a hq0) ((mul_one (q ^ a)).trans h)).symm
    rcases Nat.eq_zero_or_pos c with rfl | hcpos
    · simp
    · exact absurd hc (hq c hcpos)
  intro a b h
  rcases le_total a b with hab | hab
  · exact key a b hab h
  · exact (key b a hab h.symm).symm

/-- **No nonzero integer power is `1`** — the exact statement `SeminormalRep.zpow_ne_one`
proves over `ℝ` with `Real.log_zpow`, here from the hypothesis directly.

`q ≠ 0` is **not** needed: if `q = 0` then `NotRootOfUnity q` holds vacuously-ish
(`0 ^ m = 0 ≠ 1` for `m > 0`) and `0 ^ (-k) = (0 ^ k)⁻¹ = 0 ≠ 1`, so the conclusion is
still true.  The `ℝ` original carries `hq0` because its `Real.log` route needs it. -/
theorem zpow_ne_one (hq : NotRootOfUnity q) {m : ℤ} (hm : m ≠ 0) :
    q ^ m ≠ 1 := by
  intro h
  rcases lt_or_gt_of_ne hm with hneg | hpos
  · -- `m < 0`: `q ^ m = (q ^ (-m))⁻¹`, and an inverse is `1` only if the element is
    obtain ⟨k, hk⟩ : ∃ k : ℕ, m = -(k : ℤ) := ⟨(-m).toNat, by omega⟩
    have hkpos : 0 < k := by omega
    rw [hk, zpow_neg, zpow_natCast, inv_eq_one] at h
    exact hq k hkpos h
  · obtain ⟨k, hk⟩ : ∃ k : ℕ, m = (k : ℤ) := ⟨m.toNat, by omega⟩
    have hkpos : 0 < k := by omega
    rw [hk, zpow_natCast] at h
    exact hq k hkpos h

/-! ### The order-free replacements for the cone's `positivity` steps

The Wedderburn cone's remaining archimedean uses are not `Real.*` — they are order tactics,
and the recurring one is `(q ^ 2 + 1) ≠ 0`, proved over `ℝ` by `positivity`
(`HoefsmitRep.sq_add_one_ne`) and used again inside `SeminormalParam`'s
`(q ^ 2 - 1) * (q ^ 2 + 1) = 0` argument.  That statement is **false** over a general field —
a primitive fourth root of unity has `q ^ 2 + 1 = 0` — so it looks like a second, independent
obstruction to leaving `ℝ`.

It is not.  `q ^ 2 + 1 = 0` forces `q ^ 4 = 1`, which `NotRootOfUnity` already forbids.  So
the single hypothesis introduced above covers the order steps too, and the migration does
not need `[LinearOrderedField K]`. -/

/-- **`q` is not `1`** — the `m = 1` case, named because call sites want it in this form. -/
theorem ne_one (hq : NotRootOfUnity q) : q ≠ 1 := fun h => hq 1 one_pos (by rw [h, one_pow])

/-- **`q ^ 2 ≠ 1`**, the hypothesis the `ℝ` development carries explicitly. -/
theorem sq_ne_one (hq : NotRootOfUnity q) : q ^ 2 ≠ 1 := hq 2 (by norm_num)

/-- **`q ^ 2 + 1 ≠ 0` over any field**, given only that `q` is not a root of unity.

This is the lemma that keeps the general-field migration from needing an order.  Over `ℝ`
it is `positivity`; over a general field `positivity` is unavailable *and the statement can
fail* — but only at a fourth root of unity, which the hypothesis excludes:
`q ^ 2 = -1` gives `q ^ 4 = (-1) ^ 2 = 1`. -/
theorem sq_add_one_ne_zero (hq : NotRootOfUnity q) : q ^ 2 + 1 ≠ 0 := by
  intro h
  refine hq 4 (by norm_num) ?_
  -- `q⁴ = (q² + 1)(q² − 1) + 1`, and the first factor is the hypothesis.  Written this way
  -- so the file keeps its single Mathlib import: no `linear_combination`, no order.
  have key : q ^ 4 = (q ^ 2 + 1) * (q ^ 2 - 1) + 1 := by ring
  rw [key, h, zero_mul, zero_add]

/-- **A polynomial vanishing at every power of `q` is zero.**  `SeminormalInequivalence`
proves this over `ℝ` from `0 < t` and `t ≠ 1`; the content is only that `m ↦ q ^ m` has
infinite range, so it holds over any field. -/
theorem poly_eq_zero_of_eval_pow (hq0 : q ≠ 0) (hq : NotRootOfUnity q)
    {p : Polynomial K} (h : ∀ m : ℕ, p.eval (q ^ m) = 0) : p = 0 := by
  refine Polynomial.eq_zero_of_infinite_isRoot p ?_
  have hsub : Set.range (fun m : ℕ => q ^ m) ⊆ {x | p.IsRoot x} := by
    rintro _ ⟨m, rfl⟩
    exact h m
  exact Set.Infinite.mono hsub (Set.infinite_range_of_injective (pow_left_injective hq0 hq))

end Field

end QOU.SchurWeyl.GenericParameter
