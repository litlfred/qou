import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-casimir-exists",
  title: "Existence of the $q$-Casimir element",
  lean: { ref: "qou:QOU.QCasimir.exists",
    validation: "not_checked",
  },
  uses: ["def:q-casimir"],
  proofs: ["prf:q-casimir-exists"],
  tags: ["existence", "casimir", "quantum-group", "central-element"],
});
