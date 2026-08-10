import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ideal-tetrahedron-volume-well-defined",
  title:
    "The volume of an ideal tetrahedron does not depend on the labelling: " +
    "$D\\bigl(1/(1-z)\\bigr) = D(z)$",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "bloch-wigner",
    "well-definedness",
    "volume-functor",
  ],
  lean: {
    ref: "qou:QOU.MathlibExt.IdealTetrahedron.volume_rotate",
    validation: "leanok",
  },
  uses: ["thm:kummer-identity-radial-reduction"],
  cites: ["thurston1978", "milnor1982", "neumann-zagier1985"],
});
