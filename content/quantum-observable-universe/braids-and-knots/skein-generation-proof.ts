import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-generation",
  title: "Proof of Skein generation",
  uses: ["prop:skein-generation", "lem:skein-mass-from-linking"],
});
