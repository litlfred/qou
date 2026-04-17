import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mass-identity-exists",
  title: "Proof of well-definedness of the inertial mass identity",
  uses: ["prop:mass-identity-exists"],
});
