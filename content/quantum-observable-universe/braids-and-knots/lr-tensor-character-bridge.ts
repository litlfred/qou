import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lr-tensor-character-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.lr_tensor_character_bridge",
    validation: "not_checked",
  },
  title: "LR comultiplication bridge for tensor-product braids (trivial-interface specialisation)",
  tags: ["hecke-algebra", "littlewood-richardson", "symmetric-functions",
         "markov-trace", "compute-bridge"],
  // Note: prop:interface-knot-markov-z and def:ew-interface-knot are
  // currently unslotted orphans on main with their own large unresolved
  // conjecture cascade; .md narrative cites them via [...](#label) which
  // produces warning-level (not error) unresolved cross-refs. Lifting
  // them into uses[] requires the upstream slotting work to complete.
  uses: [
    "prop:hecke-branching-trace-decomposition",
    "rem:hecke-algebra-from-braiding",
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:wenzl-bridge-applicability-qou",
    "def:canonical-braid-interface-composition",
    "def:atomic-braid",
  ],
  cites: ["wenzl1988", "macdonald1995", "geck-pfeiffer2000", "ram1991"],
});
