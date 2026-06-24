import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-level-exists",
  proofs: ["prf:confinement-level-exists"],
  title: "Existence of the confinement level",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementLevel.exists",
    validation: "not_checked",
  },
  uses: [],
  tags: ["existence", "confinement", "filtration"],
});
