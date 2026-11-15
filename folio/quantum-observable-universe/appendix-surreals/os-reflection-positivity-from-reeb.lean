/-!
# QOU.AppendixSurreals.OSReflectionPositivity — conjectural sibling stub

**Sibling-resolution stub** for content block
[`conj:os-reflection-positivity-from-reeb`](os-reflection-positivity-from-reeb.md):
*Osterwalder–Schrader reflection positivity from the Reeb ℤ/2*.

The §3b-cond class axiomatisation lives here. The class instance is the
**conjectural witness** (sorry = conjecture per AGENTS.md §3b), not a
missing proof. Downstream theorems combining this class with the
surreal mass-gap bound (`rem:yang-mills-surreal-bound`) take
`[OSReflectionPositivity]` as an explicit `[Instance]` hypothesis to
conclude the OS / Wightman reconstruction of the standard part on
ℝ⁴.

-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/os-reflection-positivity-from-reeb.ts
-- Ref: [osterwalder1973] Osterwalder–Schrader, "Axioms for Euclidean Green's functions I," Commun. Math. Phys. 31 (1973)
-- Ref: [osterwalder1975] Osterwalder–Schrader, "Axioms for Euclidean Green's functions II," Commun. Math. Phys. 42 (1975)
-/

namespace QOU.AppendixSurreals

/-- **CONJECTURE.** The Frobenius pairing is positive-definite under
    the antipodal ℤ/2 ⊂ U(1)_ξ subgroup of the Reeb U(1) — i.e. the
    pairing ⟨θ(φ), φ⟩_F is non-negative for every state φ supported
    on the positive-time Reeb half.

    The proposition is a **parameter**: the Frobenius pairing, the Reeb
    `U(1)` and the antipode `θ` are not formalised in this file's import
    cone, so the statement cannot yet be written *about* them.
    Parameterising is what lets the carrier hold the conjecture honestly
    without fabricating it.

    **Fixed 2026-09-12 (`prop-universe-field`).** The field was typed bare
    `: Prop` — the *universe* of propositions, not a proposition — so an
    instance supplied a proposition rather than a proof of one, and
    `instance := ⟨True⟩` discharged the class. A carrier in that state
    cannot serve as a §3b conjectural witness either: it asserts nothing
    *even as a conjecture*, so a `[OSReflectionPositivity]`-conditional
    downstream theorem was conditional on nothing. Proved for the shape in
    `QOU.ProofHygiene.SelfAssumingContexts.propUniverse_inhabited`;
    demonstrated for named carriers in
    `docs/audits/2026-08-23-free-prop-field-triviality-probe.lean`.

    The conjecture itself is untouched and still open — no instance is
    supplied, and being contentless *for its own conjecture* is the correct
    semantics for a conjecture carrier (§3b). What changed is that assuming
    it now costs a proof of the parameter instead of costing nothing. -/
class OSReflectionPositivity (ReflectionPositive : Prop) : Prop where
  /-- The categorical reflection-positivity statement. The concrete
      content is: for every state φ ∈ A in the positive-time Reeb
      half, the antipode-twisted Frobenius pairing
      ⟨θ(φ), φ⟩_F is non-negative in End_C(𝟙). The class instance
      is the §3b-cond conjectural witness. -/
  -- Ref: [leitner2026] conj:os-reflection-positivity-from-reeb
  holds : ReflectionPositive

end QOU.AppendixSurreals
