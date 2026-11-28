import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-open-problems",
  title: "Open problems separating Hecke-algebra algebraics from P versus NP",
  interprets: "conj:qou-p-neq-np",
  tags: ["P-vs-NP", "open-problems", "cellular-automata", "outer-automorphism", "intent"],
  uses: [
    "sec:p-vs-np-boundary-intro",
    "conj:qou-p-neq-np",
    "quantum-observable-universe:prop:block-rigidity",
    "quantum-observable-universe:prop:bounded-width-trace-cost",
    "quantum-observable-universe:prop:jvw-tractable-orders",
    "quantum-observable-universe:def:observation",
    "quantum-observable-universe:prop:q-game-of-life",
    "quantum-observable-universe:prop:reeb-turing-completeness-classical",
  ],
  cites: [
    "jaeger1990",
    "bakergillsolovay1975",
    "razborovrudich1997",
    "aaronsonwigderson2009",
    "geckpfeiffer2000",
  ],
});
