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
  // Note: def:ew-interface-knot and prop:interface-knot-markov-z are
  // referenced via .md cross-refs but live as unslotted orphans on
  // main (PR #819, PR #801). Cannot lift into uses[] until they are
  // slotted in chapter manifests (would trigger Unresolved-uses
  // validation error). Phase 5n preserves the .md narrative refs
  // and accepts the warning-level cross-ref notice.
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
