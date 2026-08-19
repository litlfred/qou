import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:kummer-bloch-wigner-identity",
  title:
    "Kummer's identity: $D(z) = \\mathrm{Im}\\,\\mathrm{Li}_2(z) + \\log\\lVert z\\rVert\\,\\arg(1-z)$ on the upper half plane",
  tags: [
    "dilogarithm",
    "bloch-wigner",
    "lobachevsky",
    "ideal-tetrahedron",
    "hyperbolic-volume",
  ],
  lean: {
    ref: "qou:QOU.Knot.KummerRadial.kummer",
    validation: "leanok",
  },
  uses: ["thm:flat-tetrahedron-zero-volume"],
  cites: ["milnor1982", "zagier1986"],
});
