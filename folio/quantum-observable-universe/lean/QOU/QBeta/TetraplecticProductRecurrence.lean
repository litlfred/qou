/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q²-shift functional equation of the tetraplectic product (c₃ reduction backbone)

Formalize-first brick for the c₃ Faddeev tetraplectic→combinatorics reduction
(bean `qou-5843`; scope
`docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md`).

The reduction closes the Faddeev `Φ_b` contour into the modular-double residue
product whose single sinh-lattice factor is `∏_{n≥0}(1 + q^{2n+1} x)`, and reads off
`[x^k] = e_k(q, q³, q⁵, …)`. The scope doc states the lowest term is `q^{k²}` but
leaves the closed form informal; the companion Python witness pins the full closed
form `e_k = q^{k²} / (q²; q²)_k` symbolically.

This file formalizes the **recurrence backbone** that *forces* that closed form: the
finite tetraplectic product `P_N(x) = ∏_{n=0}^{N-1}(1 + q^{2n+1} x)` satisfies the
q²-dilation functional equation

  `(1 + q x) · P_N(q² x) = (1 + q^{2N+1} x) · P_N(x)`,

both sides being `P_{N+1}(x)`. A normalized power-series solution of the `N→∞` limit
`(1 + q x)·P(q²x) = P(x)` has coefficients `c_k` obeying
`c_k (1 − q^{2k}) = q^{2k−1} c_{k−1}`, i.e. `c_k = q^{k²}/(q²;q²)_k` — the closed form
the reduction needs. So this identity is the algebraic heart of the "tetraplectic →
Young → q-Pochhammer" step, proved here by telescoping.

**Scope (structural identity, not the physics).** This proves the product recurrence
only. It does **not** evaluate the c₃ carrier `S = c₃ + Vol(4₁)` — that requires the
transcendental argument map `z(q₀)` (meridian holonomy), which the deformation-gap
audit `2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md` proved is *not* a
combinatorial object (`dc₃/dq ≈ 4.7×10⁶`, smooth deformation excluded). That open
observable is beaned separately; nothing here is wired or fitted. §7c: generic
`{R : Type*} [CommRing R]`, no `ℝ`. Sorry-free.

-- Ref: [leitner2026] docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

namespace QOU.QBeta.TetraplecticProductRecurrence

open Finset

variable {R : Type*} [CommRing R]

/-- The finite tetraplectic single-lattice product
`P_N(x) = ∏_{n=0}^{N-1} (1 + q^{2n+1} x)`. -/
def tetraProd (q x : R) (N : ℕ) : R :=
  ∏ n ∈ Finset.range N, (1 + q ^ (2 * n + 1) * x)

@[simp] theorem tetraProd_zero (q x : R) : tetraProd q x 0 = 1 := by
  simp [tetraProd]

theorem tetraProd_succ (q x : R) (N : ℕ) :
    tetraProd q x (N + 1) = tetraProd q x N * (1 + q ^ (2 * N + 1) * x) := by
  simp [tetraProd, Finset.prod_range_succ]

/-- **The q²-dilation functional equation of the tetraplectic product.**
`(1 + q x) · P_N(q² x) = (1 + q^{2N+1} x) · P_N(x)`. Both sides equal `P_{N+1}(x)`:
the left factors `(1+qx)` back in as the `n=0` term after the `q²`-dilation reindexes
`n ↦ n+1`; the right appends the `n=N` term. This is the recurrence that pins the
`q^{k²}/(q²;q²)_k` coefficients of the reduction. -/
theorem tetraProd_funcEq (q x : R) (N : ℕ) :
    (1 + q * x) * tetraProd q (q ^ 2 * x) N
      = (1 + q ^ (2 * N + 1) * x) * tetraProd q x N := by
  -- right side is `P_{N+1}(x)` directly
  have hR : (1 + q ^ (2 * N + 1) * x) * tetraProd q x N = tetraProd q x (N + 1) := by
    rw [tetraProd_succ]; ring
  -- left side: dilation reindexes n ↦ n+1, and (1+qx) is the recovered n=0 factor
  have hdil : tetraProd q (q ^ 2 * x) N
      = ∏ n ∈ Finset.range N, (1 + q ^ (2 * (n + 1) + 1) * x) := by
    unfold tetraProd
    refine Finset.prod_congr rfl ?_
    intro n _
    ring
  have hL : (1 + q * x) * tetraProd q (q ^ 2 * x) N = tetraProd q x (N + 1) := by
    rw [hdil, tetraProd]
    rw [Finset.prod_range_succ']
    ring
  rw [hL, hR]

/-- **Explicit `x¹`-coefficient (the `e_1` telescope).** The first tetraplectic
symmetric function `e_1` over the finite lattice is the geometric sum
`∑_{n<N} q^{2n+1}`; here in cleared form `(q² − 1)·∑_{n<N} q^{2n+1} = q^{2N+1} − q`,
the `N→∞` limit of which is `q/(1−q²) = q^{1²}/(q²;q²)_1`, the `k=1` closed form.
Proved by induction on `N`. -/
theorem e1_lattice_sum (q : R) (N : ℕ) :
    (q ^ 2 - 1) * ∑ n ∈ Finset.range N, q ^ (2 * n + 1) = q ^ (2 * N + 1) - q := by
  induction N with
  | zero => simp
  | succ M ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    ring

end QOU.QBeta.TetraplecticProductRecurrence
