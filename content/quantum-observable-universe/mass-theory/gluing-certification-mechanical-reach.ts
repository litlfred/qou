import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:gluing-certification-mechanical-reach",
  title:
    "The exact gluing verification is mechanical to degree 14 and 14 tetrahedra: neither predicted ceiling exists",
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
    "cusp-equations",
    "ideal-triangulation",
    "shape-field",
    "codegen",
    "certificates",
  ],
  lean: {
    ref: "qou:QOU.Knot.GeneratedCertifiedHigh.Cert10100.satisfiesEdgeEquations",
    validation: "leanok",
  },
  uses: ["thm:gluing-equations-do-not-detect-hyperbolicity"],
  cites: ["thurston1978", "neumann-zagier1985"],
});
