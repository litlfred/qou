import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-cat-descended",
  title: "Proof that the descended term equals the base-level mass",
  uses: ["lem:topological-mass-cat-descended"],
});
