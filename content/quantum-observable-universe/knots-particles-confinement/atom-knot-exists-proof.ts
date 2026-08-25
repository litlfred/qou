import { proof } from "../../schema/builders";

export default proof({
  label: "prf:atom-knot-exists",
  title: "Proof of atom knot exists",
  uses: ["prop:atom-knot-exists"],
});
