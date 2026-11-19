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
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      body: "The holonomy form of the :refterm[descent]{#descent} piece is the main gap:\n[thm:topological-mass](#thm\\:topological-mass) identifies the :refterm[descent]{#descent}\ntrace categorically but does not express it as a gauge holonomy.\nBridging these two formulations is the core proof obligation.",
    },
  ],
});
