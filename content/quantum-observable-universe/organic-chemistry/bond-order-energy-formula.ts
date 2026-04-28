import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bond-order-energy-formula",
  title:
    "Linear bond-order energy formula $\\mathrm{BDE}(k) \\approx k\\,\\mathrm{BDE}_{1}$",
  tags: [
    "bond-order",
    "bond-dissociation-energy",
    "single-double-triple",
    "linearity",
    "first-order",
  ],
  lean: { ref: "qou:QOU.Organic.bondOrderEnergyFormula",
    validation: "not_checked",
  },
  uses: ["rem:organic-chain-taxonomy"],
  cites: [],
});
