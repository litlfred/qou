import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hyperbolic-knot-shape-fields",
  title:
    "Shape fields of hyperbolic knot triangulations, with the gluing equations verified exactly",
  computation: {
    engine: "sympy",
    script:
      "computations/probes/qbeta_route75_multiknot_gluing_symbolic_probe.py",
    witness:
      "computations/qbeta-route75-multiknot-gluing-symbolic.witness.json",
    status: "verified",
  },
  tags: [
    "hyperbolic-volume",
    "gluing-equations",
    "shape-field",
    "invariant-trace-field",
    "ideal-triangulation",
    "number-field",
  ],
  lean: {
    ref: "qou:QOU.Knot.GeneratedGluing.K61.edge_0",
    validation: "leanok",
  },
  uses: ["prop:thurston-volume-additivity"],
  cites: ["thurston1978", "neumann-zagier1985"],
});
