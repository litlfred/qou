import QOU.Archimedean.lepton_continuant_binet
import Mathlib.Tactic.Linarith

/-!
# QOU.Archimedean.lepton_continuant_positivity — the invariant that closes the node escape

Ordered-field companion to `lepton_continuant_binet`.  Split out per the
§7c base-ring wall: the Binet / linear-readout algebra there holds over a
bare `[Field K]`, while everything here needs an **order** on `K`.

Nothing in this file is archimedean — no `Real.sqrt`, `Real.log`, `Real.exp`
or CODATA constant appears — so it stays generic over an ordered field and
is instantiated at `ℝ` only where measured masses enter, i.e. in the Python
twin [`lepton_linear_readout_rigidity.py`](../../../../../computations/lepton_linear_readout_rigidity.py).

## What this closes

`linFunctionalK_two_step` bounds the *increment* of a readout, not its
*ratio*.  If a readout `φ` had a zero — a **node** — just below the
generation window (windings `3, 5, 7`, i.e. `n = 2, 4, 6`), then `φ(2) ≈ 0`
and `φ(4)/φ(2)` would be arbitrarily large, which *can* reproduce the
observed `m_μ/m_e = 206.8`.  So "no linear readout works" is **false** as a
bare claim, and the exclusion is incomplete without the results below.

Solving that escape exactly (a quadratic in `A/B`, in the Python twin) gives
two roots, and **both** require `φ(1)` and `φ(σ₀)` to have *opposite signs*.

That is what positivity forbids.  For `q > 1` the Hecke parameter
`h = q − q⁻¹` is positive, so the Morgan–Voyce continuant — starting `0, 1`
and built by `b_{n+2} = h·b_{n+1} + b_n` — is positive from `b₁` on.  Hence
any readout with `φ(1) ≥ 0` and `φ(σ₀) > 0` is strictly positive at every
index: its node does not lie outside the window, it **does not exist**.

The canonical Markov trace is such a readout (`tr_M(1) = 1`,
`tr_M(σ₀) = z = 1/(q^{1/2} + q^{-1/2}) > 0`), so the escape is unavailable
to the only readout the framework actually derives.  That is what makes the
exclusion scope-(b) — resting on a proved invariant — rather than a failed
search.

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K}

/-- For `q > 1` the Hecke parameter `h = q − q⁻¹` is positive. -/
lemma hecke_h_pos (hq : 1 < q) : 0 < q - q⁻¹ := by
  have hq0 : (0 : K) < q := lt_trans zero_lt_one hq
  have hmul : q⁻¹ * q = 1 := inv_mul_cancel₀ (ne_of_gt hq0)
  have hinv : (0 : K) < q⁻¹ := inv_pos.mpr hq0
  nlinarith [hmul, hinv, hq, hq0]

/-- The continuant is non-negative, and strictly positive from index `1`.

Both halves are needed simultaneously: the recurrence
`b_{n+2} = h b_{n+1} + b_n` derives positivity of `b_{n+2}` from strict
positivity of `b_{n+1}` together with non-negativity of `b_n`. -/
lemma morganVoyceBK_nonneg_and_pos (hq : 1 < q) (n : ℕ) :
    0 ≤ morganVoyceBK q n ∧ 0 < morganVoyceBK q (n + 1) := by
  induction n with
  | zero => exact ⟨le_of_eq (morganVoyceBK_zero q).symm, by
      rw [morganVoyceBK_one]; exact zero_lt_one⟩
  | succ n ih =>
      refine ⟨le_of_lt ih.2, ?_⟩
      rw [morganVoyceBK_succ_succ]
      have := mul_pos (hecke_h_pos hq) ih.2
      linarith [ih.1]

/-- **The continuant never vanishes on the physical range.** -/
theorem morganVoyceBK_pos (hq : 1 < q) (n : ℕ) : 0 < morganVoyceBK q (n + 1) :=
  (morganVoyceBK_nonneg_and_pos hq n).2

/-- **Every positive readout is strictly positive — it has no node.**

`φ(1) ≥ 0` and `φ(σ₀) > 0` suffice.  This is the invariant that
forecloses the node escape described above. -/
theorem linFunctionalK_pos (hq : 1 < q) {α β : K} (hα : 0 ≤ α) (hβ : 0 < β)
    (n : ℕ) : 0 < linFunctionalK α β q n := by
  have hb : 0 ≤ morganVoyceBK q n := (morganVoyceBK_nonneg_and_pos hq n).1
  have hb' : 0 < morganVoyceBK q (n + 1) := morganVoyceBK_pos hq n
  have h1 : 0 ≤ α * morganVoyceBK q n := mul_nonneg hα hb
  have h2 : 0 < β * morganVoyceBK q (n + 1) := mul_pos hβ hb'
  rw [linFunctionalK]
  linarith

/-- **The canonical Markov-trace readout has no node.**

`tr_M(1) = 1` and `tr_M(σ₀) = z > 0`, so the readout the framework
actually derives is positive at every winding.  Combined with
`linFunctionalK_two_step`, its generation tower is log-linear up to the
`O(q⁻²ⁿ)` remainder — it cannot be bent to the observed log-concave
lepton tower, and the node escape is not available to it. -/
theorem markovReadout_pos (hq : 1 < q) {z : K} (hz : 0 < z) (n : ℕ) :
    0 < linFunctionalK 1 z q n :=
  linFunctionalK_pos hq zero_le_one hz n

/-- Restatement of the exclusion in the form the probe asserts: a positive
readout is nonzero, so every two-step ratio `φ(n+2)/φ(n)` is finite and
governed by `linFunctionalK_two_step`.  No division by a near-node. -/
theorem linFunctionalK_ne_zero (hq : 1 < q) {α β : K} (hα : 0 ≤ α)
    (hβ : 0 < β) (n : ℕ) : linFunctionalK α β q n ≠ 0 :=
  ne_of_gt (linFunctionalK_pos hq hα hβ n)

end QOU.Archimedean
