import { remark } from "../../schema/builders";

export default remark({
  label: "rem:finiteness-bound-interpretation",
  title:
    "Physical interpretation of $[A\\!-\\!1]_q! > [2]_q^{A-1}$",
  tags: [
    "finiteness",
    "interpretation",
    "pauli-exclusion",
    "nuclear-chart",
    "drip-line",
    "shell-model",
  ],
  interprets: "prop:skein-finiteness-bound",
  uses: ["prop:skein-finiteness-bound"],
});
