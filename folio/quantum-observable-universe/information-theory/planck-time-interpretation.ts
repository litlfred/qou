import { remark } from "../../schema/builders";

export default remark({
  label: "rem:planck-time-interpretation",
  title: "Planck time: Reeb-circuit reading, regimes, field realisations, and the Planck length",
  interprets: "def:planck-time",
  tags: ["planck-time", "discrete-time", "reeb-flow", "planck-length", "information-theory"],
  uses: [
    "def:planck-time",
    "ex:q-reeb-flow",
    "rem:julia-set-reeb",
    "prop:local-substrate-q",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Julia set of Reeb flow](#rem:julia-set-reeb))" },
  ],
});
