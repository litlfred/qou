/-
Copyright (c) 2026 litlfred. All rights reserved.

# C1's ∞ Newton edge forces a quadratic extension (W2 stage S2, partial)

`L1 = (q²x−1)σ² − (q−1)σ − (q−1)`. Reading `deg_x` of the coefficients gives
`deg a₂ = 1`, `deg a₁ = 0`, `deg a₀ = 0`, hence Newton points `(0,1), (1,1), (2,0)`
at `∞` and the single edge `(2,0)→(0,1)` of slope `½` (independently reproducing
the edge recorded in `2026-08-01-c1-inf-slope-half-rsz-stokes.md`).

The edge height at `i = 1` is `½`, **not a lattice point**, so `i = 1` sits
strictly above the edge and contributes nothing. Only the endpoints do:

* `i = 2` contributes the `x`-leading coefficient of `a₂`, namely `q²`;
* `i = 0` contributes the `x`-constant coefficient of `a₀`, namely `−(q−1)`.

So the **characteristic equation of the edge** is `q²t² − (q−1) = 0`, i.e.
`t² = (q−1)/q²`.

This file proves that equation has **no solution with `t` a rational function of
`q`** — a quadratic extension is genuinely forced. Since `q²` is already a
square, that reduces to: `q − 1` is not a square in `ℚ[q]`. The argument is a
degree parity: `f² = q − 1` would need `2·deg f = 1`.

**Scope — deliberately narrow.** This is about the *characteristic equation of
the Newton edge*. It is **NOT** the identification of RSZ's `A₁, A₂`. Per RSZ
§3.3 (Astérisque 355, p. 39, `uploads/0903.0853v3.pdf`), `A₁, A₂` are the leading
matrices of the **two slope components** `P₁, P₂`, and `B₁, B₂` are *one* `d`-th
root of each — not two roots of a single object. Identifying `A₁, A₂` for C1
requires the slope decomposition and is the remaining part of stage S2
(`qou-qbr3`). Nothing here claims that identification.

For the record, the same RSZ passage is what makes the multiplier count `2`: the
obstructions are indexed by **residues mod `d`**, giving `d` obstructions in
`Mat_{r₁,r₂}(ℂ)`; with `d = 2`, `r₁ = r₂ = 1` that is `ℂ²`.

§7c: `ℚ[X]` — pure algebra over a domain; no ordering, nothing archimedean.
Sorry-free. No fit; nothing wired; no Stokes multiplier computed.

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§3.3 p. 39)
-- Ref: [manuscript] docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas

namespace QOU.QBeta

open Polynomial

/-- The Newton-edge characteristic polynomial in the unknown `t`, with the `q`-side
written additively: the edge equation is `q²t² = (q−1)`, so after clearing the
(already square) `q²` the question is whether `X − 1` is a square. -/
noncomputable def newtonEdgeConstant : Polynomial ℚ := X - C 1

@[simp] theorem newtonEdgeConstant_natDegree : newtonEdgeConstant.natDegree = 1 := by
  simpa [newtonEdgeConstant] using natDegree_X_sub_C (1 : ℚ)

theorem newtonEdgeConstant_ne_zero : newtonEdgeConstant ≠ 0 :=
  X_sub_C_ne_zero (1 : ℚ)

/-- **The ramification is not removable.** `q − 1` is not a square in `ℚ[q]`:
`f² = q − 1` would force `2·natDegree f = 1`, impossible. Hence the Newton-edge
equation `q²t² = q − 1` has no solution `t` in `ℚ(q)` (the `q²` is already a
square, so a solution there would give one here), and the slope-½ edge genuinely
requires adjoining `√(q−1)`. -/
theorem not_isSquare_newtonEdgeConstant :
    ¬ ∃ f : Polynomial ℚ, f * f = newtonEdgeConstant := by
  rintro ⟨f, hf⟩
  have hf0 : f ≠ 0 := by
    intro h
    rw [h, zero_mul] at hf
    exact newtonEdgeConstant_ne_zero hf.symm
  have hdeg : (f * f).natDegree = 1 := by
    rw [hf, newtonEdgeConstant_natDegree]
  rw [natDegree_mul hf0 hf0] at hdeg
  omega

/-- Restated in Mathlib's `IsSquare` form. -/
theorem not_isSquare_X_sub_one : ¬ IsSquare (newtonEdgeConstant) := by
  rintro ⟨f, hf⟩
  exact not_isSquare_newtonEdgeConstant ⟨f, hf.symm⟩

end QOU.QBeta
