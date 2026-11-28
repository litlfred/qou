import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-surreal-bound",
  title: "Surreal $\\omega$-order heuristic for $\\mathbf{P}$ versus $\\mathbf{NP}$, and why it cancels the problem size",
  interprets: "conj:p-vs-np-qou",
  uses: [
    "conj:p-vs-np-qou",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
    "quantum-observable-universe:rem:calculus-up-to-epsilon",
  ],
  cites: ["conway1976"],
  tags: ["P-vs-NP", "surreal", "heuristic"],
});
