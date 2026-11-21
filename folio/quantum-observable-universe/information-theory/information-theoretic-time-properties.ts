import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-theoretic-time-properties",
  interprets: "def:information-theoretic-time",
  title: "Reeb time coordinate, three regimes, and the arrow of time",
  tags: [
    "information-theory",
    "planck-time",
    "discrete-time",
    "statistical-mechanics",
    "reeb-flow",
    "julia-set",
  ],
  uses: [
    "def:information-theoretic-time",
    "prop:reeb-operations-per-planck",
    "prop:local-substrate-q",
    "def:planck-time",
    "ex:q-reeb-flow",
    "rem:information-theoretic-time-julia-microscopic",
    "rem:information-theoretic-time-arrow",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): One treats its microscopic Julia-set dynamics ([Julia-set iteration as the microscopic theory](#rem:information-theoretic-time-julia-microscopic)) and its arrow of time ([arrow of time from the braiding order](#rem:information-theoretic-time-arrow)) separately." },
  ],
  foreshadows: [
    "rem:information-theoretic-time-julia-microscopic",
    "rem:information-theoretic-time-arrow",
  ],
});
