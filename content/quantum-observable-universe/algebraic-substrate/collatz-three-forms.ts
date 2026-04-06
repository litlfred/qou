import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-three-forms",
  title: "Three faces of the $q$-Collatz conjecture",
  interprets: "prop:collatz-contact-boundary",
  uses: [
    "conj:q-collatz",
    "prop:collatz-contact-boundary",
    "prop:skein-generation",
    "def:reeb-bundle",
  ],
  tags: [
    "collatz",
    "hecke-algebra",
    "markov-trace",
    "gaussian-integers",
    "contact-order",
    "saturation",
  ],
});
