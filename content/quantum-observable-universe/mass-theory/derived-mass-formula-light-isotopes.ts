import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:derived-mass-formula-light-isotopes",
  proofs: ["prf:derived-mass-formula-light-isotopes"],
  title: "Derived-only mass formula reproduces light atomic masses to sub-percent",
  lean: {
    ref: "qou:QOU.WedderburnMass.derivedLightIsotopeFormula",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-s-classification",
  ],
});
