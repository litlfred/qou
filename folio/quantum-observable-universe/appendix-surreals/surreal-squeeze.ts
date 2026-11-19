import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:surreal-squeeze",
  title:
    "Surreal squeeze: standard-scale cost dominates infinitesimal dissipation",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.surreal_squeeze",
    validation: "not_checked",
  },
  uses: [],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
