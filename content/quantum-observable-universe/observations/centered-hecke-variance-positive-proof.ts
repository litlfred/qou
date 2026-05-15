import { proof } from "../../schema/builders";

export default proof({
  label: "prf:centered-hecke-variance-positive",
  title: "Proof: centred Hecke variance is strictly positive",
  uses: ["prop:centered-hecke-variance-positive"],
});
