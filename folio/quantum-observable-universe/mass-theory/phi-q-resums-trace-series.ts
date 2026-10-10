import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-resums-trace-series",
  interprets: "thm:six-term-mass-formula-complete",
  title:
    "$\\Phi_q$ resums an infinite series of Markov traces",
  uses: [
    "thm:six-term-mass-formula-complete",
    "prop:phi-q-aj-machinery-identification",
  ],
  tags: ["mass-tower", "markov-trace", "audit", "exposition"],
});
