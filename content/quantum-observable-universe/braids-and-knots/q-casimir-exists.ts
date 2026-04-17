import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-casimir-exists",
  title: "Existence of the $q$-Casimir element",
  lean: {
    decl: "QOU.QCasimir.exists",
    validation: "not_checked",
  },
  uses: [
    "def:q-casimir",
    "def:quantum-su2",
  ],
  proofs: ["prf:q-casimir-exists"],
  tags: ["existence", "casimir", "quantum-group", "central-element"],
});
