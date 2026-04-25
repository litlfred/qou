import { definition } from "../../schema/builders";

export default definition({
  label: "def:birthday-grading",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BirthdayGrading",
    validation: "not_checked",
  },
  title: "Birthday grading on a surreal-coefficient category",
  tags: [
    "surreal-numbers",
    "birthday",
    "ordinal",
    "grading",
    "filtration",
  ],
  uses: [
    "def:rigid-monoidal-category",
  ],
  cites: ["conway1976", "gonshor1986"],
});
