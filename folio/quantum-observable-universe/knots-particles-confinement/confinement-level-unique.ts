import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-level-unique",
  title: "Uniqueness of the confinement level",
  lean: { ref: "qou:QOU.BraidsAndKnots.ConfinementLevel.unique",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-level-exists",
    "def:local-shadow-ordering",
  ],
  tags: ["uniqueness", "confinement", "filtration"],
});
