import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:confinement-grading-correspondence-conditional",
  title:
    "Confinement = KLR grading shift (conditional on Brundan–Kleshchev isomorphism + crystal-graph realisation)",
  lean: {
    ref:
      "qou:QOU.BraidsAndKnots.confinement_grading_correspondence_conditional",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "conj:crystal-graph-realization",
    "conj:confinement-grading-correspondence",
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
    "conditional-theorem",
    "conditional-on-class",
    "computational-shortcut",
  ],
});
