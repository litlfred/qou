import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shadow-ordering-compute-shortcut",
  title: "Computational shortcut from local constancy",
  interprets: "def:local-shadow-ordering",
  uses: [
    "def:local-shadow-ordering",
    "def:unstable-atom",
    "prop:phase-boundary-variety",
    "prop:confinement-local-constancy",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): in the tower formula [mass-endomorphism-tower](#prop:mass-endomorphism-tower)" },
  ],
  tags: [
    "computational-shortcut",
    "local-constancy",
    "phase-boundary",
    "interpolation",
  ],
});
