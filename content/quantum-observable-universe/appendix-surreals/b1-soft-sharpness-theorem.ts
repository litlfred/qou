import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-soft-sharpness-theorem",
  title:
    "Soft sharpness of the keystone B1 is theorem-level — via Borel + polylog non-vanishing",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1SoftSharpnessTheorem.b1_soft_sharpness",
    validation: "not_checked",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:borel-partial-resolution",
    "prop:depth-2-identification-bloch-suslin",
    "rem:k-theory-period-rosetta",
    "rem:transcendental-accounting",
  ],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "soft-sharpness",
    "borel-theorem",
    "polylog-non-vanishing",
    "lewin-theorem",
    "keystone-discharge",
    "graded-mikusinski",
    "theorem-level",
  ],
});
