import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:deuteron-binding-frobenius-codim",
  title: "Deuteron binding from atomic Frobenius co-Casimir trace",
  lean: {
    ref: "qou:QOU.WedderburnMass.deuteronBindingFrobeniusCodim",
    validation: "not_checked",
  },
  uses: ["rem:deuteron-first-principles"],
});
