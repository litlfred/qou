import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:aether-parameter-exists",
  renamedFrom: ["thm:substrate-parameter-exists"],
  title: "Existence of the aether parameter",
  lean: { ref: "qou:QOU.ArchimedeanSubstrateField.ofReebDecomposition",
    validation: "not_checked",
  },
  uses: ["def:aether-parameter"],
  proofs: ["prf:aether-parameter-exists"],
  tags: ["existence", "substrate", "deformation"],
});
