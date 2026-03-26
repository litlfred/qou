import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-categorical",
  title: "Categorical proof of the topological decomposition of mass",
  uses: [
    "thm:topological-mass",
    "prop:descent-eigenspaces",
    "def:mass-identity",
    "def:frobenius-pairing",
    "def:descent-involution",
    "def:brane-boundary",
  ],
});
