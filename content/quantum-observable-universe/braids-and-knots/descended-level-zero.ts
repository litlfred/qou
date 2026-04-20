import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descended-level-zero",
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
    decl: "QOU.Descent.descended_level_zero",
    validation: "not_checked",
  },
  uses: [
    "def:descent-involution",
    "prop:descent-eigenspaces",
    "prf:topological-mass",
    "prop:mass-endomorphism-tower",
    "rem:mass-endomorphism-jet-tower",
    "def:recursive-brane-tower",
  ],
  cites: ["leitner2026"],
});
