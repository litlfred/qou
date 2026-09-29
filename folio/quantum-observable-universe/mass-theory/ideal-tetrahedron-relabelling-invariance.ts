import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ideal-tetrahedron-relabelling-invariance",
  title:
    "Relabelling invariance: $z \\mapsto 1/(1-z)$ cycles the dihedral angles and preserves volume",
  tags: [
    "ideal-tetrahedron",
    "hyperbolic-volume",
    "shape-parameter",
    "law-of-sines",
  ],
  lean: {
    ref: "qou:QOU.MathlibExt.IdealTetrahedron.volume_rotate",
    validation: "leanok",
  },
  uses: ["thm:kummer-bloch-wigner-identity"],
  cites: ["thurston1978", "neumann-zagier1985"],
});
