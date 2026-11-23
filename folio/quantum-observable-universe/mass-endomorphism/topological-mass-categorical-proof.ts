import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-categorical",
  title: "Categorical proof of the topological decomposition of mass",
  uses: [
    "prop:topological-mass-upper-bound",
    "lem:topological-mass-cat-descended",
    "lem:topological-mass-cat-transient",
  ],
});
