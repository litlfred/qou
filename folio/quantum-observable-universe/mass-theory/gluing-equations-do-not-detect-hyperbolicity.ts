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
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-07",
      body:
        "Archimedean specialisation (\u00a77c), acknowledged: the Lean sibling " +
        "`QOU/Knot/FlatTetrahedra.lean` works over $\\mathbb{C}$ and $\\mathbb{R}$ " +
        "because its volume half is genuinely analytic \u2014 the Bloch\u2013Wigner " +
        "dilogarithm $D$, `Complex.arg`, and the tetrahedron angles are archimedean " +
        "constructs, and `BlochWigner_lob_ofReal` (a real shape has $D = 0$) is the " +
        "statement that a flat tetrahedron has zero volume. The algebraic half \u2014 " +
        "that the trefoil's rational shapes $z_0 = -1$, $z_1 = 2$ satisfy every gluing " +
        "equation \u2014 needs no ordering and is where the theorem's content lives; the " +
        "$\\mathbb{C}$ is required only to say what \u201cvolume $0$\u201d means. " +
        "This is the wall crossing the block's narrative describes (a geometric solution " +
        "needs $\\operatorname{Im} z_i > 0$), not a gratuitous $\\mathbb{R}$.",
    },
  ],
  cites: ["thurston1978", "neumann-zagier1985", "martelli2016"],
});
