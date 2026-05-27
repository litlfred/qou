import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-transient-localisation",
  title: "Proof that transient terms localise to exceptional divisors",
  uses: ["lem:topological-mass-transient-localisation"],
});
