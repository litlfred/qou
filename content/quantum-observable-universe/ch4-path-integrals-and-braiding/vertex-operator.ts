import { definition } from "../../schema/builders";

export default definition({
  label: "def:vertex-operator",
  lean: { decl: "QOU.VertexOperator" },
  title: "Vertex operator on the exceptional divisor",
  tags: [
    "vertex-operator", "exceptional-divisor", "reeb-bundle",
    "state-operator-correspondence", "R-matrix",
  ],
  uses: [
    "def:reeb-bundle",
    "def:exceptional-divisor",
    "rem:r-matrix-braiding",
    "thm:jones-markov-trace",
  ],
  cites: ["frenkel2004", "kassel1995"],
});
