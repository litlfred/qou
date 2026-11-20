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
  tags: [
    "pairing",
    "variational",
    "quadratic-action",
    "gauge-invariance",
    "zero-mode",
    "rigid-dual",
  ],
});
