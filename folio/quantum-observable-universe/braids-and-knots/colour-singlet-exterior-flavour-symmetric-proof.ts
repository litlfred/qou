import { proof } from "../../schema/builders";

export default proof({
  label: "prf:colour-singlet-exterior-flavour-symmetric",
  title: "Proof that colour-singlet q-exterior states are flavour q-symmetric",
  uses: ["prop:colour-singlet-exterior-flavour-symmetric", "prop:colour-singlet-flavour-generator"],
});
