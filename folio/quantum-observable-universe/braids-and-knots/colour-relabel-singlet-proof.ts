import { proof } from "../../schema/builders";

export default proof({
  label: "prf:colour-relabel-singlet",
  title: "Proof that a colour swap fixes the singlet line only at q squared equal to one",
  uses: ["prop:colour-relabel-singlet"],
});
