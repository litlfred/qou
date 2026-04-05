import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-reeb-cocycle",
  title: "The genuine gap: stability of equidistribution under the Collatz-Reeb cocycle",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "prop:reeb-equidistribution",
    "rem:substrate-gm-torsion",
    "def:operational-entropy",
  ],
  tags: [
    "collatz",
    "reeb-flow",
    "ergodic",
    "cocycle",
    "lyapunov",
    "genuine-gap",
    "kam",
  ],
});
