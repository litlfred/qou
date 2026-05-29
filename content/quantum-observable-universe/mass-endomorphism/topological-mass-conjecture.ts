import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-decomposition-mass",
  title: "Conjectural Topological Decomposition of Mass",
  lean: {
    ref: "qou:QOU.TopologicalMass.TopologicalDecompositionMass",
    validation: "not_checked",
  },
  uses: ["cor:quantum-dilogarithm"],
  tags: ["mass", "topological-decomposition", "divisor", "vortex", "holonomy"],
});
