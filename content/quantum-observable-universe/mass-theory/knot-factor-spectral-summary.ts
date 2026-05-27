import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-factor-spectral-summary",
  title:
    "Spectral derivation of the empirical $a_K$ pattern across nuclei",
  interprets: "prop:knot-factor-spectral-form",
  uses: [
    "cor:knot-factor-borromean-composite",
    "cor:knot-factor-shell-closed",
  ],
  tags: [
    "interpretation",
    "knot-factor",
    "summary-table",
    "no-fitting",
  ],
});
