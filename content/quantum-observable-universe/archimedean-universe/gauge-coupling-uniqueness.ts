import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:gauge-coupling-uniqueness",
  title:
    "Uniqueness of the scalar gauge coupling on $A \\otimes A$",
  lean: {
    ref: "qou:QOU.Descartes.gauge_coupling_uniqueness",
    validation: "not_checked",
  },
  uses: ["thm:em-spectral-completeness"],
  tags: [
    "uniqueness",
    "gauge-coupling",
    "singlet",
    "central-idempotent",
    "no-other-alpha",
  ],
});
