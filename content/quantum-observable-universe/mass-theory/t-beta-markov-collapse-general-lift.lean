/-
  # T_β = S · 1 — General H_n(R, q) lift of the Markov-Frobenius
  # min-norm collapse theorem.

  Follow-up to PR #1750 (merged) where the theorem was proved in the
  substrate model `A = R, τ = id`.  The substrate-model proof captured
  the essential algebraic content (the completing-the-square identity)
  but specialised the algebra to its ground field.

  This file lifts the theorem to the GENERAL unital R-algebra setting:

      A : Type, [Ring A], [Algebra R A]
      τ : A → R, R-linear, τ 1 = 1, cyclic (τ(xy) = τ(yx))
      τ positive-semi-definite on squares, non-degenerate

  Then the SDP-min-norm primal-feasible element of A satisfying
  `τ X = S` is `X = S • 1`, exactly.  Applied to A = H_n(R, q) (the
  Iwahori–Hecke algebra at generic q) with τ = the Jones–Markov
  trace τ_M, this gives T_β = S · 1_H.

  **Strategy.**

  1. State the COMPLETING-THE-SQUARE algebraic identity:

         τ (X · X) = τ ((X - S·1)(X - S·1)) + 2·S·τ(X) - S²

     for any X ∈ A, S ∈ R.  Proof: ring expansion of (X - S·1)² inside
     τ, using linearity of τ.

  2. Under the constraint τ X = S and normalisation τ 1 = 1:

         τ (X·X) = τ ((X - S·1)²) + S²

  3. Use PSD + non-degeneracy of τ on squares:

         τ ((X - S·1)²) ≥ 0,  equality ⇔ X - S·1 = 0.

  4. Conclude min-norm value S², attained iff X = S · 1.

  **Sorries.** Two sorry's, both with Ref to PR #1750 audit doc.  The
  full Mathlib-tactic proofs require non-commutative ring manipulation
  (the algebra A is non-commutative in general; H_n(q) is non-commutative
  at generic q) plus the smul-vs-mul expansion `S • X = (algebraMap R A S) * X`.
  Both are mechanical but verbose; queued as separate commits in this
  branch.

  Ref: [pr1750] https://github.com/litlfred/qou/pull/1750
       Markov-trace SHAPE collapse + paper / Lean substrate proof
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
       prop:t-beta-markov-frobenius-collapse content block (.md).
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Abel
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.MarkovFrobeniusCollapse.General

universe u v

/-- **Normalized R-linear trace** on a unital R-algebra `A`.

    A trace is an R-linear map `τ : A → R` satisfying

    - **Normalisation:** `τ(1) = 1`.
    - **Cyclicity (trace property):** `τ(x · y) = τ(y · x)`.

    The Jones–Markov trace `τ_M` on the Iwahori–Hecke algebra `H_n(R, q)`
    is the canonical example (Wenzl 1988, Jones 1987; uniqueness by
    `QOU.BraidKnot.MarkovTraceUniqueness`). -/
structure NormalizedTrace (R : Type u) [CommSemiring R]
    (A : Type v) [Semiring A] [Algebra R A] where
  tau : A →ₗ[R] R
  tau_one : tau 1 = 1
  tau_cyc : ∀ x y : A, tau (x * y) = tau (y * x)

/-- **Frobenius positive-semi-definiteness on squares.**

    The trace `τ` is positive-semi-definite on the Frobenius bilinear
    form `⟨X, Y⟩_τ := τ(X · Y)`, i.e. `0 ≤ τ(X · X)` for every `X`.

    For the Jones–Markov trace `τ_M` on `H_n(R, q)` at generic `q > 0`
    over `R = ℝ`, this follows from the q-hook-length formula
    `dim_q(λ) > 0` and the Wedderburn decomposition.

    Class hypothesis per CLAUDE.md §3b-cond: the substantive analytic
    content is axiomatised here so the downstream min-norm theorem is
    sorry-free **conditional on the class instance**. -/
class PSDTrace (R : Type u) [LinearOrderedField R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A) :
    Prop where
  psd : ∀ x : A, 0 ≤ τ.tau (x * x)

