import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jones-birthday",
  title:
    "Birthday refinement of the Jones polynomial",
  lean: { ref: "qou:QOU.AppendixSurreals.JonesBirthday", validation: "stub" },
  tags: [
    "surreal-numbers",
    "jones-polynomial",
    "birthday",
    "knot-invariant",
    "refinement",
    "open-problem",
  ],
  uses: ["prop:hoefsmit-is-surreal-construction"],
  cites: ["gonshor1986"],
});
