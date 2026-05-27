import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-grading-correspondence",
  title:
    "Confinement levels coincide with KLR $\\mathbb{Z}$-grading shifts",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementGradingCorrespondence", validation: "stub" },
  uses: [
    "def:confinement-level",
    "prop:crystal-graph-realization",
  ],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "confinement",
    "klr",
    "grading",
    "filtration",
    "computational-shortcut",
  ],
});
