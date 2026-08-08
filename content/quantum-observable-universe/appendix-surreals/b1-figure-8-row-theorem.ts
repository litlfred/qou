import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-figure-8-row-theorem",
  title:
    "The depth correspondence is theorem-level at the figure-8 row (Bloch--Suslin + Murakami--Murakami)",
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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`B1Figure8RowContext.bloch_wigner_4_1` is the Bloch–Wigner " +
        "dilogarithm value `Im D_2(e^{iπ/3})` at the figure-8 shape " +
        "parameter — the Faddeev volume of `4_1`. That is transcendental, " +
        "so `ℝ` is forced; the companion `depth_4_1` is a plain `ℕ` " +
        "filtration index and carries no archimedean content.",
    },
  ],
});
