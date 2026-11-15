/-
Copyright (c) 2026 litlfred. All rights reserved.

# Local exponents of the C1 q-difference module at 0 (W2, Birkhoff-matrix 0-side)

W2 brick (bean `qou-xufp`). The DRSZ Birkhoff connection matrix `P=(X^∞)⁻¹X^0` of the C1
q-difference module needs the local exponents (eigenvalues of the companion) at `0`.
C1 = RSZ route-A `L1 = (q²x−1)σ² − (q−1)σ − (q−1)`; its companion at `x=0` is
`A(0) = [[0,1],[1−q,1−q]]`, with `tr A(0) = 1−q` and `det A(0) = q−1` (computed in the
witness `computations/qbeta/c3_w2_c1_module_exponents.witness.json`).

The **exponent polynomial** (characteristic polynomial of `A(0)`, `t² − tr·t + det`) is
therefore `t² + (q−1)t + (q−1)`, with exponent-discriminant `(q−1)(q−5)`. Its roots are the
C1 local exponents at 0, feeding the Fuchsian 0-side canonical solution
`X^0 = M^0·diag(e_{q,λ₊}, e_{q,λ₋})`. (At `∞` the companion is nilpotent — irregular
slope-½ — so the full Birkhoff matrix needs Stokes; beaned, not here.)

This file formalizes the exponent polynomial, its trace/det (char-poly) form, its
discriminant, and the root reduction. §7c: generic `CommRing`; the matrix trace/det are
witness-computed scalars, so no `Matrix` dependency is needed. Sorry-free. No fit; nothing
wired; no `symbol=C1` claim.

-- Ref: [manuscript] docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md (C1 = L1)
-- Ref: [manuscript] library/equations-aux-q-differences/Equations_aux_q-differences.pdf (DRSZ Birkhoff recipe)
-/
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.Mass.C1ModuleExponents

variable {R : Type*} [CommRing R]

/-- **The C1 exponent polynomial at 0** `t² + (q−1)t + (q−1)` — the characteristic
polynomial of the companion `A(0) = [[0,1],[1−q,1−q]]`. Its roots are the local exponents. -/
def c1ExponentPoly (q t : R) : R := t ^ 2 + (q - 1) * t + (q - 1)

/-- **Char-polynomial form** `t² − (tr A(0))·t + det A(0)` with `tr A(0)=1−q`, `det A(0)=q−1`
(witness-computed). Confirms `c1ExponentPoly` is the companion's characteristic polynomial. -/
theorem c1ExponentPoly_eq_char (q t : R) :
    c1ExponentPoly q t = t ^ 2 - (1 - q) * t + (q - 1) := by
  simp only [c1ExponentPoly]; ring

/-- **Exponent discriminant** `(q−1)² − 4(q−1) = (q−1)(q−5)` — the exponent difference
`(λ₊−λ₋)²`. Nonzero off `q ∈ {1,5}`, so the two local exponents at 0 are generically
distinct (diagonalisable local monodromy). -/
theorem c1_exponent_discriminant (q : R) :
    (q - 1) ^ 2 - 4 * (q - 1) = (q - 1) * (q - 5) := by ring

/-- **Root reduction.** Every exponent `t` satisfies `t² = (1−q)t − (q−1)` — the order-2
relation the C1 recurrence imposes on its local solutions. -/
theorem c1_root_reduction {q t : R} (h : c1ExponentPoly q t = 0) :
    t ^ 2 = (1 - q) * t - (q - 1) := by
  simp only [c1ExponentPoly] at h; linear_combination h

/-- **Vieta for the exponents.** If the exponent polynomial factors over `R` as
`(t − λ₊)(t − λ₋)`, the exponents sum to `1 − q` (= `tr A(0)`) and multiply to `q − 1`
(= `det A(0)`). -/
theorem c1_exponent_vieta {q lp lm : R}
    (h : ∀ t : R, c1ExponentPoly q t = (t - lp) * (t - lm)) :
    lp + lm = 1 - q ∧ lp * lm = q - 1 := by
  have h0 := h 0
  have h1 := h 1
  simp only [c1ExponentPoly] at h0 h1
  refine ⟨?_, ?_⟩
  · linear_combination h1 - h0
  · linear_combination -h0

end QOU.Mass.C1ModuleExponents
