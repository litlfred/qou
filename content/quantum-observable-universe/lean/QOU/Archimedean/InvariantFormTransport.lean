/-
# Transport of invariant forms along an intertwiner — Option B premise (i), made precise

Epic `qou-6ufi` continuation (the α_EM B2 τ-identification;
`docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md`,
consolidation `docs/audits/2026-07-25-alpha-em-b2-tau-id-consolidation.md`).
After `SchurInvariantFormProportional` (the Option-B core) the open sub-pieces
are (i) the S₅-equivariance of the τ-image on `std` and (ii) the scalar `c`.
This file pins the *shape* of premise (i) and the *gauge behaviour* of `c`,
sorry-free:

* `invariantForm_transport` — invariance of a form transports along an
  intertwiner: if `ρ' = T⁻¹ ρ T` and `M` is `ρ`-invariant, then `Tᵀ M T` is
  `ρ'`-invariant. So premise (i) is *exactly* the existence of an intertwiner
  `T` between the Hecke-side model (seminormal, carrying the Markov Gram) and
  the period-side model (carrying the Hodge Gram): no further hypothesis is
  hidden.
* `transported_proportional_of_commutantScalar` — the composite: given the
  intertwiner (premise (i)) and the scalar commutant (Schur, concrete at the
  actual block per the `alpha-em-b2-tau-id-c-pin` witness), the transported
  Markov Gram is a scalar multiple of the Hodge Gram. This is the full
  Option-B reduction as one statement, with premise (i) an explicit
  hypothesis — never discharged here.
* `invariantForm_transport_smul` — the gauge covariance of the scalar:
  rescaling the intertwiner `T ↦ μ • T` (Schur says `T` is unique only up to
  such a scalar) rescales the transported Gram by `μ²`. Hence the Schur scalar
  `c` is well-defined only modulo `μ²`.
* `transported_smul_sign_invariant` (over `ℝ`) — but `μ² > 0` for `μ ≠ 0`, so
  the **sign** of `c` is transport-independent: "is `c > 0`?" is a well-posed,
  frame-independent question. This is why the Option-C probe declined to
  report an entrywise ratio as `c` (frame-dependent) while its positivity
  bonus (Markov Gram positive at `q₀`) + the Hodge form's positivity make the
  sign check `c > 0` the honest frame-free consistency test.

STRICT (§"Axiomatization is NOT a Proof", 2026-07-19 ruling): the intertwiner
`T` — premise (i), the τ-identification's functorial content — is a *named
hypothesis* in every statement here, never constructed, never instantiated
for the physical weights. No `TauRhoHodgeLift` instance is registered.
`1/(8π)` stays a phase-4 identification; nothing is wired.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-/
import QOU.Archimedean.SchurInvariantFormProportional
import Mathlib.Tactic.NoncommRing
import Mathlib.Data.Real.Basic

namespace QOU.Archimedean.InvariantFormTransport

open Matrix
open QOU.Archimedean.SchurInvariantFormProportional

variable {n : Type*} [Fintype n] [DecidableEq n] {k : Type*} [Field k]
variable {G : Type*}

/-- **Invariance transports along an intertwiner.** If `ρ' s = T⁻¹ * ρ s * T`
(`T` an equivalence of models of the representation) and `M` is `ρ`-invariant,
then the transported form `Tᵀ * M * T` is `ρ'`-invariant. Premise (i) of the
Option-B reduction is exactly the existence of such a `T` between the
Hecke-side and period-side models of `std`. -/
theorem invariantForm_transport {ρ ρ' : G → Matrix n n k} {T : Matrix n n k}
    (hT : IsUnit T.det) (hconj : ∀ s, ρ' s = T⁻¹ * ρ s * T)
    {M : Matrix n n k} (h : InvariantForm ρ M) :
    InvariantForm ρ' (Tᵀ * M * T) := by
  intro s
  have hTT : IsUnit (Tᵀ).det := by rw [Matrix.det_transpose]; exact hT
  rw [hconj s]
  simp only [Matrix.transpose_mul, Matrix.transpose_nonsing_inv, Matrix.mul_assoc,
    Matrix.nonsing_inv_mul_cancel_left _ _ hTT, Matrix.mul_nonsing_inv_cancel_left _ _ hT]
  have hs' : (ρ s)ᵀ * (M * ((ρ s) * T)) = M * T := by
    calc (ρ s)ᵀ * (M * ((ρ s) * T)) = ((ρ s)ᵀ * M * (ρ s)) * T := by
          simp only [Matrix.mul_assoc]
      _ = M * T := by rw [h s]
  rw [hs']

/-- **The Option-B reduction, composite form.** Given (i) an intertwiner `T`
between the `ρ`-model (carrying the invariant form `M`, e.g. the Markov Gram)
and the `ρ'`-model (carrying the unit invariant form `G₁`, e.g. the Hodge
Gram), and the scalar-commutant hypothesis on `ρ'` (Schur; concrete at the
actual α_EM block per the `alpha-em-b2-tau-id-c-pin` witness), the transported
form is proportional to `G₁`. Premise (i) is the hypothesis `hconj` — stated,
not discharged: it is the open τ-identification content. -/
theorem transported_proportional_of_commutantScalar
    {ρ ρ' : G → Matrix n n k} {T : Matrix n n k}
    (hρ' : ∀ s, IsUnit (ρ' s).det)
    (schur : ∀ A : Matrix n n k, (∀ s, A * (ρ' s) = (ρ' s) * A) →
      ∃ c : k, A = c • (1 : Matrix n n k))
    {G₁ M : Matrix n n k} (hG₁ : IsUnit G₁.det)
    (h₁ : InvariantForm ρ' G₁)
    (hT : IsUnit T.det) (hconj : ∀ s, ρ' s = T⁻¹ * ρ s * T)
    (h : InvariantForm ρ M) :
    ∃ c : k, Tᵀ * M * T = c • G₁ :=
  invariantForm_proportional_of_commutantScalar hρ' schur hG₁ h₁
    (invariantForm_transport hT hconj h)

omit [DecidableEq n] in
/-- **Gauge covariance of the transported form.** Schur fixes the intertwiner
only up to a scalar `μ`; rescaling `T ↦ μ • T` rescales the transported form
by `μ²`. Hence the Schur scalar `c` of the proportionality is well-defined
only modulo squares of the intertwiner gauge. -/
theorem invariantForm_transport_smul (μ : k) (T M : Matrix n n k) :
    (μ • T)ᵀ * M * (μ • T) = (μ ^ 2) • (Tᵀ * M * T) := by
  rw [Matrix.transpose_smul]
  rw [Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul, sq]

/-- **The sign of `c` is gauge-invariant (over `ℝ`).** For a real intertwiner
gauge `μ ≠ 0`, the rescaling factor `μ²` is positive — so whether the
transported Markov Gram is a *positive* multiple of the Hodge Gram is a
frame-independent question. This is the honest frame-free consistency test
the Option-C probe pointed at (Markov Gram positive at `q₀`, Hodge form
positive ⟹ the identification requires `c > 0`), without reporting any
frame-dependent ratio as `c`. -/
theorem transported_smul_sign_invariant {μ : ℝ} (hμ : μ ≠ 0) :
    0 < μ ^ 2 :=
  lt_of_le_of_ne (sq_nonneg μ) (Ne.symm (pow_ne_zero 2 hμ))

end QOU.Archimedean.InvariantFormTransport
