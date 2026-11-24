/-!
# QOU.AppendixSurreals.WenzlPositivityImpliesSubstratePositivity

**Sibling-resolution stub** for content block
[`conj:wenzl-positivity-implies-substrate-positivity`](wenzl-positivity-implies-substrate-positivity.md):
*Wenzl positivity at q_0 implies substrate C*-Frobenius positivity*.

The §3b-cond class axiomatisation lives here. The class instance is
the **conjectural witness** (sorry = conjecture per AGENTS.md §3b),
not a missing proof. The class bridges the downstream
`OSReflectionPositivity` typeclass and a future
`WenzlPositivityAt(q_0)` typeclass on the upstream side — granting
this instance, OS reflection positivity reduces to Wenzl's classical
positivity theorem for Rep(U_q(sl_2)) at q_0 ∈ R_{>1}.

## Carrier fix, 2026-09-12 (`prop-universe-field`)

The field was typed bare `: Prop` — **the universe of propositions, not a
proposition** — so an instance supplied a *proposition* rather than a *proof*
of one, `instance := ⟨True⟩` type-checked and discharged the class, and every
`[WenzlPositivityImpliesSubstratePositivity]`-conditional result downstream
would have been conditional on nothing. Recorded as a `genuine` verdict in
`docs/audits/lean-vacuity-review-ledger.json`; the defect is type-level, not a
judgement about intent, and it is proved outright in
`QOU.ProofHygiene.SelfAssumingContexts`
(`conditional_on_propUniverse_is_unconditional`).

The class now takes the two propositions as **parameters** and carries the
**implication** between them. That is the §3b-cond shape, which the same file
proves is *not* contentless (`conditional_not_contentless`): an instance is
inhabited iff the implication holds, which is strictly weaker than the
conclusion, and `⟨True⟩` no longer type-checks.

**The conjecture is untouched and still open** — no instance is supplied here,
and nothing about what Wenzl positivity or substrate positivity *are* has been
decided. The change is that assuming it now costs a proof of an implication
instead of costing nothing. There were zero consumers of the class, so nothing
downstream moves.

-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/wenzl-positivity-implies-substrate-positivity.ts
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988)
-/

namespace QOU.AppendixSurreals

/-- **CONJECTURE.** Wenzl positivity of Rep(U_q(sl_2)) at q = q_0
    ∈ R_{>1} implies the substrate C*-Frobenius positivity axiom
    needed by `OSReflectionPositivity`.

    The two propositions are **parameters**, not constructions: neither
    `WenzlPositivityAt(q_0)` nor the substrate positivity axiom is
    formalised yet (the docstring above calls the upstream one
    "future"), and parameterising is what lets this carrier state the
    bridge without pre-empting either. -/
class WenzlPositivityImpliesSubstratePositivity
    (WenzlPositiveAtQ0 SubstrateFrobeniusPositive : Prop) : Prop where
  /-- The bridge claim: Wenzl-positivity of Rep(U_q(sl_2)) at q_0
      ∈ R_{>1} implies substrate C*-Frobenius positivity (Müger /
      BKLR sense) of the QOU Frobenius–Hopf substrate. The class
      instance is the §3b-cond conjectural witness. -/
  -- Ref: [leitner2026] conj:wenzl-positivity-implies-substrate-positivity
  holds : WenzlPositiveAtQ0 → SubstrateFrobeniusPositive

end QOU.AppendixSurreals
