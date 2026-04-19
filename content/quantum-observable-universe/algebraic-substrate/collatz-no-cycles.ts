import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-no-cycles",
  lean: {
    decl: "QOU.AlgebraicSubstrate.collatz_no_cycles",
    validation: "not_checked",
  },
  title:
    "No periodic Collatz cycles: coprimality of $[2]_q$ and $[3]_q$",
  uses: [
    "conj:q-collatz",
    "prop:collatz-contact-boundary",
  ],
  tags: [
    "collatz",
    "periodic-cycle",
    "coprimality",
    "q-integer",
    "skein-divisibility",
  ],
  cites: ["collatz1937"],
});
