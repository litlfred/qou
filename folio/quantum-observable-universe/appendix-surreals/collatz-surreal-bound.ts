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
  authorNotes: [
    { kind: "status", date: "2026-11-28", body: "Conclusion 'all orbits terminate at 1' withdrawn (2026-11-28): the scalings are asserted, not derived from C_q, and the standard-part step assumes the conclusion. Kept as an analogy." },
  ],
});
