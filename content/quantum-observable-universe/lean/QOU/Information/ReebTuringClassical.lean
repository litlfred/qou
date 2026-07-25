import Mathlib.Tactic

/-!
# QOU.Information.ReebTuringClassical — classical (q=1) Reeb Turing-completeness

**Proposition** ([`prop:reeb-turing-completeness-classical`](../../../quantum-observable-universe/information-theory/reeb-turing-completeness-classical.md)).

The proved classical anchor for
[`conj:quantum-computational-universality`](../../../quantum-observable-universe/information-theory/quantum-computational-universality.md):
Cardona–Miranda–Peralta-Salas–Presas construct, on a closed Riemannian
3-manifold, a steady Euler / Reeb field whose first-return map simulates an
arbitrary Turing machine — so the trajectory (reachability) problem of its flow
is **undecidable**. This is a *theorem* at `q = 1`; the QOU only *conjectures*
its lift to arbitrary substrate parameter `q`.
-/

namespace QOU.Information

/-- **Classical Reeb Turing-completeness (Cardona–Miranda–Peralta-Salas–Presas).**

    There is a Reeb / steady-Euler flow on a closed 3-manifold whose first-return
    dynamics is Turing-universal; consequently its reachability predicate is
    **not decidable** — there is no total decision procedure for it. We abstract
    the geometric statement to its computational shadow: the existence of a
    predicate `halts : ℕ → Prop` (the flow's encoded halting set) that admits no
    decision function.

    This is an **external theorem** (published proof), stated here as the proved
    `q = 1` anchor of `conj:quantum-computational-universality`; the `sorry`
    cites the reference rather than re-formalising the construction. -/
-- Ref: [cardona2021] https://doi.org/10.1073/pnas.2026818118
theorem ReebTuringClassical :
    ∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true := by
  sorry

end QOU.Information
