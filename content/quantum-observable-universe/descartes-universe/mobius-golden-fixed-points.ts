import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mobius-golden-fixed-points",
  title:
    "Fixed points of the baryon integration-limit transformation are $1/\\varphi$ and $-\\varphi$",
  tags: [
    "mobius-transformation",
    "golden-ratio",
    "integration-limit",
    "color-tube",
    "binomial",
    "fixed-point",
  ],
  lean: { ref: "qou:QOU.Descartes.mobius_golden_fixed_points",
    validation: "not_checked",
  },
  uses: ["def:picard-lefschetz-thimble"],
});
