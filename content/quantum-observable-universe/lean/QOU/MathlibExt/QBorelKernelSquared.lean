/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Tactic
import QOU.MathlibExt.QBorelKernel
import QOU.MathlibExt.QBorelKernelLevel

/-!
# The squared level-1 q-Borel kernel — the divisor the deuteron statistic needs

`computations/deltalambda/deuteron_qborel_kernel_level_probe.py` measures the divergence class of
the deuteron binding statistic `Z_n(q₀)` and finds `Z_n ~ q₀^{n²}` (second differences of `log Z_n`
rise to `2 ln q₀`, and `d²(a·n²) = 2a`).  The corpus had recorded `q₀^{n²/2}`; that is the order of
the kernel-STRIPPED object `S^bal = Z_n / q^{C(n,2)}`, not of `Z_n`.

This file formalises the small arithmetic that turns that measurement into a statement about
*which kernel*, so the bookkeeping is machine-checked rather than asserted in a docstring.

## The point

The level-1 q-Borel kernel is `qBorelKernel q n = q^{C(n,2)}`, and `QBorelKernelLevel` records
`qBorelExp 1 n = C(n,2)`.  The exponent needed to remove `Z_n`'s growth is `n(n+1)` (at index
`n+1`), and `two_mul_qBorelExp_one` says that is **exactly twice** the level-1 exponent.  So one
application of the level-1 kernel supplies precisely half of what is required — which is what the
probe measures: after dividing by `q^{C(n,2)}` the second difference still rises to a *positive*
constant (`ln q₀`), and only after dividing by `q^{n(n-1)}` does it fall to zero.

This is a statement of arithmetic, not of convergence.  It says which exponent is needed; it says
nothing about where the q-Laplace transform lands, and the probe explicitly does not claim that
(`R3c_residual_asymptotics_NOT_settled_scope_gate`).
-/

namespace QOU.MathlibExt.QBorelKernel

variable {R : Type*} [Monoid R]

/-- **Twice the triangular number.**  `2·C(n+1,2) = n(n+1)`.

Stated at `n+1` deliberately: `C(n,2) = n(n-1)/2` involves truncated subtraction on `ℕ`, whereas
`C(n+1,2) = n(n+1)/2` does not, so the doubled form is subtraction-free. -/
theorem two_mul_choose_two_succ (n : ℕ) : 2 * (n + 1).choose 2 = n * (n + 1) := by
  induction n with
  | zero => simp
  | succ k ih =>
    have h : (k + 2).choose 2 = (k + 1) + (k + 1).choose 2 := by
      rw [Nat.choose_succ_succ (k + 1) 1, Nat.choose_one_right]
    rw [h, Nat.mul_add, ih]
    ring

/-- **The required divisor is exactly the level-1 exponent doubled.**  `2·qBorelExp 1 (n+1) =
n(n+1)`.  One application of the level-1 q-Borel kernel supplies half of what `Z_n(q₀)` needs. -/
theorem two_mul_qBorelExp_one (n : ℕ) : 2 * qBorelExp 1 (n + 1) = n * (n + 1) := by
  rw [qBorelExp_one_eq_choose]
  exact two_mul_choose_two_succ n

/-- **The squared level-1 kernel has exponent `n(n+1)`.**  `t_{n+1}² = q^{n(n+1)}`, the divisor the
probe measures as the one that removes `Z_n`'s quadratic growth exactly. -/
theorem qBorelKernel_mul_self (q : R) (n : ℕ) :
    qBorelKernel q (n + 1) * qBorelKernel q (n + 1) = q ^ (n * (n + 1)) := by
  unfold qBorelKernel
  rw [← pow_add, ← two_mul, two_mul_choose_two_succ]

/-- **Corollary: the level-1 kernel alone is strictly short whenever `n ≥ 1`.**  Its exponent
`C(n+1,2)` is strictly below the required `n(n+1)`, so no single level-1 division can remove the
growth — the gap is another full copy of the same kernel. -/
theorem qBorelExp_one_lt_required {n : ℕ} (hn : 1 ≤ n) :
    qBorelExp 1 (n + 1) < n * (n + 1) := by
  have h2 : 2 * qBorelExp 1 (n + 1) = n * (n + 1) := two_mul_qBorelExp_one n
  have hpos : 0 < qBorelExp 1 (n + 1) := by
    rw [qBorelExp_one_eq_choose]
    exact Nat.choose_pos (by omega)
  omega

end QOU.MathlibExt.QBorelKernel
