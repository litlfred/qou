import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's single `ℝ` is the field " +
        "`borel_regulator : ℝ` of `B1SoftSharpnessContext`. Borel's regulator " +
        "is a transcendental period — it is a real number by construction, not " +
        "an element of the substrate ring — so `ℝ` is the correct base ring " +
        "here and is not a gratuitous specialisation. The depth inequality " +
        "`depth_Mikusinski ≤ depth_Goncharov` is the archimedean realisation of " +
        "the statement; no generic-ring form of the regulator exists to " +
        "generalise it to.",
    },
  ],
  label: "prop:b1-soft-sharpness-theorem",
  title:
    "Soft sharpness of the depth correspondence is theorem-level — via Borel + polylog non-vanishing",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1SoftSharpnessTheorem.b1_soft_sharpness",
    validation: "not_checked",
  },
  uses: ["prop:depth-2-identification-bloch-suslin"],
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
