import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-spectral-sequence",
  title:
    "GB-filtration spectral sequence and $E_\\infty$ convergence of the 6-term mass",
  lean: {
    ref: "qou:QOU.BraidKnot.gb_spectral_sequence",
    validation: "not_checked",
  },
  uses: ["def:hecke-normal-form"],
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "gb-filtration",
    "e-infinity",
    "convergence",
  ],
});
