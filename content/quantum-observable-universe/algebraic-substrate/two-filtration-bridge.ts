import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:two-filtration-bridge",
  title:
    "Two-filtration bridge: iterated-integral depth $\\leftrightarrow$ partition-cellular GB-depth via $e_\\lambda$",
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:curvature-rank-gb-stratification",
    "prop:quantum-dilogarithm-stratified",
    "prop:explicit-central-idempotent",
    "prop:hoefsmit-seminormal-form",
    "rem:chirality-period-pairing",
    "conj:bring-figure-eight-depth-2-witness",
    "conj:bring-trilog-depth-3-witness",
  ],
  cites: ["bloch2000"],
  tags: [
    "two-filtration-bridge",
    "iterated-integral-depth",
    "partition-cellular-depth",
    "central-idempotent",
    "graded-mikusinski",
    "open-problem",
  ],
});
