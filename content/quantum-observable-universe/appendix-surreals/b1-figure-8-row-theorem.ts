import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-figure-8-row-theorem",
  proofs: ["prf:b1-figure-8-row-theorem"],
  title:
    "B1 keystone is theorem-level at the figure-8 row (Bloch--Suslin + Murakami--Murakami)",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1Figure8RowTheorem.b1_figure_8_row",
    validation: "not_checked",
  },
  uses: ["prop:b1-soft-sharpness-theorem"],
  cites: ["murakami-murakami2001", "bloch2000", "suslin1991", "thurston1978"],
  tags: [
    "B1-discharge",
    "figure-8-knot",
    "volume-conjecture-discharged",
    "bloch-suslin",
    "murakami-murakami",
    "theorem-level",
    "graded-mikusinski",
  ],
});
