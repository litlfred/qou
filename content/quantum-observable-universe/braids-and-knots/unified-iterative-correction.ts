import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unified-iterative-correction",
  title:
    "Unified iterative LP-dual correction: per-step Wedderburn " +
    "projection over all partitions $\\lambda \\vdash k$ for " +
    "$k = 2, \\ldots, K$, starting at $A = 1$ (no special cases)",
  lean: { ref: "qou:QOU.Descartes.ConfinedKnotBinding.Unified.unified_iterative_correction",
    validation: "not_checked",
  },
  uses: [
    "prop:wigner-np-pairing",
    "prop:bw-coefficient-shadow-price",
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
