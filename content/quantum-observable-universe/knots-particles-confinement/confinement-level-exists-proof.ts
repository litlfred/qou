import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-level-exists",
  title: "Proof of confinement level exists",
  uses: ["prop:confinement-level-exists"],
});
