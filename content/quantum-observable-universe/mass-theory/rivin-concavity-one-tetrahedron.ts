import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:rivin-concavity-one-tetrahedron",
  title:
    "Rivin concavity for one ideal tetrahedron: the volume is strictly concave " +
    "on the angle simplex, although $\\Lambda$ is not concave",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "lobachevsky",
    "concavity",
    "angle-structure",
  ],
  lean: {
    ref: "qou:QOU.Knot.Rivin.strictConcaveOn_tetVolLine",
    validation: "leanok",
  },
  uses: ["thm:flat-tetrahedron-zero-volume"],
  cites: ["rivin1994", "thurston1978", "milnor1982"],
});
