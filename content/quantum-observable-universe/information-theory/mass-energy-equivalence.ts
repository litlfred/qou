import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:mass-energy-equivalence",
  proofs: ["prf:mass-energy-equivalence"],
  title: "Mass--energy equivalence ($E_{\\mathfrak{H}} = \\mathfrak{m}_{\\mathfrak{H}} \\cdot c_q^2$)",
  tags: [
    "mass-energy",
    "speed-of-light",
    "crossing-energy",
    "categorical-trace",
    "ribbon-category",
    "information-theory",
  ],
  lean: { ref: "qou:QOU.Information.massEnergyEquivalence",
    validation: "not_checked",
  },
  uses: ["def:information-speed-of-light"],
  cites: [
    "reshetikhin1991",
    "yekutieli2015",
  ],
});
