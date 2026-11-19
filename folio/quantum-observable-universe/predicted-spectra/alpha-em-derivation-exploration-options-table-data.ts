import { table } from "../../schema/builders";

export default table({
  label: "tbl:alpha-em-derivation-exploration-options-table-data",
  title:
    "Natural QOU sources for each ingredient of the $1/\\alpha_{EM}$ derivation",
  caption:
    "Per-ingredient map of where existing QOU infrastructure supplies the ingredients needed to close the $2/(3\\pi)$ derivation of $1/\\alpha_{EM}$: Hopf-fibration total space, exceptional-divisor base, three color tubes, Bring genus, spectral-sequence collapse, stratum prefactors, Wenzl-bridge $y_\\lambda$.",
  uses: ["rem:alpha-em-derivation-exploration-options"],
  tags: ["alpha-em", "derivation-map", "summary-table"],
});
