import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:kummer-identity-radial-reduction",
  title:
    "Kummer's identity for general $z$: the angle-built Bloch--Wigner function " +
    "is the dilogarithm one",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "dilogarithm",
    "bloch-wigner",
    "kummer",
  ],
  lean: {
    ref: "qou:QOU.Knot.KummerRadial.kummer",
    validation: "leanok",
  },
  uses: ["thm:ideal-tetrahedron-law-of-sines"],
  cites: ["zagier1986", "milnor1982", "neumann-zagier1985"],
});
