import { definition } from "../../schema/builders";

export default definition({
  label: "def:vertex-operator",
  lean: { ref: "qou:QOU.VertexOperator", validation: "not_checked" },
  title: "Vertex operator on the exceptional divisor",
  tags: [
    "vertex-operator", "exceptional-divisor", "reeb-bundle",
    "state-operator-correspondence", "R-matrix",
  ],
  uses: [
    "def:reeb-bundle",
    "def:contact-affine-chart",
    "ex:projective-line-su2",
    "rem:r-matrix-braiding",
    "thm:jones-markov-trace",
  ],
  examples: ["rem:skein-decomposition"],
  cites: ["frenkel2004", "kassel1995"],
});
