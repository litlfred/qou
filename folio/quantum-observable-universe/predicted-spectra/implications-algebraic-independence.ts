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
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean formalisation: algebraic independence populates the class `QOU.Archimedean.HyperbolicVolumeIndependence`.",
    },
  ],
});
