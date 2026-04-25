import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-surreal-bound",
  title:
    "Surreal bound for Collatz: contact-boundary deviation costs transfinite Reeb period",
  interprets: "conj:q-collatz",
  uses: [
    "prop:collatz-no-cycles",
    "lem:surreal-squeeze",
  ],
  tags: [
    "collatz",
    "millennium-problem",
    "surreal",
    "squeeze",
    "contact-boundary",
    "hailstone",
    "classical-limit",
  ],
  cites: ["conway1976", "lagarias2010"],
});
