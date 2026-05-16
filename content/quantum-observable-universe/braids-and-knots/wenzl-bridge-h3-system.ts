import { remark } from "../../schema/builders";

export default remark({
  label: "rem:wenzl-bridge-h3-system",
  title:
    "Wenzl-bridge $y_\\lambda$ system for $H_3(q)$ as an explicit 3×3 linear-algebra problem in Lean (2 mechanical sorries on det-nonvanishing + Cramer-rule existence)",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: [
    "prop:markov-trace-frobenius-selection",
    "rem:markov-axioms-primitive",
  ],
  cites: ["wenzl1988", "jones1985"],
  tags: [
    "lean-infrastructure",
    "wenzl-bridge",
    "linear-algebra",
    "H_3",
    "cramer-rule",
    "open-formalisation",
  ],
});
