import { remark } from "../../schema/builders";

/**
 * Mass comparison table Z = 1-20.
 */
export default remark({
  label: "rem:mass-table-z1-20",
  title: "Predicted vs observed masses, $Z = 1$--$20$",
  interprets: "thm:wedderburn-mass-formula",
  uses: ["rem:kashaev-volume-density"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): reproduced by\n[`wedderburn_mass_table_z1_20.py`](https://github.com/litlfred/qou/blob/main/computations/wedderburn_mass_table_z1_20.py)\nfrom the committed witness `wedderburn-mass-table-z1-20`, evaluating\n\ndeterminants and ratios they rest on are proved in Lean\n(`QOU.BraidKnot.detT_*`, `symAltRatio_*`, `chiralityCount_collapse`)." },
  ],
});
