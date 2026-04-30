import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-decomposition-mass",
  title: "Conjectural Topological Decomposition of Mass",
  uses: [
    "def:mass-identity",
    "def:brane-boundary",
    "thm:topological-mass",
    "cor:quantum-dilogarithm",
    "def:recursive-brane-tower",
  ],
  tags: ["mass", "topological-decomposition", "divisor", "vortex", "holonomy"],
});
