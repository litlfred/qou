import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:variational-equations",
  label: "rem:noether-theorem-callout",
  title:
    "Noether's theorem in the $q$-deformed setting: symmetries, conservation, and anomalies",
  tags: [
    "noether",
    "conservation",
    "symmetry",
    "q-deformed",
    "anomaly",
    "energy",
    "momentum",
    "angular-momentum",
    "reeb",
    "gauge",
  ],
  uses: [
    "prop:variational-equations",
    "def:q-energy",
    "def:categorical-q-reeb-flow",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([q-value transition](#def:Q-value-transition))" },
  ],
});
