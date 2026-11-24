import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:parity-regime-selection",
  title:
    "Parity regime selection for Q-values",
  tags: [
    "parity",
    "regime-selection",
    "sign",
    "odd-even",
    "q-value",
    "mass-number",
  ],
  lean: { ref: "qou:QOU.Confinement.parity_regime_selection",
    validation: "not_checked",
  },
  uses: [
    "prop:branching-qvalue-factorization",
    "def:spectator-normalization",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` inhabits unparameterised `ParityRegimeSelectionContext` at `A = 1`, `m_e = 0`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
