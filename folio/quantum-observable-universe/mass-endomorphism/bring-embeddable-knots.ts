import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bring-embeddable-knots",
  title:
    "Bring-embeddable knots: genus-bounded table and per-knot witness targets for the depth correspondence",
  interprets: "rem:knot-exhaustiveness",
  uses: [
    "rem:knot-exhaustiveness",
    "prop:explicit-central-idempotent",
  ],
  cites: ["thurston1978"],
  tags: [
    "bring-embeddable",
    "genus-bound",
    "torus-knot-generators",
    "principled-atlas",
    "falsifiability-targets",
    "graded-mikusinski",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Tabulation block.** Aggregates the existing knot atlas data\n(`../appendix-knot-periodic-table/recursive-atom-knot-atlas.md`)\nunder the graded-Mikusiński prediction. No new mathematical\ncontent; provides the *list of falsifiability targets* for B1.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): One verified the figure-$8$ row ([Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)](#conj:bring-figure-eight-depth-2-witness)), but confirming" },
  ],
});
