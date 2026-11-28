import { remark } from "../../schema/builders";

export default remark({
  label: "rem:yang-mills-surreal-bound",
  title: "Surreal-order relabelling of the crossing-energy gap, and why it does not prove a Yang--Mills mass gap",
  interprets: "conj:yang-mills-mass-gap",
  uses: [
    "conj:yang-mills-mass-gap",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:thm:quantum-gap-collapse",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
    "quantum-observable-universe:rem:calculus-up-to-epsilon",
  ],
  cites: ["conway1976", "jaffe2006"],
  tags: ["surreal", "yang-mills", "mass-gap", "heuristic"],
});
