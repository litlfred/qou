import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lr-tensor-character-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.lr_tensor_character_bridge",
    validation: "not_checked",
  },
  title: "LR comultiplication bridge for Hecke characters on tensor-product braids",
  tags: ["hecke-algebra", "littlewood-richardson", "symmetric-functions",
         "markov-trace", "compute-bridge"],
  uses: [
    "rem:hecke-algebra-from-braiding",
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:wenzl-bridge-applicability-qou",
    "def:canonical-braid-interface-composition",
    "def:atomic-braid",
  ],
  cites: ["wenzl1988", "macdonald1995", "geck-pfeiffer2000", "ram1991"],
});