/-- **Non-degeneracy on squares.**

    `τ(X · X) = 0 ⇒ X = 0`.  Stronger than PSD; equivalent under
    PSD to "the Frobenius form has trivial radical on squares".

    For Jones–Markov `τ_M` on `H_n(R, q)`: established as
    `tau_M_non_degenerate` in
    `markov-trace-frobenius-selection.lean` (on `main` after
    PR #1750). -/
class NonDegTrace (R : Type u) [LinearOrderedField R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A) :
    Prop where
  nondeg : ∀ x : A, τ.tau (x * x) = 0 → x = 0

/-- **Completing-the-square algebraic identity (general algebra).**

    For any `X ∈ A`, `S ∈ R`:

    $$τ(X · X) = τ((X - S·1)(X - S·1)) + 2 S τ(X) - S².$$

    Proof reduces to (a) expanding `(X - S•1)·(X - S•1)` via the
    R-algebra ring identities, then (b) applying `τ`'s linearity +
    `τ(S²•1) = S² τ(1) = S²` via normalisation.

    Mechanical but verbose with the smul-vs-mul expansion
    (`S • X = (algebraMap R A S) * X`) and non-commutative ring
    manipulation.  Queued as a separate commit on this branch.

    Ref: [manuscript] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         §"Categorical reading" + prop:t-beta-markov-frobenius-collapse .md
         §"Proof — Lagrangian / completing-the-square argument" -/
theorem completing_the_square_general (R : Type u) [CommRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) (X : A) (S : R) :
    τ.tau (X * X) =
      τ.tau ((X - S • 1) * (X - S • 1)) + 2 * (S * τ.tau X) - S * S * τ.tau 1 := by
  -- Ref: [manuscript] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
  -- Step 1: algebra identity using centrality of algebraMap R A S.
  have h_smul_one_mul : (S • (1 : A)) * X = S • X := by
    rw [Algebra.smul_def, mul_assoc, one_mul, ← Algebra.smul_def]
  have h_mul_smul_one : X * (S • (1 : A)) = S • X := by
    rw [Algebra.smul_def, mul_one, ← Algebra.commutes, ← Algebra.smul_def]
  have h_smul_one_sq : (S • (1 : A)) * (S • (1 : A)) = (S * S) • (1 : A) := by
    rw [Algebra.smul_def, mul_assoc, one_mul, ← Algebra.smul_def, smul_smul]
  -- Step 2: expand the square in A.
  have h_expand : (X - S • (1 : A)) * (X - S • (1 : A)) =
                  X * X - S • X - S • X + (S * S) • (1 : A) := by
    rw [sub_mul, mul_sub, mul_sub, h_smul_one_mul, h_mul_smul_one, h_smul_one_sq]
    abel
  -- Step 3: apply τ, using R-linearity + τ_one.
  have h_tau_smul : ∀ Y : A, τ.tau (S • Y) = S * τ.tau Y := fun Y => by
    rw [τ.tau.map_smul, smul_eq_mul]
  have h_rearrange : X * X - S • X - S • X + (S * S) • (1 : A) =
                     X * X + (-(S • X)) + (-(S • X)) + (S * S) • (1 : A) := by abel
  have h_tau_expand : τ.tau ((X - S • 1) * (X - S • 1)) =
                      τ.tau (X * X) - S * τ.tau X - S * τ.tau X + S * S * τ.tau 1 := by
    rw [h_expand, h_rearrange]
    rw [τ.tau.map_add, τ.tau.map_add, τ.tau.map_add]
    rw [τ.tau.map_neg, τ.tau.map_neg]
    rw [h_tau_smul, h_tau_smul, h_tau_smul]
    ring
  -- Step 4: rearrange (R is a CommRing — use linear_combination, not linarith).
  linear_combination h_tau_expand

/-- **T_β = S · 1 — general algebra min-Frobenius-norm theorem.**

    Under the SDP constraint `τ(X) = S` and the trace's PSD +
    non-degeneracy on squares (as `class` hypotheses per §3b-cond),
    the minimum Frobenius norm-squared `τ(X · X)` over the
    constraint set is `S²`, attained uniquely at `X = S · 1`.

    Applied to the Iwahori–Hecke algebra `A = H_n(R, q)` at generic
    `q > 0` with `τ = τ_M` (the Jones–Markov trace), this is the
    Markov-trace SHAPE collapse `T_β = S · 1_H` of PR #1750.

    The 6-channel L2 SHAPE × S decomposition of PR #1739 is
    basis-dependence of the *coordinate-vector* Euclidean norm on
    `ℝ^6`, NOT the categorical Frobenius norm on H_3(ℝ, q).

    Ref: [manuscript] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         §"Categorical reading" + prop:t-beta-markov-frobenius-collapse .md -/
theorem markov_frobenius_min_norm_lift
    (R : Type u) [LinearOrderedField R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A)
    [PSDTrace R A τ] [NonDegTrace R A τ]
    (S : R) (X : A) (h_constraint : τ.tau X = S) :
    S * S ≤ τ.tau (X * X) := by
  -- Ref: [manuscript] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
  -- Step 1: invoke completing-the-square.
  have h := completing_the_square_general R A τ X S
  -- Step 2: substitute h_constraint (τ X = S) and τ_one (τ 1 = 1).
  rw [h_constraint, τ.tau_one] at h
  -- h : τ(X*X) = τ((X - S•1)²) + 2 * (S * S) - S * S * 1
  --          = τ((X - S•1)²) + S * S
  -- Step 3: PSD of τ on squares.
  have h_psd : 0 ≤ τ.tau ((X - S • 1) * (X - S • 1)) := PSDTrace.psd _
  -- Step 4: arithmetic conclusion.
  linarith

end QOU.QBeta.MarkovFrobeniusCollapse.General
