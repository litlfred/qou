/-
  The photon stopping depth `L(n)`: the least `k` such that products of at most `k` sliding
  photons span `H_n(q)` (audit `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §12).

  Write `N = n(n−1)/2`, the length of the longest permutation `w₀`. The bounds are
  `⌈N/2⌉ ≤ L(n) ≤ ⌊n²/4⌋`. This file proves the parts of that argument that do not depend on a
  construction of `H_n(q)`:

  1. **Lower bound, abstract** (`photon_pow_le`, `depth_lower_bound`). Let `C m` be a
     multiplicative filtration (`C a * C b ≤ C (a + b)`, `1 ∈ C 0`) and let the photon space
     satisfy `F₁ ≤ C 2`. Then `F₁ ^ k ≤ C (2k)`. So if `x ∉ C (N − 1)` and `x ∈ F₁ ^ k`, then
     `N ≤ 2k`.
  2. **Trivial upper bound, abstract** (`filtration_le_photon_pow`). If `C 1 ≤ F₁` and
     `C (a + b) ≤ C a * C b`, then `C k ≤ F₁ ^ k`.
  3. **Staircase count** (`sum_ceil_half`): `Σ_{r<n} ⌈r/2⌉ = ⌊n²/4⌋`.

  The Hecke-specific inputs are standard theorems about the Iwahori–Matsumoto basis
  `{T_w}` of `H_n(q)` \cite{iwahori1964, kassel2008}, not conjectures. They are carried here as
  hypotheses because the corpus has a concrete Lean model of `H₃(q)` only
  (`QOU.HeckeH3Model`):
  * `C m = span{T_w : ℓ(w) ≤ m}` is multiplicative, and `C (a+b) = C a * C b` for
    `a + b ≤ N`;
  * `T_{w₀} ∉ C (N − 1)`;
  * `σᵢ ∈ C 1` and the vertex `σᵢσᵢ₊₁⁻¹ = T_{sᵢsᵢ₊₁} − h·T_{sᵢ} ∈ C 2`.
  The staircase upper bound also needs the leading-term argument written out in the audit
  (§12.2); its combinatorial count is item 3.

  Measured (exact modular rank, `photon_stopping_depth_probe.py`): `L(3) = 2`, `L(4) = 4`,
  `L(5) = 6`, `L(6) = 9`, which equals `⌊n²/4⌋` for every `n` measured. `L(3) = 2` is also
  proved in the model (`QOU.HeckeH3Model.electron_eq`, `commutator_not_mem_F1`).

  -- Ref: [iwahori1964] https://doi.org/10.15083/00039809
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import Mathlib.Algebra.Algebra.Operations
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.PhotonStoppingDepth

open Submodule

section Filtration

variable {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]

/-- **Lower-bound core.** A photon space inside filtration degree 2 stays in degree `2k`
after `k` products. -/
theorem photon_pow_le (C : ℕ → Submodule R A) (hmul : ∀ a b, C a * C b ≤ C (a + b))
    (hone : (1 : Submodule R A) ≤ C 0) (F₁ : Submodule R A) (hF : F₁ ≤ C 2) :
    ∀ k : ℕ, F₁ ^ k ≤ C (2 * k)
  | 0 => by simpa using hone
  | k + 1 => by
    rw [pow_succ]
    calc F₁ ^ k * F₁ ≤ C (2 * k) * C 2 := mul_le_mul' (photon_pow_le C hmul hone F₁ hF k) hF
      _ ≤ C (2 * k + 2) := hmul _ _
      _ = C (2 * (k + 1)) := by ring_nf

/-- **Lower bound.** If `x ∉ C (N − 1)` but `x` is a combination of products of `k` photons,
then `N ≤ 2k`. -/
theorem depth_lower_bound (C : ℕ → Submodule R A) (hmono : Monotone C)
    (hmul : ∀ a b, C a * C b ≤ C (a + b)) (hone : (1 : Submodule R A) ≤ C 0)
    (F₁ : Submodule R A) (hF : F₁ ≤ C 2) {N k : ℕ} {x : A} (hx : x ∉ C (N - 1))
    (hk : x ∈ F₁ ^ k) : N ≤ 2 * k := by
  by_contra hlt
  push_neg at hlt
  exact hx (hmono (by omega) (photon_pow_le C hmul hone F₁ hF k hk))

/-- **Trivial upper bound.** If the photons contain filtration degree 1 and the filtration is
generated in degree 1, then `C k ≤ F₁ ^ k`. -/
theorem filtration_le_photon_pow (C : ℕ → Submodule R A)
    (hsplit : ∀ a, C (a + 1) ≤ C a * C 1) (hzero : C 0 ≤ 1)
    (F₁ : Submodule R A) (hF : C 1 ≤ F₁) : ∀ k : ℕ, C k ≤ F₁ ^ k
  | 0 => by simpa using hzero
  | k + 1 => by
    rw [pow_succ]
    exact (hsplit k).trans (mul_le_mul' (filtration_le_photon_pow C hsplit hzero F₁ hF k) hF)

end Filtration

section Count

/-- **Staircase count.** `Σ_{r=0}^{n−1} ⌈r/2⌉ = ⌊n²/4⌋`, with `⌈r/2⌉ = (r + 1) / 2`. -/
theorem sum_ceil_half : ∀ n : ℕ, (∑ r ∈ Finset.range n, (r + 1) / 2) = n ^ 2 / 4
  | 0 => by simp
  | n + 1 => by
    rw [Finset.sum_range_succ, sum_ceil_half n]
    rcases Nat.even_or_odd' n with ⟨t, rfl | rfl⟩
    · have h1 : (2 * t) ^ 2 / 4 = t * t := by
        rw [show (2 * t) ^ 2 = 4 * (t * t) by ring]; omega
      have h2 : (2 * t + 1) ^ 2 / 4 = t * t + t := by
        rw [show (2 * t + 1) ^ 2 = 4 * (t * t + t) + 1 by ring]; omega
      rw [h1, h2]; omega
    · have h1 : (2 * t + 1) ^ 2 / 4 = t * t + t := by
        rw [show (2 * t + 1) ^ 2 = 4 * (t * t + t) + 1 by ring]; omega
      have h2 : (2 * t + 1 + 1) ^ 2 / 4 = t * t + 2 * t + 1 := by
        rw [show (2 * t + 1 + 1) ^ 2 = 4 * (t * t + 2 * t + 1) by ring]; omega
      rw [h1, h2]; omega

/-- The lower bound `⌈N/2⌉` never exceeds the staircase bound `⌊n²/4⌋`. -/
theorem lower_le_upper (n : ℕ) : (n * (n - 1) / 2 + 1) / 2 ≤ n ^ 2 / 4 := by
  rcases Nat.even_or_odd' n with ⟨t, rfl | rfl⟩
  · rcases t with _ | t
    · simp
    · have : (2 * (t + 1)) ^ 2 / 4 = (t + 1) * (t + 1) := by
        rw [show (2 * (t + 1)) ^ 2 = 4 * ((t + 1) * (t + 1)) by ring]; omega
      rw [this, show 2 * (t + 1) - 1 = 2 * t + 1 by omega,
        show 2 * (t + 1) * (2 * t + 1) = 2 * ((t + 1) * (2 * t + 1)) by ring]
      rw [Nat.mul_div_cancel_left _ (by norm_num)]
      nlinarith [Nat.div_mul_le_self ((t + 1) * (2 * t + 1) + 1) 2]
  · have : (2 * t + 1) ^ 2 / 4 = t * t + t := by
      rw [show (2 * t + 1) ^ 2 = 4 * (t * t + t) + 1 by ring]; omega
    rw [this, show 2 * t + 1 - 1 = 2 * t by omega,
      show (2 * t + 1) * (2 * t) = 2 * ((2 * t + 1) * t) by ring,
      Nat.mul_div_cancel_left _ (by norm_num)]
    nlinarith [Nat.div_mul_le_self ((2 * t + 1) * t + 1) 2]

end Count

end QOU.PhotonStoppingDepth
