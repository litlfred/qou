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
});
