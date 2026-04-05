import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-collatz-interpretation",
  title: "The Collatz obstruction as the fifth evaluation of $\\chi(A)$",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "thm:qou-obstruction-reduction",
    "def:skein-resolution-obstruction",
    "def:operational-entropy",
    "prop:p-bandwidth-bound",
    "def:local-q-zeta-function",
    "conj:classical-riemann-hypothesis",
    "rem:reeb-flow-bridge",
    "prop:root-of-unity-truncation",
    "thm:tannaka-krein-isomorphism",
  ],
  tags: [
    "collatz",
    "obstruction",
    "five-evaluations",
    "information-theory",
    "operational-entropy",
    "reeb-flow",
    "q-zeta",
    "kummer",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
