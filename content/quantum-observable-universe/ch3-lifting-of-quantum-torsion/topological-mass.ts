import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:topological-mass",
  title: "Topological Decomposition of Mass",
  tags: ["mass", "topological-decomposition", "descent-involution"],
  lean: {
    decl: "QOU.Torsion.mass_decomposition_categorical",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:mass-identity",
    "def:descent-involution",
    "def:brane-boundary",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-categorical", "prf:topological-mass"],});
