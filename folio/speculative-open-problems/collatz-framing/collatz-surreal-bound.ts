import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-surreal-bound",
  title: "Surreal $\\omega$-order analogy for Collatz, with its orbit-termination conclusion withdrawn",
  interprets: "conj:q-collatz",
  uses: [
    "sec:collatz-intro",
    "conj:q-collatz",
    "quantum-observable-universe:prop:balanced-holonomy-exclusion",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
    "quantum-observable-universe:rem:calculus-up-to-epsilon",
  ],
  cites: ["conway1976", "lagarias2010"],
  tags: ["collatz", "surreal", "heuristic", "withdrawn"],
});
