import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:faddeev-phib-uniqueness",
  title:
    "Uniqueness of the modular-double $\\Phi_b$: strip growth pins the quantum dilogarithm up to scale",
  lean: {
    ref: "qou:QOU.QBeta.PhiBProdUniquenessMeromorphic.phiBProd_uniqueUpToScalar_of_meromorphic",
  },
  uses: [],
  cites: [
    "faddeev1995",
    "faddeev1994",
    "faddeev-kashaev-volkov2000",
  ],
  tags: [
    "faddeev",
    "quantum-dilogarithm",
    "modular-double",
    "qbeta",
    "rigidity",
    "uniqueness",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/QBeta/PhiBProdUniquenessMeromorphic.lean` uses " +
        "`Real.pi`, `Complex.*`. These are real-analytic constructs with " +
        "no generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Moved out of the published prose (one-voice sweep): the closing line " +
        "used to read \"The full brick-by-brick chain is recorded in the " +
        "keystone arc map.\" That pointer belongs here \u2014 the arc map is a " +
        "planning record, not part of the manuscript \u2014 and the prose now " +
        "ends on the mathematical hedge it already carried.",
    },
  ],
});
