import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-exists",
  title: "Existence of the aether parameter",
  lean: { ref: "qou:QOU.ArchimedeanSubstrateField.ofReebDecomposition",
    validation: "not_checked",
  },
  uses: ["def:substrate-parameter"],
  proofs: ["prf:substrate-parameter-exists"],
  tags: ["existence", "substrate", "deformation"],
});
