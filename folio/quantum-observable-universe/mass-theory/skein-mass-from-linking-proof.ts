import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-mass-from-linking",
  title: "Proof of the Skein-resolution mass formula",
  uses: ["lem:skein-mass-from-linking"],
});
