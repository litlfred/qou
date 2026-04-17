import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unified-iterative-correction",
  title:
    "Unified iterative $(2,2)$ correction: per-step Wedderburn projection " +
    "replaces $D$ binding, knot factor, and Wigner energy",
  lean: {
    decl:
      "QOU.Descartes.ConfinedKnotBinding.Unified.unified_iterative_correction",
    validation: "not_checked",
  },
  uses: [
    "prop:wigner-np-pairing",
    "prop:confined-knot-binding",
    "prop:hook-weight-derivation",
    "prop:wedderburn-trace-identity",
    "prop:mass-endomorphism-tower",
    "prop:nuclear-knot-classification",
  ],
  cites: [
    "kerov1996",
    "feray-meliot2012",
    "satula1997",
  ],
  tags: [
    "wigner-energy",
    "iterative-correction",
    "partition-22",
    "q-hook-walk",
    "binding",
    "restartable-witness",
  ],
});
