import { remark } from "../../schema/builders";

export default remark({
  label: "rem:strong-multiplicativity-poisson-lie",
  title: "Strong multiplicativity, primitives and Poisson–Lie groups",
  interprets: "def:strong-multiplicativity",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Hand check of Remark 1.12.2 of arXiv:math/0602138 requested by the author. Claims 1 and 2 of that remark are confirmed. An earlier draft of this remark claimed the converse (necessity) by reading the proof of Prop. 1.13 backwards. That argument works in $T \\otimes T$ and does not handle the ideal, so the claim is withdrawn (QA on #8888); the remark now cites Remark 1.12.2 for the heuristic and states that the converse is not proved. Two typos in the source: 1.12.1 ends with \"eta\" for $\\eta$, and the proof of 1.13 writes $x'_t$ for $x'_r$." },
  ],
  tags: ["strong-multiplicativity", "poisson-lie", "comultiplication"],
  uses: ["def:strong-multiplicativity", "def:skewed-poisson-structure"],
  cites: ["leitner2006", "luweinstein1990"],
});
