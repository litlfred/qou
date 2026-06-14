import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bring-embeddable-knots",
  title:
    "Bring-embeddable knots: genus-bounded table and per-knot B1 witness targets",
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
  ],
});
