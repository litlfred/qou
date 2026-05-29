import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-decomposition-mass",
  title: "Conjectural Topological Decomposition of Mass",
  lean: {
    ref: "qou:QOU.TopologicalMass.TopologicalDecompositionMass",
    validation: "not_checked",
  },
  uses: [
    "def:mass-identity",
    "def:brane-boundary",
    "thm:topological-mass",
    "cor:quantum-dilogarithm",
    "def:recursive-brane-tower",
  ],
  tags: ["mass", "topological-decomposition", "divisor", "vortex", "holonomy"],
});
