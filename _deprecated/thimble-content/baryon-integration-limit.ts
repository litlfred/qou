import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:baryon-period-ratio",
  label: "rem:baryon-integration-limit",
  title:
    "The integration limit $(4-q)/(4q+3)$ and its golden ratio fixed points",
  tags: [
    "mobius-transformation",
    "golden-ratio",
    "integration-limit",
    "picard-lefschetz",
    "baryon",
    "color-tube",
    "binomial",
  ],
  uses: [
    "prop:mobius-golden-fixed-points",
    "rem:golden-ratio-degeneration",
  ],
});
