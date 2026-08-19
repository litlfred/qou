/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q-Borel theta kernel `t_n = q^{C(n,2)}` (W2 ∞-Stokes building block)

Building block for the RSZ resolution of the C1 module's ∞ slope-½ singularity (bean
`qou-xufp`, W2). Per Ramis–Sauloy–Zhang, *Local analytic classification of q-difference
equations* (Astérisque 355, `library/arxiv-0903.0853v3/0903.0853v3.pdf`) §3.3 p. 39: an irregular singularity
of level `d` is resolved by a **q-Borel transform** `B_{q,d}(∑ fₙ zⁿ) = ∑ (fₙ/tₙ) ξⁿ` whose
kernel is a theta family `(tₙ)` subject to `tₙ = q^{n−d}·t_{n−d}` (growth `q^{n²/2d}`). For
level `d = 1` the canonical choice is the **Jacobi theta coefficient** `tₙ = q^{n(n−1)/2}`;
for general `d` (the ramified case — C1 is slope ½, level `d = 2`) the family is built from
Jacobi theta functions and requires `d`-th roots.

This file formalizes the `d = 1` kernel and its defining recurrence — the concrete theta
object underlying the q-Borel transform. The exponent `n(n−1)/2 = C(n,2)` makes the
recurrence a clean Pascal identity.

**Scope.** The level-1 q-Borel kernel + its recurrence only. The ramified level-2 family for
C1's slope ½, the `d`-th roots `B₁,B₂`, and the actual Stokes matrices
(`F(P₁,P₂) ≅ Matr(ℂ)²`) are NOT here — the genuine RSZ-wild residual, beaned (`qou-xufp`).
§7c: generic `Monoid` (commutativity unused). Sorry-free. No fit; nothing wired.

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§3.3, q-Borel transform)
-/
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.Group.Basic

namespace QOU.MathlibExt.QBorelKernel

variable {R : Type*} [Monoid R]

/-- **The level-1 q-Borel (Jacobi-theta) kernel** `tₙ = q^{C(n,2)} = q^{n(n−1)/2}`. This is
the canonical kernel of the q-Borel transform `B_{q,1}` resolving an integral-slope
singularity. -/
def qBorelKernel (q : R) (n : ℕ) : R := q ^ n.choose 2

@[simp] theorem qBorelKernel_zero (q : R) : qBorelKernel q 0 = 1 := by
  simp [qBorelKernel]

@[simp] theorem qBorelKernel_one (q : R) : qBorelKernel q 1 = 1 := by
  simp [qBorelKernel]

/-- **The q-Borel kernel recurrence** `t_{n+1} = q^n · tₙ` (the level-1 case
`tₙ = q^{n−1}·t_{n−1}` of the RSZ family relation). Proof: `C(n+1,2) = C(n,1) + C(n,2) =
n + C(n,2)` (Pascal), so `q^{C(n+1,2)} = q^n · q^{C(n,2)}`. -/
theorem qBorelKernel_succ (q : R) (n : ℕ) :
    qBorelKernel q (n + 1) = q ^ n * qBorelKernel q n := by
  unfold qBorelKernel
  rw [Nat.choose_succ_succ, Nat.choose_one_right, pow_add]

end QOU.MathlibExt.QBorelKernel
