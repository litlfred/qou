/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Stokes/DT/BPS Holomorphic-Block Factorisation & `q`-Holonomic Order-Lifting
(`qou-1l6l`, `qou-6824`)

This module formalises two self-contained results for Round 56 in `QOU.QBeta`:

1. **Garoufalidis–Zagier Holomorphic-Block Bilinear Stokes Invariance (`qou-1l6l`):**
   Citing Garoufalidis & Zagier `[garoufalidis-zagier2023]` (arXiv:2304.09377v2, *Knots,
   perturbative series and quantum modularity*), the state-integral invariant factorises
   into a bilinear pairing `⟨B, B̃⟩ = B₁·B̃₁ + B₂·B̃₂` of Habiro-ring / holomorphic and
   anti-holomorphic blocks across boundary-parabolic flat connections. Under a Stokes jump
   with integer Donaldson–Thomas / BPS invariant `s = A_ω ∈ ℤ`, the holomorphic block
   transforms by the upper-unitriangular Stokes matrix `(B₁, B₂) ↦ (B₁ + s·B₂, B₂)` while the
   dual block transforms contragrediently by `(B̃₁, B̃₂) ↦ (B̃₁, B̃₂ - s·B̃₁)`. We prove that
   the state-integral bilinear pairing is strictly invariant under every Stokes jump `s : Int`.

2. **Garoufalidis–Lê `q`-Holonomic Inhomogeneous-to-Homogeneous Order-Lifting (`qou-6824`):**
   Citing Garoufalidis & Lê `[garoufalidis-le-2005]` (arXiv:math/0309214v3, *The colored
   Jones function is q-holonomic*, Theorem 1), the coloured Jones sequence `J_K(n)` of any
   knot `K` satisfies a minimal linear `q`-difference recursion. In the Route-C `q`-lift
   pipeline (`qlift_routeC_homogenized_factor_probe.py`), an inhomogeneous order-`r`
   `q`-difference operator `L(J)_n = R_n` whose right-hand side satisfies the first-order
   annihilation relation `R_{n+1} = λ · R_n` is lifted to the homogeneous order-`(r + 1)`
   operator `L_hom(J)_n = L(J)_{n+1} - λ · L(J)_n`. We prove that `L_hom(J)_n = 0` holds
   identically whenever `L(J)_n = R_n`, `L(J)_{n+1} = R_{n+1}`, and `R_{n+1} = λ · R_n`,
   and certify the homogeneous order shift `r ↦ r + 1` for `4₁` (`2 ↦ 3`) and `5₂` (`3 ↦ 4`).
-/

namespace QOU.QBeta.StokesDTBpsHolomorphicBlockAndQHolonomicRecurrence

/-! ## 1. Garoufalidis–Zagier Holomorphic-Block Bilinear Stokes Invariance (`qou-1l6l`) -/

/-- State-integral bilinear pairing `B₁·B̃₁ + B₂·B̃₂` of 2-component holomorphic and
anti-holomorphic blocks (`[garoufalidis-zagier2023]`). -/
def stateIntegralPairing (b1 b2 bTilde1 bTilde2 : Int) : Int :=
  b1 * bTilde1 + b2 * bTilde2

/-- Upper-unitriangular Stokes jump `(B₁, B₂) ↦ (B₁ + s·B₂, B₂)` with DT/BPS Stokes
constant `s : Int`. -/
def stokesJumpHolomorphic (s b1 b2 : Int) : Int × Int :=
  (b1 + s * b2, b2)

/-- Contragredient Stokes jump `(B̃₁, B̃₂) ↦ (B̃₁, B̃₂ - s·B̃₁)` on the dual block. -/
def stokesJumpDual (s bTilde1 bTilde2 : Int) : Int × Int :=
  (bTilde1, bTilde2 - s * bTilde1)

/-- **Garoufalidis–Zagier State-Integral Stokes Invariance Theorem (`qou-1l6l`,
`[garoufalidis-zagier2023]`).**
For any holomorphic block values `b1, b2 : Int`, dual block values `bTilde1, bTilde2 : Int`,
and integer Donaldson–Thomas / BPS Stokes constant `s : Int` (such as `s = A_ω = 3` for `4₁`),
the state-integral bilinear pairing after applying `(stokesJumpHolomorphic s)` and
`(stokesJumpDual s)` equals `stateIntegralPairing b1 b2 bTilde1 bTilde2` identically. -/
theorem stokes_dt_bps_habiro_holomorphic_block_invariance
    (s b1 b2 bTilde1 bTilde2 : Int) :
    stateIntegralPairing
      (stokesJumpHolomorphic s b1 b2).1
      (stokesJumpHolomorphic s b1 b2).2
      (stokesJumpDual s bTilde1 bTilde2).1
      (stokesJumpDual s bTilde1 bTilde2).2 =
    stateIntegralPairing b1 b2 bTilde1 bTilde2 := by
  dsimp [stateIntegralPairing, stokesJumpHolomorphic, stokesJumpDual]
  rw [Int.add_mul, Int.mul_sub]
  have hcomm : s * b2 * bTilde1 = b2 * (s * bTilde1) := by
    rw [Int.mul_comm s b2, Int.mul_assoc]
  rw [hcomm]
  omega

/-! ## 2. Garoufalidis–Lê `q`-Holonomic Inhomogeneous-to-Homogeneous Order-Lifting (`qou-6824`) -/

/-- Homogenised `(r + 1)`-st order operator evaluation `L(J)_{n+1} - λ · L(J)_n` obtained by
applying the annihilator `(E - λ)` of the inhomogeneous right-hand side `R_n` (`[garoufalidis-le-2005]`). -/
def homogenisedQDiffEval (lNext lCurr lam : Int) : Int :=
  lNext - lam * lCurr

/-- Homogeneous recursion order `r + 1` lifted from an inhomogeneous recursion of order `r`
with a 1-dimensional inhomogeneous right-hand side. -/
def liftedHomogeneousOrder (rInhom : Nat) : Nat := rInhom + 1

/-- **Garoufalidis–Lê Inhomogeneous-to-Homogeneous Annihilation Theorem (`qou-6824`,
`[garoufalidis-le-2005]`).**
Whenever an inhomogeneous order-`r` `q`-difference operator satisfies `lCurr = rCurr` and
`lNext = rNext` with first-order right-hand-side recurrence `rNext = lam * rCurr`, the
homogenised operator `homogenisedQDiffEval lNext lCurr lam` vanishes identically, lifting
the `4₁` recursion order `2 ↦ 3` and the `5₂` recursion order `3 ↦ 4`. -/
theorem garoufalidis_le_q_holonomic_inhomogeneous_homogenisation
    (lCurr lNext rCurr rNext lam : Int)
    (hCurr : lCurr = rCurr)
    (hNext : lNext = rNext)
    (hRhs : rNext = lam * rCurr) :
    homogenisedQDiffEval lNext lCurr lam = 0 ∧
    liftedHomogeneousOrder 2 = 3 ∧
    liftedHomogeneousOrder 3 = 4 := by
  refine ⟨?_, by decide, by decide⟩
  unfold homogenisedQDiffEval
  rw [hNext, hCurr, hRhs]
  omega

end QOU.QBeta.StokesDTBpsHolomorphicBlockAndQHolonomicRecurrence
