import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# Rational fibre object ⇒ C-finite ladder coefficients (residue-A kernel grounding)

Step 3 of the residue-A unblock kernel work
(`docs/audits/2026-06-04-residue-a-unblock-kernel-scope.md`). The fibre object
`F(u) = Q_β/[Q_A·cos α_eff]` satisfies a `q`-difference equation
`F(qξ) = R(q,ξ)·F(ξ)`; if `F` is a *rational* function `P/Q`, its ladder
coefficients `c_k` are **C-finite** — they satisfy a constant-coefficient linear
recurrence whose characteristic polynomial is the reverse of the denominator
`Q`, and the poles of `F` (in particular the simple pole at `u_substrate`) are
the reciprocals of the characteristic roots.

This grounds the search "find the kernel `R`" ≡ "find the minimal denominator
`Q`". Its **contrapositive** is the pruning used by
`computations/qbeta/qbeta_ck_recurrence_first_cut.py`: the
canonical `c_2..c_10` admit no constant-coefficient recurrence of order ≤ 4, so
`F` is **not** a low-degree rational function — the kernel is genuinely
higher-order, and the productive direction is the canonical `c_11+` extraction
(or a categorical derivation of `Q_A·cos α_eff`'s zero), not more real-q /
root-of-unity forms.

The lemma below is the load-bearing algebraic fact: a root `u₀` of the
denominator gives a root `u₀⁻¹` of the reversed (characteristic) polynomial.
Verified sorry-free against mathlib (pinned `f897ebcf`, lean v4.24.0).
-/

open scoped BigOperators

namespace QOU.QBeta

/-- **Pole ⇒ reciprocal is a characteristic root.** If `u₀ ≠ 0` is a root of the
denominator polynomial `∑_{j≤d} q j · X^j`, then `u₀⁻¹` is a root of the
reversed (characteristic) polynomial `∑_{j≤d} q j · X^(d-j)`.

This is the `find R ≡ find minimal Q` grounding for the `c_k` recurrence: the
pole `u_substrate` of `F` is exactly such a `u₀`, so `1/u_substrate` is the
dominant characteristic root of the ladder recurrence — matching the empirical
tail ratio `c_{k+1}/c_k → 1/u_substrate ≈ 117.4`. -/
theorem pole_reciprocal_is_char_root {K : Type*} [Field K] (d : ℕ) (q : ℕ → K)
    (u₀ : K) (hu : u₀ ≠ 0)
    (hroot : ∑ j ∈ Finset.range (d + 1), q j * u₀ ^ j = 0) :
    ∑ j ∈ Finset.range (d + 1), q j * (u₀⁻¹) ^ (d - j) = 0 := by
  -- Pointwise: for `j ≤ d`, `(u₀⁻¹)^(d-j) = (u₀⁻¹)^d * u₀^j`, hence each summand
  -- equals `(u₀⁻¹)^d * (q j * u₀^j)`.
  have key : ∀ j ∈ Finset.range (d + 1),
      q j * (u₀⁻¹) ^ (d - j) = (u₀⁻¹) ^ d * (q j * u₀ ^ j) := by
    intro j hj
    have hjd : j ≤ d := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    have hcancel : (u₀⁻¹) ^ j * u₀ ^ j = 1 := by
      rw [inv_pow, inv_mul_cancel₀ (pow_ne_zero j hu)]
    have hsplit : (u₀⁻¹) ^ d = (u₀⁻¹) ^ (d - j) * (u₀⁻¹) ^ j := by
      rw [← pow_add, Nat.sub_add_cancel hjd]
    have heq : (u₀⁻¹) ^ (d - j) = (u₀⁻¹) ^ d * u₀ ^ j := by
      rw [hsplit, mul_assoc, hcancel, mul_one]
    rw [heq]; ring
  -- Factor `(u₀⁻¹)^d` out of the sum and apply the denominator-root hypothesis.
  have step : ∑ j ∈ Finset.range (d + 1), q j * (u₀⁻¹) ^ (d - j)
            = (u₀⁻¹) ^ d * ∑ j ∈ Finset.range (d + 1), q j * u₀ ^ j := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl key
  rw [step, hroot, mul_zero]

end QOU.QBeta
