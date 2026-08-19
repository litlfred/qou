import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:gluing-equations-do-not-detect-hyperbolicity",
  title:
    "The gluing equations do not detect hyperbolicity: the trefoil's flat shapes satisfy them exactly",
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
    "ideal-triangulation",
    "torus-knot",
    "degenerate",
    "negative-control",
  ],
  lean: {
    ref: "qou:QOU.Knot.FlatTet.edge_equations_do_not_detect_hyperbolicity",
    validation: "leanok",
  },
  uses: ["thm:flat-tetrahedron-zero-volume"],
  cites: ["thurston1978", "neumann-zagier1985"],
});
