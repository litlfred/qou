import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-three-forms",
  title: "Three faces of the $q$-Collatz conjecture",
  interprets: "prop:collatz-contact-boundary",
  uses: ["prop:collatz-contact-boundary"],
  tags: [
    "collatz",
    "hecke-algebra",
    "markov-trace",
    "gaussian-integers",
    "contact-order",
    "saturation",
  ],
});
