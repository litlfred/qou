import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossing-energy-gap",
  title: "Crossing-energy gap positivity and $\\mu_2$-vanishing",
  lean: {
    ref: "qou:QOU.LiftingDescent.MassGap.crossingEnergyGap_pos",
    validation: "leanok",
  },
  uses: [
    "rem:aether-gm-torsion",
  ],
  tags: ["crossing-energy", "positivity", "gm-torsion", "symmetric-point"],
});
