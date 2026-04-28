import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-exists",
  title: "Existence of the substrate parameter",
  lean: { ref: "qou:QOU.SubstrateParameter.ofReebDecomposition",
    validation: "not_checked",
  },
  uses: ["def:substrate-parameter"],
  proofs: ["prf:substrate-parameter-exists"],
  tags: ["existence", "substrate", "deformation"],
});
