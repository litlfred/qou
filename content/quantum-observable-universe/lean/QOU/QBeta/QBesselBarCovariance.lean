/-
Copyright (c) 2026 litlfred. All rights reserved.

# Bar-covariance of the Hahn–Exton q-Bessel coefficient ratio (Q_β `c_k` ladder)

A formalize-first **structural constraint** for the Q_β kernel hunt (bean `qkhc`,
Stage C — `docs/scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`). It certifies
one of the four invariants any fibre-level kernel candidate must satisfy: **invariant
(b), bar-evenness under `q ↦ q⁻¹`** (`refuted-class-map §4`).

The Hahn–Exton q-Bessel argument recurrence (★), proved in
`QOU/QBeta/QBesselContiguityRecurrence.lean`, is

    c_{k+1} · (1 − q^{k+1})(1 − a q^k) = −q^k · c_k,     a = q^{ν+1}.

Its coefficient **ratio** `ρ_k := c_{k+1}/c_k = −q^k / [(1 − q^{k+1})(1 − a q^k)]`
governs the whole ladder. This file proves that under the **bar involution**
`q ↦ q⁻¹`, `a ↦ a⁻¹` the ratio transforms by a **`k`-independent twist**:

    ρ_k(q⁻¹, a⁻¹) = (a q) · ρ_k(q, a)        (a q = q^{ν+2}).

**Why it matters for the kernel hunt.** Bar-evenness of the `c_k` ladder (invariant
(b)) is, term-by-term, a `k`-dependent condition; this lemma collapses it to a
**single** `k`-independent normalisation `a q = q^{ν+2}`. So a candidate kernel either
has the right global twist (and is bar-even up to one constant) or is killed on paper
— no per-`k` anchor sweep needed. This complements the *numerical* bar-parity gate
(`qbeta_chain_d_bar_parity_gate.py`, which refuted Type-B) with the *structural*
covariance the gate rests on. It is a **necessary-condition** lemma — NOT the kernel
construction (that stays owner-gated multi-session research) and NOT a `c_k` value.

Generic base ring `[Field K]` — `q`, `a` are formal fibre parameters, no archimedean
structure (CLAUDE.md §7c). Sorry-free.

`-- Ref:` [koelink1994] https://doi.org/10.1215/S0012-7094-94-07617-0
(Hahn–Exton q-Bessel); the bar involution `q ↦ q⁻¹` is the standard quantum-group
duality (Gasper–Rahman, *Basic Hypergeometric Series*, 2nd ed., CUP 2004).
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- The coefficient ratio `ρ_k = c_{k+1}/c_k` of the Hahn–Exton q-Bessel argument
recurrence (★), with `a = q^{ν+1}` the order parameter. -/
noncomputable def heckeCoeffRatio (k : ℕ) (q a : K) : K :=
  -q ^ k / ((1 - q ^ (k + 1)) * (1 - a * q ^ k))

/-- **Bar-covariance of the q-Bessel coefficient ratio.**

Under the bar involution `q ↦ q⁻¹`, `a ↦ a⁻¹`, the ratio `ρ_k` transforms by the
`k`-independent twist `a q` (`= q^{ν+2}`):  `ρ_k(q⁻¹, a⁻¹) = (a q) · ρ_k(q, a)`.

This is the structural backbone of invariant (b) (bar-evenness): the whole `c_k`
ladder's `q ↦ q⁻¹` behaviour is a single global twist, not a `k`-by-`k` condition. -/
theorem heckeCoeffRatio_bar_covariance (k : ℕ) (q a : K)
    (hq : q ≠ 0) (ha : a ≠ 0)
    (h1 : (1 : K) - q ^ (k + 1) ≠ 0) (h2 : (1 : K) - a * q ^ k ≠ 0) :
    heckeCoeffRatio k q⁻¹ a⁻¹ = (a * q) * heckeCoeffRatio k q a := by
  unfold heckeCoeffRatio
  -- rewrite inverse-powers to `(·)⁻¹` form and `q^(k+1) → q^k * q`, so every term is
  -- a rational expression in the three atoms `q^k, q, a` and `ring` sees the inverses.
  rw [inv_pow, inv_pow, pow_succ]
  rw [pow_succ] at h1
  have hqk : q ^ k ≠ 0 := pow_ne_zero _ hq
  -- bar-side denominators are nonzero (derived from h1, h2)
  have hq1ne : q ^ k * q ≠ 1 := fun h => h1 (sub_eq_zero.mpr h.symm)
  have haqkne : a * q ^ k ≠ 1 := fun h => h2 (sub_eq_zero.mpr h.symm)
  have hb1 : (1 : K) - (q ^ k * q)⁻¹ ≠ 0 := by
    rw [sub_ne_zero]; exact (inv_ne_one.mpr hq1ne).symm
  have hb2 : (1 : K) - a⁻¹ * (q ^ k)⁻¹ ≠ 0 := by
    rw [← mul_inv, sub_ne_zero]; exact (inv_ne_one.mpr haqkne).symm
  -- generalise the atom `q^k` so `q^(k·2)` does not appear (it would block `ring`)
  set y := q ^ k with hy
  have hyq : y * q ≠ 0 := mul_ne_zero hqk hq
  have hay : a * y ≠ 0 := mul_ne_zero ha hqk
  have hd2 : (1 : K) - a * y ≠ 0 := h2
  -- put the RHS over `D₂ = (1-y*q)(1-a*y)`, cross-multiply, and clear the `⁻¹`s.
  rw [← mul_div_assoc, div_eq_div_iff (mul_ne_zero hb1 hb2) (mul_ne_zero h1 hd2)]
  field_simp
  ring

end QOU.QBeta
