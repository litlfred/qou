/-
  The channel rotation `(x, q) ↦ (ιx, q̄)` — even ↔ odd q-Hermite step.

  RELOCATED (no mathematical change).  `rotation_step`, together with the two step predicates
  `evenStep` / `oddStep` its statement is phrased in, was declared in
  `content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean`, a
  chapter-directory `.lean` belonging to a different content block, so the content-block
  resolver found it via neither candidate 1 (the citing block's own sibling) nor candidate 2
  (`<lakeRoot>/<Decl/Path>.lean`).  Moving it to the path matching its namespace makes candidate
  2 resolve.

  The declarations below are verbatim as they stood in the source file — same statement, same
  proof, same `-- Ref:` citations.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.MassEndomorphism
variable {R : Type*} [CommRing R]

/-- Even-channel (compact / binding / continuous q-Hermite) three-term step:
    `H_{n+2} = 2x·H_{n+1} − (1 − q^{n+1})·H_n`. -/
def evenStep (q x : R) (n : ℕ) (H0 H1 H2 : R) : Prop :=
  H2 = 2 * x * H1 - (1 - q ^ (n + 1)) * H0

/-- Odd-channel (non-compact / `𝔔_β` / `q⁻¹`-Hermite) three-term step,
    division-free (multiplied through by `q^{n+1}`):
    `h_{n+2} = 2x·h_{n+1} + (1 − q^{-(n+1)})·h_n`. -/
def oddStep (q x : R) (n : ℕ) (h0 h1 h2 : R) : Prop :=
  q ^ (n + 1) * h2 = 2 * x * (q ^ (n + 1) * h1) + (q ^ (n + 1) - 1) * h0

/-- **The channel rotation, categorical (the `x ↦ ιx`, `q ↦ q̄` rotation).**
    A sequence `h` satisfies the odd-channel (non-compact, `𝔔_β`) step at
    `(q, x)` **iff** its `ι`-rotation `n ↦ ι^n·h_n` satisfies the
    even-channel (compact, binding) step at the bar-conjugated data
    `(σq, ιx)` — where `ι` is a formal square root of `−1` in the fibre
    ring and `σ q * q = 1` is the division-free bar involution.

    This is the generic form of Askey (1989) / Ismail–Masson
    `h_n(x|q) = i^{-n}·H_n(ix|q^{-1})`: **same eigenfunctions, rotated**;
    the two channels of `𝔙` are one recurrence read through the rotation.
    No `ℂ`: the archimedean instance `ι = Complex.I` is downstream of τ. -/
theorem rotation_step (σ : R →+* R) {ι q x h0 h1 h2 : R}
    (hι : ι * ι = -1) (hq : σ q * q = 1) (n : ℕ) :
    evenStep (σ q) (ι * x) n (ι ^ n * h0) (ι ^ (n + 1) * h1) (ι ^ (n + 2) * h2)
      ↔ oddStep q x n h0 h1 h2 := by
  unfold evenStep oddStep
  have hιu : IsUnit (ι ^ n) :=
    (isUnit_of_mul_eq_one ι (-ι) (by rw [mul_neg, hι, neg_neg])).pow n
  have hqu : IsUnit (q ^ (n + 1)) :=
    (isUnit_of_mul_eq_one q (σ q) (by rw [mul_comm]; exact hq)).pow (n + 1)
  have hqn : (σ q) ^ (n + 1) * q ^ (n + 1) = 1 := by
    rw [← mul_pow, hq, one_pow]
  constructor
  · intro h
    -- cancel the unit ι^n to un-rotate, then multiply through by q^(n+1)
    have hh : ι ^ n * h2
        = ι ^ n * (2 * x * h1 + (1 - (σ q) ^ (n + 1)) * h0) := by
      linear_combination (-1 : R) * h + (ι ^ n * (h2 - 2 * x * h1)) * hι
    have hD := hιu.mul_left_cancel hh
    linear_combination (q ^ (n + 1)) * hD - h0 * hqn
  · intro h
    -- cancel the unit q^(n+1), then rotate by ι^n
    have hh : q ^ (n + 1) * h2
        = q ^ (n + 1) * (2 * x * h1 + (1 - (σ q) ^ (n + 1)) * h0) := by
      linear_combination h + h0 * hqn
    have hE := hqu.mul_left_cancel hh
    linear_combination (-(ι ^ n)) * hE + (ι ^ n * (h2 - 2 * x * h1)) * hι

end QOU.MassEndomorphism
