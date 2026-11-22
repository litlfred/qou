import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.ArchimedeanRemainderExponentialDecay

Primary conjecture: the archimedean brane-tower truncation remainder of
the β-decay Q-value decays exponentially in the truncation depth.

For a fixed free-neutron sector `K ⊂ H₃(q)` evaluated at the substrate
`q = q₀`, let `R N` be the depth-`N` truncation remainder
`R N = Q_β^(N) − Q_β^exact` (Form A or Form B,
`conj:q-beta-spectral-bridge`).  The conjecture asserts there exist
constants `C, c > 0`, depending only on the sector data, with

  |R N| ≤ C · exp(−c · N)   for all N.

This is the **open conjectural input** delegated by
`prop:categorical-chain-convergence-mechanisms` (Mechanism 1) and used
as the precision-ceiling by `prop:q-beta-categorical-precision-ladder`.
The geometric phrasing `|R N| ≤ ℏ_q^(2(N+1))/(1 − ℏ_q²)` is the same
bound with `c = −2 ln ℏ_q`, `C = ℏ_q²/(1 − ℏ_q²)`.

Archimedean specialisation to `ℝ` is justified (§7c): the statement uses
`Real.exp`, a strict ordering on the rate/prefactor, and an absolute
value — there is no generic-ring formulation of an exponential decay
bound.

§3b-tax classification: **primary** conjecture — the class takes no other
conjecture class as a hypothesis, so the derived `conjecture_graph` has it
as a root.

LaTeX label: `conj:archimedean-remainder-exponential-decay`
-/

namespace QOU.Interactions

/-- **Primary conjecture (archimedean remainder exponential decay).**

    Carrier class axiomatising the open input.  The single field encodes
    the conjecture's content in the *shape* of the claim: for the chosen
    free-neutron sector there exist a strictly positive prefactor `C` and
    a strictly positive rate `c` controlling the truncation remainder
    `remainder : ℕ → ℝ` (the map `N ↦ R_N(K)`) by `C · exp(−c · N)` at
    every depth `N`.

    This is **not** a vacuous marker: discharging it requires producing
    the two positive constants and proving the `∀ N` exponential bound on
    the actual remainder function — exactly the open spectral-tail
    estimate.  No instance is provided here, faithfully representing the
    conjecture's open state. -/
-- Ref: [jones1985] doi:10.2307/1971403   (Markov trace / brane-tower trace structure)
-- Ref: [leitner2026] conj:archimedean-remainder-exponential-decay
class ArchimedeanRemainderExponentialDecay (remainder : ℕ → ℝ) : Prop where
  /-- Exponential-decay control of the truncation remainder: there is a
      positive prefactor `C` and positive rate `c` with
      `|remainder N| ≤ C · exp(−c · N)` for every truncation depth `N`. -/
  exp_decay_bound :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ N : ℕ, |remainder N| ≤ C * Real.exp (-c * (N : ℝ))

end QOU.Interactions
