import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-unique",
  title: "Uniqueness of the substrate parameter",
  lean: {
    ref: "qou:QOU.SubstrateParameter.unique",
    validation: "not_checked",
  },
  uses: [
    "thm:substrate-parameter-exists",
    "prop:braiding-eigenvalue-extraction",
    "prop:positive-definite-dagger",
  ],
  proofs: ["prf:substrate-parameter-unique"],
  tags: ["uniqueness", "substrate", "deformation"],
});
