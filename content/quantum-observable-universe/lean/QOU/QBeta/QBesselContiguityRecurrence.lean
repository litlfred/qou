/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Bessel contiguity ⟹ the `c_k` coefficient recurrence; C-finite as a degeneration

The algebraic skeleton of the "derive the `c_k` recurrence from q-Bessel
contiguity" result (compute:
`folio-assistant/computations/qbeta/qbeta_qbessel_contiguity_cfinite.py`;
audit: `docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`).

The Hahn–Exton q-Bessel function `J_ν(x;q)` (the matrix coefficient of `E_q(2)`,
Vaksman–Korogodsky 1989 / Koelink 1994) has power-series coefficients

    c_k = (−1)^k q^{k(k−1)/2} / [(q;q)_k (q^{ν+1};q)_k]

satisfying the **exact first-order q-recurrence** (verified to `<1e-40` in the
compute), with `a := q^{ν+1}`:

    c_{k+1} · (1 − q^{k+1})(1 − a q^k) = −q^k · c_k.                    (★)

(★) is **first-order with `q^k`-dependent coefficients** — i.e. the `c_k` are
**q-holonomic**, NOT C-finite. A constant-coefficient (C-finite) recurrence is
the special **degeneration** that occurs only when the ratio is `k`-independent
(the rational / `q → 1` limit). This is exactly why PR #1839 found **no
low-order constant-coefficient recurrence** for the canonical `c_2..c_10`, while
the pole/dominant-root structure survives — the kernel `R` of `F(qξ)=R·F(ξ)`
(`QOU/QBeta/RationalCoeffRecurrence.lean`) is the q-Bessel q-difference
operator, not a rational degeneration.

This file proves: (1) (★) ⟹ the closed product form of the coefficients
(first-order q-holonomic); (2) the C-finite degeneration (constant ratio ⟹
geometric). The order-2 C-finite pole structure is in
`RationalCoeffRecurrence.pole_reciprocal_is_char_root`.

Generic base ring `[Field K]` (no archimedean structure — `q`, `a` are formal
fibre parameters; cf. CLAUDE.md §7c). Sorry-free.
-/
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

open scoped BigOperators

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- **First-order linear recurrence ⟹ product solution.** If `c_{k+1} = r_k · c_k`
for all `k`, then `c_k = c_0 · ∏_{j<k} r_j`. -/
theorem first_order_solution (r c : ℕ → K)
    (h : ∀ k, c (k + 1) = r k * c k) (k : ℕ) :
    c k = c 0 * ∏ j ∈ Finset.range k, r j := by
  induction k with
  | zero => simp
  | succ n ih => rw [h, ih, Finset.prod_range_succ]; ring

/-- The Hahn–Exton q-Bessel coefficient ratio `r_k = −q^k / [(1−q^{k+1})(1−a q^k)]`
(with `a = q^{ν+1}`). The `q^k`-dependence is what makes the `c_k` q-holonomic
rather than C-finite. -/
def qbesselRatio (q a : K) (k : ℕ) : K :=
  -q ^ k / ((1 - q ^ (k + 1)) * (1 - a * q ^ k))

/-- **q-Bessel contiguity ⟹ closed-form coefficients (q-holonomic).** From the
first-order q-recurrence (★) and the non-degeneracy of its denominators, the
coefficients are the q-hypergeometric product `c_k = c_0 · ∏_{j<k} r_j`. -/
theorem qbessel_coeff_closed_form (q a : K) (c : ℕ → K)
    (hD : ∀ k, (1 - q ^ (k + 1)) * (1 - a * q ^ k) ≠ 0)
    (hrec : ∀ k, c (k + 1) * ((1 - q ^ (k + 1)) * (1 - a * q ^ k)) = -q ^ k * c k)
    (k : ℕ) :
    c k = c 0 * ∏ j ∈ Finset.range k, qbesselRatio q a j := by
  refine first_order_solution (qbesselRatio q a) c (fun n => ?_) k
  rw [qbesselRatio, div_mul_eq_mul_div, eq_div_iff (hD n)]
  exact hrec n

/-- **C-finite degeneration.** When the ratio is a *constant* `ρ` (the rational /
`q → 1` limit), the sequence is geometric `c_k = c_0 · ρ^k` — C-finite of order 1
with characteristic root `ρ`. The genuine q-Bessel case has the `q^k`-dependent
ratio `qbesselRatio` above and is therefore NOT of this form: it is q-holonomic,
which is why the canonical `c_k` admit no low-order constant-coefficient
recurrence (#1839). -/
theorem geometric_of_constant_ratio (r c : ℕ → K) (ρ : K)
    (hconst : ∀ k, r k = ρ) (hrec : ∀ k, c (k + 1) = r k * c k) (k : ℕ) :
    c k = c 0 * ρ ^ k := by
  rw [first_order_solution r c hrec k]
  simp [hconst, Finset.prod_const, Finset.card_range]

end QOU.QBeta
