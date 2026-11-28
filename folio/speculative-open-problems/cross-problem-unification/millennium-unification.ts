import { remark } from "../../schema/builders";

export default remark({
  label: "rem:millennium-unification",
  title: "Cross-problem surreal comparison table, and why the Navier--Stokes row and cross-problem link fail to unify",
  interprets: "conj:yang-mills-mass-gap",
  uses: [
    "rem:rh-surreal-bound",
    "rem:collatz-surreal-bound",
    "rem:p-vs-np-surreal-bound",
    "rem:bsd-surreal-bound",
    "rem:yang-mills-surreal-bound",
    "conj:classical-riemann-hypothesis",
    "conj:q-collatz",
    "conj:p-vs-np-qou",
    "conj:q-birch-swinnerton-dyer",
    "conj:yang-mills-mass-gap",
    "quantum-observable-universe:rem:ns-surreal-bound",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:rem:conway-normal-form",
  ],
  cites: ["conway1976"],
  tags: ["surreal", "millennium-problem", "comparison-table"],
});
