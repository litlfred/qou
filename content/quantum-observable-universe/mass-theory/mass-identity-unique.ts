import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-identity-unique",
  title: "Uniqueness of the inertial mass identity",
  lean: { ref: "qou:QOU.MassIdentity.unique",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-identity-exists",
    "prop:frobenius-pairing-unique",
  ],
  proofs: ["prf:mass-identity-unique"],
  tags: ["uniqueness", "mass-identity"],
});
