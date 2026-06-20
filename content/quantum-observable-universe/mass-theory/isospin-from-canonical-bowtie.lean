/-!
# QOU.BraidsAndKnots.IsospinFromCanonicalBowtie — conjectural sibling stub

**Sibling-resolution stub** for content block
[`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md): *D9 isospin SU(2)_I*.

The §3b-cond class axiomatisation lives at
[`../lean/QOU/BraidsAndKnots/IsospinFromCanonicalBowtie.lean`](../lean/QOU/BraidsAndKnots/IsospinFromCanonicalBowtie.lean)
under the `qou` Lake package (file pending; class structure
sketched in the `.md` "Lean axiomatisation (sketch)" section).
The class instance is the **conjectural witness** (sorry =
conjecture per AGENTS.md §3b), not a missing proof; downstream
theorems take `[IsospinFromCanonicalBowtie]` as an explicit `[Instance]`
hypothesis.

This stub satisfies the lean-ref sibling-resolution rule
(AGENTS.md §0a step 1) for the `.ts` manifest's
`lean.ref = "qou:QOU.BraidsAndKnots.IsospinFromCanonicalBowtie"`.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/isospin-from-canonical-bowtie.ts
-/

namespace QOU.BraidsAndKnots

/-- **CONJECTURE.** Canonical $\\mathrm{SU}(2)_I$ isospin from the operator-valued $\\bowtie_K$ interface (regularised crystal extension) -/
class IsospinFromCanonicalBowtie where
  holds : Prop
  -- Ref: [manuscript] conj:isospin-from-canonical-bowtie

end QOU.BraidsAndKnots
