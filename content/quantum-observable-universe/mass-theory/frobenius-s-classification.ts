import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-s-classification",
  title: "Frobenius S-eigenvalue classification of the 3-term mass formula",
  lean: {
    ref: "qou:QOU.WedderburnMass.frobenius_s_classification",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula", "prop:confined-knot-binding"],
});
