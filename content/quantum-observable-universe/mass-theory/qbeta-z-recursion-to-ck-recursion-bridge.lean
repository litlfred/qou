import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.BraidKnot — z-recursion forward form (bridge to CKRecursion)

**Bridge between the $z$-Taylor recursion class `ZRecursionCoeffs`
(from `prop:qbeta-per-block-chi-closed-forms`, PR #1764) and the
generic $c_k$ depth-$d$ ladder recursion structure
`QOU.QBeta.CKRecursion.CKRecursion` (from
`prop:q-beta-c-k-recursion-from-habiro-q-difference`, landed on main
2026-06-03).**

The two recursions are STRUCTURALLY DIFFERENT — the z-recursion has
variable kernel (functions of n), the c_k ladder has constant kernel
(`Fin depth → R`). This file does NOT construct a `CKRecursion ℝ`
instance from `ZRecursionCoeffs`; instead it formalises the
forward (solve-for-`a_{n+1}`) form of the z-recursion, exposing the
n-dependent kernel structure explicitly. See the accompanying .md
for the structural-comparison table.

**Inlined `ZRecursionCoeffs` declaration.** Content-block `.lean`
files live outside the Lake source tree, so the class declaration
from PR #1764 is not cross-importable here. We inline a
byte-identical copy of `ZRecursionCoeffs` (AGENTS.md §3b-cond
class-axiomatisation pattern; the actual class instance is the open
math, both here and in PR #1764).

LaTeX label: `prop:qbeta-z-recursion-to-ck-recursion-bridge`
-/

namespace QOU.BraidKnot

/-- Inlined from `prop:qbeta-per-block-chi-closed-forms` (PR #1764). -/
class ZRecursionCoeffs where
  a : ℕ → ℝ
  initial_0 : a 0 = 1/2
  initial_1 : a 1 = 0
  recursion : ∀ n : ℕ, n ≥ 1 →
    4*((n : ℝ)+1) * a (n+1) + 6*(n : ℝ) * a n + (2*(n : ℝ)-1) * a (n-1) = 0

/-- The n-dependent kernel of the z-Taylor 3-term recursion in
forward form. Note: NOT constant in n, hence not directly an instance
of `CKRecursion ℝ`'s `Fin depth → R` constant-kernel structure. -/
noncomputable def z_recursion_kernel (n : ℕ) : Fin 2 → ℝ
  | 0 => -(3 * (n : ℝ)) / (2 * ((n : ℝ) + 1))   -- coefficient of a_n
  | 1 => -((2 * (n : ℝ) - 1)) / (4 * ((n : ℝ) + 1))  -- coefficient of a_{n-1}

/-- **Theorem (forward form of the z-recursion).** For any
`ZRecursionCoeffs` instance and any `n ≥ 1`,
`a_{n+1}` is a linear combination of `a_n` and `a_{n-1}` with
coefficients given by `z_recursion_kernel n`.

This makes explicit the depth-2 linear structure of the z-Taylor
recursion, in the form analogous to (but with variable kernel
instead of constant kernel of) `QOU.QBeta.CKRecursion.applyRecursion`.

**Proof.** Algebraic rearrangement of `w.recursion n hn`. -/
theorem z_recursion_forward_form (w : ZRecursionCoeffs) (n : ℕ) (hn : n ≥ 1) :
    w.a (n+1) = z_recursion_kernel n 0 * w.a n + z_recursion_kernel n 1 * w.a (n-1) := by
  have hrec := w.recursion n hn
  -- Solve for w.a (n+1):
  -- 4(n+1)·a(n+1) = -6n·a(n) - (2n-1)·a(n-1)
  -- a(n+1) = [-3n/(2(n+1))]·a(n) + [-(2n-1)/(4(n+1))]·a(n-1)
  unfold z_recursion_kernel
  have hn1 : ((n : ℝ) + 1) ≠ 0 := by positivity
  field_simp [hn1]
  linarith [hrec]

end QOU.BraidKnot
