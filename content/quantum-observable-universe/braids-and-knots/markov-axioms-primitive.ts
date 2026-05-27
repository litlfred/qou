import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-axioms-primitive",
  title:
    "Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988) in Lean; discharges the `MarkovDisjointStabilisation` class for `prop:categorical-chain-convergence-mechanisms`",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: [
    "prop:markov-trace-frobenius-selection",
    "prop:categorical-chain-convergence-mechanisms",
  ],
  cites: ["jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "markov-axioms",
    "primitive-axiomatisation",
    "class-discharge",
    "convergence-mechanism",
  ],
});
