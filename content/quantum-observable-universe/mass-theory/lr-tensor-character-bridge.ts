import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:lr-tensor-character-bridge",
  proofs: ["prf:lr-tensor-character-bridge"],
  lean: {
    ref: "qou:QOU.BraidsAndKnots.lr_tensor_character_bridge",
    validation: "not_checked",
  },
  title:
    "LR comultiplication bridge for tensor-product braids (trivial-interface, k-factor specialisation)",
  tags: ["hecke-algebra", "littlewood-richardson", "symmetric-functions",
         "markov-trace", "compute-bridge", "atomic-physics-specialisation"],
  uses: [
    "prop:hecke-branching-trace-decomposition",
    "prop:wenzl-bridge-applicability-qou",
    "def:canonical-braid-interface-composition",
  ],
  cites: ["wenzl1988", "macdonald1995", "geck-pfeiffer2000", "ram1991"],
});
