import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borel-partial-resolution",
  title:
    "Borel's theorem partially discharges the keystone's sharpness target — explicit dimensions",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BorelPartialResolution.borel_partial",
    validation: "not_checked",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "rem:k-theory-period-rosetta",
    "rem:bring-embeddable-knots",
    "conj:bring-figure-eight-depth-2-witness",
    "conj:bring-trilog-depth-3-witness",
    "rem:transcendental-accounting",
  ],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "borel-theorem",
    "k-theory",
    "keystone-discharge",
    "bring-natural-fields",
    "beilinson-conjecture",
    "graded-mikusinski",
    "explicit-dimensions",
  ],
});
