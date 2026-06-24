import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descended-level-zero",
  proofs: ["prf:descended-level-zero"],
  title:
    "Descended mass contribution lives at level 0 only",
  tags: [
    "descent",
    "jet-tower",
    "mass-endomorphism",
    "level-counting",
    "audit",
  ],
  lean: {
    ref: "qou:QOU.Descent.descended_level_zero",
    validation: "not_checked",
  },
  uses: ["prf:topological-mass"],
  cites: ["leitner2026"],
});
