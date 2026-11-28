import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-vs-np-qou",
  title: "Speculative Reeb--surreal non-compressibility formulation of $\\mathbf{P} \\neq \\mathbf{NP}$",
  lean: { ref: "qou:QOU.BringsSurface.PvsNPQou", validation: "stub" },
  uses: [
    "conj:qou-p-neq-np",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
    "quantum-observable-universe:rem:calculus-up-to-epsilon",
  ],
  cites: ["conway1976", "freedman2003"],
  tags: ["P-vs-NP", "surreal", "BQP", "millennium"],
});
