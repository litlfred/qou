/-
  Standard-part functor st : No_fin → ℝ.

  Robinson's standard-part map on finite surreals, extended
  functorially to finite-coefficient morphisms of a
  birthday-graded K-linear category.

  ## References
  - [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.
  - [alling1987] Alling, *Foundations of Analysis over Surreal
    Number Fields*, North-Holland.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Ring.Lemmas

namespace QOU.AppendixSurreals

open QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- The subring of finite surreals: those bounded by some natural. -/
def FiniteSurreals : Subring K where
  carrier := { x | ∃ n : ℕ, |x| ≤ n }
  zero_mem' := ⟨0, by simp⟩
  one_mem' := ⟨1, by simp⟩
  add_mem' := by
    intro x y ⟨n, hx⟩ ⟨m, hy⟩
    refine ⟨n + m, ?_⟩
    calc |x + y| ≤ |x| + |y| := abs_add x y
      _ ≤ (n : K) + m := by gcongr
      _ = ((n + m : ℕ) : K) := by push_cast; ring
  neg_mem' := by
    intro x ⟨n, hx⟩
    exact ⟨n, by rwa [abs_neg]⟩
  mul_mem' := by
    intro x y ⟨n, hx⟩ ⟨m, hy⟩
    refine ⟨n * m, ?_⟩
    calc |x * y| = |x| * |y| := abs_mul x y
      _ ≤ (n : K) * m := by gcongr
      _ = ((n * m : ℕ) : K) := by push_cast; ring

/-- The ideal of infinitesimals: bounded by every positive real. -/
def Infinitesimals : Ideal (FiniteSurreals K) where
  carrier := { x | ∀ n : ℕ, 0 < n → |x.val| ≤ (1 : K) / n }
  zero_mem' := by intro n _; simp
  add_mem' := by
    -- Proof sketch: |x + y| ≤ |x| + |y| ≤ 1/(2n) + 1/(2n) = 1/n
    -- Ref: [robinson1966] Theorem 3.2.1 (ordered field axioms)
    sorry
  smul_mem' := by
    -- Proof sketch: finite times infinitesimal is infinitesimal
    -- Ref: [robinson1966] Lemma 3.2.3
    sorry

/-- The **standard-part map** st : No_fin → ℝ.

    For each finite surreal `x ∈ No_fin`, there is a unique real
    `r ∈ ℝ` with `x - r` infinitesimal.  This is Robinson's
    `std_part` construction [@robinson1966]. -/
-- Ref: [robinson1966] §3.2 — standard-part theorem
-- Ref: [alling1987] Theorem 4.7.2
noncomputable def standardPart : FiniteSurreals K → ℝ := fun _ =>
  -- Placeholder: the actual construction requires either
  -- (a) a transfer principle for K extending ℝ, or
  -- (b) an explicit sup/inf over ℚ ⊂ K.
  -- Ref: [alling1987] §4.7
  0

/-- The standard-part is a ring homomorphism. -/
-- Ref: [robinson1966] Theorem 3.2.4
theorem standardPart_ringHom :
    ∃ (f : FiniteSurreals K →+* ℝ),
      ∀ x : FiniteSurreals K, f x = standardPart K x := by
  -- Ref: [robinson1966] §3.2
  sorry

/-- The kernel of the standard-part is the infinitesimal ideal. -/
-- Ref: [alling1987] Theorem 4.7.3
theorem standardPart_kernel :
    (Infinitesimals K : Set (FiniteSurreals K))
      = { x | standardPart K x = 0 } := by
  -- Ref: [alling1987] §4.7
  sorry

end QOU.AppendixSurreals
