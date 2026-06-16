import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-counit-closed-form",
  lean: {
    ref: "qou:QOU.Interactions.QBetaEnergyScale.Qbeta_closed",
    validation: "not_checked",
  },
  title:
    "Closed form of the counit $Q$-value $\\varepsilon(\\Delta)\\cdot\\mathfrak{E}_0$",
  uses: [
    "def:typed-crossing-operator",
    "rem:energy-scale-planck",
  ],
  tags: [
    "beta-decay",
    "q-value",
    "frobenius-counit",
    "markov-trace",
    "symbolic",
    "lean-verified",
  ],
});
