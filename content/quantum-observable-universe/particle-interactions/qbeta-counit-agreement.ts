import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qbeta-counit-agreement",
  interprets: "prop:qbeta-counit-closed-form",
  title: "Agreement of $\\mathfrak{Q}_\\beta$ with the measured value at $N=0$",
  uses: ["prop:qbeta-counit-closed-form", "rem:energy-scale-planck"],
  tags: ["beta-decay", "q-value", "brane-tower", "residual", "interpretation"],
});
