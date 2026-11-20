import QOU.MathlibExt.OcneanuTrace

/-!
# Chain factorisation of a Markov trace on ascending affine words

Let `T` be a Markov (Ocneanu) trace on a tower `H 0 ⊆ H 1 ⊆ ⋯`
(`QOU.MathlibExt.OcneanuTrace.MarkovTrace`). Take an **ascending affine word**:
one affine letter `aₘ · gₘ + bₘ` for each generator `gₘ`, used once each, in
increasing order:

  `w = (aₙ gₙ + bₙ)(aₙ₊₁ gₙ₊₁ + bₙ₊₁) ⋯ (aₙ₊ₖ₋₁ gₙ₊ₖ₋₁ + bₙ₊ₖ₋₁)`.

Then the trace factorises (`tr_chainWord`):

  `tr w = ∏_{i<k} (aₙ₊ᵢ · z + bₙ₊ᵢ)`.

Proof: peel the top letter. The prefix lies in `H (n+i)`, so by linearity and
Markov stabilisation, `tr(x · (a g + b)) = (a z + b) · tr x`.

## Why this file exists

The corpus stated the "product factorisation of the Markov trace" through three
classes named `MarkovTraceAxioms` (bean `qou-ltwg`, owner options 2 + 3 of
2026-11-20). None of them carried a trace on an algebra. Two of them defined a
function on lists whose axioms *were* the product recursion, and the third pinned
two scalars. Each could be inhabited in one line. This file proves the true
statement behind them, for **every** genuine Markov trace.

## Scope

* **Ascending words only.** The factorisation is **false** for a general braid
  word. A Markov trace is not multiplicative over generators, so for example
  `tr(g₀ g₀) ≠ tr(g₀)²` in general. Nothing here says otherwise.
* Generic `[CommRing R]`, generic `R`-algebra `A`, no ordering (§7c).
  `z` is the abstract Markov parameter of `T`, convention-neutral.

-- Ref: [jones1987] https://doi.org/10.2307/1971403 — §5, the Markov trace.
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 — Ch. X.
-/

namespace QOU.MathlibExt.OcneanuTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

namespace MarkovTrace

variable (T : MarkovTrace R A)

/-- The affine letter `a · g m + b` at generator `m`. -/
def chainLetter (a b : R) (m : ℕ) : A := a • T.g m + algebraMap R A b

theorem chainLetter_mem (a b : R) (m : ℕ) : T.chainLetter a b m ∈ T.H (m + 1) :=
  (T.H (m + 1)).add_mem ((T.H (m + 1)).smul_mem (T.g_mem m) a)
    ((T.H (m + 1)).algebraMap_mem b)

/-- **One peel.** For `x ∈ H m`, `tr(x · (a gₘ + b)) = (a z + b) · tr x`. -/
theorem tr_mul_chainLetter (a b : R) (m : ℕ) (x : A) (hx : x ∈ T.H m) :
    T.tr (x * T.chainLetter a b m) = (a * T.z + b) * T.tr x := by
  unfold chainLetter
  rw [mul_add, mul_smul_comm, ← Algebra.commutes, ← Algebra.smul_def,
    map_add, map_smul, map_smul, T.markov m x hx, smul_eq_mul, smul_eq_mul]
  ring

/-- The ascending affine word starting at generator `n`, of length `k`,
with coefficients `a, b : ℕ → R` read at the absolute generator index. -/
def chainWord (a b : ℕ → R) (n k : ℕ) : A :=
  stabWord (fun m => T.chainLetter (a m) (b m) m) n k

theorem chainWord_mem (a b : ℕ → R) (n k : ℕ) : T.chainWord a b n k ∈ T.H (n + k) :=
  T.stabWord_mem _ (fun m => T.chainLetter_mem (a m) (b m) m) n k

/-- **Chain factorisation, with a prefix.** For `x ∈ H n`,
`tr(x · w) = (∏_{i<k} (a(n+i) z + b(n+i))) · tr x`. -/
theorem tr_mul_chainWord (a b : ℕ → R) (n : ℕ) :
    ∀ (k : ℕ) (x : A), x ∈ T.H n →
      T.tr (x * T.chainWord a b n k)
        = (∏ i ∈ Finset.range k, (a (n + i) * T.z + b (n + i))) * T.tr x := by
  intro k
  induction k with
  | zero => intro x _; simp [chainWord]
  | succ k ih =>
    intro x hx
    have hmem : x * T.chainWord a b n k ∈ T.H (n + k) :=
      (T.H (n + k)).mul_mem (T.H_mono (Nat.le_add_right n k) hx) (T.chainWord_mem a b n k)
    have hsplit : x * T.chainWord a b n (k + 1)
        = x * T.chainWord a b n k * T.chainLetter (a (n + k)) (b (n + k)) (n + k) := by
      simp only [chainWord, stabWord_succ, mul_assoc]
    rw [hsplit, T.tr_mul_chainLetter _ _ _ _ hmem, ih x hx, Finset.prod_range_succ]
    ring

/-- **Chain factorisation of the Markov trace** on an ascending affine word:
`tr w = ∏_{i<k} (a(n+i) z + b(n+i))`. -/
theorem tr_chainWord (a b : ℕ → R) (n k : ℕ) :
    T.tr (T.chainWord a b n k)
      = ∏ i ∈ Finset.range k, (a (n + i) * T.z + b (n + i)) := by
  have h := T.tr_mul_chainWord a b n k 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-- **Concatenation.** Two consecutive ascending blocks: the trace of the
joint word is the product of the two block products. -/
theorem tr_chainWord_add (a b : ℕ → R) (n j k : ℕ) :
    T.tr (T.chainWord a b n (j + k))
      = (∏ i ∈ Finset.range j, (a (n + i) * T.z + b (n + i)))
        * ∏ i ∈ Finset.range k, (a (n + j + i) * T.z + b (n + j + i)) := by
  rw [tr_chainWord, Finset.prod_range_add]
  simp only [Nat.add_assoc]

/-- **Adjacent pair.** `tr(gᵢ · gᵢ₊₁) = z²`, for every `i`. -/
theorem tr_g_mul_g_succ (i : ℕ) : T.tr (T.g i * T.g (i + 1)) = T.z * T.z := by
  have h := T.tr_genWord i 2
  simp only [stabWord_succ, stabWord_zero, one_mul, Nat.add_zero] at h
  rw [h, pow_two]

end MarkovTrace

end QOU.MathlibExt.OcneanuTrace
