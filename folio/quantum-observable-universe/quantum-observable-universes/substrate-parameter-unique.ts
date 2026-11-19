import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-unique",
  title: "Uniqueness of the aether parameter",
  lean: {
    ref: "qou:QOU.SubstrateParameter.unique",
    validation: "not_checked", // Lean proof is tautological: SameQouOrigin := field equality, then unique returns h_same_qou. Narrative proof is real (3-step spectral argument) but Lean is a stub.
  },
  uses: [
    "thm:substrate-parameter-exists",
    "prop:braiding-eigenvalue-extraction",
    "prop:positive-definite-dagger",
  ],
  proofs: ["prf:substrate-parameter-unique"],
  tags: ["uniqueness", "substrate", "deformation"],
});
