import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rh-surreal-bound",
  title: "A surreal heuristic for the Riemann hypothesis, and why it is not a proof",
  interprets: "conj:classical-riemann-hypothesis",
  uses: [
    "conj:classical-riemann-hypothesis",
    "conj:macroscopic-stability-equivalence",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:thm:quantum-gap-collapse",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
  ],
  cites: ["conway1976"],
  tags: ["surreal", "riemann-hypothesis", "heuristic"],
});
