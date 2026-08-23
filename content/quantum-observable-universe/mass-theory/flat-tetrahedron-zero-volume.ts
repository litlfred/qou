import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:flat-tetrahedron-zero-volume",
  title:
    "A flat ideal tetrahedron has zero volume: $D(x) = 0$ for every real $x$",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "bloch-wigner",
    "dilogarithm",
    "degenerate",
  ],
  lean: {
    ref: "qou:QOU.Knot.FlatTet.BlochWigner_lob_ofReal",
    validation: "leanok",
  },
  uses: ["prop:thurston-volume-additivity"],
  cites: ["thurston1978", "milnor1982", "zagier1986"],
});
