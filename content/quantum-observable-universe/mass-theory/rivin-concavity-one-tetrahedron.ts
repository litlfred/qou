import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:rivin-concavity-one-tetrahedron",
  title:
    "Rivin concavity for one ideal tetrahedron: $\\Lambda(\\alpha)+\\Lambda(\\beta)+\\Lambda(\\gamma)$ is strictly concave along every line in the angle simplex",
  tags: [
    "hyperbolic-volume",
    "angle-structures",
    "casson-rivin",
    "lobachevsky",
    "concavity",
  ],
  lean: {
    ref: "qou:QOU.Knot.Rivin.strictConcaveOn_tetVolLine",
    validation: "leanok",
  },
  uses: ["thm:kummer-bloch-wigner-identity"],
  cites: ["thurston1978", "milnor1982"],
});
