import QOU.Basic
import QOU.QuantumObservableUniverses.QAnalysis


/-!
# QOU.QResolvent.unique — uniqueness of the q-resolvent

The resolvent `R_q(s) = (s + Δ̂_q)⁻¹` is determined by the q-Laplacian.

LaTeX: `\label{prop:q-resolvent-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version recorded an external axiom (a bare `Subsingleton`
was noted as too strong) referencing an auto-bound `QResolvent` — the
structure was never imported, so the claim was unchecked.

This file now imports the relocated `QResolvent` structure
(`QOU.QuantumObservableUniverses.QAnalysis`) and **proves** — with no
axiom — the genuine determination: two resolvents for the *same*
q-Laplacian agree, provided that q-Laplacian is surjective (so every
spectral argument is in its image, where the inverse witness pins the
resolvent).  Surjectivity is the categorical shadow of `s + Δ̂_q`
spanning the convolution algebra; dropping it to the full
spectral-domain statement is the open refactor.

## References

- [leitner2026] §2-quantum-observable-universes/q-resolvent-unique
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.4
-/

namespace QOU

/-- **Uniqueness of the q-resolvent (proved, conditional on
    surjectivity).**

    Two `QResolvent H` instances with the same q-Laplacian `delta_q`
    have the same resolvent `R`, provided `delta_q` is surjective: on
    `delta_q x` the inverse witness gives `R (delta_q x) = x` for both.
    This replaces an unchecked external axiom with the determination
    the inverse witness genuinely provides. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
theorem QResolvent.unique {H : Type*} (R₁ R₂ : QResolvent H)
    (hd : R₁.delta_q = R₂.delta_q)
    (hsurj : Function.Surjective R₁.delta_q) :
    R₁.R = R₂.R := by
  funext y
  obtain ⟨x, rfl⟩ := hsurj y
  rw [R₁.inverse_witness x, hd, R₂.inverse_witness x]

end QOU
