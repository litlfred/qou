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
  authorNotes: [
    {
      kind: "status",
      body: "The holonomy form of the :refterm[descent]{#descent} piece is the main gap:\n[conj:topological-mass](#thm\\:topological-mass) conjectures the :refterm[descent]{#descent}\ntrace decomposition categorically (only its upper bound is proved) but does not express it as a gauge holonomy.\nBridging these two formulations is the core proof obligation.",
    },
  ],
});
