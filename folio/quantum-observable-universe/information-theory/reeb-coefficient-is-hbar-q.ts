import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-coefficient-is-hbar-q",
  title:
    "The Reeb coefficient of $D_\\nabla$ is the quantum Planck constant: $1 - q^{-1} = (q-1)/q$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.reeb_coefficient_eq_hbar_q",
    validation: "not_checked",
  },
  // def:quantum-planck-constant is deliberately NOT listed: def:planck-time
  // already uses[] it, so naming both is transitively redundant on the
  // editorial relation (reading order is transitive).
  uses: ["def:planck-time"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): That reading is made\nexplicit in [share versus total](#rem:planck-length-share-vs-total); the finite-$q$\nconsequence for the induced metric is\n[the Reeb-step-count qualification](#rem:connes-distance-not-reeb-step-count)." },
  ],
  tags: [
    "reeb-flow",
    "dirac-operator",
    "hbar-q",
    "information-theory",
  ],
});
