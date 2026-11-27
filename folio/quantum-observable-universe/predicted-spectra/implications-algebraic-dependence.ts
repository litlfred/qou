import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:implications-algebraic-dependence",
  title:
    "Implications if the QOU volumes are algebraically dependent",
  tags: [
    "transcendence",
    "algebraic-dependence",
    "yekutieli",
    "tower-collapse",
    "falsification",
  ],
  uses: [
    "rem:yekutieli-transcendence-shadow",
    "rem:formal-chain-transcendence",
    "prop:cs-evaluation-faithfulness",
  ],
  cites: ["yekutieli2010"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean formalisation.**\nDependence implies the class `QOU.Archimedean.HyperbolicVolumeIndependence` is uninhabited. The conditional theorem `QOU.Archimedean.tower_noncollapse_implies_independence` remains vacuously true. Its hypothesis `QOU.Torsion.YekutieliLiftingCondition` is unsatisfiable." },
  ],
});
