import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:implications-algebraic-independence",
  title:
    "Implications if the QOU volumes are algebraically independent",
  tags: [
    "transcendence",
    "algebraic-independence",
    "yekutieli",
    "milnor",
    "confinement",
  ],
  uses: [
    "rem:yekutieli-transcendence-shadow",
    "prop:cs-evaluation-faithfulness",
  ],
  cites: ["yekutieli2010"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean formalisation.**\nIndependence populates the class `QOU.Archimedean.HyperbolicVolumeIndependence`. Constructing an instance requires" },
  ],
});
