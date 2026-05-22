import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-resums-trace-series",
  title:
    "$\\Phi_q$ resums an infinite series of Markov traces",
  interprets: "prop:mass-tower-operator-valued",
  uses: [
    "prop:mass-tower-operator-valued",
    "thm:topological-mass",
    "thm:six-term-mass-formula-complete",
  ],
  tags: ["mass-tower", "markov-trace", "audit", "exposition"],
});
