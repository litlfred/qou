import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-identity-exists",
  title: "Existence of the inertial mass identity",
  lean: { ref: "qou:QOU.MassIdentity.exists",
    validation: "not_checked",
  },
  uses: ["def:mass-identity"],
  proofs: ["prf:mass-identity-exists"],
  tags: ["existence", "mass-identity", "inertial-mass"],
});
