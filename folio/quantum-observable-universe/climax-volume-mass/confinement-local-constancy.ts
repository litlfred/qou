import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-local-constancy",
  title: "Local constancy of confinement level off $\\mathcal{B}$",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementLocalConstancy",
    validation: "not_checked",
  },
  uses: ["def:local-shadow-ordering", "prop:phase-boundary-variety"],
  tags: [
    "confinement-level",
    "local-constancy",
    "phase-boundary",
  ],
});
