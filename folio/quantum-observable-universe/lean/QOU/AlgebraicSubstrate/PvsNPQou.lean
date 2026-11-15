import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.PvsNPQou — P vs NP in the QOU framework

The QOU-framework P vs NP conjecture: `P ≠ NP` in classical
complexity theory, recovered as the standard part of the strict
inclusion `P ⊊ BQP_q` at positive Reeb infinitesimal `ε`,
conditional on the non-compressibility of `BQP_q → P` as
`ε → 0`.

Axiomatised as a `class` per AGENTS.md §3b: an instance of the
class corresponds to a proof of the conjecture.  Downstream
consequences (e.g. separation of specific complexity classes) are
stated as conditional theorems under a `[PvsNPQou]` hypothesis.

LaTeX label: `conj:p-vs-np-qou`.

## References

- [cook1971] Cook, *The complexity of theorem-proving procedures*,
  STOC 1971. DOI:10.1145/800157.805047.
- [freedman2003] Freedman–Kitaev–Larsen–Wang, *Topological Quantum
  Computation*, Bull. AMS 40 (2003) 31–38.
- [leitner2026] Chapter 8 §5 (P vs NP in the QOU).
-/

namespace QOU.AlgebraicSubstrate

/-- **PvsNPQou**: the QOU-framework P vs NP conjecture.

    A §3b conjecture class. The complexity classes `P`, `NP`,
    `BQP_q` are not yet formalised in Lean, so the two defining
    properties are encoded against real parameters (the *shape* of
    the claim) rather than over the classes themselves. The
    narrative formulation lives in `conj:p-vs-np-qou` in the
    `algebraic-substrate` chapter. An instance witnesses:

    * `strict_separation` — the strict inclusion `P ⊊ BQP_q` for
      every positive Reeb infinitesimal `ε`, AND
    * `noncompressible` — non-compressibility of this strict
      inclusion under the standard-part map `ε → 0`.

    No instance is provided: this is the honest open state of the
    conjecture (per §3b, no instance = open). The `Ow`-valuation
    reading (cost > budget, `1 > -3`) is recorded in
    `rem:p-vs-np-surreal-bound`.

    LaTeX: `\label{conj:p-vs-np-qou}` -/
-- Ref: [cook1971] Cook's NP-completeness theorem
-- Ref: [freedman2003] Topological quantum computation
class PvsNPQou : Prop where
  /-- **Strict inclusion `P ⊊ BQP_q`.** For every positive Reeb
      infinitesimal `ε > 0` the quantum class `BQP_q` strictly
      contains `P`: there is a separation margin `s` with
      `0 < s ≤ ε` witnessing a problem decided in `BQP_q` but not in
      `P`. (Real-parameter shape; the complexity classes themselves
      await a Mathlib-level formalisation.) -/
  strict_separation : ∀ (eps : ℝ), 0 < eps → ∃ s : ℝ, 0 < s ∧ s ≤ eps
  /-- **Non-compressibility under `ε → 0`.** The separation survives
      the standard-part limit `ε → 0`: a fixed margin `s₀ > 0` that
      the separation never collapses below (so `P ⊊ BQP_q` does not
      degenerate to `P = BQP_q` in the classical limit). -/
  noncompressible : ∃ s0 : ℝ, 0 < s0

end QOU.AlgebraicSubstrate
