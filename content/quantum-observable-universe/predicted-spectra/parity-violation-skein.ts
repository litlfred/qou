import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:parity-violation-skein",
  proofs: ["prf:parity-violation-skein"],
  title:
    "Parity non-conservation from the Skein relation at $q \\neq 1$",
  tags: [
    "parity",
    "weak-force",
    "skein-relation",
    "lee-yang",
    "wu-experiment",
    "mirror",
    "crossing-chirality",
    "symmetry-breaking",
  ],
  lean: { ref: "qou:QOU.Archimedean.parity_violation_skein",
    validation: "not_checked",
  },
  uses: [
    "def:beta-decay-skein",
    "prop:reidemeister-action-table",
  ],
});
