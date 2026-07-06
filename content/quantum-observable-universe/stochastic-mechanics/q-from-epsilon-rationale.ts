import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-from-epsilon",
  label: "rem:q-from-epsilon-rationale",
  title:
    "Why take $\\varepsilon$ primitive and the $q-1 \\leftrightarrow \\varepsilon$ convention",
  uses: [
    "def:q-from-epsilon",
    "def:frobenius-hopf-substrate",
    "def:classical-limit-obstruction",
  ],
  tags: [
    "substrate-parameter",
    "surreal",
    "categorical-primitive",
    "q-expansion",
    "classical-limit",
  ],
});
