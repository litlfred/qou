import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chain-ring-comparison",
  title:
    "Predicted vs. observed $\\mathrm{C}_6$ ring-closure barrier",
  tags: [
    "comparison",
    "experimental",
    "theoretical",
    "activation-energy",
    "benzene",
    "carbyne",
    "ring-closure",
    "substrate-parameter",
  ],
  lean: { ref: "qou:QOU.Organic.benzene_weights",
    validation: "not_checked",
  },
  uses: ["rem:chain-ring-energy"],
});
