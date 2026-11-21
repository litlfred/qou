import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pairing-gauge-fluctuation-massless",
  title:
    "Pure-gauge fluctuations of a pairing are zero modes of the contraction action",
  lean: {
    ref: "qou:QOU.Variational.coevaluation_contractionAction_massless",
    validation: "not_checked",
  },
  uses: [
    "def:frobenius-pairing",
    "def:rigid-monoidal-category",
  ],
  cites: [],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "The braided paragraph (the Frobenius handedness) is " +
        "`QOU.Variational.nondegenerate_braided_massless` and " +
        "`QOU.Variational.braided_contractionAction_massless` in the same " +
        "Lean file as the `lean.ref`; the general invariance criterion is " +
        "`QOU.Variational.QuadraticAction.isInvariantAlong_iff`.",
    },
  ],
  tags: [
    "pairing",
    "variational",
    "quadratic-action",
    "gauge-invariance",
    "zero-mode",
    "rigid-dual",
  ],
});
