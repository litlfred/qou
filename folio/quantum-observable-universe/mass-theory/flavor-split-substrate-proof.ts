import { proof } from "../../schema/builders";

export default proof({
  label: "prf:flavor-split-aether",
  renamedFrom: ["prf:flavor-split-substrate"],
  title: "Proof of the aether-pure flavor split formula",
  uses: ["prop:flavor-split-aether", "lem:pair-skein-mass-formula"],
});
